import matplotlib.pyplot as plt
from config import (
    MOST_COMMON_WORDS_LIMIT,
    FOLDER_TO_SAVE_PLOTS,
    LOG_GRAPH_SCALE_ONLY,
    MINIMUM_OCCURENCES_TO_PLOT,
)


class GraphPlotter:
    def __init__(self, word_count, text_to_process):
        self.word_count = word_count
        self.text_to_process = text_to_process

    def make_plots(self):
        # Iterate through list of tuples. Add word to x-axis and number of occurrences to y-axis.
        self.make_log_scale_plot()
        # self.save_plot("log_scale")


        if not LOG_GRAPH_SCALE_ONLY:
            self.make_linear_scale_plot()
            self.make_most_common_words_plot()

    def show_plot(self):
        # Display the chart
        plt.show()

    def save_plot(self, scale):
        # Save the chart as image
        try:
            plt.savefig(
                "{folder}/{scale}/{language}/{output_prefix_name}.png".format(
                    folder=FOLDER_TO_SAVE_PLOTS,
                    scale=scale,
                    language=self.text_to_process.get("language"),
                    output_prefix_name=self.text_to_process.get("output_prefix_name"),
                )
            )
        except FileNotFoundError:
            err = "Could not find one or more directories to save the graph into. "
            err += "Did you create sub-directory for each language (in linear_scale and log_scale folder)?"
            raise FileNotFoundError(err)
        plt.close()

    def make_log_scale_plot(self):
        x_values = []
        y_values = []
        rank = 0
        for word_x_occurrence in self.word_count:
            if word_x_occurrence[1] == MINIMUM_OCCURENCES_TO_PLOT:
                break
            rank += 1
            x_values.append(rank)
            y_values.append(word_x_occurrence[1])

        fig, ax = plt.subplots()
        fig.set_figwidth(20)
        fig.set_figheight(20)
        ax.scatter(x_values, y_values)
        ax.set_yscale("log")
        ax.set_xscale("log")
        # Add labels to the x-axis and y-axis
        plt.xlabel("Rank of occurrence")
        plt.ylabel("Number of occurrences")
        # Add a title
        plt.title(
            'Occurrences in \n"{text_name}" \n -- LOG scales --'.format(
                text_name=self.text_to_process.get("full_name")
            )
        )
        self.save_plot("log_scale")

    def make_linear_scale_plot(self):
        x_values = []
        y_values = []
        rank = 0
        for word_x_occurrence in self.word_count:
            if word_x_occurrence[1] == MINIMUM_OCCURENCES_TO_PLOT:
                break
            rank += 1
            x_values.append(rank)
            y_values.append(word_x_occurrence[1])
        fig, ax = plt.subplots()
        fig.set_figwidth(20)
        fig.set_figheight(20)
        ax.scatter(x_values, y_values)
        # Add labels to the x-axis and y-axis
        plt.xlabel("Rank of occurrence")
        plt.ylabel("Number of occurrences")
        # Add a title
        plt.title(
            'Occurrences in \n"{text_name}" \n -- LINEAR scales --'.format(
                text_name=self.text_to_process.get("full_name")
            )
        )
        self.save_plot("linear_scale")

    def make_most_common_words_plot(self):
        x_values = []
        y_values = []
        for word_x_occurrence in self.word_count:
            x_values.append(word_x_occurrence[0])
            y_values.append(word_x_occurrence[1])
            # how many vales to plot in case of linear scale
            if len(x_values) == MOST_COMMON_WORDS_LIMIT:
                break
        plt.figure(
            self.text_to_process.get("full_name"), figsize=(MOST_COMMON_WORDS_LIMIT, 10)
        )
        plt.bar(x=x_values, height=y_values, width=0.3)
        plt.xlabel(
            "Top {limit} most-occuring words".format(limit=MOST_COMMON_WORDS_LIMIT)
        )
        plt.ylabel("Number of occurences")
        plt.title(
            'Occurrences in \n"{text_name}" \n -- Most common words --'.format(
                text_name=self.text_to_process.get("full_name")
            )
        )
        self.save_plot("most_common_words")