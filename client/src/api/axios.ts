import axios, { AxiosInstance } from 'axios';

const AuthClient: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_APP_ENDPOINT, 
  timeout: 1000,
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + localStorage.getItem("token"),
  },
});

const BaseClient: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_APP_ENDPOINT,
  timeout: 1000,
});

async function Search(searchInput:any) {
  await AuthClient.get(`/members/search/${searchInput}`)
  .then(response=>{
    return response.data;
  })
  .catch(error=>{
    console.error(error);
  })
}

export default{ AuthClient, BaseClient, Search };
