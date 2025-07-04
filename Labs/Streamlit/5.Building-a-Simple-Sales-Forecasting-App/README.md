
-----

## Building a Simple Sales Forecasting App with Streamlit

This guide will walk you through creating a Streamlit application that uses a basic Linear Regression model to predict sales based on a user-controlled input (e.g., advertising spend). You'll learn how to integrate machine learning models with Streamlit's interactive widgets and visualization tools.

### Project Goal

The main objective is to build an interactive sales forecasting tool where you can:

1.  **Generate/Load Data:** Create or simulate a simple dataset for sales prediction.
2.  **Train Model:** Use Linear Regression to train a predictive model.
3.  **Interactive Prediction:** Allow users to adjust an input variable (e.g., "Advertising Spend") using a slider.
4.  **Display Forecast:** Show the predicted sales based on the input.
5.  **Visualize:** Plot the data, the regression line, and the prediction point.

### Key Streamlit, Scikit-learn, and Matplotlib Concepts You'll Learn

  * `st.slider`: To create an interactive slider for numerical input.
  * `st.selectbox`: To select different features (if you expand the model).
  * `sklearn.linear_model.LinearRegression`: For building the predictive model.
  * `matplotlib.pyplot`: For creating static plots within Streamlit.
  * Data Generation with `numpy`: For creating synthetic data if you don't have a real dataset handy.

### Create virtual environment (venv)

```
python3 -m venv myenv
source myenv/bin/activate      # Trên Linux/macOS
# or
myenv\Scripts\activate.bat     # Trên Windows
```

-----

### Step-by-Step Implementation

Let's break down the code for your Streamlit application.

#### Step 1: Set Up Your Environment

First, ensure you have the necessary libraries installed. Open your terminal or command prompt and run:

```bash
pip install streamlit pandas numpy scikit-learn matplotlib
```

Next, create a new Python file (e.g., `app.py`).

#### Step 2: Import Libraries and Set Up the Page

Start by importing all the required libraries and configuring your Streamlit page.

```python
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
```

  * **`import` statements**: We're importing Streamlit, Pandas (for data handling), NumPy (for numerical operations, especially data generation), Matplotlib (for plotting), and key modules from Scikit-learn for the model and evaluation.
  * **`st.set_page_config()`**: Sets the browser tab title and uses a `centered` layout.
  * **`st.title()` and `st.write()`**: Add a main title and description.
  * **`st.markdown("---")`**: Adds a horizontal rule for visual separation.

#### Step 3: Generate or Load Sample Data

For a simple example, we'll generate synthetic data. In a real application, you would load this from a CSV using `st.file_uploader` and `pd.read_csv`.

```python
    st.subheader("1. Data Generation (Simulated Sales Data)")
    # Generate synthetic data for demonstration
    np.random.seed(42) # for reproducibility

    # Let's assume 'Advertising Spend' is our independent variable (X)
    # And 'Sales' is our dependent variable (y)
    num_samples = 100
    advertising_spend = np.random.rand(num_samples, 1) * 100 # values between 0 and 100
    
    # Simulate a linear relationship with some noise
    # Sales = 50 + 1.5 * Advertising_Spend + noise
    sales = 50 + 1.5 * advertising_spend + np.random.randn(num_samples, 1) * 20 

    # Create a Pandas DataFrame
    data = pd.DataFrame({
        'Advertising Spend': advertising_spend.flatten(),
        'Sales': sales.flatten()
    })

    st.write("Here's a sneak peek at the simulated data:")
    st.dataframe(data.head())
    st.markdown("---")
```

  * **`np.random.seed(42)`**: Ensures that the random data generated is the same every time you run the script, making your results reproducible.
  * **`np.random.rand()`**: Generates random numbers. We scale them to represent typical "Advertising Spend" values.
  * **Linear relationship + noise**: We define `sales` as a linear function of `advertising_spend` plus some random noise (`np.random.randn() * 20`) to make it more realistic.
  * **`pd.DataFrame(...)`**: Combines the generated arrays into a Pandas DataFrame, which is the standard format for machine learning data.
  * **`st.dataframe(data.head())`**: Displays the first few rows of the generated data.

#### Step 4: Train the Linear Regression Model

This involves splitting the data and training the `LinearRegression` model.

```python
    st.subheader("2. Model Training (Linear Regression)")

    # Define features (X) and target (y)
    X = data[['Advertising Spend']] # Features - must be a 2D array/DataFrame
    y = data['Sales'] # Target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    st.success("Linear Regression Model Trained Successfully!")
    st.write(f"**Model Coefficient (Slope):** {model.coef_[0]:.2f}")
    st.write(f"**Model Intercept:** {model.intercept_:.2f}")

    # Evaluate the model on the test set
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.write(f"**Mean Squared Error (MSE) on Test Set:** {mse:.2f}")
    st.write(f"**R-squared (R2) on Test Set:** {r2:.2f}")
    st.info("R-squared indicates how well the model fits the data (closer to 1 is better).")
    st.markdown("---")
```

  * **`X = data[['Advertising Spend']]`**: Selects the 'Advertising Spend' column as our feature(s). It's crucial to use double brackets `[['Column Name']]` to ensure `X` is a DataFrame (2D array), as Scikit-learn models expect 2D input for features.
  * **`y = data['Sales']`**: Selects the 'Sales' column as our target variable.
  * **`train_test_split()`**: Splits the dataset into training and testing subsets.
      * `test_size=0.2`: 20% of the data will be used for testing, 80% for training.
      * `random_state=42`: Ensures the split is the same every time for reproducibility.
  * **`model = LinearRegression()`**: Initializes the Linear Regression model.
  * **`model.fit(X_train, y_train)`**: Trains the model using the training data. This is where the model learns the relationship between `X` and `y`.
  * **`model.coef_[0]` and `model.intercept_`**: After training, you can access the learned slope (coefficient) and y-intercept of the regression line.
  * **`model.predict(X_test)`**: Uses the trained model to make predictions on the unseen test data.
  * **`mean_squared_error()` and `r2_score()`**: These are common metrics to evaluate regression models.
      * **MSE**: Average of the squared differences between predicted and actual values (lower is better).
      * **R-squared**: Represents the proportion of variance in the dependent variable that can be predicted from the independent variable(s) (closer to 1 is better).

