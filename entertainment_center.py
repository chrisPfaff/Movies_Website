# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

jaws = media.Movie("Jaws","A story of a killer great white"
	,"https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg"
	,"https://www.youtube.com/watch?v=U1fu_sA7XhE")

#print(toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien planet",
	"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg"
	,"https://www.youtube.com/watch?v=5PSNL1qE6VY")

deadpool = media.Movie("Deadpool", "Gifted with accelerated healing powers and a twisted sense of humor, mercenary Wade Wilson (Ryan Reynolds) adopts the alter ego Deadpool and hunts down the man who nearly destroyed his life."
	,"https://pbs.twimg.com/media/CVKQTAoUkAAGbhs.jpg"
	,"https://www.youtube.com/watch?v=ZIM1HydF9UA")

star_wars_empire = media.Movie("Empire Strikes Back",
	"Second episode of star wars saga","http://vignette3.wikia.nocookie.net/starwars/images/e/e4/Empire_strikes_back_old.jpg/revision/latest?cb=20061201083417"
	,"https://www.youtube.com/watch?v=96v4XraJEPI")
#print(avatar.storyline)
#deadpool.show_trailer()
#avatar.show_trailer()
#ratatouille.show_tra  iler()

movies = [ jaws, avatar, deadpool , star_wars_empire]
fresh_tomatoes.open_movies_page(movies)


