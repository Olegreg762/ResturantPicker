import random
import streamlit as st
from util.restu_finder import get_restaurants
from util.location import get_location
from util.gps import get_gps
st.title("Eats Picker")

st.write("Welcome to the Eats Picker app!")
st.write("This app will randomly select a place for you to eat at.")

location_method = st.radio("How would you like to specify your location?", ("Zipcode", "Current Location"))

if location_method == "Zipcode":
    location = st.text_input("Enter your Zipcode", key="location")
else:
    location = get_gps()
    if location == False:
        st.warning("Failed to get current location. Please enter a zipcode.")
        
location_ready = location is not False and location != ""

if "user_loc" not in st.session_state or st.session_state.user_loc is None:
    
    if st.button("Get restaurants", disabled=not location_ready):
        if location == "":
            st.error("Zipcode field cannot be empty.")
        else:
            
            user_loc = get_location(location) if location_method == "Zipcode" else location
            st.session_state.user_loc = user_loc
            restaurants = get_restaurants(user_loc[1]) if location_method == "Zipcode" else get_restaurants(user_loc)
            
            choices = []
            for restaurant in restaurants:
                if "name" in restaurant["properties"]:
                    choices.append({"name":(restaurant["properties"]["name"]),
                    "address":(restaurant["properties"]["address_line2"].removesuffix(", United States of America"))})
            if choices:
                eat_at = (random.choice(choices))
                st.write(f"You should eat at {eat_at['name']} located at {eat_at['address']}.")
                st.balloons()
                choices.remove(eat_at)
                st.session_state.returned_choices = choices
                if st.button("Try Different Place"):
                        choices = st.session_state.returned_choices
                        eat_at = (random.choice(choices))
                        st.write(f"You should eat at {eat_at['name']} located at {eat_at['address']}.")
                        st.balloons()
                        choices.remove(eat_at)
                        st.write(len(st.session_state.returned_choices))
            else:
                st.warning('No restaurants found, try another location.')
                
else:
    if st.button("Try Different Place"):
        choices = st.session_state.returned_choices
        eat_at = (random.choice(choices))
        st.write(f"You should eat at {eat_at['name']} located at {eat_at['address']}.")
        st.balloons()
        choices.remove(eat_at)
        

    if len(st.session_state.returned_choices) == 0:
        st.write("No more places to choose from. Try a different location.")
        st.session_state.user_loc = None
