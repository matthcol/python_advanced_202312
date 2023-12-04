import itertools as it
from square import square_ok_3

def magic_sum(n):
    return n*(n**2+1) // 2


def is_magic(square):
    n = len(square)
    ms = magic_sum(n)

    # iterators on columns and diagonals
    
    # generator of generator  for columns
    columns = (( square[i][j] for i in range(n)) for j in range(n)) 

    # tuple of 2 generators for "diagonals"
    diags = (
        ( square[i][i] for i in range(n) ),
        ( square[i][-i - 1] for i in range(n) )
    )

    return all(sum(values) == ms for values in it.chain(square, columns, diags))

# test written directly in the module
def test_is_magic_ok_3():
    assert is_magic(square_ok_3)