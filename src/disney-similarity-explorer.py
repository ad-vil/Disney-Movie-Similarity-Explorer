import sys
import csv
from random import random


class MovieEnvironment:
    def __init__(self):  # constructor method to initialize variables
        filepath = r"disney-movies-data.csv"
        self.titles = []
        self.length = 0
        self.__tdict = {}
        self.__adj_list = {}

        self.__read_movie_data(filepath)
        self.__generate_graph()

    def __read_movie_data(self, filepath):
        file = open(filepath, "r")
        # open file movie data
        data = list(csv.reader(file, delimiter=","))
        # adds names of movies to list
        self.titles = [row[0] for row in data]
        file.close()
        self.length = len(self.titles)  # length = number of movies in data set

    def __generate_graph(self):
        i = 0
        while i < 500:  # number of edges in the graph.
            r1 = int(random() * self.length)
            r2 = int(random() * self.length)
            while r2 == r1:
                r2 = int(random() * self.length)
                # assigning similarity weights to each pair of movies

            while (r1, r2) in self.__tdict.keys() or (r2, r1) in self.__tdict.keys():
                r2 = int(random() * self.length)

            self.__tdict[(r1, r2)] = 1
            self.__tdict[(r2, r1)] = 1
            # adds movies to tdict with indices as keys and weight of 1

            weight = random()
            self.__adj_list.setdefault(self.titles[r1], {})[self.titles[r2]] = round(weight, 2) * 100
            self.__adj_list.setdefault(self.titles[r2], {})[self.titles[r1]] = round(weight, 2) * 100
            i += 1
            # adds similar movies to adj list

    def get_neighbours(self, m1):
        """
        Returns the neighbours (similar movies) for a movie.

        :param str m1: The movie name whose neighbours to find.
        :return dict[str,float]: The dictionary of neighbour nodes and their link weights (0-100) as float which show similarity (lower value means more similar).
        """
        return self.__adj_list[m1]

    def display_graph(self):
        import networkx as nx
        g = nx.DiGraph(self.__adj_list)
        nx.draw(g, with_labels=True, font_weight='bold')
        import matplotlib.pyplot as plt
        plt.show()


# Import the necessary modules
from collections import deque


def breadth_first_search(env, movie1, movie2):
    visited = {}  # creating visited queue for movies and their parents
    queue = deque([movie1])  # creating queue for bfs traversal
    visited[movie1] = None

    while queue:
        current_movie = queue.popleft()
        if current_movie == movie2:  # if movie2 is found then reconstruct the queue
            path = []
            while current_movie:
                path.append(current_movie)
                current_movie = visited[current_movie]
            return path[::-1]  # Reverse the path to get it from movie1 to movie2

        for neighbor in env.get_neighbours(current_movie):
            # using this for loop to find neighbors (similar movies) of current movies
            if neighbor not in visited:
                visited[neighbor] = current_movie
                queue.append(neighbor)

    return None  # base case


def depth_first_search(env, movie1, movie2):
    visited = {}
    stack = [movie1]  # using a stack for dfs
    visited[movie1] = None

    while stack:
        current_movie = stack.pop()
        if current_movie == movie2:
            path = []
            while current_movie:
                path.append(current_movie)
                current_movie = visited[current_movie]
            return path[::-1]

        for neighbor in env.get_neighbours(current_movie):
            if neighbor not in visited:
                visited[neighbor] = current_movie
                stack.append(neighbor)
                # its basically all the saem as dfs except using a stack instead of a queue

    return None


def uniform_cost_search(env, movie1, movie2):
    cost = {movie1: 0}
    # storing the cost to reach a movie
    visited = {}
    # strong the visited movies and their parent
    priorityQueue = [(0, movie1)]
    visited[movie1] = None
    # ucs uses a priority queue

    while priorityQueue:
        current_cost, current_movie = priorityQueue.pop(0)
        # pop movie with the lowest cost
        if current_movie == movie2:
            path = []
            while current_movie:
                path.append(current_movie)
                current_movie = visited[current_movie]
            return path[::-1]
        # if movie 2 is found then reconstruct the path and reverse same as dfs and bfs

        # Explore the neighbors of the current movie
        for neighbor, weight in env.get_neighbours(current_movie).items():
            total_cost = current_cost + weight
            if neighbor not in cost or total_cost < cost[neighbor]:
                cost[neighbor] = total_cost
                visited[neighbor] = current_movie
                priorityQueue.append((total_cost, neighbor))
                priorityQueue.sort(key=lambda x: x[0])
                # sorting priority queue based on its cost

    return None


if __name__ == "__main__":
    env = MovieEnvironment()

    print("available movies:")
    for movie in env.titles:
        print(movie)
        # extra method to print out all the available movies

    movie1 = input("\nenter the name of the first movie (CASE SENSITIVE!): ")
    i = 1
    while movie1 not in env.titles:
        print("movie not found in the list.")
        movie1 = input("enter the name of the first movie: ")
        i += 1
        if i >= 3:
            sys.exit()

    movie2 = input("\nenter the name of the second movie: ")
    i = 1
    while movie2 not in env.titles:
        print("movie not found in the list.")
        movie2 = input("enter the name of the second movie: ")
        i += 1
        if i >= 3:
            sys.exit()

    print("\nbreadth-first search result:", breadth_first_search(env, movie1, movie2))
    print("depth-first search result:", depth_first_search(env, movie1, movie2))
    print("uniform cost search result:", uniform_cost_search(env, movie1, movie2))

    # fixed up formatting a little bit too so it looks much nicer
    env.display_graph()
