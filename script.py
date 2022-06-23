def show(field):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i), *field[i])

def interview(field):
    while 1==1:
        coordinat = list(map(int, input('Введите две координаты через пробел:').split()))
        if len(coordinat) != 2:
            print('Вы неправильно ввели! Должно быть две координаты!!!')
            continue
        x, y = coordinat[0], coordinat[1]
        if not(0<=x<=2 and 0<=y<=2):
            print('Вы неправильно ввели! Обе координаты должны входить в диапазон от 0 до 3')
            continue
        if field[x][y] != '-':
            print('Текущие координаты заняты. Выберите другие')
            continue
        break
    return x,y

def victory(field, label):
    def win_line(a, b, c, label):
        if a == label and b == label and c == label:
            return True
    for i in range(3):
        horizontal_win = win_line(field[i][0], field[i][1], field[i][2], label)
        vertical_win = win_line(field[0][i], field[1][i], field[2][i], label)
        diagonal_win = win_line(field[0][0], field[1][1], field[2][2], label) or win_line(field[2][0], field[1][1], field[0][2], label)
        if horizontal_win or vertical_win or diagonal_win:
            return True
    return False

field = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

stroke_counter = 1
while 1==1:
    if stroke_counter == 9:
        print('Между игроками ничья!')
        break
    if not(stroke_counter % 2 == 0):
        label = 'x'
    else:
        label = '0'
    show(field)
    x,y = interview(field)
    field[x][y] = label
    if victory(field, label):
        print('Ура! Это был победный ход - победа Ваша!')
        break
    stroke_counter += 1










