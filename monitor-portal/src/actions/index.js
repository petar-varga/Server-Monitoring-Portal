import instance from "../axios";
import * as endpoints from "./endpoints";
import { AUTHORIZATION_KEY } from "../global_constants";

export const loginUser = (payload) => {
  delete instance.defaults.headers.common["Authorization"];
  return new Promise((resolve, reject) => {
    instance
      .post(endpoints.LOGIN_API_PATH, payload)
      .then((response) => {
        const { data } = response;
        instance.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${data.access_token}`;
        resolve(data);
      })
      .catch((err) => {
        reject(err);
      });
  });
};

export const getAuthUserDetail = () => {
  return new Promise((resolve, reject) => {
    const token = localStorage.getItem(AUTHORIZATION_KEY);
    if (token) {
      instance.defaults.headers.common["Authorization"] = `Bearer ${token}`;
      instance
        .get(endpoints.AUTH_USER_API_PATH)
        .then((response) => {
          resolve(response.data);
        })
        .catch((err) => {
          reject(err);
        });
    } else {
      reject();
    }
  });
};

export const getUsers = (queryString) => {
  let path = endpoints.USERS_API_PATH;
  path = path.concat("?", queryString || "");
  return instance.get(path);
};

export const createUser = (payload) => {
  return instance.post(endpoints.USERS_API_PATH, payload);
};

export const updateUser = (payload, userId) => {
  return instance.patch(
    endpoints.USERS_DETAIL_API_PATH.replace("{}", userId),
    payload
  );
};

export const getInstances = (queryString) => {
  let path = endpoints.ALL_SERVERS_API_PATH;
  return instance.get(path);
};

export const addServer = (payload) => {
  let path = endpoints.ADD_SERVER_API_PATH;
  return instance.post(path, payload);
};