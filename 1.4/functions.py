def apply_function(data, func):
    
    return [func(x) for x in data]

# Example usage:
def multiplication(x):
    return x * 2

data = [1, 2, 3, 4, 5]
result = apply_function(data, multiplication)
print(result)

def apply_functions(data, *funcs):
   
    return [[func(x) for x in data] for func in funcs]

# Example usage:
def multiplication(x):
    return x * 2

def square(x):
    return x ** 2

data = [1, 2, 3, 4, 5]
results = apply_functions(data, multiplication, square)
print(results)
