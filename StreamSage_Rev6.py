
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

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def check_and_update_usage(api_key):
    try:
        with open('usage.json', 'r') as f:
            usage_data = json.load(f)
    except FileNotFoundError:
        usage_data = {}

    current_date = str(datetime.date.today())

    if current_date not in usage_data:
        usage_data[current_date] = {}

    if api_key not in usage_data[current_date]:
        usage_data[current_date][api_key] = 1
    elif usage_data[current_date][api_key] < 50:
        usage_data[current_date][api_key] += 1
    else:
        raise Exception("API key usage limit reached for today")

    with open('usage.json', 'w') as f:
        json.dump(usage_data, f)

config = load_config('config.json')

check_and_update_usage(config['tmdb_api_key'])
check_and_update_usage(config['thetvdb_api_key'])

url_tvmaze = "http://api.tvmaze.com/shows"
response_tvmaze = requests.get(url_tvmaze)
data_tvmaze = response_tvmaze.json()

url_tmdb = f"https://api.themoviedb.org/3/tv/popular?api_key={config['tmdb_api_key']}"
response_tmdb = requests.get(url_tmdb)
data_tmdb = response_tmdb.json()

url_thetvdb = "https://api.thetvdb.com/series"
headers = {"Authorization": f"Bearer {config['thetvdb_api_key']}"}
response_thetvdb = requests.get(url_thetvdb, headers=headers)
data_thetvdb = response_thetvdb.json()

channels = set(show['network']['name'] for show in data_tvmaze if show['network'])

STREAMING_PROVIDERS = ["Netflix", "Hulu", "Apple TV+", "Prime Video", "Disney+", "HBO", "FuboTV", "Tubi"]
STREAMING_PROVIDERS.extend(channels)
STREAMING_PROVIDERS = list(set(STREAMING_PROVIDERS))

genres = list(set(genre for show in data_tvmaze for genre in show['genres']))

# Dictionary that maps full language names to their ISO 639-1 codes
language_codes = {
    'English': 'EN',
    'Japanese': 'JP',
    'Spanish': 'ES',
    'French': 'FR',
    'German': 'DE',
    'Italian': 'IT',
    'Dutch': 'NL',
    'Russian': 'RU',
    'Korean': 'KO',
    'Chinese': 'ZH',
    'Portuguese': 'PT',
    'Arabic': 'AR',
    'Hindi': 'HI',
    'Turkish': 'TR',
    'Polish': 'PL',
    'Swedish': 'SV',
    'Danish': 'DA',
    'Norwegian': 'NO',
    'Finnish': 'FI',
    'Greek': 'EL',
    'Czech': 'CS',
    'Hebrew': 'HE',
    'Hungarian': 'HU',
    'Thai': 'TH',
    'Indonesian': 'ID',
    'Malay': 'MS',
    'Romanian': 'RO',
    'Persian': 'FA',
    'Vietnamese': 'VI',
    'Urdu': 'UR',
    'Tamil': 'TA',
    'Telugu': 'TE',
    'Marathi': 'MR',
    'Bengali': 'BN',
    'Punjabi': 'PA',
    'Gujarati': 'GU',
    'Kannada': 'KN',
    'Malayalam': 'ML',
    'Odia': 'OR',
    'Assamese': 'AS',
    'Maithili': 'MA',
    'Sindhi': 'SD',
    'Nepali': 'NE',
    'Sinhala': 'SI',
    'Burmese': 'MY',
    'Khmer': 'KM',
    'Lao': 'LO',
    'Thai': 'TH',
    'Filipino': 'TL',
    # Add more mappings as needed
}

languages = list(set(show['language'] for show in data_tvmaze if show['language']) | set(tvshow['original_language'] for tvshow in data_tmdb['results']))
languages = [language_codes.get(lang, lang.upper()) for lang in languages]
languages = list(set(languages))

st.title("StreamSage")

STREAMING_PROVIDERS.sort()
genres.sort()
languages.sort()

selected_genre = st.selectbox("Choose a genre", ["Any"] + genres)
selected_language = st.selectbox("Choose a language", ["Any"] + languages)
provider = st.selectbox("Choose a streaming provider", ["ALL"] + STREAMING_PROVIDERS)
selected_duration = st.slider("Choose a maximum duration (in minutes)", 0, 200, 100)
selected_rating = st.slider("Choose a minimum rating", 0.0, 10.0, 5.0)
year = st.selectbox('Select Year of Release', ["Any"] + list(range(1950, 2023)))

filtered_shows_tvmaze = [show for show in data_tvmaze if show['network'] and (provider == "ALL" or show['network']['name'] == provider)
                         and (selected_genre == "Any" or selected_genre in show['genres'])
                         and (selected_language == "Any" or language_codes.get(show['language'], show['language'].upper()) == selected_language)
                         and (not show['runtime'] or show['runtime'] <= selected_duration)
                         and (not show.get('rating', {}).get('average') or show.get('rating', {}).get('average') >= selected_rating)
                         and (year == "Any" or (show.get('premiered') and year == int(show['premiered'].split('-')[0])))]

filtered_tvshows_tmdb = [tvshow for tvshow in data_tmdb['results'] if (selected_genre == "Any" or selected_genre in tvshow['genre_ids'])
                        and (selected_language == "Any" or selected_language == tvshow['original_language'].upper())
                        and (not tvshow.get('episode_run_time') or min(tvshow.get('episode_run_time', [0])) <= selected_duration)
                        and (not tvshow['vote_average'] or tvshow['vote_average'] >= selected_rating)
                        and (year == "Any" or (tvshow.get('first_air_date') and year == int(tvshow['first_air_date'].split('-')[0])))]

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

for tvshow in filtered_tvshows_tmdb:
    st.write(f"**Title:** {tvshow['name']}")
    st.write(f"**Year:** {tvshow['first_air_date'].split('-')[0] if tvshow.get('first_air_date') else 'N/A'}")
    st.write(f"**Genre:** {', '.join(str(genre_id) for genre_id in tvshow['genre_ids'])}")
    st.write(f"**Language:** {tvshow['original_language']}")
    st.write(f"**Duration:** {min(tvshow.get('episode_run_time', ['N/A']))} minutes")
    st.write(f"**Summary:** {tvshow['overview']}")
    st.write(f"**Rating:** {tvshow['vote_average']}")
    st.write("---")