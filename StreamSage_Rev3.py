import requests
import streamlit as st

# Fetch data from TVmaze API
url_tvmaze = "http://api.tvmaze.com/shows"
response_tvmaze = requests.get(url_tvmaze)
data_tvmaze = response_tvmaze.json()

# Fetch data from TMDb API
url_tmdb = "https://api.themoviedb.org/3/movie/popular?api_key=YOUR_TMDB_API_KEY"
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

# Extract unique genres from both TVmaze and TMDb data
genres = list(set(genre for show in data_tvmaze for genre in show['genres']) | 
              set(movie['genre_ids'] for movie in data_tmdb.get('results', [])))

languages = list(set(show['language'] for show in data_tvmaze if show['language']) | set(movie['original_language'] for movie in data_tmdb['results']))

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

# Filter shows from TVmaze
filtered_shows_tvmaze = [show for show in data_tvmaze if show['network'] and show['network']['name'] == provider
                         and (selected_genre == "Any" or selected_genre in show['genres'])
                         and (selected_language == "Any" or selected_language == show['language'])
                         and (not show['runtime'] or show['runtime'] <= selected_duration)
                         and (not show.get('rating', {}).get('average') or show.get('rating', {}).get('average') >= selected_rating)]

# Filter movies from TMDb (assuming 'genre_ids' is a list of genre IDs and 'vote_average' is the rating)
filtered_movies_tmdb = [movie for movie in data_tmdb['results'] if (selected_genre == "Any" or selected_genre in movie['genre_ids'])
                        and (selected_language == "Any" or selected_language == movie['original_language'])
                        and (not movie['runtime'] or movie['runtime'] <= selected_duration)
                        and (not movie['vote_average'] or movie['vote_average'] >= selected_rating)]

# Display the recommended shows from TVmaze
for show in filtered_shows_tvmaze:
    st.write(f"**Title:** {show['name']}")
    st.write(f"**Genre:** {', '.join(show['genres'])}")
    st.write(f"**Language:** {show['language']}")
    st.write(f"**Duration:** {show['runtime']} minutes")
    st.write(f"**Platform:** {show['network']['name']}")
    st.write(f"**Rating:** {show.get('rating', {}).get('average', 'N/A')}")
    st.write("---")

# Display the recommended movies from TMDb (assuming 'title' is the movie title and 'runtime' is the duration in minutes)
for movie in filtered_movies_tmdb:
    st.write(f"**Title:** {movie['title']}")
    st.write(f"**Genre IDs:** {', '.join(str(id) for id in movie['genre_ids'])}")  # You might want to convert these IDs to genre names
    st.write(f"**Language:** {movie['original_language']}")
    st.write(f"**Duration:** {movie['runtime']} minutes")
    st.write(f"**Rating:** {movie['vote_average']}")
    st.write("---")