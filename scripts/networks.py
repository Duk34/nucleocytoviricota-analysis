import pandas as pd
import numpy as np

def generate_cytoscape_files_evalue_cutoff(df, algorithm_name, threshold, output_path):
    ### Sorting the first two columns lexicographically, row-wise
    df[['qseqid', 'sseqid']] = np.sort(df[['qseqid', 'sseqid']].values, axis=1)


    ### Removing identical entries.
    df = df.drop_duplicates(subset=['qseqid', 'sseqid'])

    ### Convert the e-value into float
    df['evalue'] = pd.to_numeric(df['evalue'])

    ### For visual representation of the graph e-value cutoff is used
    graph_table = df[df['evalue'] < threshold]
    graph_table[['qseqid', 'sseqid', 'pident']].to_csv(output_path / (algorithm_name + ".csv"), index=False)

def generate_cytoscape_files_arbitrary_edge_number(df, algorithm_name, number_of_edges, output_path):
    ### Sorting the first two columns lexicographically, row-wise
    df[['qseqid', 'sseqid']] = np.sort(df[['qseqid', 'sseqid']].values, axis=1)


    ### Removing identical entries.
    df = df.drop_duplicates(subset=['qseqid', 'sseqid'])

    ### Convert the e-value into float
    df['evalue'] = pd.to_numeric(df['evalue'])

    ### For visual representation of the graph maximal number of edges is used as a cutoff
    graph_table = df.sort_values(by='evalue').head(number_of_edges)
    ### Saving the file as .csv
    graph_table[['qseqid', 'sseqid', 'pident']].to_csv(output_path / (algorithm_name + ".csv"), index=False)


