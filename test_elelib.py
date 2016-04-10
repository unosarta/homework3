from nose.tools import assert_equal, assert_raises

from element_data import elelib_construct, element_data, isotopes

def test_element_data():
        
        obs = element_data([0,1,2,3,4,5,6,7])
        exp = {"mm": 1, "Z": 2, "rho": 3}
        assert_equal(obs,exp)

def test_ed_failure():

        assert_raises(IndexError, element_data, [])

def test_isotopes():

        exp = [("kek",)]
        obs = isotopes(["lol 4 3 2 1", "kek", "5 6 7 8", "hue", "9 10 11 12"],"lol 4 3 2 1", ["lol",4,3,2,1])
        assert_equal(exp,obs)

def test_iso_failure():

        assert_raises(IndexError, isotopes, ["lol 4 3 2 1", "kek", "5 6 7 8", "hue", "9 10 11 12"], "lol 4 3 2 1", [])

def test_lib():

        obs = elelib_construct('filetotest')
        exp = {'lol': { 'iso': [('5','1'),('6','2'),('7','3'),('8','4')], 'rho': '3', 'mm': '1', 'Z': '2'}}
        assert_equal(obs,exp)
