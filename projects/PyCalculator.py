from math import sqrt, prod, floor, ceil, sin, cos, tan, factorial, perm, comb, gcd, lcm, pi, tau, inf
import ast, string

valid_chars = string.ascii_letters + string.digits + string.whitespace + "+-*/^().,'\"" 
def main():
    # Main Program
    print("Type 'quit' to exit the program\n")
    while(True):
        inp = input('Calculator: ')
        if inp.strip() != '':
            if inp.lower() == 'quit': break
            else:
                try:
                    invalid_str = is_valid(inp, valid_chars)
                    if invalid_str != None:
                        if len(invalid_str) > 1: raise ValueError(f"invalid characters: '{invalid_str}'")
                        else: raise ValueError(f"invalid character: '{invalid_str}'")
                    else: print_output(safe_eval(refactor(inp)))
                except Exception as e: print(f"\n\tERROR - {e}\n")

# Functions
def is_valid(in_str: str, valid_chars: str) -> str | None:
    # Check if string contains valid characters and returns invalid characters
    # returns None if all characters are valid
    invalid_chars = []
    for char in in_str:
        if char not in valid_chars and char not in invalid_chars: invalid_chars.append(char)
    return ''.join(invalid_chars) if invalid_chars != [] else None
    
def print_output(output: str | int | float | None):
    if output != None:
        if isinstance(output, float):
            output = round(output, 10)
            print(f"\n\t= {output if not output.is_integer() else int(output)}\n")
        elif isinstance(output, int): print(f"\n\t= {output}\n")
        else: print(f'\n\t{output}\n')
def refactor(in_str: str):
    # Refactor input
    expr = list(in_str)
    for i, char in enumerate(expr):
        # Handle implicit multiplication
        if char == '(':
            try:
                if i - 1 < 0: raise IndexError
                float(expr[i - 1])
                expr.insert(i, '*')
            except ValueError:
                if expr[i - 1] == ')': expr.insert(i, '*')
            except IndexError: continue
        elif char == ')':
            try:
                float(expr[i + 1])
                expr.insert(i + 1, '*')
            except ValueError:
                if expr[i + 1] == '(': expr.insert(i + 1, '*')
            except IndexError: continue
        # Replace '^' with '**'
        elif char == '^': expr[i] = '**'
    return ''.join(expr)

def root(n, x):
    if n < 0 or x < 0: raise ValueError("math domain error")
    else: return x ** (1 / n)
def sum_of(*args): return sum(args)
def prod_of(*args): return prod(args)
def floor_to(x, n = 0):
    if isinstance(n, float): raise TypeError(f"'float' object cannot be interpreted as an integer")
    result = floor(x * 10 ** n) / 10 ** n
    return result if result != int(result) else int(result)
def ceil_to(x, n = 0):
    if isinstance(n, float): raise TypeError(f"'float' object cannot be interpreted as an integer")
    result = ceil(x * 10 ** n) / 10 ** n
    return result if result != int(result) else int(result)
def constants(constant_name: str = ''):
    if constant_name != '':
        if not isinstance(constant_name, str): raise TypeError("argument must be a string")
        if constant_name not in allowed_constants: raise ValueError("constant not found")
        return f"{constant_name} = {round(allowed_constants[constant_name]['constant'], 10)}\n\n{allowed_constants[constant_name]['definition']}\n"
    else: return 'Available Constants:\n\n' + ''.join([f"\t - {key}\n" for key in allowed_constants]) + f"\n\tUse 'constants{allowed_functions['constants']['signature']}' for more information about a constant\n"
def functions(function_name: str = ''):
    if function_name != '':
        if not isinstance(function_name, str): raise TypeError("argument must be a string")
        if function_name not in allowed_functions: raise ValueError("function not found")
        return f"Syntax: {function_name + allowed_functions[function_name]['signature']}\n\n{allowed_functions[function_name]['definition']}\n"
    else: return 'Available Functions:\n\n' + ''.join([f"\t - {key}\n" for key in allowed_functions]) + f"\n\tUse 'functions{allowed_functions['functions']['signature']}' for more information about a function\n"


