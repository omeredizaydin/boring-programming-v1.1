import csv
from io import open
from queue import PriorityQueue

class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

cities = {}


def listCities(cities):
    for city in cities:
        print(city, cities[city].neighbors)

def build_graph(path, printMap):
    with open("cities.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for line in reader:
            city1 = line[0]
            city2 = line[1]
            weight = line[2]
            if city1 not in cities:
                cities[city1] = Node(city1)
            if city2 not in cities:
                cities[city2] = Node(city2)

            cities[city1].neighbors[city2] = int(weight)
            cities[city2].neighbors[city1] = int(weight)

    if printMap:
        listCities(cities)


def uniform_cost_search(graph, start, end):
    if start not in cities and end not in cities:
        CityNotFoundError(start)
        CityNotFoundError(end)
        return
    if end not in cities and start in cities:
        CityNotFoundError(end)
        return
    if end in cities and start not in cities:
        CityNotFoundError(start)
        return
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start, [start]))

    while queue:
        cost, current, route = queue.get()

        if current not in visited:
            visited.add(current)

            if current == end:
                print(" City " + start + " to " + end + ",the shortest route is: ")
                print(" ----- ".join(route))
                print(" cost : ", cost, " distance.\n")
                return

            neighbors = cities[current].neighbors
            for city in neighbors:
                if city not in visited:
                    total_cost = cost + neighbors[city]
                    queue.put((total_cost, cities[city].name, route + [cities[city].name]))


if __name__ == "__main__":
    try:
        build_graph("cities.csv", False)
        while True:
            print("*****PLEASE ENTER ENGLISH LETTERS :( *****   DON'T USE TURKISH LETTERS EXAMPLE Diyarbakir is ok.   Diyarbakır is NOT OK......")
            inputCity1 = input("Enter name of first city:  ")
            inputCity2 = input("Enter name of second city:  ")
            uniform_cost_search(cities, inputCity1, inputCity2)
    except CityNotFoundError:
        print("City not found, Something went wrong..... :((:((( ")
