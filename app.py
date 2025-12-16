import csv
from datetime import datetime
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

data = []

with open("processed-data/processed_sales_data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append({
            "date": datetime.fromisoformat(row["Date"]),
            "sales": float(row["Sales"]),
            "region": row["Region"].lower()
        })

app = Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f5f7fa",
        "padding": "30px"
    },
    children=[
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "25px",
                "borderRadius": "8px",
                "maxWidth": "1000px",
                "margin": "0 auto"
            },
            children=[
                html.H1(
                    "Pink Morsel Sales Dashboard",
                    style={"textAlign": "center"}
                ),

                html.P(
                    "Sales trend before and after the price increase on 15 January 2021",
                    style={"textAlign": "center", "color": "#555"}
                ),

                html.Div(
                    style={"textAlign": "center", "marginBottom": "20px"},
                    children=[
                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"}
                            ],
                            value="all",
                            inline=True
                        )
                    ]
                ),

                dcc.Graph(id="sales-chart")
            ]
        )
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):

    if region == "all":
        filtered = data
    else:
        filtered = [row for row in data if row["region"] == region]

    filtered.sort(key=lambda x: x["date"])

    dates = [row["date"] for row in filtered]
    sales = [row["sales"] for row in filtered]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=sales,
            mode="lines",
            name="Sales"
        )
    )

    price_date = datetime(2021, 1, 15)

    fig.add_shape(
        type="line",
        x0=price_date,
        x1=price_date,
        y0=min(sales) if sales else 0,
        y1=max(sales) if sales else 0,
        line={"dash": "dash", "color": "red"}
    )

    fig.add_annotation(
        x=price_date,
        y=max(sales) if sales else 0,
        text="Price Increase",
        showarrow=True,
        yanchor="bottom"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales",
        yaxis_tickprefix="$",
        plot_bgcolor="white"
    )

    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    return fig

if __name__ == "__main__":
    app.run(debug=True)
