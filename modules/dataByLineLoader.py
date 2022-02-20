
def load_file(file_name, l):
    lines = []
    with open(file_name) as f:
        lines = f.readlines()

    # for line in lines:
    #     return line.split(" ")[0].strip()

    return [line.split(" ")[0].strip() for line in lines if line != "" and len(line.split(" ")[0].strip()) > l]
