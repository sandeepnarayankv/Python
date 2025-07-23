import random

def ask_question():

    symbols = ["*", "+", "-", "/", "**"]

    while True:
        num1 = random.randint(0, 100)
        num2 = random.randint(1, 100)
        symbol = random.choice(symbols)

        print(f"Question: {num1} {symbol} {num2}")

        answer = float(input("Answer: "))
        correct_answer : float = 0

        match symbol:
            case "+":
                correct_answer = num1 + num2
            case "-":
                correct_answer = num1 - num2
            case "*":
                correct_answer = num1 * num2
            case "/":
                correct_answer = num1 / num2
            case "**":
                correct_answer = num1 ** num2

        if answer != correct_answer:
            print (f"Your Answer is incorrect, Correct Answer: {correct_answer}, Exiting")        
            break
        else:
            print("Correct Answer, Great Going!!")


if __name__ == "__main__":
    ask_question()