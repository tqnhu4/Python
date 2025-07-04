# Learn Streamlit in 7 Days
This guide will walk you through the fundamentals of Streamlit, a powerful and easy-to-use Python library for creating beautiful custom web apps for machine learning and data science. Each day builds upon the previous day's knowledge.


## Day 1: 🚀 Getting Started & Your First App
Goal: Install Streamlit and create a simple "Hello, World!" app.

Concepts:

- Installation
- streamlit run command
- st.write()
- st.title()
- st.header()
- st.text()
Steps:

- Install Streamlit:
Open your terminal or command prompt and run:
```bash
pip install streamlit
```

- Create your first app (app.py):
```python
# app.py
import streamlit as st

st.title("My First Streamlit App")
st.header("Hello, Streamlit!")
st.write("This is my very first Streamlit application.")
st.text("You're going to love this!")
```

- Run your app:
  Navigate to the directory where you saved app.py in your terminal and run:

```bash
streamlit run app.py
```

This will open your app in your web browser.

### Code Example:

```python
# Day 1: app.py
import streamlit as st

st.title("My First Streamlit App")
st.header("Hello, Streamlit!")
st.write("This is my very first Streamlit application.")
st.text("You're going to love this!")

# You can also use Markdown with st.write()
st.write("## Subheader with Markdown")
st.write("Here's some **bold text** and *italic text*.")

```

## Day 2: 📊 Displaying Data & Interactive Widgets
Goal: Learn how to display dataframes and introduce basic interactive widgets.

### Concepts:

- st.dataframe()
- st.table()
- st.text_input()
- st.number_input()
- st.checkbox()
- st.button()
### Steps:

- Displaying DataFrames: Use st.dataframe() to show Pandas DataFrames.
- Getting User Input:
  - st.text_input() for string input.
  - st.number_input() for numerical input.
  - st.checkbox() for boolean toggles.
  - st.button() for simple actions.
### Code Example:

```python
# Day 2: app_day2.py
import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Display and Basic Widgets")

st.header("Displaying DataFrames")
data = pd.DataFrame({
    'Column A': [1, 2, 3, 4],
    'Column B': [10, 20, 30, 40]
})
st.dataframe(data)

st.subheader("Interactive Widgets")

user_name = st.text_input("Enter your name:")
if user_name:
    st.write(f"Hello, {user_name}!")

age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
st.write(f"You are {age} years old.")

if st.checkbox("Show secret message"):
    st.write("The secret is... Streamlit is awesome!")

if st.button("Click me!"):
    st.write("Button clicked!")

st.write("---")
st.write("More data display:")
st.table(data.head(2)) # Displays a static table
```

## Day 3: 📈 Visualizations & Media
### Goal: Integrate common Python plotting libraries and display images/videos.

### Concepts:

- st.line_chart()
- st.bar_chart()
- st.map()
- st.image()
- st.video()
- matplotlib and seaborn integration
### Steps:

- Streamlit's Built-in Charts: Use st.line_chart(), st.bar_chart(), st.area_chart() for quick visualizations.
- Plotting with Matplotlib/Seaborn: Display plots from matplotlib and seaborn using st.pyplot().
- Displaying Media: Show images and videos with st.image() and st.video().
### Code Example:

```python
# Day 3: app_day3.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Visualizations and Media")

st.header("Streamlit Built-in Charts")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
st.bar_chart(chart_data)

st.subheader("Matplotlib and Seaborn Integration")
fig, ax = plt.subplots()
ax.scatter(x=chart_data['a'], y=chart_data['b'])
ax.set_title("Scatter Plot (Matplotlib)")
st.pyplot(fig) # Pass the figure object

st.subheader("Geospatial Data (st.map)")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], # Example San Francisco coordinates
    columns=['lat', 'lon']
)
st.map(map_data)

st.subheader("Displaying Media")
# You'll need an image file named 'sample_image.jpg' in the same directory
# st.image("sample_image.jpg", caption="A sample image", use_column_width=True)

# You'll need a video file named 'sample_video.mp4' in the same directory
# st.video("sample_video.mp4")

st.write("---")
st.write("If you want to try `st.image` or `st.video`, replace the commented lines with actual file paths.")
st.write("For an image, you can download one and put it in the same folder as your script.")
st.write("Example: `st.image('https://www.streamlit.io/images/brand/streamlit-logo-primary-dark.svg', caption='Streamlit Logo')`")
```

