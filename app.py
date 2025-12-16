import csv
from datetime import datetime
from dash import Dash, dcc, html
import plotly.graph_objects as go
 
dates = []
sales = []

with open("processed-data/processed_sales_data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dates.append(datetime.fromisoformat(row["Date"]))
        sales.append(float(row["Sales"]))
 
combined = list(zip(dates, sales))
combined.sort(key=lambda x: x[0])

dates, sales = zip(*combined)
 
figure = go.Figure()

figure.add_trace(
    go.Scatter(
        x=dates,
        y=sales,
        mode="lines",
        name="Sales"
    )
)
 
price_increase_date = datetime(2021, 1, 15)

figure.add_shape(
    type="line",
    x0=price_increase_date,
    x1=price_increase_date,
    y0=min(sales),
    y1=max(sales),
    line=dict(
        color="red",
        dash="dash"
    )
)

figure.add_annotation(
    x=price_increase_date,
    y=max(sales),
    text="Price Increase<br>(15 Jan 2021)",
    showarrow=True,
    arrowhead=1,
    yanchor="bottom"
)
 
figure.update_layout(
    title="Pink Morsel Sales Over Time",
    xaxis_title="Date",
    yaxis_title="Total Sales",
)

figure.update_yaxes(tickprefix="$")
 
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "Impact of Pink Morsel Price Increase on Sales",
            style={"textAlign": "center"}
        ),
        dcc.Graph(figure=figure)
    ]
)
if __name__ == "__main__":
    app.run(debug=True)
