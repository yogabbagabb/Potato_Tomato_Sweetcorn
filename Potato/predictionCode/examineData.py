import numpy as np
import pandas as pd
import sys
import os


homePath = os.getcwd()
def examineData():

    os.chdir("../")
    with open("csvNameFile.txt") as f:
        content = f.readlines()
    os.chdir(homePath)

    cropName = content[1].strip()
    if (cropName == "potato"):
        A = pd.read_csv("potato_with_anomaly.csv")
    if (cropName == "tomato"):
        A = pd.read_csv("tomato_with_anomaly.csv")
    if (cropName == "sweetcorn"):
        A = pd.read_csv("sweetcorn_with_anomaly.csv")


    # For each X in S = {5,6,7,8,9}, test if precipX, tempX and vpdaveX are each missing (ie NA) iff the remaining four entries in S are missing (ie NA). In other words, we want to determine
    # whether we can claim that for every data point, either every precipitation entry is not null or every precipitation entry is null
    # If this claim is true, then the print statement below will report false

    first = pd.isnull(A["precip5"]) & pd.isnull(A["precip6"]) & pd.isnull(A["precip7"]) & pd.isnull(A["precip8"]) & pd.isnull(A["precip9"])
    second = ~(pd.isnull(A["precip5"])) & ~(pd.isnull(A["precip6"])) & ~(pd.isnull(A["precip7"])) & ~(pd.isnull(A["precip8"])) & ~(pd.isnull(A["precip9"]))
    print(any(~(first | second)))


    # See the comments above. They are apropos here, except that we consider vpdave in place of precip
    first = pd.isnull(A["vpdave5"]) & pd.isnull(A["vpdave6"]) & pd.isnull(A["vpdave7"]) & pd.isnull(A["vpdave8"]) & pd.isnull(A["vpdave9"])
    second = ~(pd.isnull(A["vpdave5"])) & ~(pd.isnull(A["vpdave6"])) & ~(pd.isnull(A["vpdave7"])) & ~(pd.isnull(A["vpdave8"])) & ~(pd.isnull(A["vpdave9"]))
    print(any(~(first | second)))

    # See the comments above above. They are apropos here, except that we consider tave in place of precip
    first = pd.isnull(A["tave5"]) & pd.isnull(A["tave6"]) & pd.isnull(A["tave7"]) & pd.isnull(A["tave8"]) & pd.isnull(A["tave9"])
    second = ~(pd.isnull(A["tave5"])) & ~(pd.isnull(A["tave6"])) & ~(pd.isnull(A["tave7"])) & ~(pd.isnull(A["tave8"])) & ~(pd.isnull(A["tave9"]))
    print(any(~(first | second)))

    # First suppose that the answer to all three claims above is positive: that either
    # a data entry has all 5 of its precipitation, vpdave, or tave entries as NULL, or else
    # all 5 entries are not null

    # The following three tests assess whether for a given data entry we can claim that
    # for a given entry, all precipitation entries are null and iff all vpdave entries are null
    # If a test reports positive, then the claim is true

    first = pd.isnull(A["precip5"]) & pd.isnull(A["vpdave5"]) 
    second = ~(pd.isnull(A["precip5"])) & ~(pd.isnull(A["vpdave5"]))
    print(any(~(first | second)))

    # The following three tests assess whether for a given data entry we can claim that
    # for a given entry, all vpdave entries are null and iff all tave entries are null

    first = pd.isnull(A["vpdave5"]) & pd.isnull(A["tave5"]) 
    second = ~(pd.isnull(A["vpdave5"])) & ~(pd.isnull(A["tave5"]))
    print(any(~(first | second)))

    # The following three tests assess whether for a given data entry we can claim that
    # for a given entry, all tave5 entries are null and iff all precip5 entries are null
    first = pd.isnull(A["tave5"]) & pd.isnull(A["precip5"]) 
    second = ~(pd.isnull(A["precip5"])) & ~(pd.isnull(A["tave5"]))
    print(any(~(first | second)))



if __name__ == "__main__":
    examineData()
