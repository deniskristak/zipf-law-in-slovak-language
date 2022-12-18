import simplemma
import re
from config import FOLDER_TO_SAVE_CSV
import csv
from .lemmatiser.slovak_lemmatiser import Lemmatiser


class WordCounter:
    def __init__(self, text_to_process):
        self.text_to_process = text_to_process

        self.text = ""
        self.text_normalized = ""
        self.text_normalized_list = []
        self.words_lemmatized = []
        self.word_count_assorted = {}
        self.word_count_final_tuples = []
        self.lemmatiser = Lemmatiser()


    def get_word_count(self) -> list[tuple[str]]:
        """Main method - returns dictionary with words as keys and number of occurrences as values

        Returns:
            list[tuple[str, int]]: List of tuples produced from the given filename. It contains pairs of (<word>, <number of occurrences>)
        """

        # get the text, put it into string
        text_path = "texts/" + self.text_to_process.get("input_filename")
        with open(text_path, "r") as t:
            self.text = t.read()

        self.normalize_text()

        # lemmatisation - putting all words into their 'basic' form
        self.lemmatize_text()

        # create assorted word count dictionary
        self.get_word_count_assorted()

        self.get_word_count_sorted()

        # save it to CSV file
        self.save_output_to_file()

        return self.word_count_final_tuples

    @staticmethod
    def value_getter(item):
        return item[1]

    def normalize_text(self):
        # putting everything into lowercase
        self.text_normalized = self.text.lower()

        # remove numbers from text
        numbers_regex = r"[0-9]"
        self.text_normalized = re.sub(numbers_regex, "", self.text_normalized)

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
            "–",
            "▪",
        ]
        for special_string in strings_to_remove:
            self.text_normalized = self.text_normalized.replace(special_string, " ")

        # removing newlines (windows + linux + mac newlines)
        self.text_normalized = self.text_normalized.replace("\r", "")
        self.text_normalized = self.text_normalized.replace("\n", " ")

        # removing unnecessary whitespaces
        self.text_normalized = re.sub(r"(\s)\1{1,}", r"\1", self.text_normalized)

        # transforming normalised string into list with single whitespace as a separator
        self.text_normalized_list = self.text_normalized.split(" ")

    def lemmatize_text(self):
        for w in self.text_normalized_list:
            if w != "":
                
                # if language is SK, cutom-made lematiser (more precise) is used, else use the fairly good pypi package
                if self.text_to_process.get("language") == "sk":
                    word_lemmatised = self.lemmatiser.lemmatise(w)
                else:
                    word_lemmatised = simplemma.lemmatize(w, lang=self.text_to_process.get("language"))

                self.words_lemmatized.append(word_lemmatised)

    # create a dict like {<word>:<number_of_occurrences>}
    def get_word_count_assorted(self):

        for word in self.words_lemmatized:
            if word in self.word_count_assorted.keys():
                self.word_count_assorted[word] += 1
            else:
                self.word_count_assorted[word] = 1

    def get_word_count_sorted(self):
        # make sorted list of tuples so that pairs with highest occurrences come first
        self.word_count_final_tuples = sorted(
            self.word_count_assorted.items(), key=WordCounter.value_getter, reverse=True
        )

    def save_output_to_file(self):
        filename = "{folder_for_output}/{language}/{text_filename_prefix}.csv".format(
            folder_for_output=FOLDER_TO_SAVE_CSV,
            language=self.text_to_process.get("language"),
            text_filename_prefix=self.text_to_process.get("output_prefix_name"),
        )
        try:
            with open(filename, "w", newline="") as csvfile:
                # write the JSON string to the file
                writer = csv.writer(csvfile)
                writer.writerow(["word", "number_of_occurences"])
                for row in self.word_count_final_tuples:
                    writer.writerow([row[0], row[1]])

        except FileNotFoundError:
            err = "Could not find one or more directories to save the text output (word count) into. "
            err += "Did you create sub-directory for each language?"
            raise FileNotFoundError(err)
