import { Table } from "antd";
import { useHistory } from "react-router";

const NotFoundPage = () => {
  const history = useHistory();
  const dataSource = [
    {
      key: '1',
      serverInfo: {
        "name": "MFS Prod",
        "ip": "127.0.0.1"
      },
      operatingSystem: "Ubuntu",
      status: 'Running',
    },
    {
      key: '2',
      serverInfo: {
        "name": "MFS Prod",
        "ip": "127.0.0.1"
      },
      operatingSystem: "CentOS",
      status: 'Stopped',
    },
  ];
  
  const columns = [
    {
      title: 'Server',
      dataIndex: 'serverInfo',
      key: 'serverInfo',
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
      dataIndex: 'operatingSystem',
      key: 'operatingSystem',
    },
    {
      title: 'Status',
      dataIndex: 'status',
      key: 'status',
    },
  ];

  return (
    <div className="not-found-page">
      <div className="text-center">
        <p className="text-5xl font-bold secondary-font secondary mb-4">
          SERVER MANAGEMENT
        </p>
        <Table 
          dataSource={dataSource} 
          columns={columns}

        />
      </div>
    </div>
  );
};

export default NotFoundPage;
