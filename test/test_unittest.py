import sys
import os
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):
    
    def test_fun1(self):
        """Test addition function."""
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)
        self.assertEqual(calculator.fun1(10, 20), 30)
        self.assertAlmostEqual(calculator.fun1(5.5, 3.2), 8.7)
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            calculator.fun1("5", 3)
        with self.assertRaises(ValueError):
            calculator.fun1(5, None)
    
    def test_fun2(self):
        """Test subtraction function."""
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)
        self.assertEqual(calculator.fun2(10, 3), 7)
        self.assertAlmostEqual(calculator.fun2(10.5, 3.2), 7.3)
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            calculator.fun2("10", 3)
        with self.assertRaises(ValueError):
            calculator.fun2(10, [3])
    
    def test_fun3(self):
        """Test multiplication function."""
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)
        self.assertEqual(calculator.fun3(10, 4), 40)
        self.assertEqual(calculator.fun3(2.5, 4), 10.0)
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            calculator.fun3("5", 3)
        with self.assertRaises(ValueError):
            calculator.fun3(5, None)
    
    def test_fun4(self):
        """Test sum of three numbers function."""
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)
        self.assertEqual(calculator.fun4(0, 0, 0), 0)
        self.assertAlmostEqual(calculator.fun4(1.5, 2.5, 3.5), 7.5)
    
    def test_fun5(self):
        """Test division function."""
        self.assertEqual(calculator.fun5(10, 2), 5.0)
        self.assertEqual(calculator.fun5(15, 3), 5.0)
        self.assertEqual(calculator.fun5(-10, 2), -5.0)
        self.assertEqual(calculator.fun5(10, -2), -5.0)
        self.assertEqual(calculator.fun5(-10, -2), 5.0)
        self.assertAlmostEqual(calculator.fun5(7.5, 2.5), 3.0)
        self.assertEqual(calculator.fun5(0, 5), 0.0)
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            calculator.fun5(10, 0)
        with self.assertRaises(ZeroDivisionError):
            calculator.fun5(0, 0)
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            calculator.fun5("10", 2)
        with self.assertRaises(ValueError):
            calculator.fun5(10, "2")
    
    def test_fun6(self):
        """Test square root function."""
        self.assertEqual(calculator.fun6(4), 2.0)
        self.assertEqual(calculator.fun6(9), 3.0)
        self.assertEqual(calculator.fun6(16), 4.0)
        self.assertEqual(calculator.fun6(25), 5.0)
        self.assertEqual(calculator.fun6(0), 0.0)
        self.assertAlmostEqual(calculator.fun6(2), 1.414213, places=5)
        self.assertEqual(calculator.fun6(6.25), 2.5)
        
        # Test negative number
        with self.assertRaises(ValueError):
            calculator.fun6(-4)
        with self.assertRaises(ValueError):
            calculator.fun6(-1)
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            calculator.fun6("4")
        with self.assertRaises(ValueError):
            calculator.fun6(None)


if __name__ == '__main__':
    unittest.main()