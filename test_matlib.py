from nose.tools import assert_equal, assert_raises

from material_data import matlib_construct, mass_fraction, mat_data

def test_mass():

    obs = mat_data(["lol", 1,2,3,4])
    exp = {"rho":1}
    assert_equal(obs, exp)

def test_iso():

        obs = mass_fraction('lol 4 1', ["lol", '4','1'], ['lol 4 1', 'kek 5 6 7 8', 'lol 9 1 2 3'])
        exp = [['kek', '5', '6', '7', '8']]
        assert_equal(obs, exp)

def test_lib():

        obs = matlib_construct("filetotest")
        exp = {'lol': { 'fraction' : [['5', '1'], ['6', '2']], 'rho' : '1'}}
        assert_equal(obs,exp)
