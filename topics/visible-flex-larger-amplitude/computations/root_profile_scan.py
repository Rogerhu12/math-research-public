#!/usr/bin/env python3
"""Find low-height linear resonances for a planar core and a physical tail port.

This is a design screen, not a nonlinear solution, a closed surface, or a
reach certificate. A selected design must subsequently be solved at fixed g.
The two-component linear equation is the one recorded in the source topic's
notes/fixed_metric_mode3_flow.py, with an arbitrary base mode m >= 2.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import hashlib
import json
import math
import time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.optimize import brentq


def flat_ramp(u, eps, eta):
    u = np.asarray(u)
    up, down = u < eps, u > 1-eps
    t = np.clip(np.where(up, u/eps, (1-u)/eps), 0., 1.)
    z = np.minimum(t, 1-t)
    x = z/eta
    edge = z < eta
    f = np.where(edge, eta/(1-eta)*(x**3-x**4/2),
                 (z-eta/2)/(1-eta))
    primitive = np.where(edge, eta*eta/(1-eta)*(x**4/4-x**5/10),
                         (z*z/2-eta*z/2+.15*eta*eta)/(1-eta))
    derivative = np.where(edge, (3*x*x-2*x**3)/(1-eta), 1/(1-eta))
    F = np.where(t <= .5, f, 1-f)
    P = np.where(t <= .5, primitive, .5-(1-t)+primitive)
    return (np.where(up | down, F, 1.),
            np.where(up, eps*P, np.where(down, 1-eps-eps*P, u-eps/2)),
            np.where(up, derivative/eps, np.where(down, -derivative/eps, 0.)))


def linear_matrix(a, v, mode):
    b = np.sqrt(1-v*v)
    mm = mode*mode
    return np.array([[-(mm-1)*v, -mm*b],
                     [(mm-1)*v*v/b, mm*v]])/a


class Bridge:
    def __init__(self, cut, mode, slope):
        self.cut = cut
        self.sigma = -1
        self.pt = math.atan2(1., cut['backgroundSlope'])
        self.ps = cut['backgroundSecond']/(1+cut['backgroundSlope']**2)**1.5
        self.g, self.gw = np.polynomial.legendre.leggauss(64)
        def gap(L):
            return L*self.integral(np.array([1.]), L)[0] - (1-cut['radius'])
        grid = np.geomspace(1e-5, 10., 300)
        brackets = [(x,y) for x,y in zip(grid[:-1], grid[1:]) if gap(x)*gap(y) <= 0]
        if not brackets:
            raise ValueError('No positive bridge length found.')
        self.L = brentq(gap, *brackets[0], xtol=2e-14)
        c2=3*self.pt-self.L*self.ps;c3=-2*self.pt+self.L*self.ps
        critical=-2*c2/(3*c3) if c3 else -1.
        maximum=max(self.pt,c2*critical**2+c3*critical**3 if 0<critical<1 else 0.)
        if maximum>=math.pi/2:
            raise ValueError('Cubic bridge crosses the positive-binormal chart boundary')
        w, r = cut['backgroundSlope'], cut['radius']
        terminal = np.array([-w*(r*slope-mode*mode)/(mode*mode-1), 1.])
        terminal /= np.linalg.norm(terminal)
        self.mode = mode
        self.solution = solve_ivp(lambda s,y: linear_matrix(*self.profile(s)[:2], mode)@y,
                                  (self.L,0.), terminal, method='DOP853',
                                  rtol=2e-11, atol=2e-13, dense_output=True,
                                  max_step=self.L/80)
        if not self.solution.success:
            raise RuntimeError(self.solution.message)
        self.initial = self.solution.y[:,-1]
        self.initial /= np.linalg.norm(self.initial)

    def turn(self, t, L=None):
        L = self.L if L is None else L
        return (self.pt*(3*t*t-2*t**3)+L*self.ps*(t**3-t*t),
                (self.pt*(6*t-6*t*t)+L*self.ps*(3*t*t-2*t))/L)

    def integral(self, t, L=None):
        t = np.atleast_1d(t)
        phi, _ = self.turn(t[:,None]*(1+self.g[None,:])/2, L)
        return t/2*(np.sin(phi)@self.gw)

    def profile(self, s):
        t = np.asarray(s)/self.L
        phi, dphi = self.turn(t)
        aa = 1-self.L*self.integral(t)
        if np.ndim(s) == 0:
            aa = float(aa[0])
        return aa, -np.sin(phi), -np.cos(phi)*dphi


class Design:
    def __init__(self, cfg, bridge):
        self.cfg, self.bridge = cfg, bridge
        self.delta, self.vu, self.vd = cfg['delta'], cfg['vu'], cfg['vd']
        self.eps, self.eta = cfg['ramp'], cfg['ramp_eta']
        self.Tu = self.delta/(self.vu*(1-self.eps))
        self.Td = self.delta/(self.vd*(1-self.eps))
        self.period = self.Tu+self.Td
        self.end = self.period*cfg['cycles']+bridge.L

    def stage(self, u, upward):
        w, primitive, wp = flat_ramp(u, self.eps, self.eta)
        vv = self.vu if upward else self.vd
        length = self.Tu if upward else self.Td
        start = 1. if upward else 1+self.delta
        sign = 1 if upward else -1
        return start+sign*self.delta*primitive/(1-self.eps), sign*vv*w, sign*vv*wp/length

    def core_line(self, dense=False, rtol=3e-9):
        y = self.bridge.initial.copy()
        segments = []
        for cycle in reversed(range(self.cfg['cycles'])):
            for upward in (False,True):
                length = self.Tu if upward else self.Td
                def fun(u,z):
                    aa,vv,_ = self.stage(u,upward)
                    return length*(linear_matrix(float(aa),float(vv),self.bridge.mode)@z)
                sol = solve_ivp(fun, (1.,0.), y, method='DOP853', rtol=rtol,
                                atol=rtol/100, max_step=.055, dense_output=dense)
                if not sol.success:
                    raise RuntimeError(sol.message)
                if dense:
                    segments.append((cycle,upward,sol))
                y = sol.y[:,-1]
                if not np.all(np.isfinite(y)):
                    raise ArithmeticError('Nonfinite projective transport.')
                if not dense:
                    y /= np.linalg.norm(y)
        return y, segments

    def summary(self):
        y0, segments = self.core_line(dense=True)
        rows = []
        total_height = 0.
        for cycle,upward,sol in reversed(segments):
            length = self.Tu if upward else self.Td
            u = np.linspace(0.,1.,401)
            aa,vv,acc = self.stage(u,upward)
            h = total_height+cumulative_trapezoid(np.sqrt(1-vv*vv),u*length,initial=0.)
            f,g = sol.sol(u)/y0[0]
            rows.append((aa,vv,acc,h,f,g))
            total_height = float(h[-1])
        s = np.linspace(0.,self.bridge.L,501)
        aa,vv,acc = self.bridge.profile(s)
        h = total_height+cumulative_trapezoid(np.sqrt(1-vv*vv),s,initial=0.)
        # Match the normalization used at the prefix/bridge interface.
        original = self.bridge.solution.sol(np.array([0.]))[:,0]
        ratio = float(np.dot(original,self.bridge.initial))
        f,g = self.bridge.solution.sol(s)/ratio/y0[0]
        rows.append((aa,vv,acc,h,f,g))
        a,v,acc,h,f,g = (np.concatenate([r[i] for r in rows]) for i in range(6))
        b=np.sqrt(1-v*v)
        kappa=float(np.max(np.maximum(abs(acc)/b,b/a)))
        budgets=[]
        for q in (.1,.2,.28,.32,.38,.42):
            # Only a first-order embedding proxy. In particular it does not
            # turn this linear trial into an exact isometric immersion.
            r2=np.maximum((a+q*f)**2+(h+q*g)**2,(a-q*f)**2+(h-q*g)**2)
            diam=2*math.sqrt(float(r2.max()))
            budgets.append(dict(q=q,linear_ball_D=diam,linear_core_gap_over_D=2*q/diam,
                                background_kappa_times_D=kappa*diam))
        return dict(config=self.cfg,mode=self.bridge.mode,linear_core_g_over_f=float(y0[1]/y0[0]),
                    meridian_length=self.end,background_height=float(h[-1]),
                    background_kappa_sample=kappa,linear_tail_height_gain=float(g[-1]),
                    linear_f_max=float(abs(f).max()),linear_g_max=float(abs(g).max()),
                    budgets=budgets)


def parse_port(d, mode):
    if 'linearSlope' in d:
        cut=d['cut']; modes=d['modes']; slope=d['linearSlope'][modes.index(mode)]
    else:
        c=d['cut'];cut=dict(radius=c['r'],backgroundSlope=c['w'],backgroundSecond=c['wr'])
        slope=next(r['slope'] for r in d['rows'] if r['mode']==mode)
    return cut,float(slope)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--port',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--mode',type=int,default=2)
    p.add_argument('--quick',action='store_true')
    p.add_argument('--vu',type=float,nargs='+')
    p.add_argument('--vd',type=float,nargs='+')
    p.add_argument('--ramp',type=float,nargs='+',default=[.4])
    a=p.parse_args()
    data=json.loads(a.port.read_text());cut,slope=parse_port(data,a.mode)
    bridge=Bridge(cut,a.mode,slope)
    vu=a.vu or ([.17,.3,.45] if a.quick else [.12,.17,.22,.28,.35,.43,.52,.62,.72])
    vd=a.vd or ([.18,.35,.5] if a.quick else [.15,.18,.24,.32,.42,.55,.68,.8])
    values=[.006,.012,.022,.04,.065,.1,.15,.23,.34,.5,.75]
    report=dict(scope=__doc__,port=str(a.port),port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest(),
                mode=a.mode,cut=cut,slope=slope,bridge_length=bridge.L,rows=[])
    start=time.time();a.out.parent.mkdir(parents=True,exist_ok=True)
    for eps in a.ramp:
        for u in vu:
            for v in vd:
                cfg=dict(direction='outward',vu=u,vd=v,ramp=eps,ramp_eta=.05,cycles=1)
                def scalar(delta):
                    return float(Design({**cfg,'delta':delta},bridge).core_line()[0][1])
                prev=None;roots=[];errors=[]
                for delta in values:
                    try:
                        value=scalar(delta)
                        if prev is not None and value*prev[1]<0:
                            root=brentq(scalar,prev[0],delta,xtol=3e-10)
                            roots.append(Design({**cfg,'delta':root},bridge).summary())
                        prev=delta,value
                    except Exception as exc:
                        errors.append(dict(delta=delta,error=repr(exc)));prev=None
                report['rows'].append(dict(config=cfg,roots=roots,errors=errors))
                report['seconds']=time.time()-start
                a.out.write_text(json.dumps(report,indent=2)+'\n')
                print(json.dumps(dict(config=cfg,roots=[dict(delta=r['config']['delta'],
                  height=r['background_height'],gain=r['linear_tail_height_gain'],
                  q38=r['budgets'][4]) for r in roots],seconds=report['seconds'])),flush=True)


if __name__=='__main__':
    main()
