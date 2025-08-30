import tkinter as tk
from tkinter import messagebox
import chess
import chess.engine
from PIL import Image, ImageTk
import threading

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.board = chess.Board()
        self.square_size = 60
        self.canvas = tk.Canvas(root,
                                width=8*self.square_size,
                                height=8*self.square_size)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.selected = None
        self.images = {}
        self.load_images()
        self.draw_board()
        self.draw_pieces()
        self.engine = chess.engine.SimpleEngine.popen_uci("stockfish")  # or path to engine

    def load_images(self):
     pieces = ['r', 'n', 'b', 'q', 'k', 'p']
     colors = ['w', 'b']
     for color in colors:
        for piece in pieces:
            key = color + piece
            img_path = f"images/{key}.png"
            try:
                img = Image.open(img_path)
                img = img.resize((60, 60), Image.Resampling.LANCZOS)
                self.images[key] = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"❌ Failed to load {img_path}: {e}")
    def draw_board(self):
        self.canvas.delete("square")
        color1, color2 = "#F0D9B5", "#B58863"
        for r in range(8):
            for c in range(8):
                color = color1 if (r+c)%2==0 else color2
                self.canvas.create_rectangle(c*self.square_size,
                                             r*self.square_size,
                                             (c+1)*self.square_size,
                                             (r+1)*self.square_size,
                                             fill=color, tags="square")

    def draw_pieces(self):
        self.canvas.delete("piece")
        for square, piece in self.board.piece_map().items():
            r = 7 - (square // 8)
            c = square % 8
            key = ('w' if piece.color else 'b') + piece.symbol().lower()
            self.canvas.create_image(c*self.square_size + self.square_size/2,
                                     r*self.square_size + self.square_size/2,
                                     image=self.images[key], tags="piece")

    def on_click(self, event):
        c = event.x // self.square_size
        r = 7 - (event.y // self.square_size)
        sq = chess.square(c, r)
        if self.selected is None:
            piece = self.board.piece_at(sq)
            if piece and piece.color == self.board.turn:
                self.selected = sq
        else:
            move = chess.Move(self.selected, sq)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.selected = None
                self.draw_pieces()
                if self.board.is_game_over():
                    messagebox.showinfo("Game Over", str(self.board.result()))
                else:
                    threading.Thread(target=self.ai_move).start()
            else:
                self.selected = None

    def ai_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(depth=2))
        self.board.push(result.move)
        self.root.after(100, self.draw_pieces)
        if self.board.is_game_over():
            messagebox.showinfo("Game Over", str(self.board.result()))

    def close(self):
        self.engine.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()
