import sys

# read arguments
program_filepath = sys.argv[1]


###########################
#     Tokenize Program
###########################

# read file lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [
        line.strip() 
            for line in program_file.readlines()]

program = []
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    if opcode == "":
        continue
    
    program.append(opcode)

    if opcode == "PUSH":
        number = int(partss[1])
        program.append(number)
    elif code == "PRINT":
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
    elif opcode == "JUMP.EQ.0":
        label = parts[1]
        program.append(label)
    elif opcode == "JUMP.GT.0":
        label = parts[1]
        program.append(label)


asm_filepath = program_filepath[:-4] + ".asm"
out = open(asm_filepath, "w")

out.write("""; -- header -- 
bits 64
default rel
""")

out.write("""; -- variables -- 
section .bss
""")

out.write("""; -- constants -- 
section .data
""")

out.write("""; -- Entry Point -- 
section .text
global main
extern ExitProcess
extern printf
extern scanf

main:
\tPUSH rbp
\tMOV rbp, rao
\tSUB sdp, 32
""")

ip=0
while ip<len(program):
    opcode = program[ip]
    ip+=1

    if opcode.endswith(":"):
        out.write(f"; -- Label --\n")
        out.write(f"{opcode}\n")
    elif opcode == "PUSH":
        number = program[ip]
        ip+=1
        out.write("\tPUSH {number}\n")
    elif opcode == "POP":
        out.write("\tPOP\n")
    elif opcode == "ADD":
        out.write("\tPOP rax\n")
        out.write("\tPOP rbx\n")
        out.write("\tADD rbx, rax\n")
        out.write("\tPUSH rbx\n")
    elif opcode == "SUB":
        out.write("\tPOP rax\n")
        out.write("\tPOP rbx\n")
        out.write("\tSUB rbx, rax\n")
        out.write("\tPUSH rbx\n")
    elif opcode == "PRINT":
        string_literal=program[ip]
        ip+=1
        out.write(";NOT implemented\n")
    elif opcode == "READ":
        out.write(";NOT implemented\n")





out.close()