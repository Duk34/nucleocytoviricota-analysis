import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

COLORS = ['magenta', 'cyan', 'yellow']

def plot_score(names, data, output_path):

    data_to_plot = [df['bitscore'] for df in data]

    plt.figure(figsize=(10, 6))

    # Plotting
    n, bins, patches = plt.hist(
        data_to_plot,
        bins=25,
        label=names,
        color=COLORS,
        histtype='bar',
        edgecolor='black',
        linewidth=0.5,
    )

    # Formatting the plot
    plt.legend()
    plt.xlabel('Score range')
    ### Locate bin centers
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    ### Make labels that reflect the range of all bins
    range_labels = [f"{int(bins[i])} - {int(bins[i + 1])}" for i in range(len(bins) - 1)]
    ### Only display the range every second bin for clearer depiction.
    for i in range(len(range_labels)):
        if i % 2 != 0:
            range_labels[i] = ""
    plt.xticks(
        bin_centers,
        range_labels,
        rotation=45,
        ha='right'
    )
    plt.ylabel('Frequency [log]')
    plt.yscale('log')
    plt.title('Score comparison side-by-side')
    plt.tight_layout()
    plt.savefig(output_path / "SCORE.png", dpi=300)

def plot_degree_distribution(names, data, output_path):
    ### To plot the degree distribution the data needs to be converted into an edge list.
    degree_distributions = []
    for df in data:
        ### To avoid doubling (A-B == B-A) the data is sorted and only unique entries are taken into account.
        edges_sorted = np.sort(df[['qseqid','sseqid']].values, axis=1)
        unique_edges = pd.DataFrame(edges_sorted).drop_duplicates()

        ### After getting the unique edges they might be concatenated into a list.
        ### Each occurrence of a node in this list corresponds to a single edge going out from this node.
        all_nodes = pd.concat([unique_edges[0], unique_edges[1]])
        degrees = all_nodes.value_counts().values
        degree_distributions.append(degrees)

    plt.figure(figsize=(10, 6))

    # Plotting
    n, bins, patches = plt.hist(
        degree_distributions,
        bins=25,
        label=names,
        color=COLORS,
        histtype='bar',
        edgecolor='black',
        linewidth=0.5,
    )

    plt.legend()
    plt.xlabel('Degree range')
    ### Locate bin centers
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    ### Make labels that reflect the range of all bins
    range_labels = [f"{int(bins[i])} - {int(bins[i + 1])}" for i in range(len(bins) - 1)]
    ### Only display the range every second bin for clearer depiction.
    for i in range(len(range_labels)):
        if i % 2 != 0:
            range_labels[i] = ""
    plt.xticks(
        bin_centers,
        range_labels,
        rotation=45,
        ha='right'
    )
    plt.ylabel('Frequency [log]')
    plt.yscale('log')
    plt.title('Degree distribution comparison side-by-side')
    plt.tight_layout()
    plt.savefig(output_path / "DEGREE_DISTRIBUTION.png", dpi=300)

def plot_pident(input_path, file_names, output_path):
    averages = {}
    for algorithm, file in file_names.items():
        ### Extracting the column from the data.
        df = pd.read_csv(input_path / file, usecols=['pident'])
        pident = df['pident'].to_numpy()
        if algorithm == "MMseqs2":
            pident = pident * 100

        ###
        averages[algorithm] = np.mean(pident)

        ### Plotting
        custom_bins = np.arange(0, 101, 1)
        plt.figure(figsize=(3, 2.5))

        plt.hist(pident,
                 bins=custom_bins,
                 color='skyblue',
                 edgecolor='black',
                 linewidth=0.125,
        )

        plt.title(f"{algorithm}, avg={float(averages[algorithm]):.2f}", fontsize=14)
        plt.xlabel("Percentage", fontsize=12)
        plt.ylabel("Frequency", fontsize=12)

        plt.tight_layout()
        plt.savefig(output_path / f"{algorithm}_pident.png", dpi=300)

        averages[algorithm] = np.mean(pident)
    print(averages)
    return
