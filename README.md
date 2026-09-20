# EDO Separable — Solución Analítica y Método de Euler

## Descripción

Se eligió la siguiente ecuación diferencial separable:

```
dy/dt = k * y / (1 + t)
```

Esta ecuación describe una cantidad `y` que crece con el tiempo `t`, pero cuya
tasa de crecimiento se va frenando poco a poco a medida que `(1 + t)` aumenta.

**Condiciones:**
- Condición inicial: `y(0) = 5`
- Constante: `k = 0.3`
- Intervalo de aproximación: `t ∈ [0, 1]`
- Paso del método de Euler: `h = 0.2`

## Solución analítica (separación de variables)

**Paso 1 — Separar las variables:**

```
dy/dt = k * y / (1 + t)
dy / y = k / (1 + t) dt
```

**Paso 2 — Integrar ambos lados:**

```
∫ dy/y = ∫ k / (1+t) dt
ln|y| = k * ln|1+t| + C
```

**Paso 3 — Despejar y:**

```
y = e^(k*ln|1+t| + C) = e^C * (1+t)^k
```

**Paso 4 — Aplicar la condición inicial y(0) = 5:**

```
5 = e^C * (1+0)^k = e^C   →   e^C = 5
```

**Paso 5 — Solución final:**

```
y(t) = 5 * (1 + t)^0.3
```

## Aproximación numérica (método de Euler)

El método de Euler aproxima la solución usando la fórmula:

```
y_(n+1) = y_n + h * f(t_n, y_n)
```

donde `f(t, y) = k * y / (1 + t)`.

## Resultados

| t   | y (Euler) | y (exacta) |
|-----|-----------|------------|
| 0.0 | 5.0000    | 5.0000     |
| 0.2 | 5.3000    | 5.2811     |
| 0.4 | 5.5650    | 5.5311     |
| 0.6 | 5.8035    | 5.7571     |
| 0.8 | 6.0211    | 5.9642     |
| 1.0 | 6.2218    | 6.1557     |

## Archivos

- `edo_separable.py` — código que resuelve el problema (incluye la
  resolución analítica documentada en comentarios, la aproximación por
  Euler y su comparación con la solución exacta).