## Day 4: 🏗️ Layouts & User Input Advanced
### Goal: Organize your app with sidebars and columns, and explore more input widgets.

### Concepts:

- st.sidebar
- st.columns()
- st.slider()
- st.selectbox()
- st.multiselect()
- st.radio()
### Steps:

- Sidebar: Place widgets and information in a collapsible sidebar.
- Columns: Arrange content in multiple columns for better layout.
- Advanced Inputs:
  - st.slider() for numerical ranges.
  - st.selectbox() for single selection from a list.
  - st.multiselect() for multiple selections.
  - st.radio() for mutually exclusive choices.
## Code Example:

```python
# Day 4: app_day4.py
import streamlit as st
import pandas as pd
import numpy as np

st.title("Layouts and Advanced Input Widgets")

st.sidebar.header("Sidebar Controls")
option = st.sidebar.selectbox(
    "Which number do you like best?",
    (1, 2, 3, 4, 5)
)
st.sidebar.write(f"You selected: {option}")

st.sidebar.slider_val = st.sidebar.slider(
    "Select a range",
    min_value=0, max_value=100, value=(25, 75)
)
st.sidebar.write(f"Selected range: {st.sidebar.slider_val}")


st.header("Main Content Area")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Column 1")
    st.write("This is content for column 1.")
    selected_fruit = st.selectbox(
        "Choose a fruit:",
        ["Apple", "Banana", "Orange", "Grape"]
    )
    st.write(f"You chose: {selected_fruit}")

with col2:
    st.subheader("Column 2")
    st.write("This is content for column 2.")
    selected_colors = st.multiselect(
        "Choose your favorite colors:",
        ["Red", "Green", "Blue", "Yellow", "Purple"]
    )
    st.write(f"You chose: {', '.join(selected_colors)}")

with col3:
    st.subheader("Column 3")
    st.write("This is content for column 3.")
    radio_choice = st.radio(
        "Select an option:",
        ("Option A", "Option B", "Option C")
    )
    st.write(f"You selected: {radio_choice}")

st.write("---")
st.write("Layouts help organize your app for better user experience.")
```

## Day 5: 🔄 State Management & Performance
### Goal: Understand how Streamlit re-runs and how to manage application state efficiently.

### Concepts:

- Streamlit's execution model (re-runs)
- st.cache_data()
- st.cache_resource()
- Session State (st.session_state)
### Steps:

- Understanding Re-runs: Learn that Streamlit scripts run from top to bottom on every user interaction.
- Caching: Use @st.cache_data for data loading/processing functions and @st.cache_resource for resources that need to be initialized once (like ML models).
- Session State: Persist information across re-runs using st.session_state.
### Code Example:

```python
# Day 5: app_day5.py
import streamlit as st
import time
import pandas as pd

st.title("State Management and Performance")

st.header("Streamlit's Execution Model")
st.write("Every interaction re-runs the script from top to bottom.")
if st.button("Click to re-run"):
    st.write("The script just re-ran!")

st.header("Caching with `@st.cache_data` and `@st.cache_resource`")

@st.cache_data
def load_data():
    st.write("Loading data... (This message appears only once per run)")
    time.sleep(2) # Simulate heavy data loading
    return pd.DataFrame(
        {'Value': [10, 20, 30, 40],
         'Category': ['A', 'B', 'C', 'D']}
    )

data = load_data()
st.dataframe(data)

@st.cache_resource
def initialize_model():
    st.write("Initializing model... (This message appears only once)")
    time.sleep(3) # Simulate heavy model loading
    return "My Pre-trained ML Model"

model = initialize_model()
st.write(f"Model loaded: {model}")

st.subheader("Session State (`st.session_state`)")

# Initialize session state variable if it doesn't exist
if 'counter' not in st.session_state:
    st.session_state.counter = 0

st.write(f"Current counter: {st.session_state.counter}")

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.rerun() # Forces a re-run to update the display

st.write("Session state allows you to store and retrieve values across re-runs.")
```

