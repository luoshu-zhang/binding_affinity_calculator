import os


def flex_peptide_docking():
    os.system("lib/rosetta/source/bin/FlexPepDocking.linuxgccrelease @flags_prepack_flex -overwrite")
    os.system("lib/rosetta/source/bin/FlexPepDocking.linuxgccrelease @flags_generation_flex")
