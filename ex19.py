def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} units of cheese.")
    print(f"You have {boxes_of_crackers} boxes of crackers to pair with your vino.")

print("We can give the function numbers directly.")
cheese_and_crackers(20, 30)

print("Or, we can use variables from our script.")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Math is perfectly fine here.")
cheese_and_crackers(10 + 20, 5 + 6)

print("We can even use variables with our math!")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
