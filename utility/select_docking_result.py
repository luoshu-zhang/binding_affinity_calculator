def interpret_docking_result(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    categories_docking = get_categories(lines)
    param_table = []
    for line in lines:
        if "SCORE:" not in line or "total_score" in line:
            continue
        line_preprocessed = line.replace("SCORE:", "")
        data = line_preprocessed.split()
        if len(data) != len(categories_docking):
            continue
        converted_data = []
        for d in data:
            if check_convertibility(d):
                converted_data.append(float(d))
            else:
                converted_data.append(d)
        param_table.append(converted_data)
    param_table.sort(key=lambda x: x[4])
    target_file = param_table[0][-1]
    return param_table, target_file


def get_categories(file_lines):
    categories = []
    for i in range(len(file_lines)):
        if "total_score" in file_lines[i]:
            line = file_lines[i].replace("SCORE:", "").strip()
            categories += line.split()
            break
    return categories


def check_convertibility(string_item):
    try:
        float(string_item)
        return True
    except ValueError:
        return False
