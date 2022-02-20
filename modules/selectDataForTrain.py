import random


def prepare_data(input_file, output_file, size, max_world_length):
    lines = []
    words = []
    S = set()

    outfile = open(output_file, 'w')
    with open(input_file) as f:
        lines = f.readlines()

    words = [line.split(" ")[0].strip() for line in lines if
             line != "" and len(line.split(" ")[0].strip()) < max_world_length]

    while True:
        rand = random.randint(0, len(words))
        try:
            S.add(words[rand].strip())
            if len(S) >= size: break
        except Exception as e:
            pass

    for s in S:
        print(s)
        outfile.write(s + '\n')
    print(len(S))
