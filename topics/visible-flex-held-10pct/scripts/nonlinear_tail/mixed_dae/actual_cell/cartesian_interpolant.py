"""Actual Cartesian two-jets of the explicitly interpolated angular map.

Radial differentiation uses second-order forward algebra, not the Darboux
equation. Background w_rr is supplied separately with its numerical audit.
The angular primitive is the same centered discrete Fourier primitive as the
archived development. This is a finite interpolation audit, not a C2 proof.
"""
import numpy as np


class Jet2:
    __array_priority__ = 1000
    def __init__(self, value, first=0., second=0.):
        self.v, self.d, self.dd = [np.asarray(a, float) for a in (value, first, second)]

    @staticmethod
    def cast(value):
        return value if isinstance(value, Jet2) else Jet2(value)

    def __add__(self, value):
        value = self.cast(value)
        return Jet2(self.v+value.v, self.d+value.d, self.dd+value.dd)
    __radd__ = __add__

    def __neg__(self):
        return Jet2(-self.v, -self.d, -self.dd)

    def __sub__(self, value):
        return self+-self.cast(value)

    def __rsub__(self, value):
        return self.cast(value)+-self

    def __mul__(self, value):
        value = self.cast(value)
        return Jet2(self.v*value.v, self.d*value.v+self.v*value.d,
                    self.dd*value.v+2*self.d*value.d+self.v*value.dd)
    __rmul__ = __mul__

    def reciprocal(self):
        return Jet2(1/self.v, -self.d/self.v**2, 2*self.d**2/self.v**3-self.dd/self.v**2)

    def __truediv__(self, value):
        return self*self.cast(value).reciprocal()

    def __rtruediv__(self, value):
        return self.cast(value)*self.reciprocal()

    def sqrt(self):
        q = np.sqrt(self.v)
        return Jet2(q, self.d/(2*q), self.dd/(2*q)-self.d*self.d/(4*q**3))

    def sin(self):
        s, c = np.sin(self.v), np.cos(self.v)
        return Jet2(s, c*self.d, c*self.dd-s*self.d*self.d)


