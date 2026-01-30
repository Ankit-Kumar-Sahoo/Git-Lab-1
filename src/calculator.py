def fun1(x, y):

    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    result = x + y
    return result


def fun2(x, y):
    
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    result = x - y
    return result


def fun3(x, y):
    
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    result = x * y
    return result


def fun4(x, y, z):
    
    total_sum = x + y + z
    return total_sum


def fun5(x, y):
    
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    
    result = x / y
    return result


def fun6(x):
    
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a number.")
    
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    
    result = x ** 0.5
    return result