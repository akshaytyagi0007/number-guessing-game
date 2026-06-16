# 🎯 Number Guessing Game

A fun and interactive command-line game built with Python where the player tries to guess a randomly generated secret number within a limited number of attempts.

---

## 📌 About the Project

This is a beginner-level Python project that demonstrates core programming concepts such as functions, loops, conditionals, error handling, and modern Python syntax like `match-case`. The game supports three difficulty levels, each with a different number range and attempt limit.

---

## 🎮 How to Play

1. Run the program
2. Choose a difficulty level — Easy, Medium, or Hard
3. Enter your guess when prompted
4. The game tells you if your guess is too high or too low
5. Keep guessing until you find the secret number or run out of attempts
6. At the end, choose whether to play again or quit

---

## ⚙️ Difficulty Levels

| Level  | Number Range | Max Attempts |
|--------|-------------|--------------|
| Easy   | 1 to 50     | 12           |
| Medium | 1 to 100    | 10           |
| Hard   | 1 to 500    | 7            |

---

## ✨ Features

- Three difficulty levels with different ranges and attempt limits
- Remaining attempts shown after every guess
- Proper input validation — handles letters, decimals, and out-of-range inputs gracefully
- Game over message reveals the secret number if the player runs out of attempts
- Play again option after every round without restarting the program
- Clean and readable code structure using functions and modern Python syntax

---

## 🛠️ Tech Stack

- **Language** — Python 3.10+
- **Libraries** — `random` (built-in, no installation needed)

---

## 🚀 How to Run

**Step 1 — Make sure Python 3.10 or above is installed**

```bash
python --version
```

**Step 2 — Clone this repository**

```bash
git clone https://github.com/akshaytyagi0007/number-guessing-game.git
```

**Step 3 — Navigate into the project folder**

```bash
cd number-guessing-game
```

**Step 4 — Run the game**

```bash
python number_guessing_game.py
```

---

## 📸 Sample Output

```
Please enter the difficulty
1. Easy
2. Medium
3. Hard
2

Please enter the number: 50
Too low! Guess higher. 9 attempts remaining.

Please enter the number: 75
Too high! Guess lower. 8 attempts remaining.

Please enter the number: 63
🎉 You guessed it in 3 attempts!

Do you want to play again? (yes/no): no
Thanks for playing! Goodbye 👋
```

---

## 📂 Project Structure

```
number-guessing-game/
│
├── number_guessing_game.py   # Main game file
└── README.md                 # Project documentation
```

---

## 💡 Concepts Used

- `random` module for generating secret numbers
- `match-case` statement (Python 3.10+)
- `while/else` loop for detecting game over
- `try/except` for input validation
- Functions to organise and reuse code

---

## 🔮 Future Improvements

- Add warm and cold hints based on how close the guess is
- Add a high score tracker saved to a file
- Add a leaderboard with player names and scores
- Add a timer to track how fast the player guesses
- Build a GUI version using Tkinter

---

## 👨‍💻 Author

**Your Name**
- GitHub — [@akshaytyagi0007](https://github.com/akshaytyagi0007)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).