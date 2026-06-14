# nucleocytoviricota-analysis
My attempt to compare three local sequence alignment algorithms (SWIPE, BLAST+ and MMseq2), as part of university work.
# Project Description
This repository contains a comparative analysis of three sequence similarity search tools — **SWIPE**, **BLAST+**, and **MMseqs2** — applied to the analysis of the Nucleocytoviricota (NCLDV) sequence dataset. The goal is to evaluate the performance (time/memory) and sensitivity of these tools in detecting homologous sequences.

# Project Workflow
### 1.Computational Pipeline (LISC):
The computational tasks were executed on the LISC cluster using the Bash shell. The workflow involved manual execution of individual tool commands (*workflow.sh*) for database indexing and sequence similarity searching, ensuring full control over parameters and resource monitoring at each step.
### 2. Data analysis (local enviornment):
Post-processing and statistical analysis were performed using Python (utilizing *pandas* for data manipulation and *matplotlib* for visualization). This stage included:

* **Data Filtering & Parsing:** Importing raw alignment outputs into Python, extracting relevant metrics (alignment scores, percentage identity, E-values), and filtering the datasets to isolate the top 10,000 highest-scoring edges (lowest e-value) for network construction.
* **Statistical Visualization:** Generating comparative histograms on a logarithmic scale to analyze and compare the score distributions and node degree distributions.
* **Network Analysis (Cytoscape):** Exporting the filtered edge lists into Cytoscape to extract, analyze, and visually compare the topology of the largest connected components (giant components) also comparing their sequence identity percentages (`pident`) across all three algorithms.

### 3. Key Findings & Repository Structure
* **Performance vs. Topology:** The analysis highlights the trade-offs between heuristic speed (MMseqs2, BLAST+) and exhaustive mathematical sensitivity (SWIPE), showcasing how these algorithmic strategies directly shape the final network density and structure.
* `scripts/` — Contains Python scripts for data parsing, statistics, and matplotlib plotting.
