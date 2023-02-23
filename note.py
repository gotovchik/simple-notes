from datetime import datetime


class Note:
    __id = 0
    __name = ""
    __date = ""
    __text = ""

    def __init__(self):
        self.__date = datetime.now()

    def set_id(self, value):
        self.__id = value

    def set_name(self, name):
        self.__name = name

    def set_text(self, text):
        self.__text = text

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_text(self):
        return self.__text
