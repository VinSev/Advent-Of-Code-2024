from file_reader import FileReader
from location_analyzer import LocationAnalyzer
from compute_strategy import DistanceDeltaCalculator, SimilarityScoreCalculator


def main() -> None:
    location_id_pairs = FileReader.read_matrix('data.txt', separator='  ', target_type=int)
    
    distance_strategy = DistanceDeltaCalculator()
    similarity_strategy = SimilarityScoreCalculator()

    location_analyzer = LocationAnalyzer(location_id_pairs, distance_strategy, similarity_strategy)

    distance_delta = location_analyzer.get_distance_delta()
    print(f'Distance Delta: {distance_delta}')
    
    similarity_score = location_analyzer.get_similarity_score()
    print(f'Similarity Score: {similarity_score}')


if __name__ == '__main__':
    main()
