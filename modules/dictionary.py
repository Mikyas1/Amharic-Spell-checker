
class Dictionary:

  def __init__(self, dict) -> None:
      result = {}
      for key in dict:
          result[key] = self.load_set_from_file(dict[key])
      self.dict = result


  def load_set_from_file(self, file_name):
      lines = []
      S = set()
      with open(file_name) as f:
          lines = f.readlines()

      for line in lines:
          try:
              S.add(line.strip())
          except Exception as e:
              print(e)
      return S

  def is_in_dict(self, word, type) -> bool:
      return word in self.dict[type]


