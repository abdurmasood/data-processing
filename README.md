# data-processing

## Assumptions
- At least one sheet will always be present in the configuration
- The filename format of the workbook to read will be the same everytime
- Output workbooks may or may not be specified
- Formatting will be not be needed at all so automatic removal
- When creating a new column and defining its formula we will assume that the only operations that will be used are +, -, *, / and there will only be two elements that will be processed
- We are assuming that there will only be one sheet for every workbook created