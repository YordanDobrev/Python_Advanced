import os

while True:
    command, *data = input().split("-")

    if command == "Create":
        with open(f"resources/{data[0]}", "w"):
            pass

    elif command == "Add":
        with open(f"resources/{data[0]}", "a") as file:
            file.write(f"{data[1]}\n")

    elif command == "Replace":
        try:
            with open(f"resources/{data[0]}", "r+") as file:
                new_text = file.read()
                new_text = new_text.replace(data[1], data[2])

                file.seek(0)
                file.write(new_text)
                file.truncate()

        except FileNotFoundError:
            print("File does not exist !")

    elif command == "Delete":
        try:
            os.remove(f"resources/{data[0]}")
        except FileNotFoundError:
            print("File does not exist for deletion !")
    elif command == "End":
        break
