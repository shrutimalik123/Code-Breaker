# 🔐 Secret Code Breaker - Logic & Deduction Game

A simplified version of the classic "Mastermind" game. The computer generates a secret 3-digit combination, and the player must use logic and process of elimination to crack the code within 10 attempts.

This project focuses on teaching:
* **Input Validation:** Ensuring the user provides exactly what the program needs (3 digits).
* **Positional Comparison:** Using loops to compare two lists at specific index points.
* **List Conversion:** Turning strings into lists to manipulate individual characters.
* **Range-Based Loops:** Using `range()` to iterate a specific number of times.

---

## ✨ Features

* **Randomized Codes:** Every game generates a unique 3-digit combination from 000 to 999.
* **Real-time Feedback:** Tells you exactly how many digits you placed in the correct "slot."
* **Error Handling:** Prevents the loss of an attempt if the player types letters or the wrong amount of numbers.
* **Attempt Tracker:** Keeps the pressure on with a 10-try limit.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed on your system.

### 2. Setup and Execution
1.  **Save the Code:** Save the Python script as `code_breaker.py`.
2.  **Open Terminal:** Navigate to the folder containing the file.
3.  **Run the Script:**
    ```bash
    python code_breaker.py
    ```

### 3. Gameplay Instructions
1.  Think of a 3-digit number (e.g., `123`).
2.  Type your guess and press **Enter**.
3.  **Analyze the feedback:** * If the result is `1`, it means one of your numbers is in the exact right spot.
    * Use your next guess to test which number it was!
4.  Win the game by getting `3` digits in the correct place.

---

## 🧠 Code Structure Highlights

### Comparing Positions
The heart of the game is comparing the `guess_list` to the `secret_code`. We use a loop to check the same index in both lists:



```python
for i in range(3):
    if guess_list[i] == secret_code[i]:
        correct_position += 1

