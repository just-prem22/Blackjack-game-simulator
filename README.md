# Blackjack-game-simulator

# 🃏 Blackjack Game in Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Project Type](https://img.shields.io/badge/Project-Console%20Game-green)
![Level](https://img.shields.io/badge/Level-Beginner-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A console-based implementation of the classic **Blackjack** card game developed using Python.  
This project simulates a simplified version of Blackjack where a player competes against the computer using rule-based logic and random card generation.

The goal of this project is to strengthen core programming concepts such as functions, loops, condition handling, and logical flow design through a real-world mini project.

---

## 📌 Project Description

Blackjack is one of the most popular casino card games. The objective is to reach a score as close to **21** as possible without exceeding it.

In this implementation:
- Cards are generated randomly using Python’s built-in `random` module.
- The player competes against a computer opponent.
- The computer follows automated Blackjack rules.
- The entire game runs in the terminal using interactive input.

This project focuses on **logic building and structured programming** rather than graphical interface design.

---

## 🎯 Project Objectives

- Practice Python fundamentals  
- Understand modular programming using functions  
- Implement real-world game logic  
- Improve problem-solving skills  
- Learn how to structure a small software project  

---

## ⚙️ Game Rules (Simplified Version)

- Number cards (2–10) count as their face value  
- Face cards (Jack, Queen, King) count as **10**  
- Ace counts as **11** or **1** depending on the total score  
- Blackjack occurs when the first two cards equal **21**  
- If a player's score exceeds **21**, they lose  
- The computer draws cards until its score becomes **17 or higher**

---

## 🧠 Concepts Used

- Functions and modular design  
- Conditional statements (`if-else`)  
- Loops (`while`, `for`)  
- Lists and list operations  
- Random module usage  
- User input handling  
- Logical game flow implementation  

---

## 🏗️ Program Structure

### `deal_card()`
Returns a random card.

### `calculate_score(cards)`
Calculates total score and adjusts Ace value when necessary.

### `compare(user_score, computer_score)`
Determines the final game result.

### `play_game()`
Controls the main gameplay logic.

### `main()`
Allows replay functionality.



---

## ▶️ How to Run the Project

### 1. Install Python

### 2. Clone Repository

### 3. Run Program

---


## 🎮 Example Gameplay

Your cards: [10, 7] | Current score: 17
Computer's first card: 9

Type 'y' to get another card, type 'n' to pass: n

----- Final Result -----



Your final hand: [10, 7] | Final score: 17
Computer final hand: [9, 8] | Final score: 17
It's a Draw.

<p align="center">
  <img src="assets/blackjack1.png" width="600">
</p>

<p align="center">
  <img src="assets/blackjack2.png" width="600">
</p>

