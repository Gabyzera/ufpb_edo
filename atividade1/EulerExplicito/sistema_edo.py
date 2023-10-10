def euler_explicito_sistema(x: float, x_f: float, n: int, y: tuple, f: callable) -> (list[float], list[tuple]):
  h = (x_f - x) / n
  VetX = [x]
  VetY = [y]  
  
  print('i |   x   |   y1  |  y2   | f1(x,y1,y2) | f2(x,y1,y2)')
    
  for i in range(0, n):
    Fxy = f(x, y[0], y[1]) 
     
    print(f'{i} | {x:.3f} | {y[0]:.3f} | {y[1]:.3f} | {Fxy[0]:.3f} | {Fxy[1]:.3f}')
    
    y = (y[0] + h * Fxy[0], y[1] + h * Fxy[1])
    x += h 
    VetX.append(x)
    VetY.append(y) 
    
  return VetX, VetY

def exemplo(x: float, y1: float, y2: float) -> tuple:
  f1 = x - 2*y1 + y2
  f2 = y1 + x + y2
  
  return f1, f2

if __name__ == "__main__":
  x, x_f, n, y = 0, 1, 10, (1, 0)
  VetX, VetY = euler_explicito_sistema(x, x_f, n, y, exemplo)
  
  print("\nVetX:", VetX)
  print("VetY:", VetY)