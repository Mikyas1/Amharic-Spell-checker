unwanted = ["<", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "።", "፣", ".", "፤", "-", "/", "\"", ]

word_class = ['ADJC', 'PREP', 'VN', 'NUMPC', 'NUMC', 'PUNC', 'N', 'UNC', 'PREPC', 'ADJPC', 'PRON', 'ADJ', 'V', 'VPC',
              'NUMP', 'CONJ', 'AUX', 'VC', 'NC', 'NP', 'ADV', 'VREL', 'NUMCR', 'NPC', 'PRONC', 'PRONPC', 'ADJP',
              'NUMOR', 'PRONP', 'INT', 'VP'
              ]


def load_wic_file(file_name):
    res = []
    lines = []
    S = set()
    with open(file_name) as f:
        lines = f.readlines()

    # return [line.split(" ")[0].strip() for line in lines if (line != ""
    #                                                          and
    #                                                          len(line.split(" ")[0].strip()) > l
    #                                                          )]

    count = 0
    outfile = open('./data/wic-corpus.txt', 'w')
    for line in lines:
        if not any(un in line for un in unwanted):
            ns = line.strip()
            try:
                nsarr = ns.split()
                if len(nsarr) == 3:
                    # print(ns)
                    # outfile.write(nsarr[0] + '\n')
                    S.add(nsarr[0])
                    print(ns)
                    count += 1
            except Exception as e:
                pass
            # arl = len(ns.split())
            # if arl != 3:
            #     print(arl)
    print(count)
    for s in S:
        outfile.write(s + '\n')
