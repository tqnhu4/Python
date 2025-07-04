import streamlit as st

def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI).
    BMI = weight (kg) / (height (m))^2
    """
    if height > 0: # Ensure height is not zero to prevent division by zero
        # Convert height from cm to meters if needed (assuming input is in cm)
        # If your input is in meters, remove the division by 100
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)
        return bmi
    else:
        return None # Return None or raise an error for invalid height

def get_bmi_category(bmi):
    """
    Returns the BMI category based on the calculated BMI value.
    Source: WHO BMI classification
    """
    if bmi is None:
        return "Invalid Input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# --- Streamlit Application Layout ---

st.title('BMI Calculator 🏋️‍♀️')

st.write('Enter your weight and height below to calculate your Body Mass Index.')

# Input for Weight (in kg)
# min_value and max_value help in validating input
weight = st.number_input(
    'Enter your weight (kg):',
    min_value=1.0, # Minimum reasonable weight
    max_value=300.0, # Maximum reasonable weight
    value=70.0, # Default starting value
    step=0.1 # Incremental step for the input
)

# Input for Height (in cm)
height = st.number_input(
    'Enter your height (cm):',
    min_value=50.0, # Minimum reasonable height
    max_value=250.0, # Maximum reasonable height
    value=170.0, # Default starting value
    step=0.1
)

# Button to trigger the calculation
# The calculation only runs when this button is clicked
if st.button('Calculate BMI'):
    bmi_value = calculate_bmi(weight, height)

    if bmi_value is not None:
        bmi_category = get_bmi_category(bmi_value)

        st.success('BMI Calculated!') # Display a success message

        # Display the BMI value using st.metric for a prominent display
        st.metric(label="Your BMI", value=f"{bmi_value:.2f}")

        # Display the BMI category
        st.write(f"**Category:** {bmi_category}")

        # Provide some general advice based on category (optional)
        if bmi_category == "Underweight":
            st.info("Consider consulting a healthcare professional for advice on gaining weight healthily.")
        elif bmi_category == "Normal weight":
            st.info("Great! Maintain a healthy lifestyle.")
        elif bmi_category == "Overweight":
            st.warning("Consider healthy diet and exercise. Consult a healthcare professional if concerned.")
        elif bmi_category == "Obesity":
            st.error("It is highly recommended to consult a healthcare professional for guidance on weight management.")
    else:
        st.error("Please enter valid height and weight values.")

st.write('---')
st.write('BMI is a general indicator and may not apply to everyone. Consult a healthcare professional for personalized advice.')
