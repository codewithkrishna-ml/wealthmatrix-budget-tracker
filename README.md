# WealthMatrix - Personal Finance & Budget Tracker 💰📊

WealthMatrix is a smart, fully object-oriented console application built in Python to help users manage their personal finances. The system handles income logging, balance updates, and dynamic expense tracking with real-time insufficient balance validation using strict class relationships.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Dynamic Wallet / Income Management:** Allows users to easily add income to their profile, instantly converting inputs into floating-point metrics with strict `> 0` value checks.
*   **Smart Overdraft / Expense Validation:** Prevents users from overspending by automatically blocking expense tracking entries if the transaction amount exceeds the current available profile balance.
*   **Categorized Expense Logs:** Tracks individual expense details including explicit transaction values, specific spending categories (e.g., Food, Travel), custom descriptions, and transaction dates.
*   **Comprehensive Financial History Dashboard:** Features a clean log layout displaying all past spending entries side by side, alongside a quick profile overview widget.

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This codebase focuses on modularity, clean interactions, and data isolation:
*   **Classes & Blueprints:** Structured cleanly around three distinct entities: `User` (profile and balance host), `Expense` (individual transaction node), and `BudgetManager` (controller engine).
*   **Composition / Object Aggregation:** Illustrates high-quality structural design where the `BudgetManager` class takes a live `User` object reference directly inside its constructor (`__init__`) to alter user balances and append internal lists safely.
*   **Data Integrity & Casting:** Ensures mathematical precision by converting raw inputs directly into floats, making sure that financial metrics do not mismatch during subtraction or addition operations.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd wealthmatrix-budget-tracker
    ```
3.  **Run the interactive finance menu:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   Python 3.x installed on your machine.
