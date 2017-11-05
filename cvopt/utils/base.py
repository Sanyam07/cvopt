import os, copy
import pandas as pd, numpy as np
from sklearn.base import clone


def mk_dir(path, error=False):
    if os.path.isdir(path):
        if error:
            raise Exception("this dir could not be made (already exist)")
    else:
        os.makedirs(path, mode=0o777)
        os.chmod(path, mode=0o777)


def to_nparray(Xy, ravel_1d):
    """
    ravel_1d
        When True, Xy.shape=(n,1) -> Xy.shape=(n,)
    """
    if isinstance(Xy, (pd.core.frame.DataFrame, pd.core.frame.Series)):
        Xy = Xy.values

    if (ravel_1d) and (len(Xy.shape) == 2) and (Xy.shape[1] == 1):
        return Xy.ravel()
    else:
        return Xy


def chk_Xy(Xy, none_error, ravel_1d, msg_sjt):
    base_msg = " must be np.array or pd.DataFrame."
    if Xy is None:
        if none_error:
            raise TypeError(msg_sjt+base_msg)
    elif not isinstance(Xy, (np.ndarray, pd.core.frame.DataFrame)):
        raise TypeError(msg_sjt+base_msg)

    return to_nparray(Xy, ravel_1d)


def clone_estimator(estimator, params):
    try:
        estimator = clone(estimator).set_params(**params)
    except RuntimeError:
        estimator = copy.deepcopy(estimator).set_params(**params)
    return estimator