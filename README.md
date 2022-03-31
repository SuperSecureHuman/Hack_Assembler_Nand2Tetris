# Hack assembler in python

Untill this is done, I'll be updating this with the latest code input and output.


## Current status

Now it can convert instructions to binary if the program dosent have symbols.

Additionally, now it goes through the program and checks for new labels. Also adds them into the table.


Input add.asm

Output

```Java
@2
0000000000000010
-------------------------- 

D=A
1110100110000000
-------------------------- 

@3
0000000000000011
-------------------------- 

D=D+A
1110100000010000
-------------------------- 

@0
0000000000000000
-------------------------- 

M=D
1110010001100000
-------------------------- 

(var)
D=M
1110101110000000
-------------------------- 

R0	0
R1	1
R2	2
R3	3
R4	4
R5	5
R6	6
R7	7
R8	8
R9	9
R10	10
R11	11
R12	12
R13	13
R14	14
R15	15
SCREEN	16384
KBD	24576
SP	0
LCL	1
ARG	2
THIS	3
THAT	4
var	6


```