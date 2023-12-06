import pytest
from city import City

def test_city_constructor1():
    city = City("Toulouse","31000")
    assert city.name == "Toulouse"
    assert city.zipcode == "31000"
    assert city.population == 0

def test_city_constructor2():
    city = City("Toulouse","31000", population=470_000)
    assert city.name == "Toulouse"
    assert city.zipcode == "31000"
    assert city.population == 470_000

def test_city_constructor3():
    city = City(name="Toulouse", zipcode="31000", population=470_000)
    assert city.name == "Toulouse"
    assert city.zipcode == "31000"
    assert city.population == 470_000

def test_city_eq_ok():
    city1 = City(name="Toulouse", zipcode="31000", population=470_000)
    city2 = City(name="Toulouse", zipcode="31000", population=470_001)
    assert city1 == city2
    assert not city1 != city2

def test_city_eq_ko():
    city1 = City(name="Toulouse", zipcode="31000", population=470_000)
    city2 = City(name="Toulouse", zipcode="31001", population=470_000)
    assert city1 != city2
    assert not city1 == city2

def test_city_lt_ok():
    city1 = City(name="Toulouse", zipcode="31000", population=470_000)
    city2 = City(name="Toulouse", zipcode="31001", population=470_000)
    assert city1 < city2
    assert city1 <= city2

@pytest.mark.xfail(raises=AttributeError)
def test_city_add_attr_ko():
    city1 = City(name="Toulouse", zipcode="31000", population=470_000)
    city1.dep = 31
    # assert city1.dep == 31

def test_city_del_attr():
    city1 = City(name="Toulouse", zipcode="31000", population=470_000)
    del city1.name
    x = city1.name.upper()
