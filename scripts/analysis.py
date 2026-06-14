import pandas as pd
import numpy as np
from pathlib import Path
from plots import *
from networks import *
import winsound

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "data" / "raw"
FIG_DIR = BASE_DIR / "figures"
OUTPUT_DIR = BASE_DIR / "data" / "processed"

E_VALUE_THRESHOLD = 10e-20

FILES = {
    "SWIPE" : "Nucleocytoviricota.swipe.wo_self.m8",
    "BLAST" : "Nucleocytoviricota.blastp.wo_self.m8",
    "MMseqs2" : "Nucleocytoviricota.mmseqs.wo_self.m8",
}
FILES_GC = {
    "SWIPE" : "SWIPE_GC.csv",
    "BLAST" : "BLAST_GC.csv",
    "MMseqs2" : "MMseqs2_GC.csv",
}

COLUMN_NAMES = ['qseqid',
                'sseqid',
                'pident',
                'length',
                'mismatch',
                'gapopen',
                'qstart',
                'qend',
                'sstart',
                'send',
                'evalue',
                'bitscore',
]


def main():
    data = []
    names = []
    for name, filename in FILES.items():
        file_path = INPUT_DIR / filename
        ### Reading the data into the memory
        df = pd.read_csv(file_path, sep="\t", header=None, names=COLUMN_NAMES)

        ### To account for the output of the SWIPE program for later creation of a graph, the names have to be cleared.
        if name == "SWIPE":
            ### Clear the Target column
            df['sseqid'] = df['sseqid'].str.replace('ref|', '', regex=False)
            df['sseqid'] = df['sseqid'].str.replace('|', '', regex=False)

            ### Clear the query column just in case.
            df['qseqid'] = df['qseqid'].str.replace('ref|', '', regex=False)
            df['qseqid'] = df['qseqid'].str.replace('|', '', regex=False)

        data.append(df)
        names.append(name)

    ### Generating the score chart:
    plot_score(names, data, FIG_DIR)

    ### Generating the degree chart:
    plot_degree_distribution(names, data, FIG_DIR)

    ### Generating the pident charts
    plot_pident(INPUT_DIR, FILES_GC, FIG_DIR)

    ### Generating the files for later generation of graphs:
    for name, df in zip(names, data):
        #generate_cytoscape_files_evalue_cutoff(df, name, E_VALUE_THRESHOLD, OUTPUT_DIR)
        generate_cytoscape_files_arbitrary_edge_number(df, name, 10000, OUTPUT_DIR)




if __name__ == "__main__":
    main()
    winsound.Beep(1000, 500)











