# Simple script to convert Excel-like tables to Latex tables (tabularx package format)
For script to convert table, first either copy selected cells in excel (using CTRL-C) and paste to input.txt file or write it yourself. 

Formating of the table could look like following:
```
FIELD1 FIELD2 FIELD3 
1      2      3
4 5 6
7   8   9
```
- There could mix of spaces and tabs in between columns but rows need to be seperated by new line character

`CUSTOM_FIELDS` variable can be set to either `True` or `False`
- When set to `False` it will append generic row with: Field1, Field2, ... , Field(n)
- When set to `True` it will just generate table as it is copied or written
