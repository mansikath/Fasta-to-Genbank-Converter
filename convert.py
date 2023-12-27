from Bio import SeqIO

def fasta_to_genbank(fasta_filename, genbank_filename, molecule_type="DNA"):
    # Read sequences from the FASTA file
    records = list(SeqIO.parse(fasta_filename, "fasta"))

    # Set molecule_type in annotations
    for record in records:
        record.annotations["molecule_type"] = molecule_type

    # Write sequences to the GenBank file
    SeqIO.write(records, genbank_filename, "genbank")

# Ask the user for input and output filenames
fasta_input = input("Enter the input FASTA filename: ")
genbank_output = input("Enter the output GenBank filename: ")

# Ask the user for molecule type (default is DNA)
molecule_type_input = input("Enter the molecule type (default is DNA): ").strip().upper() or "DNA"

# Call the function with user-specified filenames and molecule type
fasta_to_genbank(fasta_input, genbank_output, molecule_type_input)
