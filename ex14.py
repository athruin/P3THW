from sys import argv
script, user_name = argv
prompt = '> '

print(f"Hello {user_name}. I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print("Where do you reside, friend?")
location = input(prompt)

print("What kind of computer do I call home?")
pc = input(prompt)

print(f"""
So, you said this about me: {likes}.\nI'm not a very smart program, so I don't know if that's good or bad.\nI sure hope it's good!
You say you live in {location}. Again, I'm not very smart, so I don't know where that is. I hope you like it there.
And I'm running on a {pc}! Gotta say, I dig it here.
Ciao, {user_name}!
""")
