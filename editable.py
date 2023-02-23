from abc import ABC, abstractmethod


class Editable(ABC):

    @abstractmethod
    def add_note(self, note):  # добавить заметку
        pass

    @abstractmethod
    def delete_note_by_id(self, value):  # удалить заметку по идентификатору
        pass

