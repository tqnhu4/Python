
-----

## Building a Keyword Text Search App with Streamlit

This guide will walk you through creating a simple Streamlit application where users can input a block of text and then search for specific keywords within that text. You'll learn how to use `st.text_area`, `st.text_input`, and basic Python string manipulation.

### Project Goal

The primary goal is to build an interactive tool where you can:

1.  **Input Text:** Provide a large block of text.
2.  **Enter Keywords:** Specify one or more keywords to find.
3.  **Search & Display Results:** Show whether the keywords were found and how many times they appeared.

### Key Streamlit and Python Concepts You'll Learn

  * `st.text_area`: For multi-line text input (your main content).
  * `st.text_input`: For single-line text input (your keywords).
  * Basic Python String Processing: `lower()`, `split()`, `strip()`, `in` operator, and `count()`.

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

First, make sure you have Streamlit installed. If not, open your terminal or command prompt and run:

```bash
pip install streamlit
```

Next, create a new Python file (e.g., `keyword_search_app.py`).

#### Step 2: Import Streamlit and Set Up the Page

Start by importing the `streamlit` library. It's good practice to set up your page configuration for a better user experience.

```python
import streamlit as st

def main():
    # Configure the page title and layout
    st.set_page_config(page_title="Keyword Text Search", layout="centered")

    # Add a title and description for your app
    st.title("Text Search by Keyword")
    st.write("Enter your text below and then provide keywords to find them within the text.")
```

  * `st.set_page_config()`: This function allows you to set global properties for your Streamlit app, like the browser tab title (`page_title`) and the layout (`centered` or `wide`).
  * `st.title()` and `st.write()`: These are used to add a main title and a brief description to your application.

#### Step 3: Create the Text Input Areas

Now, let's add the input fields where users will type or paste their text and keywords.

```python
    # Input for the main text content
    text_content = st.text_area(
        "Enter your text here:",
        height=250, # Sets the height of the text area
        help="Paste or type the text you want to search." # Provides a tooltip for the user
    )

    # Input for the keywords
    keyword_input = st.text_input(
        "Enter keywords (comma-separated):",
        help="Enter one or more keywords, separated by commas (e.g., apple, orange, banana)."
    )
```

  * `st.text_area()`: This widget is perfect for receiving multi-line text.
      * The first argument is the label that appears above the text area.
      * `height` controls the visible height in pixels.
      * `help` provides a small tooltip when the user hovers over the input field.
  * `st.text_input()`: This widget is used for single-line text input, ideal for keywords.
      * Similar to `text_area`, it takes a label and a `help` message.

#### Step 4: Implement the Search Logic

This is where you'll use basic Python string manipulation to process the input and find the keywords. We'll also add a button to trigger the search.

