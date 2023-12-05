from typing import override

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