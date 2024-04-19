
import requests
import json
import datetime
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

# Function to load configuration parameters from a JSON file
def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

# Function to check and update the usage count
def check_and_update_usage(api_key):
    # Load the usage data
    try:
        with open('usage.json', 'r') as f:
            usage_data = json.load(f)
    except FileNotFoundError:
        usage_data = {}

    # Get the current date
    current_date = str(datetime.date.today())

    # Check if the current date exists in the data
    if current_date not in usage_data:
        usage_data[current_date] = {}

    if api_key not in usage_data[current_date]:
        # If the API key is not in the data for the current date, add it and set the count to 1
        usage_data[current_date][api_key] = 1
    elif usage_data[current_date][api_key] < 50:
        # If the API key is in the data and the count is less than 50, increment the count
        usage_data[current_date][api_key] += 1
    else:
        # If the count is 50 or more, deny the API request
        raise Exception("API key usage limit reached for today")

    # Save the updated usage data
    with open('usage.json', 'w') as f:
        json.dump(usage_data, f)

# Load configuration parameters
config = load_config('config.json')

# Check and update the usage count for TMDb
check_and_update_usage(config['tmdb_api_key'])

# Check and update the usage count for TheTVDB
check_and_update_usage(config['thetvdb_api_key'])

# Fetch data from TVmaze API
url_tvmaze = "http://api.tvmaze.com/shows"
response_tvmaze = requests.get(url_tvmaze)
data_tvmaze = response_tvmaze.json()

# Fetch data from TMDb API
url_tmdb = f"https://api.themoviedb.org/3/tv/popular?api_key={config['tmdb_api_key']}"
response_tmdb = requests.get(url_tmdb)
data_tmdb = response_tmdb.json()

# Fetch data from TheTVDB API
url_thetvdb = "https://api.thetvdb.com/series"
headers = {"Authorization": f"Bearer {config['thetvdb_api_key']}"}
response_thetvdb = requests.get(url_thetvdb, headers=headers)
data_thetvdb = response_thetvdb.json()

# Print the data_thetvdb dictionary to the console
#print(data_thetvdb)

# Calculate the total count of TV series from TVmaze, TMDb, and TheTVDB APIs
#total_count = len(data_tvmaze) + len(data_tmdb['results']) + len(data_thetvdb['data']) if 'data' in data_thetvdb else 0

# Display the total count on the web app
#st.markdown(f"## Total TV Series Found: {total_count}")

# Fetch data from IMDb API -- not yet ready
##url_imdb = "https://imdb-api.com/en/API/MostPopularTVs/your_imdb_api_key"
##response_imdb = requests.get(url_imdb)
##data_imdb = response_imdb.json()

# Extract unique channels from the TVmaze data
channels = set(show['network']['name'] for show in data_tvmaze if show['network'])

# Your original list of streaming providers
STREAMING_PROVIDERS = ["Netflix", "Hulu", "Apple TV+", "Prime Video", "Disney+", "HBO", "FuboTV", "Tubi"]

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
languages = list(set(show['language'] for show in data_tvmaze if show['language']) | set(tvshow['original_language'] for tvshow in data_tmdb['results']))

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

# Add filters for genre, language, provider, duration, rating, and year of release
selected_genre = st.selectbox("Choose a genre", ["Any"] + genres)
selected_language = st.selectbox("Choose a language", ["Any"] + languages)
provider = st.selectbox("Choose a streaming provider", ["ALL"] + STREAMING_PROVIDERS)
selected_duration = st.slider("Choose a maximum duration (in minutes)", 0, 200, 100)
selected_rating = st.slider("Choose a minimum rating", 0.0, 10.0, 5.0)
year = st.selectbox('Select Year of Release', ["Any"] + list(range(1950, 2023)))

# Filter shows from TVmaze
filtered_shows_tvmaze = [show for show in data_tvmaze if show['network'] and (provider == "ALL" or show['network']['name'] == provider)
                         and (selected_genre == "Any" or selected_genre in show['genres'])
                         and (selected_language == "Any" or language_codes.get(show['language'], show['language'].upper()) == selected_language)
                         and (not show['runtime'] or show['runtime'] <= selected_duration)
                         and (not show.get('rating', {}).get('average') or show.get('rating', {}).get('average') >= selected_rating)
                         and (year == "Any" or (show.get('premiered') and year == int(show['premiered'].split('-')[0])))]

# Filter TV shows from TMDb
filtered_tvshows_tmdb = [tvshow for tvshow in data_tmdb['results'] if (selected_genre == "Any" or selected_genre in tvshow['genre_ids'])
                        and (selected_language == "Any" or selected_language == tvshow['original_language'].upper())
                        and (not tvshow.get('episode_run_time') or min(tvshow.get('episode_run_time', [0])) <= selected_duration)
                        and (not tvshow['vote_average'] or tvshow['vote_average'] >= selected_rating)
                        and (year == "Any" or (tvshow.get('first_air_date') and year == int(tvshow['first_air_date'].split('-')[0])))]


# Display the recommended shows from TVmaze
for show in filtered_shows_tvmaze:
    st.write(f"**Title:** {show['name']}")
    st.write(f"**Year:** {show['premiered'].split('-')[0] if show.get('premiered') else 'N/A'}")
    st.write(f"**Genre:** {', '.join(show['genres'])}")
    st.write(f"**Language:** {show['language']}")
    st.write(f"**Duration:** {show['runtime']} minutes")
    st.write(f"**Platform:** {show['network']['name']}")
    summary = BeautifulSoup(show['summary'], "html.parser").get_text()
    st.write(f"**Summary:** {summary}")
    st.write(f"**Rating:** {show.get('rating', {}).get('average', 'N/A')}")
    st.write("---")

# Display the recommended TV shows from TMDb
for tvshow in filtered_tvshows_tmdb:
    st.write(f"**Title:** {tvshow['name']}")
    st.write(f"**Year:** {tvshow['first_air_date'].split('-')[0] if tvshow.get('first_air_date') else 'N/A'}")
    st.write(f"**Genre:** {', '.join(str(genre_id) for genre_id in tvshow['genre_ids'])}")
    st.write(f"**Language:** {tvshow['original_language']}")
    st.write(f"**Duration:** {min(tvshow.get('episode_run_time', ['N/A']))} minutes")
    st.write(f"**Summary:** {tvshow['overview']}")
    st.write(f"**Rating:** {tvshow['vote_average']}")
    st.write("---")