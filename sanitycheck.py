import pytest
import pandas as pd

def test_check_duplicates():
    df = pd.read_csv("Employee.csv",sep=",")
    dupcount = df.duplicated().sum()
    assert dupcount == 0, "Duplicate rows found in the dataset"
