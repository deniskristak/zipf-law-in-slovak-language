import matplotlib.pyplot as plt
from config import LINEAR_SCALE_LIMIT_OUTPUT_TO, FOLDER_TO_SAVE_PLOTS, LOG_GRAPH_SCALE, LOG_SCALE_MINIMUM_OCCURENCES_TO_PLOT


class GraphPlotter:
    def __init__(self, word_count, text_to_process):
        self.word_count = word_count
        self.text_to_process = text_to_process

    def make_plot_bar(self):
        # Iterate through list of tuples. Add word to x-axis and number of occurrences to y-axis.
        if LOG_GRAPH_SCALE:
            self.make_log_scale_plot()
        else:
            self.make_linear_scale_plot()

    def show_plot(self):
        # Display the chart
        plt.show()

    def save_plot(self):
        # Save the chart as image
        try:
            plt.savefig(
                "{folder}/{scale}/{language}/{output_prefix_name}.png".format(
                    folder=FOLDER_TO_SAVE_PLOTS,
                    scale="log_scale" if LOG_GRAPH_SCALE else "linear_scale",
                    language=self.text_to_process.get("language"),
                    output_prefix_name=self.text_to_process.get("output_prefix_name"),
                )
            )
        except FileNotFoundError:
            err = "Could not find one or more directories to save the graph into. "
            err += "Did you create sub-directory for each language (in linear_scale and log_scale folder)?"
            raise FileNotFoundError(err)

    def make_log_scale_plot(self):
        x_values = []
        y_values = []
        rank = 0
        for word_x_occurrence in self.word_count:
            if word_x_occurrence[1]==LOG_SCALE_MINIMUM_OCCURENCES_TO_PLOT:
                break
            rank += 1
            x_values.append(rank)
            y_values.append(word_x_occurrence[1])
        fig, ax = plt.subplots(figsize = (8, 8))
        ax.scatter(x_values, y_values)
        ax.set_yscale('log')
        ax.set_xscale('log')
            # Add labels to the x-axis and y-axis
        plt.xlabel("Rank of occurrence")
        plt.ylabel("Number of occurrences")
        # Add a title
        plt.title(
            'Occurrences in \n"{text_name}" \n -- LOG scale --'.format(
                text_name=self.text_to_process.get("full_name")
            )
        )

    def make_linear_scale_plot(self):
        x_values = []
        y_values = []
        for word_x_occurrence in self.word_count:
            x_values.append(word_x_occurrence[0])
            y_values.append(word_x_occurrence[1])
            # how many vales to plot in case of linear scale
            if len(x_values) == LINEAR_SCALE_LIMIT_OUTPUT_TO:
                break
        plt.figure(
            self.text_to_process.get("full_name"), figsize=(LINEAR_SCALE_LIMIT_OUTPUT_TO, 10)
        )
        plt.bar(x=x_values, height=y_values, width=0.3)
        plt.xlabel("Top 20 most-occuring words")
        plt.ylabel("Number of occurences")
        plt.title(
            'Occurrences in \n"{text_name}" \n -- Linear scale --'.format(
                text_name=self.text_to_process.get("full_name")
            )
        )
