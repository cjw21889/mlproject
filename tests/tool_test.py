# -*- coding: UTF-8 -*-

# Import from standard library
import mlproject
# Import from our lib
from mlproject.tools import haversine
import pytest


def test_clean_data():
    assert haversine(1,2,1,4) == 222.38985328911747
