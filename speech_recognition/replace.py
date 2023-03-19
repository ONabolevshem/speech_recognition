#каждая функция открывает txt файл и проверяет наличие ключевых слов, после чего меняет их на знаки и сохраняет файл
def comma():
    with open('file.txt', 'r') as f:
        old_data = f.read()
    new_data = old_data.replace('запятая', ',')
    with open('file.txt', 'w') as f:
        f.write(new_data)


def point():
    with open('file.txt', 'r') as f:
        old_data = f.read()
    new_data = old_data.replace('точка', '.')
    with open('file.txt', 'w') as f:
        f.write(new_data)


def period_comma():
    with open('file.txt', 'r') as f:
        old_data = f.read()
    new_data = old_data.replace('точка запятая', ';')
    with open('file.txt', 'w') as f:
        f.write(new_data)


def colon():
    with open('file.txt', 'r') as f:
        old_data = f.read()
    new_data = old_data.replace('двоеточие', ':')
    with open('file.txt', 'w') as f:
        f.write(new_data)


comma()
point()
period_comma()
colon()
