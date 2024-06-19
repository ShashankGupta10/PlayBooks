import { store } from "../../../store/index.ts";
import { playbookSelector } from "../../../store/features/playbook/playbookSlice.ts";
import { PlaybookContractStep, Step } from "../../../types.ts";

function extractNumbers(input: string) {
  if (!input) return [];
  // Use regular expression to match numbers in the string
  const numbers = input.match(/\d+/g);

  // Convert the matched strings to integers
  const result = numbers ? numbers.map(Number) : [];

  return result;
}

export const stateToStepRelation = (
  playbookContractSteps: PlaybookContractStep[],
) => {
  const { playbookEdges, steps } = playbookSelector(store.getState());

  const relations = (playbookEdges ?? [])
    .filter((e) => e.source !== "playbook")
    .map((edge) => {
      const [parentIndex] = extractNumbers(edge.source);
      const [childIndex] = extractNumbers(edge.target);
      const parent = playbookContractSteps[parentIndex];
      const child = playbookContractSteps[childIndex];

      const parentStep: Step = steps[parentIndex];

      return {
        parent: {
          reference_id: parent.reference_id,
        },
        child: {
          reference_id: child.reference_id,
        },
        condition:
          edge.conditions?.length > 0
            ? {
                rules: edge.conditions?.map((e) => {
                  return {
                    type: parentStep.resultType,
                    task: {
                      reference_id: parent.tasks[0].reference_id,
                    },
                    [parentStep.resultType!.toLowerCase()]: {
                      type: "CUMULATIVE",
                      function: e.function,
                      operator: e.operation,
                      threshold: e.value,
                    },
                  };
                }),
                logical_operator: edge.globalRule,
              }
            : {},
      };
    });

  return relations;
};
