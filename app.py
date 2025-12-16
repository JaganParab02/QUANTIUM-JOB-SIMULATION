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
        "backgroundColor": "#f4f6f8",
        "padding": "30px"
    },
    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            }
        ),

        html.P(
            "Analyse how Pink Morsel sales changed before and after the price increase, "
            "with the ability to filter by region.",
            style={
                "textAlign": "center",
                "color": "#555"
            }
        ),

        html.Div(
            style={
                "marginTop": "20px",
                "marginBottom": "20px",
                "textAlign": "center"
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={"fontWeight": "bold", "marginRight": "10px"}
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True
                )
            ]
        ),

        dcc.Graph(id="sales-line-chart")
    ]
)

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = [
            row for row in data if row["region"] == selected_region
        ]

    filtered_data.sort(key=lambda x: x["date"])

    dates = [row["date"] for row in filtered_data]
    sales = [row["sales"] for row in filtered_data]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=sales,
            mode="lines",
            name="Sales"
        )
    )

    price_increase_date = datetime(2021, 1, 15)

    fig.add_shape(
        type="line",
        x0=price_increase_date,
        x1=price_increase_date,
        y0=min(sales) if sales else 0,
        y1=max(sales) if sales else 0,
        line=dict(color="red", dash="dash")
    )

    fig.add_annotation(
        x=price_increase_date,
        y=max(sales) if sales else 0,
        text="Price Increase (15 Jan 2021)",
        showarrow=True,
        yanchor="bottom"
    )

    fig.update_layout(
        title="Pink Morsel Sales Over Time",
        xaxis_title="Date",
        yaxis_title="Total Sales",
        plot_bgcolor="white"
    )

    fig.update_yaxes(tickprefix="$")

    return fig

if __name__ == "__main__":
    app.run(debug=True)
