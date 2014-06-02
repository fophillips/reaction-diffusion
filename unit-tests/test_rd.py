from nose.tools import *
import numpy as np

from rd import RD

class TestRD:
    def setup(self):
        self.init_conc = np.array([0, 0, 0, 0, 0])
        self.reaction = np.array([0, 0, 1, 0, 0])
        self.diff = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
        self.dt = 0.5
        self.dx = 1

    def test_one_timestep(self):
        expected = np.array([0, 0, 0.5, 0, 0])
        actual = RD.integrate(1, self.init_conc, self.reaction, self.diff, self.dt, self.dx)
        self.check_arrays(expected, actual)
        
    def test_two_timesteps(self):
        expected = np.array([0, 0.025, 0.95, 0.025, 0])
        actual = RD.integrate(2, self.init_conc, self.reaction, self.diff, self.dt, self.dx)
        self.check_arrays(expected, actual)

    def test_three_timesteps(self):
        expected = np.array([0.00125, 0.07, 1.3575, 0.07, 0])
        actual = RD.integrate(3, self.init_conc, self.reaction, self.diff, self.dt, self.dx)
        self.check_arrays(expected, actual)

    def check_arrays(self, expected, actual):
        print("Expected:",expected)
        print("Actual:",actual)
        assert(np.allclose(expected, actual))
