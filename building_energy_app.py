import streamlit as st
import numpy as np
import pickle as pkl

# Title of the app
st.title("SmartEnergy: Predicting Building Energy Consumption")

# Summary of application
st.write("""**Welcome to our Energy Consumption Prediction Platform**

In an era where sustainability is key, optimizing energy use in buildings is more important than ever. 
Our platform uses advanced data analytics and machine learning to predict energy consumption in real-time. 
By considering factors such as building type, size, occupancy patterns, and environmental conditions like temperature, 
we provide building owners and managers with actionable insights to reduce energy waste.

Our mission is to help create smarter, more sustainable buildings. 
By utilizing cutting-edge technology, we enable better decision-making that leads to cost savings, environmental benefits, and efficient energy use. 
Whether you're managing a single building or an entire portfolio, our solution is designed to promote energy conservation and optimize your building's performance.""")

# Select Building Type
building_type = st.selectbox(
    "Select Building Type", 
    ["Residential", "Commercial", "Industrial"]
)

# Input for Square Footage
square_footage = st.number_input(
    "Enter Square Footage of the Building (in square feet)",
    min_value=1, 
    step=1
)

# Input for Number of Occupants
num_occupants = st.number_input(
    "Enter Number of Occupants in the Building",
    min_value=1, 
    step=1
)

# Input for Appliances Used
appliances_used = st.number_input(
    "Enter Number of Appliances Used in the Building",
    min_value=1, 
    step=1
)

# Input for Average Temperature
avg_temperature = st.number_input(
    "Enter Average Temperature in Celsius",
    min_value=-10.0, 
    max_value=50.0, 
    step=0.1
)

# Select Day of the Week (Weekday or Weekend)
day_of_week = st.radio(
    "Select Day of Week", 
    ["Weekday", "Weekend"]
)

# Submit button and validation
if st.button("Predict Energy Consumption"):
    # Check if all inputs are filled
    if not all([building_type, square_footage, num_occupants, appliances_used, avg_temperature, day_of_week]):
        st.error("Please fill in all fields.")
    else:
        
        # Preparing the feature array
        features = [
            building_type,        # Building Type
            square_footage,       # Square Footage
            num_occupants,        # Number of Occupants
            appliances_used,      # Appliances Used
            avg_temperature,      # Average Temperature
            day_of_week           # Day of Week 
        ]

        # Prepare the input for prediction
        input_data = np.array([features])
        
        # Get the prediction from the ML model
        pipe = pkl.load(open("model\pred_building_energy_consumption.pkl", "rb"))
        prediction = pipe.predict(input_data)

        # Display the entered data
        st.write("### Building Information Summary")
        st.write(f"**Building Type**: {building_type}")
        st.write(f"**Square Footage**: {square_footage} sq. ft.")
        st.write(f"**Number of Occupants**: {num_occupants}")
        st.write(f"**Appliances Used**: {appliances_used}")
        st.write(f"**Average Temperature**: {avg_temperature}°C")
        st.write(f"**Day of Week**: {day_of_week}")
        
        # Display the model's prediction
        st.write(f"### Energy Consumption of Building: {prediction[0]:.2f} kWh (kilowatt-hours)")
