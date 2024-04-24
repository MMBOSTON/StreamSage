import requests
import os
import json
import datetime
import streamlit as st
from bs4 import BeautifulSoup

st.markdown("""
<center>

# Welcome to StreamSage: Your All-in-One Streaming Companion!

</center>

<center>

Explore a wide range of TV shows from various streaming providers and channels using this app.

</center>

## Instructions:
1. Use the dropdown menus to filter TV shows by streaming provider, genre, and language.
2. The main panel will update to display the TV shows that match your filters.

Enjoy exploring!
""", unsafe_allow_html=True)

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def check_and_update_usage(api_key):
    usage_file = 'usage.json'
    if os.path.exists(usage_file):
        with open(usage_file, 'r') as f:
            try:
                usage_data = json.load(f)
            except json.JSONDecodeError:
                usage_data = {}  # Set to an empty dict if file is empty
    else:
        usage_data = {}  # Set to an empty dict if file does not exist
    current_date = str(datetime.date.today())

    if current_date not in usage_data:
        usage_data[current_date] = {}

    if api_key not in usage_data[current_date]:
        usage_data[current_date][api_key] = 1
    elif usage_data[current_date][api_key] < 200:
        usage_data[current_date][api_key] += 1
    else:
        raise Exception("API key usage limit reached for today")

    with open('usage.json', 'w') as f:
        json.dump(usage_data, f)

config = load_config('config.json')

check_and_update_usage(config['tmdb_api_key'])
check_and_update_usage(config['tvdb_api_key'])

# Fetch series data from TVMaze
url_tvmaze = "http://api.tvmaze.com/shows"
response_tvmaze = requests.get(url_tvmaze)
data_tvmaze = response_tvmaze.json()

# Fetch series data from TMDB
url_tmdb = f"https://api.themoviedb.org/3/tv/popular?api_key={config['tmdb_api_key']}"
response_tmdb = requests.get(url_tmdb)
data_tmdb = response_tmdb.json()

# Fetch genre data from TMDB
url_tmdb_genres = f"https://api.themoviedb.org/3/genre/tv/list?api_key={config['tmdb_api_key']}"
response_tmdb_genres = requests.get(url_tmdb_genres)
data_tmdb_genres = response_tmdb_genres.json()

genres = [genre['name'] for genre in data_tmdb_genres['genres']]
genre_dict = {genre['id']: genre['name'] for genre in data_tmdb_genres['genres']}

# Fetch trending series from TMDB
url_tmdb_trending = f"https://api.themoviedb.org/3/trending/tv/day?api_key={config['tmdb_api_key']}"
response_tmdb_trending = requests.get(url_tmdb_trending)
data_tmdb_trending = response_tmdb_trending.json()

# Extract series names and construct URLs for TMDB
trending_series_tmdb = [(show['name'], f"https://www.themoviedb.org/tv/{show['id']}") for show in data_tmdb_trending['results']]

# Extract series names and construct URLs for TVMaze
trending_series_tvmaze = [(show['name'], show['url']) for show in data_tvmaze]

# Combine trending series from both TMDB and TVMaze
trending_series = trending_series_tmdb + trending_series_tvmaze

class _SessionState:
    def __init__(self):
        self._state = {}

    def __getitem__(self, key):
        return self._state[key]

    def __setitem__(self, key, val):
        self._state[key] = val

def get_session_state():
    if not hasattr(st, '_session_state'):
        st._session_state = _SessionState()
    return st._session_state

# Fetch series data from TVMaze
# ... (previous code) ...

# Get the session state
state = get_session_state()
if not hasattr(state, 'page_number'):
    state.page_number = 0

# Display in sidebar
sidebar = st.sidebar
sidebar.header('Trending Series')

# Display 20 trending series per page
start = state.page_number * 20
end = start + 20
for show, url in trending_series[start:end]:
    sidebar.markdown(f"[{show}]({url})")

