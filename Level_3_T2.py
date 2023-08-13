import plotly.express as px
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Sample dataset for Indian states
data = {
    'State': ['Maharashtra', 'Uttar Pradesh', 'Tamil Nadu', 'Gujarat', 'Karnataka'],
    'Population': [123, 231, 78, 67, 56],
    'GDP (Trillion INR)': [2.56, 1.98, 1.76, 1.45, 1.30]
}

df = pd.DataFrame(data)

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Indian State Data Visualization"),

    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[1],  # Default selection
        multi=False
    ),

    dcc.Graph(id='visualization')
])

@app.callback(
    Output('visualization', 'figure'),
    [Input('column-dropdown', 'value')]
)
def update_visualization(selected_column):
    figure = None

    if selected_column:
        if selected_column == 'State':
            figure = px.bar(df, x='State', y='Population', title='Population by State')
        elif selected_column == 'Population':
            figure = px.scatter(df, x='State', y='Population', title='Population by State')
        elif selected_column == 'GDP (Trillion INR)':
            figure = px.bar(df, x='State', y='GDP (Trillion INR)', title='GDP by State')

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
