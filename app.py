# app.py
import streamlit as st
import folium
from streamlit_folium import folium_static

# Sample geospatial data
data = [
    {"name": "Asset 1", "location": [28.7041, 77.1025], "status": "active"},  # Delhi, India
    {"name": "Asset 2", "location": [19.0760, 72.8777], "status": "inactive"},  # Mumbai, India
    {"name": "Asset 3", "location": [13.0827, 80.2707], "status": "maintenance"},  # Chennai, India
]

def main():
    st.title("Interactive Geospatial Data Visualization")

    # Sidebar for filtering
    st.sidebar.title("Filter Options")
    selected_status = st.sidebar.selectbox("Select Status", ["All"] + list(set(asset["status"] for asset in data)))

    # Create a map centered around a specific location
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered on India

    # Add markers to the map
    for asset in data:
        if selected_status == "All" or asset["status"] == selected_status:
            color = "green" if asset["status"] == "active" else "red" if asset["status"] == "inactive" else "orange"
            folium.Marker(location=asset["location"], popup=f"{asset['name']} ({asset['status']})", icon=folium.Icon(color=color)).add_to(m)

    # Display the map using Streamlit
    folium_static(m)

if __name__ == "__main__":
    main()
