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
