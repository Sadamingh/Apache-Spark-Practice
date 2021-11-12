from start import *
import os

filename = "start.py"


def test_q1():
    start_service()
    assert Q1() == ['1,2,3', '4,104', '5,6,105'], "Q1 returns wrong result."


def test_q2():
    assert Q2() == [3, 104, 105, 11, 13, 17], "Q2 returns wrong result."


def test_q3():
    assert Q3() == 42.17, "Q3 returns wrong result."


def test_sanity():
    stream = os.popen('pycodestyle ' + filename)
    assert stream.read() == "", "File should be in PEP8 format."


def test_ending():
    end_service()
