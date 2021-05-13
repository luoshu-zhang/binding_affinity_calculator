# Binding Affinity Calculator
Binding Affinity Calculator is an efficient tool to compute the binding affinity between a unknown peptide and MHC. For now, the Binding Affinity Calculator can be run on Linux system only.

## Setup
After cloning the project, there are several things to do before executing the codes of Binding Affinity Calculator. First of all, you need to compile the Rosetta source code to create an approperiate environment for execution. To do this, you need to first locate the position of rosetta source code by typing in the following commands in the Linux terminal.
```bash
cd lib/rosetta/source
```
After that, you need to execute the `scons.py` by inputing the following commands in the Linux terminal:
```bash
./scons.py -j <number_of_cores_to_use> mode=release bin
```
If everything goes well, you should be able to see several new directories, including the bin. Now you can start executing the program! If you still have some problem in setting up the environment, you can check [here](https://www.rosettacommons.org/demos/latest/tutorials/install_build/install_build) for more detail.
## Input
To input a peptide sequence, you need to locate the `peptide_sequences_to_be_calculated.txt` file and write a peptide sequence (in abbreviation) in the file. One example is:

```
WIKTISKRM
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
