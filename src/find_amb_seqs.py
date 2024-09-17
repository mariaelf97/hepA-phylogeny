from Bio import SeqIO
import pandas as pd

def filter_sequences(fasta_file, output_file):
    # Define ambiguous bases
    ambiguous_bases = {'N', 'R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'X'}
    
    # List to store sequence names and ambiguous base counts
    data = []
    
    # List to store filtered sequences
    filtered_sequences = []

    # Read the multifasta file
    with open(fasta_file, 'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            sequence = str(record.seq)
            ambiguous_count = sum(1 for base in sequence if base in ambiguous_bases)
            
            # Keep track of sequences and ambiguous counts
            data.append({'Sequence Name': record.id, 'Ambiguous Bases': ambiguous_count})
            
            # Append the sequence to the filtered list if it has 10 or fewer ambiguous bases
            if ambiguous_count <= 10:
                filtered_sequences.append(record)
    
    # Write the filtered sequences to a new FASTA file
    with open(output_file, 'w') as output_handle:
        SeqIO.write(filtered_sequences, output_handle, 'fasta')

    return data

def main():
    fasta_file = '/home/mahmadi/hepA_seqs/ncbi_search.fasta'  # Input FASTA file
    output_file = 'filtered_sequences.fasta'  # Output FASTA file after filtering
    
    # Filter sequences and collect ambiguous base data
    data = filter_sequences(fasta_file, output_file)
    
    # Create a DataFrame from the collected data
    df = pd.DataFrame(data)
    
    # Optionally, save the DataFrame to a CSV file for reporting
    df.to_csv('ambiguous_bases_counts_filtered.csv', index=False)

if __name__ == "__main__":
    main()
