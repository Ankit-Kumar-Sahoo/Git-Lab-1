def fun1(x, y):
    """
    Performs addition operation on two numbers.
    
    Parameters:
        x (int/float): The first operand.
        y (int/float): The second operand.
    
    Returns:
        int/float: The sum of the two numbers.
    
    Raises:
        ValueError: When either input is not a valid number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    result = x + y
    return result


def fun2(x, y):
    """
    Performs subtraction operation on two numbers.
    
    Parameters:
        x (int/float): The minuend (number to subtract from).
        y (int/float): The subtrahend (number to be subtracted).
    
    Returns:
        int/float: The result of subtracting y from x.
    
    Raises:
        ValueError: When either input is not a valid number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    result = x - y
    return result


def fun3(x, y):
    """
    Performs multiplication operation on two numbers.
    
    Parameters:
        x (int/float): The first multiplicand.
        y (int/float): The second multiplicand.
    
    Returns:
        int/float: The product of the two numbers.
    
    Raises:
        ValueError: When either input is not a valid number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    result = x * y
    return result


def fun4(x, y, z):
    """
    Calculates the sum of three numbers.
    
    Parameters:
        x (int/float): The first number to add.
        y (int/float): The second number to add.
        z (int/float): The third number to add.
    
    Returns:
        int/float: The total sum of all three numbers.
    """
    total_sum = x + y + z
    return total_sum


def fun5(x, y):
    """
    Performs division operation on two numbers.
    
    Parameters:
        x (int/float): The dividend (number to be divided).
        y (int/float): The divisor (number to divide by).
    
    Returns:
        float: The quotient of dividing x by y.
    
    Raises:
        ValueError: When either input is not a valid number.
        ZeroDivisionError: When attempting to divide by zero.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    
    result = x / y
    return result


def fun6(x):
    """
    Calculates the square root of a number.
    
    Parameters:
        x (int/float): The number to find the square root of.
    
    Returns:
        float: The square root of the given number.
    
    Raises:
        ValueError: When input is not a valid number or is negative.
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a number.")
    
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    
    result = x ** 0.5
    return result