from grid_search_strategy import GridSearchStrategy


class WordSearch:  
    def __init__(self, search_strategy: 'GridSearchStrategy') -> None:
        self._search_strategy = search_strategy

    def set_search_strategy(self, search_strategy: 'GridSearchStrategy') -> None:
        self._search_strategy = search_strategy

    def search(self) -> int:
        return self._search_strategy.search()
