
import streamlit as st


gps_component = st.components.v2.component(
    "gps_component",
    html="""
        <p id="gps-status">Requesting location...</p>
    """,
    js="""
        export default function({ parentElement, setStateValue }) {

            const status = parentElement.querySelector("#gps-status");

            if (!navigator.geolocation) {
                status.textContent =
                    "Geolocation is not supported by this browser.";
                return;
            }

            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const latitude = position.coords.latitude;
                    const longitude = position.coords.longitude;

                    status.textContent = "Location found!";

                    setStateValue("latitude", latitude);
                    setStateValue("longitude", longitude);
                },

                (error) => {
                    status.textContent =
                        "Location error " +
                        error.code +
                        ": " +
                        error.message;

                    console.error("Geolocation error:", error);
                },

                {
                    enableHighAccuracy: true,
                    timeout: 15000,
                    maximumAge: 60000
                }
            );
        }
    """
)


def get_gps():
    result = gps_component(
        default={
            "latitude": None,
            "longitude": None
        },
        on_latitude_change=lambda: None,
        on_longitude_change=lambda: None,
        key="gps"
    )

    if result.latitude is None or result.longitude is None:
        return None

    return [result.longitude, result.latitude]
