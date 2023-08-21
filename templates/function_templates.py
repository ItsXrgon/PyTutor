import inspect

def generate_function_example(functions):
    out = ""
    for function in functions:
        if function in function_templates:
            template = function_templates[function]
            example = template.format("x", "y", "z")
            
            # Get the documentation for the function
            
            try:
                function_obj = eval(example)
                docstring = inspect.getdoc(function_obj)
            except:
                docstring = None
            finally:
                # Use the docstring if available, otherwise use the predefined explanation
                explanation = docstring if docstring else explanations.get(function, "No explanation available.")
            
            out += example + "\n" + explanation+ "\n\n"
    if out == "":
        return "Sorry, I don't know that function."
    return out
        

function_templates = {
    "print": "print('{}')",
    "len": "length = len({})",
    "input": "input('{}')",
    "int": "int({})",
    "float": "float({})",
    "str": "str({})",
    "bool": "bool({})",
    "list": "list({})", 
    "dict": "dict({})",
    "tuple": "tuple({})",
    "set": "set({})",
    "range": "range({})",
    "for": "for {} in {}:",
    "while": "while {}:",
    "if": "if {}:",
    "elif": "elif {}:",
    "else": "else:",
    "def": "def {}({}):",
    "class": "class {}({}):",
    "return": "return {}",
    "break": "break",
    "continue": "continue",
    "pass": "pass",
    "import": "import {}",
    "from": "from {} import {}",
    "as": "as {}",
    "try": "try:",
    "except": "except {}:",
    "finally": "finally:",
    "raise": "raise {}",
    "with": "with {} as {}:",
    "lambda": "lambda {}: {}",
    "global": "global {}",
    "nonlocal": "nonlocal {}",
    "del": "del {}",
    "assert": "assert {}",
    "yield": "yield {}",
    "in": "{} in {}",
    "not in": "{} not in {}",
    "is": "{} is {}",
    "is not": "{} is not {}",
    "and": "{} and {}",
    "or": "{} or {}",
    "not": "not {}",
    "if else": "{} if {} else {}",
    "if elif else": "{} if {} else {} if {} else {}",
    "for range": "for {} in range({}):",
    "for": "for {} in {}:",
    "while": "while {}:",
    "while else": "while {} else:",
    "try except": "try:\n\t{}except {}:\n\t\t{}",
    "try except else": "try:\n\t{}except {}:\n\t\t{}\n\telse:\n\t\t{}",
    "try except finally": "try:\n\t{}except {}:\n\t\t{}\n\tfinally:\n\t\t{}",
    "try except else finally": "try:\n\t{}except {}:\n\t\t{}\n\telse:\n\t\t{}\n\tfinally:\n\t\t{}",
    "range": "for i in range({}):"
}

explanations = {
    "print": "This function is used to print the provided value.",
    "len": "This function returns the length of the provided object.",
    "input": "This function takes user input and returns it as a string.",
    "int": "This function converts a value to an integer.",
    "float": "This function converts a value to a floating-point number.",
    "str": "This function converts a value to a string.",
    "bool": "This function converts a value to a boolean.",
    "list": "This function converts an iterable to a list.",
    "dict": "This function converts a sequence of key-value pairs to a dictionary.",
    "tuple": "This function converts an iterable to a tuple.",
    "set": "This function converts an iterable to a set.",
    "range": "This function generates a sequence of numbers within the specified range.",
    "for": "This loop iterates over the items in the provided iterable.",
    "while": "This loop repeatedly executes a block of code while a condition is true.",
    "if": "This statement performs a conditional check on a value.",
    "elif": "This statement is used to check additional conditions in an if statement.",
    "else": "This statement defines a block of code to execute if none of the previous conditions are met.",
    "def": "This keyword is used to define a new function.",
    "class": "This keyword is used to define a new class.",
    "return": "This statement returns a value from a function.",
    "break": "This statement exits the current loop prematurely.",
    "continue": "This statement skips the rest of the current iteration of a loop.",
    "pass": "This statement is a placeholder that does nothing."
}
