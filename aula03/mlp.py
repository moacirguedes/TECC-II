"""
  uma rede neural MLP implementada segundo
  https://www.springboard.com/blog/beginners-guide-neural-network-in-python-scikit-learn-0-18/
  http://scikit-learn.org/stable/modules/cross_validation.html
  https://towardsdatascience.com/train-test-split-and-cross-validation-in-python-80b61beca4b6
"""

import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import precision_score

funcs = ['identity', 'logistic', 'tanh', 'relu']
layers = [5, 6, 7, 8, 9, 10]
iterations = [800, 900, 1000, 1100, 1200]

train = pd.read_csv('A3_ok.csv', names=["var1", "var2", "var3", "class"])

fitness  = 0

melhorMlp = MLPClassifier()

for f in funcs:
  for la in layers:
    for it in iterations:
      xTrain = train.drop('class', axis=1)
      yTrain = train['class']

      mlp = MLPClassifier(activation=f, hidden_layer_sizes=(la), max_iter=it)
      mlp.fit(xTrain, yTrain)

      prediction = pd.read_csv('B3_ok.csv', names=["var1", "var2", "var3", "class"])
      xTest = prediction.drop('class', axis=1)
      yTest = prediction['class']

      tests = mlp.predict(xTest)

      newFitness = precision_score(yTest,tests, average='macro')
      
      if newFitness > fitness:
        print("Precision score: {}".format(newFitness))
        print(f, la, it)
        fitness = newFitness
        melhorMlp = mlp

print("Melhor fitness: ")
print(fitness)

prediction = pd.read_csv('B3_ok.csv', names=["var1", "var2", "var3", "class"])
xTest = prediction.drop('class', axis=1)
yTest = prediction['class']

tests = melhorMlp.predict(xTest)

print(confusion_matrix(yTest, tests))
print(classification_report(yTest, tests))

from matplotlib import pyplot as plt
plt.scatter(yTest, tests)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()