```python
    # Button to trigger the search
    # The search will also run if the keyword_input changes, which is useful
    if st.button("Search Text") or keyword_input:
        # Basic validation: Check if text content is provided
        if not text_content:
            st.warning("Please enter some text to search within.")
            return # Stop execution if no text is provided

        # Basic validation: Check if keywords are provided
        if not keyword_input:
            st.info("Please enter at least one keyword to search for.")
            return

        # 1. Process Keywords: Split by comma, remove whitespace, convert to lowercase
        keywords = [k.strip().lower() for k in keyword_input.split(',') if k.strip()]

        # Check if any valid keywords were extracted after processing
        if not keywords:
            st.info("No valid keywords entered. Please enter keywords separated by commas.")
            return

        # Prepare the main text for search: Convert to lowercase to ensure case-insensitive search
        text_lower = text_content.lower()

        # Dictionary to store found keywords and their counts
        found_keywords = {}

        # 2. Iterate through each keyword and search in the text
        for keyword in keywords:
            if keyword in text_lower:
                # 3. Count occurrences of the keyword
                count = text_lower.count(keyword)
                found_keywords[keyword] = count

        # 4. Display Results
        if found_keywords:
            st.success("Keywords found!")
            for keyword, count in found_keywords.items():
                st.write(f"- The keyword **'{keyword}'** was found **{count}** time(s).")
        else:
            st.info("No matching keywords were found in the text.")
```

  * **`if st.button("Search Text") or keyword_input:`**: This condition means the code inside will execute either when the "Search Text" button is clicked OR when the `keyword_input` field is changed (which provides a more interactive feel without needing to always click the button).
  * **Input Validation:** `if not text_content:` and `if not keyword_input:` check if the user has provided any input. `st.warning()` and `st.info()` display informative messages.
  * **Keyword Processing (`keywords = [...]`):**
      * `keyword_input.split(',')`: Splits the input string into a list of strings based on the comma delimiter.
      * `k.strip()`: Removes any leading or trailing whitespace from each keyword.
      * `k.lower()`: Converts each keyword to lowercase. This is crucial for a **case-insensitive search**, meaning "Apple" will match "apple" in the text.
      * `if k.strip()`: This filters out empty strings that might result from extra commas (e.g., "apple,,banana").
  * **Text Preparation (`text_lower = text_content.lower()`):** The entire input text is converted to lowercase for consistent, case-insensitive matching with the keywords.
  * **Searching (`if keyword in text_lower:`):** The `in` operator efficiently checks if a substring (your keyword) exists within another string (your text).
  * **Counting Occurrences (`text_lower.count(keyword)`):** The `count()` method returns the number of non-overlapping occurrences of the substring in the string.
  * **Displaying Results (`st.success()`, `st.info()`, `st.write()`):**
      * `st.success()`: Displays a success message in green.
      * `st.info()`: Displays an informational message in blue.
      * `st.write()`: A versatile function to display almost anything in Streamlit. We use f-strings for formatted output.

#### Step 5: Run the Application

Finally, add the standard Python entry point to run your Streamlit application.

```python
if __name__ == "__main__":
    main()
```

  * `if __name__ == "__main__":`: This is a standard Python idiom that ensures the `main()` function is called only when the script is executed directly (not when imported as a module).

-----

### Complete Code Example

```python
import streamlit as st

def main():
    st.set_page_config(page_title="Keyword Text Search", layout="centered")

    st.title("Text Search by Keyword")
    st.write("Enter your text below and then provide keywords to find them within the text.")

    # Input for the main text
    text_content = st.text_area(
        "Enter your text here:",
        height=250,
        help="Paste or type the text you want to search."
    )

    # Input for the keywords
    keyword_input = st.text_input(
        "Enter keywords (comma-separated):",
        help="Enter one or more keywords, separated by commas (e.g., apple, orange, banana)."
    )

    # Process search when button is clicked or on keyword input change
    if st.button("Search Text") or keyword_input:
        if not text_content:
            st.warning("Please enter some text to search within.")
            return

        if not keyword_input:
            st.info("Please enter at least one keyword to search for.")
            return

        # Process keywords: split, strip whitespace, convert to lowercase
        keywords = [k.strip().lower() for k in keyword_input.split(',') if k.strip()]

        if not keywords:
            st.info("No valid keywords entered. Please enter keywords separated by commas.")
            return

        # Prepare the main text for case-insensitive search
        text_lower = text_content.lower()

        found_keywords = {}

        # Search for each keyword
        for keyword in keywords:
            if keyword in text_lower:
                count = text_lower.count(keyword) # Count occurrences
                found_keywords[keyword] = count

        # Display results
        if found_keywords:
            st.success("Keywords found!")
            for keyword, count in found_keywords.items():
                st.write(f"- The keyword **'{keyword}'** was found **{count}** time(s).")
        else:
            st.info("No matching keywords were found in the text.")

if __name__ == "__main__":
    main()
```

-----

### How to Run Your Application

1.  **Save the code:** Save the complete code above as a Python file (e.g., `keyword_search_app.py`).

2.  **Open your terminal/command prompt:** Navigate to the directory where you saved the file.

3.  **Run the Streamlit app:** Execute the following command:

    ```bash
    streamlit run app.py
    ```

    Your web browser should automatically open to display your Streamlit application\!

