import { useEffect, useState } from "react";
import { Modal, Form, Input, Select, message } from "antd";
import { assignMysqlQuery } from "../../../actions";

const AddMySQLQueryAssignmentModal = ({ isModalVisible, listAllMysqlQueries, setIsModalVisible, serverId, mySqlQueries }) => {

  const [form] = Form.useForm();
  const [mysqlAssignmentAdding, setMysqlAssignmentAdding] = useState(false);

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  const onSubmit = (values) => {
    setMysqlAssignmentAdding(true);
    values["server_id"] = serverId;
    values["mysql_password"] = values["mysql_password"] === undefined ? "" : values["mysql_password"];
    assignMysqlQuery(values)
      .then((response) => {
        setMysqlAssignmentAdding(false);
        setIsModalVisible(false);
        listAllMysqlQueries();
        form.resetFields();
        console.log(response);
      })
      .catch((err) => {
        setMysqlAssignmentAdding(false);
        message.error(err.response.data.detail.error);
      });
  }

  useEffect(() => {
    if (isModalVisible) {
      setIsModalVisible(true);
      form.setFieldsValue({
        mysql_port: "3306"
     });
    }
  }, [isModalVisible]);

  return (
    <Modal
      title="Add MySQL Query Assignment For This Server"
      okText="Add"
      cancelText="Close"
      visible={isModalVisible}
      onOk={() => form.submit()}
      onCancel={() => handleCancel()}
      confirmLoading={mysqlAssignmentAdding}
    >
      <Form
        form={form}
        onFinish={(values) => onSubmit(values)}
      >
        <Form.Item
          name="mysql_query_id"
          rules={[
            {
              required: true,
              message: "Please select the MySQL Query to Assign to this Server!",
            },
          ]}
        >
          <Select
            mode="single"
            allowClear
            style={{ width: '100%' }}
            placeholder="Select the MySQL Query to Assign to this Server"
          >
            {mySqlQueries.map((item) => {
              return (
                <Select.Option value={item.id} key={item.id}>
                  {item.name }
                </Select.Option>
              );
            })}
          </Select>
        </Form.Item>
        <Form.Item
          name="name"
          rules={[
            {
              required: true,
              message: "Please input descriptive assignment name!",
            },
          ]}
        >
          <Input
            size="middle"
            placeholder="Assignment name"
          />
        </Form.Item>
        <Form.Item
          name="notes"
          rules={[
            {
              message: "Please input descriptive assignment notes!",
            },
          ]}
        >
          <Input.TextArea
            size="middle"
            placeholder="Assignment notes"

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
        >
          <Input.Password
            size="middle"
            autoComplete="new-password"
            placeholder="Enter MySQL Password for query execution (Default is empty string: '')"
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
        >
          <Input
            size="middle"
            placeholder="Enter MySQL Port for query execution"
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

export default AddMySQLQueryAssignmentModal;
