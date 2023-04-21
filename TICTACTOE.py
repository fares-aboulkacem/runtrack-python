import tkinter as tk
from tkinter import messagebox

# Variables globales
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "
BOARD_SIZE = 3

# Classe pour la fenêtre principale
class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = PLAYER_X
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.create_widgets()
        
    def create_widgets(self):
        self.buttons = []
        for i in range(BOARD_SIZE):
            row = []
            for j in range(BOARD_SIZE):
                button = tk.Button(self.window, text="", width=10, height=2, font=("Helvetica", 20),
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
        
        restart_button = tk.Button(self.window, text="Restart", width=10, height=2, font=("Helvetica", 20),
                                   command=self.restart_game)
        restart_button.grid(row=BOARD_SIZE, columnspan=BOARD_SIZE, sticky="WE")
        
    def on_button_click(self, row, col):
        if self.board[row][col] == EMPTY:
            self.buttons[row][col].configure(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.quit()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            else:
                self.switch_player()
        
    def switch_player(self):
        if self.current_player == PLAYER_X:
            self.current_player = PLAYER_O
        else:
            self.current_player = PLAYER_X
            
    def check_winner(self):
        for i in range(BOARD_SIZE):
            # Check horizontal
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != EMPTY:
                return True
            # Check vertical
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != EMPTY:
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY:
            return True
        return False
    
    def check_draw(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] == EMPTY:
                    return False
        return True
    
    def restart_game(self):
        self.window.destroy()
        self.__init__()
        self.window.mainloop()

# Création de la fenêtre principale
if __name__ == "__main__":
    game = TicTacToeGUI()
    game.window.mainloop()
