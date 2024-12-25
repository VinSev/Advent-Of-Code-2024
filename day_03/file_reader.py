from abc import ABC, abstractmethod
from typing import Any, List, Type


class FileReader:
    @staticmethod
    def _read(
        file_path: str, 
        transformer: 'FileDataTransformer' = None
    ) -> Any:
        try:
            with open(file_path, 'r') as file:
                data = file.read()
                return transformer.transform(data)

        except FileNotFoundError:
            raise FileNotFoundError(f'File not found: {file_path}')
        
        except Exception as e:
            raise IOError(f'Error reading the file {file_path}: {e}')

    @staticmethod
    def read_file(file_path: str, target_type: Type = str) -> Any:
        transformer = FileDataTransformerToType(target_type)
        return FileReader._read(file_path, transformer)

    @staticmethod
    def read_lines(file_path: str, target_type: Type = str) -> List[Any]:
        transformer = FileDataTransformerToList(target_type)
        return FileReader._read(file_path, transformer)

    @staticmethod
    def read_matrix(
        file_path: str, 
        target_type: Type = str, 
        separator: str = ' '
    ) -> List[List[Any]]:
        transformer = FileDataTransformerToMatrix(target_type, separator)
        return FileReader._read(file_path, transformer)


class FileDataTransformer(ABC):
    @abstractmethod
    def transform(self, data: str) -> Any:
        raise NotImplementedError


class FileDataTransformerToType(FileDataTransformer):
    def __init__(self, target_type: Type = str):
        self._target_type = target_type
        
    def transform(self, data: str) -> Any:
        return self._target_type(data)


class FileDataTransformerToList(FileDataTransformer):
    def __init__(self, target_type: Type = str):
        self._target_type = target_type

    def transform(self, data: str) -> List[Any]:
        return [self._target_type(row.strip()) for row in data.splitlines()]


class FileDataTransformerToMatrix(FileDataTransformer):
    def __init__(
        self, target_type: Type = str, 
        separator: str = ' '
    ) -> None:
        self._target_type = target_type
        self._separator = separator

    def transform(self, data: str) -> List[List[Any]]:
        return [
            [self._target_type(value) for value in row.split(self._separator)] 
            for row in data.splitlines()
        ]

