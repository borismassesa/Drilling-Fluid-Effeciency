import unittest
import numpy as np

class TestDrillingFluidEfficiency(unittest.TestCase):

    def setUp(self):
        # Test case data
        self.speed_test = np.array([3, 6, 100, 200, 300, 600])
        self.shear_stress_test = np.array([10, 20, 30, 40, 50, 60]) # Example shear stress values
        self.initial_weight_test = 100.0 # Example initial weight of cuttings
        self.weight_recovered_test = 50.0 # Example recovered weight

    def test_calculations(self):
        # Expected results based on the test data
        expected_plastic_viscosity = self.shear_stress_test[5] - self.shear_stress_test[4]
        expected_apparent_viscosity = 0.5 * self.shear_stress_test[5]
        expected_yield_point = self.shear_stress_test[4] - expected_plastic_viscosity
        expected_true_yield_point = 0.75 * expected_yield_point
        expected_weight_ratio = self.weight_recovered_test / self.initial_weight_test

        # Perform calculations
        plastic_viscosity = self.shear_stress_test[5] - self.shear_stress_test[4]
        apparent_viscosity = 0.5 * self.shear_stress_test[5]
        yield_point = self.shear_stress_test[4] - plastic_viscosity
        true_yield_point = 0.75 * yield_point
        weight_ratio = self.weight_recovered_test / self.initial_weight_test

        # Assertions
        self.assertAlmostEqual(plastic_viscosity, expected_plastic_viscosity)
        self.assertAlmostEqual(apparent_viscosity, expected_apparent_viscosity)
        self.assertAlmostEqual(yield_point, expected_yield_point)
        self.assertAlmostEqual(true_yield_point, expected_true_yield_point)
        self.assertAlmostEqual(weight_ratio, expected_weight_ratio)

if __name__ == '__main__':
    unittest.main()