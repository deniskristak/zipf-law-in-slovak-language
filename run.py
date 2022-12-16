from app.word_counter import WordCounter
from app.plot_graphs import GraphPlotter
from config import SAVE_GRAPHS_TO_JPG, DISPLAY_PLOTTED_GRAPHS
from texts_details import input_texts_details

def run_script():

    # run main methods (get word count + plot graph) for each of the texts
    for text_to_process in input_texts_details:

        word_count = WordCounter.get_word_count(text_to_process=text_to_process)

        graph_plotter_instance = GraphPlotter(word_count=word_count, text_to_process=text_to_process)
        graph_plotter_instance.make_plot_bar()

        if SAVE_GRAPHS_TO_JPG:
            graph_plotter_instance.save_plot()

    if DISPLAY_PLOTTED_GRAPHS:
        graph_plotter_instance.show_plot()

    return 0


if __name__ == "__main__":
    run_script()
