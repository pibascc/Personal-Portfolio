from math import *
import re, ast

# Main Program
def main():
    print("Type 'quit' to exit the program\n")
    while(True):
        inp = input('Calculator: ')
        if inp != '':
            if inp.lower() == 'quit': break
            else:
                try:
                    if not is_valid(inp): raise ValueError('input contains invalid characters')
                    else:
                        # Insert '*' between parentheses and numbers and replace '^' with '**'
                        expr = list(inp)
                        for i, char in enumerate(expr):
                            if char == '(':
                                try:
                                    if i - 1 < 0: raise IndexError
                                    float(expr[i - 1])
                                    expr.insert(i, '*')
                                except (IndexError, ValueError): continue
                            elif char == ')':
                                try:
                                    float(expr[i + 1])
                                    expr.insert(i + 1, '*')
                                except (IndexError, ValueError): continue
                            elif char == '^':
                                expr.pop(i)
                                expr.insert(i, '**')

                        # Evaluate
                        output = safe_eval(''.join(expr))
                        if output == None: raise ValueError("no output")
                        elif isinstance(output, (int, float)): print(f'\t= {smart_int(output)}\n')
                        else: print(f'{output}\n')
                except Exception as e: print(f"\tERROR - {e}\n")

# Functions
def is_valid(string): return re.search(r'^[\+\-\*\/\^\(\)\.\_\,0-9a-zA-Z]+$', ''.join(string.split())) != None
def smart_int(x: int | float):
    if isinstance(x, int): return x
    else:
        if x.is_integer(): x = int(x)
        return x
def root(index, radicand): return radicand ** (1/index)
def sum_args(*args): return sum(args) # Make sum() accept arguments
def prod_args(*args): return prod(args) # Make prod() accept arguments
def help(): return '\tAvailable Functions:\n\n' + ''.join([(f'\t{key}()\n') for key in allowed_functions.keys()])

def evaluate(node, variables):
    if isinstance(node, ast.Constant): return node.n
    elif isinstance(node, ast.Name): return variables.get(node.id, None)
    elif isinstance(node, ast.BinOp):
        left = evaluate(node.left, variables)
        right = evaluate(node.right, variables)
        if isinstance(node.op, ast.Add): return left + right
        elif isinstance(node.op, ast.Sub): return left - right
        elif isinstance(node.op, ast.Mult): return left * right
        elif isinstance(node.op, ast.Div): return left / right
        elif isinstance(node.op, ast.Pow): return left ** right
    elif isinstance(node, ast.UnaryOp):
        operand = evaluate(node.operand, variables)
        if isinstance(node.op, ast.UAdd): return operand
        elif isinstance(node.op, ast.USub): return -operand
    elif isinstance(node, ast.Call):
        func_name = node.func.id
        args = [evaluate(arg, variables) for arg in node.args]
        if func_name in allowed_functions: return allowed_functions[func_name](*args)
        else: raise ValueError(f"function '{func_name}' unrecognized or not allowed, use 'help()' for the list of functions")
    else: raise ValueError("invalid expression")
def safe_eval(expr, variables={}):
    parsed_expr = ast.parse(expr, mode='eval')
    return evaluate(parsed_expr.body, variables)

allowed_functions = {
    'abs': abs,
    'min': min, 'max': max,
    'round': round, 'ceil': ceil, 'floor': floor,
    'sum': sum_args, 'prod': prod_args,
    'sqrt': sqrt, 'root': root,
    'sin': sin, 'cos': cos, 'tan': tan,
    'factorial': factorial, 'perm': perm, 'comb': comb,
    'gcd': gcd, 'lcm': lcm,
    'help': help
}

main()