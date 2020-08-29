from typing import List

import pytest

from domainmodel.movie import Movie


class WatchList:
    def __init__(self):
        self.__watch_list: List[Movie] = list()

    def __repr__(self):
        return repr(self.__watch_list)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.__watch_list):
            self.index += 1
            return self.__watch_list[self.index]
        else:
            raise StopIteration

    def add_movie(self, movie):
        if type(movie) is Movie and movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie):
        if type(movie) is Movie and movie in self.__watch_list:
            self.__watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if type(index) is int:
            if index >=0 and index < len(self.__watch_list):
                return self.__watch_list[index]
            else:
                return None

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        if len(self.__watch_list) > 0:
            return self.__watch_list[0]
        else:
            return None
