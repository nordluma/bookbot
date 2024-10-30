def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    word_count = count_words(text)
    unique_letters = count_unique_letters(text)
    print_report(word_count, unique_letters)


def count_words(text: str) -> int:
    return len(text.split())


def count_unique_letters(text: str) -> dict[str, int]:
    letter_count = {}
    for c in text.lower():
        if c.isalpha():
            letter_count[c] = letter_count.get(c, 0) + 1
    return dict(sorted(letter_count.items(), key=lambda x: x[1], reverse=True))


def print_report(word_count: int, unique_letters: dict[str, int]):
    print("--- Begin report of books/frankenstein.txt ---")
    print("\n")
    print(f"{word_count} words found in the document")
    for letter, count in unique_letters.items():
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
