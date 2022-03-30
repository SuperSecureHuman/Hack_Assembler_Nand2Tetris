# run assembler.py Mult.asm in cli

import sys

'''
Build Parser
'''


class parser:

    def __init__(self, inst):
        # Strip the instruction to remove leading and trailing spaces
        self.inst = inst.strip()
        # Storing the type of the instruction
        self.type = None
        # Calling the type check function
        self.RemoveComment()
        self.CheckType()

    """
    This function check the type of the passed in instruction and returns the type.

    Input = self.inst

    Output = self.type (A, C, L)
    """
    def CheckType(self):
        # If Else to check the starting character of the instruction
        # And setting the type of the instruction
        if self.inst.startswith('//') or self.inst == '':
            return
        if self.inst.startswith('('):
            self.type = 'L'
        elif self.inst.startswith('@'):
            self.type = 'A'
        else:
            self.type = 'C'


    """
    Read A value, and return the value only
    This function splits the comments, and returns only the needed part
    Input = A inst (if u input something else, it will ignore)

    Output = A inst value (stuff after @)
    """
    def A_Value(self):
        # If inst is not A type, return none
        if self.type != 'A':
            return None
        # If its A type, then return the pure value of the instruction
        # I've used split to split the instruction into two parts, and take only the number part
        self.valueA = self.inst[1:].split(' ')[0]
        return self.valueA

    """
    Takes the instruction as input, locates the comment string, and strips based on it.
    Additionally, it strips the whitespaces.

    Input = self.inst

    Output = Clean inst without ending space or comments
    """

    def RemoveComment(self):
        self.inst = self.inst.strip()
        CommentLoc = self.inst.find('//')
        # If the comment is not found, return the instruction as it is
        # find() returns -1 if the string is not found
        if CommentLoc == -1:
            self.inst = self.inst.strip()
        # If the first location is a //, then return blank string
        elif CommentLoc == 0:
            self.inst = ''
        # If the comment is found, then return the instruction without the comment
        else:
            self.inst = self.inst[:CommentLoc].strip()

    """
    Function to return true for blank lines
    """
    def RemoveBlankLine(self):
        # If the instruction is blank, return blank string
        if self.inst == '':
            return True
        # If the instruction is not blank, then return the instruction as it is
        else:
            return self.inst

    def dst(self):
        pass

    # Reading the file
    def main():
        # Uses python file handling to open file
        # The file name is taken from sys.argv, which is the command line arguments
        #with open(sys.argv[1], 'r') as asm_file:
        with open('Mult.asm', 'r') as asm_file:
            # Reads the file line by line
            asm_lines = asm_file.readlines()
            # Printing lines

            for line in asm_lines:
                p = parser(line)
                if p.inst == '\n' or p.inst == '':
                    continue
                else:
                    if p.type == 'A':
                        
                        print(p.inst)
                        print(p.type + ' Type Inst With A Value of ' + p.A_Value())
                    else:    
                        print(p.inst)
                        print(p.type + ' Type Inst')
                        print('')
parser.main()