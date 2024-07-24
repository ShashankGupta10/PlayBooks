import React from "react";
import { useSelector } from "react-redux";
import { additionalStateSelector } from "../../../store/features/drawers/drawersSlice.ts";
import useEdgeConditions from "../../../hooks/useEdgeConditions.ts";
import { HandleTypesPropTypes } from "../HandleTypes.tsx";
import Checkbox from "../../common/Checkbox/index.tsx";
import { addConditionToEdgeByIndex } from "../../../utils/conditionals/addConditionToEdgeByIndex.ts";
import { operationOptions } from "../../../utils/conditionals/operationOptions.ts";
import CustomInput from "../../Inputs/CustomInput.tsx";
import { InputTypes } from "../../../types/inputs/inputTypes.ts";

function GrepCount({ condition, conditionIndex, rule }: HandleTypesPropTypes) {
  const { id } = useSelector(additionalStateSelector);
  const { handleCondition, edgeIndex } = useEdgeConditions(id);
  const keyValue = condition?.type?.toLowerCase();

  const handleChange = (val: string, type: string) => {
    handleCondition(`${keyValue}.${type}`, val, conditionIndex);
  };

  return (
    <div className="flex flex-wrap gap-2 items-center">
      <CustomInput
        inputType={InputTypes.TEXT}
        value={rule.pattern}
        handleChange={(val: string) => handleChange(val, `pattern`)}
        placeholder={"Enter pattern to evaluate"}
        className="!w-[200px]"
      />

      <Checkbox
        id="case_sensitive"
        isChecked={rule.case_sensitive}
        onChange={() => {
          addConditionToEdgeByIndex(
            `${keyValue}.case_sensitive`,
            !rule.case_sensitive,
            edgeIndex,
            conditionIndex,
          );
        }}
        label="Pattern is Case Sensitive"
        isSmall={true}
      />

      <CustomInput
        inputType={InputTypes.DROPDOWN}
        error={undefined}
        options={operationOptions}
        value={rule.operator}
        handleChange={(id: string) => handleChange(id, `operator`)}
        placeholder={`Select Operator`}
      />

      <CustomInput
        inputType={InputTypes.TEXT}
        value={rule.threshold}
        handleChange={(val: string) => handleChange(val, `threshold`)}
        placeholder={"Enter threshold"}
        className="!w-[200px]"
      />
    </div>
  );
}

export default GrepCount;
