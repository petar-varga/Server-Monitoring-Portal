import React from "react";
import {
  UserOutlined,
  MoneyCollectOutlined,
  DeploymentUnitOutlined,
} from "@ant-design/icons";

import NotFoundPage from "./pages/404Page";

import Login from "./pages/login";
import ServerManagement from "./pages/serverManagement";

const ServerManagementComponent = React.lazy(() =>
  import("./pages/serverManagement")
);

export const INDEX_ROUTE = "/";
export const SERVERS_ROUTE = "/";

// ROUTES
export const NON_LOGIN_ROUTES = [
  {
    exact: true,
    name: "login",
    path: INDEX_ROUTE,
    component: Login,
  },
  {
    component: NotFoundPage,
  },
];

export const LOGGED_IN_ROUTES = [
  {
    name: "layout",
    path: INDEX_ROUTE,
    component: ServerManagement,
    routes: [
      {
        exact: true,
        name: "servers-management",
        path: SERVERS_ROUTE,
        component: ServerManagementComponent,
      }
    ],
  },
  {
    component: NotFoundPage,
  },
];

export const SIDEBAR_ITEMS = [
  {
    name: "home",
    label: "Home",
    route: INDEX_ROUTE,
    icon: <UserOutlined />,
  },
  {
    name: "servers-management",
    label: "Servers management",
    route: SERVERS_ROUTE,
    icon: <DeploymentUnitOutlined />,
  }
];
