import { useEffect, useState } from "react";
import { Link, useHistory } from "react-router-dom";
import { Table, Modal, Button, Form, Input, Card, Space, message } from "antd";

import { getInstances, addServer } from "../../actions";
import AddServerModal from "./addServerModal"

const ServerManagementPage = () => {
  const [instances, setInstances] = useState([]);
  const [loading, setLoading] = useState(false);

  const [isAddServerModalVisible, setIsAddServerModalVisible] = useState(false);

  const columns = [
    {
      title: 'Server',
      dataIndex: 'server_info',
      key: 'server_info',
      render: serverInfo =>
        <>
          <p style={{
            display: "block",
            fontWeight: "bold",
          }}>{serverInfo.name}</p>
          <p>{serverInfo.ip}</p>
        </>
    },
    {
      title: 'OS',
      dataIndex: 'operating_system',
      key: 'operating_system',
    },
    {
      title: 'Status',
      dataIndex: 'status',
      key: 'status',
    },
    {
      key: "action",
      title: "Action",
      render: (record) => (
        <Link to={"server/" + record.id}> Manage </Link>
      )
    },
  ];

  const showModal = () => {
    setIsAddServerModalVisible(true);
  };

  function getList(page = 1) {
    setLoading(true);
    const params = "";
    getInstances(params).then((response) => {
      const { data } = response;
      setLoading(false);
      setInstances(data.map(
        (instance) => {
          instance.server_info = {
            name: instance.name,
            ip: instance.ip
          }
          instance.key = instance.id
          return instance;
        }
      ));
    });
  }

  useEffect(() => {
    getList();
  }, []);

  return (
    <div className="not-found-page">
      <Card
        className="no-padding"
        title={
          <p className="text-5xl font-bold secondary-font secondary mb-4">
            SERVER MANAGEMENT
          </p>
        }
        extra={
          <Space>
            <Button type="primary" onClick={showModal}>Add Server</Button>
          </Space>
        }
      >
        <Table
          dataSource={instances}
          columns={columns}
          loading={loading}
        />
      </Card>

      <AddServerModal
        isModalVisible={isAddServerModalVisible}
        getList={getList}
        setIsModalVisible={setIsAddServerModalVisible}
      />
    </div>
  );
};

export default ServerManagementPage;
