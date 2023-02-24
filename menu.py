from list_of_notes import ListOfNotes
from view import View


class Menu:
    __view = View()
    __notes = ListOfNotes()
    __commands = {1: __notes.add_note, 2: __notes.read_note_by_id, 3: __notes.read_all_notes,
                  4: __notes.edit_note, 5: __notes.save_notes_to_file, 6: __notes.delete_note_by_id}

    def start(self):
        self.__view.greeting()
        while(True):
            self.__view.show_menu()
            choice = self.__view.input_number(len(self.__commands.keys()), 'menu')
            if choice == 0:
                self.__view.exit_msg()
                break
            else:
                self.__commands[choice]()
