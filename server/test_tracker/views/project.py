"""Everything related to the project."""
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from server.test_tracker.api.response import CustomResponse
from server.test_tracker.api.permission import HasProjectAccess, UserIsAuthenticated
from server.test_tracker.models.dashboard import Member, Project
from server.test_tracker.serializers.dashboard import ProjectsSerializer
from server.test_tracker.serializers.member import ProjectTeamSerializer
from server.test_tracker.utils.validations import Validator

from server.test_tracker.services.dashboard import is_success_project, get_project_by_id
from server.test_tracker.services.member import get_member_by_id
from server.test_tracker.services.project import (
    project_member_validation,
    update_activity,
)

import datetime


class ProjectsDetailAPIView(GenericAPIView):
    """
    Class ProjectsAPIView have all the functionality based on the project
    Methods [GET, PUT, DELETE]
    """

    serializer_class = ProjectsSerializer
    permission_classes = (HasProjectAccess,)

    def get(self, request: Request, project_id: str) -> Response:
        """Return a single project based on the given project id"""
        project = get_project_by_id(project_id)
        serializer = ProjectsSerializer(project, context={"request": request})
        if project is not None:
            return CustomResponse.success(
                data=serializer.data,
                message="Project found successfully",
            )
        return CustomResponse.not_found(
            message="Project not found",
        )

    def put(self, request: Request, project_id: int) -> Response:
        """Put some data into the project"""
        project = get_project_by_id(project_id)
        if project is None:
            return CustomResponse.not_found(message="Project not found")

        serializer = self.get_serializer(project, data=request.data)
        if not serializer.is_valid():
            return CustomResponse.bad_request(
                error=serializer.errors,
                message="Project update failed",
            )

        project_title: str = serializer.validated_data.get("title")
        validate_name: str = Validator().validate_string(project_title)
        if not validate_name:
            return CustomResponse.bad_request(
                message=f"Name '{project_title}' is not a valid name, Please choose a valid project name.",
            )

        project = is_success_project(request.user, project, project_title)
        if not project:
            return CustomResponse.bad_request(
                message="Please choose a project name that does not exist in your projects.",
                status_code=400,
            )
        project = serializer.save(user=request.user)
        update_activity(
            datetime.datetime.now(),
            request.user,
            project,
            "Create",
            "Project",
            project.title,
        )
        return CustomResponse.success(
            data=serializer.data,
            message="Project updated successfully",
            status_code=201,
        )

    def delete(self, request: Request, project_id: int) -> Response:
        project = get_project_by_id(project_id)
        if project is not None and project.user == request.user:
            update_activity(
                datetime.datetime.now(),
                request.user,
                project,
                "Delete",
                "Project",
                project.title,
            )
            project.delete()
            return CustomResponse.success(status_code=204)
        return CustomResponse.not_found(
            message="Project not found",
        )


class ProjectActivityAPIView(GenericAPIView):
    """Get all project activity"""

    permission_classes = (UserIsAuthenticated,)

    def get(self, request: Request, project_id: str) -> Response:
        project = get_project_by_id(project_id)
        if project is None:
            return CustomResponse.not_found(message="Project not found")
        result = []
        if len(project.activity) > 0:
            for items, values in project.activity.items():
                result.append(
                    {"date": values.get("date"), "action": values.get("action")}
                )

        return CustomResponse.success(message="Success plans found.", data=result[::-1])


class AddMemberToProjectAPIView(GenericAPIView):
    """
    * Usage
    Add Member to project
    """

    permission_classes = (HasProjectAccess,)

    def put(self, request: Request, project_id: Project, member_id: Member) -> Response:
        """
        Add Member to project
        You must be authenticated to access this view
        """
        project = get_project_by_id(project_id)
        member = get_member_by_id(member_id)
        user = request.user
        if project_member_validation(project, member, user) is not True:
            return project_member_validation(project, member, user)
        update_activity(
            datetime.datetime.now(),
            request.user,
            project,
            f"added {member.first_name.title()} to",
            "Project",
            project.title,
        )
        project.members.add(member)
        return CustomResponse.success(
            message="Member added to project successfully",
            status_code=201,
            data=ProjectTeamSerializer(project.members.all(), many=True).data,
        )

    def delete(
        self, request: Request, project_id: Project, member_id: Member
    ) -> Response:
        """
        Add Member to project
        You must be authenticated to access this view
        """
        project = get_project_by_id(project_id)
        member = get_member_by_id(member_id)
        user = request.user

        if project_member_validation(project, member, user, remove=True) is not True:
            return project_member_validation(project, member, user)
        update_activity(
            datetime.datetime.now(),
            request.user,
            project,
            f"removed {member.first_name.title()} from",
            "Project",
            project.title,
        )
        project.members.remove(member)
        return CustomResponse.success(status_code=204)


