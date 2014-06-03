import numpy as np

class RD:
    @classmethod
    def next_concentration(cls, conc, reac, diff, dt, dx):
        next_conc = np.empty(conc.shape)
        for i in range(conc.size):
            if i == 0:
                next_conc[i] = conc[i] \
                               + 0.5 * dt / dx**2 \
                               * (diff[i+1] + diff[i]) * (conc[i+1] - conc[i]) \
                               + reac[i] * dt
            elif i == conc.size-1:
                next_conc[i] = 0
            else:
                next_conc[i] = conc[i] \
                               + 0.5 * dt / dx**2 \
                               * ((diff[i+1] + diff[i]) * (conc[i+1] - conc[i]) \
                               + (diff[i-1] + diff[i]) * (conc[i-1] - conc[i])) \
                               + reac[i] * dt
            if next_conc[i] < 0:
                next_conc[i] = 0
        return next_conc

    @classmethod
    def integrate(cls, n, conc, reac, diff, dt, dx):
        next_conc = conc
        for _ in range(n):
            next_conc = cls.next_concentration(next_conc, reac, diff, dt, dx)
        return next_conc
