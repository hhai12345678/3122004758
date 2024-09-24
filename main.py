
import argparse
import random
import fractions

# 定义生成题目时使用的四种基本运算符
OPERATORS = ['+', '-', '*', '/']

# 生成一个分数，分母的最大值由max_denominator参数决定
def generate_fraction(max_denominator):
    denominator = random.randint(2, max_denominator)  # 随机生成分母，避免分母为1
    numerator = random.randint(1, denominator - 1)  # 随机生成分子，确保分子小于分母
    return fractions.Fraction(numerator, denominator)  # 返回一个分数对象

# 生成一个操作数，可以是整数或者分数
def generate_operand(max_range):
    if random.choice([True, False]):  # 随机选择生成整数或分数
        return str(random.randint(1, max_range - 1))  # 返回随机整数，避免整数为0
    else:
        fraction = generate_fraction(max_range)  # 生成一个分数
        return f"{fraction.numerator}/{fraction.denominator}"  # 返回分数形式的字符串

# 生成一个带有随机操作符的算术表达式，表达式中包含多个操作数和运算符
def generate_expression(max_range, max_operators):
    num_operators = random.randint(1, max_operators)  # 随机生成表达式中运算符的个数
    expression = generate_operand(max_range)  # 生成第一个操作数
    for _ in range(num_operators):
        operator = random.choice(OPERATORS)  # 随机选择一个运算符
        operand = generate_operand(max_range)  # 生成下一个操作数
        expression += f" {operator} {operand}"  # 将运算符和操作数添加到表达式中
    return expression  # 返回完整的表达式字符串

# 计算一个表达式的结果
def calculate_expression(expression):
    try:
        # 通过将字符串分割成单词来解析表达式，假设表达式格式正确
        tokens = expression.split()
        result = fractions.Fraction(tokens[0])  # 将第一个操作数转换为分数类型

        # 遍历剩余的运算符和操作数，并按顺序进行计算
        for i in range(1, len(tokens), 2):
            operator = tokens[i]  # 当前的运算符
            operand = fractions.Fraction(tokens[i + 1])  # 当前的操作数（以分数形式表示）

            # 根据运算符执行相应的操作
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                result /= operand  # 确保除法的结果是分数形式
        return result  # 返回计算结果，类型为Fraction
    except ZeroDivisionError:  # 捕捉除以零的情况
        return None  # 如果发生除以零，返回None表示无效的结果

# 生成指定数量的算术题目，并计算其答案
def generate_exercise(num_exercises, max_range, max_operators):
    exercises = []  # 存储生成的算术题目
    answers = []  # 存储对应的答案
    while len(exercises) < num_exercises:  # 循环直到生成所需数量的题目
        expression = generate_expression(max_range, max_operators)  # 生成一个题目
        result = calculate_expression(expression)  # 计算其答案
        if result is not None:  # 确保没有除以零的无效结果
            exercises.append(expression)  # 将题目添加到列表
            # 将答案转换为字符串形式，如果是整数则去掉分母
            answers.append(
                f"{result.numerator}/{result.denominator}" if result.denominator != 1 else str(result.numerator))
    return exercises, answers  # 返回题目和答案的列表

# 将题目或答案写入文件，每行一个
def write_to_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:  # 以写模式打开文件
        for line in lines:
            file.write(line + '\n')  # 每行写入一个字符串，并换行

# 从文件中读取内容，返回每行组成的列表
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:  # 以读模式打开文件
        return [line.strip() for line in file]  # 读取所有行，并去掉每行末尾的换行符

# 检查答案的正确性，将正确和错误的题目编号分别存储
def check_answers(exercise_file, answer_file):
    exercises = read_file(exercise_file)  # 从文件读取题目
    answers = read_file(answer_file)  # 从文件读取答案
    correct_indices = []  # 存储正确答案的题目编号
    wrong_indices = []  # 存储错误答案的题目编号

    # 遍历每个题目及其对应的用户答案
    for index, (exercise, user_answer) in enumerate(zip(exercises, answers), start=1):
        correct_answer = calculate_expression(exercise)  # 计算题目的正确答案
        correct_answer_str = f"{correct_answer.numerator}/{correct_answer.denominator}" if correct_answer.denominator != 1 else str(
            correct_answer.numerator)  # 将正确答案转换为字符串
        if user_answer == correct_answer_str:  # 检查用户答案是否正确
            correct_indices.append(index)  # 如果正确，记录题目编号
        else:
            wrong_indices.append(index)  # 如果错误，记录题目编号

    return correct_indices, wrong_indices  # 返回正确和错误的题目编号

# 将成绩（正确和错误的题目编号）写入文件
def write_grades(correct, wrong):
    with open('Grade.txt', 'w', encoding='utf-8') as file:  # 以写模式打开成绩文件
        file.write(f"Correct: {len(correct)} ({', '.join(map(str, correct))})\n")  # 写入正确的题目数量和编号
        file.write(f"Wrong: {len(wrong)} ({', '.join(map(str, wrong))})\n")  # 写入错误的题目数量和编号

# 程序主函数，处理命令行参数
def main():
    parser = argparse.ArgumentParser(description="Generate and check elementary arithmetic problems.")  # 创建参数解析器
    parser.add_argument('-n', type=int, help="Number of exercises to generate.")  # 生成题目的数量
    parser.add_argument('-r', type=int, help="Range of numbers in exercises.")  # 操作数的范围
    parser.add_argument('-e', type=str, help="Exercise file to check answers.")  # 用于检查的题目文件
    parser.add_argument('-a', type=str, help="Answer file to check answers.")  # 用于检查的答案文件

    args = parser.parse_args()  # 解析命令行参数

    # 如果提供了生成题目所需的参数，生成题目并保存到文件
    if args.n and args.r:
        exercises, answers = generate_exercise(args.n, args.r, 3)  # 生成题目和答案，最大操作符数量为3
        write_to_file('Exercises.txt', exercises)  # 将题目写入文件
        write_to_file('Answers.txt', answers)  # 将答案写入文件
        print(f"Generated {args.n} exercises with answers.")  # 打印生成题目的信息
    # 如果提供了检查答案的文件，检查答案并生成成绩
    elif args.e and args.a:
        correct, wrong = check_answers(args.e, args.a)  # 检查答案
        write_grades(correct, wrong)  # 写入成绩
        print("Checked answers and wrote grades to Grade.txt.")  # 打印检查完成的信息
    else:
        parser.print_help()  # 如果参数不完整，打印帮助信息

# 运行主函数
if __name__ == "__main__":
    main()
