import argparse
import random
import fractions

# 定义生成题目所需的常量和函数
OPERATORS = ['+', '-', '*', '/']


def generate_fraction(max_denominator):
    denominator = random.randint(2, max_denominator)
    numerator = random.randint(1, denominator - 1)
    return fractions.Fraction(numerator, denominator)


def generate_operand(max_range):
    if random.choice([True, False]):
        return str(random.randint(0, max_range - 1))
    else:
        fraction = generate_fraction(max_range)
        return f"{fraction.numerator}/{fraction.denominator}"


def generate_expression(max_range, max_operators):
    num_operators = random.randint(1, max_operators)
    expression = generate_operand(max_range)
    for _ in range(num_operators):
        operator = random.choice(OPERATORS)
        operand = generate_operand(max_range)
        expression += f" {operator} {operand}"
    return expression


