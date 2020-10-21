# Tame of Thrones (Geektrust)

The project is my solution of the [Tame of Thrones](https://www.geektrust.in/coding-problem/backend/tame-of-thrones) problem given by Geek Trust.

## Problem Statement

Shan, the gorilla king of the Space kingdom wants to rule all Six Kingdoms in the universe of Southeros.

There is no ruler today and pandemonium reigns. Shan is sending secret messages to all kingdoms to ask for their allegiance. Your coding challenge is to help King Shan send the right message to the right kingdom to win them over. Each kingdom has their own emblem and the secret message should contain the letters of the emblem in it. Once Shan has the support of 3 other kingdoms, he is the ruler!

Input needs to be read from a text file, and output should be printed to console. Your program should execute and take the location to the test file as parameter.

---

# Solution Details

## Requirements

- Python >= v3.8

## Usage

- To run the program :  
  `python -m geektrust <absolute_path_to_input_file>`  
  _Note: Sample Input File included: sample_input.py_
- To build the program (run with tests)"
  `python`

### Additional Details

- The input file is required to be in the following format:  
  `KINGDOM_1 SECRET_MSG_TO_KINGDOM_1 KINGDOM_2 SECRET_MSG_TO_KINGDOM_2 … KINGDOM_N SECRET_MSG_TO_KINGDOM_N`

- The program is built on taking a few assumptions:
  - If multiple messages are sent to a kingdom, even a **Single Accepted Message** would make them ally for our kingdom and all the **Unaccaptable Messages** recieved thereafter would be disregarded.
- The project is designed for extensible use. This is doen by making a Configuration file _(globals\configs.py)_ where all the configuration parameters are added that can be modified according to the requirements of the end-user.
