# extracting the unique words from the input.txt file

# ---> give the actual path of the file
file_open = open("D:/python programs/18-unique-words-program/input.txt", "r")
line = file_open.read()

# convert to lower case words
lower_case = line.lower()

# exclude the space between words
split_words = lower_case.split()

# extract the unique words
unique_words = set(split_words)

# convert to list
set_to_list = list(unique_words)

# sorting
set_to_list.sort()

print(set_to_list)
