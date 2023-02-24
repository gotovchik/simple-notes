from note import Note
from view import View


class ListOfNotes:
    __notes = []
    __view = View()
    __maxid = 10

    def add_note(self):
        note = Note()
        note.set_name(self.__view.input_note_name())
        note.set_text(self.__view.input_note_text())
        self.__notes.append(note)
        note.set_id(len(self.__notes))
        self.__view.info_note_msg('add')

    def delete_note(self, note):
        self.__notes.remove(note)
        self.__view.info_note_msg('del')


    def read_all_notes(self):
        result = f"\t***Все заметки***\n" \
                 f"Найдено заметок: {str(len(self.__notes))}\n"
        for note in self.__notes:
            self.__view.show_note(note)

    def manage_note_by_id(self):
        commands =  {1: self.__view.show_note,
                     2: self.delete_note,
                     3: self.__view.edit_note }
        flag = False
        self.__view.show_manage_note_menu()
        choice = self.__view.input_number(len(commands.keys()), 'menu')
        value = self.__view.input_number(self.__maxid, 'id')
        for note in self.__notes:
            if note.get_id() == value:
                commands[choice](note)
                flag = True
        if not flag:
            self.__view.not_found()

    def save_notes_to_file(self):
        pass






