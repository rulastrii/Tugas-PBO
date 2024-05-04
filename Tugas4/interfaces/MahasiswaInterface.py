# interfaces/MahasiswaInterface.py
from abc import ABC, abstractmethod

class MahasiswaInterface(ABC):
    @abstractmethod
    def all():
        pass

    @abstractmethod
    def store(mahasiswa_obj):
        pass

    @abstractmethod
    def find(mahasiswa_id):
        pass

    @abstractmethod
    def update(mahasiswa_id, mahasiswa_obj):
        pass

    @abstractmethod
    def delete(mahasiswa_id):
        pass