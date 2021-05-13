# The executable file of the binding affinity tool based on the Rosetta platform.
# The estimation does not yield high level of accuracy. The API is designed for rough calculation only.
from utility.dock import dock
import os
from utility.side_chain_removal import remove_side_chain
from utility.dock_peptide import flex_peptide_docking
from utility.select_docking_result import interpret_docking_result


if __name__ == '__main__':
    # Execute the mutation source file to change the peptide sequence to the peptide sequence to be calculated
    print("Starting the mutation of atoms...")
    os.system("python3 generate_mutation.py")

    # Perform the docking process and calculate the binding interaction energy in the first step
    print("The mutation of atoms finished. Starting the docking process...")
    binding_energy_docking = dock()

    # Remove the side chain of the MHC to facilitate the further calculation
    print("The docking process completed. Starting the calculation of binding affinity...")
    remove_side_chain()

    # Perform the FlexPepDocking and compute the corresponding binding affinity
    flex_peptide_docking()
    interpret_docking_result("structures/pep_docked_output/score_flexpep_generation.fasc")
