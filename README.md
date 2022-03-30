# Hack assembler in python

Untill this is done, I'll be updating this with the latest code input and output.


## Current status

I think parser is fully done.

I added some random comments, added unwanted space between some inst, and it removed them all.



Input Mult.asm

Output

```Java
@i
A instruction
None destination
None comp
None jump


M=0
C instruction
M destination
0 comp
None jump


@R2
A instruction
None destination
None comp
None jump


M=0
C instruction
M destination
0 comp
None jump


(LOOP)
L instruction
None destination
None comp
None jump


@R1
A instruction
None destination
None comp
None jump


D=M
C instruction
D destination
M comp
None jump


@i
A instruction
None destination
None comp
None jump


D=D-M
C instruction
D destination
D-M comp
None jump


@END
A instruction
None destination
None comp
None jump


D;JEQ
C instruction
None destination
D comp
JEQ jump


@R0
A instruction
None destination
None comp
None jump


D=M
C instruction
D destination
M comp
None jump


@R2
A instruction
None destination
None comp
None jump


M=D+M
C instruction
M destination
D+M comp
None jump


@1
A instruction
None destination
None comp
None jump


D=A
C instruction
D destination
A comp
None jump


@i
A instruction
None destination
None comp
None jump


M=D+M
C instruction
M destination
D+M comp
None jump


@LOOP
A instruction
None destination
None comp
None jump


0;JMP
C instruction
None destination
0 comp
JMP jump


(END)
L instruction
None destination
None comp
None jump


@END
A instruction
None destination
None comp
None jump


0;JMP
C instruction
None destination
0 comp
JMP jump

```