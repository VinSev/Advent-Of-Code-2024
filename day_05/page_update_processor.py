from abc import ABC, abstractmethod
from typing import List

from page_update_sorter import PageUpdateSorter


class PageUpdateProcessor(ABC):
    @abstractmethod
    def sum_of_middle_page_updates(self, page_updates: List[List[int]], page_ordering_rules: List[List[int]]) -> int:
        raise NotImplementedError
    
    def _is_ordered(self, page_update: List[int], page_ordering_rules: List[List[int]]) -> bool:
        for page_x, page_y in page_ordering_rules:
            if page_x in page_update and page_y in page_update:
                x = page_update.index(page_x)
                y = page_update.index(page_y)
                
                if x > y:
                    return False
                
        return True

    def _get_middle_page_update(self, page_update: List[int]) -> int:
        middle_index = int(len(page_update) / 2)
        
        return page_update[middle_index]
 
   
class OrderedPageUpdateProcessor(PageUpdateProcessor):
    def sum_of_middle_page_updates(self, page_updates: List[List[int]], page_ordering_rules: List[List[int]]) -> int:
        total = 0
    
        for page_update in page_updates:
            if self._is_ordered(page_update, page_ordering_rules):
                total += self._get_middle_page_update(page_update)
                
        return total

        
class UnorderedPageUpdateProcessor(PageUpdateProcessor):
    def __init__(self, page_update_sorter: 'PageUpdateSorter') -> None:
        self._page_update_sorter = page_update_sorter
    
    def sum_of_middle_page_updates(self, page_updates: List[List[int]], page_ordering_rules: List[List[int]]) -> int:
        total = 0
    
        for page_update in page_updates:
            if not self._is_ordered(page_update, page_ordering_rules):
                sorted_page_update = self._page_update_sorter.sort(page_update, page_ordering_rules)
                total += self._get_middle_page_update(sorted_page_update)
                
        return total
