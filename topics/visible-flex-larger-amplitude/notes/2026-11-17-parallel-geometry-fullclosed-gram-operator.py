#!/usr/bin/env python3
"""C2 quintic + analytic material-circle lift, angle-value Gram operator.

No nonlinear solver, no Pr-CU inverse, and no finite-spectrum completeness
claim.  All scalar values, the physical mesh, R, and width are fixed inputs.
The caller must bind their precise Hold/oracle identities.  This module's
binary64 evaluations are not continuous/interval geometry certificates.

Free coordinates: c[K:], A0_XY, every interior (Y,U,A), Hcap.  The exact
affine field definition imposes the core support curve, U0=ez, A0_Z=0,
and all three terminal residual jets zero.  Y/U/A describe the residual q;
the full physical field is q + the untruncated analytic lift.
"""
from dataclasses import dataclass
import numpy as np


@dataclass
class Prepared:
    jets: np.ndarray
    height: object
    core: np.ndarray
    rho: np.ndarray
    rho_phi: np.ndarray
    delta: np.ndarray
    er: np.ndarray
    et: np.ndarray


class ClosedGram:
    """Actual shared-quintic nodes/midpoints and all N angular values.

    residual() returns shape (2*J-1,N,3), ordered (ss,sphi,phiphi).
    jvp()/vjp() are the exact derivatives/transposes of those finite node
    evaluations in exact arithmetic.  Frobenius (1,2,1), quadrature, or
    optimization weights are deliberately external and must be applied to
    the forward and adjoint consistently.
    """

    def __init__(self, mesh, a_at_nodes_mid, radius, fixed_core_first,
                 *, M=160, N=2048, width=0.05):
        self.M, self.N = int(M), int(N)
        self.n = 3*self.M+2
        self.mesh = np.array(mesh, dtype=float, copy=True)
        self.a = np.array(a_at_nodes_mid, dtype=float, copy=True)
        self.fixed_core = np.array(fixed_core_first, dtype=float, copy=True)
        self.K = len(self.fixed_core)
        self.J = len(self.mesh)
        self.S, self.R, self.width = float(self.mesh[-1]), float(radius), float(width)
        if (self.M < 1 or self.N < 2 or not 0 <= self.K <= self.M or self.J < 2
                or self.mesh[0] != 0. or not np.all(np.diff(self.mesh) > 0)
                or not np.isfinite(self.mesh).all()
                or not np.isfinite(self.fixed_core).all()
                or not np.isfinite([self.R, self.width]).all()
                or not 0 < self.width < self.S or self.R <= 0):
            raise ValueError('Invalid frozen field-space inputs')
        self.P = 2*self.J-1
        if self.a.shape != (self.P,) or not np.isfinite(self.a).all() or not np.all(self.a > 0):
            raise ValueError('Need positive fixed a at every node and actual midpoint')
        if self.a[0] != 1. or self.a[-1] != self.R:
            raise ValueError('Scalar sample endpoints must use the same literal 1/R carriers')
        self.times = np.empty(self.P)
        self.times[::2] = self.mesh
        self.times[1::2] = self.mesh[:-1]+np.diff(self.mesh)/2
        self.freq = 2.*np.arange(1,self.M+1)
        self.qfreq = 1.-self.freq*self.freq
        self.phi = 2*np.pi*np.arange(self.N)/self.N
        self.cos = np.column_stack((np.ones(self.N), np.cos(self.phi[:,None]*self.freq)))
        self.sin = np.sin(self.phi[:,None]*self.freq)
        self.free_size = (self.M-self.K)+(2*self.M+1)+3*(self.J-2)*self.n+1
        self.lift_scalar = np.array([self._lift_scalar(float(s)) for s in self.times])
        self.mid_weights = [self._mid_weights(float(h)) for h in np.diff(self.mesh)]

    def _lift_scalar(self, s):
        if s <= self.S-self.width:
            chi, cp, cpp = 0., 0., 0.
        elif s >= self.S:
            chi, cp, cpp = 1., 0., 0.
        else:
            u = (s-self.S+self.width)/self.width
            chi = u*u*u*(10+u*(-15+6*u))
            cp = 30*u*u*(1-u)*(1-u)/self.width
            cpp = 60*u*(1-u)*(1-2*u)/(self.width*self.width)
        # Preserve the literal terminal R carrier when s is exactly S.
        b = self.R+(self.S-s)
        return chi, cp, cpp, chi*b, cp*b-chi, cpp*b-2*cp

    @staticmethod
    def _mid_weights(h):
        # Endpoint order (Yleft,Uleft,Aleft,Yright,Uright,Aright).
        return np.array([[.5,5*h/32,h*h/64,.5,-5*h/32,h*h/64],
                         [-15/(8*h),-7/16,-h/32,15/(8*h),-7/16,h/32],
                         [0.,-3/(2*h),-.25,0.,3/(2*h),-.25]])

    def unpack(self, x, *, tangent=False):
        x = np.asarray(x)
        if x.shape != (self.free_size,):
            raise ValueError('Wrong free-coordinate shape')
        dtype = np.result_type(x.dtype,float)
        jets = np.zeros((self.J,3,self.n),dtype=dtype)
        c = np.zeros(self.M,dtype=dtype)
        if not tangent:
            c[:self.K] = self.fixed_core
            jets[0,0,0] = 1.
            jets[0,1,2*self.M+1] = 1.
        at = self.M-self.K
        c[self.K:] = x[:at]
        jets[0,0,1:self.M+1] = c
        jets[0,0,self.M+1:2*self.M+1] = -self.freq*c
        jets[0,2,:2*self.M+1] = x[at:at+2*self.M+1]
        at += 2*self.M+1
        count = 3*(self.J-2)*self.n
        jets[1:-1] = x[at:at+count].reshape((self.J-2,3,self.n))
        return jets, x[-1], c

    def pack(self, jets, height, *, require_affine=True):
        """Encode a seed; no silent projection if require_affine is True.

        With False, returns the explicit new affine candidate coordinates
        and the complete max/RMS projection differences for each jet.
        The original supplied arrays are never modified.
        """
        jets = np.asarray(jets)
        if jets.shape != (self.J,3,self.n):
            raise ValueError('Wrong residual-jet shape')
        x = np.concatenate((jets[0,0,1+self.K:self.M+1],
                            jets[0,2,:2*self.M+1],jets[1:-1].ravel(),
                            np.asarray([height])))
        projected, _, _ = self.unpack(x)
        delta = projected-jets
        info = dict(exact_affine_input=bool(np.array_equal(projected,jets)),
                    per_jet_max=np.max(np.abs(delta),axis=(0,2)).tolist(),
                    per_jet_rms=np.sqrt(np.mean(np.abs(delta)**2,axis=(0,2))).tolist())
        if require_affine and not info['exact_affine_input']:
            raise ValueError('Seed is outside the exact affine space; declare its projection explicitly: '+str(info))
        return x, info

    def _free_adjoint(self, g, gh):
        core = g[0,0,1:self.M+1]-self.freq*g[0,0,self.M+1:2*self.M+1]
        return np.concatenate((core[self.K:],g[0,2,:2*self.M+1],
                               g[1:-1].ravel(),np.asarray([gh])))

    def prepare(self, x):
        jets, height, core = self.unpack(x)
        rho = 1+self.cos[:,1:]@(self.qfreq*core)
        rho_phi = -self.sin@(self.freq*self.qfreq*core)
        delta = self.sin@((self.qfreq/self.freq)*core)
        co, si = np.cos(delta), np.sin(delta)
        zeros = np.zeros_like(co)
        return Prepared(jets,height,core,rho,rho_phi,delta,
                        np.column_stack((co,si,zeros)),
                        np.column_stack((-si,co,zeros)))

    def synth(self, y):
        M = self.M
        return np.column_stack((self.cos@y[:M+1],
                                self.sin@y[M+1:2*M+1],
                                self.cos@y[2*M+1:]))

    def synth_t(self, g):
        return np.concatenate((self.cos.T@g[:,0],self.sin.T@g[:,1],self.cos.T@g[:,2]))

    def angular(self, y, *, order=1):
        M, nu = self.M, self.freq
        r,t,z = y[:M+1],y[M+1:2*M+1],y[2*M+1:]
        R,T,Z = self.cos@r,self.sin@t,self.cos@z
        Rp,Tp,Zp = -self.sin@(nu*r[1:]),self.cos[:,1:]@(nu*t),-self.sin@(nu*z[1:])
        if order == 1:
            return np.column_stack((Rp-T,Tp+R,Zp))
        if order == 2:
            Rpp = -self.cos[:,1:]@(nu*nu*r[1:])
            Tpp = -self.sin@(nu*nu*t)
            Zpp = -self.cos[:,1:]@(nu*nu*z[1:])
            return np.column_stack((Rpp-2*Tp-R,Tpp+2*Rp-T,Zpp))
        raise ValueError('Only actual first/two angular derivatives are defined')

    def angular_t(self, g):
        M,nu = self.M,self.freq
        r = self.cos.T@g[:,1]
        r[1:] -= nu*(self.sin.T@g[:,0])
        t = -self.sin.T@g[:,0]+nu*(self.cos[:,1:].T@g[:,1])
        z = np.zeros(M+1,dtype=np.result_type(g.dtype,float))
        z[1:] = -nu*(self.sin.T@g[:,2])
        return np.concatenate((r,t,z))

    def stage_jets(self, jets, stage):
        if stage % 2 == 0:
            return jets[stage//2]
        i = stage//2
        return self.mid_weights[i]@jets[i:i+2].reshape((6,self.n))

    def _stage_adjoint(self, grad, stage, gy, gu):
        if stage % 2 == 0:
            grad[stage//2,0] += gy
            grad[stage//2,1] += gu
        else:
            i = stage//2
            b0,b1,_ = self.mid_weights[i]
            grad[i:i+2] += (b0[:,None]*gy+b1[:,None]*gu).reshape((2,3,self.n))

    def _first(self, p, stage):
        y,u,_ = self.stage_jets(p.jets,stage)
        chi,cp,cpp,f,fp,fpp = self.lift_scalar[stage]
        V = self.synth(u)+fp*p.er
        V[:,2] += cp*p.height
        d = self.angular(y)+f*p.rho[:,None]*p.et
        return V,d

    def six_jets(self, p, stage):
        """All physical jets in the rotating-phi orthonormal frame.

        The angular derivatives already contain the frame connection.
        Do not differentiate these component arrays as Cartesian arrays.
        """
        y,u,acc = self.stage_jets(p.jets,stage)
        chi,cp,cpp,f,fp,fpp = self.lift_scalar[stage]
        F = self.synth(y)+f*p.er
        F[:,2] += chi*p.height
        Fs = self.synth(u)+fp*p.er
        Fs[:,2] += cp*p.height
        Fss = self.synth(acc)+fpp*p.er
        Fss[:,2] += cpp*p.height
        Fphi = self.angular(y)+f*p.rho[:,None]*p.et
        Fsphi = self.angular(u)+fp*p.rho[:,None]*p.et
        Fphiphi = self.angular(y,order=2)+f*(p.rho_phi[:,None]*p.et-p.rho[:,None]**2*p.er)
        return dict(F=F,Fs=Fs,Fss=Fss,Fphi=Fphi,Fsphi=Fsphi,Fphiphi=Fphiphi)

    @staticmethod
    def dot(a,b):
        # Bilinear, so complex-step is the analytic continuation of the
        # real Euclidean squared norm, not a conjugate/Hermitian extension.
        return np.sum(a*b,axis=1)

    def residual(self, x):
        p = self.prepare(x)
        result = np.empty((self.P,self.N,3),dtype=np.result_type(p.jets.dtype,float))
        with np.errstate(over='raise',invalid='raise',divide='raise'):
            for j,a in enumerate(self.a):
                V,d = self._first(p,j)
                ar = a*p.rho
                result[j,:,0] = self.dot(V,V)-1
                result[j,:,1] = self.dot(V,d)/ar
                result[j,:,2] = self.dot(d,d)/(ar*ar)-1
        return result

    def jvp(self, x, direction):
        p = self.prepare(x)
        djets,dH,dc = self.unpack(direction,tangent=True)
        drho = self.cos[:,1:]@(self.qfreq*dc)
        dtheta = self.sin@((self.qfreq/self.freq)*dc)
        result = np.empty((self.P,self.N,3),dtype=np.result_type(p.jets.dtype,djets.dtype,float))
        with np.errstate(over='raise',invalid='raise',divide='raise'):
            for j,a in enumerate(self.a):
                dy,du,_ = self.stage_jets(djets,j)
                _,cp,_,f,fp,_ = self.lift_scalar[j]
                V,d = self._first(p,j)
                dV = self.synth(du)+fp*dtheta[:,None]*p.et
                dV[:,2] += cp*dH
                dd = self.angular(dy)+f*(drho[:,None]*p.et-(p.rho*dtheta)[:,None]*p.er)
                ar = a*p.rho
                result[j,:,0] = 2*self.dot(V,dV)
                result[j,:,1] = (self.dot(d,dV)+self.dot(V,dd))/ar-self.dot(V,d)*drho/(a*p.rho**2)
                result[j,:,2] = 2*self.dot(d,dd)/(ar*ar)-2*self.dot(d,d)*drho/(a*a*p.rho**3)
        return result

    def vjp(self, x, weights):
        p = self.prepare(x)
        weights = np.asarray(weights)
        if weights.size != self.P*self.N*3:
            raise ValueError('Adjoint needs every stage/angle/residual value')
        weights = weights.reshape((self.P,self.N,3))
        dtype = np.result_type(p.jets.dtype,weights.dtype,float)
        grad = np.zeros(p.jets.shape,dtype=dtype)
        gc = np.zeros(self.M,dtype=dtype)
        gh = np.zeros((),dtype=dtype)
        with np.errstate(over='raise',invalid='raise',divide='raise'):
            for j,a in enumerate(self.a):
                V,d = self._first(p,j)
                w0,w1,w2 = weights[j].T
                ar = a*p.rho
                gV = 2*w0[:,None]*V+(w1/ar)[:,None]*d
                gd = (w1/ar)[:,None]*V+(2*w2/(ar*ar))[:,None]*d
                grho = -w1*self.dot(V,d)/(a*p.rho**2)-2*w2*self.dot(d,d)/(a*a*p.rho**3)
                self._stage_adjoint(grad,j,self.angular_t(gd),self.synth_t(gV))
                _,cp,_,f,fp,_ = self.lift_scalar[j]
                theta_weight = fp*self.dot(gV,p.et)-f*p.rho*self.dot(gd,p.er)
                rho_weight = f*self.dot(gd,p.et)+grho
                gc += (self.qfreq/self.freq)*(self.sin.T@theta_weight)+self.qfreq*(self.cos[:,1:].T@rho_weight)
                gh += cp*np.sum(gV[:,2])
        grad[0,0,1:self.M+1] += gc
        return self._free_adjoint(grad,gh)

    def affine_diagnostics(self, x):
        """Literal structural facts, not a geometry/domain certification."""
        p = self.prepare(x)
        jets = p.jets
        expected_u = np.zeros(self.n);expected_u[2*self.M+1] = 1.
        core_t = jets[0,0,self.M+1:2*self.M+1]
        return dict(core_position_Z_exact_zero=bool(np.all(jets[0,0,2*self.M+1:]==0)),
                    core_U_exact_ez=bool(np.array_equal(jets[0,1],expected_u)),
                    core_A_Z_exact_zero=bool(np.all(jets[0,2,2*self.M+1:]==0)),
                    core_T_exact_formula=bool(np.array_equal(core_t,-self.freq*p.core)),
                    terminal_residual_three_jets_exact_zero=bool(np.all(jets[-1]==0)),
                    lift_core_three_jets_exact_zero=bool(np.all(self.lift_scalar[0]==0)),
                    lift_terminal_radial_three_jets=self.lift_scalar[-1,3:].tolist(),
                    free_variables=self.free_size,full_angular_residual_values=self.P*self.N*3,
                    finite_spectrum_completeness_claimed=False,
                    continuous_geometry_certified=False,nonlinear_solve_executed=False)


if __name__ == '__main__':
    raise SystemExit('Import-only operator: an identity-bound actual warm/scalar bundle is required; no synthetic scientific probe or solve is launched.')
