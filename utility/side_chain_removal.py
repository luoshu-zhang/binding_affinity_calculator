import os


def remove_side_chain():
    os.system("grep -v \" B \" structures/docked_intermediate/mutated_pmhc_complex_local_refine_0001.pdb > "
              "structures/docked_intermediate/docked_file_wo_side_chain.pdb")
