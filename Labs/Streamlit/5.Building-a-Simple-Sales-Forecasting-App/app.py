import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def main():
    st.set_page_config(page_title="Simple Sales Forecasting", layout="centered")

    st.title("💰 Simple Sales Forecasting App")
    st.write("Predict sales based on a single input variable using Linear Regression.")
    st.markdown("---")

    # --- 1. Data Generation (Simulated Sales Data) ---
    st.subheader("1. Data Generation (Simulated Sales Data)")
    np.random.seed(42) # for reproducibility

    num_samples = 100
    advertising_spend = np.random.rand(num_samples, 1) * 100 # values between 0 and 100
    sales = 50 + 1.5 * advertising_spend + np.random.randn(num_samples, 1) * 20 

    data = pd.DataFrame({
        'Advertising Spend': advertising_spend.flatten(),
        'Sales': sales.flatten()
    })

    st.write("Here's a sneak peek at the simulated data:")
    st.dataframe(data.head())
    st.markdown("---")

    # --- 2. Model Training (Linear Regression) ---
    st.subheader("2. Model Training (Linear Regression)")

    X = data[['Advertising Spend']] # Features (must be 2D)
    y = data['Sales'] # Target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    st.success("Linear Regression Model Trained Successfully!")
    st.write(f"**Model Coefficient (Slope):** {model.coef_[0]:.2f}")
    st.write(f"**Model Intercept:** {model.intercept_:.2f}")

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.write(f"**Mean Squared Error (MSE) on Test Set:** {mse:.2f}")
    st.write(f"**R-squared (R2) on Test Set:** {r2:.2f}")
    st.info("R-squared indicates how well the model fits the data (closer to 1 is better).")
    st.markdown("---")

    # --- 3. Make a Sales Prediction ---
    st.subheader("3. Make a Sales Prediction")

    min_spend = float(data['Advertising Spend'].min())
    max_spend = float(data['Advertising Spend'].max())

    input_spend = st.slider(
        "Select your Advertising Spend ($):",
        min_value=min_spend,
        max_value=max_spend,
        value=(min_spend + max_spend) / 2,
        step=0.1
    )

    predicted_sales = model.predict(np.array([[input_spend]]))[0]

    st.markdown(f"With an **Advertising Spend of ${input_spend:.2f}**, the predicted **Sales** are:")
    st.metric(label="Predicted Sales", value=f"${predicted_sales:.2f}")
    st.markdown("---")

    # --- 4. Visualization of Data and Prediction ---
    st.subheader("4. Visualization of Data and Prediction")

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(data['Advertising Spend'], data['Sales'], color='blue', label='Actual Data Points')

    x_line = np.linspace(min_spend, max_spend, 100).reshape(-1, 1)
    y_line = model.predict(x_line)
    ax.plot(x_line, y_line, color='red', label='Regression Line')

    ax.scatter(input_spend, predicted_sales, color='green', s=200, marker='X', label=f'Predicted Sales (${predicted_sales:.2f})')

    ax.set_xlabel("Advertising Spend ($)")
    ax.set_ylabel("Sales ($)")
    ax.set_title("Sales vs. Advertising Spend with Linear Regression")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)

    st.pyplot(fig)

if __name__ == "__main__":
    main()