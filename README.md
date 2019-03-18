# Nomad
Custom CPU made in Logisim. HCS Tech Fair 2019

# What makes Nomad Special?
Nomad is an Eight-Bit CPU designed entirely by myself.  
For those interested in developing software for it, there is a compiler available, although currently there is no formal documentation on the format of the language.

# What makes Nomad Unique?
It's made entirely by me. Some bulit-in components are used, but only to display the useful-ness of the language features.  
The lone fact that it was entirely designed by me makes it interesting, at least to me.

# What does Nomad feature?
ROM Storage: 256 * 16 Addressable Bits of Memory | 512 Bytes of ROM Program Storage   (soon to be upgraded to 2048 * 16 bits of ROM)  
RAM Storage: 256 * 08 Addressable Bits of Memory | 256 Bytes of Random Access Memory  
Registers: 016 * 08 Registers | 16 Bytes of Registers (12 RW, 4 R-)  
Input Methods: Keyboard, Switches, Buttons, Joystick  
Output Methods: Hexadecimal Display, Terminal Screen, LED Array

Operations: 
> Add  
> Subtract  
> AND   
> NOT  
> OR  
> XOR  
> LSL  
> LSR  
> Mov  
> LMR (Locate Memory to Register)  
> LRM (Locate Register to Memory)  
> JEQ  
> JNQ  
> JGT  
> JLT  
Most operations perform using the A and B registers as their inputs. NOT uses A.

Instructions are formatted as $op - $rs - $or. Operation, Register Select, Operand.  
In LMR and LRM, the operand is used to select an address. In the Jump operations, the Operand is the address to jump to. The register select is usually the place that is output to, although in LRM it is the input. Mov places the value in the operand in a register.  
Copying directly from a Register to another Register is not supported. If you wish to shift a register, move a value to memory, then copy it back to another register.

# What Programs have been made?
So far, only a few. I'm making a few sample programs that demonstrate the capabilities of Nomad though. I have not tested all features so far.

As of writing, the current programs are  
> Fibonnaci Sequence Printing (With no Overflow Protection)  
> Hello World  
> Python Output Test (Just another Hello World, ignore it)

# What other tools go along with Nomad?
I'm planning on writing some python scripts to simplify writing programs for Nomad, as they take quite a long time to write out by hand. Check the scripts folder for what's in so far.

# To-Do
- [ ] Extend Program Space

- [ ] Write more Sample Programs

- [x] Write a compiler

- [ ] Maybe an extension of the original operation set..?
