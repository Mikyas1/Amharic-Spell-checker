def extract_feature(file_name, out_put_file, word_length):
    lines = []
    features = ["n", "v", "p", "s", "0"]
    outfile = open(out_put_file, 'w')

    with open(file_name) as f:
        lines = f.readlines()

    print("You Ready for feature extraction!!!")
    print("Lets go!!!")

    title, feature_length = generate_title_and_feature_length(word_length)

    done = 0
    for line in lines:
        cv_word = line.split()[1]
        word = line.split()[0]

        print(f"Word `{word}`")
        print(f"CV Word `{cv_word}`")
        print(title)

        if done != 0: print(f"{done} done KEEP IT UP!!!!!")

        for i in range(len(cv_word)):
            matrix = generate_query_word(feature_length, cv_word, i)

            while True:
                feature = input(matrix).lower()
                valid_feature = is_valid_feature(feature, features)
                if valid_feature:
                    outfile.write(f"{matrix + feature}\n")
                    break
                else:
                    print("ERROR: unsupported feature, only use from ", features)
                    print("  * / *  Come On guys Pay attention")
                    print(f"Word `{word}`")
                    print(f"CV Word `{cv_word}`")
                    print(title)
        done += 1


def generate_query_word(feature_length, word, row):
    res = ""
    word_start_point = int((feature_length - 1) / 2 - (row - 1))
    count = 0
    for col in range(feature_length):
        if col < word_start_point - 1:
            res += "0,"
        else:
            try:
                res += f"{word[count]},"
                count += 1
            except IndexError as e:
                res += "0,"
            # res += "1,"
    # print(len(res.split(",")))
    return res


def generate_title_and_feature_length(word_length):
    feature_length = (word_length * 2) - 1
    x = ""
    for i in range(feature_length):
        if i == int(feature_length / 2):
            x += "V,"
        else:
            x += "0,"
    return x, feature_length


def is_valid_feature(val, features):
    if val in features:
        return True
    return False
