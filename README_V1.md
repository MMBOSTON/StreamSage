# StreamSage: Your All-in-One Streaming Companion

**Updated: 2024.04.17**

StreamSage is a easy-to-use progressive web app (PWA) designed to be your one-stop area for managing your streaming life. Whether you're a die-hard movie buff or a serial series watcher, StreamSage keeps you organized and entertained.

Here's what StreamSage offers:

**Track Your Progress**: Keep tabs on everything you've watched, are currently watching, and what's next in your queue. No more forgetting where you left off!
**AI-Powered Recommendations**: Discover new shows and movies you'll love based on your watch history. Let StreamSage be your personal streaming guru.
**Spoiler-Free Zones**: Tired of accidentally getting spoiled? StreamSage helps you navigate the platform spoiler-free.
**Filter Frenzy**: Find exactly what you're looking for with advanced filtering options.

But wait, there's more!

StreamSage goes beyond just managing your watchlist. It's also a community hub:

**Share Your Thoughts**: Review what you've watched and see what others are saying. StreamSage fosters a space to connect with fellow viewers.
With StreamSage, take control of your streaming experience and maximize your entertainment enjoyment.


Project and Work Product Description:

*Rev1*: Simple working app. Manually added some streaming services (i.e. Netflix, Amazon Prime, Hulu, Tubi, etc.) and added a few "fake series data" to check/validate the app functionality.
*Details* : StreamSage_Rev1.py is the initial version of the StreamSage application. This application is a Streamlit web app that allows users to explore a wide range of TV shows from various streaming providers and channels.

Key Features: User-friendly interface: Users can filter TV shows by streaming provider, genre, and language. The main panel of the app displays the TV shows that match the selected filters.

Show details: Users can select a show to get more information about it, including the name, language, genres, runtime, rating, and summary.

Technical Details:

Streamlit: The app is built with Streamlit, a Python library for creating web apps.

Data source: The TV show data is fetched from a function fetch_data(), which currently returns a hard-coded list of TV shows. In a production environment, this function could be updated to fetch data from a database or an API.

BeautifulSoup: The app uses the BeautifulSoup library to parse the summary of the selected show. The parsed summary is then displayed in the app.

*Rev2*: Fetching data from tvmaze open source site. App is working as designed.
StreamSage_Rev2.py is the second revision of the StreamSage application. This version introduces a more user-friendly interface with clear instructions for users.

Key Updates:

Improved User Interface: The application now starts with a welcome message and instructions on how to use the app. This makes the app more user-friendly and intuitive.

Markdown Formatting: The welcome message and instructions are written in Markdown, which allows for easy formatting of the text. The unsafe_allow_html=True parameter is used to allow HTML tags in the Markdown text.

Centered Text: The welcome message is centered using the <center> HTML tag to make it more visually appealing.

Technical Details:

Streamlit Markdown: The app uses Streamlit's st.markdown() function to display the welcome message and instructions. This function allows Markdown and HTML to be used in the app.
The rest of the app remains the same as in StreamSage_Rev1.py, including the user filters and the display of TV show details. To run the app, Streamlit and BeautifulSoup need to be installed.

Rev3: Fetching data from tvmaze and themoviedb.org site. WIP!!!!
StreamSage_Rev3.py is the third revision of the StreamSage application. This version introduces integration with external APIs to fetch real TV show data.

Key Updates:

Integration with TVmaze and TMDb APIs: The application now fetches TV show data from the TVmaze and TMDb APIs. This allows the app to display a wide range of TV shows from various streaming providers and channels.

Filtering of TV Shows: The app filters the TV shows based on the user's selected genre, language, duration, and rating. The filtered shows are then displayed in the app.

Display of TV Show Details: The app displays the details of each recommended TV show, including the title, genre, language, duration, platform, summary, and rating. The summary is parsed using BeautifulSoup to remove any HTML tags.

Technical Details:

Requests: The app uses the requests library to send HTTP requests to the TVmaze and TMDb APIs.

BeautifulSoup: The app uses the BeautifulSoup library to parse the summary of each TV show.

List Comprehensions: The app uses list comprehensions to filter the TV shows based on the user's selected filters.

The rest of the app remains the same as in StreamSage_Rev2.py, including the welcome message and instructions. To run the app, Streamlit, BeautifulSoup, and requests need to be installed.

