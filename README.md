# Proving Zip's Law in Slovak language texts
## This is an attempt to find occurrences of Zipf law in Slovak, and other less well-documented, languages.

Zip's law is a well-known statistical law that states that the frequency of a word in a text is inversely proportional to its rank in the frequency table. This law has been observed in a wide variety of texts, including books, articles, and even tweets.

This project is an attempt to prove Zip's law using a variety of text datasets, all written in Slovak language. We will analyze the frequency of words in different texts, and compare the results to Zip's law to see if it holds true, while the main output will be graphs and `.csv` files that compare occurrences of words with their order of occurrence.

User doesn't have to use Slovak language only. In sample output, English has been used, but there are multiple languages that should be supported. For more information, scroll down to `Supported languages` section of this file.

For Slovak language, lemmatisation is based on http://korpus.juls.savba.sk/morphology_database.html , which should be very accurate.
For other languages, https://github.com/adbar/simplemma has been used.

# 
# Setup:
1. Install dependencies using `pipenv`
```bash
pipenv install
```
2. Activate `pipenv shell` (any python command should be run with `pipenv shell` active)
```bash
pipenv shell
```

# Usage:
1. Pick a book/article/recipe... in any supported language and copy it's text. If there is anything obvious that would mess up with the result (like name of the book on every page), try to remove it using e.g. text editor. Save the text in the "texts" folder.
2. Write simple details about the book (mostly for you to find the output easily) in `texts_details.py` (be sure to name the text file correctly)
3. Run the script with python:
```bash
python run.py
```
# Output:
## Explained
There are two main types of output:

CSV files
- One `.csv` file per text file entry (specified in `texts_details.py`)
- Each containes order pairs of `word`:`number_of_occurrences` of each word inside a proccessed textfile.

Graphs
- exported graphs that compare occurrence and rank in 3 different flavours:
    1. Plotting full output dataset on **linear scale**.
        - `y-axis` - number of occurences of particular word
        - `x-axis` - rank of 'commonness' the word is on (most common word is on the left, progressing towards least common on the right)
        - note: as we are handling very large number of disctinct words, it's impossible to label each one of them in the graph - that is why we only use rank.
    2. Plotting full output dataset on **logarithmic scale**.
        - same as above, except both `y-axis` and `x-axis` are converted to logarithmic scale
    3. Bar graph of **most common words**
        - mostly for fun
        - you can specify number of words to depict here in `config.py`

## Output files:
- Outputs are sub-divided according to the **type** of output and according to the `language` of the processed text
- Default folder is `./output`
- Subfolders:
    - `plots/`
        - `linear_scale`
            - `sk/`
            - `en/`
        - `log_scale`
            - `sk/`
            - `en/`
        - `most_common_words`
            - `sk/`
            - `en/`
    - `word_count_csv/` (folder containing generated CSV files)
        - `sk/`
        - `en/`

# Configuration:
## All the relevant configuration is in the folder `config.py`.
Here is an overview of configuration with default values:
```python
# where to save generated CSV files
FOLDER_TO_SAVE_CSV = 'output/word_count_csv'
```
```python
# where to save plotted graph images
FOLDER_TO_SAVE_PLOTS = 'output/plots'
```
```python
# should the graphs be generated on LOG scale?
# If not, linear scale with custom limit (see following 2 config options below) is used
LOG_GRAPH_SCALE_ONLY = False
```
```python
# while plotting a bar with most common words, only mark <this number> of highest ranking words (prevents cluttering the graph)
MOST_COMMON_WORDS_LIMIT = 50
```
```python
# Only mark a point if <this number> of occurences  (or higher) are present (prevents cluttering the graph)
MINIMUM_OCCURENCES_TO_PLOT = 10
```
```python
# should all warnings be printed?
VERBOSE = False
```

# Supported languages:
For support for multiple languages, please consult https://github.com/adbar/simplemma#supported-languages , since `simplemma` takes crucial part in the functionality of this project.
Presumably, this project therefore works with any of the supported languages of `simplemma`, but it hasn't been tested (for other than `Slovak` and `English`).
To use other language, simply write it's `Code` (pick one from supported languages in `simplemma` Docs) to the `texts_details.py` configuration file.

# Notes:
- the script will first format the text by removing:
    - ! ? : ' ' " “ „  - / \ ( ) % $ # @ & * + = § _ € www https http .com .sk
    - numbers
    - newlines
    - trailing whitespaces
    - it will also put everything in lowercase
    - it will also attempt to lemmatize each word

# TODO:
- create / implement pdf parser that will ignore footers and headers of pages
