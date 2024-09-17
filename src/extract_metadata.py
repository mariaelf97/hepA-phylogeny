from Bio import SeqIO
import pandas as pd

# Function to extract metadata, including geolocation, title, and genotype from a GenBank record
def extract_metadata(record):
    # Initialize variables
    sample_id = record.id
    geolocation = None
    strain = None
    host = None
    title = None
    genotype = None

    # Access the date in the LOCUS line
    date = record.annotations.get("date")

    # Extract title from the first reference (publication)
    if "references" in record.annotations:
        references = record.annotations["references"]
        if references:
            title = references[0].title  # Assuming the title of the first reference is desired

    # Iterate through features in the GenBank record
    for feature in record.features:
        # Extract geolocation
        if "geo_loc_name" in feature.qualifiers:
            geolocation = "; ".join(feature.qualifiers.get("geo_loc_name"))
        
        # Extract strain
        if "strain" in feature.qualifiers:
            strain = "; ".join(feature.qualifiers.get("strain"))
        
        # Extract host
        if "host" in feature.qualifiers:
            host = "; ".join(feature.qualifiers.get("host"))
        
        # Extract genotype (if present)
        if "genotype" in feature.qualifiers:
            genotype = "; ".join(feature.qualifiers.get("genotype"))
        
        # If genotype is stored in a note or misc_feature, check here
        if "note" in feature.qualifiers:
            note = "; ".join(feature.qualifiers.get("note"))
            if "genotype" in note.lower():
                genotype = note  # Assign the note if it mentions genotype

    # If genotype wasn't found in the features, try other methods (e.g., infer from references)
    if not genotype and "references" in record.annotations:
        for ref in record.annotations["references"]:
            if "genotype" in ref.title.lower():
                genotype = ref.title  # Infer genotype from the publication title if mentioned

    return strain, date, host, sample_id, geolocation, title, genotype

# Function to parse a multi-sequence GenBank file and return a DataFrame
def parse_genbank_file(file_path):
    data = []
    
    # Parse the GenBank file
    for record in SeqIO.parse(file_path, "genbank"):
        strain, sample_date, host, sample_ID, geolocation, title, genotype = extract_metadata(record)
        data.append({"strain": strain, "sample_date": sample_date,
                     "host": host, "accession": sample_ID, "country": geolocation, 
                     "title": title, "genotype": genotype})  # Add title and genotype to the DataFrame
    
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(data)
    
    return df

# Specify the path to your GenBank file
file_path = "/home/mahmadi/hepA_seqs/ncbi_search.gb"

# Parse the GenBank file and get the DataFrame
df = parse_genbank_file(file_path)

# Optionally, save the DataFrame to a CSV/TSV file
df.to_csv("metadata/ncbi_search_metadata.tsv", index=False, sep="\t")
