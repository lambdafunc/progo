import fresh_tomatoes
from media import Movie

toy_story = Movie("Toy Story", "Story of a Toy", "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
                  "https://www.youtube.com/watch?v=JcpWXaA2qeg")

avatar = Movie("Avatar", "Story of marine in alien land", "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

lion_king = Movie("The Lion King", "Story of a Lion Family",
                "https://images-na.ssl-images-amazon.com/images/I/418g2jo7fBL._AC_UL320_SR216,320_.jpg",
                "https://www.youtube.com/watch?v=GibiNy4d4gc")



#print "Movie name is {}, This is {}".format(toy_story.title, toy_story.storyline)
#print "Movie name is {}, This is {}".format(avatar.title, avatar.storyline)
#print "Movie name is {}, This is {}".format(lion_king.title, lion_king.storyline)

#toy_story.show_trailer()
movies = [toy_story, avatar, lion_king]
fresh_tomatoes.open_movies_page(movies)