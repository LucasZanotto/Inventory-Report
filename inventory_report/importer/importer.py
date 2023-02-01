from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(convert_data):
        raise NotImplementedError
