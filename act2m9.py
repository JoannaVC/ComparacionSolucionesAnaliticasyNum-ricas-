# Ecuación diferencial: dy/dt = k * y / (1 + t)
# --------------------------------------------------------------------
# RESOLUCION ANALITICA POR SEPARACION DE VARIABLES
# --------------------------------------------------------------------
# 1. Separar las variables
#     dy/dt = k * y / (1 + t)
#     dy / y = k / (1 + t) dt

# 2. Integrar ambos lados
#     Integral( dy / y )        = Integral( k / (1 + t) dt )
#     ln|y|                     = k * ln|1 + t| + C

# 3. Despejar y
#     y = e^(k*ln|1+t| + C) = e^C * (1+t)^k

# 4. Aplicar la condicion inicial y(0) = y0 = 5
#     5 = e^C * (1+0)^k = e^C   ->   e^C = 5

# 5. Escribir la solucion final
#     y(t) = 5 * (1 + t)^0.3

# Esta formula es la que se implementa abajo en solucion_exacta(t).
# --------------------------------------------------------------------

# Constantes
k, y0 = 0.3, 5

# Ecuacion diferencial dy/dt = f(t, y)
def f(t, y):
    return k * y / (1 + t)

# Solucion analitica
def solucion_exacta(t):
    return y0 * (1 + t) ** k

# Parametros del intervalo y paso
t0, h, t_final = 0, 0.2, 1

# Numero de pasos a realizar
n_pasos = int((t_final - t0) / h)

# Listas de resultados de Euler
t_valores = [t0]
y_euler = [y0]

# Metodo de Euler
for i in range(n_pasos):
    y_siguiente = y_euler[-1] + h * f(t_valores[-1], y_euler[-1])
    t_siguiente = t_valores[-1] + h
    y_euler.append(y_siguiente)
    t_valores.append(t_siguiente)

# Resultados
print("Aproximacion por metodo de Euler vs. solución analítica")
print("Ecuación: dy/dt = k*y/(1+t)")
print("Variables:  k =", k, ",  y(0) =", y0)
print("Solución analítica: y(t) = y0 * (1+t)^k")
print("-" * 50)
print(f"{'t':>5}{'y_Euler':>12}{'y_exacta':>12}")
for t, y_aprox in zip(t_valores, y_euler):
    y_real = solucion_exacta(t)
    print(f"{t:5.1f}{y_aprox:12.4f}{y_real:12.4f}")