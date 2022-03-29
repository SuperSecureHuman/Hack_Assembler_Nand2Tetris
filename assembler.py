# run assembler.py Mult.asm in cli

import sys

'''
Build Parser
'''

class parser:

    def __init__(self, inst):
        #Strip the instruction to remove leading and trailing spaces
        self.inst = inst.strip()
        #Storing the type of the instruction
        self.type = None
        #Calling the type check function
        self.CheckType()
    
    def CheckType(self):
        #If Else to check the starting character of the instruction
        #And setting the type of the instruction
        if self.inst.startswith('//') or self.inst == '':
            return
        if self.inst.startswith('('):
            self.type = 'L'
        elif self.inst.startswith('@'):
            self.type = 'A'
        else:
            self.type = 'C'
    
    def A_Value(self):
        #If inst is not A type, return none
        if self.type != 'A':
            return None
        # If its A type, then return the pure value of the instruction
        #I've used split to split the instruction into two parts, and take only the number part
        self.valueV = self.inst[1:].split(' ')[0]
        return self.valueV
        
    #Reading the file
    def main():
        #Uses python file handling to open file
        #The file name is taken from sys.argv, which is the command line arguments
        with open (sys.argv[1], 'r') as asm_file:
            #Reads the file line by line
            asm_lines = asm_file.readlines()
            #Printing lines
            
            for line in asm_lines:
                p = parser(line)
                if p.type == 'A':
                    print(p.A_Value())
                #print(p.type)

parser.main()