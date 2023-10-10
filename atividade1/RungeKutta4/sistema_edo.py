def runge_kutta_4_system(x: float, x_f: float, n: int, y1: float, y2: float, f1: callable, f2: callable) -> (list[float], list[float], list[float]):
  h = (x_f - x) / n
  VetX = [x]
  VetY1 = [y1]
  VetY2 = [y2]
  
  print('i |   x   |  y1  |  y2')
  print(f'{0} | {x:.4f} | {y1:.4f} | {y2:.4f}')
    
  for i in range(1, n):
    k1_y1 = f1(x, y1, y2)
    k1_y2 = f2(x, y1, y2)
 
    k2_y1 = f1(x + h/2, y1 + h/2*k1_y1, y2 + h/2*k1_y2)
    k2_y2 = f2(x + h/2, y1 + h/2*k1_y1, y2 + h/2*k1_y2)
        
    k3_y1 = f1(x + h/2, y1 + h/2*k2_y1, y2 + h/2*k2_y2)
    k3_y2 = f2(x + h/2, y1 + h/2*k2_y1, y2 +h/2*k2_y2)
        
    k4_y1 = f1(x + h, y1 + h*k3_y1, y2 + h*k3_y2)
    k4_y2 = f2(x + h, y1 + h*k3_y1, y2 + h*k3_y2)
        
    y1 += (h/6) * (k1_y1 + 2 * (k2_y1 + k3_y1) + k4_y1)
    y2 += (h/6) * (k1_y2 + 2 * (k2_y2 + k3_y2) + k4_y2)
    x += h
        
    print(f'{i} | {x:.4f} | {y1:.4f} | {y2:.4f}')
        
    VetX.append(x)
    VetY1.append(y1)
    VetY2.append(y2)
        
  return VetX, VetY1, VetY2

def f1_exemplo(x: float, y1: float, y2: float) -> float:
  return 2*x*y1 + y2

def f2_exemplo(x: float, y1: float, y2: float) -> float:
  return y1

if __name__ == "__main__":
  x, x_f, n, y1, y2 = 0, 0.4, 2, 0, 1
  runge_kutta_4_system(x, x_f, n, y1, y2, f1_exemplo, f2_exemplo)
