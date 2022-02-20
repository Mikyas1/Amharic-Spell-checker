def load_file(file_name):
    S = set()
    lines = []
    outfile = open('./data/merk.txt', 'w')
    with open(file_name) as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        # return line.split(" ")[0].strip()
        words = line.strip().split("፣")
        for w in words:
            if w != "":
                print(w)
                try:
                    S.add(w.strip())
                except Exception as e:
                    pass

    for s in S:
        outfile.write(s + '\n')
        count += 1

    print(count)


    # return [line.split(" ")[0].strip() for line in lines if line != ""]
