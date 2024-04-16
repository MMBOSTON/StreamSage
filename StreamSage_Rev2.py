import requests
import streamlit as st

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
st.title("StreamSage")

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
for show in filtered_shows:
    st.write(f"**Title:** {show['name']}")
    st.write(f"**Genre:** {', '.join(show['genres'])}")
    st.write(f"**Language:** {show['language']}")
    st.write(f"**Duration:** {show['runtime']} minutes")
    st.write(f"**Platform:** {show['network']['name']}")
    st.write(f"**Rating:** {show.get('rating', {}).get('average', 'N/A')}")
    st.write("---")