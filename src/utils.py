import pandas as pd
file = r"B:\Machine Learning\Sprint1\YC2_DiabetesTrackAI\data\dataset-diabete-68e2810ab0d7e949117525.csv"

def load_data():
    content = pd.read_csv(file)
    return content
