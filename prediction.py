from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import csv
from numpy import genfromtxt

#setting random seed
np.random.seed(0)

#train_file = 'C:\Users\Mythili Sivakumar\Desktop\kaggle\titanic\dataset\train.csv'
string1 = "C:/Users/Mythili Sivakumar/Desktop"
string2 = "/kaggle/titanic/dataset/train.csv"
#train_data = genfromtxt(string1+string2,delimiter = ',')
train_file = string1+string2
with open(train_file , 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        #print (row[0])
        for col in row:
            
            if col in (None,""):
                print(col)
