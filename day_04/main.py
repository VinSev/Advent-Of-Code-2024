from file_reader import FileReader

from grid import Grid
from grid_search_strategy import WordSearchStrategy, CrossPatternSearchStrategy
from word_search import WordSearch


def main() -> None:
    grid_data = FileReader.read_matrix('data.txt', separator='')
    grid = Grid(grid_data)
    
    direction_deltas = [-1, 0, 1]

    target_word = list('XMAS')
    word_search_strategy = WordSearchStrategy(grid, direction_deltas, target_word)
    word_search = WordSearch(word_search_strategy)
    
    total_word_occurrences = word_search.search()
    print(f'Total Occurrences of \'XMAS\': {total_word_occurrences}')


    target_patterns = [list('MAS'), list('SAM')]
    cross_pattern_search_strategy = CrossPatternSearchStrategy(grid, direction_deltas, target_patterns)
    word_search.set_search_strategy(cross_pattern_search_strategy)
    
    total_cross_pattern_occurrences = word_search.search()
    print(f'Total Occurrences of Cross-Shaped MAS: {total_cross_pattern_occurrences}')


if __name__ == '__main__':
    main()
