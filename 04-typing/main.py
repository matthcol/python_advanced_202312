from typing import List, Dict, Set, Tuple, Any, Sequence, Iterable, Iterator

def f(text: str) -> str:
    return text.upper()

def extract_odd_elements(l: list) -> list:
    return l[1::1]

def extract_odd_elements2(l: Sequence) -> Sequence:
    return l[1::1]

def find_after_index(seq: Sequence, index: int, value: Any) -> Any|None: # i.e Optional[Any] 
    for e in seq[index:]:
        if e == value:
            return e
    return None

def sum_square(l: List[int]) -> int:
    return sum(x**2 for x in  l)

def sum_square2(l: Iterable[int]) -> int:
    return sum(x**2 for x in  l)

def play_with_lists() -> None:
    l1: List[int] = [1,2,3,44]
    l2: List[str] = ["Toulouse", "Pau"]
    # reveal_type(l1)
    # reveal_type(l2)
    print(extract_odd_elements(l1))
    print(extract_odd_elements(l2))
    s1 = sum_square(l1)
    # error: Argument 1 to "sum_square" has incompatible type "list[str]"; expected "list[int]"
    # s1 = sum_square(l2)

def play_with_tuples_dicts() -> None:
    city_t: Tuple[str,int,str] = ("Toulouse", 470_000, "31000")
    city_d: Dict[str, str] = {
        "name": "Toulouse",
        "zipcode": "31000",
        "departement": "Haute Garonne",
    }
    city2_d: Dict[str, Any] = {
        "name": "Toulouse",
        "population": 470_000,
        "zipcode": "31000",
        "dep_code": 31,   
        "dep_name": "Haute Garonne",
    }
    city2_d["is_coastal"] = False
    city3_d: Dict[str, str|int] = {
        "name": "Toulouse",
        "population": 470_000,
        "zipcode": "31000",
        "dep_code": 31,   
        "dep_name": "Haute Garonne",
    }
    city3_d["is_coastal"] = False # ok because bool is a subclass of int
    # city3_d["avg_temp"] = 13.5 # error type
    # reveal_type(city3_d)
    print(city_t, city_d, city2_d, city3_d)


def play_with_sequence_iterable() -> None:
    l1: List[int] = [1,2,3,44]
    t2: Tuple[str, int] = ("Toulouse", 470_000)
    s3: Set[str] = { "Toulouse", "Pau" }
    r1 = extract_odd_elements2(l1)
    r2 = extract_odd_elements2(t2)
    # r3 = extract_odd_elements2(s3) # not a sequence

    # t4: Tuple[int,int,int,int] = (12,21,34,43) # ok
    t4: Sequence[int] = (12,21,34,43) # ok
    r5: range = range(1000)
    g6: Iterator[int] = (x**3-1 for x in range(10)) 
    sum1 = sum_square2(l1)
    sum2 = sum_square2(t4)
    sum3 = sum_square2(r5)
    sum4 = sum_square2(g6)
    # sum5 = sum_square2(t2) # error




if __name__== "__main__":
    print(f("toulouse"))
    
    # error: Argument 1 to "f" has incompatible type "int"; expected "str"
    # print(f(2)) 

    city: str = "Pau"
    # error: Incompatible types in assignment (expression has type "int", variable has type "str")
    # city = 12

    play_with_lists()
    play_with_tuples_dicts()
    play_with_sequence_iterable()
    