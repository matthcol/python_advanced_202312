# Object Oriented Programming 

## Static type checking
```
mypy -p classic
mypy -m classic.city
```

## Pytest
Options: 
- -v (verbose)
- -k pattern (test selection)
```
pytest
pytest -v 
pytest -k test_not_equals
pytest -k test_not_equals -v 
pytest tests/classic/test_city_equals.py 
```