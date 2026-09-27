import numpy as np


def sigmoide(t):
    return 1.0 / (1.0 + np.exp(-t))


def p_theta(theta, x):
    theta0, theta1 = theta
    return sigmoide(theta0 + theta1 * x)


def riesgo_empirico(theta, x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    p = p_theta(theta, x)

    eps = 1e-12
    p = np.clip(p, eps, 1 - eps)

    return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))