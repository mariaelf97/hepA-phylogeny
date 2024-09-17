library(treeio)
library(ggtree)
library(data.table)
library(tidyverse)

# read tree file
tree <- read.tree("mnt/hepA_seqs/mafft_aligned_ncbi_search_editted.fasta.treefile")
# Read isolate name and genotype information
tip_labels <- fread("mnt/git_repos/hepA-phylogeny/metadata/ncbi_search_metadata.tsv") 
tree_nodes <- as.data.frame(tree$tip.label)
# to be able to change tip names
joined_labels <- tip_labels %>% select(accession, real_genotype)%>%
  inner_join(tree_nodes, by = c("accession"="tree$tip.label"))
# create genotype, isolate name value 
joined_labels$label_genotype <- paste(joined_labels$real_genotype,joined_labels$accession,sep = "_")
tree_nodes$`tree$tip.label`[!tree_nodes$`tree$tip.label` %in% tip_labels$accession ]
# remove outgroup, duplicated sequences, animal sequences
# and sequences where metadata does not 
# match the phylogeny placement on the tree.
tree <- drop.tip(tree, "M59809.1_2")
tree <- drop.tip(tree, "EU140838.1_2")
tree <- root(tree, outgroup = "EU140838.1", edgelabel = TRUE)
tree <- drop.tip(tree, c("EU140838.1","HV192266.1",
                         "HV192265.1","D00924.1",
                         "OR452344.1","OR452340.1",
                         "OQ559662.1",
                         "ON524432.1",
                         "ON524474.1","ON524440.1",
                         "ON524444.1","ON524432.1",
                         "ON524436.1","ON524460.1",
                         "ON524426.1","HM769724.1",
                         "ON524431.1","ON524458.1",
                         "ON524443.1","ON524473.1",
                         "ON524424.1","ON524430.1",
                         "ON524435.1","ON524427.1",
                         "ON524439.1"))
# rename tree nodes
tree_renamed <- rename_taxa(tree, joined_labels,accession,label_genotype) 
# visualize tree with sequences names
ggtree(tree_renamed) +
  geom_tiplab(size=2) 
# color tips based on genotype
p <- ggtree(tree_renamed, right = TRUE)
p %<+% (joined_labels %>% select(label_genotype,real_genotype)) +
  geom_tippoint(aes(color=real_genotype), size=2)


