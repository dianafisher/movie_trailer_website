import webbrowser

__author__ = 'diana_fisher'


class Movie():
    """Class Movie contains all metadata for a particular movie.

    Attritubes:
        title: A string which contains the title of the movie.
        release_year: An integer containing the year the movie was
        released in theaters (in the US).

        cast: A list of strings.  Each string is the
        cast member's full name.

        director: A string containing the full name of the director.

        production_company: A string containing the company
        which produced the movie, e.g. Disney, Fox, ...

        synopsis: A string containing a brief summary of the movie plot.
        poster_image_url: A string containing the full url
        to the movie poster image.

        trailer_youtube_url: A string containing the full
        url to the movie trailer on youtube.

    """

    def __init__(self, title, release_year, cast, director,
                 production_company, synopsis, poster_image_url,
                 trailer_youtube_url):
        """Initializes Movie with title, release_year,
        cast, director, production_company, synopsis,
        poster_image_url, and trailer_youtube_url.
        """

        self.title = title
        self.release_year = release_year
        self.cast = cast
        self.director = director
        self.production_company = production_company
        self.synopsis = synopsis
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Launches a web browser with the youtube trailer url.

        Args: none

        Returns: none
        """
        webbrowser.open(self.trailer_youtube_url)
