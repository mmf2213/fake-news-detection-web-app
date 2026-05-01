import matplotlib.pyplot as plt

def plot_results(df):
    counts = df['prediction'].value_counts()

    ax = counts.plot(kind='bar')
    plt.title("Fake News Detection Results")
    plt.xlabel("Category")
    plt.ylabel("Count")

    for bar in ax.patches:
        height = bar.get_height()
        ax.annotate(str(int(height)),
                    (bar.get_x() + bar.get_width() / 2, height),
                    ha='center', va='bottom')

    plt.savefig("outputs/graph.png")
    plt.show()