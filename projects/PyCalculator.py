import re

def validate(string): return re.search(r"^[\+\-\*\/\^\(\)\.0-9]+$", "".join(string.split())) != None
def last_index(list, value): return len(list) - list[::-1].index(value) - 1
def num(x):
    if not isinstance(x, float): x = float(x)
    if x.is_integer(): x = int(x)
    return x
def operation(list, operator_index, func):
    start, end = operator_index - 1, operator_index + 1
    list.insert(start, str(num(func(num(list[start]), num(list[end])))))
    for i in range((end + 1) - start): list.pop(start + 1) 
def solve(string):
    if string == "": raise ValueError("input not valid: 'empty'")
    elif not validate(string): raise ValueError(f"input not valid: '{string}'")
    else: 
        formula = list(filter(None, re.split(r"([\+\-\*\/\^\(\)])", "".join(string.split()))))
        
        # Handle parenthesis
        if formula.count("(") != formula.count(")"):
            raise ValueError("missing parenthesis")
        while "(" in formula or ")" in formula:
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
            for i in range(len(formula[open_paren:close_paren + 1])): formula.pop(result_index + 1)
            try:
                float(formula[result_index - 1])
                formula.insert(result_index, "*")
                result_index += 1
            except: pass
            try:
                float(formula[result_index + 1])
                formula.insert(result_index + 1, "*")
            except: pass
        
        # Handle negatives
        formula = list(filter(None, re.split(r"([\+\-\*\/\^\(\)])", "".join(formula).strip("+*/^"))))
        while "-" in formula:
            minus = last_index(formula, "-")
            formula.insert(minus, str(num(formula[minus + 1]) * -1))
            for i in range(2): formula.pop(minus + 1)
            try:
                if minus - 1 < 0:
                    raise IndexError
                float(formula[minus - 1])
                formula.insert(minus, "+")
            except: continue
        
        # Handle operations
        while True:
            if "^" in formula: operation(formula, last_index(formula, "^"), lambda x, y: x ** y)
            elif "*" in formula: operation(formula, formula.index("*"), lambda x, y: x * y)
            elif "/" in formula: operation(formula, formula.index("/"), lambda x, y: x / y)
            elif "+" in formula: operation(formula, formula.index("+"), lambda x, y: x + y)
            else: return str(num("".join(formula))) 
    

print("Type \"quit\" to exit the program\n")
while(True):
    inp = input("Calculator: ")
    if inp.lower() == "quit": break
    else:
        try: print(f"\t= {solve(inp)}\n")
        except Exception as e: print(f"\tERROR - {e}\n")