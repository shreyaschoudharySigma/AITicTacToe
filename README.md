# 🎮 Unbeatable Tic-Tac-Toe AI

A classic Tic-Tac-Toe game built in Python that runs in the command line (CLI). The highlight of this project is a **Smart AI** opponent that uses a priority-based decision engine to play near-perfectly against human players.

## 🚀 Features

- **Smart AI Logic:** The computer doesn't just play randomly. It actively tries to win and blocks your winning moves.
- **Robust Input Handling:** The game won't crash if you enter invalid numbers or text.
- **Clean Interface:** clear visual representation of the board in the terminal.
- **Tuple-Based Coordinates:** Uses efficient coordinate mapping `(row, col)` for game logic.

## 🧠 How the AI Works

The AI (`tryAI` function) follows a strict hierarchy of decisions to determine the best move:

1.  **Attack (Win):** First, it checks if it has 2 'O's in a row. If yes, it takes the third spot to win immediately.
2.  **Defense (Block):** If it can't win, it checks if the player ('X') has 2 marks in a row. It immediately blocks that spot to prevent a loss.
3.  **Strategic Center:** If the center spot (5) is open, it takes it (statistically the best position).
4.  **Corner Control:** If the center is taken, it prioritizes empty corners.
5.  **Random Fallback:** If no strategic moves are left, it picks a random empty spot.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Modules:** `random` (for non-critical moves)
- **Tools:** Developed using Pydroid 3 (Android) / Python IDLE.

## 💻 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/shreyaschoudharySigma/AITicTacToe.git](https://github.com/shreyaschoudharySigma/AITicTacToe.git)
    ```
2.  **Navigate to the directory:**
    ```bash
    cd tictactoe-ai
    ```
3.  **Run the game:**
    ```bash
    python AITicTacToe.py
    ```
4.  Follow the on-screen prompt and enter a number from **1 to 9** to place your X.

## 🔮 Future Improvements - Add a GUI using Tkinter or Pygame.

## 👤 Author

**Shreyas Choudhary**
*Class 9 | Jyoti Niketan School, Azamgarh*
- Passionate about Python, Java, and AI logic.

---
*Created with ❤️ and Python.*
