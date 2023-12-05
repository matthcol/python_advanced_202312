from typing import override
from functools import total_ordering
# NB: class classic.city.City

@total_ordering
class City:
    """class City representing a city with:
    - its name
    - its population
    - its main zipcode
    """
    
    def __init__(self, name=None, population=None, zipcode=None):
        self.name = name
        self.population = population
        self.zipcode = zipcode
        
    # overrides both __repr__ and __str__ if no override of __str__
    @override
    def __repr__(self):
        return f"City[name={self.name}, pop={self.population}, zipcode={self.zipcode}]"
    
    @override
    def __str__(self):
        return f"{self.name} (pop={self.population}, zipcode={self.zipcode})"
    
    @override
    def __eq__(self, other):
        # other is a City (strict with type() or isinstance to accept subclasses)
        # other has attributes: name, zipcode, population
        if type(other) is not City:
            return NotImplemented
        return (self.name, self.zipcode) == (other.name, other.zipcode)
    
    @override
    def __lt__(self, other):
        if type(other) is not City:
            return NotImplemented
        # specific case with None
        match (self.name, self.zipcode, other.name, other.zipcode):
            case (None, _, _, _) if other.name is not None:
                return False
            case (_, _, None, _) if self.name is not None:
                return True
            case (_, None, _, _) if (self.name == other.name) and (other.zipcode is not None):
                return False
            case (_, _, _, None) if (self.name == other.name) and (self.zipcode is not None):
                return True
            case _:
                return (self.name, self.zipcode) < (other.name, other.zipcode)