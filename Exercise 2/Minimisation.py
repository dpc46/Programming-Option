from scipy.optimize import minimize
import math

parameters = [-6.40354312e+01, -4.32871675e+01,  6.86530307e-03,  6.05248631e+01, -1.58261131e-04, -4.14713377e+01,  1.37864040e-06,  1.41056445e+01, -4.87354872e-09, -1.90822678e+00,  5.78093429e-12]

def function(data, a, b, c, d, e, f, g, h, i, j, k):
    x = data[0]
    y = data[1]
    return a + b*(x) + c*(y) + d*(x**2) + e*(y**2) + f*(x**3) + g*(y**3) + h*(x**4) + i*(y**4) + j*(x**5) + k*(y**5)
args=tuple(parameters)
min = minimize(function, [1,100], args)

min_array = min['x']
r_0 = min_array[0]
theta_0 = min_array[1]
E_min = min['fun']
print(r_0)
print(theta_0)
print(E_min)

print(function([r_0, theta_0], *parameters))

k_r = 2 * parameters[3]
k_theta = 2 * parameters[4]
print (k_theta)
print(k_theta)
m_u =  1.66053886e-27
a = (1 / (2 * (math.pi)))

v_1 = a * (math.sqrt(k_r / (2 * m_u)))
v_2 = a * ((k_theta * 2)**0.5 / (m_u * ((r_0*10**-10) ** 2)))
print(v_1)
print(v_2)
