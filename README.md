# Difference generator
### Hexlet tests and linter status:
[![Actions Status](https://github.com/Labidahrom/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Labidahrom/python-project-50/actions)
[![Actions Status](https://github.com/Labidahrom/python-project-50/actions/workflows/python-package.yml/badge.svg)](https://github.com/Labidahrom/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d710eb18965ebe6feb22/maintainability)](https://codeclimate.com/github/Labidahrom/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d710eb18965ebe6feb22/test_coverage)](https://codeclimate.com/github/Labidahrom/python-project-50/test_coverage)
## Project description
This utility calculate differences between 2 files in json or yaml format. Differences can be represented by 3 formats:
- stylish format (default). Shows all keys and values ​​from the first and second files, the status of the key is marked with a plus or minus, depending on whether it was added or removed. Nested keys are also displayed, even if they have not been modified in any way
- plain format. Data about keys and their status is displayed as strings. If the key is not modified in any way, the nested keys are displayed as [complex value]
- json format. Difference between two files is shown by json format
## System requirements
- Linux
- Python (3.6 or later)
- PIP
- Poetry
- GIT
## Installation
Open your terminal and type:
```
git clone https://github.com/Labidahrom/python-project-50
cd python-project-50
make package-install
```
## How to use
To run with default stylish view:
```
gendiff file1 file2
```
To run with plain view:
```
gendiff file1 file2 -f plain
```
To run with json view:
```
gendiff file1 file2 -f json
```
## Usage examples
### Get diffrence between two json files by cli command
[![asciicast](https://asciinema.org/a/I5WzbjeyHCh4kIs0PacrSH6xm.svg)](https://asciinema.org/a/I5WzbjeyHCh4kIs0PacrSH6xm)
### Get diffrence between two yaml files by cli command
[![asciicast](https://asciinema.org/a/I5WzbjeyHCh4kIs0PacrSH6xm.svg)](https://asciinema.org/a/I5WzbjeyHCh4kIs0PacrSH6xm)
### Get diffrence between two nested yaml or json files by cli command
[![asciicast](https://asciinema.org/a/SLVVmi8wkspeH5ksw9AdMLjrj.svg)](https://asciinema.org/a/SLVVmi8wkspeH5ksw9AdMLjrj)
### Get diffrence between two nested yaml or json files by cli command with plain format
[![asciicast](https://asciinema.org/a/okoSKhdzH8GVdhJ7LLw5HwIwY.svg)](https://asciinema.org/a/okoSKhdzH8GVdhJ7LLw5HwIwY)
### Get diffrence between two nested yaml or json files by cli command with json format
[![asciicast](https://asciinema.org/a/gb4fmyB5mN5eGQtRBUINI0G8B.svg)](https://asciinema.org/a/gb4fmyB5mN5eGQtRBUINI0G8B)
