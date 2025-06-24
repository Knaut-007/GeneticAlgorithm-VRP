import unittest
import random
import numpy as np

# Dummy data for testing
num_locations = 5
num_vehicles = 2
locations = [(10, 10), (20, 20), (30, 30), (40, 40), (50, 50)]
depot = (0, 0)

def evalVRP(individual):
    total_distance = 0
    distances = []
    for i in range(num_vehicles):
        vehicle_route = [depot] + [locations[individual[j]] for j in range(i, len(individual), num_vehicles)] + [depot]
        vehicle_distance = sum(np.linalg.norm(np.array(vehicle_route[k+1]) - np.array(vehicle_route[k])) for k in range(len(vehicle_route)-1))
        total_distance += vehicle_distance
        distances.append(vehicle_distance)
    balance_penalty = np.std(distances)
    return total_distance, balance_penalty

class TestVRP(unittest.TestCase):
    def test_evalVRP_returns_tuple(self):
        # Individual is a permutation of location indices
        individual = [0, 1, 2, 3, 4]
        result = evalVRP(individual)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_evalVRP_non_negative(self):
        individual = [4, 3, 2, 1, 0]
        total_distance, balance_penalty = evalVRP(individual)
        self.assertGreaterEqual(total_distance, 0)
        self.assertGreaterEqual(balance_penalty, 0)

if __name__ == '__main__':
    unittest.main()
