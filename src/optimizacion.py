import numpy as np
from scipy.optimize import minimize
from src.modelo import riesgo_empirico


def ajustar_theta(x, y, theta_inicial=(0.0, 0.0), maxiter=None):
    opciones = {}
    if maxiter is not None:
        opciones["maxiter"] = maxiter

    resultado = minimize(
        fun=riesgo_empirico,
        x0=np.array(theta_inicial, dtype=float),
        args=(x, y),
        options=opciones,
    )

    theta_hat = resultado.x
    riesgo_hat = resultado.fun

    return theta_hat, riesgo_hat, resultado