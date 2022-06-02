import pandas as pd
import plotly.express as px

df = pd.read_csv("main.csv")

TOEFL_Score = df["TOEFL Score"].tolist()
Chances_of_admit = df["Chance of admit"].tolist()

fig = px.scatter(x = TOEFL_Score, y = Chances_of_admit)
fig.show()

m = 0.01
c = -2.5
y = []
for x in TOEFL_Score:
    y_value = m*x + c
    y.append(y_value)

fig = px.scatter(x = TOEFL_Score, y = Chances_of_admit)
fig.update_layout(shapes=[
    dict(
        type = 'line'
        y0 = min(y), y1 = max(y),
        x0 = min(TOEFL_Score), x1 = max(TOEFL_Score)
    )
])  
fig.show()

x = 600
y = m * x + c
print(f"chances of admit based on their TOEFL Score {x} is {y}")

