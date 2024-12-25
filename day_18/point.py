class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __repr__(self) -> str:
        return f'{self.x},{self.y}'
    
    def move(self, direction: 'Point') -> 'Point':
        return self + direction
