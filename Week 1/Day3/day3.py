# open(filename)


from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("If you dont want to do that, press Ctrl + C")
print("Or press enter if you want to continue")

input("?")

print("Opening the file.....")
target = open(filename, "w")
print("Truncating the file now. Goodbye !")
target.truncate()

print("Now I'm going to ask you 3 lines")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write this into your file")

target.write(f"{line1}\n{line2}\n{line3}")

print("Done !")
target.close()
