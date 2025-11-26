from datetime import datetime

class LibraryBook:
    def __init__(self, title, author, year, genre, is_taken=False):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_taken = is_taken

    def is_taken(self):
        return self.is_taken

    def take_book(self):
        if not self.is_taken:
            self.is_taken = True
            print(f'Книга "{self.title}" взята')
        else:
            print(f'Книга "{self.title}" уже взята')

    def return_book(self):
        if self.is_taken:
            self.is_taken = False
            print(f'Книга "{self.title}" возвращена')
        else:
            print(f'Книга "{self.title}" не была взята')

    def get_info(self):
        if self.is_taken:
            status = 'выдана'
        else:
            status = 'в наличии'
        return f'"{self.title}" ({self.year}), {self.author}, жанр: {self.genre}, статус: {status}'

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title=data_dict['title'],
            author=data_dict['author'],
            year=data_dict['year'],
            genre=data_dict['genre'],
            is_taken=data_dict.get('is_taken', False)
        )

    @staticmethod
    def is_classic(year):
        current_year = datetime.now().year
        return current_year - year >= 50

book = LibraryBook("Война и мир", "Лев Толстой", 1869, "Роман-эпопея")
print(book.get_info())
print(f"Классика ли? {LibraryBook.is_classic(book.year)}")
book.return_book()