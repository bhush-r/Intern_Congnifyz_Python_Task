file_name = input("Enter the name of the file: ")
word_counts = {}

try:
    with open(file_name, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                # Remove punctuation & convert to lowercase
                word = word.strip(".,!?()[]{}\"'").lower()

                word_counts[word] = word_counts.get(word, 0) + 1

except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
    exit()

sorted_word_counts = sorted(word_counts.items())

print("Word\t\t\tCount")
for word, count in sorted_word_counts:
    print(f"{word}\t\t\t{count}")
