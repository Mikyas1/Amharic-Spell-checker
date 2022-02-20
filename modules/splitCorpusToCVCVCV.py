from CVCV import cvcv, ccvc


def load_file(file_name):
    lines = []
    S = set()
    with open(file_name) as f:
        lines = f.readlines()

    for line in lines:
        S.add(line.strip())
    return S


def PrepareCVCVCV(input_file, output_file):
    data = load_file(input_file)
    outfile = open(output_file, 'w')
    count = 0
    for d in data:
        try:
            cv = cvcv(d)
            ccv = ccvc(cv)
            print(cv, "=======", d, "=======", ccv)
            outfile.write(f"{d} {cv}\n")
            count += 1
        except Exception as e:
            pass
    print(f"{count} lines created")
