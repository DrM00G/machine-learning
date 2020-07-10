from GradientDescent import GradientDescent

def f(x,y):
    return 1 + (2*x)**2 + (y-1)**2
minimizer = GradientDescent(f)

minimizer.grid_search([-4,-2,0,-2,4],[-4,-2,0,-2,4])
 
minimizer.min
 
minimizer.compute_gradient(delta=0.01)
 
minimizer.descend(scaling_factor=0.001, delta=0.01, num_steps=4, logging=True)
 
minimizer.min
