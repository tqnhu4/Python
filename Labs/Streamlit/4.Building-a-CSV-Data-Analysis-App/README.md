
-----

## Building a CSV Data Analysis App with Streamlit

This guide will walk you through creating a Streamlit application that allows users to upload a CSV file, display its content as a table, and show some basic statistics and visualizations.

### Project Goal

The main objective is to create an interactive tool where you can:

1.  **Upload CSV File:** Allow users to upload a `.csv` file.
2.  **Display Table:** Show the uploaded CSV data in a clear, interactive table format.
3.  **Basic Statistics:** Provide summary statistics for numerical columns.
4.  **Visualize Data:** Generate simple charts (e.g., bar charts) for selected columns.

### Key Streamlit and Python Concepts You'll Learn

  * `st.file_uploader`: For handling file uploads.
  * `pandas`: The essential library for data manipulation and analysis in Python.
  * `st.dataframe`: To display Pandas DataFrames as interactive tables.
  * `st.bar_chart`: For creating simple bar charts directly from DataFrame columns.

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

#### Step 1: Set Up Your Streamlit Environment

First, ensure you have Streamlit and Pandas installed. If not, open your terminal or command prompt and run:

```bash
pip install streamlit pandas
```

Next, create a new Python file (e.g., `app.py`).

#### Step 2: Import Libraries and Set Up the Page

Start by importing the necessary libraries and configuring your Streamlit page.

```python
import streamlit as st
import pandas as pd

def main():
    # Configure the page title and layout
    st.set_page_config(page_title="CSV Data Analyzer", layout="wide")

    # Add a title and description for your app
    st.title("CSV Data Analysis Application")
    st.write("Upload your CSV file to view its content, statistics, and visualizations.")
```

  * **`import streamlit as st`**: Imports the Streamlit library.
  * **`import pandas as pd`**: Imports the Pandas library, commonly aliased as `pd`.
  * **`st.set_page_config()`**: Sets up the browser tab title and uses a `wide` layout to give more space for tables and charts.
  * **`st.title()` and `st.write()`**: Add a main title and a brief description to your application.

#### Step 3: Implement CSV File Uploader

This is the core component for getting data into your application.

```python
    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Only proceed if a file has been uploaded
    if uploaded_file is not None:
        try:
            # Read the CSV file into a Pandas DataFrame
            df = pd.read_csv(uploaded_file)
            st.success("CSV file successfully loaded!")

            # --- Display Data Table ---
            st.subheader("Data Table")
            st.dataframe(df) # Displays the DataFrame as an interactive table

            # --- Display Basic Statistics ---
            st.subheader("Basic Statistics")
            st.write(df.describe()) # Shows descriptive statistics for numerical columns

            # --- Data Visualization (Bar Chart) ---
            st.subheader("Data Visualization")

            # Get numerical columns for charting
            numerical_cols = df.select_dtypes(include=['number']).columns.tolist()

            if numerical_cols:
                # Allow user to select a column for bar chart
                selected_column = st.selectbox("Select a column to visualize (Bar Chart):", numerical_cols)

                if selected_column:
                    st.write(f"Bar Chart for **'{selected_column}'**")
                    # Group by the selected column and count occurrences for a simple bar chart
                    # Or, if you want a sum/average, you'd do df.groupby(...)[selected_column].sum()
                    chart_data = df[selected_column].value_counts().reset_index()
                    chart_data.columns = [selected_column, 'Count']
                    st.bar_chart(chart_data.set_index(selected_column))
            else:
                st.info("No numerical columns found for visualization.")

        except Exception as e:
            st.error(f"Error loading or processing file: {e}")
            st.info("Please ensure it's a valid CSV file.")
```

  * **`uploaded_file = st.file_uploader("Choose a CSV file", type="csv")`**:
      * This widget creates a "Browse files" button.
      * `"Choose a CSV file"` is the label.
      * `type="csv"` filters the file selection dialog to only show CSV files and tells Streamlit to expect a CSV.
  * **`if uploaded_file is not None:`**: This condition checks if a file has actually been uploaded by the user. If `None`, it means no file has been selected yet.
  * **`try...except` block**: It's crucial to wrap file reading in a `try...except` block to handle potential errors (e.g., if the user uploads a corrupted file or a non-CSV file, despite the `type="csv"` hint).
  * **`df = pd.read_csv(uploaded_file)`**: This is the Pandas function that reads the uploaded file's content directly into a **DataFrame**. Streamlit passes the uploaded file as a file-like object, which `pd.read_csv` can handle.
  * **`st.success()`**: Displays a green success message.
  * **`st.subheader()`**: Creates smaller, bold headings for different sections of your app.

-----

