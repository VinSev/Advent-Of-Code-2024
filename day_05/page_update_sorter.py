from abc import ABC, abstractmethod
from functools import cmp_to_key
from typing import List


class PageUpdateSorter(ABC):
    @abstractmethod
    def sort(self) -> List[int]:
        raise NotImplementedError
    
    
class SimplePageUpdateSorter(PageUpdateSorter):
    def sort(self, page_update: List[int], page_ordering_rules: List[List[int]]) -> List[int]:
        page_update_comparator = lambda x, y: self._compare_page_update(page_ordering_rules, x, y)
        
        return sorted(page_update, key=cmp_to_key(page_update_comparator))
    
    def _compare_page_update(self, page_ordering_rules: List[List[int]], x: int, y: int) -> int:
        if [x, y] in page_ordering_rules:
            return 1
        
        if [y, x] in page_ordering_rules:
            return -1
        
        return 0
