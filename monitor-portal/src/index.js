import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

import {
  accountDataReducer,
  initialState as accountData,
} from "./reducers/accountDataReducer";
import { AccountDataProvider } from "./context/accountData";

import "./styles/style.scss";

ReactDOM.render(
  <AccountDataProvider 
    initialState={accountData} 
    reducer={accountDataReducer}
  >
    <App />
  </AccountDataProvider>,
  document.getElementById("root")
);