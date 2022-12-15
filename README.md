# Zipf law in Slovak language
## This is an attempt to find occurences of Zipf law in Slovak language.
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
1. Pick a book in Slovak language and copy it's text. If there is anything obvious that would mess up with the result (like name of the book on every page), try to remove it using e.g. text editor. Save the text into the "texts" folder.
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