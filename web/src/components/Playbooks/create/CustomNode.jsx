import React from "react";
import { Handle, NodeToolbar, Position } from "reactflow";
import { useDispatch, useSelector } from "react-redux";
import {
  deleteStep,
  playbookSelector,
  setCurrentStepIndex,
} from "../../../store/features/playbook/playbookSlice.ts";
import { cardsData } from "../../../utils/cardsData.js";
import { CircularProgress } from "@mui/material";
import { CheckCircleOutline, Delete, ErrorOutline } from "@mui/icons-material";
import CustomButton from "../../common/CustomButton/index.tsx";
import useDrawerState from "../../../hooks/useDrawerState.ts";
import { DrawerTypes } from "../../../store/features/drawers/drawerTypes.ts";
import AddCondition from "../../AddCondition/index.tsx";

const id = DrawerTypes.STEP_DETAILS;
const addDataId = DrawerTypes.ADD_DATA;

export default function CustomNode({ data }) {
  const { toggle: toggleAddData, addAdditionalData } =
    useDrawerState(addDataId);
  const dispatch = useDispatch();
  const { currentStepIndex } = useSelector(playbookSelector);
  const { toggle } = useDrawerState(id);
  const step = data.step;

  const handleNoAction = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleClick = () => {
    dispatch(setCurrentStepIndex(data.index));
    toggle();
  };

  const handleDelete = (e) => {
    handleNoAction(e);
    dispatch(deleteStep(data.index));
  };

  const handleAdd = (e) => {
    handleNoAction(e);
    toggleAddData();
    addAdditionalData({ parentIndex: data.index });
  };

  return (
    <>
      <div
        className={`${
          currentStepIndex === data.index.toString() ? "shadow-violet-500" : ""
        } px-4 py-2 shadow-md rounded-md bg-white border-2 border-stone-400 w-[200px] h-48 cursor-pointer transition-all hover:shadow-violet-500`}
        onClick={handleClick}>
        <div className="">
          {(step.outputLoading || step.inprogress) && (
            <CircularProgress size={20} />
          )}
          {(step.outputError ||
            Object.keys(data?.step?.errors ?? {}).length > 0) && (
            <ErrorOutline color="error" size={20} />
          )}
          {!step.outputError &&
            !step.outputLoading &&
            step.showOutput &&
            step.outputs?.data?.length > 0 &&
            Object.keys(data?.step?.errors ?? {}).length === 0 && (
              <CheckCircleOutline color="success" size={20} />
            )}
        </div>

        <div
          className="absolute top-0 right-0 m-2 text-violet-500"
          onClick={handleDelete}>
          <Delete fontSize="medium" />
        </div>

        <div className="flex flex-col items-center gap-4">
          {data?.step?.source && (
            <img
              className="w-10 h-10"
              src={
                cardsData.find(
                  (e) => e.enum === data?.step?.source.replace("_VPC", ""),
                )?.url ?? ""
              }
              alt="logo"
            />
          )}
          <p className="text-lg font-bold text-center z-10 break-word line-clamp-3">
            {data?.step?.description ||
              data?.step?.selectedSource ||
              `Step - ${data?.index + 1}`}
          </p>
        </div>

        <Handle
          type="target"
          position={Position.Top}
          className="!bg-white !w-5 !h-5 absolute !top-0 !transform !-translate-x-1/2 !-translate-y-1/2 !border-violet-500 !border-2"
        />

        <Handle
          type="source"
          position={Position.Bottom}
          className="!bg-white !w-5 !h-5 absolute !bottom-0 !transform !-translate-x-1/2 !translate-y-1/2 !border-violet-500 !border-2"
        />

        <NodeToolbar isVisible={true} position={Position.Bottom}>
          <CustomButton onClick={handleAdd}>Add Step</CustomButton>
        </NodeToolbar>

        {step.requireCondition && (
          <NodeToolbar
            isVisible={true}
            position={Position.Left}
            onClick={handleNoAction}
            className="nodrag">
            <AddCondition step={step} />
          </NodeToolbar>
        )}
      </div>

      <div className="absolute top-0 left-0 w-screen"></div>
    </>
  );
}
