# Count Word Frequencies in a Text File
with open("rita.txt", "r") as file:
    data = file.read()

lower_data = data.lower()
lower_data = lower_data.replace(",", "").replace(".","")

words = lower_data.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)