# Hack assembler in python

Untill this is done, I'll be updating this with the latest code input and output.


## Current status

Now it can convert instructions to binary if the program dosent have symbols


Input add.asm

Output

```Java
@2
A instruction
None destination
None comp
None jump


2
0000000000000010
-------------------------- 

D=A
C instruction
D destination
A comp
None jump


dst part
D
010
cmp part
A
0110000
jump part
None
000
-------------------------- 

@3
A instruction
None destination
None comp
None jump


3
0000000000000011
-------------------------- 

D=D+A
C instruction
D destination
D+A comp
None jump


dst part
D
010
cmp part
D+A
0000010
jump part
None
000
-------------------------- 

@0
A instruction
None destination
None comp
None jump


0
0000000000000000
-------------------------- 

M=D
C instruction
M destination
D comp
None jump


dst part
M
001
cmp part
D
0001100
jump part
None
000
-------------------------- 


```