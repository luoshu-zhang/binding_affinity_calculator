# This function can help loading the peptides listed in the target txt file.
import sys


# Args:
#   file_name: The file that stores the list of peptides that needs to be calculated.
# Returns:
#   The list of peptides that needs to be calculated.
def load_peptides(file_name):
    with open(file_name, "r") as f:
        peptides = f.readlines()
    peptides = [i.strip() for i in peptides]
    # Determine whether there is only one peptide sequence in the pdb file.
    try:
        if len(peptides) > 1:
            raise AssertionError
        return peptides
    except AssertionError:
        sys.exit("Please input only one peptide sequence in the input file.")
