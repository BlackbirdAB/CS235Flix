from typing import List
from domainmodel.movie import Movie
from domainmodel.review import Review


class User:
    def __init__(self, user_name, password):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password
        self.__watched_movies: List[Movie] = list()
        self.__reviews: List[Review] = list()
        self.__time_spent_watching_movies_minutes: int = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> List[Movie]:
        return self.__watched_movies

    @property
    def reviews(self) -> List[Review]:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if type(other) is not User:
            return False
        else:
            return self.__user_name == other.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if type(movie) is Movie:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if type(review) is Review:
            self.__reviews.append(review)
