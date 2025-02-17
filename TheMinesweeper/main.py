import random

class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

class GamePole:
    def __init__(self, N, M):
        self.N = N 
        self.M = M
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]
        self.init()

    def init(self):
        """
            Расстановка мин 
        """
        mines_placed = 0
        while mines_placed < self.M:
            x = random.randint(1, self.N - 1)
            y = random.randint(1, self.N - 1)
            if not self.pole[x][y].mine:
                self.pole[x][y].mine = True
                mines_placed += 1

        """ Подсчет мин в каждой клетке """
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].mine:
                    self.pole[i][j].around_mines = self.count_mines_around(i, j)

    def count_mines_around(self, x, y):
        """
            Подсчёт мин в соседних клетках
        """
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < self.N and 0 <= j < self.N and self.pole[i][j].mine:
                    count += 1
        return count

    #def show(self):
        print("\nТекущее состояние поля:")
        for row in self.pole:
            for cell in row:
                if not cell.fl_open:
                    print("#", end=" ")
                elif cell.mine:
                    print("*", end=" ")
                else:
                    print(cell.around_mines, end=" ")
            print()  

    def open_cell(self, x, y):
        """
            Открытие клетки
        """
        if x < 0 or x >= self.N or y < 0 or y >= self.N:
            return

        cell: Cell = self.pole[x][y]

        if cell.fl_open:
            return

        cell.fl_open = True

        if cell.mine:
            self.show()
            return True

        if cell.around_mines == 0:
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < self.N and 0 <= j < self.N and not self.pole[i][j].fl_open:
                        self.open_cell(i, j)
        if self.check_win():
            self.show()
            return True
        return False

    def check_win(self):
        """
            Проверка на победу
        """
        for row in self.pole:
            for cell in row:
                if not cell.mine and not cell.fl_open:
                    return False
        return True


""" N = 10  
M = 12  
pole_game = GamePole(N, M)
pole_game.show()

while True:
    try:
        x, y = map(int, input("Введите координаты клетки (x y): ").split())
        game_over = pole_game.open_cell(x, y)
        if game_over:
            break
        pole_game.show()
    except ValueError:
        print("Ошибка ввода! Введите два числа через пробел") """

