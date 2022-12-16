# where to save generated CSV files
FOLDER_TO_SAVE_CSV = 'output/word_count_csv'

# should the graphs be saved as images?
SAVE_GRAPHS_TO_JPG = True

# should the graphs be opened in new windows after being plotted?
# careful, this could be messy if too many texts are analysed
DISPLAY_PLOTTED_GRAPHS = False

# where to save plotted graph images
FOLDER_TO_SAVE_PLOTS = 'output/plots'

# should the graphs be generated on LOG scale?
# If not, linear scale with custom limit (see below) is used
LOG_GRAPH_SCALE = True

# if graphs use linear scale, only depict <this number> of highest ranking words (prevents cluttering the graph)
LINEAR_SCALE_LIMIT_OUTPUT_TO = 50

# If using LOG scale, only mark a point if <this number> of occurences  (or higher) are present (prevents cluttering the graph)
LOG_SCALE_MINIMUM_OCCURENCES_TO_PLOT = 10
