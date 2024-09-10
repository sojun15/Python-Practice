file1 = open("previous.txt","r")
file2 = open("updated.txt","w")

value = 1
for single_line in file1.readlines():
    if "//" in single_line:
        continue
    elif "/*" in single_line:
        value = 0
    elif "*/" in single_line:
        value = 1
    elif value:
        file2.write(single_line)

file1 = open("previous.txt","r")

# determine keywords from previous file then write them into updated file 
for single_line in file1.readlines():
    if "else if" in single_line:
        file2.write("\nelse if")
    if "if" in single_line:
        file2.write("\nif")
    if "for" in single_line:
        file2.write("\nfor")
    if "int" in single_line:
        file2.write("\nint")
    if "using" in single_line:
        file2.write("\nusing")