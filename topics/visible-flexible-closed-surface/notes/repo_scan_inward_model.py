"""Inward-first counterpart of the repository's cycle/bridge BVP.

Only changes the finite profile and its breakpoints.  The endpoint Robin
condition is provisional linear data; this class supplies no compact tail.
The inherited full geometric ODE/BC/audit are used without linearizing them.
"""
import math
import numpy as np
from f6curve_inward_bvp import InwardPrefix
from f6curve_bidirectional_bridge import DirectionalBridge
from f6curve_outward_bridge_linear import BackwardLine
from f6curve_outward_bridge_bvp import OutwardTailBVP


class InwardCycleBridge(OutwardTailBVP):
    def __init__(self, port_data, modes=1, amplitude=.01, delta=.3,
                 vu=.7, vd=.8, eps=.3, cycles=1, angular=128, base_mode=2):
        if not 0 < delta < 1:
            raise ValueError('Inward excursion must lie in (0,1)')
        self.bridge = None
        self.port = None
        self.port_data = port_data
        InwardPrefix.__init__(self, modes, amplitude, delta/(1-delta), vu, vd,
                              eps, cycles, angular, base_mode, compute_stable=False)
        self.prefix_end = self.end
        self.bridge = DirectionalBridge(port_data['cut'])
        self.end = self.prefix_end+self.bridge.L
        self.sigma = self.bridge.sigma
        self.breaks = []
        for c in range(cycles):
            start = c*self.period
            self.breaks.extend(start+np.array([
                0., self.eps*self.Td, (1-self.eps)*self.Td, self.Td,
                self.Td+self.eps*self.Tu,
                self.Td+(1-self.eps)*self.Tu, self.period]))
        self.breaks = np.unique(np.r_[self.breaks, self.end])
        self.breakpoints = self.breaks.copy()
        self.linearD = np.asarray(port_data['linearSlope'][:modes])
        if len(self.linearD) != modes:
            raise ValueError('Not enough complete physical modes in linear port')
        self.linear = []
        self.rows = []
        r = port_data['cut']['radius']
        w = port_data['cut']['backgroundSlope']
        for m, D in zip(self.even, self.linearD):
            terminal = [self.sigma*w*(r*D-m*m)/(m*m-1), 1.]
            line = BackwardLine(lambda s,y:self.linear_rhs(s,y,int(m)),
                                self.breaks, terminal)
            self.linear.append(line)
            self.rows.append(dict(mode=int(m), physical_tail_D=float(D),
                rho=line.rho, terminal_g_over_core_g=line.gain,
                logscale=line.logscale))
        self.rhos = np.array([line.rho for line in self.linear])
        self.h0 = -1/(base_mode**2*self.rhos[0])
        if self.h0 <= 0:
            raise ValueError('Inward complete line has nonpositive core halfwidth')
        self.bcweights = np.maximum(self.bscale,1e-6)
        for row in self.rows:
            m = row['mode']
            rho = row['rho']
            direction = np.array([1.,0.]) if m%4 == 0 else np.array([-m*m*self.h0,1.])
            row['core_transversality'] = float(abs(direction[1]-rho*direction[0])/
                (np.linalg.norm(direction)*math.hypot(1,rho)))

    def profile(self, s):
        s = np.atleast_1d(s)
        if self.bridge is None:
            return InwardPrefix.profile(self,s)
        a,v,acc = InwardPrefix.profile(self,np.minimum(s,self.prefix_end))
        mask = s>self.prefix_end
        if np.any(mask):
            a[mask],v[mask],acc[mask] = self.bridge.profile(s[mask]-self.prefix_end)
        return a,v,acc

    def seed(self,nodes):
        x = np.unique(np.r_[np.linspace(0,self.prefix_end,nodes*self.cycles),
            np.linspace(self.prefix_end,self.end,max(61,nodes//2)),self.breaks])
        p = np.zeros(self.M)
        f,g = self.linear[0].sol(x)
        y = np.zeros((self.n,len(x)))
        y[1] = f
        y[self.M+1] = -f/self.base_mode
        y[self.iz] = g
        y += (self.initial(p)-y[:,0])[:,None]*np.maximum(0,1-x/(self.Td/2))[None,:]**3
        return x,y,p
