
# SmartEnergy: Predicting Building Energy Consumption

Welcome to **SmartEnergy**, a platform that predicts energy consumption in buildings using advanced machine learning and data analytics. This application helps building owners and managers make data-driven decisions to optimize energy usage, reduce waste, and improve sustainability.

## Features

- **Building Type**: Choose from Residential, Commercial, or Industrial.
- **Square Footage**: Enter the building's square footage.
- **Number of Occupants**: Specify how many people occupy the building.
- **Appliances Used**: Enter the number of appliances used in the building.
- **Average Temperature**: Provide the building's average temperature in Celsius.
- **Day of Week**: Select whether it's a Weekday or Weekend.
- **Energy Consumption Prediction**: Based on the provided inputs, the platform uses a machine learning model to predict the building's energy consumption in kilowatt-hours (kWh).

## How It Works

1. **User Input**: The user inputs the building type, square footage, number of occupants, number of appliances, average temperature, and day of the week.
2. **Data Processing**: The app processes the input data and passes it to a pre-trained machine learning model.
3. **Prediction**: The app displays the predicted energy consumption of the building in kilowatt-hours (kWh).
4. **Actionable Insights**: The prediction helps building managers optimize energy use, reduce waste, and make decisions that benefit both the environment and operating costs.

## Requirements

### Python 3.x

Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Install Required Libraries

You need to install the following Python libraries:

- **Streamlit**: For building the web app interface.
- **Numpy**: For numerical operations.
- **Scikit-Learn**: For data preprocessing and model building.
- **Pickle**: For loading the pre-trained machine learning model.

To install the necessary libraries, run the following commands:

```bash
pip install streamlit numpy scikit-learn
```

## How to Run

1. **Clone the repository** (if applicable) or download the `building_energy_app.py` file.
2. **Install dependencies**:
   Make sure to install the required libraries as mentioned above.
   
3. **Download the Pre-trained Model**:
   Ensure that you have the pre-trained model file, `pred_building_energy_consumption.pkl`, located in the `model/` folder. If you don't have this model, you'll need to train one and save it as a pickle file.

4. **Run the Streamlit App**:
   In your terminal, navigate to the directory where the file is located and run:

   ```bash
   streamlit run building_energy_app.py
   ```

5. **Open the App**:
   After running the command, the app will be accessible at `http://localhost:8501` in your browser.

## Example

### Input:

- **Building Type**: Commercial
- **Square Footage**: 2500 sq. ft.
- **Number of Occupants**: 10
- **Appliances Used**: 15
- **Average Temperature**: 22°C
- **Day of Week**: Weekday

### Output:

- **Predicted Energy Consumption**: 2465.00 kWh

## How the Model Works

The model was trained using various building parameters (type, square footage, occupancy, appliances, temperature, day of the week) to predict energy consumption in kilowatt-hours (kWh). The app loads the pre-trained model using **Pickle** and uses it to make predictions based on the user's inputs.

**Note**: If you want to use your own model, ensure it is saved as a `.pkl` file and placed in the `model/` folder.

### Example code for loading your own model:

```python
import pickle

# Load pre-trained model
pipe = pickle.load(open("model/pred_building_energy_consumption.pkl", "rb"))

# Make predictions using the model
prediction = pipe.predict(input_data)
```

## Contributing

Feel free to contribute to this project! If you have suggestions for improvements or find bugs, open an issue or submit a pull request.

## License

This application is provided under the Apache License. See the [LICENSE](license/LICENSE) file for more details.
