'''
StreamSage is a Streamlit app that allows users to explore a wide range of 
TV shows from various streaming providers and channels. 

Overview

The app provides a user-friendly interface where users can filter TV shows by 
streaming provider, genre, and language. The main panel of the app displays the 
TV shows that match the selected filters. Users can select a show to get more 
information about it, including the name, language, genres, runtime, rating, and summary.

Architecture

The app is built with Streamlit, a Python library for creating web apps. It fetches 
TV show data from the TVmaze API and extracts unique channels, genres, and languages 
from the data. These are used to populate the filters in the app.

The app uses the BeautifulSoup library to parse the summary of the selected show. 
The parsed summary is then displayed in the app.

Usage

To run the app, you need to have Streamlit, BeautifulSoup, and requests installed. 
You can install these packages with pip:

'''

import requests
import streamlit as st
from bs4 import BeautifulSoup

# Fetch data from TVmaze API
url = "http://api.tvmaze.com/shows"
response = requests.get(url)
data = response.json()

# Extract unique channels from the data
channels = set(show['network']['name'] for show in data if show['network'])

# Your original list of streaming providers
STREAMING_PROVIDERS = ["Netflix", "Hulu", "Prime Video", "Disney+", "HBO"]

# Add the channels from TVmaze to your list
STREAMING_PROVIDERS.extend(channels)

# Remove duplicates (if any)
STREAMING_PROVIDERS = list(set(STREAMING_PROVIDERS))

# Extract unique genres and languages
genres = list(set(genre for show in data for genre in show['genres']))
languages = list(set(show['language'] for show in data if show['language']))

# Streamlit app
st.markdown("""
<center>

# Welcome to StreamSage: Your All-in-One Streaming Companion!

</center>

Explore a wide range of TV shows from various streaming providers and channels using this app. 

## Instructions:
1. Use the dropdown menus to filter TV shows by streaming provider, genre, and language.
2. The main panel will update to display the TV shows that match your filters.

Enjoy exploring!
""", unsafe_allow_html=True)

# Sort the list of streaming providers, genres, and languages
STREAMING_PROVIDERS.sort()
genres.sort()
languages.sort()

# Add "Any" to the list of streaming providers
STREAMING_PROVIDERS = ["Any"] + STREAMING_PROVIDERS

provider = st.selectbox("Choose a streaming provider", STREAMING_PROVIDERS)

# Add filters for genre, language, duration, and rating
selected_genre = st.selectbox("Choose a genre", ["Any"] + genres)
selected_language = st.selectbox("Choose a language", ["Any"] + languages)
selected_duration = st.slider("Choose a maximum duration (in minutes)", 0, 200, 100)
selected_rating = st.slider("Choose a minimum rating", 0.0, 10.0, 5.0)

filtered_shows = [show for show in data if (provider == "Any" or (show['network'] and show['network']['name'] == provider))
                  and (selected_genre == "Any" or selected_genre in show['genres'])
                  and (selected_language == "Any" or selected_language == show['language'])
                  and (not show['runtime'] or show['runtime'] <= selected_duration)
                  and (not show.get('rating', {}).get('average') or show.get('rating', {}).get('average') >= selected_rating)]

# Display the recommended shows
if filtered_shows:
    # Add "All" to the list of shows and select it by default
    selected_show = st.selectbox("Select a show", ["All"] + [show['name'] for show in filtered_shows])

    if selected_show != "All":
        # If a specific show is selected, display its details
        show_details = next(show for show in filtered_shows if show['name'] == selected_show)

        st.write("Name:", show_details['name'])
        st.write("Language:", show_details['language'])
        st.write("Genres:", ", ".join(show_details['genres']))
        st.write("Runtime:", show_details['runtime'])
        st.write("Rating:", show_details.get('rating', {}).get('average'))
        st.write("Summary:", BeautifulSoup(show_details['summary'], "html.parser").get_text())
    else:
    # If "All" is selected, display the details of all shows
        for show in filtered_shows:
            st.write("Name:", show['name'])
            st.write("Language:", show['language'])
            st.write("Genres:", ", ".join(show['genres']))
            st.write("Runtime:", show['runtime'])
            st.write("Rating:", show.get('rating', {}).get('average'))
            st.write("Summary:", BeautifulSoup(show['summary'], "html.parser").get_text())
            st.write("Streaming Provider:", show['network']['name'] if show['network'] else "N/A")
            st.write("---")  # Add a separator between shows
else:
    st.write("No shows found with the selected filters.")