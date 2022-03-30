# Hack assembler in python

Untill this is done, I'll be updating this with the latest code input and output.


## Current status

Input Mult.asm

Output

```Java
@i
M=0
@R2
M=0
(LOOP)
@R1
D=M
@i
D=D-M
@END
D;JEQ
@R0
D=M
@R2
M=D+M
@1
D=A
@i
M=D+M
@LOOP
0;JMP
(END)
@END
0;JMP
```