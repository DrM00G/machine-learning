from logistic_regression import Logistic_Regressor
import matplotlib.pyplot as plt
plt.style.use('bmh')

data = [(0, 0.01), (0, 0.01), (0, 0.05), (10, 0.02), (10, 0.15), (50, 0.12), (50, 0.28), (73, 0.03), (80, 0.10), (115, 0.06), (150, 0.12), (170, 0.30), (175, 0.24), (198, 0.26), (212, 0.25), (232, 0.32), (240, 0.45), (381, 0.93), (390, 0.87), (402, 0.95), (450, 0.98), (450, 0.85), (450, 0.95), (460, 0.91), (500, 0.95)]

lin_agres = Logistic_Regressor(data)

print("Coefficients:")
print("["+str(round((lin_agres.solve_coefficients())[0][0],3))+"],["+str(round((lin_agres.solve_coefficients())[1][0],3))+"]")

proboblity = lin_agres.evaluate(lin_agres.solve_coefficients(),300)
print()
print("Proboblity of beating average player after 300 hours of practice:")
print(str(round(proboblity, 3)))


x_coords = range(750)
win_probobily = []
for time_played in range(750):
    win_probobily.append(lin_agres.evaluate(lin_agres.
    solve_coefficients(),time_played))

plt.title('Probability to beat average player base on time played.') 
plt.plot(x_coords,win_probobily,linewidth = 0.75)
plt.legend(['Probobility against average player'])
plt.xlabel('Hours Played')
plt.ylabel('Percent chance of winning')


plt.show()