#### Step 5: Interactive Sales Prediction

This section will use `st.slider` for user input and `st.metric` for displaying the prediction.

```python
    st.subheader("3. Make a Sales Prediction")

    # Get the min and max values from our generated 'Advertising Spend' for the slider range
    min_spend = float(data['Advertising Spend'].min())
    max_spend = float(data['Advertising Spend'].max())

    # Create a slider for user input
    input_spend = st.slider(
        "Select your Advertising Spend ($):",
        min_value=min_spend,
        max_value=max_spend,
        value=(min_spend + max_spend) / 2, # Default value in the middle
        step=0.1 # Increments of 0.1
    )

    # Make a prediction based on the slider value
    # The input for predict must also be a 2D array, even for a single value
    predicted_sales = model.predict(np.array([[input_spend]]))[0]

    st.markdown(f"With an **Advertising Spend of ${input_spend:.2f}**, the predicted **Sales** are:")
    st.metric(label="Predicted Sales", value=f"${predicted_sales:.2f}")
    st.markdown("---")
```

  * **`min_spend`, `max_spend`**: We dynamically get the range of our `Advertising Spend` data to set appropriate bounds for the slider.
  * **`st.slider(...)`**:
      * The first argument is the label for the slider.
      * `min_value` and `max_value` define the range of the slider.
      * `value` sets the initial position of the slider.
      * `step` defines how much the value changes when the user drags the slider or uses arrow keys.
  * **`np.array([[input_spend]])`**: Crucially, the `predict()` method of Scikit-learn models expects a 2D array-like input, even if you're predicting for a single value. `[[value]]` creates a 2D array.
  * **`[0]`**: After prediction, `model.predict()` returns an array. We take the first element `[0]` as our single predicted value.
  * **`st.metric()`**: A great widget to display a single, prominent numerical value.

#### Step 6: Visualize the Results

Plot the original data, the regression line, and the prediction point using Matplotlib.

```python
    st.subheader("4. Visualization of Data and Prediction")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot original data points
    ax.scatter(data['Advertising Spend'], data['Sales'], color='blue', label='Actual Data Points')

    # Plot the regression line
    # To plot the line, we need predictions across the entire range of X
    x_range = np.linspace(min_spend, max_spend, 100).reshape(-1, 1)
    y_line = model.predict(x_range)
    ax.plot(x_range, y_line, color='red', label='Regression Line')

    # Plot the prediction point
    ax.scatter(input_spend, predicted_sales, color='green', s=200, marker='X', label=f'Predicted Sales (${predicted_sales:.2f})')

    # Add labels and title
    ax.set_xlabel("Advertising Spend ($)")
    ax.set_ylabel("Sales ($)")
    ax.set_title("Sales vs. Advertising Spend with Linear Regression")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)

    # Display the plot in Streamlit
    st.pyplot(fig)
```

  * **`fig, ax = plt.subplots(figsize=(10, 6))`**: Creates a Matplotlib figure and a single subplot (axes) for plotting.
  * **`ax.scatter(...)`**: Plots the original data points as a scatter plot.
  * **`np.linspace(min_spend, max_spend, 100).reshape(-1, 1)`**: Generates 100 evenly spaced points within the range of `Advertising Spend`. This is used to draw a smooth regression line across the entire data range. `reshape(-1, 1)` makes it a 2D array.
  * **`ax.plot(...)`**: Plots the regression line.
  * **`ax.scatter(input_spend, predicted_sales, ...)`**: Plots a distinct marker (an 'X' in green) for the specific prediction made by the slider.
  * **`ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()`, `ax.legend()`, `ax.grid()`**: Standard Matplotlib functions to add labels, title, a legend, and a grid to the plot for better readability.
  * **`st.pyplot(fig)`**: This is the crucial Streamlit function that renders the Matplotlib figure in your web application.

#### Step 7: Run the Application

Finally, add the standard Python entry point to run your Streamlit application.

```python
if __name__ == "__main__":
    main()
```

  * **`if __name__ == "__main__":`**: Ensures the `main()` function is called only when the script is executed directly.

-----

### Complete Code Example (`app.py`)

```python
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
```

-----

### How to Run Your Application

1.  **Save the code:** Save the complete code above as a Python file (e.g., `app.py`).

2.  **Open your terminal/command prompt:** Navigate to the directory where you saved the file.

3.  **Run the Streamlit app:** Execute the following command:

    ```bash
    streamlit run app.py
    ```
