def custom_write(file_name, strings):
    n = 0
    strings_positions = {}
    file_name ='test.txt'
    file = open(file_name,'w', encoding='utf-8')
    for string in strings:
        tell = file.tell()
        n += 1
        file.write(string + '\n')
        strings_positions.update({(n, tell): string})
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)