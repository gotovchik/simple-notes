from note import Note
from editable import Editable


class ListOfNotes(Editable):
    __notes = []

    def __init__(self, notes):
        self.__notes = notes

    def add_note(self, note):
        self.__notes.append(note)
        return "Заметка успешно добавлена!"

    def delete_note_by_id(self, value):
        count = 0
        for note in self.__notes:
            if note.get_id() == value:
                self.__notes.remove(note)
                count += 1
        if count > 0:
            return "Заметка успешно удалена!"
        return "Заметки с таким номером не найдено."

    def read_all_notes(self):
        result = "***Все заметки***\n"
        for note in self.__notes:
            result += note.get_id() + "\t"
            result += "[" + note.get_date() + "]\t"
            result += "[" + note.get_name() + "]\n"
            result += note.get_text() + "\n"
        return result




