def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    word_count = count_words(text)
    unique_letters = count_unique_letters(text)
    print(unique_letters)


def count_words(text: str) -> int:
    return len(text.split())


def count_unique_letters(text: str) -> dict[str, int]:
    unique_letters = {}
    lower_case_text = text.lower()
    for i in range(len(lower_case_text)):
        c = lower_case_text[i].strip()
        if c not in unique_letters and c.isalpha():
            unique_letters[c] = 1
        elif c.isalpha():
            unique_letters[c] += 1
    return dict(sorted(unique_letters.items(), key=lambda x: x[1], reverse=True))


if __name__ == "__main__":
    main()
