import math
import numpy as np
from configuration import *

def Aitken_transform(items: np.ndarray, steps=-1) -> np.ndarray:
    if steps == -1:
        steps = int((len(items) - 1) / 2)
    
    for _ in range(steps):
        acel = np.zeros(len(items) - 2, dtype=DT)

        for i in range(0, len(items) - 2):
            acel[i] = (items[i] * items[i+2] - items[i+1]**2) / \
                (items[i+2] - 2 * items[i+1] + items[i])

        items = acel

        if len(acel) < 3:
            return acel
        
    return acel

def Aitken_transform_m(series, error=1e-5) -> np.ndarray:
    n = 10
    acel = np.zeros(n-2, dtype=DT)
    s = series(n) # series of n elements (np.array)

    for i in range(0, n-2):
        acel[i] = (s[i] * s[i+2] - s[i+1]**2) / \
            (s[i+2] - 2 * s[i+1] + s[i])
    
    while abs(acel[len(acel)-1] - math.pi**2 / 6) > error:
        n += 2
        acel = np.zeros(n-2, dtype=DT)
        s = series(n) # series of n elements (np.array)

        for i in range(0, n-2):
            acel[i] = (s[i] * s[i+2] - s[i+1]**2) / \
                (s[i+2] - 2 * s[i+1] + s[i])
    
    print(n)
    return acel


def Richardson_transform(items: np.ndarray, p=1, steps=-1) -> np.ndarray:
    """Receive a p that represents the power of the Richardson transform"""
    if steps == -1:
        steps = int(math.log2(len(items))) - 1
    
    for _ in range(steps):
        acel = np.zeros(int(len(items)/2), dtype=DT)

        for i in range(0, int(len(items)/2)):
            acel[i] = items[2*i] + (items[2*i] - items[i]) / \
                np.expm1(p * math.log(2))

        items = acel
        p = p + 1
    
    return acel

def Richardson_transform_m(series, p=1, error=1e-5) -> np.ndarray:
    n = 4
    acel = np.zeros(int(n/2), dtype=DT)
    s = series(n) # series of n elements (np.array)

    for i in range(0, int(n/2)):
        acel[i] = s[2*i] + (s[2*i] - s[i]) / \
            np.expm1(p * math.log(2))
    
    while abs(acel[-1] - math.pi**2 / 6) > error:
        n += 2
        acel = np.zeros(int(n/2), dtype=DT)
        s = series(n)

        for i in range(0, int(n/2)):
            acel[i] = s[2*i] + (s[2*i] - s[i]) / \
                np.expm1(p * math.log(2))
    
    print(n)
    return acel

def Epsilon_transfom(items: np.ndarray, steps=-1) -> np.ndarray:
    # Initial values
    aux = np.zeros(len(items)+1, dtype=DT)
    acel = items

    if steps == -1:
        steps = int(len(items) / 2) - 1

    for _ in range(steps):
        for i in range(0, len(aux) - 3):
            aux[i] = acel[i+1] + 1/(acel[i+1] - acel[i])
        aux = aux[:-2]

        for i in range(0, len(acel) - 3):
            acel[i] = acel[i+1] + 1/(aux[i+1] - aux[i])
        acel = acel[:-2]
        
    
    return acel

def G_transform(items: np.ndarray, steps=-1) -> np.ndarray:
    # Initial values
    aux1 = np.ones(len(items) + 1, dtype=DT)
    aux2 = np.zeros(len(items), dtype=DT)

    aux2[0] = items[0]
    for i in range(1, len(items)):
        aux2[i] = items[i] - items[i-1]
    
    acel = items

    if steps == -1:
        steps = len(items) - 1

    for _ in range(steps):
        for i in range(len(aux1) - 2):
            aux1[i] = aux1[i+1] * (aux2[i+1] / aux2[i] - 1)
        aux1 = aux1[:-1]

        for i in range(len(aux2) - 2):
            aux2[i] = aux2[i+1] * (aux1[i+1] / aux1[i] - 1)
        aux2 = aux2[:-1]

        for i in range(len(acel) - 2):
            acel[i] = acel[i] - aux2[i] * (acel[i+1] - acel[i])/(aux2[i+1] - aux2[i])
        acel = acel[:-1]
    
    return acel


if __name__ == "__main__":
    
    print("Hello World")
