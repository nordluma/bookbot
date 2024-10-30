def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    print(count_words(text))


def count_words(text: str) -> int:
    return len(text.split())




if __name__ == "__main__":
    main()
