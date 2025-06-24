# Project: Genetic Algorithm for Vehicle Routing Problem (VRP)

## Project Structure

- **README.md**: Overview and instructions.
- **data/**: Input data and data README.
- **results/**: Outputs, plots, and results.
- **src/**: Source code and notebooks.
- **tests/**: Unit tests for code.
- **notes/**: All project notes and theoretical explanations.

## Initial Setup

- Created a GitHub repository for version control and collaboration.
- Organized folders for code, data, results, tests, and notes.
- Set up the project in Google Colab for interactive development and easy cloud execution.

## Next Steps

- Install dependencies and set up the genetic algorithm code.

### Installing Dependencies

- The main Python packages used in this project are: matplotlib (for plotting), deap (for genetic algorithms), and numpy (for numerical operations).
- These dependencies are listed in src/requirements.txt for easy project setup and reproducibility.

### Problem Parameters and Data Generation

- The Vehicle Routing Problem (VRP) is set up with 10 delivery locations and 3 vehicles.
- Each location is represented by random (x, y) coordinates within a 100x100 grid.
- The depot, where all vehicles start and end their routes, is fixed at the center point (50, 50).
- This setup provides a simple, random test environment for the genetic algorithm to solve.

Primary sources:  
- https://en.wikipedia.org/wiki/Genetic_algorithm  
- https://www.turing.com/kb/genetic-algorithm-in-python  
- https://www.geeksforgeeks.org/genetic-algorithms/

---

### What is a Genetic Algorithm?

A genetic algorithm is a way to solve tough problems by mimicking how nature works. It starts with a bunch of possible solutions (called a population) and tries to make them better over time.

Each solution (sometimes called an individual or chromosome) is given a score by a fitness function, which tells how good that solution is. The best solutions are picked to be parents, and new solutions are made by combining parts of two parents (crossover) or making small random changes (mutation).

This process goes on for many generations. Over time, the solutions usually get better, because the weaker ones get replaced by stronger ones. The algorithm stops when it finds a good enough answer or after a set number of generations.

**How it works, step by step:**
1. Start with a random group of solutions.
2. Score each solution.
3. Pick the better ones to be parents.
4. Mix and tweak them to make new solutions.
5. Replace the old group with the new one.
6. Repeat until you’re happy with the answer.

Genetic algorithms are great for problems where there are too many possibilities to check one by one, or when the problem is just too complicated for regular methods.

### Genetic Algorithm Structure

- Used the DEAP library to set up the main parts of the genetic algorithm:
    - Defined a fitness function that tries to minimize both the total distance traveled and how balanced the routes are between vehicles.
    - Each solution (individual) is a shuffled list of location indices, representing a possible way to assign locations to vehicles.
    - Registered functions for creating individuals, populations, and genetic operators (crossover, mutation, selection).
- This structure allows the algorithm to generate, evaluate, and evolve solutions for the VRP.

### Running the Genetic Algorithm and Visualizing Results

The genetic algorithm runs for 300 generations, starting with a big group of possible solutions. Over time, the solutions improve as the algorithm keeps mixing and tweaking them. The best solution found is shown on a plot, where each vehicle’s route is drawn in a different color. This makes it easy to see how the locations are divided up and how balanced the routes are.
