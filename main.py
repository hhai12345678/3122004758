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


def calculate_expression(expression):
    try:
        return eval(expression, {"__builtins__": None}, {})
    except ZeroDivisionError:
        return None


def generate_exercise(num_exercises, max_range, max_operators):
    exercises = []
    answers = []
    while len(exercises) < num_exercises:
        expression = generate_expression(max_range, max_operators)
        result = calculate_expression(expression)
        if result is not None:
            exercises.append(expression)
            answers.append(str(result))
    return exercises, answers


def write_to_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


def check_answers(exercise_file, answer_file):
    exercises = read_file(exercise_file)
    answers = read_file(answer_file)
    correct_indices = []
    wrong_indices = []

    for index, (exercise, user_answer) in enumerate(zip(exercises, answers), start=1):
        correct_answer = str(calculate_expression(exercise))
        if user_answer == correct_answer:
            correct_indices.append(index)
        else:
            wrong_indices.append(index)

    return correct_indices, wrong_indices


def write_grades(correct, wrong):
    with open('Grade.txt', 'w', encoding='utf-8') as file:
        file.write(f"Correct: {len(correct)} ({', '.join(map(str, correct))})\n")
        file.write(f"Wrong: {len(wrong)} ({', '.join(map(str, wrong))})\n")


def main():
    parser = argparse.ArgumentParser(description="Generate and check elementary arithmetic problems.")
    parser.add_argument('-n', type=int, help="Number of exercises to generate.")
    parser.add_argument('-r', type=int, help="Range of numbers in exercises.")
    parser.add_argument('-e', type=str, help="Exercise file to check answers.")
    parser.add_argument('-a', type=str, help="Answer file to check answers.")

    args = parser.parse_args()

    if args.n and args.r:
        exercises, answers = generate_exercise(args.n, args.r, 3)
        write_to_file('Exercises.txt', exercises)
        write_to_file('Answers.txt', answers)
        print(f"Generated {args.n} exercises with answers.")
    elif args.e and args.a:
        correct, wrong = check_answers(args.e, args.a)
        write_grades(correct, wrong)
        print("Checked answers and wrote grades to Grade.txt.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
