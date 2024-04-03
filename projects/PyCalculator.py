import re

def validate(string): return re.search(r"^[\+\-\*\/\^\(\)\.0-9]+$", "".join(string.split())) != None
def sint(x):
    x = float(x)
    if x.is_integer(): return int(x)
    else: return x
def last_index(list, value):
    return len(list) - list[::-1].index(value) - 1

def add(num1 = 0, num2 = 0): return sint(num1 + num2)
def subtract(num1 = 0, num2 = 0): return sint(num1 - num2)
def multiply(num1 = 1, num2 = 1): return sint(num1 * num2)
def divide(num1 = 1, num2 = 1): return sint(num1 / num2)
def exponent(num1 = 1, num2 = 1): return sint(num1 ** num2)

def operation(list, operator_index, func):
    start, end = operator_index - 1, operator_index + 1
    after_result = start + 1
    list.insert(start, str(func(float(list[start]), float(list[end]))))
    for i in range((end + 1) - start): list.pop(after_result)
    
def solve(string):
    if string == "": raise ValueError(f"input not valid: '{string}'")
    elif not validate(string): raise ValueError("input not valid: 'empty'")
    else: 
        formula = list(filter(None, re.split(r"([\+\-\*\/\^\(\)])", "".join(string.split()))))
        if formula.count("(") != formula.count(")"):
            raise ValueError("missing parenthesis")
        while formula.count("(") > 0 and formula.count(")") > 0:
            open_paren = formula.index("(")
            close_paren = open_paren
            open_paren_count, close_paren_count = 0, 0
            for i, item in enumerate(formula):
                if item == "(": open_paren_count += 1
                elif item == ")":
                    close_paren_count +=1
                    if open_paren_count == close_paren_count:
                        close_paren = i
                        break
            formula.insert(open_paren, solve("".join(formula[open_paren + 1:close_paren])))
            result_index = open_paren
            for i in range(len(formula[open_paren:close_paren + 1])): formula.pop(open_paren + 1)
            try:
                float(formula[result_index - 1])
                formula.insert(result_index, "*")
                result_index += 1
            except: pass
            try:
                float(formula[result_index + 1])
                formula.insert(result_index + 1, "*")
            except: pass
            formula = list(filter(None, re.split(r"([\+\-\*\/\^\(\)])", "".join(formula).strip("+-*/^"))))
        
        while True:
            if "^" in formula: operation(formula, last_index(formula, "^"), exponent)
            elif "*" in formula: operation(formula, formula.index("*"), multiply)
            elif "/" in formula: operation(formula, formula.index("/"), divide)
            elif "+" in formula: operation(formula, formula.index("+"), add)
            elif "-" in formula: operation(formula, formula.index("-"), subtract)
            else: return str(sint("".join(formula))) 
    

print("Type \"quit\" to exit the program\n")
while(True):
    inp = input("Calculator: ")
    if inp.lower() == "quit": break
    else:
        try: print(f"\t= {solve(inp)}\n")
        except Exception as e: print(f"\tERROR - {e}\n")