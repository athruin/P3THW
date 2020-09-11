def add(a, b):
    print(f"ADDING {a} + {b}.")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}.")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}.")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}.")
    return a / b

print("Let's do some math!")

age = add(25, 5)
height = subtract(78, 6)
weight = multiply(80, 2)
iq = divide(250, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}.")

print("And now, a puzzler.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print(f"That comes out to: {what}. Can you do it by hand?")
