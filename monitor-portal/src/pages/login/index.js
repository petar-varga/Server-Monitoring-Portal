import { useState } from "react";
import { LockOutlined, UserOutlined } from "@ant-design/icons";
import { Form, Input, Button, Checkbox, Card, message } from "antd";

import { loginUser } from "../../actions";
import { AUTHORIZATION_KEY } from "../../global_constants";

import AccountHook from "../../hooks/account";

const Login = ({ setAccountData }) => {
  const [form] = Form.useForm();
  const [processing, setProcessing] = useState(false);

  function onSubmit(values) {
    setProcessing(true);
    loginUser(values)
      .then((response) => {
        setProcessing(false);
        setAccountData(response);
        localStorage.setItem(AUTHORIZATION_KEY, response.token);
      })
      .catch((err) => {
        setProcessing(false);
        message.error(err.response.data.detail.error);
      });
  }

  return (
    <div className="login-page">
      <Card bordered>
        <p className="text-2xl semi-bold mb-16">Monitoring Portal</p>
        <Form form={form} onFinish={(values) => onSubmit(values)}>
          <Form.Item
            name="email"
            rules={[
              {
                type: "email",
                message: "The input is not valid E-mail!",
              },
              {
                required: true,
                message: "Please input your email!",
              },
            ]}
          >
            <Input
              size="middle"
              prefix={<UserOutlined />}
              placeholder="Email"
            />
          </Form.Item>
          <Form.Item
            name="password"
            rules={[
              {
                required: true,
                message: "Please input your Password!",
              },
              {
                min: 5,
                message: "The Password must be at least 5 characters long",
              },
            ]}
          >
            <Input.Password
              size="middle"
              prefix={<LockOutlined />}
              placeholder="Password"
            />
          </Form.Item>
          <Form.Item name="remember" valuePropName="checked">
            <Checkbox>Remember me</Checkbox>
          </Form.Item>
          <Form.Item noStyle>
            <Button
              block
              type="primary"
              className="mt-8"
              htmlType="submit"
              loading={processing}
            >
              Log in
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </div>
  );
};
export default AccountHook(Login);