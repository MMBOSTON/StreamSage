"""
StreamSage: Your All-in-One Streaming Companion!

This program is a Streamlit web application that allows users to explore a wide range of TV shows 
from various streaming providers and channels. It fetches data from the TVmaze API, which provides 
information about TV shows, including their genres, languages, runtimes, ratings, and summaries.

The main features of the program are:

1. Filtering: Users can filter TV shows by streaming provider, genre, and language using dropdown menus. 
The available options for each filter are dynamically extracted from the fetched data, ensuring that they 
always reflect the current state of the TVmaze database.

2. Displaying Recommendations: After the user selects their filters, the main panel of the web application 
updates to display the TV shows that match the selected filters. For each recommended show, the program 
displays the title, genre, language, duration, platform, summary, and rating.

3. User-Friendly Interface: The program uses Streamlit to provide a user-friendly web interface. Streamlit's 
interactive widgets are used for the filters, and its markdown support is used to format the displayed information 
in a readable way.

4. HTML Tag Removal: The program uses BeautifulSoup to remove HTML tags from the summaries of the TV shows 
before displaying them. This ensures that the summaries are displayed in plain text, making them easier to read.

This program is useful for anyone who wants to discover new TV shows to watch. By providing a wide range 
of filters and displaying detailed information about each recommended show, it helps users find shows that 
match their preferences and interests.

To run the program, you need Python 3 and the following Python libraries: requests, json, streamlit, 
and BeautifulSoup. You can install these libraries using pip:

    pip install requests json streamlit beautifulsoup4

After installing the required libraries, you can run the program using the following command:

    streamlit run StreamSage_Rev3.py

Enjoy exploring!
"""

import requests
import json
import streamlit as st
from bs4 import BeautifulSoup

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

# Fetch data from TVmaze API
url_tvmaze = "http://api.tvmaze.com/shows"
response_tvmaze = requests.get(url_tvmaze)
data_tvmaze = response_tvmaze.json()

# Fetch data from TMDb API
url_tmdb = "https://api.themoviedb.org/3/movie/popular?api_key=30694fa5f1cc552504ecce5c16034f5d"
response_tmdb = requests.get(url_tmdb)
data_tmdb = response_tmdb.json()

# Extract unique channels from the TVmaze data
channels = set(show['network']['name'] for show in data_tvmaze if show['network'])

# Your original list of streaming providers
STREAMING_PROVIDERS = ["Netflix", "Hulu", "Prime Video", "Disney+", "HBO"]

# Add the channels from TVmaze to your list
STREAMING_PROVIDERS.extend(channels)

# Remove duplicates (if any)
STREAMING_PROVIDERS = list(set(STREAMING_PROVIDERS))

# Extract unique genres from TVmaze data
genres = list(set(genre for show in data_tvmaze for genre in show['genres']))

# Dictionary that maps full language names to their ISO 639-1 codes
language_codes = {
    'English': 'EN',
    'Japanese': 'JP',
    # Add more mappings as needed
}

# Extract unique languages from TVmaze data and TMDb data
languages = list(set(show['language'] for show in data_tvmaze if show['language']) | set(movie['original_language'] for movie in data_tmdb['results']))

# Standardize language names using the language_codes dictionary
languages = [language_codes.get(lang, lang.upper()) for lang in languages]

# Remove duplicates (if any)
languages = list(set(languages))

# Streamlit app
st.title("StreamSage")

# Sort the list of streaming providers, genres, and languages
STREAMING_PROVIDERS.sort()
genres.sort()
languages.sort()

# Add filters for genre, language, provider, duration, and rating
selected_genre = st.selectbox("Choose a genre", ["Any"] + genres)
selected_language = st.selectbox("Choose a language", ["Any"] + languages)
provider = st.selectbox("Choose a streaming provider", ["ALL"] + STREAMING_PROVIDERS)
selected_duration = st.slider("Choose a maximum duration (in minutes)", 0, 200, 100)
selected_rating = st.slider("Choose a minimum rating", 0.0, 10.0, 5.0)

# Filter shows from TVmaze
filtered_shows_tvmaze = [show for show in data_tvmaze if show['network'] and (provider == "ALL" or show['network']['name'] == provider)
                         and (selected_genre == "Any" or selected_genre in show['genres'])
                         and (selected_language == "Any" or language_codes.get(show['language'], show['language'].upper()) == selected_language)
                         and (not show['runtime'] or show['runtime'] <= selected_duration)
                         and (not show.get('rating', {}).get('average') or show.get('rating', {}).get('average') >= selected_rating)]

# Filter movies from TMDb
filtered_movies_tmdb = [movie for movie in data_tmdb['results'] if (selected_genre == "Any" or selected_genre in movie['genre_ids'])
                        and (selected_language == "Any" or selected_language == movie['original_language'].upper())
                        and (not movie.get('runtime') or movie.get('runtime') <= selected_duration)
                        and (not movie['vote_average'] or movie['vote_average'] >= selected_rating)]

# Display the recommended shows from TVmaze
for show in filtered_shows_tvmaze:
    st.write(f"**Title:** {show['name']}")
    st.write(f"**Genre:** {', '.join(show['genres'])}")
    st.write(f"**Language:** {show['language']}")
    st.write(f"**Duration:** {show['runtime']} minutes")
    st.write(f"**Platform:** {show['network']['name']}")
    summary = BeautifulSoup(show['summary'], "html.parser").get_text()
    st.write(f"**Summary:** {summary}")
    st.write(f"**Rating:** {show.get('rating', {}).get('average', 'N/A')}")
    st.write("---")

# Display the recommended movies from TMDb
for movie in filtered_movies_tmdb:
    st.write(f"**Title:** {movie['title']}")
    st.write(f"**Genre:** {', '.join(str(genre_id) for genre_id in movie['genre_ids'])}")
    st.write(f"**Language:** {movie['original_language']}")
    st.write(f"**Duration:** {movie.get('runtime', 'N/A')} minutes")
    st.write(f"**Summary:** {movie['overview']}")
    st.write(f"**Rating:** {movie['vote_average']}")
    st.write("---")