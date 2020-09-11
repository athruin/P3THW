people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should NOT take the cars.")
else:
    print("No decision can be made.")

if trucks > cars:
    print("That's too many freakin' trucks.")
elif trucks < cars:
    print("Perhaps the trucks are worth considering.")
else:
    print("Dang, we still can't decide!")

if people > trucks:
    print("Fine, let's take the damn trucks.")
else:
    print("Fuck it, we're staying home.")
