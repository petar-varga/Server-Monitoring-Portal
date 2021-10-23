import axios from "axios";

let headers = {
  "Content-Type": "application/json",
};

const axiosInstance = axios.create({
  headers,
  timeout: 16000,
  baseURL: `${process.env.REACT_APP_API_HOST}/api/v1/`,
});

export default axiosInstance;
