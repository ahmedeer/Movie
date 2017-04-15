import fresh_tomatoes
import media

midnight_in_paris = media.Movie("Midnight in Paris",
                        "exaggerated screenwriter, his materialistic fiancée.",
                        "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=BYRWfS2s2v4")

#print (midnight_in_paris.storyline)

inception= media.Movie("Inception",
                            "stealing valuable secrets from subconscious during the dream state.",
                            "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                            "https://www.youtube.com/watch?v=YoHD9XEInc0")
#print (inception.storyline)
#inception.show_trailer()

interstellar= media.Movie("Interstellar",
                            "future of the earth where humanity is struggling to survive.",
                            "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                            "https://www.youtube.com/watch?v=M-xglYg-TTw")

chappie= media.Movie("Chappie",
                      "Robot, mimics a human mind to the point of feeling emotions and having opinions",
                      "https://upload.wikimedia.org/wikipedia/en/7/71/Chappie_poster.jpg",
                      "https://www.youtube.com/watch?v=l6bmTNadhJE")

now_you_see_me= media.Movie("Now you see Me",
                             "Story of 4 magicians, who steels money",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Now_You_See_Me_Poster.jpg",
                             "https://www.youtube.com/watch?v=4OtM9j2lcUA")

focus= media.Movie("Focus",
                    "never to lose focus when faced with unexpected situations",
                    "https://upload.wikimedia.org/wikipedia/en/b/bf/2015_Focus_film_poster.png",
                    "https://www.youtube.com/watch?v=MxCRgtdAuBo")

the_pursuit_of_happyness= media.Movie("The Pursuit of Happyness",
                                      "salesman invests his entire life savings in portable bone density scanners",
                                      "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                                      "https://www.youtube.com/watch?v=89Kq8SDyvfg")
baahubali_2_the_conclusion= media.Movie("Baahubali 2 - The Conclusion",
                                        "Empire of Mahishmati, Sivagami, emerges injured from a cave adjoining waterfall",
                                        "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                                        "https://www.youtube.com/watch?v=G62HrubdD6o")

movies = [inception, interstellar, chappie, now_you_see_me, focus, midnight_in_paris, the_pursuit_of_happyness, baahubali_2_the_conclusion]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
#print (media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
