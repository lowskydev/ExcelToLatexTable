CUSTOM_FIELDS=True

file = open('input.txt', 'r')
lines = [x.rstrip('\n').split('\t') for x in file.readlines()]
file.close()

row_size = len(lines)
col_size = len(lines[0])

output = "\\begin{center}\n\\begin{tabularx}{0.9\\textwidth} {"
output += "\n | >{\\centering\\arraybackslash}X " * col_size
output += "| }\n\\hline\n"

if not CUSTOM_FIELDS:
    for i in range(col_size):
        output += f"field {i + 1}"
        if i != col_size-1:
            output += " & "
    output += " \\\\\n\\hline\n"

for i in range(row_size):
    for j in range(col_size):
        output += f"{lines[i][j]}"
        if j != col_size - 1:
            output += " & "
    output += " \\\\\n\\hline\n"

output += "\\end{tabularx}\n\\end{center}"

print(output)