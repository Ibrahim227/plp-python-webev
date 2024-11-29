try:
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("Welcome to week 4!")
except FileNotFoundError:
    print("File Not Found!")