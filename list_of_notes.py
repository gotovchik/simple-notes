from note import Note
from view import View


class ListOfNotes:
    __notes = []
    __count = 0
    __view = View()

    def add_note(self):
        note = Note()
        note.set_name(self.__view.input_note_name())
        note.set_text(self.__view.input_note_text())
        self.__notes.append(note)
        self.__count += 1
        note.set_id(self.__count)
        self.__view.add_note(self.__count)

    def delete_note_by_id(self):
        count = 0
        value = self.__view.input_note_number()
        for note in self.__notes:
            if note.get_id() == value:
                self.__notes.remove(note)
                self.__count -= 1
                count += 1
        if count > 0:
            self.__view.del_note()
        else:
            self.__view.not_found_note()

    def read_all_notes(self):
        result = f"***Все заметки***\n" \
                 f"Найдено заметок: + {str(len(self.__notes))}\n"
        for note in self.__notes:
            result += f"{str(note.get_id())}|\t"
            result += f"[{str(note.get_date())}]\t"
            result += f"[{str(note.get_name())}]\n"
            result += f"{str(note.get_text())}\n"
        self.__view.show(result)



