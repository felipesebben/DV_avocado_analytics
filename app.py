from dash import Dash
from dash import dcc
from dash import html
import pandas as pd

data = pd.read_csv('data/avocado.csv')
data = data.query("type == 'conventional' and region == 'Albany'")
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
data.sort_values('Date', inplace=True)

external_stylesheets = [
    {
        'href': 'https://fonts.googleapis.com/css2?'
        'family=Lato:wght@400;display=swap',
        'rel': 'stylesheet',
    },
]
# Initializing Applications
app = Dash(__name__, external_stylesheets= external_stylesheets)
app.title = "Avocado Analytics: Understand your Avocados!"

# Definfing the Layout of the App
app.layout = html.Div(
    children =[
        html.Div(
            children=[
                html.P(children= '🥑', className='header-emoji'),
                html.H1(children="Avocado Analytics",
                className='header-title'),
                html.P(
                    children="Analyze the behavior of avocado prices"
                    " and between the number of avocados sold in the US"
                    " between 2015 and 2018",
                    className='header-description'
                ),
            ],
            className='header',
        ),
        # Style the charts.
        html.Div(
            children=dcc.Graph(
                id="price-chart",
                config={"displayModeBar": False},
                figure={
                    "data": [
                        {
                            "x": data["Date"],
                            "y": data["AveragePrice"],
                            "type": "lines",
                            "hovertemplate": "$%{y:.2f}<extra></extra>",                       
                        },
                    ],
                    "layout": {
                        "title": {
                            "text": "Average Price of Avocados",
                            "x": 0.05,
                            "xanchor": "left",
                        },
                        "xaxis": {"fixedrange": True},
                        "yaxis": {"tickprefix": "$", "fixedrange": True},
                        "colorway": ["#17B897"],
                    },
                },
            ),
            className="card",
        ),
        html.Div(
            children=dcc.Graph(
                id="volume-chart",
                config={"displayModeBar": False},
                figure={
                    "data": [
                        {
                            "x": data["Date"],
                            "y": data["Total Volume"],
                            "type": "lines",
                        },
                    ],
                    "layout": {
                        "title": {
                            "text": "Avocados Sold",
                            "x": 0.05,
                            "xanchor": "left",
                        },
                        "xaxis": {"fixedrange": True},
                        "yaxis": {"fixedrange": True},
                        "colorway": ["#E12D39"]
                    },
                },
            ),
            className="card",
        ),
    ],
    className="wrapper",
)

if __name__ == '__main__':
    app.run_server(debug=True)