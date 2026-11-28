"""Finite R704 central developed shoulder on its original material, with six true endpoint columns."""
from collections import Counter
from functools import lru_cache
import math

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

from r688_actual_r664_window_collars import mollifier_cdf, require_public, true_curvature
from r688_true_caps_and_reference_sections import D, W, sym_step


UNIT = np.eye(3)
TURN = np.pi / 3
LENGTH = .125 * TURN
ALPHA = .016
T0 = np.array([0., np.cos(ALPHA), np.sin(ALPHA)])
E2 = np.cross(UNIT[0], T0)
CENTERS = np.array([.20, .50, .80])
WIDTH = .01
CUTS = (.10, .19, .21, .49, .51, .79, .81, .90)


def about_x(phase):
    c, s = np.cos(phase), np.sin(phase)
    return np.array([[1., 0., 0.], [0., c, -s], [0., s, c]])


def integral(fn, left, right, order=64):
    if right == left:
        return np.asarray(fn(np.asarray([left])))[0]*0.
    x, w = gauss(order)
    h = (right-left)/2
    return h*np.tensordot(w, fn(left+h*(x+1)), axes=(0, 0))


@lru_cache(maxsize=6)
def gauss(order):
    return np.polynomial.legendre.leggauss(order)


def angle(y):
    return TURN*(y-.001)/.998


def speed(y):
    theta = angle(y)
    return np.hypot(np.cos(theta), np.cos(ALPHA)*np.sin(theta))


def source_k(y):
    return np.cos(ALPHA)*(8/.998)/speed(y)**3


def bump(x):
    inside = 1-x*x
    return np.where(inside > 0, np.exp(-1/np.maximum(inside, 1.e-300)), 0.)


def phase_center(lam, tight, count):
    # R693's real C_lam(0). Integrate only the nonconstant part of the left pulse.
    tol = 2.e-13 if tight else 1.e-11
    v0 = -.93
    state = np.array([0., v0, 0.])
    for v1 in (-.91, -.89, -.87, -.65, -.63, -.61, -.59):
        def rhs(v, ys):
            k = float(true_curvature(np.asarray(v), lam))
            return [k, np.cos(ys[0]), np.sin(ys[0])]
        sol = solve_ivp(rhs, (v0, v1), state, method='DOP853', rtol=tol, atol=tol*.01)
        count['centerline_rhs'] += sol.nfev
        if not sol.success:
            raise ArithmeticError(sol.message)
        state, v0 = sol.y[:, -1], v1
    extension = .59*np.array([np.cos(state[0]), np.sin(state[0])])
    return np.r_[0., state[1:]+extension], float(state[0])


