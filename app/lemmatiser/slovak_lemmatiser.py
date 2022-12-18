import pickle


# lemmatiser for slovak language based on morphology database
# by institution "Jazykovedny ustav ludovita stura"
# http://korpus.juls.savba.sk/morphology_database.html
class Lemmatiser:

    def __init__(self):
        # Open the file in binary read mode
        # contains pickle-d python dictionary in form:
        # {'<original_form>': '<lemma>', '<original_form2>': '<lemma>'...}
        with open('app/lemmatiser/SVK_lemmas_dictionary.pickle', 'rb') as f:
            # Load the dictionary from the file
            self.__lemmas_dict = pickle.load(f)

    def lemmatise(self, word):
        try:
            word_lemmatised = self.__lemmas_dict[word]
        except KeyError:
            word_lemmatised = word
            print("Warning: Cant lemmatise word '" + word + "'")
        return word_lemmatised
