from dataclasses import dataclass, field

# @dataclass(kw_only=True) # disable constructor with positional arguments
@dataclass(order=True, slots=True)
class City:

    # NB: in traditional class without @dataclass
    # __slots__ = ['name','zipcode','population']

    name: str
    zipcode: str
    population: int = field(default=0, compare=False) # eq and lt don't use this field