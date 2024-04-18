# StreamSage: Your All-in-One TV Show Recommender

This project recommends TV shows based on user preferences.

> See this project in action on Streamlit! Click here: https://streamsage.streamlit.app/


## Project - Work Product Description:

StreamSage is a TV show recommendation application. It fetches real TV show data from the TVmaze and TMDb APIs and filters the shows based on the user's selected genre, language, duration, and rating. The problem is that there are so many TV shows available on various streaming platforms, making it difficult for users to choose what to watch. Our goal is to make TV show selection easier and more personalized.

| The Project As-Is: | The Project To-Be: |
| --------------- | --------------- |
| Diagram 1 | Diagram 2 |
| **File Format:** Input user preferences. Output a list of recommended TV shows. | **File Format:** Output a list of recommended TV shows and personalized viewing suggestions, personalized recommendations, viewing history. Webscrapping other Databases | 
| **Python Packages:** Streamlit, Pandas, Requests, BeautifulSoup,  scikit-learn |

## Description of Solution: 

We use Python and the Streamlit library to create an interactive web application that recommends TV shows. Our vision is that all users can easily find TV shows that match their preferences, saving them time and enhancing their viewing experience.

* Workflow Diagram

  * Workflow diagram of future ("TO-BE") state (improved processes from your solution).

* Minimum Viable Product (MVP) 1.0 delivered:

  * The app filters the TV shows based on the user's selected genre, language, duration, and rating.


* Later MVP, i.e., v2, v3, vN+ functionality to be delivered
For future enhancements, in the next versions of this project:
  * Version 1: Clean up Technical Debt
    * Debug Sterammlit.io App deployment issue 
  * Version 2.0: The app displays the details of each recommended TV show, including the title, genre, language, duration, platform, summary, and rating.
  * Version 3.0: Code has been developed to fetch TV show data from the TVmaze and TMDb APIs
  * Version 4.0: 
  * Version 5.0:
    * Incorporate user viewing history to provide personalized recommendations
    * Incorporate user viewing history to provide personalized recommendations.
    * Add user reviews and ratings to the TV show data.
    * Use machine learning algorithms to improve the recommendation system.
  * Version 6.0:
    * User Authentication: Implement user authentication to allow users to create accounts and save their preferences.
    * User Profile Creation: Allow users to create profiles where they can input information such as their favorite genres, preferred runtime, language, etc.
    * Recommendation Engine: Develop a recommendation engine that suggests TV series based on user preferences. You can use collaborative filtering, content-based filtering, or a hybrid approach for this.
    * Personalized Recommendations: Provide personalized recommendations based on the user's profile and viewing history.
    * Search Functionality: Implement a search feature that allows users to search for TV series by title, genre, actors, directors, etc.
    * Rating System: Allow users to rate TV series they've watched to improve future recommendations.
    * Feedback Mechanism: Incorporate a feedback mechanism where users can provide feedback on the recommendations they receive to further refine the algorithm.
    * Integration with Streaming Platforms: If possible, integrate with streaming platforms like Netflix, Hulu, etc., to provide direct links to recommended TV series.
    * Trending and Popular Shows: Display trending and popular TV series to give users more options.
    * Responsive UI: Design a user-friendly interface using Streamlit that is responsive and easy to navigate.
    * Recommendation Details: Provide details for each recommended TV series, including synopsis, ratings, cast, trailers, and streaming platform availability.
    * Save and Bookmark: Allow users to save and bookmark TV series they're interested in watching later.
    * Notifications: Optionally, incorporate a notification system to alert users about new episodes of their favorite TV series or when new recommendations are available.
    * Feedback and Support: Include a feedback form and support section where users can report issues or suggest improvements.
    * Privacy and Data Security: Ensure user data privacy and security by implementing appropriate measures to protect user information.


## Solution Design (high-level):

This project uses Streamlit, BeautifulSoup, and requests libraries to fetch, process, and display TV show data.

## Solution Code Description (low-level design): 

First, import the necessary Python libraries. Streamlit is used to create the web app, BeautifulSoup is used to parse HTML, and requests is used to send HTTP requests.
Fetch TV show data: The app sends HTTP requests to the TVmaze and TMDb APIs to fetch TV show data.
Filter TV shows: The app uses list comprehensions to filter the TV shows based on the user's selected genre, language, duration, and rating.
Display TV show details: The app displays the details of each recommended TV show, including the title, genre, language, duration, platform, summary, and rating. The summary is parsed using BeautifulSoup to remove any HTML tags.

## Actual Working Product Code: 

* The code is available to the public here on this GitHub Repository. 
* 
> See this project in action on Streamlit! Click here: https://streamsage.streamlit.app/

## Application Instructions:

Here are the step-by-step instructions to install, set up, and use this project:

1. Download and install these software tools:
  * Anaconda Navigator
  * Visual Studio Code
2. Run these command in the Visual Studio Code terminal:
  * To create the conda virtual environment and install required Python packages:
> conda create -n streamsage_env -c conda-forge streamlit beautifulsoup4 requests
  * To switch into the created environment where all the packages were installed
> activate streamsage_env
  * To run the project
> streamlit run StreamSage_Rev4.py
>

