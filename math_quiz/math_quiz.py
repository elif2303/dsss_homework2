import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generate a random math operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])


def evaluate_expression(n1, n2, operator):
    """
    Evaluate an arithmetic expression and return both the expression and the answer.
    """
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    expression = f"{n1} {operator} {n2}"
    return expression, answer


def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = generate_random_integer(1, 10)
        n2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = evaluate_expression(n1, n2, operator)
        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