def periodic_operator(value, derivative=0):
    value = np.asarray(value)
    n = len(value)
    k = np.fft.fftfreq(n)*n
    q = np.fft.fft(value)
    q[0] = 0.
    if n % 2 == 0:
        q[n//2] = 0.
    if derivative:
        q *= 1j*k
    else:
        q[1:] /= 1j*k[1:]
    return np.fft.ifft(q).real


def primitive_jet(value):
    return Jet2(*(periodic_operator(v) for v in (value.v, value.d, value.dd)))


def cartesian_jets(fields, Y, vr, vrr, Lr, Lrr, r, w, wr, wrr):
    d, N = fields.d, fields.angular
    v, L = Y[:d], Y[2*d:]
    u = 2*np.pi*np.arange(N)/N
    P = Jet2(v@fields.dphi, vr@fields.dphi, vrr@fields.dphi)
    Pt = Jet2(v@fields.ddphi, vr@fields.ddphi, vrr@fields.ddphi)
    Lv = Jet2(L@fields.Phi, Lr@fields.Phi, Lrr@fields.Phi)
    R, W = Jet2(r, 1., 0.), Jet2(w, wr, wrr)
    W2 = W*W
    E = 1+W2
    K = Lv-Pt
    T = 2*K+K*K+E*P*P
    q = W2*T
    D, S = 1-q, 1-W2*P*P
    sd, sqrtS = D.sqrt(), S.sqrt()
    fc = q*(2+sd)/(2*sd*(1+sd)*(1+sd))
    gc = W2*(P*P+S*T/(1+sd))/(S*sd)
    quad = .5*(K*K+E*P*P)+K*Pt+T*fc+(1+K)*Pt*gc
    omega_correction = W2*(Lv+quad)
    phase = primitive_jet(omega_correction)
    sp = phase.sin()
    halfsin = (phase*.5).sin()
    cpminus = -2*halfsin*halfsin
    ds, dc = np.sin(u)*cpminus+np.cos(u)*sp, np.cos(u)*cpminus-np.sin(u)*sp
    rho = R*sqrtS
    drho = -R*W2*P*P/(1+sqrtS)
    dxT, dyT = -np.sin(u)*drho-rho*ds, np.cos(u)*drho+rho*dc
    dx, dy = primitive_jet(dxT), primitive_jet(dyT)
    shape = Jet2(v@fields.phi, vr@fields.phi, vrr@fields.phi)
    height = R*W*shape
    # The background height is separated. Its perturbation mean has derivative
    # w*L0 and second derivative wr*L0+w*L0_r, without assuming Gauss.
    mean_first, mean_second = w*L[0], wr*L[0]+w*Lr[0]
    V = np.c_[dx.v, dy.v, height.v]
    Vr = np.c_[dx.d, dy.d, height.d+mean_first]
    Vt = np.c_[dxT.v-dxT.v.mean(), dyT.v-dyT.v.mean(), r*w*P.v]
    Vrr = np.c_[dx.dd, dy.dd, height.dd+mean_second]
    Vrt = np.c_[dxT.d-dxT.d.mean(), dyT.d-dyT.d.mean(), (w+r*wr)*P.v+r*w*P.d]
    Vtt = np.c_[periodic_operator(dxT.v, 1), periodic_operator(dyT.v, 1), r*w*Pt.v]
    return np.stack([V, Vr, Vt, Vrr, Vrt, Vtt], axis=1), dict(
        angular_holonomy=float(abs(omega_correction.v.mean())),
        translation_period=float(2*np.pi*np.hypot(dxT.v.mean(), dyT.v.mean())),
        minimum_D=float(np.min(D.v)), minimum_S=float(np.min(S.v)))


def relative_geometry(jets, r, w, wr):
    n = jets.shape[0]
    u = 2*np.pi*np.arange(n)/n
    c, s = np.cos(u), np.sin(u)
    E = 1+w*w
    sqE = np.sqrt(E)
    Ep, Kg = 2*w*wr, w*wr/(r*E*E)
    Vr, Vt, Vrr, Vrt, Vtt = [jets[:, j] for j in range(1,6)]
    U0 = np.c_[c/sqE, s/sqE, np.full(n, w/sqE)]
    V0 = np.c_[-s, c, np.zeros(n)]
    H10 = np.c_[-w*wr*c/E**2, -w*wr*s/E**2, np.full(n, wr/E**2)]
    H30 = np.c_[-w*w*c/(E*r), -w*w*s/(E*r), np.full(n, w/(E*r))]
    dU, dV = Vr/sqE, Vt/r
    dH1 = (Vrr-Ep*Vr/(2*E))/E
    dH2 = (Vrt-Vt/r)/(r*sqE)
    dH3 = Vtt/(r*r)+Vr/(E*r)
    dot = lambda a,b:np.sum(a*b,axis=1)
    outer = lambda a,b:np.einsum('ni,nj->nij',a,b)
    A, B, C = 2*dot(U0,dU)+dot(dU,dU), dot(U0,dV)+dot(V0,dU)+dot(dU,dV), 2*dot(V0,dV)+dot(dV,dV)
    tensor = .5*(outer(H10,dH3)+outer(dH3,H10)+outer(dH1,H30)+outer(H30,dH1)+outer(dH1,dH3)+outer(dH3,dH1))-outer(dH2,dH2)
    tensor += Kg*(outer(U0,dU)+outer(dU,U0)+outer(dU,dU)+outer(V0,dV)+outer(dV,V0)+outer(dV,dV))
    cross = np.cross(U0+dU,V0+dV)
    area = np.linalg.norm(cross,axis=1)
    normal = cross/area[:,None]
    b11, b12, b22 = dot(normal,H10+dH1), dot(normal,dH2), dot(normal,H30+dH3)
    detG, detB = area*area, b11*b22-b12*b12
    tr = (1+C)*b11+(1+A)*b22-2*B*b12
    curvature = (abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*detG*detB)))/(2*detG)
    return dict(metric_error=float(np.max(.5*(abs(A+C)+np.hypot(A-C,2*B)))),
                full_tensor_defect=float(np.max(np.linalg.norm(tensor,axis=(1,2)))),
                actual_gauss_difference=float(np.max(abs(detB/detG-Kg))),
                actual_curvature=float(np.max(curvature)),minimum_normalized_area=float(np.min(area)))
