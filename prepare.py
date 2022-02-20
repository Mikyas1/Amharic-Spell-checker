from modules.featureExteractor import extract_feature


if __name__ == "__main__":
  extract_feature("./data/mike.txt", "./data/out-mike-for-demo.txt", 20)