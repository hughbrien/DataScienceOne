from sklearn import tree
from sklearn.datasets import load_iris
from sklearn import tree
import graphviz


X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)


prediction = clf.predict([[2., 2.]])
print(prediction)

predict_probability = clf.predict_proba([[2., 2.]])
print(predict_probability)



iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

