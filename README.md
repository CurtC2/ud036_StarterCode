# ud036_StarterCode
Source code for a Movie Trailer website project as part of Udacity's Full Stack
Web Developer NanoDegree.

## Installation
Clone the GitHub repository and run the entertainment_center.py in Python 2.7
(developed using Python 2.7.13).  This will generate and load a web page in the
default system browser that shows information about the six configured movies.

## Configuration
As cloned, the application will use the metadata coded in the movies.cfg
sections for each movie:
- The Movie DB movie ID
- Title
- Story Line
- Poster Image
- Trailer URL

The app also offers the option of looking that information up from The Movie
DB API.  To configure and turn on the API use, a valid API Key must be entered
at the top of the movies.cfg file.  In the event the API fails or is
misconfigured the app will revert to using the metadata in the config file.

### The Movie DB API Key
1. Sign up for an account at The Movie DB:  https://www.themoviedb.org/account/signup
2. For your user, access Account Settings
3. Choose the API section, and click the link to "Request an API Key" for a Developer
4. Fill out the form, Suggested type of use:  Personal, URL: None
5. Place the API key (v3 auth) in the [themoviedb] section of the movies.cfg file

## Files
- **entertainment_center.py**
-- Main module that configures and launches the fresh_tomatoes
open_movies_page function.
- **media.py**
-- Implements the Movie class to store information and launch the trailer URL.
- **moviedbapi.py**
-- Implements the MovieDBAPI class to handle the Movie DB API calls.
- **movies.cfg**
-- Configuration data for entertainment_center.py.
- **fresh_tomatoes.py**
-- Udacity supplied HTML page generator functions, with minor modifications 
for styling, display of storyline, and attribution for TMDb data.
