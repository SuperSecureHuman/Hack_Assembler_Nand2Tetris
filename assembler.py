# run assembler.py Mult.asm in cli

import sys


#file = sys.argv[1]
file = "Mult.asm"

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

        # This will remove all the space in a line
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
            self.compValue = self.inst[equalLocation +
                                       1: semiColonLocation].strip()
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
        self.jumpValue = self.inst[semiColonLocation + 1:].strip()
        return self.jumpValue


class code:
    def __init__(self, term):
        self.term = term
        self.A_Value_Bin = None

    """
    Function to convert a given number into binary

    Input = Anything
    
    Ouput = Binary
    """

    def decToBin(self, dec):
        return format(dec, '016b')

    """
    Convert A value to binary, just uses the earlier defined function
    """

    def A_Value_Binary(self):
        if self.term == None:
            return None
        self.A_Value_Bin = self.decToBin(int(self.term))
        return self.A_Value_Bin

    """
    Convert C inst to binary. Just bunch of if else

    Input = Valid C destination

    Output = Hack assembly translation
    """

    def dst(self):
        if self.term == None:
            self.destBin = '000'
        elif self.term == 'M':
            self.destBin = '001'
        elif self.term == 'D':
            self.destBin = '010'
        elif self.term == 'MD':
            self.destBin = '011'
        elif self.term == 'A':
            self.destBin = '100'
        elif self.term == 'AM':
            self.destBin = '101'
        elif self.term == 'AD':
            self.destBin = '110'
        elif self.term == 'AMD':
            self.destBin = '111'
        return self.destBin

    """
    Another set of if else to read the cmp part of the instruction
    Then convert to assembly

    Input = CMP of the inst

    Ouput = Hack assembly translation
    """

    def cmp(self):
        a = '0'
        c = ''
        if self.term == None:
            self.compB = None
        elif self.term == '0':
            a = '0'
            c = '101010'
        elif self.term == '1':
            a = '0'
            c = '111111'
        elif self.term == '-1':
            a = '0'
            c = '111010'
        elif self.term == 'D':
            a = '0'
            c = '001100'
        elif self.term == 'A':
            a = '0'
            c = '110000'
        elif self.term == '!D':
            a = '0'
            c = '001101'
        elif self.term == '!A':
            a = '0'
            c = '110001'
        elif self.term == '-D':
            a = '0'
            c = '001111'
        elif self.term == '-A':
            a = '0'
            c = '110011'
        elif self.term == 'D+1':
            a = '0'
            c = '011111'
        elif self.term == 'A+1':
            a = '0'
            c = '110111'
        elif self.term == 'D-1':
            a = '0'
            c = '001110'
        elif self.term == 'A-1':
            a = '0'
            c = '110010'
        elif self.term == 'D+A':
            a = '0'
            c = '000010'
        elif self.term == 'D-A':
            a = '0'
            c = '010011'
        elif self.term == 'A-D':
            a = '0'
            c = '000111'
        elif self.term == 'D&A':
            a = '0'
            c = '000000'
        elif self.term == 'D|A':
            a = '0'
            c = '010101'
        elif self.term == 'M':
            a = '1'
            c = '110000'
        elif self.term == '!M':
            a = '1'
            c = '110001'
        elif self.term == '-M':
            a = '1'
            c = '110011'
        elif self.term == 'M+1':
            a = '1'
            c = '110111'
        elif self.term == 'M-1':
            a = '1'
            c = '110010'
        elif self.term == 'D+M':
            a = '1'
            c = '000010'
        elif self.term == 'D-M':
            a = '1'
            c = '010011'
        elif self.term == 'M-D':
            a = '1'
            c = '000111'
        elif self.term == 'D&M':
            a = '1'
            c = '000000'
        elif self.term == 'D|M':
            a = '1'
            c = '010101'
        self.cmpBin = a + c
        return self.cmpBin

    """
    Another set of if else to read the jump part of the instruction
    Then convert to assembly

    Input = jump of the inst

    Ouput = Hack assembly translation
    """

    def jump(self):
        if self.term == None:
            self.jmpBin = '000'
        elif self.term == 'JGT':
            self.jmpBin = '001'
        elif self.term == 'JEQ':
            self.jmpBin = '010'
        elif self.term == 'JGE':
            self.jmpBin = '011'
        elif self.term == 'JLT':
            self.jmpBin = '100'
        elif self.term == 'JNE':
            self.jmpBin = '101'
        elif self.term == 'JLE':
            self.jmpBin = '110'
        elif self.term == 'JMP':
            self.jmpBin = '111'
        return self.jmpBin
    

class passes:

    def __init__(self, symbol):
        self.symbol = symbol
    def firstPass(self):
        with open(file, 'r') as asm:
            lineNo = -1
            for inst in asm:
                p = parser(inst)
                if p.type == 'A' or p.type == 'C':
                    lineNo += 1
                if p.type == 'L':
                    sym = p.inst[1:-1]
                    if not self.symbol.CheckSymbolExist(sym):
                       self.symbol.AddSymbols(sym, lineNo+1)
    
    def secondPass(self):

        with open (file.split('.')[0] + '.hack', 'w') as hack:
            with open (file, 'r') as asm:
                variableLocation = 16
                for inst in asm:
                    input = parser(inst)
                    if input.type == 'A':
                        SYMBOL = input.inst[1:]
                        if self.symbol.CheckSymbolExist(SYMBOL):
                            out = code(self.symbol.GetSymbolValue(SYMBOL))
                            hack.write(out.A_Value_Binary() + '\n')
                        else:
                            try:
                                val = int(SYMBOL)
                                out = code(val)
                                hack.write(out.A_Value_Binary() + '\n')
                            except ValueError:
                                self.symbol.AddSymbols(SYMBOL, variableLocation)
                                out = code(variableLocation)
                                hack.write(out.A_Value_Binary() + '\n')
                                variableLocation += 1
                    elif input.type == 'C':
                        d = code(input.dst())
                        c = code(input.cmp())
                        j = code(input.jump())
                        hack.write('111'+c.cmp()+d.dst()+j.jump()+'\n') 




class symbol:
    def __init__(self):
        self.symbols = {}
        for MemReg in range(0, 16):
            self.symbols['R' + str(MemReg)] = MemReg
        self.symbols["SCREEN"] = 16384
        self.symbols["KBD"] = 24576
        self.symbols["SP"] = 0
        self.symbols["LCL"] = 1
        self.symbols["ARG"] = 2
        self.symbols["THIS"] = 3
        self.symbols["THAT"] = 4

    def CheckSymbolExist(self, symbol):
        if self.symbols.get(symbol) == None:
            return False
        else:
            return True
    def AddSymbols(self, symbol, value):
        self.symbols[symbol] = value
    def GetSymbolValue(self, symbol):
        return self.symbols.get(symbol)

def main():
    st = symbol()
    p = passes(st)
    p.firstPass()
    p.secondPass()

main()