# Proving Zip's Law in Slovak language texts
## This is an attempt to find occurrences of Zipf law in Slovak language.

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
1. Pick a book in Slovak language and copy it's text. If there is anything obvious that would mess up with the result (like name of the book on every page), try to remove it using e.g. text editor. Save the text in the "texts" folder.
2. Run the script with python and specify your output file, for example:
```bash
python produce_word_count_and_rank.py > output/dobsinsky_ludove_rozpravky.output
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
