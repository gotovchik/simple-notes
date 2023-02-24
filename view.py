class View:
    def greeting(self):
        print("Вас приветствует приложение для управления личными заметками!")

    def show_menu(self):
        print("Что вы хотите сделать? Выберите пункт меню:\n" \
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

    def info_note_msg(self, key):
        info = {'add': 'добавлена', 'del': 'удалена', 'edit': 'изменена'}
        print(f"Заметка успешно {info[key]}!")

    def not_found(self):
        print("Такого значения не найдено. Попробуйте еще раз.")

    def input_note_name(self):
        return input("Введите название заметки:")

    def input_note_text(self):
        return input("Текст заметки:")

    def input_number(self, limit, preset):
        presets = {'id': 'заметки', 'menu': 'пункта меню'}
        value = 0
        while True:
            try:
                value = int(input(f"Введите номер {presets[preset]}: "))
            except ValueError:
                self.error()
                continue
            if 0 <= value <= limit:
                break
            else:
                self.not_found()
        return value

    def exit_msg(self):
        print("Всего хорошего!")
