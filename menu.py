from list_of_notes import ListOfNotes


class Menu:
    __notes = ListOfNotes()
    __greeting = "Вас приветствует приложение для управления личными заметками!"
    __text_menu = "Что вы хотите сделать? Выберите пункт меню (введите номер):\n" \
                  "\t1. Добавить заметку\n" \
                  "\t2. Прочитать заметку\n" \
                  "\t3. Прочитать все заметки\n" \
                  "\t4. Редактировать заметку\n" \
                  "\t5. Сохранить заметки\n" \
                  "\t6. Удалить заметку\n" \
                  "\t0. Выйти из приложения"
    __commands = {1: __notes.add_note, 2: __notes.read_all_notes, 3: __notes.read_all_notes,
                  4: __notes.read_all_notes, 5: __notes.read_all_notes, 6: __notes.delete_note_by_id}

    def start(self):
        print(self.__greeting)
        while True:
            print(self.__text_menu)
            try:
                choice = int(input())
            except ValueError:
                print("!!! Введите корректное число")
            else:
                if choice == 0:
                    print("Всего хорошего!")
                    break
                else:
                    self.__commands[choice]()
