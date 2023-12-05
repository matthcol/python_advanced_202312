import classic.city as cty
import pytest

@pytest.fixture
def city_greater():
    return cty.City("Valence")

def test_less_than_ok(city1, city_greater):
    assert city1 < city_greater

def test_greater_than_ok(city1, city_greater):
    assert city_greater > city1

def test_less_or_equals_ok(city1, city_greater):
    assert city1 <= city_greater

def test_greater_or_equals_ok(city1, city_greater):
    assert city_greater >= city1

def test_less_than_none_field(city1):
    city2 = cty.City()
    assert city1 < city2

# test sort cities ...
def test_sort(city1):
    c2 = cty.City()
    c3 = cty.City("Toulouse")
    c4 = cty.City(zipcode=10000)
    c5 = cty.City("Marseille", 900000, 13000)
    c6 = cty.City("Bordes", 752, 65190)
    c7 = cty.City("Bordes", 2803, 64510)
    c8 = cty.City(city1.name, city1.population, city1.zipcode)
    cities = [city1, c2, c3, c4, c5, c6, c7, c8]
    cities_sorted = sorted(cities)
    assert cities_sorted == [c7, c6, c5, city1, c8, c3, c4, c2]
    assert cities_sorted == [c7, c6, c5, c8, city1, c3, c4, c2]
    assert cities_sorted[3] is city1
    assert cities_sorted[4] is c8