def evaluate(node):
    if isinstance(node, ast.Constant): return node.value
    elif isinstance(node, ast.UnaryOp):
        operand = evaluate(node.operand)
        if isinstance(node.op, ast.UAdd): return operand
        elif isinstance(node.op, ast.USub): return -operand
        
    elif isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)
        if isinstance(node.op, ast.Add): return left + right
        elif isinstance(node.op, ast.Sub): return left - right
        elif isinstance(node.op, ast.Mult): return left * right
        elif isinstance(node.op, ast.Div): return left / right
        elif isinstance(node.op, ast.Pow): return left ** right

    elif isinstance(node, ast.Name):
        const_name = node.id
        if const_name in allowed_constants: return allowed_constants[const_name]['constant']
        else: raise ValueError(f"constant '{const_name}' unrecognized or not allowed, use 'constants()' for the list of constants")
    elif isinstance(node, ast.Call):
        func_name = node.func.id
        args = [evaluate(arg) for arg in node.args]
        if func_name in allowed_functions: return allowed_functions[func_name]['function'](*args)
        else: raise ValueError(f"function '{func_name}' unrecognized or not allowed, use 'functions()' for the list of functions")

    else: raise ValueError(f"invalid expression{node}")
def safe_eval(expr):
    parsed_expr = ast.parse(expr, mode='eval')
    return evaluate(parsed_expr.body)

allowed_constants = {
    'pi': {
        'constant': pi,
        'definition': " - the ratio of the circumference and diameter of a circle" 
    },
    'tau': {
        'constant': tau,
        'definition': " - the ratio of the circumference and radius of a circle" 
    },
    'inf': {
        'constant': inf,
        'definition': " - the floating-point value for positive infinity" 
    }
}

allowed_functions = {
    'abs': {
        'function': abs,
        'signature': '(x)',
        'definition': " - provides absolute value of 'x'"
    },
    'min': {
        'function': min,
        'signature': '(n1, n2, n3, ...)',
        'definition': " - provides the smallest number among the given numbers"
    },
    'max': {
        'function': max,
        'signature': '(n1, n2, n3, ...)',
        'definition': " - provides the largest number among the given numbers"
    },
    'round': {
        'function': round,
        'signature': '(x, n)',
        'definition': " - rounds 'x' to the 'n'th decimal place\n - returns an integer if 'n' is omitted"
    },
    'ceil': {
        'function': ceil_to,
        'signature': '(x, n)',
        'definition': " - rounds 'x' up to the 'n'th decimal place\n - returns an integer if 'n' is omitted"
    },
    'floor': {
        'function': floor_to,
        'signature': '(x, n)',
        'definition': " - rounds 'x' down to the 'n'th decimal place\n - returns an integer if 'n' is omitted"
    },
    'sum': {
        'function': sum_of,
        'signature': '(n1, n2, n3, ...)',
        'definition': " - provides the sum of the given numbers"
    },
    'prod': {
        'function': prod_of,
        'signature': '(n1, n2, n3, ...)',
        'definition': " - provides the product of the given numbers"
    },
    'sqrt': {
        'function': sqrt,
        'signature': '(x)',
        'definition': " - provides the square root of 'x'"
    },
    'root': {
        'function': root,
        'signature': '(n, x)',
        'definition': " - provides the 'n'th root of 'x'"
    },
    'sin': {
        'function': sin,
        'signature': '(x)',
        'definition': " - provides the sine of 'x'"
    },
    'cos': {
        'function': cos,
        'signature': '(x)',
        'definition': " - provides the cosine of 'x'"
    },
    'tan': {
        'function': tan,
        'signature': '(x)',
        'definition': " - provides the tangent of 'x'"
    },
    'factorial': {
        'function': factorial,
        'signature': '(x)',
        'definition': " - provides the factorial of 'x'"
    },
    'perm': {
        'function': perm,
        'signature': '(n, k)',
        'definition': " - provides the total possible permutations when picking 'k' items from a pool of 'n' items"
    },
    'comb': {
        'function': comb,
        'signature': '(n, k)',
        'definition': " - provides the total possible combinations when picking 'k' items from a pool of 'n' items"
    },
    'gcd': {
        'function': gcd,
        'signature': '(n1, n2, n3, ...)',
        'definition': " - provides the greatest common divisor of the given numbers"
    },
    'lcm': {
        'function': lcm,
        'signature': '(n1, n2, n3, ...)',
        'definition': " - provides the least common multiple of the given numbers"
    },
    'constants': {
        'function': constants,
        'signature': '(constant_name)',
        'definition': " - provides information about the given constant\n - if 'constant_name' is omitted, returns a list of available constants"
    },
    'functions': {
        'function': functions,
        'signature': '(function_name)',
        'definition': " - provides information about the given function\n - if 'function_name' is omitted, returns a list of available functions"
    }
}

main()