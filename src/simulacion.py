import numpy as np

from src.modelo import sigmoide


def generar_datos(n, rng, theta_verdadero=(-1, 2)):
    theta0, theta1 = theta_verdadero

    x = rng.uniform(-2, 2, size=n)
    probabilidades = sigmoide(theta0 + theta1 * x)
    y = rng.binomial(1, probabilidades)

    return x, y