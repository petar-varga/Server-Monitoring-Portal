import { useEffect, useState } from "react";
import { Link, useHistory } from "react-router-dom";
import { Table, Modal, Button, Form, Input, Card, Space, Tabs, message } from "antd";
import { getMysqlQueries } from "../../actions";

const { TabPane } = Tabs;


const SingleServerManagementPage = () => {
    const [loading, setLoading] = useState(false);
    const [mysqlQueries, setQueries] = useState([]);

    const columns = [
        {
            title: 'Query Name',
            dataIndex: 'name',
            key: 'name'
        },
        {
            title: 'Query',
            dataIndex: 'sql_query',
            key: 'sql_query',
        },
        {
            key: "action",
            title: "Action",
            render: (record) => (
                <a onClick={()=> executeMysqlQuery(record.id)}> Execute Query </a>
                
            ),
          },
    ];

    function executeMysqlQuery(mysqlQueryId) {
        alert(mysqlQueryId, "is query id");
    }

    function listAllMysqlQueries(page = 1) {
        setLoading(true);
        const params = "";
        getMysqlQueries(params).then((response) => {
            const { data } = response;
            setLoading(false);
            setQueries(data);
        });
    }

    useEffect(() => {
        listAllMysqlQueries();
      }, []);

    return (
        <Tabs defaultActiveKey="1" centered>
            <TabPane tab="Overview" key="1">
                Contents of generic overview
            </TabPane>
            <TabPane tab="Health" key="2">
                Generic server health metrics
            </TabPane>
            <TabPane tab="MySQL Queries" key="3">
                Custom MySQL Queries
                <Table
                    dataSource={mysqlQueries}
                    columns={columns}
                    loading={loading}
                />
            </TabPane>
            <TabPane tab="Alerts" key="4">
                Server Alerts setup and configuration
            </TabPane>
            <TabPane tab="Actions" key="5">
                Server actions
            </TabPane>
        </Tabs>
    );
};

export default SingleServerManagementPage;
