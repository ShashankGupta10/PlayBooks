/* eslint-disable react-hooks/exhaustive-deps */
import { CircularProgress, Tab, Tabs } from "@mui/material";
import Heading from "../../Heading.js";
import styles from "./index.module.css";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  connectorSelector,
  integrationsSelector,
  setCurrentConnector,
} from "../../../store/features/integrations/integrationsSlice.ts";
import { useNavigate, useParams } from "react-router-dom";
import Config from "./Config.jsx";
import TabPanel from "./TabPanel.jsx";
import Assets from "./Assets.jsx";
import { connectorsWithoutAssets } from "../../../utils/connectorsWithoutAssets.ts";
import { unsupportedConnectors } from "../../../utils/unsupportedConnectors.ts";
import {
  useGetConnectorKeyOptionsQuery,
  useGetConnectorKeysQuery,
} from "../../../store/features/integrations/api/index.ts";
import { ChevronLeft } from "@mui/icons-material";
import GoogleChatIntegration from "./GoogleChatIntegration.jsx";

function ConnectorPageBeta() {
  const { id, connectorEnum } = useParams();
  const navigate = useNavigate();

  const dispatch = useDispatch();
  const connectors = useSelector(integrationsSelector);
  const currentConnector = useSelector(connectorSelector);
  const [selectedTab, setSelectedTab] = useState(0);
  const { data: keyOptions, isFetching: optionsLoading } =
    useGetConnectorKeyOptionsQuery(connectorEnum);
  const { isFetching: keysLoading } = useGetConnectorKeysQuery(id);

  useEffect(() => {
    if (connectors?.length > 0 && id) {
      dispatch(setCurrentConnector(id));
    }
  }, [connectors]);

  const handleTabChange = (_, newValue) => {
    setSelectedTab(newValue);
  };

  const containsAssets = !connectorsWithoutAssets.includes(
    connectorEnum.toUpperCase(),
  );

  const isActive = currentConnector?.is_active;

  switch (id) {
    case unsupportedConnectors.GOOGLE_CHAT:
      return <GoogleChatIntegration />;
    default:
      break;
  }

  if (optionsLoading || keysLoading) {
    return (
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          height: "100vh",
        }}>
        <CircularProgress />
      </div>
    );
  }

  return (
    <div>
      <Heading
        heading={`${
          currentConnector?.displayTitle ?? currentConnector?.type
        } Integration Setup`}
        onTimeRangeChangeCb={false}
        onRefreshCb={false}
      />

      <button
        onClick={() => navigate(-1)}
        className="p-1 text-sm border border-violet-500 rounded m-2 text-violet-500 flex items-center cursor-pointer hover:text-white hover:bg-violet-500 transition-all">
        <ChevronLeft /> All Integrations
      </button>

      {isActive && (
        <Tabs
          value={selectedTab}
          onChange={handleTabChange}
          className={styles["tab-section"]}>
          <Tab label="Config" id="tab-0" aria-controls="tabpanel-0" />
          {containsAssets && (
            <Tab label="Assets" id="tab-1" aria-controls="tabpanel-1" />
          )}
        </Tabs>
      )}

      <TabPanel
        value={selectedTab}
        index={0}
        className={styles["config-section"]}>
        <Config keyOptions={keyOptions} />
      </TabPanel>

      {isActive && containsAssets && (
        <TabPanel
          value={selectedTab}
          index={1}
          className={styles["config-section"]}>
          <Assets />
        </TabPanel>
      )}
    </div>
  );
}

export default ConnectorPageBeta;
