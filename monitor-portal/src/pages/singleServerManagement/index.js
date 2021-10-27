import { useEffect, useState } from "react";
import { Link, useHistory } from "react-router-dom";
import { Table, Modal, Button, Form, Input, Card, Space, Tabs, Select, message } from "antd";
import { getMysqlQueries } from "../../actions";

const { TabPane } = Tabs;
const { Option } = Select;

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
                <a onClick={() => executeMysqlQuery(record.id)}> Execute Query </a>

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

    function onChange(value) {
        console.log(`selected ${value}`);
    }

    function onBlur() {
        console.log('blur');
    }

    function onFocus() {
        console.log('focus');
    }

    function onSearch(val) {
        console.log('search:', val);
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
                <Select
                    showSearch
                    style={{ width: 200 }}
                    placeholder="Select a person"
                    optionFilterProp="children"
                    onChange={onChange}
                    onFocus={onFocus}
                    onBlur={onBlur}
                    onSearch={onSearch}
                    filterOption={(input, option) =>
                        option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
                    }
                >
                    <Option value="jack">Jack</Option>
                    <Option value="lucy">Lucy</Option>
                    <Option value="tom">Tom</Option>
                </Select>
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
