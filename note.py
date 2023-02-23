class Note:
    __name = ""
    __date = ""
    __text = ""

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_text(self):
        return self.__text

    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_text(self, text):
        self.__text = text
