class View:
    def greeting(self):
        print("Вас приветствует приложение для управления личными заметками!")

    def show_menu(self):
        print("Что вы хотите сделать? Выберите пункт меню (введите номер):\n" \
              "\t1. Добавить заметку\n" \
              "\t2. Прочитать заметку\n" \
              "\t3. Прочитать все заметки\n" \
              "\t4. Редактировать заметку\n" \
              "\t5. Сохранить заметки\n" \
              "\t6. Удалить заметку\n" \
              "\t0. Выйти из приложения")

    def error(self):
        print("!!! Введите корректное число")

    def show(self, value):
        print(value)

    def add_note(self, value):
        print(f"Заметка успешно добавлена! Номер заметки {value}")

    def del_note(self):
        print("Заметка успешно удалена!")

    def not_found_note(self):
        print("Заметка с таким номером не найдена.")

    def input_note_name(self):
        return input("Введите название заметки:")

    def input_note_text(self):
        return input("Текст заметки:")

    def input_note_number(self, length):
        value = 0
        while True:
            try:
                value = int(input("Введите номер"))
            except ValueError:
                self.error()
                continue
            if 0 > value <= length:
                break
            else:
                self.not_found_note()
        return value
