def main():
    file_path = "books/frankenstein.txt"
    text = read_file(file_path)
    num_words = count_words(text)
    char_list = dict_converter(count_chars(text))
    print(f"--- start report of {file_path} ---")
    print(f"{num_words} was found")
    for x in char_list:
        print(f"The char {x['char']} was found {x['val']} times")
    print("--- end of report ---")


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
        if not char.isalpha():
            continue
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def get_val(dict):
    return dict["val"]


def dict_converter(dict):
    lst = []
    for key in dict:
        lst.append({"char": key, "val": dict[key]})
    lst.sort(key=get_val, reverse=True)
    return lst


main()
