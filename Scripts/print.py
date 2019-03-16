# This program helps create a print sequence for Nomad
# If you have no idea what this does,
# Please read some of the other documentation.
# You can find this project at 
# https://github.com/gabrielrrussell/Nomad

humantext = input("PNT Translator\nKeep in mind that there's currently a 256 max instruction limit.\nEnter your Text: ")
print()
# For Each Character in Text Input
for char in humantext:
  # Convert to ASCII Decimal, Convert to Hex, 
  # Strip the 0x symbol, Print
  print("9A" + hex(ord(char))[2:])
# Print the ending character. Not setting the register to zero will cause it to repeatedly print the same character.
print("9A00")