from src.item import Item


class MixinLang:
    lang_numb = 1

    def __init__(self):
        self.language = self.language

    def change_lang(self):
        self.lang_numb += 1
        if self.lang_numb % 2 == 0:
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self


class KeyBoard(Item, MixinLang):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.language = 'EN'
