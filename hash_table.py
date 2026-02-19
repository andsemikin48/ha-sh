class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get_food(self, key): #Тут должна быть функция поиска search, но в данном примере мне больше нравится get
        index = self.hash_function(key)
        if self.table[index] is None:
            return f"{None} Кот {key} - не найден" #None
        for pair in self.table[index]:
            if pair[0] == key:
                return f"Еда для {key} - {pair[1]}"
                #или return pair
                #или return pair[1]
        return f"{None} Кот найден, но это не {key}" #None

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                res = self.table[index].pop(i)
                return f"Кот {res[0]} - удален"
                #return True
        return False

    def resize(self):
        self.table.extend([None] * self.size)
        self.size *= 2

    def size(self):
        return len(self.table)

def aspi_hash(string_):
    #конкатенация ASCII значений в виде строки
    result = ''
    for i in string_:
        result += str(ord(i))
    return result

def aspi_hash_sum(string_):
    #сумма ASCII значений, более короткий резутат
    result = 0
    for i in string_:
        result += ord(i)
    return result


table = HashTable(10)
print(table.size)
table.insert('Филя', 'Вискас')
table.insert('Мурка', 'Рыба')
table.insert('Симон', 'Китикет')
print(table.get_food('Филя'))
print(table.get_food('Пушок'))
print(table.size)
print(table.table)
table.resize()
print(table.size)
print(table.table)
print(table.delete('Симон'))
print(table.table)

print(aspi_hash('Филя'))
print(aspi_hash('Симон'))
print(aspi_hash_sum('Симон'))
print(aspi_hash_sum('Мурка'))
print(aspi_hash_sum('Кот'))
print(aspi_hash_sum('Ток')) #Коллизия буквы одинаковые, и сумма будет одинаковая
print(aspi_hash('Кот'))
print(aspi_hash('Ток')) #Тут хеш будет различаться, так как индексы букв разные