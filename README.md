# StreamSage: Your All-in-One Streaming Companion

**Updated: 2024.04.15**

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

**Rev1**
Packages Needed: This program uses the streamlit package. Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. You can install it using pip: pip install streamlit.

Functions Needed: The fetch_data() function is needed which is not shown in the provided code. This function should return a list of TV shows, where each TV show is a dictionary with keys like "title", "genre", "language", "duration", "platform", and "rating".

Program Execution:

The program first fetches the data by calling fetch_data() and stores the result in TV_SHOWS.

It then creates selectboxes for the streaming service provider, genre, language, and user ratings using the st.selectbox function. The options for these selectboxes are taken from STREAMING_PROVIDERS, GENRES, LANGUAGES, and a list of ratings from 1 to 10.

The program then filters the TV shows based on the user's preferences. It creates a new list filtered_shows that includes only the shows that match the selected platform, genre, language, and have a rating greater than or equal to the selected rating.

Finally, the program displays the recommended shows. For each show in filtered_shows, it writes the title, genre, language, duration, platform, and rating to the Streamlit app using st.write.

How to Run the Program: To run the program, you need to have Streamlit installed and then you can run the script using the command streamlit run StreamSage_Rev1.py in your terminal. This will start a local server and open the Streamlit app in your web browser.

- AS-IS Workflow: [Insert diagram here] - This diagram will illustrate the current method businesses use to evaluate potential customers without Acct_Score. [TBD]
- TO-BE Workflow: [Insert diagram here] - This diagram will demonstrate how Acct_Score streamlines and enhances the customer evaluation process. [TBD]
Description of Solution:

Software functions for solving problem(s) step by step: Python script that will be able to intake custom ideal customer profile attributes like company size, geo, revenue, industry, etc via a GUI. The user can modify inputs for weighing attributes. Input csv file of account data to score the fit of them against the ideal customer profile attributes, output csv with scores.

	- Intake of Custom Attributes: Users can enter attributes such as company size, geography, revenue, and industry via a graphical user interface.
	- Weight Modification: Users have the flexibility to adjust the weights of different attributes based on their significance.
	- Data Processing: The application processes input CSV files containing account data and computes scores based on the predefined attributes and weights.
	- Output Generation: Outputs a CSV file with accounts scored against the ideal customer profiles.

• Workflow diagram of future ("TO-BE") state (improved processes from your solution). [TBD]
• MVP 1.0 Features: Basic attribute input, weight adjustments, score calculation, and CSV output.
• Future Releases (V1.x and beyond): 
	- Improve scoring model accuracy (AI and explore packages)
	- Improve automatic reading of CSV and auto-populating input fields
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


• Complete code: https://github.com/marketerscode/Acct_Score/
Actual Working Product Code: [TBD] Functions, modules, packages, documentation

Application Instructions: Instructions to install, set-up, and use software:

Clone the repository: git clone [https://github.com/marketerscode/Acct_Score/]
Create and activate the Conda environment: conda env create -f environment.yml conda activate acct_score_env
Install required packages: conda install -r requirements.txt
Start the application: python acct_score.py Follow the GUI prompts to upload data and input attributes and weights.
Review the output CSV for scored accounts.

• Additional Important Guidelines for Product Usability (for others to use your work products:
 - Ensure all input CSV files are formatted correctly with the necessary headers as specified.
 - Check the compatibility of your Python version with the libraries used.
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

How to Use
To use the application, follow these steps:

Open the application in your web browser.
For each attribute, input the target value and weight. For numerical attributes, the target value should be a number. For categorical attributes, the target value should be one of the possible categories.
Click the 'Calculate Fit Scores' button to calculate the fit scores for each account.
The fit scores will be displayed in a table. You can sort the table by any column by clicking on the column header.
Requirements
To run this application, you will need:

**Future enhancements**:

Adding more attributes
Allowing the user to upload their own data
Adding more sophisticated scoring algorithms
Improving the user interface
Contributing
Contributions to this project are welcome. Please fork the repository and create a pull request with your changes.
