import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100
ON = 255
OFF = 0
vals = [ON, OFF]

# заполняем сетку случайными значениями
grid = np.random.choice(vals, N*N, p=[0.3, 0.7]).reshape(N, N)

def update(data):
  global grid
  newGrid = grid.copy()
  for i in range(N):
    for j in range(N):
      total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
               grid[(i-1)%N, j] + grid[(i+1)%N, j] +
               grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
               grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255
      if grid[i, j]  == ON:
        if (total < 2) or (total > 3):
          newGrid[i, j] = OFF
      else:
        if total == 3:
          newGrid[i, j] = ON
  grid = newGrid
  mat.set_data(grid)
  return [mat]

# настраиваем анимацию
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=40, save_count=1000)

ani.save('game_of_life.gif', writer='pillow', fps=25)