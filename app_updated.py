import streamlit as st
import day_1, day_2, day_3, day_4, day_6   # include day_6

# Map pages to their run() functions
PAGES = {
    "Part 1 - Intro": day_1,
    "Part 2 - Emotion Recognition": day_2,
    "Part 3 - Speech": day_3,
    "Part 4 - Memory (DB)": day_4,
    "Part 5 - Physical Well-being": day_6
}

def main():
    st.sidebar.title("Saathi's Navigation")
    choice = st.sidebar.radio("Go to:", list(PAGES.keys()))
    page = PAGES[choice]
    page.run()   # each day file should have a `run()` function

if __name__ == "__main__":
    main()
