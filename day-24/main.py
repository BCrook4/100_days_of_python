# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("C:/Users/bento/OneDrive - The University of Western Ontario/Desktop/my_file.txt", mode= "a") as file:
#     file.write("\nNew text.")

with open("../../../../../../OneDrive - The University of Western Ontario/Desktop/my_file.txt", mode= "a") as file:
    file.write("\nNew text relative.")

with open("new_file.txt", mode= "w") as file:
    file.write("New file, new text.")