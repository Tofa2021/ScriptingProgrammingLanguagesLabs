class List:
    def __init__(self):
        self._elements = []
        self._size = 0

    def append(self, element):
        self._elements.append(element)
        self._size += 1

    def insert(self, index, element):
        self._elements.insert(index, element)
        self._size += 1

    def remove(self, element):
        self._elements.remove(element)
        self._size -= 1

    def clear(self):
        self._elements = []
        self._size = 0

    def get(self, index):
        return self._elements[index]

my_list = List()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print(f'Элемент по индексу 3: {my_list.get(3)}')