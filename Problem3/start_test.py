from start import *
import os

filename = "start.py"


def test_q1():
    start_service()
    assert Q1() == "DayOrder,DayOfWeekStr,starttime,endtime,permit,PermitLocation,locationid,scheduleid,start24," \
                   "end24,CNN,Addr_Date_Create,Addr_Date_Modified,block,lot,ColdTruck,Applicant,X,Y,Latitude," \
                   "Longitude,Location", "Q1 returns wrong result. "


def test_q2():
    assert Q2() == [0, 1, 2, 3, 4, 5, 6], "Q2 returns wrong result."


def test_q3():
    assert Q3() == [datetime(2017, 10, 2, 10, 45, 56),
                    datetime(2017, 10, 2, 10, 45, 56),
                    datetime(2017, 10, 2, 10, 45, 56)], "Q3 returns wrong result."


def test_q4():
    assert Q4() == 650613184, "Q4 returns wrong result."


def test_q5():
    assert Q5() == [36.0, 36.0, 36.0, 3603216.0, 3603216.0], "Q5 returns wrong result."


def test_sanity():
    stream = os.popen('pycodestyle ' + filename)
    assert stream.read() == "", "File should be in PEP8 format."


def test_ending():
    end_service()
