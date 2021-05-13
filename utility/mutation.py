# This file defines the function of performing mutation on the peptide.
# After referencing this file, a new pdb file with desired peptide sequence is generated.
import sys
import threading
from pymol import cmd
from .residue_matching_loader import load_residue_matching

# The lock here is to prevent the synchronization problems imposed in multi-thread programming.
lock = threading.Lock()


# Args:
#   desired_sequence: A new sequence of peptide that can be substituted to the peptide-MHC complex
# Returns:
#   No return values. However, the pdb files with new sequences will be written to the directory of
#   structures/mutated_intermediate.
def mutate_atoms(desired_sequence):
    # Acquire the lock once you execute this program
    lock.acquire()
    cmd.reset()
    # Check the length of peptide sequence
    # If the sequence does not match the MHC structure, the program will terminate.
    try:
        if len(desired_sequence) != 9:
            raise AssertionError
    except AssertionError:
        sys.exit("Please input a peptide sequence with exactly 9 residues (in short abbreviation, no space)!")

    # Execute the mutation command based on the PyMOL API.
    # For each round, we construct a new PyMOL object to avoid the problem of different mutation affecting each other.
    cmd.wizard("mutagenesis")
    cmd.load("structures/3pwn_clear_original.pdb")
    new_sequence = translate_sequence(desired_sequence)
    for i in range(len(new_sequence)):
        cmd.refresh_wizard()
        cmd.get_wizard().set_mode(new_sequence[i])
        cmd.get_wizard().do_select("C/%d/" % (i+1))
        cmd.get_wizard().apply()
    cmd.save("structures/mutated_intermediate/mutated_pmhc_complex.pdb")
    cmd.quit()
    # Release the lock when the program ends
    lock.release()


def translate_sequence(sequence):
    translated_sequence = []
    residue_matching = load_residue_matching()
    for i in range(len(sequence)):
        translated_sequence.append(residue_matching[sequence[i]])
    return translated_sequence
