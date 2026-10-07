import requests
from requests.structures import CaseInsensitiveDict
import streamlit as st

def get_restaurants(location):

    api_key = st.secrets["API_KEY"]
    lon = location[0]
    lat = location[1]
    location = f"circle:{lon},{lat},5000&bias=proximity:{lon},{lat}"

    url = f"https://api.geoapify.com/v2/places?categories=catering.restaurant,catering.fast_food&filter={location}&limit=200&apiKey={api_key}"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    return(resp.json()['features'])