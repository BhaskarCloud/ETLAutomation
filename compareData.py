import pandas as pd
import pytest
#from sqlalchemy import create_engine

def test_compareData():
    # extract data from source
    df_src = pd.read_csv("Employee1.csv",sep=",")
    print(df_src)
    # transform source

    # extract data from target
    df_tgt = pd.read_excel("Employee.xlsx")

    df_src_duplicate = df_src.duplicated(subset=['emp_no'])




    #compare both data frame
    assert df_tgt.equals(df_src),"test fail"
    print("all pass")
