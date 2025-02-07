def count_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document\n")
    char_counts = count_characters(file_contents)
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in char_counts:
            print(f"The '{char}' character was found {char_counts[char]} times")
    print("--- End report ---")
    #print(char_counts)

main()
