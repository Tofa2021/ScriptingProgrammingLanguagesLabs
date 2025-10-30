from datetime import datetime

class LibraryBook:
    genres = ['Fiction', 'Non-fiction', 'Mystery', 'Science', 'Biography']

    def __init__(self, title, author, year, genre, is_checked_out=False):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_checked_out = is_checked_out

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f'Книга "{self.title}" взята')
        else:
            print(f'Книга "{self.title}" уже взята')

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f'Книга "{self.title}" возвращена')
        else:
            print(f'Книга "{self.title}" не была взята')

    def get_info(self):
        status = 'в наличии' if not self.is_checked_out else 'выдана'
        return f'"{self.title}" ({self.year}), {self.author}, жанр: {self.genre}, статус: {status}'

    @classmethod
    def get_genres(cls):
        return cls.genres

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title=data_dict['title'],
            author=data_dict['author'],
            year=data_dict['year'],
            genre=data_dict['genre'],
            is_checked_out=data_dict.get('is_checked_out', False)
        )

    @staticmethod
    def is_classic(year):
        current_year = datetime.now().year
        return current_year - year >= 50


# Пример использования
book = LibraryBook("Война и мир", "Лев Толстой", 1869, "Fiction")
print(book.get_info())
book.check_out()
print(f"Классика ли? {LibraryBook.is_classic(book.year)}")
book.return_book()
print(LibraryBook.get_genres())