class Rod:
    def __init__(self):
        require_public()
        self.count = Counter()
        # The native constants below fix the normalization used in all calls and stored controls.
        self.norm = np.array([self.bump_integral(c, 96) for c in CENTERS])
        self.norm_check = np.array([self.bump_integral(c, 160) for c in CENTERS])
        def projected_start(y):
            th = TURN*sym_step(y)
            return LENGTH*np.column_stack((np.cos(th), np.sin(th)))
        knots = (0., .0005, .0015, .10)
        self.start_xz = np.array([W+.001, D])+sum(
            integral(projected_start, l, r, 96) for l, r in zip(knots, knots[1:]))
        self.source_origin = self.source_frame(.10)[0].copy()

    @staticmethod
    def bump_integral(center, order):
        return float(integral(lambda x: WIDTH*LENGTH*bump(x)*speed(center+WIDTH*x), -1., 1., order))

    def source_frame(self, y):
        th, th0 = angle(y), angle(.10)
        radius = .125*.998
        x, zeta = self.start_xz+radius*np.array([np.sin(th)-np.sin(th0), np.cos(th0)-np.cos(th)])
        c = x*UNIT[0]+zeta*np.cos(ALPHA)*E2
        e = (np.cos(th)*UNIT[0]+np.sin(th)*np.cos(ALPHA)*E2)/speed(y)
        return np.array([c, e, T0, np.cross(e, T0)])

    def data(self, y, q):
        x = (y-CENTERS)/WIDTH
        vals = bump(x)/self.norm
        inn = abs(x)<1
        deriv = np.zeros(3)
        deriv[inn] = vals[inn]*(-2*x[inn])/(1-x[inn]**2)**2/(WIDTH*LENGTH*speed(y))
        k0 = source_k(y)
        th = angle(y)
        b = speed(y)
        b_l = -(np.sin(ALPHA)**2)*np.sin(th)*np.cos(th)*(8/.998)/b
        k0_t = -3*k0*b_l/b**2
        k, j = k0+vals@q[:3], vals@q[3:]
        dk, dj = k0_t+deriv@q[:3], deriv@q[3:]
        p = j/k
        pt = (dj-p*dk)/k
        return k, j, p, pt

    @lru_cache(maxsize=128)
    def static_point(self, arc, y):
        # Original upper curve beyond the controlled sub-arc, through all three R686 turns.
        turns = ((0.,TURN,LENGTH),(TURN,0.,LENGTH),(0.,-np.pi/2,.101*np.pi/2))
        if arc==0:
            return W+.001*y,D,0.,0.
        if arc==4:
            x,height,_,_=self.static_point(3,1.)
            return x,height*(1.-y),-np.pi/2,0.
        x,zeta,_,_=self.static_point(arc-1,1.)
        a,b,length=turns[arc-1]
        def tangent(t):
            ang=a+(b-a)*sym_step(t)
            return length*np.column_stack((np.cos(ang),np.sin(ang)))
        cuts=[0.]+[t for t in (.0005,.0015,.9985,.9995) if t<y]+[y]
        for lo,hi in zip(cuts,cuts[1:]):
            dx,dz=integral(tangent,lo,hi,96)
            x+=dx;zeta+=dz
        theta=a+(b-a)*sym_step(np.asarray(y))
        ds=(mollifier_cdf((np.asarray(y)-.001)/.0005)-mollifier_cdf((np.asarray(y)-.999)/.0005))/.998
        return float(x),float(zeta),float(theta),float((b-a)*ds/length)

    def rigid_seam(self, phase, sigma, arc, y, v):
        x,zeta,th,k=self.static_point(arc,y)
        X=x*UNIT[0]+zeta*UNIT[2]+v*T0
        e=np.cos(th)*UNIT[0]+np.sin(th)*UNIT[2]
        acc=k*(-np.sin(th)*UNIT[0]+np.cos(th)*UNIT[2])
        jets=np.array([X,e,T0,acc,np.zeros(3),np.zeros(3)])
        if arc==0 or (arc==1 and y<=.10):
            R=about_x(phase)
            jets=jets@R.T
            jets[0]+=D*UNIT[2]-R@(D*UNIT[2])
        else:
            jets[0]+=sigma*UNIT[0]
        return jets

    def endpoints(self, lam, sigma):
        R = about_x(lam)
        near = self.source_frame(.10)@R.T
        near[0] += D*UNIT[2]-R@(D*UNIT[2])
        far = self.source_frame(.90).copy()
        far[0] += sigma*UNIT[0]
        return near, far

    def integrate(self, lam, sigma, q, tight=False, columns=True, dense=False):
        near, target = self.endpoints(lam, sigma)
        state = np.r_[near.ravel(), np.zeros(36)] if columns else near.ravel()
        pieces = []
        tol = 4.e-14 if tight else 1.e-12
        self.count['rod_integrations'] += 1
        if columns:
            self.count['complete_six_column_integrations_started'] += 1
        for left, right in zip(CUTS, CUTS[1:]):
            def rhs(y, state):
                c, e, T, n = state[:12].reshape(4,3)
                B = bump((y-CENTERS)/WIDTH)/self.norm
                k, j = source_k(y)+B@q[:3], B@q[3:]
                primal = np.array([e, k*n, -j*n, -k*e+j*T])
                if not columns:
                    return LENGTH*speed(y)*primal.ravel()
                omega = -np.vstack((B[:,None]*T, B[:,None]*e))
                moment = np.cross(c-self.source_origin, omega)
                return LENGTH*speed(y)*np.r_[primal.ravel(), np.column_stack((omega,moment)).ravel()]
            sol = solve_ivp(rhs, (left,right), state, method='DOP853', rtol=tol, atol=.006*tol,
                            dense_output=dense, max_step=(right-left)/(5 if tight else 3))
            self.count['rod_rhs'] += sol.nfev
            if not sol.success:
                raise ArithmeticError(sol.message)
            state = sol.y[:,-1]
            if dense:
                pieces.append(sol.sol)
        end = state[:12].reshape(4,3)
        residual = (end-target).ravel()
        jac = None
        if columns:
            twist = state[12:].reshape(6,6)
            rot, tran = twist[:,:3], twist[:,3:]
            Jc = np.cross(rot,end[0]-self.source_origin)+tran
            jac = np.column_stack([Jc]+[np.cross(rot,w) for w in end[1:]]).T
            self.count['complete_six_column_integrations_finished'] += 1
        return dict(end=end, target=target, near=near, residual=residual, J=jac, solution=pieces)

    @lru_cache(maxsize=2048)
    def tcoord(self, y):
        return float(integral(speed,.10,y,48)*LENGTH)

    def seam(self, result, q, y, v):
        # y labels the original source l, not the new ruling foot.
        ref = self.source_frame(y)
        zeta = np.dot(ref[0], E2)/np.cos(ALPHA)
        z = v+zeta*np.sin(ALPHA)
        u = self.tcoord(y)
        def equation(t):
            return self.tcoord(t)+z*self.data(t,q)[2]-u
        foot = y if y in (.10,.90) else brentq(equation,.10,.90,xtol=5.e-15)
        idx = min(len(CUTS)-2,np.searchsorted(CUTS,foot,side='right')-1)
        c,e,T,n = result['solution'][idx](foot)[:12].reshape(4,3)
        k,j,p,pt = self.data(foot,q)
        den = 1+z*pt
        th = angle(y)
        b = speed(y)
        bp = -(np.sin(ALPHA)**2)*np.sin(th)*np.cos(th)*(8/.998)/b
        zl = np.sin(th)*np.sin(ALPHA)
        zll = np.cos(th)*np.sin(ALPHA)*(8/.998)
        u1 = b-p*zl
        X = c+z*(p*e+T)
        return np.array([X,b*e+zl*T,T,k/den*u1**2*n+bp*e+zll*T,
                         -k/den*p*u1*n,k/den*p*p*n]), [float(foot),float(den)]
