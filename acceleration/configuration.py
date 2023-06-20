import numpy as np
from mpmath import mp

# SET DATA TYPE
DT = np.dtype('float128') # numpy precision
mp.dps = 100 # mpmath precision

# SET zeta(1.2), PI, log 2, limit of slow series VALUE APPROXIMATION (~100)
Z = 5.591582441177750776536563193423143277629903241802331099473728250024897906802651077991103320801610144
PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067
L2 = 0.693147180559945309417232121458176568075500134360255254120680009493393621969694715605863326996418687
C1 = 2.10974280123689197447

constants = np.array([Z, PI, L2, C1], dtype=DT)
