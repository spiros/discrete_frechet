
import sys
import os
import numpy as np
import pytest

from frechetdist import frdist

TEST_CASES = [

    {
        'P': [[1, 1], [2, 1], [2, 2]],
        'Q': [[2, 2], [0, 1], [2, 4]],
        'expected': 2.0
    },

    {
        'P': np.array((np.linspace(0.0, 1.0, 100), np.ones(100))).T,
        'Q': np.array((np.linspace(0.0, 1.0, 100), np.ones(100))).T,
        'expected': 0
    },

    {
        'P': [[-1, 0], [0, 1], [1, 0], [0, -1]],
        'Q': [[-2, 0], [0, 2], [2, 0], [0, -2]],
        'expected': 1.0
    },

    {
        'P': np.array((np.linspace(0.0, 1.0, 100), np.ones(100)*2)).T,
        'Q': np.array((np.linspace(0.0, 1.0, 100), np.ones(100))).T,
        'expected': 1.0
    },
    # Test with curves of different lengths
    {
        'P': [[0, 0], [1, 1], [2, 2]],
        'Q': [[0, 1], [1, 2]],
        'expected': 1.0
    },
    # Test with curves that have duplicate points
    {
        'P': [[0, 0], [1, 1], [1, 1], [2, 2]],
        'Q': [[0, 1], [1, 2], [2, 3]],
        'expected': 1.0
    },
    # Test with a self-intersecting curve
    {
        'P': [[0, 0], [2, 2], [0, 2], [2, 0]],
        'Q': [[0, 1], [1, 1], [1, 2]],
        'expected': 2.23606797749979
    },
    # Test with single point curves
    {
        'P': [[0, 0]],
        'Q': [[1, 1]],
        'expected': 1.4142135623730951
    },
    # Test with 3D curves
    {
        'P': [[0, 0, 0], [1, 1, 1], [2, 2, 2]],
        'Q': [[0, 0, 1], [1, 1, 2], [2, 2, 3]],
        'expected': 1.0
    }
]


def test_main():
    for test_case in TEST_CASES:
        P = test_case['P']
        Q = test_case['Q']
        eo = test_case['expected']

        assert np.isclose(frdist(P, Q), eo)


def test_errors():

    P = []
    Q = [[2, 2], [0, 1], [2, 4]]

    with pytest.raises(ValueError):
        frdist(P, Q)

    P = [[1, 1]]
    Q = []

    with pytest.raises(ValueError):
        frdist(P, Q)
