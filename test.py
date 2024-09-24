import random
import unittest
import fractions
from io import StringIO
import sys
from main import (generate_fraction, generate_operand, generate_expression,
                              calculate_expression, generate_exercise, write_to_file, read_file,
                              check_answers)


class TestMathExercise(unittest.TestCase):

    def test_generate_fraction(self):
        fraction = generate_fraction(10)
        self.assertTrue(isinstance(fraction, fractions.Fraction))
        self.assertGreaterEqual(fraction.denominator, 2)
        self.assertGreaterEqual(fraction.numerator, 1)





    def test_generate_expression(self):
        random.seed(0)  # 固定随机种子保证生成结果一致
        expression = generate_expression(10, 3)
        self.assertTrue(any(op in expression for op in ['+', '-', '*', '/']))

    def test_calculate_expression_addition(self):
        expression = "1/2 + 1/2"
        result = calculate_expression(expression)
        self.assertEqual(result, fractions.Fraction(1, 1))

    def test_calculate_expression_subtraction(self):
        expression = "3/4 - 1/4"
        result = calculate_expression(expression)
        self.assertEqual(result, fractions.Fraction(1, 2))

    def test_calculate_expression_multiplication(self):
        expression = "2/3 * 3/4"
        result = calculate_expression(expression)
        self.assertEqual(result, fractions.Fraction(1, 2))

    def test_calculate_expression_division(self):
        expression = "2/3 / 4/5"
        result = calculate_expression(expression)
        self.assertEqual(result, fractions.Fraction(10, 12))

    def test_generate_exercise(self):
        exercises, answers = generate_exercise(5, 10, 3)
        self.assertEqual(len(exercises), 5)
        self.assertEqual(len(answers), 5)

    def test_check_answers(self):
        exercises = ["1/2 + 1/2", "3/4 - 1/4", "2/3 * 3/4", "2/3 / 4/5"]
        answers = ["1", "1/2", "1/2", "5/6"]

        # 模拟写入和读取文件
        with open('Exercises.txt', 'w') as f_ex:
            f_ex.write('\n'.join(exercises))

        with open('Answers.txt', 'w') as f_ans:
            f_ans.write('\n'.join(answers))

        correct, wrong = check_answers('Exercises.txt', 'Answers.txt')
        self.assertEqual(correct, [1, 2, 3, 4])
        self.assertEqual(wrong, [])

    def test_write_to_file(self):
        data = ["1 + 1", "2 - 2", "3 * 3", "4 / 4"]
        write_to_file("TestOutput.txt", data)

        read_back = read_file("TestOutput.txt")
        self.assertEqual(data, read_back)

    def test_read_file(self):
        data = ["5 + 5", "6 - 6"]
        write_to_file("TestRead.txt", data)
        read_back = read_file("TestRead.txt")
        self.assertEqual(data, read_back)


if __name__ == '__main__':
    unittest.main()
#


