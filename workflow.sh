# ==============================================================================
# NCLDV Sequence Alignment Pipeline
# Reproducing findings of Yutin et al. (2009)
# ==============================================================================

# The main author of this comments is my university professor Thomas Rattei
# I just modified them to suit my needs

# 1. SETUP & PREREQUISITES
# Ensure your sequence file is named 'Nucleocytoviricota.faa' and placed in the root direct

# Converting the file into BLAST+ database
module load BLAST+
makeblastdb -dbtype prot -in Nucleocytoviricota.faa -parse_seqids -blastdb_version 4
module unload BLAST+

# Calculate swipe all-vs-all comparison
module load SWIPE
module list SWIPE
/usr/bin/time swipe --query Nucleocytoviricota.faa --db Nucleocytoviricota.faa --out Nucleocytoviricota.swipe.m8 --outfmt 8 --matrix BLOSUM45 --gapopen 11 --gapextend 3 --evalue 1 --num_alignments 50636 --num_threads 4
module unload SWIPE

# Calculate blastp all-vs-all comparison
module load BLAST+
module list BLAST+
/usr/bin/time blastp -query Nucleocytoviricota.faa -db Nucleocytoviricota.faa -out Nucleocytoviricota.blastp.m8 -outfmt 6 -matrix BLOSUM45 -gapopen 11 -gapextend 3 -evalue 1 -num_alignments 50636 -num_threads 32
module unload BLAST+

# Remove self hits and unneeded protein name prefixes
cat Nucleocytoviricota.swipe.m8 | sed 's/lcl|//' | awk '$1!=$2' >Nucleocytoviricota.swipe.wo_self.m8 
cat Nucleocytoviricota.blastp.m8 | sed 's/lcl|//' | awk '$1!=$2' >Nucleocytoviricota.blastp.wo_self.m8

# Creating temporary directory for the MMseqs2
mkdir temp

# Calculate mmseqs all-vs-all comparison
module load MMseqs2
module list MMseqs2
mmseqs createdb Nucleocytoviricota.faa Nucleocytoviricota
/usr/bin/time mmseqs search Nucleocytoviricota Nucleocytoviricota result tmp --threads 32
mmseqs convertalis Nucleocytoviricota Nucleocytoviricota result Nucleocytoviricota.mmseqs.m8
cat Nucleocytoviricota.mmseqs.m8 | sed 's/lcl|//' | awk '$1!=$2' >Nucleocytoviricota.mmseqs.wo_self.m8
rm -rf temp
# Keep all relevant output files in our home directory
mv *.wo_self.m8 ~/


