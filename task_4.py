def aspi_hash(string_):
    #конкатенация ASCII значений в виде строки
    result = ''
    for i in string_:
        result += str(ord(i))
    return {string_: result}

def search_by_key(dict_, key):
    if key in dict_:
        return dict_[key]
    else:
        return 'Ключ не найден'

def add_to_dict(dict_, key):
    if key in dict_:
        return 'Ключ уже существует'
    else:
        return dict_.update(aspi_hash(key))

value_dict = ['Мурка', 'Барсик', 'Мурзик', 'Филя', 'Симон', 'Пушок','Кот', 'Ток']
dict_hash = {}
for value in value_dict:
    dict_hash.update(aspi_hash(value))

print(dict_hash)
print(search_by_key(dict_hash, 'Мурзик'))
print(search_by_key(dict_hash, 'Кат'))
add_to_dict(dict_hash, 'Чип')
print(list(dict_hash.items())[-1]) #Проверяем что Чип добавился и просчитал хеш-сумму

