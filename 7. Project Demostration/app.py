import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="*****************")

# Function to generate itinerary
def generate_itinerary(destination, days, nights):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Create a detailed travel itinerary for {destination}
    for {days} days and {nights} nights.

    Include daily activities, attractions, and food suggestions.
    """

    response = model.generate_content(prompt)

    return response.text


# Streamlit UI
st.title("Travel Itinerary Generator ✈️")

destination = st.text_input("Enter Destination")
days = st.number_input("Number of Days", min_value=1)
nights = st.number_input("Number of Nights", min_value=0)

if st.button("Generate Itinerary"):

    if destination.strip() == "":
        st.error("Please enter a destination")
    else:
        with st.spinner("Generating itinerary..."):
            result = generate_itinerary(destination, days, nights)

        st.text_area("Your Travel Plan:", result, height=400)
