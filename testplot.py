# library & dataset
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = sns.load_dataset('iris')

A = [5,5,3,3,5,7,7,3,9,]
B = [1,2,3,4,5,6,7,8,9,]

dataframe = pd.DataFrame(A, B)
dfhead = dataframe.head()

jsondf = pd.read_json('./events.json')

print(jsondf)

