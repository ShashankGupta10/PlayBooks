/* eslint-disable react-hooks/exhaustive-deps */
import { useState } from "react";
import { Tooltip } from "@mui/material";
import styles from "../playbooks.module.css";
import Notes from "./Notes.jsx";
import DeleteIcon from "@mui/icons-material/Delete";
import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import { useDispatch } from "react-redux";
import {
  addExternalLinks,
  deleteStep,
  toggleExternalLinkVisibility,
} from "../../../store/features/playbook/playbookSlice.ts";
import ExternalLinks from "./ExternalLinks.jsx";
import Query from "./Query.jsx";
import useIsPrefetched from "../../../hooks/useIsPrefetched.ts";
import { unsupportedRunners } from "../../../utils/unsupportedRunners.ts";
import ExternalLinksList from "../../common/ExternalLinksList/index.tsx";
import { executeStep } from "../../../utils/execution/executeStep.ts";
import Interpretation from "./Interpretation.jsx";

function Step({ step }) {
  const isPrefetched = useIsPrefetched();
  const [addQuery, setAddQuery] = useState(
    step?.isPrefetched ?? step.source ?? false,
  );
  const dispatch = useDispatch();

  function handleDeleteClick() {
    dispatch(deleteStep());
  }

  const toggleExternalLinks = () => {
    dispatch(toggleExternalLinkVisibility());
  };

  const setLinks = (links) => {
    dispatch(addExternalLinks(links));
  };

  return (
    <div className={styles["step-card"]}>
      <div
        className={styles["step-card-content"]}
        style={{ paddingBottom: "0px" }}>
        <div className={styles["step-name"]}>
          {step.isPrefetched && step.description && (
            <div className={styles.head}>
              <ExternalLinksList />
            </div>
          )}
        </div>
        <div className={styles["step-section"]}>
          <div className={styles["step-info"]}>
            <div>
              <div
                className={styles["addConditionStyle"]}
                onClick={() => setAddQuery(true)}>
                <b className="add_data">{!addQuery ? "+ Add Data" : "Data"}</b>
              </div>

              {addQuery && <Query />}
            </div>
          </div>
          <Notes />
          <Interpretation />
          {!isPrefetched && (
            <div className={styles["step-buttons"]}>
              {step.source && !unsupportedRunners.includes(step.source) && (
                <button
                  className={styles["pb-button"]}
                  onClick={() => executeStep(step)}>
                  <Tooltip title="Run this Step">
                    <>
                      Run <PlayArrowIcon />
                    </>
                  </Tooltip>
                </button>
              )}
              <button
                className={styles["pb-button"]}
                onClick={handleDeleteClick}>
                <Tooltip title="Remove this Step">
                  <DeleteIcon />
                </Tooltip>
              </button>
            </div>
          )}
          {!isPrefetched && (
            <div>
              <div>
                <div
                  className={styles["addConditionStyle"]}
                  onClick={toggleExternalLinks}>
                  <b className="ext_links">
                    {step.showExternalLinks ? "-" : "+"}
                  </b>{" "}
                  Add External Links
                </div>

                {step.showExternalLinks && (
                  <ExternalLinks
                    links={step.externalLinks}
                    setLinks={setLinks}
                  />
                )}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Step;
