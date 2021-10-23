import { useEffect, useState } from "react";
import { Switch, BrowserRouter } from "react-router-dom";

import { Spin } from "antd";
import { isEmpty } from "./_dash";
import { getAuthUserDetail } from "./actions";

import { NON_LOGIN_ROUTES, LOGGED_IN_ROUTES } from "./routes";

import AccountHook from "./hooks/account";
import RouteWithSubRoutes from "./components/routeWithSubRoutes";

const App = ({ accountData, setAccountData }) => {
  const isLoggedIn = !isEmpty(accountData);

  const [loading, setLoading] = useState(true);
  const [appRoutes, setAppRoutes] = useState(NON_LOGIN_ROUTES);

  useEffect(() => {
    getAuthUserDetail()
      .then((response) => {
        setAccountData(response);
        setLoading(false);
      })
      .catch((err) => {
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    if (!loading) {
      if (isLoggedIn) {
        setAppRoutes(LOGGED_IN_ROUTES);
      } else {
        setAppRoutes(NON_LOGIN_ROUTES);
      }
    }
  }, [isLoggedIn, loading]);

  if (loading) {
    return <Spin />;
  }

  return (
    <BrowserRouter>
      <Switch>
        {appRoutes.map((route, i) => {
          return <RouteWithSubRoutes key={i} {...route} />;
        })}
      </Switch>
    </BrowserRouter>
  );
};

export default AccountHook(App);
