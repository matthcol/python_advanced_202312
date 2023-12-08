import numpy as np

from city import City
from typing import List

def compute(n: int) -> List[City]:
    nums = np.random.normal(1000, 10, n)
    return [
        City(name="Lost", zipcode="00000", population=int(v)) 
        for v in nums
    ]