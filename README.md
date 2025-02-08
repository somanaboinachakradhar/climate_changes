# Hackathon Project

## Project Overview
This project is a climate prediction dashboard built using Dash and Plotly. It predicts future average temperatures based on various climate-related features and provides precautionary actions based on the predictions. The dashboard aims to raise awareness about climate change and help communities prepare for future climate conditions.

## Files
- `package-lock.json`: Contains the dependency tree of the project.
- `climate_pridiction.py`: Main script for the Dash application that handles data processing, model training, prediction, and visualization.
- `requirements.txt`: Lists all the dependencies required to run the project.
- `README.md`: Provides an overview and instructions for the project.
- `assets/`: Contains static files like CSS and images used in the dashboard.

## Requirements
- Python 3.x
- Dash
- Plotly
- Pandas
- NumPy
- Scikit-learn

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd /climate_changes
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Ensure you have the `climate_change_dataset.csv` file in the project directory.
2. Run the Dash application:
    ```bash
    python climate_pridiction.py
    ```
3. Open your web browser and go to `http://127.0.0.1:8050/` to view the dashboard.

## Features
- **Temperature Prediction**: Predicts average temperatures for the years 2026-2030.
- **Precautionary Actions**: Provides precautionary actions based on predicted temperatures.
- **Visualizations**: Includes a line graph for temperature predictions and a pie chart for energy source distribution.
- **Interactive Dashboard**: Users can interact with the visualizations to explore different aspects of the data.
- **Data Filtering**: Allows users to filter data based on specific criteria such as country or year.

## Data Handling
- Missing values in numerical columns are filled with the mean of the respective columns.
- Missing values in the 'Country' column are filled with the mode of the column.
- Data is normalized to ensure consistent scaling across features.

## Model
- Uses Linear Regression to predict future average temperatures based on features such as CO2 emissions, rainfall, population, renewable energy percentage, and forest area percentage.
- The model is trained on historical climate data to ensure accurate predictions.

## Precautions
- Provides different levels of precautionary actions based on the predicted temperature ranges.
- Suggests actions such as increasing green cover, reducing carbon footprint, and preparing for extreme weather conditions.

## License
This project is licensed under the ISC License.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact
For any questions or feedback, please contact the project maintainers at [23955A3304@iare.ac.in].
