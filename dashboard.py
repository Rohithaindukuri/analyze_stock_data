import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
# Load processed data
processed_data = pd.read_csv('processed_data.csv', index_col='Date', parse_dates=True)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='stock-price',
        figure={
            'data': [
                go.Scatter(
                    x=processed_data.index,
                    y=processed_data['Close'],
                    mode='lines',
                    name='Close Price'
                ),
                go.Scatter(
                    x=processed_data.index,
                    y=processed_data['20d_ma'],
                    mode='lines',
                    name='20 Day MA'
                ),
                go.Scatter(
                    x=processed_data.index,
                    y=processed_data['50d_ma'],
                    mode='lines',
                    name='50 Day MA'
                )
            ],
            'layout': go.Layout(
                title='Stock Prices with Moving Averages',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Price'},
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
