import { useEffect, useState } from "react";
import { useHistory, useLocation, matchPath } from "react-router-dom";
import { Avatar, Col, Row, Space, Menu, Dropdown, Layout } from "antd";
import {
  LogoutOutlined,
  MenuFoldOutlined,
  MenuUnfoldOutlined,
} from "@ant-design/icons";

import { AUTHORIZATION_KEY } from "../../global_constants";
import { INDEX_ROUTE, SIDEBAR_ITEMS } from "../../routes";

import AccountHook from "../../hooks/account";
import RenderRoutes from "../../components/renderRoutes";

const { Header, Content, Sider } = Layout;

const DashboardLayout = ({ routes, accountData, setAccountData }) => {
  const history = useHistory();
  const { pathname } = useLocation();

  const [collapsed, setCollapsed] = useState(false);
  const [selectedMenu, setSelectedMenu] = useState({});

  useEffect(() => {
    SIDEBAR_ITEMS.forEach((item) => {
      const matchedPath = matchPath(pathname, {
        path: item.route,
        exact: true,
      });
      if (matchedPath) {
        if (selectedMenu.name !== item.name) {
          setSelectedMenu(item);
        }
      }
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [pathname]);

  function logout() {
    setAccountData({});
    history.push(INDEX_ROUTE);
    localStorage.removeItem(AUTHORIZATION_KEY);
  }

  return (
    <Layout className="app-layout">
      <Sider trigger={null} collapsible collapsed={collapsed} width={225}>
        <div className="logo" />
        <Menu theme="dark" mode="inline" selectedKeys={[selectedMenu.name]}>
          {SIDEBAR_ITEMS.map((item) => {
            return (
              <Menu.Item
                key={item.name}
                icon={item.icon}
                onClick={() => history.push(item.route)}
              >
                {item.label}
              </Menu.Item>
            );
          })}
        </Menu>
      </Sider>
      <Layout>
        <Header>
          <Row justify="space-between" align="middle">
            <Col>
              <Choose>
                <When condition={collapsed}>
                  <MenuUnfoldOutlined
                    onClick={() => setCollapsed(!collapsed)}
                  />
                </When>
                <Otherwise>
                  <MenuFoldOutlined onClick={() => setCollapsed(!collapsed)} />
                </Otherwise>
              </Choose>
            </Col>
            <Col>
              <Dropdown
                arrow
                trigger={["click"]}
                overlay={
                  <Menu>
                    <Menu.Item key="logout" onClick={() => logout()}>
                      <Space>
                        <LogoutOutlined />
                        <p className="text-xl">Logout</p>
                      </Space>
                    </Menu.Item>
                  </Menu>
                }
              >
                <Space className="header-menu">
                  <Avatar>{accountData.initials}</Avatar>
                  <p className="text-xl">{accountData.full_name}</p>
                </Space>
              </Dropdown>
            </Col>
          </Row>
        </Header>
        <Content>
          <div className="feature-container">
            <RenderRoutes routes={routes} />
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

export default AccountHook(DashboardLayout);
