import simplemma
import re


def get_words_occurences(text_name: str) -> dict:
    """Main method - returns dictionary with words as keys and number of occurences as values

    Args:
        text_name (str): Filename of text file to parse.

    Returns:
        dict: Dictionary produced from the given filename. It contains words as keys and number of occurences as values
    """

    # get the text, put it into string
    text_name = "texts/" + text_name
    with open(text_name, "r") as t:
        text = t.read()

    text_normalized = normalize_text(text=text)

    # transforming normalised string into list with single whitespace as a separator
    normalized_words_list = text_normalized.split(" ")

    # lematisation - putting all words into their 'basic' form
    word_count = lematize_text(normalized_words_list)

    return word_count


def normalize_text(text: str) -> str:
    # putting everything into lowercase
    text_normalized = text.lower()

    numbers_regex = r"[0-9]"
    text_normalized = re.sub(numbers_regex, "", text_normalized)

    # removing special strings
    # order is important here (e.g. '.com' must come before '.')
    strings_to_remove = [
        "!",
        "?",
        ":",
        "'",
        '"',
        "“",
        "„",
        "-",
        ",",
        "www",
        "https",
        "http",
        ".com",
        ".sk",
        "/",
        "\\",
        "(",
        ")",
        "%",
        "$",
        "#",
        "@",
        "&",
        "*",
        "+",
        "=",
        "§",
        "_",
        "€",
        ".",
    ]

    for special_string in strings_to_remove:
        text_normalized = text_normalized.replace(special_string, " ")

    # removing newlines (windows + linux + mac newlines)
    text_normalized = text_normalized.replace("\r", "")
    text_normalized = text_normalized.replace("\n", " ")

    # removing unnecessary whitespaces
    text_normalized = re.sub(r"(\s)\1{1,}", r"\1", text_normalized)

    # return normalised text, still as string
    return text_normalized


def lematize_text(normalized_words_list: list) -> dict[str, int]:
    words_lematized = []
    for w in normalized_words_list:
        if w != "":
            words_lematized.append(simplemma.lemmatize(w, lang="sk"))

    word_count = {}

    for word in words_lematized:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def value_getter(item):
    return item[1]


if __name__ == "__main__":
    word_count = get_words_occurences("ludove_rozpravky.txt")
    total = 0
    for occurences in word_count.items():
        total += occurences[1]
    print(total)
    print(sorted(word_count.items(), key=value_getter, reverse=True))
