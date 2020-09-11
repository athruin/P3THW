from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file already exist? {exists(to_file)}")
print("Ready to rock. Press RETURN to proceed or CTRL-C to cancel.")
input()

outdata = open(to_file, 'w').write(indata)

print("Alright! All done.")

exit()