Rev4:
StreamSage_Rev4.py is the fourth revision of the StreamSage application. This version enhances the user experience and provides more detailed information about TV shows.

Key Updates:

Dynamic Filtering: The available options for each filter (streaming provider, genre, and language) are now dynamically extracted from the fetched data. This ensures that the filter options always reflect the current state of the TVmaze database.

Enhanced Display of Recommendations: The display of recommended TV shows has been enhanced. For each recommended show, the program now displays the title, genre, language, duration, platform, summary, and rating.

User-Friendly Interface: The user interface has been improved. Streamlit's interactive widgets are used for the filters, and its markdown support is used to format the displayed information in a readable way.

HTML Tag Removal: The program now uses BeautifulSoup to remove HTML tags from the summaries of the TV shows before displaying them. This ensures that the summaries are displayed in plain text, making them easier to read.

Technical Details:

Streamlit: The app uses Streamlit's interactive widgets for the filters and its markdown support to format the displayed information.

BeautifulSoup: The app uses the BeautifulSoup library to remove HTML tags from the summaries of the TV shows.

The rest of the app remains the same as in StreamSage_Rev3.py, including the fetching of TV show data from the TVmaze and TMDb APIs. To run the app, Streamlit, BeautifulSoup, and requests need to be installed.


**Rev1**
Packages Needed: This program uses the streamlit package. Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. You can install it using conda-forge: install streamlit.

Functions Needed: The fetch_data() function is needed which is not shown in the provided code. This function should return a list of TV shows, where each TV show is a dictionary with keys like "title", "genre", "language", "duration", "platform", and "rating".

Program Execution:

The program first fetches the data by calling fetch_data() and stores the result in TV_SHOWS.

It then creates selectboxes for the streaming service provider, genre, language, and user ratings using the st.selectbox function. The options for these selectboxes are taken from STREAMING_PROVIDERS, GENRES, LANGUAGES, and a list of ratings from 1 to 10.

The program then filters the TV shows based on the user's preferences. It creates a new list filtered_shows that includes only the shows that match the selected platform, genre, language, and have a rating greater than or equal to the selected rating.

Finally, the program displays the recommended shows. For each show in filtered_shows, it writes the title, genre, language, duration, platform, and rating to the Streamlit app using st.write.

How to Run the Program: To run the program, you need to have Streamlit installed and then you can run the script using the command streamlit run StreamSage_Rev1.py in your terminal. This will start a local server and open the Streamlit app in your web browser.

- AS-IS Workflow: [Insert diagram here] - This diagram will illustrate the current method businesses use to ....... [TBD]
- TO-BE Workflow: [Insert diagram here] - This diagram will demonstrate how ....... [TBD]

Description of Solution:

• Workflow diagram of future ("TO-BE") state (improved processes from your solution). [TBD]
• Future Releases (V1.x and beyond): 
	- Plans include adding more interactive features for data visualization, real-time data processing, and integration with CRM systems.
• Additional requirements, Graphical User Interfaces (GUI), usability, etc. for later versions
 		- Enhanced GUI features for more intuitive user interaction, UI features like sliding scale adjustments
	- Advanced data validation and error handling to ensure robust application performance.
Solution Design (high-level): [TBD]

Solution Code Description (low-level design):

This section provides an in-depth look at the code structure, explaining the purpose and functionality of each component of the application.

• Software packages (Python packages, etc.)
- Streamlit: For building the interactive web app.
- BeautifulSoup: Python library that is used for web scraping purposes to pull the data out of HTML and XML files.

Actual Working Product Code: [TBD] Functions, modules, packages, documentation

Application Instructions: Instructions to install, set-up, and use software:

Clone the repository: git clone [https://github.com/MMBOSTON/StreamSage]
Create and activate the Conda environment: conda env create -f environment.yml conda activate acct_score_env
Install required packages: conda install -r requirements.txt
Start the application: python acct_score.py Follow the GUI prompts to upload data and input attributes and weights.

Rich's 6 D Agile Process:

Idea8
Define
Design
Develop
Debug
Document
Deliver
Deploy
Jinja2 Jinja3 ==> Jinja

**Future enhancements**:
-
-
-


