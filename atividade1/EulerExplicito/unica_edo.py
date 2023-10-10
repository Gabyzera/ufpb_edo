def euler_explicito(x: float, x_f: float, n: int, y: float, f: callable) -> (list[float], list[float]):
  h = (x_f - x) / n
  VetX = [x]
  VetY = [y]
  
  print('i |   x   |   y   |  F(xy) ')
  print(f'{0} | {x:.3f} | {y:.3f} | {f(x, y):.3f}')
    
  for i in range(1, n):
    Fxy = f(x, y)
    y+= h * Fxy
    x += h  
    VetX.append(x)
    VetY.append(y) 
    
    print(f'{i} | {x:.3f} | {y:.3f} | {Fxy:.3f}')
    
  return VetX, VetY

def exemplo(x: float, y: float) -> float:
  return x - 2 * y + 1

if __name__ == "__main__":
  x, x_f, n, y = 0, 1, 10, 1
  VetX, VetY = euler_explicito(x, x_f, n, y, exemplo)
  
  print("\nVetX:", VetX)
  print("VetY:", VetY)