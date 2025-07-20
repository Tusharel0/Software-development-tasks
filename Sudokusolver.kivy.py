from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class SudokuSolver(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 9
        self.rows = 9
        self.cells = []

        # Create the Sudoku input grid
        for _ in range(81):
            cell = TextInput(multiline=False, halign="center", font_size=24, input_filter='int')
            self.cells.append(cell)
            self.add_widget(cell)

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.cells[i*9 + j].text
                row.append(int(val) if val.isdigit() else 0)
            board.append(row)
        return board

    def set_board(self, board):
        for i in range(9):
            for j in range(9):
                self.cells[i*9 + j].text = str(board[i][j])

    def solve_board(self):
        board = self.get_board()
        if self.solve(board):
            self.set_board(board)

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

class SudokuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.grid = SudokuSolver()
        solve_button = Button(text="Solve", size_hint=(1, 0.1), font_size=20)
        solve_button.bind(on_press=lambda instance: self.grid.solve_board())

        layout.add_widget(self.grid)
        layout.add_widget(solve_button)
        return layout

if __name__ == "__main__":
    SudokuApp().run()
