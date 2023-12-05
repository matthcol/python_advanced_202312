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