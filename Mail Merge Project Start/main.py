#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_template = letter_file.read()
    for name in names:
        recipient = name.strip()

        with open(f"Output/ReadyToSend/letter_for_{recipient}.txt",mode= "w") as file:
            # new_letter = letter_file.read()
            new_letter = letter_template.replace("[name]", f"{recipient}")
            new_letter = new_letter.replace("Angela", "Benton")
            file.write(new_letter.strip())