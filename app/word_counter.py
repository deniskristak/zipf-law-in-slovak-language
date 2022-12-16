import simplemma
import re
from config import FOLDER_TO_SAVE_WORD_COUNT_DICT
import json


class WordCounter:
    @staticmethod
    def get_word_count(text_to_process: str) -> list[tuple[str]]:
        """Main method - returns dictionary with words as keys and number of occurrences as values

        Args:
            text_name (str): Filename of text file to parse.

        Returns:
            list[tuple[str, int]]: List of tuples produced from the given filename. It contains pairs of (<word>, <number of occurrences>)
        """

        # get the text, put it into string
        text_path = "texts/" + text_to_process.get("input_filename")
        with open(text_path, "r") as t:
            text = t.read()

        text_normalized = WordCounter.normalize_text(text=text)

        # transforming normalised string into list with single whitespace as a separator
        normalized_words_list = text_normalized.split(" ")

        # lematisation - putting all words into their 'basic' form
        lematized_words = WordCounter.lematize_text(normalized_words_list=normalized_words_list, language=text_to_process.get("language"))

        # create assorted word count dictionary
        word_count_assorted = WordCounter.get_word_count_assorted(lematized_words)

        # make sorted list of tuples so that pairs with highest occurrences come first
        word_count = sorted(
            word_count_assorted.items(), key=WordCounter.value_getter, reverse=True
        )

        # save it to JSON file
        WordCounter.save_output_to_file(
            word_count=word_count, text_to_process=text_to_process
        )

        return word_count

    @staticmethod
    def value_getter(item):
        return item[1]

    @staticmethod
    def normalize_text(text: str) -> str:
        # putting everything into lowercase
        text_normalized = text.lower()

        # remove numbers from text
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
            "‘",
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

    @staticmethod
    def lematize_text(normalized_words_list: list[str], language) -> list[str]:
        words_lematized = []
        for w in normalized_words_list:
            if w != "":
                words_lematized.append(
                    simplemma.lemmatize(w, lang=language)
                )
        return words_lematized

    # create a dict like {<word>:<number_of_occurrences>}
    @staticmethod
    def get_word_count_assorted(words_lematized: list[str]) -> dict[str, int]:
        word_count = {}

        for word in words_lematized:
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

    @staticmethod
    def save_output_to_file(word_count, text_to_process):
        json_string = json.dumps(word_count)
        filename = "{folder_for_output}/{text_filename_prefix}.json".format(
            folder_for_output=FOLDER_TO_SAVE_WORD_COUNT_DICT,
            text_filename_prefix=text_to_process.get("output_prefix_name"),
        )
        with open(filename, "w") as f:
            # write the JSON string to the file
            f.write(json_string)
