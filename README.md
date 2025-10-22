# Roman Numeral Calculator

This repository contains a simple command-line calculator that performs
basic arithmetic using Roman numerals. It supports addition, subtraction,
multiplication and integer division.

## Usage

```
python roman_calculator.py ROMAN1 OPERATOR ROMAN2
```

Example:

```
python roman_calculator.py X + V
```

This will output `XV`. Division uses integer division, so any remainder is discarded.
If the result is zero or negative, an error message is shown because Roman
numerals do not represent such values.

## Graphical Calculator

A simple GUI application is provided using Tkinter. Launch it with:

```
python roman_calculator_gui.py
```

Use the buttons to enter Roman numerals and choose an operation. The result will be displayed in Roman numerals. The `C` button clears the display.

## Windows Executable

If you want a standalone `.exe` for Windows you can build one using
[PyInstaller](https://pyinstaller.org/). After installing PyInstaller with
`pip install pyinstaller`, run the following command from this directory:

```
pyinstaller --onefile --windowed roman_calculator_gui.py
```

The resulting executable will be placed in the `dist` folder and can be run on
Windows without needing Python installed.
