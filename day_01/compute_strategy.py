from abc import ABC, abstractmethod
from collections import Counter
from typing import List


class ComputeStrategy(ABC):
    @abstractmethod
    def compute(self, left_location_ids: List[int], right_location_ids: List[int]) -> int:
        pass
    
    
class DistanceDeltaCalculator(ComputeStrategy):
    def compute(self, left_location_ids: List[int], right_location_ids: List[int]) -> int:
        sorted_left_location_ids = sorted(left_location_ids)
        sorted_right_location_ids = sorted(right_location_ids)
        
        distance_delta = 0
        
        for left_location_id, right_location_id in zip(sorted_left_location_ids, sorted_right_location_ids):
            distance_delta += abs(left_location_id - right_location_id)
        
        return distance_delta
    

class SimilarityScoreCalculator(ComputeStrategy):
    def compute(self, left_location_ids: List[int], right_location_ids: List[int]):
        right_location_ids_counts = Counter(right_location_ids)
        
        similarity_score = 0
        
        for left_location_id in left_location_ids:
            count_in_right = right_location_ids_counts.get(left_location_id, 0)
            similarity_score += left_location_id * count_in_right
        
        return similarity_score
