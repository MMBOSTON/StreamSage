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
##st.title("StreamSage: Your All-in-One Streaming Companion")

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

provider = st.selectbox("Choose a streaming provider", STREAMING_PROVIDERS)

# Add filters for genre, language, duration, and rating
selected_genre = st.selectbox("Choose a genre", ["Any"] + genres)
selected_language = st.selectbox("Choose a language", ["Any"] + languages)
selected_duration = st.slider("Choose a maximum duration (in minutes)", 0, 200, 100)
selected_rating = st.slider("Choose a minimum rating", 0.0, 10.0, 5.0)

filtered_shows = [show for show in data if show['network'] and show['network']['name'] == provider
                  and (selected_genre == "Any" or selected_genre in show['genres'])
                  and (selected_language == "Any" or selected_language == show['language'])
                  and (not show['runtime'] or show['runtime'] <= selected_duration)
                  and (not show.get('rating', {}).get('average') or show.get('rating', {}).get('average') >= selected_rating)]

# Display the recommended shows
if filtered_shows:
    selected_show = st.selectbox("Select a show", [show['name'] for show in filtered_shows])
    show_details = next(show for show in filtered_shows if show['name'] == selected_show)

    # Display the details of the selected show
    st.write("Name:", show_details['name'])
    st.write("Language:", show_details['language'])
    st.write("Genres:", ", ".join(show_details['genres']))
    st.write("Runtime:", show_details['runtime'])
    st.write("Rating:", show_details.get('rating', {}).get('average'))
    st.write("Summary:", BeautifulSoup(show_details['summary'], "html.parser").get_text())
else:
    st.write("No shows found with the selected filters.")