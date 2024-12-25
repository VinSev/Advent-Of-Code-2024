from blink_processor import BlinkProcessor
from file_reader import FileReader


def main() -> None:
    stones = FileReader.read_matrix('data.txt', target_type=int)[0]
    
    blind_processor = BlinkProcessor()
    
    result = blind_processor.process_blinks(stones, blinks=25)
    print(f'Number of Stones after 25 Blinks: {result}')
    
    result = blind_processor.process_blinks(stones, blinks=75)
    print(f'Number of Stones after 75 Blinks: {result}')
    
if __name__ == '__main__':
    main()
