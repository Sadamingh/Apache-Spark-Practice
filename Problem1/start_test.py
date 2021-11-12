from start import *
import os

filename = "start.py"


def test_q1():
    start_serive()
    assert Q1() == ['3,91427'], "Q1 returns wrong result."


def test_q2():
    assert Q2() == [[8, 29131],
                    [7, 51231],
                    [6, 47288],
                    [5, 46283],
                    [3, 91427],
                    [3, 10909],
                    [2, 52451],
                    [1, 29145]], "Q2 returns wrong result."


def test_q3():
    assert Q3() == [1, 2, 3, 5, 6, 7, 8], "Q3 returns wrong result."


def test_q4():
    assert Q4() == 1, "Q4 returns wrong result."


def test_sanity():
    stream = os.popen('pycodestyle ' + filename)
    assert stream.read() == "", "File should be in PEP8 format."


def test_ending():
    end_serive()
