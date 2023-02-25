import pickle
from note import Note
from view import View


class ListOfNotes:
    __notes = []
    __view = View()
    __count = 0

    def __init__(self):
        try:
            with open('notes.pkl', 'rb') as file:
                self.__notes = pickle.load(file)
                self.__count = len(self.__notes)
        except EOFError:
            self.__notes = []
            self.__view = View()
            self.__count = 0

    def add_note(self):
        note = Note()
        note.set_name(self.__view.input_note_name())
        note.set_text(self.__view.input_note_text())
        note.update_date()
        note.set_id(self.__count)
        self.__notes.append(note)
        self.__count = len(self.__notes)
        self.__view.info_note_msg('add')

    def delete_note(self, note):
        self.__notes.remove(note)
        self.__count = len(self.__notes)
        self.__view.info_note_msg('del')


    def read_all_notes(self):
        self.__view.show_read_all_banner(len(self.__notes))
        for note in self.__notes:
            self.__view.show_note(note)

    def manage_note_by_id(self):
        commands =  {1: self.__view.show_note,
                     2: self.__view.edit_note,
                     3: self.delete_note}
        flag = False
        self.__view.show_manage_note_menu()
        choice = self.__view.input_number(len(commands.keys()), 'menu')
        value = self.__view.input_number(len(self.__notes), 'id')
        for note in self.__notes:
            if note.get_id() == value:
                commands[choice](note)
                flag = True
        if not flag:
            self.__view.not_found()

    def save_notes_to_file(self):
        with open('notes.pkl', 'wb') as file:
            pickle.dump(self.__notes, file, protocol=pickle.HIGHEST_PROTOCOL)




