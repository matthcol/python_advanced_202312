def f(text: str) -> str:
    return text.upper()

def extract_odd_elements(l: list) -> list:
    return l[1::1]

def sum_square(l: list) -> int:
    return sum(x**2 for x in  l)

def play_with_lists():
    l1 = [1,2,3,44]
    l2 = ["Toulouse", "Pau"]
    print(extract_odd_elements(l1))
    print(extract_odd_elements(l2))
    s1 = sum_square(l1)
    s1 = sum_square(l2)


if __name__== "__main__":
    print(f("toulouse"))
    
    # error: Argument 1 to "f" has incompatible type "int"; expected "str"
    # print(f(2)) 

    city: str = "Pau"
    # error: Incompatible types in assignment (expression has type "int", variable has type "str")
    # city = 12

    play_with_lists()
    