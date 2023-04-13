# where to save generated CSV files
FOLDER_TO_SAVE_CSV = 'output/word_count_csv'

# where to save plotted graph images
FOLDER_TO_SAVE_PLOTS = 'output/plots'

# should the graphs be generated ONLY on LOG scale?
# If not, linear scale with custom limit (see following 2 config options below) is used
LOG_GRAPH_SCALE_ONLY = False

# while plotting a bar with most common words, only mark <this number> of highest ranking words (prevents cluttering the graph)
MOST_COMMON_WORDS_LIMIT = 50

# Only mark a point if <this number> of occurences  (or higher) are present (prevents cluttering the graph)
MINIMUM_OCCURENCES_TO_PLOT = 10

# should all warnings be printed?
VERBOSE = False
