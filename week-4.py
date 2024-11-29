try:
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("Welcome to week 4!")  # write "Welcome to week 4" to the file
except FileNotFoundError:  # Handle exception in case the file is not found
    print("File Not Found!")