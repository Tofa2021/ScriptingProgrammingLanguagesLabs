import string
from typing import override


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self, lang, letters):
        super().__init__("En", string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter in self.letters

    @override
    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "Hello world"