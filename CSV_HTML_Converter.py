import pandas as pd

Weather = pd.read_csv("cities.csv")
Weather.head()
print(Weather.to_html())