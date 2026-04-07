import pandas as pd
from eda_report import generate_eda_report

df = pd.read_csv("data/student_performance.csv")

generate_eda_report(df)