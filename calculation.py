import numpy as np
from scipy.optimize import fsolve


def equations(vars):
    x11, x12, x21, x22, x31, x32, gamma, lambda_ = vars
    eq1 = 25*x11 + 30*x12 + 3*x21 + 20*x22 + 40*x31 + 13*x32 - 10000000
    eq2 = 0.003*x11 + 0.007*x12 + 0.001*x21 + 0.002*x22 + 0.007*x31 + 0.002*x32 - 4.5
    eq3 = 0.5*(100 - 25)*(np.sqrt((100 - 25)*x11)**(-1)) - 25*lambda_ - gamma*0.003
    eq4 = 0.5*(150 - 30)*(np.sqrt((150 - 30)*x12)**(-1)) - 30*lambda_ - gamma*0.007
    eq5 = 0.5*(10 - 3)*(np.sqrt((10 - 3)*x21)**(-1)) - 3*lambda_ - 0.001*gamma
    eq6 = 0.5*(50 - 20)*(np.sqrt((50 - 20)*x22)**(-1)) - 20*lambda_ - 0.002*gamma
    eq7 = 0.5*(70 - 40)*(np.sqrt((70 - 40)*x31)**(-1)) - 40*lambda_ - 0.007*gamma
    eq8 = 0.5*(30 - 13)*(np.sqrt((30 - 13)*x32)**(-1)) - 13*lambda_ - 0.002*gamma
    return [eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8]


x_guess = np.ones(8)
solution = fsolve(equations, x_guess)


solution = list(solution)
for i in range(len(solution)):
  solution[i] = int(np.ceil(solution[i]))

pollution = sum(np.array(solution[:6]) * np.array([0.003, 0.007, 0.001, 0.002, 0.007, 0.002]))/1000

print(f"""
      {solution}\n
      {pollution}
      """)
