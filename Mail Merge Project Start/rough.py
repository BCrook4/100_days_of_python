with open("Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:

    for name in names:
        recipient = name.strip()

        with open(f"Output/ReadyToSend/letter_for_{recipient}.txt",mode= "w") as file:
            new_letter = letter_file.read()
            new_letter = new_letter.replace("[name]", f"{recipient}")
            new_letter = new_letter.replace("Angela", "Benton")
            file.write(new_letter.strip())