"""
Author:
    Gabriel Russell

Program Purpose:
    Provides a function that can be used to compile Nomad Assembly Files
License:
    GPL v3
    https://www.gnu.org/licenses/gpl-3.0.en.html
"""
# Nomad Assembler
# Gabriel Russell 2019
# https://github.com/gabrielrrussell/Nomad

# Translation of Register Values.
registerKeys = {
        "A": "0","B": "1",
        "x0": "2","x1": "3","x2": "4","x3": "5","x4": "6","x5": "7","x6": "8",
        "s0": "9","s1": "A","s2": "B",
        "i0": "C","i1": "D","i2": "E","i3": "F"
        }

# Translation of Operation Values
operationKeys = {
    "nop": "0", "//": "0",
    "add": "1", "sub": "2",
    "and": "3", "not": "4", "or": "5", "xor": "6",
    "lsl": "7", "lsr": "8",
    "mov": "9", "pnt": "9", "lmr": "A", "lrm": "B",
    "jeq": "C", "jnq": "D", "jgt": "E", "jlt": "F", "print": "9"
    }

# I slapped it into this really ugly function for a reason. I'll probably
# Clean it up later.
def compile(inFile, outFile):
    inFile = open(inFile, 'r')
    outFile = open(outFile, 'w')
    outFile.write("v2.0 raw\n")
    register = 0
    operation = 0
    operand = 0
    currentLine = 0
    # Go through each line in the file individually
    for line in inFile:
        currentLine += 1
        # Check if the maximum program size has been exceeded before Assembly
        if currentLine > 255:
            print("MAXIMUM PROGRAM LIMIT REACHED. STOPPING ASSEMBLY")
            break

        # Split the instruction into a list via spaces
        command = line.split()

        # Translate the operation for assembly
        operation = operationKeys[command[0]]

        # Why not use the translated key instead of the operation name?
        # It's easier to spot the specific line of code needed. Not much else for it.

        # The operations all follow a similar format, so only the ones that follow a different format must have a separate definition / execution.

        # No Operation, Clear. 0000 does nothing to the CPU state
        if command[0] in ("nop"):
            operand = "00"
            register = "0"
        # Print. Symbolic, will get complete printing working later.
        elif command[0] in "pnt":
            operation = "9"
            register = "A"
            operand = hex(ord(command[1]))[2:]
        elif command[0] in ("add", "sub", "and", "not", "or", "xor"):
            register = registerKeys[command[1]]
            operand = "00"
        elif command[0] in ("lsl", "lsr"):
            # Since Nomad is 8 Bits, the maximum Logical Shift is 7 bits.
            # Check for unexpected behavior
            # Only the first three bits of the operand are read for a (0-7) shift,
            # so 00000111 could be read as seven, but 8 would be read as
            # 00001000 => Logical Shift by Zero Bits. Unexpected Behavior
            if int(command[2]) > 7:
                print("ERROR: CANNOT LOGICAL SHIFT MORE THAN SEVEN BITS. LINE " + str(currentLine))
                print("Stopping Assembly")
                break
            register = registerKeys[command[1]]
            print (command[2])
            shiftBy = int(command[2])
            shiftBy = hex(shiftBy)[2:]
            print(shiftBy)
            operand = "0" + str(shiftBy)
        # Locate Memory / Register Memory / Register are simply swapped values for their definition.
        elif command[0] in "lmr":
            if command[2][0:2] != "0x":
                print("MEMORY MUST BE ADDRESSED IN HEX FORM 0x, ERROR AT LINE " + str(currentLine))
                break
            if len(command[2][2:]) > 2:
                print("MEMORY ADDRESS IS LIMITED TO TWO HEX VALUES, IMPOSSIBLE ADDRESS DETECTED, ERROR AT LINE " + str(currentLine))
                break
            register = registerKeys[command[1]]
            operand = command[2][2:]
        elif command[0] in "lrm":
            if command[1][0:2] != "0x":
                print("MEMORY MUST BE ADDRESSED IN HEX FORM 0x, ERROR AT LINE " + str(currentLine))
                break
            if len(command[1][2:]) > 2:
                print("MEMORY ADDRESS IS LIMITED TO TWO HEX VALUES, IMPOSSIBLE ADDRESS DETECTED, ERROR AT LINE " + str(currentLine))
                break
            register = registerKeys[command[2]]
            operand = command[1][2:]
        elif command[0] in "mov":
            if int(command[2]) > 255:
                print("IMPOSSIBLE NUMBER DETECTED, MAX BIT WIDTH IS 8 BITS OR VALUE OF 255 DEC, ERROR AT LINE " + str(currentLine))
                break
            register = registerKeys[command[1]]
            operand = hex(int(command[2]))[2:]
        # Only the operand is read in a jump command.
        elif command[0] in ("jeq", "jnq", "jgt", "jlt"):
            operand = command[1][2:]
            register = "0"

        # Check to make sure values aren't dropped. Each address is four hex values wide
        # meaning that if a single character is dropped, an instruction might be parsed wrong
        if len(str(operand)) < 2:
            operand = "0" + str(operand)
        # Print the instruction for verification, and write to the file.
        if command[0] == "print":
            temp = ""
            res = ""
            i = 0
            for item in command[1:]:
                item.replace('"', "")
                res += item
                res += " "

            for char in res:
                hexAscii = hex(ord(char))[2:]
                outFile.write("9A" + hexAscii + "\n")
            outFile.write("9A00")
                
        if command[0] != "//" and command[0] != "print":
            print(str(operation) + str(register) + str(operand))
            outFile.write(str(operation) + str(register) + str(operand) + "\n")
    outFile.close()
