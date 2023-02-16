# Игра в крестики-нолики для консоли

# Функция для отрисовки игрового поля
def print_board(board):
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))


# Функция для проверки выигрыша
def check_win(board):
    win_conditions = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False


# Игровой цикл
def game_loop():
    board = [' '] * 9  # Создаем пустое поле
    current_player = 'X'  # Задаем начального игрока

    while True:
        # Выводим поле
        print_board(board)
        # Проверяем выигрыш
        if check_win(board):
            print("Игрок победил!")
            return
        # Проверяем ничью
        if all(space != ' ' for space in board):
            print("Ничья!")
            return
        # Ход игрока
        print("Ход игрока {}.".format(current_player))
        while True:
            move = int(input("Введите номер ячейки (1-9): ")) - 1
            if move >= 0 and move < 9 and board[move] == ' ':
                break
            else:
                print("Некорректный ход, попробуйте еще раз.")
        board[move] = current_player
        # Смена игрока
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


# Запуск игры
game_loop()