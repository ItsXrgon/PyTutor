import inspect

def generate_library_example(libraries):
    out = ""
    for library in libraries:
        if library in library_templates:
            template = library_templates[library]
            explanation = library_explanations.get(library, "No explanation available.")
            
            # Get the module object
            library_module = __import__(library)
            
            # Create a list of function names in the module
            function_names = [name for name, obj in inspect.getmembers(library_module) if inspect.isfunction(obj)]
            
            out += template + "\n" + explanation + "\n\n" + "Functions in this library: " + ", ".join(function_names) + "\n\n"
    if out == "":
        return "Sorry, I don't know that library."
    return out
            
    
library_templates = {
    "math": "import math\n\n# Example usage of math library functions:\nresult = math.sqrt(25)\nprint(result)",
    "random": "import random\n\n# Example usage of random library functions:\nrandom_number = random.randint(1, 100)\nprint(random_number)",
    "datetime": "import datetime\n\n# Example usage of datetime library functions:\ncurrent_time = datetime.datetime.now()\nprint(current_time)",
    "os": "import os\n\n# Example usage of os library functions:\nfile_list = os.listdir('.')\nprint(file_list)",
    "numpy": "import numpy as np\n\n# Example usage of numpy library:\narr = np.array([1, 2, 3])\nprint(arr)",
    "pandas": "import pandas as pd\n\n# Example usage of pandas library:\ndata = {'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']}\ndf = pd.DataFrame(data)\nprint(df)",
    "matplotlib": "import matplotlib.pyplot as plt\n\n# Example usage of matplotlib library:\nx = [1, 2, 3]\ny = [4, 5, 6]\nplt.plot(x, y)\nplt.show()",
}

library_explanations = {
    "math": "The math library provides various mathematical functions and constants.",
    "random": "The random library provides functions to generate random numbers and choices.",
    "datetime": "The datetime library offers classes for working with dates and times.",
    "os": "The os library provides functions for interacting with the operating system, including file operations.",
    "numpy": "The numpy library provides support for arrays and numerical computations.",
    "pandas": "The pandas library offers data structures and tools for data analysis and manipulation.",
    "matplotlib": "The matplotlib library is used for creating visualizations and plots.",
}
