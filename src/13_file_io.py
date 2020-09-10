"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('./foo.txt') as f:
    read_data = f.read()

    print(read_data)



# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f = open('./bar.txt', 'a')
f.write('Water. Earth. Fire. Air.\nLong ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.\nOnly the Avatar, master of all four elements, could stop them. But when the world needed him most, he vanished.\nA hundred years passed and my brother and I discovered the new Avatar, an airbender named Aang, and although his airbending skills are great, he still has a lot to learn before he\'s ready to save anyone.\nBut I believe Aang can save the world.\n')
f.close()

with open('./bar.txt') as b:
    read_data = b.read()

    print(read_data)