class GetLast5ProjectsUpdatedAPIView(GenericAPIView):
    """
    * Usage
    Class to get last 5 Updated
    """

    serializer_class = ProjectsSerializer
    permission_classes = (UserIsAuthenticated,)

    def get(self, request: Request) -> Response:
        """
        Get last 5 projects updated based on user
        You must be authenticated to access this view
        """
        member = get_member_by_id(str(request.user.id))

        if member is not None:
            # Thats mean the request from a member
            user = member.host_user
            projects = Project.objects.filter(
                members__in=[request.user.id], user=user
            ).order_by("-modified")
        else:
            projects = Project.objects.filter(user=request.user).order_by("-modified")
        projects = projects[:5]

        return CustomResponse.success(
            message="Success projects found.",
            data=ProjectsSerializer(projects, many=True).data,
        )


class GetActivityOfLast5ProjectsAPIView(GenericAPIView):
    """
    * Usage
    This class to concatenate the activity of the last 5 projects updated.
    """

    permission_classes = (UserIsAuthenticated,)

    def get(self, request: Request) -> Response:
        """A get method that returns last update from last 5 projects activity"""
        member = get_member_by_id(str(request.user.id))
        if member:
            projects = Project.objects.filter(
                members__in=[member.id], user=member.host_user
            ).order_by("-modified")
        else:
            projects = Project.objects.filter(user=request.user).order_by("-modified")
        projects = projects[:5]
        result = []

        for project in projects:
            if len(project.activity) > 0:
                activity = list(project.activity.values())[::-1][0]
                activity["project_title"] = project.title
                result.append(activity)

        return CustomResponse.success(message="Success activity found.", data=result)


class SearchProjectAPIView(GenericAPIView):
    """
    * Usage
    This class to filter all op projects based on project name.
    """

    serializer_class = ProjectsSerializer
    permission_classes = (UserIsAuthenticated,)

    def get(self, request: Request, project_name: str):
        """
        Get all projects based on project name
        You must be authenticated to access this view
        """
        user = request.user
        member = get_member_by_id(request.user.id)
        if member:
            user = member.host_user
            projects = Project.objects.filter(
                title__icontains=project_name, user=user, members__in=[member.id]
            )
        else:
            projects = Project.objects.filter(title__icontains=project_name, user=user)
        return CustomResponse.success(
            message="Success projects found.",
            data=ProjectsSerializer(projects, many=True).data,
        )


class AccountMembersNotInProjectAPIView(GenericAPIView):
    """
    * Usage
    Class to get all account members where members not in project
    """

    permission_classes = (HasProjectAccess,)
    serializer_class = ProjectTeamSerializer

    def get(self, request: Request, project_id: str):
        """Get all members of user account where members not in project"""
        project = get_project_by_id(project_id)
        if not project:
            return CustomResponse.not_found(message="Project not found")
        user = request.user
        if project.user == user:
            account_members = Member.objects.filter(host_user=user).values_list(
                "id", flat=True
            )
            project_members = Member.objects.filter(
                id__in=project.members.values_list("id", flat=True)
            )
            not_in_project = Member.objects.exclude(
                id__in=project_members.values_list("id", flat=True)
            )
            not_in_project = not_in_project.filter(id__in=account_members)
            return CustomResponse.success(
                data=ProjectTeamSerializer(not_in_project, many=True).data,
                message="Successfully Added",
            )
        return CustomResponse.unauthorized(
            message="You are not authorized to access this view"
        )
