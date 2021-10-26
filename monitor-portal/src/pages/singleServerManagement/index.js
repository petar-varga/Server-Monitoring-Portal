import { useEffect, useState } from "react";
import { Table, Modal, Button, Form, Input, Card, Space, Tabs, message } from "antd";

const { TabPane } = Tabs;

const SingleServerManagementPage = () => {
    const [loading, setLoading] = useState(false);

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
