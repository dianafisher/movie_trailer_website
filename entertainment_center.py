import media
import fresh_tomatoes

__author__ = 'diana_fisher'

# Create an instance of class Movie with metadata for Toy Story.
toy_story = media.Movie("Toy Story", 1995,
                        ["Tom Hanks", "Tim Allen", "Andrew Stanton",
                         "Wallace Shawn"], "John Lasseter", "Pixar",
                        "Woody (Tom Hanks), a good-hearted cowboy doll who "
                        "belongs to a young boy named "
                        "Andy (John Morris), sees his position as Andy's "
                        "favorite toy jeopardized when his"
                        " parents buy him a Buzz Lightyear (Tim Allen) action "
                        "figure. Even worse, the arrogant "
                        "Buzz thinks he's a real spaceman on a mission to "
                        "return to his home planet. When Andy's "
                        "family moves to a new house, Woody and Buzz must "
                        "escape the clutches of maladjusted neighbor "
                        "Sid Phillips (Erik von Detten) and reunite with "
                        "their boy.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13"
                        "/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")

# Create an instance of class Movie with metadata for School of Rock.
school_of_rock = media.Movie("School of Rock", 2003,
                             ["Jack Black", "Joan Cusack", "Mike White",
                              "Sarah Silverman"], "Richard Linklater",
                             "Paramount Pictures",
                             "After being kicked out of a rock band, "
                             "Dewey Finn becomes a substitute teacher of a "
                             "strict elementary private school, only to try "
                             "and turn it into a rock band.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb"
                             "/1/11/School_of_Rock_Poster.jpg/220px"
                             "-School_of_Rock_Poster.jpg",
                             "https://youtu.be/3PsUJFEBC74")

# Create an instance of class Movie with metadata for Ratatouille.
ratatouille = media.Movie("Ratatouille", 2007,
                          ["Patton Oswalt", "Ian Holm", "Lou Romano"],
                          "Brad Bird", "Walt Disney Pictures",
                          "A rat who can cook makes an unusual alliance with "
                          "a young kitchen worker at a famous "
                          "restaurant.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/5"
                          "/50/RatatouillePoster.jpg/220px"
                          "-RatatouillePoster.jpg",
                          "https://youtu.be/md_eEM9BWd8")

# Create an instance of class Movie with metadata for Gravity.
gravity = media.Movie("Gravity", 2013, ["Sandra Bullock", "George Clooney"],
                      "Alfonso Cuaron", "Esperanto Filmoj",
                      "A medical engineer and an astronaut work together to "
                      "survive after a catastrophe destroys "
                      "their shuttle and leaves them adrift in orbit.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/f/f6"
                      "/Gravity_Poster.jpg/220px-Gravity_Poster"
                      ".jpg", "https://www.youtube.com/watch?v=OiTiKOy59o4")

# Create an instance of class Movie with metadata for Edge of Tomorrow.
edge_of_tomorrow = media.Movie("Edge of Tomorrow", 2014,
                               ["Tom Cruise", "Emily Blunt", "Bill Paxton",
                                "Brendan Gleeson"], "Doug Liman",
                               "Village Roadshow",
                               "A military officer is brought into an alien "
                               "war against an extraterrestrial enemy who "
                               "can reset the day and know the future. When "
                               "this officer is enabled with the same "
                               "power, he teams up with a Special Forces "
                               "warrior to try and end the war.",
                               "https://upload.wikimedia.org/wikipedia/en"
                               "/thumb/f/f9/Edge_of_Tomorrow_Poster.jpg"
                               "/220px-Edge_of_Tomorrow_Poster.jpg",
                               "https://www.youtube.com/watch?v=vw61gCe2oqI")

# Create an instance of class Movie with metadata for Jurassic World.
jurassic_world = media.Movie("Jurassic World", 2015,
                             ["Chris Pratt", "Bryce Dallas Howard",
                              "Vincent D'Onofrio"], "Colin Trevorrow",
                             "Amblin Entertainment",
                             "A new theme park is built on the original site "
                             "of Jurassic Park. Everything is going "
                             "well until the park's newest attraction--a "
                             "genetically modified giant stealth killing "
                             "machine--escapes containment and goes on a "
                             "killing spree.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb"
                             "/6/6e/Jurassic_World_poster.jpg/220px"
                             "-Jurassic_World_poster.jpg",
                             "https://youtu.be/RFinNxS5KN4")


# Create a list of Movie objects.
movies = [toy_story, school_of_rock, ratatouille, gravity, edge_of_tomorrow,
          jurassic_world]

# Pass the list of movie objects into the open_movies_page function of
# fresh_tomatoes.
fresh_tomatoes.open_movies_page(movies)