## Day 6: 📤 File Uploads & Custom Components
### Goal: Allow users to upload files and explore the concept of custom components (briefly).

### Concepts:

- st.file_uploader()
- Working with uploaded files (CSV, images)
- Introduction to custom components (conceptual)
### Steps:

- File Uploader: Use st.file_uploader() to let users upload files.
- Processing Uploaded Files: Read and process the uploaded content (e.g., read CSV into a DataFrame).
- Custom Components (Theory): Understand that Streamlit allows extending functionality with custom components (often built with React, but you can use existing ones). This is more advanced but good to know.
### Code Example:

```python
# Day 6: app_day6.py
import streamlit as st
import pandas as pd
from PIL import Image # For image processing

st.title("File Uploads and Custom Components (Conceptual)")

st.header("File Uploader")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

uploaded_image = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.write("Image uploaded successfully!")
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

st.subheader("Custom Components (Advanced - Conceptual)")
st.write("Streamlit allows you to extend its functionality by building custom components.")
st.write("These can be used to integrate more complex UI elements or JavaScript libraries.")
st.write("You can also find many existing custom components in the Streamlit Component Gallery.")
st.write("Example: `pip install streamlit_option_menu` for a custom navigation menu.")
# You would then use it like:
# from streamlit_option_menu import option_menu
# with st.sidebar:
#     selected = option_menu(
#         menu_title="Main Menu",  # required
#         options=["Home", "Projects", "Contact"],  # required
#         icons=["house", "book", "envelope"],  # optional
#         menu_icon="cast",  # optional
#         default_index=0,  # optional
#     )
# st.write(f"Selected option: {selected}")
```

## Day 7: ☁️ Deployment & Further Learning
### Goal: Understand how to deploy your Streamlit app and where to find more resources.

### Concepts:

- Deployment options (Streamlit Cloud, Heroku, Docker)
- requirements.txt
- Community and documentation
### Steps:

- Deployment Overview: Learn about different ways to deploy your Streamlit app.
- Streamlit Cloud (Recommended for quick deployment): Easiest way, directly from your GitHub repository.
- Heroku, AWS, Google Cloud, Azure (more involved, requiring Docker or specific configurations).
- requirements.txt: Create a requirements.txt file listing all your Python dependencies. This is crucial for deployment.
- Further Learning: Explore the official documentation, community forums, and examples.

### Code Example (Conceptual - no runable app for deployment):

1. app.py (your main app from previous days)

```python
# Day 7: app.py (Imagine this is your polished app)
import streamlit as st
import pandas as pd

st.title("My Deployed Streamlit App")
st.write("This is a simple app demonstrating deployment readiness.")

st.sidebar.header("About")
st.sidebar.info("This app showcases what you've learned in 7 days.")

# Example of a simple feature
number = st.slider("Select a number:", 0, 10)
st.write(f"You selected: {number}")

st.success("Congratulations on completing the 7-day Streamlit guide!")
```

2. requirements.txt (in the same directory as app.py)

```text
streamlit
pandas
numpy
matplotlib
seaborn
Pillow # If you used st.image with local files
# Add any other libraries your app uses
```

### Deployment with Streamlit Cloud:

- Push your app.py and requirements.txt (and any other necessary files like images) to a GitHub repository.
- Go to Streamlit Cloud.
- Connect your GitHub account.
- Select your repository and the main branch.
- Specify the main file (app.py).
- Click "Deploy!"
### Further Learning Resources:

- Official Streamlit Documentation: https://docs.streamlit.io/
- Streamlit Gallery: https://streamlit.io/gallery (See examples of what's possible)
- Streamlit Community Forum: https://discuss.streamlit.io/ (Ask questions, get help)
- YouTube Tutorials: Search for "Streamlit tutorial" for video guides.