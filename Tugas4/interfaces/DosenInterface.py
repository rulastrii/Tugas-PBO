from abc import ABC, abstractmethod

class DosenInterface(ABC):
    @abstractmethod
    def all():
        pass

    @abstractmethod
    def store(dosen_obj):
        pass

    @abstractmethod
    def find(dosen_id):
        pass

    @abstractmethod
    def update(dosen_id, dosen_obj):
        pass

    @abstractmethod
    def delete(dosen_id):
        pass
