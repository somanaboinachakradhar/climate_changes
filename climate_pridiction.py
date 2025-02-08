import dash
from dash import dcc, html
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv("climate_change_dataset.csv")

# Handle missing values
df.fillna(df.select_dtypes(include=['number']).mean(), inplace=True)
df['Country'].fillna(df['Country'].mode()[0], inplace=True)

# Select features and target variable
features = df[['Year', 'CO2 Emissions (Tons/Capita)', 'Rainfall (mm)', 'Population', 'Renewable Energy (%)', 'Forest Area (%)']]
target = df['Avg Temperature (°C)']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Future data for prediction (e.g., years 2026-2030)
years_future = pd.DataFrame({
    'Year': [2026, 2027, 2028, 2029, 2030],
    'CO2 Emissions (Tons/Capita)': [7.0, 7.2, 7.5, 7.8, 8.0],
    'Rainfall (mm)': [1000, 1020, 1040, 1060, 1080],
    'Population': [7800000000, 7900000000, 8000000000, 8100000000, 8200000000],
    'Renewable Energy (%)': [20, 22, 24, 25, 27],
    'Forest Area (%)': [30, 29.5, 29, 28.5, 28]
})

# Predict future temperatures
y_future_pred = model.predict(years_future)

# Function to provide precautions based on predicted temperature
def climate_precautions(predicted_temperature):
    precautions = []
    if predicted_temperature > 3:
        precautions.append("Urgent: Immediate global action required to limit carbon emissions and prevent severe global warming.")
        precautions.append("Massive shift to renewable energy sources (solar, wind) is essential.")
        precautions.append("Increase efforts on reforestation and protecting biodiversity.")
        precautions.append("Promote sustainable agricultural practices to reduce emissions.")
        precautions.append("Adapt to the risks of extreme weather events: floods, droughts, and storms.")
    elif 2 <= predicted_temperature <= 3:
        precautions.append("Critical: Strengthening international climate agreements and transitioning to a carbon-neutral economy.")
        precautions.append("Increase the adoption of electric vehicles and sustainable transportation.")
        precautions.append("Boost investments in green technologies and energy-efficient infrastructure.")
        precautions.append("Prepare for severe droughts and floods; invest in climate-resilient infrastructure.")
        precautions.append("Ensure the protection of vulnerable populations from climate impacts.")
    elif 1 <= predicted_temperature < 2:
        precautions.append("Important: Gradual transition to sustainable energy and reduction in carbon emissions.")
        precautions.append("Support conservation of forests and ecosystems that act as carbon sinks.")
        precautions.append("Encourage sustainable water use practices to mitigate the impacts of climate change.")
        precautions.append("Invest in early warning systems for climate-related disasters.")
    else:
        precautions.append("Positive: Continue efforts to reduce carbon emissions and promote sustainable practices.")
        precautions.append("Focus on enhancing global awareness and climate education.")
        precautions.append("Monitor and protect the environment, aiming for a carbon-neutral world.")
    return precautions

# Set up the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Climate Change Predictions and Precautions", style={'textAlign': 'center', 'marginBottom': '30px'}),
    
    # Enhanced Graph for predicted temperature changes
    dcc.Graph(
        id='temp-predictions',
        figure={
            'data': [
                go.Scatter(
                    x=years_future['Year'],
                    y=y_future_pred,
                    mode='lines+markers',
                    name='Predicted Temperature (°C)',
                    line={'color': 'red', 'width': 3},
                    marker={'size': 8}
                ),
            ],
            'layout': go.Layout(
                title='Predicted Average Temperature (°C) for 2026-2030',
                xaxis={'title': 'Year'},
                yaxis={'title': 'Avg Temperature (°C)'},
                hovermode='x unified',
                template='plotly_dark'
            ),
        }
    ),
    
    # Pie Chart for Renewable Energy vs Fossil Fuel Usage
    dcc.Graph(
        figure=go.Figure(
            data=[go.Pie(
                labels=['Renewable Energy (%)', 'Fossil Fuel (%)'],
                values=[years_future['Renewable Energy (%)'].mean(), 100 - years_future['Renewable Energy (%)'].mean()],
                hole=0.4,
                marker=dict(colors=['green', 'gray'])
            )],
            layout=go.Layout(
                title='Average Energy Source Distribution (2026-2030)'
            )
        )
    ),
    
    # Precautions section for future years
    html.Div([
        html.H3("Precautionary Actions Based on Predictions", style={'textAlign': 'center'}),
        html.Div(id='precautions-output', style={'fontSize': 18, 'padding': '20px'}),
    ]),
])

# Callback to display precautions based on temperature predictions
@app.callback(
    dash.dependencies.Output('precautions-output', 'children'),
    [dash.dependencies.Input('temp-predictions', 'relayoutData')]
)
def update_precautions(input_data):
    return html.Div([
        html.Div([
            html.H4(f"Year: {year}", style={'color': 'blue'}),
            html.P(f"Predicted Temperature: {y_future_pred[i]:.2f}°C", style={'fontWeight': 'bold'}),
            html.Ul([html.Li(precaution) for precaution in climate_precautions(y_future_pred[i])]),
        ], style={
            'border': '1px solid #ddd', 'borderRadius': '10px', 'padding': '15px', 'marginBottom': '10px',
            'boxShadow': '2px 2px 10px #aaa', 'backgroundColor': '#f9f9f9'
        })
        for i, year in enumerate(years_future['Year'])
    ])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
