from typing import TypedDict

class Movie(TypedDict):
    name: str
    year: int
    
movie: Movie = {"name": "Blade Runner", "year": 1982}
movie2: Movie = {"name": "123", "year": 1982}
print(movie)

# run "mypy TypedDict.py" to check.