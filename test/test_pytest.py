import sys
import os
import pytest

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))



from calculator import fun1, fun2, fun3, fun4, fun5, fun6


class TestFun1Addition:
    """Test cases for addition function."""
    
    def test_positive_numbers(self):
        assert fun1(5, 3) == 8
        assert fun1(10, 20) == 30
    
    def test_negative_numbers(self):
        assert fun1(-5, -3) == -8
        assert fun1(-10, 5) == -5
    
    def test_float_numbers(self):
        assert fun1(5.5, 3.2) == pytest.approx(8.7)
        assert fun1(0.1, 0.2) == pytest.approx(0.3)
    
    def test_zero(self):
        assert fun1(0, 5) == 5
        assert fun1(5, 0) == 5
        assert fun1(0, 0) == 0
    
    def test_invalid_input(self):
        with pytest.raises(ValueError, match="Both inputs must be numbers"):
            fun1("5", 3)
        with pytest.raises(ValueError):
            fun1(5, "3")
        with pytest.raises(ValueError):
            fun1(None, 5)


class TestFun2Subtraction:
    """Test cases for subtraction function."""
    
    def test_positive_numbers(self):
        assert fun2(10, 3) == 7
        assert fun2(20, 5) == 15
    
    def test_negative_result(self):
        assert fun2(3, 10) == -7
        assert fun2(5, 20) == -15
    
    def test_negative_numbers(self):
        assert fun2(-5, -3) == -2
        assert fun2(-10, 5) == -15
    
    def test_float_numbers(self):
        assert fun2(10.5, 3.2) == pytest.approx(7.3)
        assert fun2(0.5, 0.2) == pytest.approx(0.3)
    
    def test_zero(self):
        assert fun2(5, 0) == 5
        assert fun2(0, 5) == -5
        assert fun2(0, 0) == 0
    
    def test_invalid_input(self):
        with pytest.raises(ValueError, match="Both inputs must be numbers"):
            fun2("10", 3)
        with pytest.raises(ValueError):
            fun2(10, [3])


class TestFun3Multiplication:
    """Test cases for multiplication function."""
    
    def test_positive_numbers(self):
        assert fun3(5, 3) == 15
        assert fun3(10, 4) == 40
    
    def test_negative_numbers(self):
        assert fun3(-5, 3) == -15
        assert fun3(-5, -3) == 15
        assert fun3(5, -3) == -15
    
    def test_float_numbers(self):
        assert fun3(2.5, 4) == 10.0
        assert fun3(1.5, 2.5) == pytest.approx(3.75)
    
    def test_zero(self):
        assert fun3(0, 5) == 0
        assert fun3(5, 0) == 0
        assert fun3(0, 0) == 0
    
    def test_one(self):
        assert fun3(1, 5) == 5
        assert fun3(5, 1) == 5
    
    def test_invalid_input(self):
        with pytest.raises(ValueError, match="Both inputs must be numbers"):
            fun3("5", 3)
        with pytest.raises(ValueError):
            fun3(5, None)


class TestFun4SumOfThree:
    """Test cases for sum of three numbers function."""
    
    def test_positive_numbers(self):
        assert fun4(1, 2, 3) == 6
        assert fun4(10, 20, 30) == 60
    
    def test_negative_numbers(self):
        assert fun4(-1, -2, -3) == -6
        assert fun4(-10, 5, 3) == -2
    
    def test_float_numbers(self):
        assert fun4(1.5, 2.5, 3.5) == pytest.approx(7.5)
        assert fun4(0.1, 0.2, 0.3) == pytest.approx(0.6)
    
    def test_with_zeros(self):
        assert fun4(0, 0, 0) == 0
        assert fun4(5, 0, 3) == 8
        assert fun4(0, 5, 0) == 5
    
    def test_mixed_types(self):
        assert fun4(5, 2.5, 3) == 10.5
        assert fun4(1.1, 2, 3.3) == pytest.approx(6.4)


class TestFun5Division:
    """Test cases for division function."""
    
    def test_positive_numbers(self):
        assert fun5(10, 2) == 5.0
        assert fun5(15, 3) == 5.0
    
    def test_negative_numbers(self):
        assert fun5(-10, 2) == -5.0
        assert fun5(10, -2) == -5.0
        assert fun5(-10, -2) == 5.0
    
    def test_float_numbers(self):
        assert fun5(7.5, 2.5) == pytest.approx(3.0)
        assert fun5(10.0, 4.0) == 2.5
    
    def test_result_with_decimal(self):
        assert fun5(10, 3) == pytest.approx(3.333333, rel=1e-5)
        assert fun5(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            fun5(10, 0)
        with pytest.raises(ZeroDivisionError):
            fun5(0, 0)
    
    def test_zero_dividend(self):
        assert fun5(0, 5) == 0.0
        assert fun5(0, -5) == 0.0
    
    def test_invalid_input(self):
        with pytest.raises(ValueError, match="Both inputs must be numbers"):
            fun5("10", 2)
        with pytest.raises(ValueError):
            fun5(10, "2")


class TestFun6SquareRoot:
    """Test cases for square root function."""
    
    def test_perfect_squares(self):
        assert fun6(4) == 2.0
        assert fun6(9) == 3.0
        assert fun6(16) == 4.0
        assert fun6(25) == 5.0
    
    def test_non_perfect_squares(self):
        assert fun6(2) == pytest.approx(1.414213, rel=1e-5)
        assert fun6(3) == pytest.approx(1.732050, rel=1e-5)
        assert fun6(10) == pytest.approx(3.162277, rel=1e-5)
    
    def test_zero(self):
        assert fun6(0) == 0.0
    
    def test_float_numbers(self):
        assert fun6(6.25) == 2.5
        assert fun6(2.25) == 1.5
    
    def test_negative_number(self):
        with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
            fun6(-4)
        with pytest.raises(ValueError):
            fun6(-1)
    
    def test_invalid_input(self):
        with pytest.raises(ValueError, match="Input must be a number"):
            fun6("4")
        with pytest.raises(ValueError):
            fun6(None)
        with pytest.raises(ValueError):
            fun6([4])