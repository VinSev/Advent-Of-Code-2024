from typing import Any, Callable, List, Type


class FileReader:    
    @staticmethod
    def _read_helper(file_path: str, transformer: Callable = None) -> Any:
        try:
            with open(file_path, 'r') as file:
                if transformer:
                    return [transformer(line) for line in file]
                else:
                    return file.read()
                
        except FileNotFoundError:
            raise FileNotFoundError(f'File not found: {file_path}')
        
        except Exception as e:
            raise IOError(f'Error reading the file {file_path}: {e}')

    @staticmethod
    def read_file(file_path: str, target_type: Type = str) -> Any:
        content = FileReader._read_helper(file_path)
        return target_type(content)

    @staticmethod
    def read_lines(file_path: str, target_type: Type = str) -> List[Any]:
        return FileReader._read_helper(
            file_path, 
            transformer=lambda line: 
                target_type(line.strip())
        )

    @staticmethod
    def read_matrix(file_path: str, separator: str = ' ', target_type: Type = str) -> List[List[Any]]:
        return FileReader._read_helper(
            file_path, 
            transformer=lambda line: 
                [target_type(value) for value in line.split(separator)]
        )
