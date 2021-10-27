import { useEffect, useState } from "react";
import { useParams } from "react-router";
import { Link, useHistory } from "react-router-dom";
import { Table, Modal, Button, Form, Input, Card, Space, Tabs, Select, message } from "antd";
import { getMysqlQueries } from "../../actions";

const { TabPane } = Tabs;
const { Option } = Select;

const SingleServerManagementPage = () => {
    const [loading, setLoading] = useState(false);
    const [mySqlQueries, setmySqlQueries] = useState([]);

    const params = useParams();
    const { serverId } = params;

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
                <a onClick={() => executeMysqlQuery(record.id)}> Execute Query </a>

            ),
        },
    ];

    function executeMysqlQuery(mysqlQueryId) {
        alert(mysqlQueryId, "is query id");
    }

    function listAllMysqlQueries() {
        setLoading(true);
        const params = "";
        getMysqlQueries(params).then((response) => {
            const { data } = response;
            setLoading(false);
            setmySqlQueries(data);
        });
    }

    function handleChange(value) {
        console.log(`selected ${value}`);
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
                Select Desired Queries to add to server
                <Select
                    mode="multiple"
                    allowClear
                    style={{ width: '100%' }}
                    placeholder="Please select"
                    defaultValue={(mySqlQueries).map((item) => {
                        return item.id
                    })}
                    onChange={() =>handleChange()}
                >
                    {(mySqlQueries).map((item) => {
                        return (
                            <Select.Option value={item.id} key={item.id}>
                                {item.name}
                            </Select.Option>
                        );
                    })}
                </Select>

                <Table
                    dataSource={(mySqlQueries).filter((item) => {
                        if(item.id === 2) return true;
                    })}
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
