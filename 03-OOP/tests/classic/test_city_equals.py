import pytest
import classic.city as cty

def test_equals_ok_same(city1):
    assert city1 == city1

def test_not_equals_ko_same(city1):
    assert not city1 != city1

# write test ok with other same name,zipcode, diff pop
# write test ok with other same name,zipcode, pop

# write test ko with other diff name
# write test ko with other diff zipcode
#...
# write test ko with other not a City

@pytest.mark.parametrize(
        "other", ["Toulouse", True, 470_000], 
        ids=["with_str", "with_bool", "with_int"]
)
def test_equals_ko_other_not_a_city(city1, other):
    assert not city1 == other
    assert not other == city1

@pytest.mark.parametrize(
        "other", ["Toulouse", True, 470_000], 
        ids=["with_str", "with_bool", "with_int"]
)
def test_not_equals_ok_other_not_a_city(city1, other):
    assert city1 != other
    assert other != city1
