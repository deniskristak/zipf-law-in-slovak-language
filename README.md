# Proving Zip's Law in Slovak language texts
## This is an attempt to find occurrences of Zipf law in Slovak, and other less well-documented, languages.

Zip's law is a well-known statistical law that states that the frequency of a word in a text is inversely proportional to its rank in the frequency table. This law has been observed in a wide variety of texts, including books, articles, and even tweets.

This project is an attempt to prove Zip's law using a variety of text datasets, all written in Slovak language. We will analyze the frequency of words in different texts, and compare the results to Zip's law to see if it holds true, also getting help by visualising the numbers of occurrences in texts.
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
4. Outputs are by default generated in `./output/` directory. First, go into the correct language folder (`sk` / `en`) according to what language the text is written in. Then look for `word_count` folder, containing CSV files, and `plots`, containing plotted graphs as images. Folder `plots` contains another division according to what scale you chose to generate the graph on.

# Config:
## All the relevant configuration is in the folder `config.py`.
Here is an overview of configuration with default values:
```python
# where to save generated CSV files
FOLDER_TO_SAVE_CSV = 'output/word_count_csv'
```
```python
# should the graphs be saved as images?
SAVE_GRAPHS_TO_JPG = True
```
```python
# should the graphs be opened in new windows after being plotted?
# careful, this could be messy if too many texts are analysed
DISPLAY_PLOTTED_GRAPHS = False
```
```python
# where to save plotted graph images
FOLDER_TO_SAVE_PLOTS = 'output/plots'
```
```python
# should the graphs be generated on LOG scale?
# If not, linear scale with custom limit (see below) is used
LOG_GRAPH_SCALE = True
```
```python
# if graphs use linear scale, only depict <this number> of highest ranking words (prevents cluttering the graph)
LINEAR_SCALE_LIMIT_OUTPUT_TO = 50
```
```python
# If using LOG scale, only mark a point if <this number> of occurences  (or higher) are present (prevents cluttering the graph)
LOG_SCALE_MINIMUM_OCCURENCES_TO_PLOT = 10
```

# Notes:
- the script will first format the text by removing:
    - ! ? : ' ' " “ „  - / \ ( ) % $ # @ & * + = § _ € www https http .com .sk
    - numbers
    - newlines
    - trailing whitespaces
    - it will also put everything in lowercase
    - it will also attempt to lematize each word

# TODO:
- think about grouping words in different gender form like 'ktorý', 'ktorá', 'ktoré' into one
- create pdf parser that will ignore footers and headers of pages
