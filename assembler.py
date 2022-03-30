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
        self.RemoveCommentSpace()
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

    Output = Clean inst without space or comments
    """

    def RemoveCommentSpace(self):
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
        
        #This will remove all the space in a line
        self.inst = self.inst.replace(' ', '')


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

    """
    Takes in the instruction, checks if its C, or if it dosent have =
    If it is C, then it will return the dest part of the instruction.

    Input = self.inst

    Output = 
    """

    def dst(self):
        equalIndex = self.inst.find('=')
        if self.type != 'C' or equalIndex == -1:
            return
        else:
            self.destValue = self.inst[:equalIndex].strip()
        return self.destValue

    """
    This function takes in inst and returns comp part of the instruction.

    Input = self.inst

    Ouput = comp part of the instruction
    """

    def cmp(self):
        # Search for = and ;
        equalLocation = self.inst.find('=')
        semiColonLocation = self.inst.find(';')

        if self.type != 'C':
            return None
        # Checking through all the possible cases of = and ;, and getting the comp part of the instruction
        if equalLocation != -1 and semiColonLocation != -1:
            self.compValue = self.inst[equalLocation + 1 : semiColonLocation].strip()
        elif equalLocation != -1 and semiColonLocation == -1:
            self.compValue = self.inst[equalLocation+1:].strip()
        elif equalLocation == -1 and semiColonLocation != -1:
            self.compValue = self.inst[0:semiColonLocation].strip()
        elif equalLocation == -1 and semiColonLocation == -1:
            self.compValue = self.inst.strip()
        return self.compValue

    """
    This function takes in inst and returns comp part of the instruction.

    Input = self.inst

    Ouput = jump part of the instruction
    """
    def jump(self):
        semiColonLocation = self.inst.find(';')
        if self.type != 'C' or semiColonLocation == -1:
            return None        
        self.jumpValue = self.inst[semiColonLocation + 1 :].strip()
        return self.jumpValue

    # Reading the file

    def main():
        # Uses python file handling to open file
        # The file name is taken from sys.argv, which is the command line arguments
        # with open(sys.argv[1], 'r') as asm_file:
        with open('Mult.asm', 'r') as asm_file:
            # Reads the file line by line
            asm_lines = asm_file.readlines()
            # Printing lines

            for line in asm_lines:
                p = parser(line)
                if p.inst == '\n' or p.inst == '':
                    continue
                else:
                    print(p.inst)
                    print(p.type + ' instruction')
                    print(str(p.dst()) + ' destination')
                    print(str(p.cmp()) + ' comp')
                    print(str(p.jump()) + ' jump')
                    print('\n')

parser.main()
