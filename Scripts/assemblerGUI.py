"""
Author:
    Gabriel Russell

Program Purpose:
    Provides a GUI for compiling Nomad assembly files

License:
    GPL v3
    https://www.gnu.org/licenses/gpl-3.0.en.html
"""
import assembler
from appJar import gui

def press(button):
    if button == "Compile":
        assembler.compile(app.getEntry("input"), app.getEntry("output"))
    elif button == "Quit":
        app.stop()

app = gui()

app.addLabel("title", "Nomad Assembler")
app.addLabel("author", "Gabriel Russell 2019")
app.addLabel("license", "Licensed under the GPL v3")

app.addLabelEntry("input")
app.addLabelEntry("output")

app.addButtons(["Compile", "Quit"], press)

app.go()
