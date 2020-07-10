import sys
sys.path.append('src')
from GradientDescent import GradientDescent

def single_variable_function(x,y,z):
    return (x-1)**2
def two_variable_function(x, y, z):
    return (x-1)**2 + (y-1)**3
def three_variable_function(x, y, z):
    return (x-1)**2 + (y-1)**3 + (z-1)**4
def six_variable_function(x1, x2, x3, x4, x5, x6):
    return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6

min = GradientDescent(single_variable_function)

gradient = min.compute_gradient(delta=0.01)
print(gradient)

assert gradient == (-2.0000000000000018, 0.0, 0.0), 'Gradient should be (-2.0000000000000018, 0.0, 0.0) but was actually '+str(gradient)

min = GradientDescent(two_variable_function)

gradient = min.compute_gradient(delta=0.01)
print(gradient)

assert gradient == (-2.0000000000000018, 3.0001000000000055, 0.0), 'Gradient should be [-2.0000000000000018, 3.0001000000000055, 0.0] but was actually '+str(gradient)

min = GradientDescent(three_variable_function)

gradient = min.compute_gradient(delta=0.01)
print(gradient)

assert gradient == (-2.0000000000000018, 3.0001000000000055, -4.0004000000000035), 'Gradient should be (-2.0000000000000018, 3.0001000000000055, -4.0004000000000035) but was actually '+str(gradient)

print("tests passed")