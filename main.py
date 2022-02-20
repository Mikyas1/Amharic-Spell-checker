from CVCV import cvcv, ccvc
from modules.dataPrepForSeber import load_file
# from modules.dataByLineLoader import load_file
# from modules.stemPrepare import load_file as stem_load_file
from modules.featureExteractor import extract_feature
from modules.spellChecker import SpellChecker
from modules.splitCorpusToCVCVCV import PrepareCVCVCV
from modules.selectDataForTrain import prepare_data
from modules.dictionary import Dictionary
from knn.knn import Knn
from timbl.timbl import Morphology

from flask import Flask
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


# load main dict
Dict = Dictionary({
    "MAIN": "./necessaryData/corpus.txt",
    "s": "./necessaryData/s.txt",
    "p": "./necessaryData/p.txt",
    "st": "./necessaryData/st.txt",
})

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def add_income():
    body = request.get_json()
    if "text" in body:
        try:
            # result = m.analyse()
            spellChecker = SpellChecker(body["text"], Dict, Morphology(body["text"]), True)
            spellChecker.doSpellChecking()
            
            return spellChecker.result, 200

        except Exception as e:
            print(e.with_traceback())
            return "Error happend", 500


# corpus = 150, wic-corpus = 150, seber = 100, merk = 100
if __name__ == "__main__":
    app.run(debug=True)



















    # extract_feature("./data/mary.txt", "data/out-mary.txt", 20)

    # k = Knn("./data/gold.csv", 0.2)
    # k.fit_classifier()
    # k.run_test()

    # print("everything good")

    # PrepareCVCVCV("./data/main.txt", "./data/main-cv.txt")

    # prepare_data("./data/corpus.txt", "unnecessary data/corpus-150.txt", 150, 10)
    # prepare_data("./data/wic-corpus.txt", "./data/wic-corpus-150.txt", 150, 10)
    # prepare_data("./data/seber.txt", "./data/seber-100.txt", 100, 10)
    # prepare_data("./data/merk.txt", "./data/merk-100.txt", 100, 10)

    # m = Morphology("ማብጠልጠሉን")
    # m.run()
    # m.do_morphology()
    # print(m.generate_s_st_p())

    # correct_words = Dict.dict["MAIN"]

    # word = "መታለላቸው"

    # temp = [(edit_distance(word, w),w) for w in correct_words if w[0]==word[0]]

    # # for t in temp:
    # #     print(t)
    # sorted_temp = sorted(temp, key = lambda val:val[0])
    # print(sorted_temp[0][1])
    # print(sorted_temp[1][1])
    # print(sorted_temp[2][1])
    # print(sorted_temp[3][1])
