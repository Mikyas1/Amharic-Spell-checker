from nltk.metrics.distance import edit_distance


class SpellChecker:
    def __init__(self, word, Dictionary, Morphology, UseGeneralSuggestion) -> None:
        self.word = word
        self.Dictionary = Dictionary
        self.Morphology = Morphology
        self.UseGeneralSuggestion = UseGeneralSuggestion
        self.result = {
            "correct": None,
            "morf_used": False,
            "morf_log": None,
            "morf": None,
            "corrected_morf": None,
            "corrected_morf_log": None,
        }

    def doSpellChecking(self):
        if self.isWordInMainDict():
            self.result["correct"] = True
        else:
            self.result["morf_used"] = True
            resDict = self.doMorphology()
            self.result["morf_log"] = resDict["log"]
            self.result["morf"] = resDict["morf"]

            self.result["corrected_morf"] = self.doMorphologyCorrection(
                self.result["morf"].copy()
            )

            correct = True
            corrected_morf_log = {}
            for key in self.result["corrected_morf"]:
                
                is_in_dictt = self.Dictionary.is_in_dict(
                    self.result["corrected_morf"][key], key
                )
                correct = correct and is_in_dictt

                corrected_morf_log[key] = {
                    "word": self.result["corrected_morf"][key],
                    "matched_in_dict": is_in_dictt,
                }

                if not is_in_dictt:
                    corrected_morf_log[key]["suggestions"] = self.getSuggestion(
                        key, self.result["corrected_morf"][key]
                    )

            self.result["corrected_morf_log"] = corrected_morf_log
            self.result["correct"] = correct

            if self.UseGeneralSuggestion:
                self.result["general_suggestions"] = self.getSuggestion(
                    "MAIN", self.word
                )

    def isWordInMainDict(self) -> bool:
        return self.Dictionary.is_in_dict(self.word, "MAIN")

    def doMorphology(self):
        return self.Morphology.analyse()

    def doMorphologyCorrection(self, morf):
        if "st" in morf:
            return morf
        else:
            if "s" in morf:
                morf["st"] = morf["s"]
                del morf["s"]
            elif "p" in morf:
                morf["st"] = morf["p"]
                del morf["p"]
        return morf

    def getSuggestion(self, s, word):
        correct_words = self.Dictionary.dict[s]
        temp = [(edit_distance(word, w), w) for w in correct_words if w[0] == word[0]]
        sorted_temp = sorted(temp, key=lambda val: val[0])
        
        result = []
        for stemp in sorted_temp:
            result.append(stemp[1])
            if len(result) > 2:
                break
            
        return result