import { useEffect, useState } from "react";
import { Table, Modal, Button, Form, Input, message } from "antd";

import { getInstances, addServer } from "../../../actions";

const AddServerModal = ({ isModalVisible, getList, setIsModalVisible }) => {
  
  const [form] = Form.useForm();
  const [serverAdding, setServerAdding] = useState(false);

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  function onSubmit(values) {
    setServerAdding(true);
    addServer(values)
      .then((response) => {
        setServerAdding(false);
        setIsModalVisible(false);
        getList();
        form.resetFields();
        console.log(response);
      })
      .catch((err) => {
        setServerAdding(false);
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
        title="Add server instance"
        okText="Add"
        cancelText="Close"
        visible={isModalVisible}
        onOk={() => form.submit()}
        onCancel={() => handleCancel()}
        confirmLoading={serverAdding}
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
                message: "Please input server name!",
              },
            ]}
          >
            <Input
              size="middle"
              placeholder="Server Name"
            />
          </Form.Item>
          <Form.Item
            name="ip"
            rules={[
              {
                required: true,
                message: "Please input server IP!",
              },
            ]}
          >
            <Input
              size="middle"
              placeholder="Server IP"
            />
          </Form.Item>
        </Form>
      </Modal>
  );
};

export default AddServerModal;
