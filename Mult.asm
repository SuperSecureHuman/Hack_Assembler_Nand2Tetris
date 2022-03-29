// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[3], respectively.)

   @i
   M=0 //This is a test comment
   @R2
   M=0

// Comment but in middle
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

(END) //Comment but in declaration
   @END
   0;JMP

//Comment but in end