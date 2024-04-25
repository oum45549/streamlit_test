import streamlit as st

# Create a text input widget
input_text = st.text_input("Enter some text:")

# Define a function to convert text to blue
def text_to_blue(text):
    return "<p style='color:blue'>" + text + "</p>"

# Display the input text in blue
if input_text:
    st.markdown(text_to_blue(input_text), unsafe_allow_html=True)