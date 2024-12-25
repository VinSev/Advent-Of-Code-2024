from abc import ABC, abstractmethod
from typing import Any, List, Type


class FileReader:
    @staticmethod
    def _read(file_path: str,
              transformer: 'FileDataTransformer' = None) -> Any:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()
                return transformer.transform(data)

        except FileNotFoundError as e:
            raise FileNotFoundError(f'File not found: {file_path}') from e

        except Exception as e:
            raise IOError(f'Error reading the file {file_path}: {e}') from e

    @staticmethod
    def read_lines(file_path: str, target_type: Type = str) -> List[Any]:
        transformer = FileDataTransformerToList(target_type)
        return FileReader._read(file_path, transformer)


class FileDataTransformer(ABC):
    @abstractmethod
    def transform(self, data: str) -> Any:
        raise NotImplementedError


class FileDataTransformerToList(FileDataTransformer):
    def __init__(self, target_type: Type = str):
        self._target_type = target_type

    def transform(self, data: str) -> List[Any]:
        return [self._target_type(row.strip()) for row in data.splitlines()]
