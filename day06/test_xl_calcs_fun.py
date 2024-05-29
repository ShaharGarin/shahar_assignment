import xl_calcs_fun as xc
import numpy as np
from scipy import stats


def test_calc_loc_ratio():
    test_col1 = [0, 0, 0, 6, 9, 0, 0, 0, 3, 6, 0, 0, 0, 0, 0, 0, 15]
    test_col2 = [0, 0, 0, 6, 2, 0, 0, 0, 2, 6, 0, 0, 0, 0, 0, 0, 2]
    assert(xc.calc_loc_ratio(test_col1, test_col2) == [0, 0, 0, 1.0, 2/9, 0, 0, 0, 2/3, 1.0, 0, 0, 0, 0, 0, 0, 2/15])
    
    test_col1 = [1, 1, 1, 6, 9, 0, 0, 0, 3, 6, 0, 1, 0, 0, 0, 0, 15]
    test_col2 = [0, 0, 0, 6, 2, 0, 0, 0, 2, 6, 0, 1, 0, 0, 0, 0, 2]
    assert(xc.calc_loc_ratio(test_col1, test_col2) == [0, 0, 0, 1.0, 2/9, 0, 0, 0, 2/3, 1.0, 0, 1.0, 0, 0, 0, 0, 2/15])

def test_calc_comp_ratio():
    test_col = [0.3, 0.4, 0, 0.7]
    assert(xc.calc_comp_ratio(test_col) == [1-0.3, 1-0.4, 1-0, 1-0.7])

def test_calc_ave_cov():
    test_col = ["[20.0, 40.0, 60.5]", "[0.0, 100.0, 1.0]", "[3.0]", "[100.0]"]
    assert(xc.calc_ave_cov(test_col) == [np.mean([20, 40, 60.5]), np.mean([0, 100, 1]), np.mean([3]), np.mean([100])])

def test_calc_col_ava():
    test_col = [0.8, 1.0, 0.78959, 0.1, 0.0, 1.0]
    assert(xc.calc_col_ava(test_col) == [np.mean(test_col), stats.sem(test_col)])
