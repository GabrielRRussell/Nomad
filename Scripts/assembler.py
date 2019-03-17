# Gabriel Russell 2019
# https://github.com/gabrielrrussell/Nomad
# Extremely Inneficient Assembler
# Only part way done. Will probably clean up later.
# The only current documentation on the assembly language is on my computer,
# More information will be released later.

command = input("Enter in a command ")
command = command.split()

# Set some temporary global values
register = 0 
operation = 0
operand = 0

# Translation of Register Values.
registerKeys = {
        "A": "0","B": "1",
        "x0": "2","x1": "3","x2": "4","x3": "5","x4": "6","x5": "7","x6": "8",
        "s0": "9","s1": "A","s2": "B",
        "i0": "C","i1": "D","i2": "E","i3": "F"
    }
# Translation of Operation Values
operationKeys = {
    "nop": "0",
    "add": "1", "sub": "2",
    "and": "3", "not": "4", "or": "5", "xor": "6",
    "lsl": "7", "lsr": "8",
    "mov": "9", "lmr": "A", "lrm": "B",
    "jeq": "C", "jnq": "D", "jgt": "E", "jlt": "F"
    }

operation = operationKeys[command[0]]
    
if command[0] in ("nop"):
    operand = "00"
    register = "0"
elif command[0] in ("add, sub", "and", "not", "or", "xor"):
    register = command[1]
    operand = "00"
elif command[0] in ("lsl", "lsr"):
    # TO DO:
    # ADD PROTECTIONS, 3 BIT MAXIMUM FOR SHIFTS. IF OR > 7, REJECT CODE
    register = registerKeys[command[1]]
    operand = "0" + str(hex(int(command[2]))[2:])
elif command[0] in "lmr":
    register = registerKeys[command[1]]
    operand = command[2][2:]
elif command[0] in "lrm":
    register = registerKeys[command[2]]
    operand = command[1][2:]
elif command[0] in "mov":
    register = registerKeys[command[1]]
    operand = hex(int(command[2]))[2:]
elif command[0] in ("jeq", "jnq", "jgt", "jlt"):
    operand = hex(int(command[1]))[2:]

print(str(operation) + str(register) + str(operand))

# Comment this out for now - just some special formulas to copy
# register = registerKeys[command[1]]
# operand = hex(int(command[2]))[2:]
# print(str(operation) + str(register) + str(operand))
