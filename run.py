from app.word_counter import WordCounter
from app.plot_graphs import GraphPlotter
from texts_details import input_texts_details

def run_script():

    # run main methods (get word count + plot graph) for each of the texts
    for text_to_process in input_texts_details:

        word_counter = WordCounter(text_to_process=text_to_process)
        word_count = word_counter.get_word_count()

        graph_plotter_instance = GraphPlotter(word_count=word_count, text_to_process=text_to_process)
        graph_plotter_instance.make_plots()

    return 0


if __name__ == "__main__":
    run_script()
