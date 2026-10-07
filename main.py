import random
import streamlit as st
from util.restu_finder import get_restaurants
from util.location import get_location
import random

st.title("restaurant Picker")

st.write("Welcome to the restaurant Picker app!.")
st.write("This app will randomly select a restaurant for you.")

location = st.text_input("Enter your Zipcode", key="location")

if st.button("Get restaurants"):
    if location == "":
        st.error("Zipcode field cannot be empty.")
    else:
        # st.write(f"Your location: {get_location(location)}")
        restaurants = get_restaurants(get_location(location))
        # st.write(f"Found {len(restaurants)} restaurants:")
        # st.write(restaurants)
        choices = []
        for restaurant in restaurants:
            if "name" in restaurant["properties"]:
                choices.append({"name":(restaurant["properties"]["name"]),
                "address":(restaurant["properties"]["address_line2"].strip(", United States of America"))})
        eat_at = (random.choice(choices))
        st.balloons()
        st.write(f"You should eat at {eat_at['name']} located at {eat_at['address']}.")