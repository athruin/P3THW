def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("This function doesn't have any arguments.")

print_two("Brandon", "Lee")
print_two_again("Brandon", "Lee")
print_one("Go Cubs go.")
print_none()
