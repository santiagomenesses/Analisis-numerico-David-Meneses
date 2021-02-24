import numpy as np
from bokeh.plotting import figure, output_file, show
from decimal import *
import math 
from scipy.special import lambertw

limite = 5000
def uno(x):
    return np.cos(x)

def dos(x): 
    return 1/(np.sin(x))

def tres(x):
    return ((2*x**2) - (4/3*x) + (8/27))**(1/3)

def cuatro(x): 
    e = math.e
    return 681 * (20* lambertw(-49/(20*e**(49/20)))+49)/2000

def cinco(x): 
    return (2*x + 5)**(1/3)

def steffensen(tol,x0,f, grafica): 
    y_vals = []
    y_vals.append(x0)
    x1 = f(x0)
    y_vals.append(x1)
    x2 = f(x1)
    y_vals.append(x2)
    x3 = x0 - ((x1 - x0)**2)/(x2 - 2*x1 + x0)
    y_vals.append(x3)
    iterador = 3
    if(x3 != 0):
        while abs((x3-x0)/x3) > tol: 
            x0 = x3
            x1 = f(x0)
            y_vals.append(x1)
            x2 = f(x1)
            y_vals.append(x2)
            if  ((x2 - 2*x1 + x0) != 0): 
                x3 = x0 - ((x1 - x0)**2)/(x2 - 2*x1 + x0) 
                y_vals.append(x3)
            iterador += 3
            if x3 == 0: 
                break
    x_vals = list(range(len(y_vals)))
    output_file(grafica + f"-{tol}.html")
    fig = figure()
    fig.line(x_vals, y_vals, line_width=2)
    #show(fig)

    resultado = []
    resultado.append(iterador)
    resultado.append(x3)
    return resultado
        
            
if __name__ == "__main__": 
    getcontext().prec = 56
    tols = [10**-8, 10**-16, 10**-32, 10**-56]
    x = 0.7
    
    for tol in tols:  
        retorno = steffensen(tol, x, uno, "steffensen1")
        iteraciones = retorno[0]
        raiz = retorno[1]
        print(f'En {iteraciones} iteraciones y tolerancia de {tol} se obtuvieron las raices {Decimal(raiz)} y {-1*Decimal(raiz)}')
    for tol in tols:  
        retorno = steffensen(tol, x, dos, "steffensen2")
        iteraciones = retorno[0]
        raiz = retorno[1]
        print(f'En {iteraciones} iteraciones y tolerancia de {tol} se obtuvieron las raices {Decimal(raiz)}')
    for tol in tols:  
        retorno = steffensen(tol, x, tres, "steffensen3")
        iteraciones = retorno[0]
        raiz = retorno[1]
        print(f'En {iteraciones} iteraciones y tolerancia de {tol} se obtuvieron las raices {Decimal(raiz)}')
    for tol in tols:  
        retorno = steffensen(tol, x, cuatro, "steffensen4")
        iteraciones = retorno[0]
        raiz = retorno[1]
        print(f'En {iteraciones} iteraciones y tolerancia de {tol} se obtuvieron las raices {raiz}')
    for tol in tols:  
        retorno = steffensen(tol, x, cinco, "steffensen5")
        iteraciones = retorno[0]
        raiz = retorno[1]
        print(f'En {iteraciones} iteraciones y tolerancia de {tol} se obtuvieron las raices {Decimal(raiz)}')

    