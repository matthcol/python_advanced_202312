import pytest
import classic.city as cty

@pytest.fixture
def city1():
    return cty.City("Toulouse", 470_000, 31000)