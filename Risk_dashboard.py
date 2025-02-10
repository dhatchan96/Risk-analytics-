import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load data
df = pd.read_csv("risk_results.csv")

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Risk Management Dashboard"),
    
    dcc.Graph(
        id="lcr-trend",
        figure=px.line(df, x="Date", y="Liquidity Coverage Ratio (LCR)",
                       title="Liquidity Coverage Ratio Over Time")
    ),
    
    dcc.Graph(
        id="pd-trend",
        figure=px.line(df, x="Date", y="Probability of Default (PD)",
                       title="Probability of Default Over Time")
    ),
    
    dcc.Graph(
        id="npa-trend",
        figure=px.line(df, x="Date", y="Non-Performing Assets (NPA)",
                       title="Non-Performing Assets Over Time")
    ),
    
    dcc.Graph(
        id="fraud-score",
        figure=px.bar(df, x="Date", y="Fraud Detection Score",
                      title="Fraud Detection Score Over Time")
    ),

    dcc.Graph(
        id="efficiency-score",
        figure=px.scatter(df, x="Date", y="Operational Efficiency Score",
                          color="Risk Alert Level", title="Operational Efficiency Score vs Risk Alert Level")
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
