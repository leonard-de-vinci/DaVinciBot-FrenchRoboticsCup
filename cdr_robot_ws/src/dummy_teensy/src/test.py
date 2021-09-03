from scipy import signal
import numpy as np
import matplolib.pyplot as plt

def p(x):
        A=0.6093
        B = 2.794
        C = 99.69
        a = 1
        b = 30.04
        c = 390
        d = 2080
        return ((A*x*x)+(B*x)+C)/((a*x*x*x)+(b*x*x)+(c*x)+d)

num = [0.6093,2.794,99.69]
den = [1,30.04,390,2080]

tf = signal.TransferFunction(num, den,dt=0.01)

print(signal.impule)