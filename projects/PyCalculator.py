import re

class Calculator:
    @classmethod
    def validate(cls, string):
        valid_chars = "+-*/^().1234567890"
        text = "".join(string.split())
        for char in text:
            if char not in valid_chars:
                return False
        return True
    
    @classmethod
    def add(cls, num1 = 0, num2 = 0):
        return num1 + num2
    @classmethod
    def subtract(cls, num1 = 0, num2 = 0):
        return num1 - num2
    @classmethod
    def multiply(cls, num1 = 1, num2 = 1):
        return num1 * num2
    @classmethod
    def divide(cls, num1 = 1, num2 = 1):
        return num1 / num2
    @classmethod
    def exponent(cls, num1 = 1, num2 = 1):
        return num1 ** num2

    @classmethod
    def operation(cls, list, start, end, func):
        x = start + 1
        list.insert(start, str(func(float(list[start]), float(list[end]))))
        for i in range(end - start + 1):
            list.pop(x)

    @classmethod
    def solve(cls, string):
        if cls.validate(string):
            no_open_paren = False
            no_close_paren = False
            string = "".join(string.split())
            formula = re.split(r"([\+\-\*\/\^\(\)])", string)
            formula = list(filter(None, formula))
            try:
                open_paren = formula.index("(")
            except:
                no_open_paren = True
            try:
                close_paren = len(formula) - formula[-1::-1].index(")") - 1
            except:
                no_close_paren = True
            if not no_open_paren and not no_close_paren:
                formula.insert(open_paren, "*")
                formula.insert(open_paren, cls.solve("".join(formula[open_paren + 2:close_paren + 1])))
                formula.insert(open_paren, "*")
                for i in range(len(formula[open_paren:close_paren + 1])):
                    formula.pop(open_paren + 3)
            formula = re.split(r"([\+\-\*\/\^\(\)])", "".join(formula).strip("+-*/^"))
            while(True):
                sym = 0
                if "^" in formula:
                    try:
                        sym = formula.index("^")
                    except:
                        pass
                    cls.operation(formula, sym - 1, sym + 1, cls.exponent)
                elif "*" in formula:
                    try:
                        sym = formula.index("*")
                    except:
                        pass
                    cls.operation(formula, sym - 1, sym + 1, cls.multiply)
                elif "/" in formula:
                    try:
                        sym = formula.index("/")
                    except:
                        pass
                    cls.operation(formula, sym - 1, sym + 1, cls.divide)
                elif "+" in formula:
                    try:
                        sym = formula.index("+")
                    except:
                        pass
                    cls.operation(formula, sym - 1, sym + 1, cls.add)
                elif "-" in formula:
                    try:
                        sym = formula.index("-")
                    except:
                        pass
                    cls.operation(formula, sym - 1, sym + 1, cls.subtract)
                else:
                    result = float("".join(formula))
                    if result.is_integer():
                        result = int(result)
                    return str(result) 
        else:
            raise ValueError(f"character not valid: '{string}'")

print("Type \"quit\" to exit the program\n")
while(True):
    inp = input("Calculator: ")
    if inp.lower() == "quit":
        break
    else:
        try:
            print(f"\t= {Calculator.solve(inp)}\n")
        except Exception as e:
            print(f"\tERROR - {e}\n")