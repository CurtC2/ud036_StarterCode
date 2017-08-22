import json
import httplib


class MovieDBAPI():
    '''This class provides access helper functions to The Movie DB API.'''

    def __init__(self, api_key):
        self.api_key = api_key

        # HTTP query for the current API configuration data (JSON)
        # used to build URLs etc. for this instance
        conn = httplib.HTTPConnection('api.themoviedb.org')
        payload = '{}'
        conn.request('GET', '/3/configuration?api_key=' + self.api_key,
                     payload)
        res = conn.getresponse()

        # if the API key worked, continue
        if res.status == 200:
            self.status = 'OK'

            data = res.read()
            conn.close()

            # Use json stdlib to load config data to a dictionary
            config = json.loads(data)

            # Rather than keeping the whole config JSON around, just pull out
            # what we need for now into instance vars
            self.base_url = config['images']['base_url']
            # Get an appropriate available poster_size
            if 'w342' in config['images']['poster_sizes']:
                self.poster_size = 'w342'
            elif 'w500' in config['images']['poster_sizes']:
                self.poster_size = 'w500'
            else:
                self.poster_size = 'original'

        # API key query for configuration failed, set error status
        else:
            self.status = 'Error'

    def get_movie_data(self, tmdb_id):
        '''Query the movie DB for the TMDB movie ID passed in.
           Returns a dictionary of selected info formatted for Movies()'''

        # Get the JSON data payload for the movie ID passed in
        conn = httplib.HTTPConnection('api.themoviedb.org')
        payload = '{}'
        conn.request('GET',
                     '/3/movie/'+tmdb_id+'?api_key=' + self.api_key +
                     '&append_to_response=videos',
                     payload)
        res = conn.getresponse()
        data = res.read()
        conn.close()

        # Use json stdlib to load data to a dictionary
        temp = json.loads(data)

        # Dictionary with movie data formatted for Movies() class init
        movie_data = {}
        movie_data['title'] = temp['title']
        movie_data['storyline'] = temp['overview']
        movie_data['poster_image_url'] = self.base_url + self.poster_size + \
            temp['poster_path']

        # Pick out the list of video results
        videos = temp['videos']['results']

        # iterate the list of dictionaries for the youtube trailer
        trailer = next((dx for dx in videos
                       if (dx['type'] == 'Trailer' and
                           dx['site'] == 'YouTube')),
                       'None found')

        if trailer == 'None found':
            trailer_url = ''
        else:
            trailer_url = 'https://youtu.be/' + trailer['key']

        movie_data['trailer_url'] = trailer_url

        return movie_data
