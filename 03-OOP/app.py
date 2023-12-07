import classic.city as cty
import sys

city1 = cty.City("Toulouse", 470_000, 31000)

if __name__ == '__main__':
    city2 = cty.City("Marseille", 900_000, 13000)
    print(city1, city2)
    print(sys.argv)