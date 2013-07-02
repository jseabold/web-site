"""
Key for Homework 5.
"""

import numpy as np

def exp_growth(t, const=100, growth_rate=.1):
    """
    True solution
    """
    return const * np.exp(growth_rate * t)

def dPdt(P, t, growth_rate):
    return P*growth_rate

def euler(func, initial, ntime, dt, args=()):
    nsteps = int(ntime/dt)
    population = np.zeros(nsteps+1)
    population[0] = initial
    for i in range(1, len(population)):
        t = i * dt
        dP = func(population[i-1], t, *args)
        population[i] = population[i-1] + dP*dt
    return population


# 1.1

def relative_error(estimate, analytic):
    return np.abs(estimate - analytic)/np.abs(analytic)

# 1.2

def runge_kutta2(func, initial, ntime, dt, args=()):
    nsteps = int(ntime/dt)
    population = np.zeros(nsteps+1)
    population[0] = initial
    for i in range(1, len(population)):
        t = i * dt
        t1 = (i - 1) * dt # lagged t
        dP_euler = func(population[i-1], t1, *args)
        y_n = population[i-1] + dP_euler*dt
        dP = .5 * (dP_euler + func(y_n, t, *args))*dt
        population[i] = population[i-1] + dP
    return population

# 1.3

population1 = runge_kutta2(dPdt, 100, 100, 1, args=(.1,))
population2 = runge_kutta2(dPdt, 100, 100, .5, args=(.1,))
population3 = runge_kutta2(dPdt, 100, 100, .25, args=(.1,))

print "1.3"
print population1[-1]
print population2[-1]
print population3[-1]

print
print "1.4"
print "dt=1"
re1 = relative_error(population1[-1], exp_growth(100))
print re1
print "dt=.5"
re2 = relative_error(population2[-1], exp_growth(100))
print re2
print "dt=.25"
re3 = relative_error(population3[-1], exp_growth(100))
print re3

print
print "1.5"
print "Reduction 1 -> .5"
print re2/re1
print "Reduction .5 -> .25"
print re3/re2

def dPdt(P, t):
    return .5 * (1 - P/1000.)*P

P0 = 20.
dt = 2.

def exact_func(t):
    return 10/(.01+.49*np.exp(-.5*t))

pop1 = euler(dPdt, P0, 4, dt)

print
print "2.a"
print pop1[1]
print "2.b"
print pop1[2]
print "2.c"
print "%2.4f%%" % (relative_error(pop1[1], exact_func(2))*100)

pop2 = runge_kutta2(dPdt, P0, 4, dt)
print "3.a"
print pop2[1]
print "3.b"
print pop2[2]
print "3.c"
print "%2.4f%%" % (relative_error(pop2[1], exact_func(2))*100)

def runge_kutta4(func, initial, ntime, dt, args=()):
    nsteps = int(ntime/dt)
    population = np.zeros(nsteps + 1)
    population[0] = initial
    for i in range(1, len(population)):
        t = i * dt # current t
        t1 = (i - 1) * dt # lagged t
        pn1 = population[i-1] # lagged P
        d1 = func(pn1, t1)*dt
        d2 = func(pn1+.5*d1, t1+.5*dt)*dt
        d3 = func(pn1+.5*d2, t1+.5*dt)*dt
        d4 = func(pn1+d3, t1+dt)*dt
        population[i] = population[i-1] + (d1 + 2*d2 + 2*d3 + d4)/6.
    return population

pop3 = runge_kutta4(dPdt, P0, 4, dt)

print
print "4.a"
print pop3[1]
print "4.b"
print pop3[2]
print "4.c"
print "%2.4f%%" % (relative_error(pop3[1], exact_func(2))*100)
