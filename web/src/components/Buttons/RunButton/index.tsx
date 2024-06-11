import React from "react";
import CustomButton from "../../common/CustomButton/index.tsx";
import { PlayArrowRounded } from "@mui/icons-material";
import { executeStep } from "../../../utils/execution/executeStep.ts";
import useCurrentStep from "../../../hooks/useCurrentStep.ts";
import useIsPrefetched from "../../../hooks/useIsPrefetched.ts";
import { unsupportedRunners } from "../../../utils/unsupportedRunners.ts";
import { CircularProgress, Tooltip } from "@mui/material";
import { useDispatch, useSelector } from "react-redux";
import useIsExisting from "../../../hooks/useIsExisting.ts";
import {
  playbookSelector,
  setPlaybookKey,
} from "../../../store/features/playbook/playbookSlice.ts";
import { useStartExecutionMutation } from "../../../store/features/playbook/api/index.ts";
import { useSearchParams } from "react-router-dom";

type RunButtonProps = {
  index: number;
};

function RunButton({ index }: RunButtonProps) {
  const { executionId, currentPlaybook } = useSelector(playbookSelector);
  const [, setSearchParams] = useSearchParams();
  const [step] = useCurrentStep(index);
  const dispatch = useDispatch();
  const isPrefetched = useIsPrefetched();
  const isExisting = useIsExisting();
  const [triggerStartExecution, { isLoading: executionLoading }] =
    useStartExecutionMutation();
  const loading = step.outputLoading || executionLoading;

  const handleStartExecution = async () => {
    if (executionId) return;
    const response = await triggerStartExecution(currentPlaybook.id);
    if ("data" in response) {
      const { data } = response;
      return data.playbook_run_id;
    }
  };

  const handleExecuteStep = async () => {
    if (isExisting && !executionId) {
      const id = await handleStartExecution();
      dispatch(setPlaybookKey({ key: "executionId", value: id }));
      await executeStep(step, index);
      setSearchParams({ executionId: id });
    } else {
      executeStep(step, index);
    }
  };

  if (isPrefetched || !step.source || unsupportedRunners.includes(step.source))
    return <></>;

  return (
    <Tooltip title="Run this Step">
      <CustomButton onClick={handleExecuteStep}>
        {loading ? "Running" : "Run"}
        {loading ? (
          <CircularProgress color="inherit" size={20} />
        ) : (
          <PlayArrowRounded fontSize="medium" />
        )}
      </CustomButton>
    </Tooltip>
  );
}

export default RunButton;
