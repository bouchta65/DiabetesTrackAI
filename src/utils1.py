import pandas as pd
import matplotlib.pyplot as mpt
import seaborn as sbn
import numpy as np
from sklearn.impute import KNNImputer


file = r"B:\Machine Learning\Sprint1\YC2_DiabetesTrackAI\data\dataset-diabete-68e2810ab0d7e949117525.csv"

def load_data():
    content = pd.read_csv(file)
    return content

def cols1():
    return ["Pregnancies","Glucose","BloodPressure","SkinThickness",
            "Insulin","BMI","DiabetesPedigreeFunction","Age"]

