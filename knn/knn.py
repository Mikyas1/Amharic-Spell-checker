import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from alphabet import Alphabet


class Knn:
    def __init__(self, file_name, test_size) -> None:
        self.file_name = file_name
        dataset = pd.read_csv(self.file_name)
        self.X = dataset.iloc[:, :-2].values

        for row in range(len(self.X)):
          for col in range(len(self.X[row])):
            if self.X[row, col] == "0" or self.X[row, col] == 0:
              self.X[row, col] = 0
            else:
              self.X[row, col] = Alphabet[self.X[row, col]].value


        self.Y = dataset.iloc[:, 39].values
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.X, self.Y, test_size=test_size
        )
        self.Classifier = KNeighborsClassifier(n_neighbors=15, metric="minkowski", p=2)

    def fit_classifier(self):
        self.Classifier.fit(self.X_train, self.Y_train)

    def run_test(self):
        y_pred = self.Classifier.predict(self.X_test)
        cm = confusion_matrix(self.Y_test, y_pred)
        print(cm)
        for i in range(len(y_pred)):
          print(f"{y_pred[i]} - {self.Y_test[i]}")


# model = KNeighborsClassifier(n_neighbors=5)

# model.fit()
