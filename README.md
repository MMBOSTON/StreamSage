# StreamSage: Your All-in-One TV Show Recommender

This project recommends TV shows based on user preferences.

See this project in action on Streamlit! Click here: https://streamsage.streamlit.app/

Project and Work Product Description:
StreamSage is a TV show recommendation application. It fetches real TV show data from the TVmaze and TMDb APIs and filters the shows based on the user's selected genre, language, duration, and rating. The problem is that there are so many TV shows available on various streaming platforms, making it difficult for users to choose what to watch. Our goal is to make TV show selection easier and more personalized.

The Project As-Is:	The Project To-Be:
Diagram 1	Diagram 2
File Format: Input user preferences. Output a list of recommended TV shows.	File Format: Input user preferences and viewing history. Output a list of recommended TV shows and personalized viewing suggestions.
Python Packages: Streamlit, BeautifulSoup, requests	Python Packages: Streamlit, BeautifulSoup, requests, pandas, scikit-learn
Description of Solution:
We use Python and the Streamlit library to create an interactive web application that recommends TV shows. Our vision is that all users can easily find TV shows that match their preferences, saving them time and enhancing their viewing experience.

Workflow Diagram

Workflow diagram of future ("TO-BE") state (improved processes from your solution).
Minimum Viable Product (MVP) 1.0 delivered: In the completed version 1.0 of this project:

Code has been developed to fetch TV show data from the TVmaze and TMDb APIs.
The app filters the TV shows based on the user's selected genre, language, duration, and rating.
The app displays the details of each recommended TV show, including the title, genre, language, duration, platform, summary, and rating.
Later MVP, i.e., v2, v3, vN+ functionality to be delivered For future enhancements, in the next versions of this project: Version 2.0: Incorporate user viewing history to provide personalized recommendations. Version 3.0: Add user reviews and ratings to the TV show data. Version 4.0: Use machine learning algorithms to improve the recommendation system.

Solution Design (high-level):
This project uses Streamlit, BeautifulSoup, and requests libraries to fetch, process, and display TV show data.

Solution Code Description (low-level design):
First, import the necessary Python libraries. Streamlit is used to create the web app, BeautifulSoup is used to parse HTML, and requests is used to send HTTP requests.
Fetch TV show data: The app sends HTTP requests to the TVmaze and TMDb APIs to fetch TV show data.
Filter TV shows: The app uses list comprehensions to filter the TV shows based on the user's selected genre, language, duration, and rating.
Display TV show details: The app displays the details of each recommended TV show, including the title, genre, language, duration, platform, summary, and rating. The summary is parsed using BeautifulSoup to remove any HTML tags.
Actual Working Product Code:
The code is available to the public here on this GitHub Repository.
The required packages are:
Streamlit
BeautifulSoup
requests
See this project in action on Streamlit! Click here: https://streamsage.streamlit.app/

Application Instructions:
Here are the step-by-step instructions to install, set up, and use this project:

Download and install these software tools:
Anaconda Navigator
Visual Studio Code
Run these command in the Visual Studio Code terminal:
To create the conda virtual environment and install required Python packages:
conda create -n streamsage_env -c conda-forge streamlit beautifulsoup4 requests

To switch into the created environment where all the packages were installed
activate streamsage_env

To run the project
streamlit run StreamSage_Rev3.py