import { InputTypes } from "../../../types";
import CustomInput from "../../Inputs/CustomInput";
import { notificationOptions } from "./utils";

function AddNotification() {
  return (
    <div className="flex flex-col gap-1">
      <p className="font-bold text-violet-500 text-sm">Notification</p>
      <div className="flex flex-col items-start gap-1">
        <CustomInput
          inputType={InputTypes.DROPDOWN}
          options={notificationOptions}
          value={""}
          placeholder={`Select Source`}
          handleChange={() => {}}
          error={undefined}
        />
      </div>
    </div>
  );
}

export default AddNotification;
