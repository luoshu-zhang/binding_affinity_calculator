# This file defines the function of performing mutation on the peptide.
# After referencing this file, the docking process is performed
# and some primary binding interaction energy is generated.
import subprocess


def dock():
    result = subprocess.run(["lib/rosetta/source/bin/docking_protocol.linuxgccrelease",
                             "@flag_local_refine", "-overwrite"], stdout=subprocess.PIPE)
    record = result.stdout
    lines = record.splitlines()
    with open("structures/docked_intermediate/docking_record.txt", "w") as f:
        for line in lines:
            f.write(str(line) + "\n")
        f.close()
    energy_dict = {}
    for i in range(len(lines)-1, -1, -1):
        if len(energy_dict) >= 3:
            break
        line = str(lines[i])
        if "energy" not in line:
            continue
        elif "interaction" in line:
            interaction_energy = get_energy_value(line)
            energy_dict["interaction"] = interaction_energy
            continue
        elif "unbound" in line:
            bounded_energy = get_energy_value(line)
            energy_dict["unbounded"] = bounded_energy
            continue
        elif "bound" in line and "unbound" not in line:
            unbounded_energy = get_energy_value(line)
            energy_dict["bounded"] = unbounded_energy
            continue
    write_energy(energy_dict)
    return energy_dict


def get_energy_value(energy_line):
    components = energy_line.split(":")
    raw_value = components[-1].strip()
    preprocessed_value = ""
    for i in range(len(raw_value)):
        if raw_value[i] in "-1234567890.":
            preprocessed_value += raw_value[i]
    energy_value = float(preprocessed_value)
    return energy_value


def write_energy(energy_dict_ref):
    print("Some side product of the docking: ")
    with open("result/binding_energy_based_on_docking.csv", "w") as f:
        for energy_type, energy_value in energy_dict_ref.items():
            f.write("%s,%f\n" % (str(energy_type.capitalize()), float(energy_value)))
            print("%s Energy is: %f" % (str(energy_type.capitalize()), float(energy_value)))
