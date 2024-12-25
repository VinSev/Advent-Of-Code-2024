from file_reader import FileDataTransformerToMatrix
from page_update_sorter import SimplePageUpdateSorter
from page_update_processor import OrderedPageUpdateProcessor, UnorderedPageUpdateProcessor
from safety_manual import SafetyManual

    
def main() -> None:
    with open('data.txt', 'r') as file:
        content = file.read().split('\n\n')
    
    page_ordering_rules = FileDataTransformerToMatrix(target_type=int, separator='|').transform(content[0])
    page_updates = FileDataTransformerToMatrix(target_type=int, separator=',').transform(content[1])

    page_update_processor = OrderedPageUpdateProcessor()
    safety_manual = SafetyManual(page_updates, page_ordering_rules, page_update_processor)
    ordered_sum = safety_manual.sum_of_middle_page_updates()
    print(f'Sum of middle page numbers from ordered page updates: {ordered_sum}')
    
    page_update_sorter = SimplePageUpdateSorter()
    page_update_processor = UnorderedPageUpdateProcessor(page_update_sorter)
    safety_manual.set_page_update_processor(page_update_processor)
    unordered_sum = safety_manual.sum_of_middle_page_updates()
    print(f'Sum of middle page numbers from unordered page updates: {unordered_sum}')


if __name__ == '__main__':
    main()
