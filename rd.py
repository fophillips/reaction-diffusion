import numpy as np

class RD:
    def __init__(self, reaction, diffusivities, dt, dx):
        self.reaction = reaction
        self.diff = diffusivities
        self.dt = dt
        self.dx = dx
        
    def next_concentrations(self, conc):
        next_conc = np.empty(conc.shape)
        for i in range(conc.size):
            if(i == 0):
                next_conc[i] = conc[i] \
                               + 0.5 * self.dt / self.dx**2 \
                               * (self.diff[i+1] + self.diff[i]) * (conc[i+1] - conc[i]) \
                               + self.reaction[i] * self.dt
            elif(i == conc.size-1):
                next_conc[i] = 0
            else:
                next_conc[i] = conc[i] \
                               + 0.5 * self.dt / self.dx**2 \
                               * ((self.diff[i+1] + self.diff[i]) * (conc[i+1] - conc[i]) \
                               + (self.diff[i-1] + self.diff[i]) * (conc[i-1] - conc[i])) \
                               + self.reaction[i] * self.dt
            if next_conc[i] < 0:
                next_conc[i] = 0
        return next_conc

    def n_timesteps(self, conc, n):
        next_conc = conc
        for _ in range(n):
            next_conc = self.next_concentrations(next_conc)
        return next_conc
