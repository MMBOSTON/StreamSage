import streamlit as st

# List of all streaming service providers
STREAMING_PROVIDERS = ["Netflix", "Amazon Prime Video", "Hulu", "Disney+", 
                       "HBO Max", "Apple TV+", "Peacock", "Paramount+", 
                       "YouTube Premium", "Sling TV", "Twitch", "ESPN+", 
                       "Discovery+", "Peacock Free", "Tubi", "Crackle", 
                       "Pluto TV", "IMDb TV", "Vudu's Movies on Us", 
                       "Roku Channel", "YouTube"]

# List of all genres
GENRES = ["Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", 
          "Documentary", "Drama", "Family", "Fantasy", "Film-Noir", "Game-Show", 
          "History", "Horror", "Music", "Musical", "Mystery", "News", "Reality-TV", 
          "Romance", "Sci-Fi", "Sport", "Talk-Show", "Thriller", "War", "Western"]

# List of all languages
LANGUAGES = ["English", "German", "Spanish", "French", "Italian"]

def fetch_data():
    return [
        {
            "title": "Breaking Bad",
            "genre": "Crime, Drama, Thriller",
            "language": "English",
            "duration": "49 min",
            "platform": "Netflix",
            "rating": "9.5"
        },
        {
            "title": "Game of Thrones",
            "genre": "Action, Adventure, Drama",
            "language": "English",
            "duration": "57 min",
            "platform": "HBO Max",
            "rating": "9.3"
        },
        {
            "title": "Stranger Things",
            "genre": "Drama, Fantasy, Horror",
            "language": "English",
            "duration": "51 min",
            "platform": "Netflix",
            "rating": "8.7"
        },
        {
            "title": "The Mandalorian",
            "genre": "Action, Adventure, Fantasy",
            "language": "English",
            "duration": "40 min",
            "platform": "Disney+",
            "rating": "8.8"
        },
        {
            "title": "The Witcher",
            "genre": "Action, Adventure, Drama",
            "language": "English",
            "duration": "60 min",
            "platform": "Netflix",
            "rating": "8.2"
        },
        {
            "title": "Westworld",
            "genre": "Drama, Mystery, Sci-Fi",
            "language": "English",
            "duration": "62 min",
            "platform": "HBO Max",
            "rating": "8.6"
        },
        {
            "title": "The Boys",
            "genre": "Action, Comedy, Crime",
            "language": "English",
            "duration": "60 min",
            "platform": "Amazon Prime Video",
            "rating": "8.7"
        },
        {
            "title": "The Crown",
            "genre": "Biography, Drama, History",
            "language": "English",
            "duration": "58 min",
            "platform": "Netflix",
            "rating": "8.7"
        },
        {
            "title": "The Handmaid's Tale",
            "genre": "Drama, Sci-Fi, Thriller",
            "language": "English",
            "duration": "60 min",
            "platform": "Hulu",
            "rating": "8.4"
        },
        {
            "title": "The Expanse",
            "genre": "Drama, Mystery, Sci-Fi",
            "language": "English",
            "duration": "60 min",
            "platform": "Amazon Prime Video",
            "rating": "8.5"
        }
    ]

TV_SHOWS = fetch_data()

# Add new selectboxes for streaming service provider, genre, and language
platform = st.selectbox("Streaming Service Provider", options=[""] + STREAMING_PROVIDERS)
genre = st.selectbox("Genre", options=[""] + GENRES)
language = st.selectbox("Language", options=[""] + LANGUAGES)
rating = st.selectbox("User Ratings", options=["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

# Filter the TV shows based on the user's preferences
filtered_shows = [
    show for show in TV_SHOWS 
    if (not genre or genre in show["genre"].split(", ")) 
    and (not platform or show["platform"] == platform) 
    and (not language or show["language"] == language)
    and (not rating or float(show['rating']) >= float(rating))
]

st.write("## Recommended Shows")

# Display the recommended shows
for show in filtered_shows:
    st.write(f"**Title:** {show['title']}")
    st.write(f"**Genre:** {show['genre']}")
    st.write(f"**Language:** {show['language']}")
    st.write(f"**Duration:** {show['duration']}")
    st.write(f"**Platform:** {show['platform']}")
    st.write(f"**Rating:** {show['rating']}")
    st.write("---")