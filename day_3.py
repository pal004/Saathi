# day2_maitri_demo.py
# day3.py
import streamlit as st
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def run():
    st.title("SAATHI Speaks (Part 3)")
    st.write("Type something and SAATHI will say it out loud")

    text_input = st.text_area("Enter what you want SAATHI to speak:")

    if st.button("Speak"):
        if text_input.strip():
            speak_text(text_input)
            st.success("SAATHI just spoke your words aloud! ")
        else:
            st.warning("Please type something first.")
