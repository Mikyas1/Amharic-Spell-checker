def load_file(file_name):
    lines = []
    S = set()
    outfile = open("./necessaryData/stt.txt", "w")

    with open(file_name) as f:
        lines = f.readlines()

    count = 0

    for line in lines:
        try:
            S.add(line.split()[1].strip())
        except Exception as e:
            pass

    for s in S:
        outfile.write(s + "\n")
        count += 1

    print(count)