# Add "Previous" and "Next" buttons at the bottom of the sidebar
if sidebar.button('Load More') and end < len(trending_series):
    state.page_number += 1
    start = state.page_number * 20
    end = start + 20
    sidebar.empty()
    for show, url in trending_series[start:end]:
        sidebar.markdown(f"[{show}]({url})")
if sidebar.button('Prev') and state.page_number > 0:
    state.page_number -= 1
    start = state.page_number * 20
    end = start + 20
    sidebar.empty()
    for show, url in trending_series[start:end]:
        sidebar.markdown(f"[{show}]({url})")

channels = set(show['network']['name'] for show in data_tvmaze if show['network'])

STREAMING_PROVIDERS = ["Netflix", "Hulu", "Apple TV+", "Prime Video", "Disney+", "HBO", "FuboTV", "Tubi"]
STREAMING_PROVIDERS.extend(channels)
STREAMING_PROVIDERS = list(set(STREAMING_PROVIDERS))

genres = list(set(genre for show in data_tvmaze for genre in show['genres']))

# Define the list of countries
countries = ['USA', 'UK', 'Canada', 'Australia', 'Germany', 'France', 'Italy', 'Spain', 'Japan', 'China', 'India', 'Other']

# Define the list of statuses
statuses = ['Running', 'Ended', 'In Development', 'To Be Determined', 'Pilot', 'Canceled', 'Other']

# Define the list of qualities
qualities = ['HD', 'SD', '4K', 'Other']

# Define the list of subtitles
subtitles = ['English', 'Spanish', 'French', 'German', 'Italian', 'Japanese', 'Chinese', 'Hindi', 'Other']

# Define the list of audios
audios = ['English', 'Spanish', 'French', 'German', 'Italian', 'Japanese', 'Chinese', 'Hindi', 'Other']

# Load language codes from JSON file
with open('language_codes.json', 'r') as f:
    language_codes = json.load(f)

languages = list(set(show['language'] for show in data_tvmaze if show['language']) | set(tvshow['original_language'] for tvshow in data_tmdb['results']))
languages = [language_codes.get(lang, lang.upper()) for lang in languages]
languages = list(set(languages))

st.title("StreamSage")

STREAMING_PROVIDERS.sort()
genres.sort()
languages.sort()

