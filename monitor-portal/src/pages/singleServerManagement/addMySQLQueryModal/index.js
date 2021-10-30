import { useEffect, useState } from "react";
import { Modal, Form, Input, message } from "antd";
import { addMysqlQuery } from "../../../actions";

const AddMySQLQueryModal = ({ isModalVisible, listAllMysqlQueries, setIsModalVisible }) => {

  const [form] = Form.useForm();
  const [mysqlAdding, setMysqlAdding] = useState(false);

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  const onSubmit = (values) => {
    setMysqlAdding(true);
    addMysqlQuery(values)
      .then((response) => {
        setMysqlAdding(false);
        setIsModalVisible(false);
        listAllMysqlQueries();
        form.resetFields();
        console.log(response);
      })
      .catch((err) => {
        setMysqlAdding(false);
        message.error(err.response.data.detail.error);
      });
  }

  useEffect(() => {
    if (isModalVisible) {
      setIsModalVisible(true);
    }
  }, [isModalVisible]);

  return (
    <Modal
      title="Add MySQL Query"
      okText="Add"
      cancelText="Close"
      visible={isModalVisible}
      onOk={() => form.submit()}
      onCancel={() => handleCancel()}
      confirmLoading={mysqlAdding}
    >
      <Form
        form={form}
        onFinish={(values) => onSubmit(values)}
      >
        <Form.Item
          name="name"
          rules={[
            {
              required: true,
              message: "Please input descriptive MySQL name!",
            },
          ]}
        >
          <Input
            size="middle"
            placeholder="MySQL query name"
          />
        </Form.Item>
        <Form.Item
          name="sql_query"
          rules={[
            {
              required: true,
              message: "Please input MySQL Query!",
            },
          ]}
        >
          <Input.TextArea
            size="middle"
            placeholder="Enter MySQL Query to execute"
          />
        </Form.Item>
        <Form.Item
          name="mysql_username"
          rules={[
            {
              required: true,
              message: "Please input MySQL Username!",
            },
          ]}
        >
          <Input
            size="middle"
            placeholder="Enter MySQL Username for query execution"
          />
        </Form.Item>
        <Form.Item
          name="mysql_password"
          rules={[
            {
              required: true,
              message: "Please input MySQL Password!",
            },
          ]}
        >
          <Input.Password
            size="middle"
            placeholder="Enter MySQL Password for query execution"
          />
        </Form.Item>
        <Form.Item
          name="mysql_host"
          rules={[
            {
              required: true,
              message: "Please input MySQL Host!",
            },
          ]}
        >
          <Input
            size="middle"
            placeholder="Enter MySQL Host for query execution"
          />
        </Form.Item>
        <Form.Item
          name="mysql_port"
          rules={[
            {
              required: true,
              message: "Please input MySQL Port!",
            },
          ]}
        >
          <Input
            size="middle"
            placeholder="Enter MySQL Port for query execution"
            value={"3306"}
          />
        </Form.Item>
        <Form.Item
          name="mysql_database"
          rules={[
            {
              required: true,
              message: "Please input MySQL Database name!",
            },
          ]}
        >
          <Input
            size="middle"
            placeholder="Enter MySQL Database name for query execution"
          />
        </Form.Item>
      </Form>
    </Modal>
  );
};

export default AddMySQLQueryModal;
