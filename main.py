def main():
    file_path = "books/frankenstein.txt"
    text = read_file(file_path)
    print(count_words(text))
    print(count_chars(text))


def count_words(text):
    words = text.split()
    return len(words)


def read_file(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents


def count_chars(text):
    chars = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


main()
