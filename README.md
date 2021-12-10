
# BasicCalc

[![CircleCI](https://circleci.com/gh/import-brain/basic_calc/tree/main.svg?style=svg)](https://circleci.com/gh/import-brain/basic_calc/tree/main)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/1cb791a00b3b47ffbe91b104ff320667)](https://www.codacy.com/gh/import-brain/basic_calc/dashboard?utm_source=github.com&utm_medium=referral&utm_content=import-brain/basic_calc&utm_campaign=Badge_Coverage)

## Description

BasicCalc is a small, command-line calculator that performs\\
the standard four mathematical functions and more (remainder,/ circumference of circle given radius, etc.) written using Python3. 🧮\
*See full documentation at basic-calc-docs.vercel.app.*

## Installation

REQUIRES PYTHON VERSION 3.10 OR LATER

Download the latest release on the right of the main repo page, extract it using an unzipping utility (WinRar, 7Zip, unzip command for Linux aficionados, etc.), and scroll down until you find a file named something similar to "calc.exe" for your operating system. This file is the calculator. Enjoy! :)

## CONTRIBUTORS/CONTRIBUTING

Please fork the project, create a new branch in the fork, and PR request changes from the branch you made in your fork to the **main** branch in this repo.

Please follow the established naming conventions present in the code, it makes it easier for all of us to maintain this project.

## TODO

- [x] Add conversion to and from radians/degrees
- [x] Add trigonometric functions (sin, cos, tan, etc.)
- [x] Create new release (use PyInstaller --onefile argument to create less messy rar files)
- [x] Make linux binaries/executables with next release
- [x] Add ability for program to save all calculations done to a file (python read/write)
- [x] Add coverage report functionality
- [ ] Refactor if-else-elif statements to use new "match" statement introduced in Python 3.10
- [ ] Add a safety feature (not just intentionally crashing users) for "match" statements when user is not using Python 3.10 or above (add a legacy component that still        uses if-else-elif statements could be a good route)
- [ ] Improve test coverage (see top of README for Codacy test coverage button)
- [ ] Add ability for program to read from config file for options (e.g. rounding place, save to file, etc.)
- [ ] Possibly in the future: Rebuild app using TKinter / or construct a front end enclosing the current code, given that it can be used in a headless environment
