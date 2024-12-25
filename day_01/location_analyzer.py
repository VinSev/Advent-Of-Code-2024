from compute_strategy import ComputeStrategy
from typing import List, Tuple
   
    
class LocationAnalyzer:
    def __init__(
        self, 
        location_id_pairs: List[List[int]], 
        distance_calculator: ComputeStrategy, 
        similarity_calculator: ComputeStrategy
    ) -> None:
        self.left_location_ids, self.right_location_ids = self._parse_input(location_id_pairs)
        self.distance_calculator = distance_calculator
        self.similarity_calculator = similarity_calculator
        
    @staticmethod
    def _parse_input(location_id_pairs: List[List[int]]) -> Tuple[List[int], List[int]]:
        left_location_ids, right_location_ids = zip(*location_id_pairs)
        
        return list(left_location_ids), list(right_location_ids)

    def get_distance_delta(self) -> int:
        return self.distance_calculator.compute(self.left_location_ids, self.right_location_ids)

    def get_similarity_score(self) -> int:
        return self.similarity_calculator.compute(self.left_location_ids, self.right_location_ids)
