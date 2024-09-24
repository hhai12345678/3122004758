import random
import unittest
import fractions
from io import StringIO
import sys
from main import (generate_fraction, generate_operand, generate_expression,
                  calculate_expression, generate_exercise, write_to_file, read_file,
                  check_answers)


class TestMathExercise(unittest.TestCase):
    """
    TestMathExercise类用于测试与数学练习生成相关的函数。
    """

    def test_generate_fraction(self):
        """
        测试生成分数函数 generate_fraction(n) 是否返回合法的 fractions.Fraction 实例。
        分子应当大于等于 1，分母应当大于等于 2。
        """
        fraction = generate_fraction(10)
        self.assertTrue(isinstance(fraction, fractions.Fraction))  # 检查生成结果是否为 Fraction 实例
        self.assertGreaterEqual(fraction.denominator, 2)  # 检查分母是否符合条件
        self.assertGreaterEqual(fraction.numerator, 1)  # 检查分子是否符合条件

    def test_generate_expression(self):
        """
        测试生成表达式函数 generate_expression(max_value, num_operands)。
        确保生成的表达式中包含加减乘除运算符。
        使用固定随机种子以保证测试结果一致。
        """
        random.seed(0)  # 固定随机种子以保证测试的可重复性
        expression = generate_expression(10, 3)
        # 确保表达式中至少包含一个四则运算符号
        self.assertTrue(any(op in expression for op in ['+', '-', '*', '/']))

    def test_calculate_expression_addition(self):
        """
        测试计算表达式的函数 calculate_expression(expression) 对加法表达式的处理。
        例如： "1/2 + 1/2" 应该返回 1。
        """
        expression = "1/2 + 1/2"
        result = calculate_expression(expression)
        self.assertEqual(result, fractions.Fraction(1, 1))  # 检查结果是否为1

    def test_calculate_expression_subtraction(self):
        """
        测试 calculate_expression(expression) 对减法表达式的处理。
        例如："3/4 - 1/4" 应该返回 1/2。
        """
        expression = "3/4 - 1/4"
        result = calculate_expression(expression)
        self.assertEqual(result, fractions.Fraction(1, 2))  # 检查结果是否为1/2

    def test_calculate_expression_multiplication(self):
        """
        测试 calculate_expression(expression) 对乘法表达式的处理。
        例如："2/3 * 3/4" 应该返回 1/2。
        """
        expression = "2/3 * 3/4"
        result = calculate_expression(expression)
        self.assertEqual(result, fractions.Fraction(1, 2))  # 检查结果是否为1/2

    def test_calculate_expression_division(self):
        """
        测试 calculate_expression(expression) 对除法表达式的处理。
        例如："2/3 / 4/5" 应该返回 10/12 (即 5/6)。
        """
        expression = "2/3 / 4/5"
        result = calculate_expression(expression)
        self.assertEqual(result, fractions.Fraction(10, 12))  # 检查结果是否为10/12

    def test_generate_exercise(self):
        """
        测试生成练习题函数 generate_exercise(num_exercises, max_value, num_operands)。
        确保生成的练习题数目与答案数目都符合预期（即 num_exercises 个）。
        """
        exercises, answers = generate_exercise(5, 10, 3)
        self.assertEqual(len(exercises), 5)  # 检查生成的练习题数量是否正确
        self.assertEqual(len(answers), 5)  # 检查生成的答案数量是否正确

    def test_check_answers(self):
        """
        测试检查答案的函数 check_answers(exercise_file, answer_file)。
        这里通过创建包含四个算式的文件，然后检查答案是否全部正确。
        """
        exercises = ["1/2 + 1/2", "3/4 - 1/4", "2/3 * 3/4", "2/3 / 4/5"]
        answers = ["1", "1/2", "1/2", "5/6"]

        # 模拟写入“练习题”和“答案”文件
        with open('Exercises.txt', 'w') as f_ex:
            f_ex.write('\n'.join(exercises))

        with open('Answers.txt', 'w') as f_ans:
            f_ans.write('\n'.join(answers))

        # 调用 check_answers 函数检查答案
        correct, wrong = check_answers('Exercises.txt', 'Answers.txt')
        self.assertEqual(correct, [1, 2, 3, 4])  # 检查是否所有答案都正确
        self.assertEqual(wrong, [])  # 检查是否没有错误答案

    def test_write_to_file(self):
        """
        测试写文件函数 write_to_file(filename, data)。
        确保文件中写入的数据与原始数据相同。
        """
        data = ["1 + 1", "2 - 2", "3 * 3", "4 / 4"]
        write_to_file("TestOutput.txt", data)

        # 读取文件并验证内容是否正确
        read_back = read_file("TestOutput.txt")
        self.assertEqual(data, read_back)  # 检查文件内容是否与原始数据一致

    def test_read_file(self):
        """
        测试读文件函数 read_file(filename)。
        确保从文件中读取的数据与原始写入的数据相同。
        """
        data = ["5 + 5", "6 - 6"]
        write_to_file("TestRead.txt", data)
        read_back = read_file("TestRead.txt")
        self.assertEqual(data, read_back)  # 检查读取的数据是否正确


if __name__ == '__main__':
    unittest.main()



