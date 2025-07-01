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
