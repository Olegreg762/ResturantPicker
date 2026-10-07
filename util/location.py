import requests
from requests.structures import CaseInsensitiveDict
import streamlit as st
import json


def get_location(zipcode):
    api_key = st.secrets["API_KEY"]

    url = f"https://api.geoapify.com/v1/geocode/search?text={zipcode}&type=postcode&format=json&limit=1&apiKey={api_key}"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    return [json.dumps(resp.json()["results"][0]['lon']), json.dumps(resp.json()["results"][0]['lat'])]