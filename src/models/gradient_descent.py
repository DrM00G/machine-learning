class GradientDescent:
    def __init__(self, function):
        self.f = function
        self.min = (0,0,0)

    def grid_search(self, *grid_data):
        param_combos = [(i, j) for i in grid_data[0]
                        for j in grid_data[1]]
        min_pos = self.min
        min_err = float('inf')
        for pos in param_combos:
            err = self.f(*pos)
            if err < min_err:
                min_err = err
                min_pos = pos
        self.min = min_pos

    def descend(self, scaling_factor=0.01, delta=0.01, num_steps=50, logging=False):
        old_min = self.min
        gradient = self.compute_gradient(delta)
        self.min = tuple(beta - scaling_factor *
                             val for beta, val in zip(old_min, gradient))
        if logging:
            print(self.min)
        if num_steps > 1:
            self.descend(scaling_factor, delta, num_steps-1, logging)

    def cartesian_product(self,arrays):
        result = []
        temp = []
        for i in range(len(arrays)):
            temp = result
            result = []
            for j in arrays[i]:
                if i > 0:
                    for k in temp:
                        result.append(k + [j])
                else:
                    result.append([j])
        return result

    def compute_gradient(self, delta=0.001):
        result = []
        for i in range(len(self.min)):
            altered_guess = list(self.min)
            altered_guess[i] += delta
            f_approx = self.f(*altered_guess)
            altered_guess[i] -= 2*delta
            b_approx = self.f(*altered_guess)
            result.append(f_approx - b_approx)
        return tuple(g / (2*delta) for g in result)
