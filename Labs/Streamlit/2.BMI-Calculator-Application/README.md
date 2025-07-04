## How to Run This Application:
Save the Code: Save the Python code above into a file named bmi_app.py (or any .py file name).

Install Streamlit: If you haven't already, open your terminal or command prompt and run:

Create virtual environment (venv)

```
python3 -m venv myenv
source myenv/bin/activate      # Trên Linux/macOS
# or
myenv\Scripts\activate.bat     # Trên Windows
```


```

pip install streamlit
```
Run the App: Navigate to the directory where you saved bmi_app.py in your terminal, and then execute:

```

streamlit run app.py
```
This command will open a new tab in your web browser, showing the BMI Calculator. You can then input different values for weight and height, click "Calculate BMI", and see the results update dynamically!