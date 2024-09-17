# hepA-phylogeny

1. Extract all hepA genomes on nucleotides database: "(hepatitis a[All Fields] AND (viruses[filter] AND is_nuccore[filter] AND ("7000"[SLEN] : "8000"[SLEN]))) AND "Hepatovirus A"[porgn:__txid12092]" 
2. Exclude all non-human host sequences and sequences with more than 10 ambigious bases.
3. include EU140838.1 Simian hepatitis A virus as an outgroup.
4. Filter out sequences with their genotype metadat (found in their gbk file) 
not matching their phylogentic placement on the tree.