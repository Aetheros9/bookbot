def main():
    import os
    print(os.getcwd())
    with open("github.com/Aetheros9/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    book_path = "github.com/Aetheros9/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()