import { useEffect, useState } from "react";
import { Table } from "antd";

import { getInstances } from "../../actions";

const ServerManagementPage = () => {
  const [instances, setInstances] = useState([]);
  const [loading, setLoading] = useState(false);

  function getList(page = 1) {
    setLoading(true);
    const params = "";
    getInstances(params).then((response) => {
      const { data } = response;
      setLoading(false);
      setInstances(data.map(
        (instance) => {
          instance.key = instance.id
          return instance;
        }
      ));
    });
  }
  
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
  ];

  useEffect(() => {
    getList();
  }, []);

  return (
    <div className="not-found-page">
      <div className="text-center">
        <p className="text-5xl font-bold secondary-font secondary mb-4">
          SERVER MANAGEMENT
        </p>
        <Table 
          dataSource={instances} 
          columns={columns}
          loading={loading}
        />
      </div>
    </div>
  );
};

export default ServerManagementPage;
