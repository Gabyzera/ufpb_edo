def runge_kutta_4(x: float, x_f: float, n: int, y: float, f: callable) -> (list[float], list[float]):
  h = (x_f - x) / n
  VetX = [x]
  VetY = [y]
  
  print('i |   x    |   y')
  print(f'{0} | {x:.4f} | {y:.4f}')
    
  for i in range(1, n):
    k1 = f(x, y)
    k2 = f(x + h/2, y + h/2*k1)
    k3 = f(x + h/2, y + h/2*k2)
    k4 = f(x + h, y + h*k3)
    
    y += (h/6) * (k1 + 2 * (k2+k3) + k4)
    x += h
    
    print(f'{i} | {x:.4f} | {y:.4f}')
    
    VetX.append(x)
    VetY.append(y)
    
  return VetX, VetY

def exemplo(x: float, y: float) -> float:
  return x**2 + y

if __name__ == "__main__":
  x, x_f, n, y = 0, 0.6, 3, 0
  runge_kutta_4(x, x_f, n, y, exemplo)