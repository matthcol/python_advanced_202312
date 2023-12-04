import magicsquare as mg
import square as sq

def test_is_magic_ko_3_row():
    assert not mg.is_magic(sq.square_ko_row)


def test_is_magic_ko_3_col():
    assert not mg.is_magic(sq.square_ko_col)

def test_is_magic_ko_3_diag():
    assert not mg.is_magic(sq.square_ko_diag)

def test_is_magic_ok_12():
    assert mg.is_magic(sq.square_ok_12)