def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    word_count = count_words(text)
    unique_letters = count_unique_letters(text)
    print(unique_letters)


def count_words(text: str) -> int:
    return len(text.split())


def count_unique_letters(text: str) -> dict[str, int]:
    letter_count = {}
    for c in text.lower():
        if c.isalpha():
            letter_count[c] = letter_count.get(c, 0) + 1
    return dict(sorted(letter_count.items(), key=lambda x: x[1], reverse=True))


if __name__ == "__main__":
    main()
