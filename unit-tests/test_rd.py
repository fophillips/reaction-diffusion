from nose.tools import *
import numpy as np

from rd import RD

class TestRD:
    def setup(self):
        self.init_conc = np.array([0, 0, 0])
        self.reaction = np.array([0, 1, 0])
        self.diff = np.array([1, 1, 1])
        self.rd = RD(self.reaction, self.diff)

    def test_one_timestep(self):
        expected = np.array([0, 1, 0])
        actual = self.rd.next_concentrations(self.init_conc)
        assert(np.array_equal(expected, actual))
        
    def test_two_timesteps(self):
        expected = np.array([1, 0, 0])
        actual = self.rd.n_timesteps(self.init_conc, 2)
        print("Expected:",expected)
        print("Actual:",actual)
        assert(np.array_equal(expected, actual))

    def test_three_timesteps(self):
        expected = np.array([0, 2, 0])
        actual = self.rd.n_timesteps(self.init_conc, 3)
        print("Expected:",expected)
        print("Actual:",actual)
        assert(np.array_equal(expected, actual))
