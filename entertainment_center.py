import fresh_tomatoes
import media
import ConfigParser

# Read in configuration file data
config = ConfigParser.ConfigParser()
config.read('movies.cfg')

# See if there is an The Movie DB API Key set
api_key = config.get('themoviedb', 'api_key')
api_failed = False

if len(api_key) > 0:
    # Create Movie instances from TMDB API
    import moviedbapi
    movie_data = {}

    # Config API instance
    movie_api = moviedbapi.MovieDBAPI(api_key)

    if movie_api.status == 'OK':
        # Pull data & create Movie instances with it
        movie_data = movie_api.get_movie_data(config.get('office_space',
                                                         'tmdb_id'))
        office_space = media.Movie(movie_data['title'],
                                   movie_data['storyline'],
                                   movie_data['poster_image_url'],
                                   movie_data['trailer_url'])

        movie_data = movie_api.get_movie_data(config.get('holy_grail',
                                                         'tmdb_id'))
        holy_grail = media.Movie(movie_data['title'],
                                 movie_data['storyline'],
                                 movie_data['poster_image_url'],
                                 movie_data['trailer_url'])

        movie_data = \
            movie_api.get_movie_data(config.get('lebowski', 'tmdb_id'))
        lebowski = media.Movie(movie_data['title'],
                               movie_data['storyline'],
                               movie_data['poster_image_url'],
                               movie_data['trailer_url'])

        movie_data = movie_api.get_movie_data(config.get('top_gun', 'tmdb_id'))
        top_gun = media.Movie(movie_data['title'],
                              movie_data['storyline'],
                              movie_data['poster_image_url'],
                              movie_data['trailer_url'])

        movie_data = movie_api.get_movie_data(config.get('pulp_fiction',
                                                         'tmdb_id'))
        pulp_fiction = media.Movie(movie_data['title'],
                                   movie_data['storyline'],
                                   movie_data['poster_image_url'],
                                   movie_data['trailer_url'])

        movie_data = \
            movie_api.get_movie_data(config.get('silver_linings_playbook',
                                                'tmdb_id'))
        silver_linings_playbook = media.Movie(movie_data['title'],
                                              movie_data['storyline'],
                                              movie_data['poster_image_url'],
                                              movie_data['trailer_url'])
    else:
        api_failed = True

# if not configured to use API, or it failed, then use config data
if len(api_key) == 0 or api_failed:
    # Create Movie instances from the config data
    office_space = media.Movie(config.get('office_space', 'title'),
                               config.get('office_space', 'storyline'),
                               config.get('office_space', 'poster_image_url'),
                               config.get('office_space', 'trailer_url'))

    holy_grail = media.Movie(config.get('holy_grail', 'title'),
                             config.get('holy_grail', 'storyline'),
                             config.get('holy_grail', 'poster_image_url'),
                             config.get('holy_grail', 'trailer_url'))

    lebowski = media.Movie(config.get('lebowski', 'title'),
                           config.get('lebowski', 'storyline'),
                           config.get('lebowski', 'poster_image_url'),
                           config.get('lebowski', 'trailer_url'))

    top_gun = media.Movie(config.get('top_gun', 'title'),
                          config.get('top_gun', 'storyline'),
                          config.get('top_gun', 'poster_image_url'),
                          config.get('top_gun', 'trailer_url'))

    pulp_fiction = media.Movie(config.get('pulp_fiction', 'title'),
                               config.get('pulp_fiction', 'storyline'),
                               config.get('pulp_fiction', 'poster_image_url'),
                               config.get('pulp_fiction', 'trailer_url'))

    silver_linings_playbook = \
        media.Movie(config.get('silver_linings_playbook', 'title'),
                    config.get('silver_linings_playbook', 'storyline'),
                    config.get('silver_linings_playbook', 'poster_image_url'),
                    config.get('silver_linings_playbook', 'trailer_url'))

movies = [office_space, holy_grail, lebowski, top_gun, pulp_fiction,
          silver_linings_playbook]

fresh_tomatoes.open_movies_page(movies)
