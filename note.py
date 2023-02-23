from datetime import datetime

class Note:
    __id = 0
    __name = ""
    __date = ""
    __text = ""

    def __init__(self, name, text):
        self.__date = datetime.now()
        self.__name = name
        self.__text = text
        self.id += 1

    def get_id(self):
        return self.id

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_text(self):
        return self.__text


