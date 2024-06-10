import { useState, useEffect } from "react";
import styles from "./index.module.css";

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Button,
  Dialog,
  DialogActions,
} from "@mui/material";

import SeeMoreTextWithoutModal from "../common/SeeMoreTextWithoutModal/index.tsx";

const PlayBookRunDataTable = ({ title, result, timestamp }) => {
  const [showTable, setShowTable] = useState(false);
  const [open, setOpen] = useState(false);

  const [tableData, setTableData] = useState([]);

  useEffect(() => {
    if (
      result &&
      result.table &&
      result.table.rows &&
      result.table.rows.length > 0
    ) {
      setTableData(result.table.rows);
      setShowTable(true);
    }
  }, [result]);

  const handleClose = () => {
    setOpen(false);
  };

  const columnLength = tableData[0]?.columns?.length;
  const shouldNoWrap = columnLength < 5;

  return (
    <div className={styles["graph-box"]}>
      <p className={styles["graph-title"]}>{title}</p>
      {!showTable && <p className={styles["graph-error"]}>No data available</p>}
      {showTable && (
        <Table
          stickyHeader
          className={`text-xs min-w-[50px] !border !rounded !overflow-hidden mt-2`}>
          <TableHead>
            <TableRow>
              {tableData[0]?.columns
                ?.filter((x) => x.name !== "@ptr")
                .map((col, index) => {
                  return (
                    <TableCell className="!text-sm !w-fit !min-w-[50px] !max-w-[200px]">
                      <SeeMoreTextWithoutModal text={col.name} maxLength={50} />
                    </TableCell>
                  );
                })}
            </TableRow>
          </TableHead>
          <TableBody>
            {tableData?.map((row, rowIndex) => {
              return (
                <TableRow key={rowIndex}>
                  {row?.columns
                    ?.filter((x) => x.name !== "@ptr")
                    .map((col, colIndex) => {
                      return (
                        <TableCell
                          key={colIndex}
                          className={`${
                            col.name === "@message"
                              ? "min-w-[100px]"
                              : "min-w-[50px]"
                          } !text-xs`}>
                          <SeeMoreTextWithoutModal
                            shouldNoWrap={shouldNoWrap}
                            text={col.value}
                            maxLength={200}
                          />
                        </TableCell>
                      );
                    })}
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      )}
      {!showTable && timestamp && (
        <p className={styles["graph-ts-error"]}>
          <i>Updated at: {timestamp}</i>
        </p>
      )}
      {showTable && timestamp && (
        <p className={styles["graph-ts"]}>
          <i>Updated at: {timestamp}</i>
        </p>
      )}
      <Dialog open={open} onClose={handleClose}>
        <DialogActions>
          <Button onClick={handleClose} color="primary">
            Close
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default PlayBookRunDataTable;
