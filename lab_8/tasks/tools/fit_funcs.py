# -*- coding: utf-8 -*-
def least_sq(xy):
    """
    Fits linear function to given vector of 2D points.

    Funkcja liczy parametry funkcji liniowej ax+b do danych za pomocą metody
    najmniejszych kwadratów.
    (1 pkt.)

    A = (N*Sum(xy)-Sum(x)*Sum(y))/Delta
    B = (Sum(x^2)*Sum(y)-Sum(x)*Sum(xy))/Delta
    Delta = N*Sum(x^2) - (Sum(x)^2)

    :param xy: vector of 2D points (shape (2, n))
    :type xy: np.ndarray
    :return: Tuple of fitted parameters
    """

    N = xy.shape[1]
    x = xy[0]
    y = xy[1]

    x_sum = x.sum()
    x_2sum = (x**2).sum()
    y_sum = y.sum()
    xy_sum = (x*y).sum()

    Delta = N * x_2sum - x_sum**2
    B = (x_2sum*y_sum - x_sum*xy_sum) / Delta
    A = (N*xy_sum - x_sum*y_sum) / Delta

    return A, B
