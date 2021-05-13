# The executable file of mutating the peptide sequence based on the sample file.
from utility.mutation import mutate_atoms
from utility.peptide_loader import load_peptides


if __name__ == '__main__':
    # load a list of peptide sequence from input file
    peptides = load_peptides("lib/sample_peptide_sequences.txt")
    # generate mutated molecule file for further processing
    for p in peptides:
        mutate_atoms(str(p))
