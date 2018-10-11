import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import pdb
import os


homePath = os.getcwd()

def get_prediction_for_year(df):
    all_FIPS = df["FIPS"].unique()
    model_txt = "Q('yield_ana') ~ tave5 + tave6 + tave7 + C(FIPS,levels=all_FIPS)"
    addToDF = list()
    for y in range(2003,2017,1):
        train_data = df[(df['year']!=y)]
        test_data = df[(df['year']==y)]
    
        results = smf.ols(model_txt, data=train_data,missing='drop').fit()
        # pdb.set_trace()
        prediction_frame = results.predict(test_data).to_frame('Predicted_yield_ana')
        prediction_frame = pd.concat([prediction_frame, test_data["FIPS"].to_frame("FIPS"),test_data["year"].to_frame("year")],axis=1)
        print(prediction_frame)

        addToDF.append(prediction_frame)
    return pd.concat(addToDF,axis=0)


if __name__ == "__main__":
    os.chdir("../")
    with open("csvNameFile.txt") as f:
        content = f.readlines()
    os.chdir(homePath)
    cropName = content[1].strip()
    formula = ""
    if (cropName == "potato"):
        formula = '../dataFiles/potato_with_anomaly.csv'
    if (cropName == "tomato"):
        formula = '../dataFiles/tomato_with_anomaly.csv'
    if (cropName == "sweetcorn"):
        formula = '../dataFiles/sweetcorn_with_anomaly.csv'
    df = pd.read_csv(formula,dtype={'FIPS':str})
    newDF = get_prediction_for_year(df)
    print("______________\n\n")
    finalDF = newDF.merge(df,on=["FIPS","year"])
    finalDF.to_csv("python_temp_model_A")
