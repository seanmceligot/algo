from typing import  List
import math

def parse_decimal(decimal: str) -> float:
    number: float = 0.0
    #add decimal .1 = 1*10^-1, .01=1*10^-2
    keep_decimal = True
    if keep_decimal:
        power:int = -1
        for ch in decimal:
            n:int = int(ch)
            print(f"{n} * 10^{power} ( {math.pow(10,power)} )")
            add:float = n*math.pow(10,power)
            #print(f"add {type(n)} {type(add)} {type(number)}")
            number = number + add
            power-=1
    print(f"{decimal} == {number}")
    return number

def parse_integer(integer:str) -> int:
    number: int = 0
    power:int = len(integer)-1
    for ch in integer:
        n:int = int(ch)
        print(f"{n} * 10^{power} ( {math.pow(10,power)} )")
        add:int = n*int(math.pow(10,power))
        #print(f"add {type(n)} {type(add)} {type(number)}")
        number = number + add
        power-=1
    print(f"{integer} == {number}")
    return number

def is_only_digits(s:str) -> bool:
    return len(s) == 0 or s.isdigit() 

def ignore_leading(s:str, index: int, size: int, chars: List[str]) -> int:
    while index < size and s[index] in chars: 
        index += 1
    return index
    
class Solution:
    def myAtoi(self, s:str) -> int:
        print(f"atoi: {s}")
        pos_neg = 1
        index = 0
        size: int = len(s)
        
        if index>=size:
            return 0
       
        index = ignore_leading(s, index, size, [' '])
        if index>=size:
            return 0

        # Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
        ch = s[index]
        if ch in ['+', '-']: 
            if ch == '+':
               pos_neg = 1
            if ch == '-':
               pos_neg = -1 
            index += 1
            if index>=size:
                return 0
            ch = s[index]
        # Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
        # Return the integer as the final result.
        if ch < '0' or ch > '9':
            return 0
        # Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
        only_digits_and_decimal = ""
        integer = ""
        while ch >= '0' and ch<= '9':
                integer += ch
                index+=1
                if index>=size:
                    break
                ch = s[index]
       
        decimal = ""
        if ch == '.':
            index+=1
            if index<size:
                while ch >= '0' and ch<= '9':
                        decimal += ch
                        index+=1
                        if index>=size:
                            break
                        ch = s[index]
         
        print(f"integer {integer}")
        print(f"decimal {decimal}")
        print(f"rest {s[index:]}")
        assert is_only_digits(integer)
        assert is_only_digits(decimal)
        if len(integer) == 0 and len(decimal) == 0:
            return 0
        # add number ones, tens, hundreds...
        number:float= 0 
        number = number + parse_integer(integer)
        number = number + parse_decimal(decimal)
        number *= pos_neg
        top = int(math.pow(2, 31))-1
        bottom = int(math.pow(-2, 31))
        number = min(number, top)
        number = max(number, bottom)
        print(f"result: {number}")
        return int(number)

solution = Solution()
if __name__ == "__main__":
   assert math.isclose(parse_decimal("123"), 0.123)
   assert solution.myAtoi("42") == 42 
   assert solution.myAtoi("-42") == -42 
   assert solution.myAtoi("  42") == 42 
   assert solution.myAtoi("  -42") == -42 
   assert solution.myAtoi("42 blah") == 42 
   assert solution.myAtoi("42.1") == 42
   assert solution.myAtoi("3.14159") == 3
   assert solution.myAtoi("+-12") == 0
   assert solution.myAtoi("+") == 0
   assert solution.myAtoi("") == 0
   assert solution.myAtoi("00000-42a1234") == 0
