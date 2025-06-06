file = None

try:
    file = open("numbers.txt", "r")
    for line in file:
        try:
            number = float(line.strip())
            print(f"Read number: {number}")

        except ValueError:
            print(f"Skipping invalid line: {line.strip()}")

        except FileNotFoundError:
            print(f"Error: File not found.")

finally:
    if file:
        file.close()
        print("File closed.")