import streamlit as st

# Set page configuration for better UI
st.set_page_config(page_title="BMI Calculator", layout="centered")

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height * height)

# App Title
st.title("BMI Calculator")

# Instructions
st.write("""
    This app calculates your Body Mass Index (BMI).
    - BMI is a simple index of weight-for-height commonly used to classify underweight, normal weight, overweight, and obesity in adults.
""")

# Input Fields for Weight and Height with Sliders
st.sidebar.header("Enter your details")
weight = st.sidebar.slider("Weight (kg)", min_value=1, max_value=500, value=70, step=1)
height = st.sidebar.slider("Height (m)", min_value=0.5, max_value=3.0, value=1.75, step=0.01)

# Calculate BMI
if st.sidebar.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: **{bmi:.2f}**")

        # Categorize BMI
        if bmi < 18.5:
            st.write("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.write("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.write("Category: Overweight")
        else:
            st.write("Category: Obese")
    else:
        st.error("Please enter valid weight and height.")
