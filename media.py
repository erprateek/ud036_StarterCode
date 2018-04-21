
import fresh_tomatoes
import webbrowser

class Movie(object):
	def __init__(self, name, storyline, poster, trailer_url):
		self.title = name
		self.storyline = storyline
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	def get_storyline(self):
		return self.storyline

	def show_poster(self):
		webbrowser.open(self.poster_image_url)



Avatar = Movie(
	name="Avatar",
	storyline = "Avatar, marketed as James Cameron's Avatar, is a 2009 American[7][8] epic science fiction film directed, written, produced, and co-edited by James Cameron, and starring Sam Worthington, Zoe Saldana, Stephen Lang, Michelle Rodriguez, and Sigourney Weaver.",
	poster="https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
	trailer_url = "https://www.youtube.com/watch?v=5PSNL1qE6VY"
	)

ToyStory = Movie(
	name="ToyStory",
	storyline = "oy Story is a 1995 American computer-animated buddy comedy adventure film produced by Pixar Animation Studios for Walt Disney Pictures. The directorial debut of John Lasseter, Toy Story was the first feature-length computer-animated film and the first feature film produced by Pixar.",
	poster="https://upload.wikimedia.org/wikipedia/sco/6/69/Toy_Story_3_poster.jpg",
	trailer_url = "https://www.youtube.com/watch?v=KYz2wyBy3kc"
	)

Matrix = Movie(
	name="The Matrix",
	storyline = "The Matrix is a 1999 science fiction action film written and directed by The Wachowskis (credited as The Wachowski Brothers) and starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano",
	poster="https://upload.wikimedia.org/wikipedia/sco/c/c1/The_Matrix_Poster.jpg",
	trailer_url = "https://www.youtube.com/watch?v=m8e-FF8MsqU"
	)

fresh_tomatoes.open_movies_page([ToyStory, Avatar, Matrix])