# Create an expander for the filters with larger, bold text
# Inject custom CSS
st.markdown("""
    <style>
        .reportview-container .main .block-container .element-container .stExpander > div:first-child {
            font-size: 20px;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

# Create an expander for the filters
# Create an expander for the filters
filters_expander = st.expander('Filters')

# Place all the filters inside the expander
with filters_expander:
    # Create four columns
    col1, col2, col3 = st.columns([3,3,3])

    # Place your content in the first column
    with col1:
        search_query = st.text_input("Search for TV series by title, genre, actors, directors, etc.")
        selected_genre = st.selectbox("Choose a genre", ["Any"] + genres)
        selected_language = st.selectbox("Choose a language", ["Any"] + languages)
        provider = st.selectbox("Choose a streaming provider", ["ALL"] + STREAMING_PROVIDERS)
        year = st.selectbox('Select Year of Release', ["Any"] + list(range(1950, 2023)))

    with col2:
        selected_country = st.selectbox("Choose a country", ["Any"] + countries)
        selected_status = st.selectbox("Choose a status", ["Any"] + statuses)
        selected_quality = st.selectbox("Choose a quality", ["Any"] + qualities)
        selected_subtitles = st.selectbox("Choose subtitles", ["Any"] + subtitles)
        selected_audio = st.selectbox("Choose audio", ["Any"] + audios)

    with col3:
        selected_duration = st.slider("Choose a maximum duration (in minutes)", 0, 200, 100)
        selected_rating = st.slider("Choose a minimum rating", 0.0, 10.0, 5.0)
        selected_seasons = st.slider("Choose a maximum number of seasons", 0, 20, 10)
        selected_episodes = st.slider("Choose a maximum number of episodes", 0, 200, 100)
        selected_views = st.slider("Choose a minimum number of views", 0, 1000000, 500000)


filtered_shows_tvmaze = [show for show in data_tvmaze if show['network'] and (provider == "ALL" or show['network']['name'] == provider)
                         and (selected_genre == "Any" or any(selected_genre == genre_dict.get(id, "Unknown genre") for id in show.get('genre_ids', [])))
                         and (selected_language == "Any" or language_codes.get(show['language'], show['language'].upper()) == selected_language)
                         and (not show['runtime'] or show['runtime'] <= selected_duration)
                         and (not show.get('rating', {}).get('average') or show.get('rating', {}).get('average') >= selected_rating)
                         and (year == "Any" or (show.get('premiered') and year == int(show['premiered'].split('-')[0])))
                         and (search_query.lower() in show['name'].lower())]

filtered_tvshows_tmdb = [tvshow for tvshow in data_tmdb['results'] if (selected_genre == "Any" or any(selected_genre == genre_dict.get(id, "Unknown genre") for id in tvshow.get('genre_ids', [])))
                        and (selected_language == "Any" or selected_language == tvshow['original_language'].upper())
                        and (not tvshow.get('episode_run_time') or min(tvshow.get('episode_run_time', [0])) <= selected_duration)
                        and (not tvshow['vote_average'] or tvshow['vote_average'] >= selected_rating)
                        and (year == "Any" or (tvshow.get('first_air_date') and year == int(tvshow['first_air_date'].split('-')[0])))
                        and (search_query.lower() in tvshow['name'].lower())]

# Initialize page if it's not already in the session state
if 'page' not in st.session_state:
    st.session_state.page = 0

# Display the shows for the current page from filtered_shows_tvmaze
for show in filtered_shows_tvmaze[st.session_state.page*5:(st.session_state.page+1)*5]:
    st.markdown(f"**Title:** [{show['name']}]({show['url']})")
    st.write(f"**Year:** {show['premiered'].split('-')[0] if show.get('premiered') else 'N/A'}")
    genres = ', '.join([genre_dict.get(id, "Unknown genre") for id in show.get('genre_ids', [])])
    st.write(f"**Genre:** {genres if genres else 'N/A'}")
    st.write(f"**Language:** {show['language']}")
    st.write(f"**Duration:** {show['runtime']} minutes")
    st.write(f"**Platform:** {show.get('network', {}).get('name', 'N/A')}")
    summary = BeautifulSoup(show['summary'], "html.parser").get_text()
    st.write(f"**Summary:** {summary}")
    st.write(f"**Rating:** {show.get('rating', {}).get('average', 'N/A')}")
    st.write("---")

# Display the shows for the current page from filtered_tvshows_tmdb
for tvshow in filtered_tvshows_tmdb[st.session_state.page*5:(st.session_state.page+1)*5]:
    st.markdown(f"**Title:** [{tvshow['name']}](https://www.themoviedb.org/tv/{tvshow['id']})")
    st.write(f"**Year:** {tvshow['first_air_date'].split('-')[0] if tvshow.get('first_air_date') else 'N/A'}")
    genres = ', '.join([genre_dict.get(id, "Unknown genre") for id in tvshow.get('genre_ids', [])])
    st.write(f"**Genre:** {genres if genres else 'N/A'}")
    st.write(f"**Language:** {tvshow['original_language']}")
    st.write(f"**Duration:** {min(tvshow.get('episode_run_time', [0]))} minutes")
    st.write(f"**Platform:** {tvshow.get('network', {}).get('name', 'N/A')}")
    st.write(f"**Summary:** {tvshow['overview']}")
    st.write(f"**Rating:** {tvshow['vote_average']}")
    st.write("---")

# Create two columns
col1, col2 = st.columns(2)

# Place the "Previous" button in the left column
with col1:
    if st.button('Previous'):
        st.session_state.page -= 1

# Place the "Next" button in the right column
with col2:
    if st.button('Next'):
        st.session_state.page += 1