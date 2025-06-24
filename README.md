# Genetic Algorithm for Vehicle Routing Problem (VRP)

This project uses a genetic algorithm to solve a simple version of the Vehicle Routing Problem (VRP). The goal is to find efficient routes for a small fleet of vehicles to deliver to a set of locations, starting and ending at a central depot.

---

## What is a Genetic Algorithm?

A genetic algorithm is a way to solve hard problems by mimicking how nature works. It starts with a bunch of possible solutions and tries to make them better over time. Each solution is scored, and the best ones are mixed and tweaked to create new solutions. Over many generations, the solutions usually get better, as weaker ones get replaced by stronger ones. This approach is great for problems where there are too many possibilities to check one by one.

---

## Features

- Randomly generates delivery locations on a grid
- Assigns locations to vehicles using a genetic algorithm (with DEAP)
- Tries to keep routes short and balanced between vehicles
- Visualizes the best result as a plot
- Includes basic tests for reliability

---

## How to Run

1. **Install dependencies:**
    ```
    pip install matplotlib deap numpy
    ```
2. **Run the main notebook:**  
   Open `src/main.ipynb` (works great in Google Colab).
3. **To run tests:**
    ```
    python3 tests/test_vrp.py
    ```

---

## Project Structure

- `src/` – Main code and notebook
- `tests/` – Simple test suite
- `notes/` – Project notes and explanations
- `results/` – Plots and outputs
- `data/` – (Optional) Input data

---

## References

- [Wikipedia: Genetic Algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm)
- [DEAP Documentation](https://deap.readthedocs.io/en/master/)
- [Turing: Genetic Algorithm in Python](https://www.turing.com/kb/genetic-algorithm-in-python)
- [GeeksforGeeks: Genetic Algorithms](https://www.geeksforgeeks.org/genetic-algorithms/)
