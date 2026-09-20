# Problema: Crecimiento poblacional
# Ecuacion diferencial: dy/dt = k * y
k, y0 = 2, 100   # tasa de crecimiento y valor inicial de població

# Funcion que describe la ecuacion diferencial
def f(t, y):
    return k * y

# Parametros del intervalo y paso
t0, h, t_final = 0, 0.1, 2

# Numero de pasos a realizar
n_pasos = int((t_final - t0) / h)

# Listas de resultados
t_valores = [t0]
y_valores = [y0]

# Metodo de Euler
for i in range(n_pasos):
    y_siguiente = y_valores[-1] + h * f(t_valores[-1], y_valores[-1])
    t_siguiente = t_valores[-1] + h
    y_valores.append(y_siguiente)
    t_valores.append(t_siguiente)

# Resultados
print("Aproximacion por metodo de Euler")
print("dy/dt = k * y,  k =", k, ",  y(0) =", y0)
print("-" * 40)
for t, y in zip(t_valores, y_valores):
    print(f"t = {t:.1f}, y = {y:.4f}")