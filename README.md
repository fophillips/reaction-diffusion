# reaction-diffusion

Simple 1-D reaction-diffusion equation solver in Python.

## Usage
Open up iPython with `ipython qtconsole --pylab=inline`

```python
In [1]: %run path/to/rd.py

In [2]: concentration = zeros(101) # concentrations are initially zero

In [3]: diffusivity = zeros(101) # initialise
   ...: diffusivity[:51] = 0.01 # low diffusion on bottom half
   ...: diffusivity[51:] = 1 # high diffusion on top half

In [4]: reaction = zeros(101) # no reaction anywhere...
   ...: reaction[50] = 1 # except a source at x=50

In [5]: dt = 0.1 # delta t
   ...: dx = 1 # delta x

In [6]: n = 10000 # number of timesteps

In [7]: new_conc = RD.integrate(n, reaction, diffusivity, concentration, dt, dx) # and wait a little bit

In [8]: plot(new_conc)
Out[8]: [<matplotlib.lines.Line2D at 0x1136fbf28>]
```
![RD](http://imgur.com/PuYemcA.png)
