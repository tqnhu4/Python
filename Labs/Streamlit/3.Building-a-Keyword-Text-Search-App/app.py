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