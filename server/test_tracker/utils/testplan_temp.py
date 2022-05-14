from pyini_parser.configure.parser import ConfigParser

from server.components import BASE_DIR

class TestPlanTemp():
    """
    This class only to set something like plan temps to user
    """

    @staticmethod
    def create_temps():
        config = ConfigParser()
        with open(f'{BASE_DIR}/server/temps.ini', 'r') as file:
            return config.read(file)