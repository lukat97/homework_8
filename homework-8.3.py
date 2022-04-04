number_one = input("input first number")

number_two = input("input second number")

operation = input("which arithmetic operation do you want to use")

if operation == "+":
    print(int(number_one) + int(number_two))
elif operation == "-":
    print(int(number_one) - int(number_two))
elif operation == "*":
    print(int(number_one) * int(number_two))
elif operation == "/":
    print(int(number_one) / int(number_two))
else:
    print("I don't recognize that operation")



