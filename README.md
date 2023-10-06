# Randomizer and Stress Test

This repository contains the source code and documentation for two parts of the "Clash of UCLan" game development project. Part 1 focuses on generating random full names for in-game non-player characters (NPCs), and Part 2 involves stress testing the game server.

## Part 1 - The Randomizer

### Overview
In this part of the project, we aim to generate a list of 4000 random full names for NPCs in the game "Clash of UCLan" using Python. We'll achieve this by processing input data files containing first names, last names, and NPC locations.

#### Tasks
1. **Trim Data Files**: We'll write a Python program to trim each data file so that they only contain 4000 lines of data. The program will also output the number of lines in each file.

2. **Generate Random Full Names**: We'll randomly select first names and last names from the trimmed data files to create a list of 4000 full names. These full names will be saved into a text file.

3. **Find Longest Full Name**: We'll find the longest full name (the one with the highest number of characters) in the generated list using both recursion and iteration.

#### Learning Outcomes
- Data processing (Learning Outcome 5)
- Random data generation (Learning Outcomes 1, 2, 5)
- Algorithmic analysis (Learning Outcomes 1, 2, 5)

### Deliverables
- `randomizer.py`: Python program for Part 1.
- `generated_names.txt`: Text file containing the output of randomly generated full names.

## Part 2 - Stress Test

### Overview
In this part of the project, we'll run a stress test on the game server to evaluate its performance under a high volume of concurrent gamers. We'll generate lists of integer values (user player IDs) and implement sorting algorithms to measure their efficiency.

#### Tasks
1. **Generate Random Integer Lists**: We'll create three randomly generated arrays of integers with sizes of 10,000, 100,000, and 1,000,000. Each integer will be a 7-digit number.

2. **Implement Sorting Algorithms**: We'll populate the `MasterClass.py` file with sorting algorithms, including QuickSort, Merge Sort, and Selection Sort. We'll also implement a method to compare their time and space complexity.

3. **Measure Sorting Performance**: We'll feed the randomly generated integer arrays into each sorting algorithm, record the time it takes for sorting, and compare the results.

#### Learning Outcomes
- Random data generation (Learning Outcome 5)
- Algorithm implementation (Learning Outcomes 1, 3, 5)
- Performance analysis (Learning Outcomes 1, 2, 5)

### Deliverables
- `stress_test.py`: Python program for Part 2.
- `MasterClass.py`: Python file containing sorting algorithms and complexity analysis.
- `sorted_lists.txt`: Text file containing the three sorted randomly generated lists.

## Getting Started

To run either Part 1 or Part 2 of the project, follow the instructions provided in the respective directories.

## Contributions

Contributions to this project are not expected, as it is part of an individual assignment. However, if you have suggestions or encounter issues, feel free to open an issue in this repository.

## License

This project is provided under the MIT License.
