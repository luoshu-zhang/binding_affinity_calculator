# This function defines the method to loading the matching dictionary between residue names and residue abbreviations.

# Args:
#   file_name: The file that stores the list of peptides that needs to be calculated.
# Returns:
#   The dictionary of residue matching between the residue name and abbreviation.
def load_residue_matching():
    with open("lib/residue_name_matching.txt", "r") as f:
        residues = f.readlines()
    residue_matching = {}
    for i in range(len(residues)):
        name, abbreviation = residues[i].split()
        name.strip()
        abbreviation.strip()
        residue_matching[abbreviation] = name
    return residue_matching
