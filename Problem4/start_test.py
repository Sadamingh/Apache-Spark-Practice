from start import *
import os

filename = "start.py"


def test_q1():
    start_service()
    assert Q1() == (2, 3), "Q1 returns wrong result."


def test_q2():
    assert Q2() == (6, 7), "Q2 returns wrong result."


def test_q3():
    assert Q3() == [1, 2, 6, 3, 4, 7, 1, 9, 3, 4, 2, 8, 5], "Q3 returns wrong result."


def test_q4():
    assert Q4() == [6, 7], "Q4 returns wrong result."


def test_q5():
    assert Q5() == [1, 2, 3, 4], "Q5 returns wrong result."


def test_sanity():
    stream = os.popen('pycodestyle ' + filename)
    assert stream.read() == "", "File should be in PEP8 format."


def test_ending():
    end_service()
