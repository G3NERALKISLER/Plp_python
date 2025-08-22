file=open("input.txt", "r")
with open("input.txt", "r") as file: data=file.read()

words = data.split()
word_count= len(words)

uppercase_text = data.upper()

with open("output.txt", "w") as file:
    file.write("Processed Text:\n")
    file.write(uppercase_text + "\n")
    file.write(f"Word Count: {word_count}\n")
    print("output.txt has been created successfully!")