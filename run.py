from app.word_counter import WordCounter
from app.plot_graphs import GraphPlotter
from texts_details import input_texts_details


def run_script():
    no_of_texts = len(input_texts_details)
    # run main methods (get word count + plot graph) for each of the texts
    for text_to_process in input_texts_details:
        fullname = text_to_process.get("full_name")
        no_of_texts -= 1
        msg = f"Processing '{fullname}'."
        print(msg)
        print("Counting words...")
        word_counter = WordCounter(text_to_process=text_to_process)
        word_count = word_counter.get_word_count()
        print("Plotting graphs...")
        graph_plotter_instance = GraphPlotter(
            word_count=word_count, text_to_process=text_to_process
        )
        graph_plotter_instance.make_plots()
        msg = f"{no_of_texts} more to go." if no_of_texts > 0 else ""
        print(msg)
    print("Done!")
    return 0


if __name__ == "__main__":
    run_script()
