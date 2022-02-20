import subprocess

from CVCV import cvcv, ccvc
from modules.featureExteractor import (
    generate_query_word,
    generate_title_and_feature_length,
)


class Morphology:

    input_file_name = "./data/runFolder/input.txt"
    output_file_name = "./data/runFolder/output.txt"
    model_file_name = "./data/runFolder/trainModel"

    def __init__(self, word) -> None:
        self.input_file = open(Morphology.input_file_name, "w")
        self.max_word = 20
        self.word = word
        self.CVCV = cvcv(self.word)

        _, feature_len = generate_title_and_feature_length(self.max_word)

        for i in range(len(self.CVCV)):
            wd = generate_query_word(feature_len, self.CVCV, i)
            self.input_file.write(f"{wd}0\n")

        self.input_file.close()

    def run(self):
        x = subprocess.run(
            [
                "timbl",
                "-i",
                Morphology.model_file_name,
                "-t",
                Morphology.input_file_name,
                "-o",
                Morphology.output_file_name,
            ]
        )
        x.check_returncode()

    def load_results(self):
        results = []
        with open(self.output_file_name) as f:
            lines = f.readlines()

            for line in lines:
                cols = line.split(",")
                last_i = len(cols)
                results.append(cols[last_i - 1][0])

        return results

    def do_morphology(self):
        res = self.load_results()
        dict = {}
        temp = ""
        log = []
        for i in range(len(res)):
            log.append([self.CVCV[i], res[i]])
            print(f"{self.CVCV[i]} - {res[i]}")
            c_class = res[i]
            c = self.CVCV[i]
            if c_class == "0" or c_class == 0:
                temp += c
            else:
                temp += c
                if c_class in dict:
                    dict[c_class] = dict[c_class] + temp
                else:
                    dict[c_class] = temp
                temp = ""
        if temp != "":
            if "s" in dict:
                dict["s"] = dict["s"] + temp
            else:
                dict["s"] = temp

        # suffix correction
        # if "s" in dict and len(dict["s"]) > 8:
        #     dict["v"] = dict["s"]
        #     dict.pop("s")

        for key in dict:
            dict[key] = ccvc(dict[key])

        self.morp_dict = dict
        return dict, log

    def generate_s_st_p(self):
        dict = {}
        for key in self.morp_dict:
            if key == "n" or key == "v":
                if "st" in dict:
                    dict["st"] = dict["st"] + self.morp_dict[key]
                else:
                    dict["st"] = self.morp_dict[key]
            else:
                dict[key] = self.morp_dict[key]
        return dict

    def analyse(self):
        self.run()
        _, log = self.do_morphology()
        morf = self.generate_s_st_p()

        return {"log": log, "morf": morf}
