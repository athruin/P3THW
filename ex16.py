from sys import argv

script, filename = argv

print(f"We're going to clobber (erase) {filename}.\nIf you don't want that, press CTRL-C.\nIf you do, you sick bastard, press RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file.")
target.truncate()

print("Truncation complete! Now I need three lines.")
line1 = input("The first: ")
line2 = input("The second: ")
line3 = input("And the third: ")

print("I'm going to write these lines to the file we deleted.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"Closing the file. Go check my work!\nNotice how this fails (silently!) if the file is in use by another process?\nMore on that later.")
target.close()

exit()
