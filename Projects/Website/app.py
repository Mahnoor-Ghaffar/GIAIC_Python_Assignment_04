import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# App title
st.title("Data Analysis Dashboard")
st.sidebar.header("Configuration")

# Upload data
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read data
    df = pd.read_csv(uploaded_file)
    
    # Show raw data
    if st.sidebar.checkbox("Show raw data"):
        st.subheader("Raw Data")
        st.write(df)
    
    # Basic statistics
    if st.sidebar.checkbox("Show statistics"):
        st.subheader("Basic Statistics")
        st.write(df.describe())
    
    # Column selection
    selected_column = st.sidebar.selectbox("Select a column to analyze", df.columns)
    
    # Visualization options
    plot_type = st.sidebar.selectbox("Select plot type", 
                                    ["Histogram", "Box Plot", "Line Chart", "Scatter Plot"])
    
    if plot_type == "Histogram":
        st.subheader(f"Histogram of {selected_column}")
        fig, ax = plt.subplots()
        sns.histplot(df[selected_column], kde=True, ax=ax)
        st.pyplot(fig)
        
    elif plot_type == "Box Plot":
        st.subheader(f"Box Plot of {selected_column}")
        fig, ax = plt.subplots()
        sns.boxplot(x=df[selected_column], ax=ax)
        st.pyplot(fig)
        
    elif plot_type == "Line Chart":
        st.subheader(f"Line Chart of {selected_column}")
        fig, ax = plt.subplots()
        ax.plot(df[selected_column])
        st.pyplot(fig)
        
    elif plot_type == "Scatter Plot":
        st.subheader("Scatter Plot")
        x_axis = st.sidebar.selectbox("X-axis", df.columns)
        y_axis = st.sidebar.selectbox("Y-axis", df.columns)
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
        st.pyplot(fig)
        
else:
    st.info("Please upload a CSV file to get started")
    st.write("Or try this sample data:")
    
    # Sample data
    sample_data = pd.DataFrame({
        'A': np.random.randn(100),
        'B': np.random.randint(0, 100, 100),
        'C': np.random.choice(['X', 'Y', 'Z'], 100)
    })
    st.write(sample_data)