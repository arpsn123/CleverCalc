# Arp's Calculator

![GitHub Repo Stars](https://img.shields.io/github/stars/arpsn123/CleverCalc?style=social)
![GitHub Forks](https://img.shields.io/github/forks/arpsn123/CleverCalc?style=social)
![GitHub Issues](https://img.shields.io/github/issues/arpsn123/CleverCalc)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/arpsn123/CleverCalc)
![GitHub Last Commit](https://img.shields.io/github/last-commit/arpsn123/CleverCalc)
![GitHub Contributors](https://img.shields.io/github/contributors/arpsn123/CleverCalc)
![GitHub License](https://img.shields.io/github/license/arpsn123/CleverCalc)
![GitHub Repo Size](https://img.shields.io/github/repo-size/arpsn123/CleverCalc)
![GitHub Language Count](https://img.shields.io/github/languages/count/arpsn123/CleverCalc)
![GitHub Top Language](https://img.shields.io/github/languages/top/arpsn123/CleverCalc)
![GitHub Watchers](https://img.shields.io/github/watchers/arpsn123/CleverCalc?style=social)
![Commit Activity](https://img.shields.io/github/commit-activity/m/arpsn123/CleverCalc)
![Maintenance Status](https://img.shields.io/badge/Maintained-Yes-green)


## Overview

Arp's Calculator is a simple graphical user interface (GUI) calculator built using Python's Tkinter library. This calculator can perform basic arithmetic operations including addition, subtraction, multiplication, and division. It also handles invalid input gracefully, providing user-friendly error messages.

## Features

- Basic arithmetic operations: Addition, Subtraction, Multiplication, Division
- Clear entry functionality
- User-friendly interface with error handling

## Technology Stack
![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-8.6-green.svg)
- **Programming Language**: Python
- **GUI Framework**: Tkinter

## Theory

This calculator leverages the Tkinter library to create a windowed application. It uses `StringVar` to manage the display of input and results in the entry field. The calculator evaluates user input using Python's built-in `eval()` function, which allows for dynamic evaluation of mathematical expressions entered by the user.

### Event Handling

The calculator uses event binding to handle button clicks. Each button is linked to a callback function (`clickme`) that processes the user's input:

- If the user clicks `=`, the input is evaluated, and the result is displayed.
- If the user clicks `C`, the input is cleared.
- Any other button click appends the corresponding value to the input string.

### Error Handling

The application includes error handling for invalid expressions using `try` and `except`, displaying a message box with an appropriate error message if the evaluation fails.

## Installation

To run the calculator, ensure you have Python installed on your system. Follow these steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Required Packages**:
   Ensure you have the Tkinter library installed. It is typically included with Python installations. If you encounter issues, you may need to install the `tk` package depending on your operating system.

3. **Run the Application**:
   Open a terminal, navigate to the directory where the calculator script is located, and run:
   ```bash
   python calculator.py
   ```

## Usage

Once the application is running, you will see a simple interface. Use the buttons to perform calculations:

- Click numbers and operators to enter an expression.
- Press `=` to calculate the result.
- Press `C` to clear the current input.

## License

This project is licensed under the MIT License. Feel free to modify and distribute it as needed.