#### Displaying Data: `st.dataframe`

  * **`st.dataframe(df)`**: This is one of the easiest ways to display a Pandas DataFrame in Streamlit. It renders an interactive table where users can sort columns, search, and resize.

-----

#### Basic Statistics: `df.describe()`

  * **`st.write(df.describe())`**: The `describe()` method of a Pandas DataFrame generates a summary of numerical columns (count, mean, standard deviation, min, max, quartiles). `st.write()` is used to display this summary.

-----

#### Data Visualization: `st.bar_chart`

  * **`numerical_cols = df.select_dtypes(include=['number']).columns.tolist()`**: This line uses Pandas to identify all columns in your DataFrame that have a numerical data type (integers or floats). This ensures you only try to chart appropriate data.
  * **`st.selectbox("Select a column to visualize (Bar Chart):", numerical_cols)`**: If numerical columns exist, this creates a dropdown menu, allowing the user to pick one column for visualization.
  * **`df[selected_column].value_counts().reset_index()`**:
      * `df[selected_column].value_counts()`: Counts the occurrences of each unique value in the `selected_column`. This is great for categorical data or discrete numerical data.
      * `.reset_index()`: Converts the Series returned by `value_counts()` back into a DataFrame, which is often easier to work with for charting.
      * `chart_data.columns = [selected_column, 'Count']`: Renames the columns of the `chart_data` DataFrame for clarity.
  * **`st.bar_chart(chart_data.set_index(selected_column))`**:
      * `chart_data.set_index(selected_column)`: Sets the selected column as the index of the DataFrame. Streamlit's charting functions often use the index for the x-axis.
      * `st.bar_chart()`: Renders a bar chart. It automatically interprets the DataFrame structure to draw the chart.

-----

#### Step 4: Run the Application

Finally, add the standard Python entry point to run your Streamlit application.

```python
if __name__ == "__main__":
    main()
```

  * **`if __name__ == "__main__":`**: This ensures the `main()` function is called only when the script is executed directly.

-----

### Complete Code Example

```python
import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="CSV Data Analyzer", layout="wide")

    st.title("CSV Data Analysis Application")
    st.write("Upload your CSV file to view its content, statistics, and visualizations.")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Only proceed if a file has been uploaded
    if uploaded_file is not None:
        try:
            # Read the CSV file into a Pandas DataFrame
            df = pd.read_csv(uploaded_file)
            st.success("CSV file successfully loaded!")

            # --- Display Data Table ---
            st.subheader("1. Data Table")
            st.dataframe(df)

            # --- Display Basic Statistics ---
            st.subheader("2. Basic Statistics")
            # Display descriptive statistics for numerical columns
            st.write(df.describe())
            
            # Display information about the DataFrame (columns, non-null counts, dtypes)
            st.subheader("DataFrame Info")
            buffer = pd.io.common.StringIO()
            df.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)


            # --- Data Visualization (Bar Chart) ---
            st.subheader("3. Data Visualization")

            # Get all column names
            all_columns = df.columns.tolist()

            # Allow user to select a column for bar chart
            selected_column_for_chart = st.selectbox("Select a column to visualize:", all_columns)

            if selected_column_for_chart:
                # Check if the selected column is numerical or suitable for value_counts
                if pd.api.types.is_numeric_dtype(df[selected_column_for_chart]):
                    st.write(f"Bar Chart for **'{selected_column_for_chart}'**")
                    # For numerical data, a histogram might be better, but a bar chart of value_counts also works for discrete data
                    # Let's do a simple count of unique values, which is versatile.
                    chart_data = df[selected_column_for_chart].value_counts().reset_index()
                    chart_data.columns = [selected_column_for_chart, 'Count']
                    st.bar_chart(chart_data.set_index(selected_column_for_chart))
                elif pd.api.types.is_string_dtype(df[selected_column_for_chart]) or pd.api.types.is_categorical_dtype(df[selected_column_for_chart]):
                    st.write(f"Bar Chart for **'{selected_column_for_chart}'** (Categorical Counts)")
                    # For categorical/string data, value_counts is ideal
                    chart_data = df[selected_column_for_chart].value_counts().reset_index()
                    chart_data.columns = [selected_column_for_chart, 'Count']
                    st.bar_chart(chart_data.set_index(selected_column_for_chart))
                else:
                    st.info(f"Cannot generate a bar chart for '{selected_column_for_chart}' (unsupported data type for this visualization).")

        except pd.errors.EmptyDataError:
            st.error("The uploaded CSV file is empty. Please upload a file with data.")
        except pd.errors.ParserError:
            st.error("Could not parse the CSV file. Please check if it's a valid CSV format.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
            st.info("Please ensure it's a valid CSV file and try again.")

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
