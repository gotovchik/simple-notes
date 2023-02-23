from note import Note


class ListOfNotes:
    __notes = []
    __count = 0

    def add_note(self):
        note = Note()
        note.set_name(input("Введите название заметки:"))
        note.set_text(input("Текст заметки:"))
        self.__notes.append(note)
        self.__count += 1
        note.set_id(self.__count)
        return "Заметка успешно добавлена!"

    def delete_note_by_id(self):
        count = 0
        value = int(input("Введите номер заметки:"))
        for note in self.__notes:
            if note.get_id() == value:
                self.__notes.remove(note)
                self.__count -= 1
                count += 1
        if count > 0:
            print("Заметка успешно удалена!")
        print("Заметки с таким номером не найдена.")

    def read_all_notes(self):
        result = f"***Все заметки***\n" \
                 f"Найдено заметок: + {str(len(self.__notes))}\n"
        for note in self.__notes:
            result += f"{str(note.get_id())}|\t"
            result += f"[{str(note.get_date())}]\t"
            result += f"[{str(note.get_name())}]\n"
            result += f"{str(note.get_text())}\n"
        print(result)



