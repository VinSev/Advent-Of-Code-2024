from typing import List

from page_update_processor import PageUpdateProcessor


class SafetyManual():
    def __init__(self, page_updates: List[List[int]], page_ordering_rules: List[int], page_update_processor: 'PageUpdateProcessor') -> None:
        self._page_updates = page_updates
        self._page_ordering_rules = page_ordering_rules
        self._page_update_processor = page_update_processor
        
    def set_page_update_processor(self, page_update_processor: 'PageUpdateProcessor') -> None:
        self._page_update_processor = page_update_processor
        
    def sum_of_middle_page_updates(self) -> int:
        return self._page_update_processor.sum_of_middle_page_updates(self._page_updates, self._page_ordering_rules)
      