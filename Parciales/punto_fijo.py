#f = lambda x: (np.cos(x)*np.cos(x)) - x*2
#g = lambda x: np.cos(x)

#ecuacion 2
#f = lambda x: xnp.sin(x)-1
#g = lambda x:1/np.sin(x)

#ecuacion 3
#f = lambda x: (x**3)-((2*x)**2)+((4*x)/3)-(8/27)
#g = lambda x: 2/3

#ecuacion 4
#f = lambda x:  ((667.38)/x)*(1-np.exp^(-0.146843*x))-40
#g = lambda x:

#ecuacion 
#f = lambda x: (x**3)-(2x)-5 =0
#g = lambda x: ((45 - sqrt(1929))^(1/3) + (45 + sqrt(1929))^(1/3))/(2^(1/3) 3^(2/3))

#punto fijo
	
import numpy as np
from bokeh.plotting import figure, output_file, show
from decimal import *
import math
from scipy.special import lambertw

def puntoFijo(x, error_permitido, g, iters):
    iteraciones = 0
    y_vals = []
    y_vals.append(x)
    while abs(g(x)-x) > error_permitido and iteraciones < iters:
        iteraciones += 1
        x = g(x)
        y_vals.append(x)
    if x > 0.7 and x < 0.75:
        print(f'Se obtuvieron las raices {Decimal(x)} y {Decimal(x * -1)} en {iteraciones} iteraciones')
    elif x > 14 and x < 15: 
        print(f'Se obtuvo la raiz {x} en {iteraciones} iteraciones')
    else: 
        print(f'Se obtuvo la raiz {Decimal(x)} en {iteraciones} iteraciones')
    return y_vals

if __name__ == "__main__": 
    getcontext().prec = 56
    tols = [10**-8, 10**-16, 10**-32, 10**-56]
    x = 0.7 

    #Ecuación 1
    g = lambda x: np.cos(x)
    for tol in tols: 
        y_vals = puntoFijo(x,tol, g, 1000)
        output_file(f"punto_fijo1-{tol}.html")
        fig = figure()
        x_vals = list(range(len(y_vals)))
        fig.line(x_vals, y_vals, line_width=2)
        #show(fig)

    #Ecuación 2
    g = lambda x: 1/(np.sin(x))
    for tol in tols: 
        y_vals = puntoFijo(x,tol, g, 1000)
        output_file(f"punto_fijo2-{tol}.html")
        fig = figure()
        x_vals = list(range(len(y_vals)))
        fig.line(x_vals, y_vals, line_width=2)
        #show(fig)

    #Ecuación 3
    g = lambda x: ((2*x**2) - (4/3*x) + (8/27))**(1/3)
    for tol in tols: 
        y_vals = puntoFijo(x,tol, g, 1000)
        output_file(f"punto_fijo3-{tol}.html")
        fig = figure()
        x_vals = list(range(len(y_vals)))
        fig.line(x_vals, y_vals, line_width=2)
        #show(fig)

    #Ecuación 4
    e = math.e
    g = lambda x: 681 * (20* lambertw(-49/(20*e**(49/20)))+49)/2000
    for tol in tols: 
        y_vals = puntoFijo(x,tol, g, 1000)
        output_file(f"punto_fijo3-{tol}.html")
        fig = figure()
        x_vals = list(range(len(y_vals)))
        fig.line(x_vals, y_vals, line_width=2)
        #show(fig)
    
    #Ecuación 5
    g = lambda x: (2*x + 5)**(1/3)
    for tol in tols: 
        y_vals = puntoFijo(x,tol, g, 1000)
        output_file(f"punto_fijo5-{tol}.html")
        fig = figure()
        x_vals = list(range(len(y_vals)))
        fig.line(x_vals, y_vals, line_width=2)
        #show(fig)