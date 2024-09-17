# hepA-phylogeny

This repository contains scripts and data for analyzing Hepatitis A virus (HepA) genomes and constructing a phylogenetic tree. Follow these steps to extract and process the data:

1. **Extract Hepatitis A Genomes**:
   Query the NCBI nucleotide database with the following search string:
 "(hepatitis a[All Fields] AND (viruses[filter] AND is_nuccore[filter] AND ("7000"[SLEN] : "8000"[SLEN]))) AND "Hepatovirus A"[porgn:__txid12092]" 

2. **Filter Sequences**:
- Exclude all sequences that are not from human hosts.
- Remove sequences with more than 10 ambiguous bases.

3. **Include Outgroup**:
Add the following outgroup sequence to your dataset:
- **EU140838.1**: Simian hepatitis A virus.

4. **Verify Genotype Metadata**:
- Ensure that the genotype metadata (found in the GenBank files) matches the phylogenetic placement of the sequences on the tree.

5. **Generate Barcodes**:
- Use the provided scripts to generate barcodes for the sequences.

### Phylogenetic Tree

[![Tree](https://github.com/mariaelf97/hepA-phylogeny/blob/main/tree/hepA_tree.png)](https://github.com/mariaelf97/hepA-phylogeny/blob/main/tree/hepA_tree.png)
