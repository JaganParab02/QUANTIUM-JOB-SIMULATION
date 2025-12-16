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
        "minHeight": "100vh",
        "backgroundColor": "#F4F6FB",
        "display": "flex",
        "justifyContent": "center",
        "paddingTop": "40px",
        "fontFamily": "Segoe UI, Arial"
    },
    children=[
        html.Div(
            style={
                "backgroundColor": "white",
                "width": "90%",
                "maxWidth": "1200px",
                "borderRadius": "16px",
                "padding": "32px",
                "boxShadow": "0 10px 30px rgba(0,0,0,0.08)"
            },
            children=[
                html.H1(
                    "Pink Morsel Sales Analysis",
                    style={
                        "textAlign": "center",
                        "color": "#2992F0",
                        "marginBottom": "8px"
                    }
                ),

                html.P(
                    "Sales performance before and after the January 15, 2021 price increase",
                    style={
                        "textAlign": "center",
                        "color": "#616E7C",
                        "marginBottom": "32px"
                    }
                ),

                html.Div(
                    style={
                        "display": "flex",
                        "justifyContent": "center",
                        "marginBottom": "20px"
                    },
                    children=[
                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": "All Regions", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"}
                            ],
                            value="all",
                            inline=True,
                            style={
                                "fontSize": "15px",
                                "color": "#7E72ED",
                                "gap": "20px"
                            }
                        )
                    ]
                ),

                dcc.Graph(
                    id="sales-line-chart",
                    config={"displayModeBar": False}
                )
            ]
        )
    ]
)

@app.callback(
    Output("sales-line-chart", "figure"),
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
            line={"width": 3, "color": "#2992F0"},
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
        line={"color": "#CF72ED", "dash": "dash"}
    )

    fig.add_annotation(
        x=price_date,
        y=max(sales) if sales else 0,
        text="Price Increase",
        showarrow=True,
        yanchor="bottom",
        font={"color": "#CF72ED"}
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin={"l": 40, "r": 20, "t": 40, "b": 40},
        xaxis_title="Date",
        yaxis_title="Total Sales",
        yaxis_tickprefix="$"
    )

    fig.update_xaxes(showgrid=True, gridcolor="#E5E7EB")
    fig.update_yaxes(showgrid=True, gridcolor="#E5E7EB")

    return fig

if __name__ == "__main__":
    app.run(debug=True)
