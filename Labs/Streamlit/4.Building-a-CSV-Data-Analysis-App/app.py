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