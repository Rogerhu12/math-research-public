#!/usr/bin/env python3
"""Native three-field Gauss--Codazzi equations with exact endpoint liftings.

The unknown correction contains even n,l and odd m Fourier coefficients.
The exact balanced central seed and exact developable tail are added as
functions, not replaced by their Fourier projections. Thus a zero cut
correction really preserves all of the tail's cut values, including its
mean and high modes. No equation divides by any second-form entry.

The radial trapezoidal scheme and projected Gauss equations below are a
finite branch finder only. Their solution is not a continuous metric bound.
The complete, unprojected residual and actual positions still require the
R119/R129 consumer. The scalar outer metric parameter T changes physical g.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import numpy as np
from scipy import sparse
from fd2d_balanced_curvature_core import FixedBalancedGeometry, BalancedCurvatureCore
from fd2d_gc_blended import BlendedIntrinsicGC
from fd2d_gc_design_profile import CoastDesignProfile
from fd2d_flat_developable_family import FlatDevelopableFamily


class CertifiedReference:
    def __init__(self, geometry):
        self.geometry, self.a0 = geometry, geometry.a0

    def reference_coordinate(self, phi):
        q = self.geometry.material_coordinate(phi)
        return dict(u=q['u'], u_theta=q['u_phi'], u_theta_theta=q['u_phi_phi'])


def step5(t):
    q = np.clip(t, 0., 1.)
    return q**3*(10-15*q+6*q*q), 30*q*q*(1-q)**2


def mesh_for(profile, max_step, blend):
    knots = sorted(set([float(x) for x in profile.breaks] + list(blend)))
    return np.unique(np.concatenate([
        np.linspace(a, b, max(1, int(np.ceil((b-a)/max_step)))+1)
        for a, b in zip(knots[:-1], knots[1:])]))


class RawLiftedDAE:
    def __init__(self, source, *, modes=7, max_step=.04, gap=.9,
                 blend=(.58, 1.4), base_kind='balanced_seed',
                 profile_kind='legacy_coast', tail_kind='signed_bubble'):
        self.K = int(modes)
        self.e, self.d, self.q = self.K+1, 2*self.K+1, 3*self.K+2
        self.parameter_count = 2*self.K+2
        self.gap, self.base_kind = float(gap), base_kind
        self.source = source
        self.profile_kind, self.tail_kind = profile_kind, tail_kind
        self.geometry = FixedBalancedGeometry()
        if profile_kind == 'legacy_coast':
            profile_class = CoastDesignProfile
        elif profile_kind == 'positive_clock':
            from fd2d_gc_design_profile_positive import PositiveCoastDesignProfile
            profile_class = PositiveCoastDesignProfile
        else:
            raise ValueError('Unknown explicit physical radial chart')
        if tail_kind == 'signed_bubble':
            self.tail_class = FlatDevelopableFamily
        elif tail_kind == 'positive_bernstein':
            from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily
            self.tail_class = PositiveFlatDevelopableFamily
        else:
            raise ValueError('Unknown exact developable tail family')
        self.profile = profile_class(source)
        right = min(float(blend[1]), .94*self.profile.end)
        left = min(float(blend[0]), .6*right)
        self.blend = (left, right)
        self.chart = BlendedIntrinsicGC(self.profile, maximum_mode=2*self.K+1,
            oversample=4, reference=CertifiedReference(self.geometry),
            blend_interval=self.blend)
        self.x = mesh_for(self.profile, max_step, self.blend)
        self.N = len(self.x)
        self.size = self.q*self.N+self.parameter_count
        theta = np.asarray(self.chart.theta, dtype=float)
        self.work = len(theta)
        frequencies = 2*np.arange(self.K+1)
        self.E = np.cos(theta[:, None]*frequencies)
        self.O = np.sin(theta[:, None]*frequencies[1:])
        self.Ex = -np.sin(theta[:, None]*frequencies)*frequencies
        self.Ox = np.cos(theta[:, None]*frequencies[1:])*frequencies[1:]
        self.PE = 2*self.E.T/self.work
        self.PE[0] *= .5
        self.PO = 2*self.O.T/self.work
        self.core_basis = self.E[:, 1:]-np.asarray(self.geometry.mu[:self.K], float)
        self.core_coefficients = np.vstack((-np.asarray(self.geometry.mu[:self.K], float),
                                            np.eye(self.K)))
        rho = np.asarray(self.geometry.radius(theta), float)
        rhop = np.asarray(self.geometry.radius_derivative(theta), float)
        if base_kind == 'balanced_seed':
            self.seed, self.seed_xi = 1/rho, -rhop/rho**2
        elif base_kind == 'circle':
            self.seed, self.seed_xi = np.full_like(rho, 1/float(self.geometry.a0)), np.zeros_like(rho)
        else:
            raise ValueError('Unknown actual central curve definition')
        self.coords = {k: np.asarray(v, float) for k, v in self.chart.coordinates(self.x).items()}
        self.h = np.diff(self.x)
        self.select = np.zeros((self.d, self.q))
        self.select[:, :self.d] = np.eye(self.d)
        self._operator_cache = {}
        self._last_c = self._last_core = self._last_axes = None

    def unpack(self, vector):
        z = np.asarray(vector, dtype=float)
        return z[:self.q*self.N].reshape(self.N, self.q), z[self.q*self.N:]

    def impose_linear_boundary_values(self, vector):
        """Retain the exact central and full-cut affine endpoint values."""
        z = np.array(vector, dtype=float, copy=True)
        y, p = self.unpack(z)
        y[-1] = 0.
        y[0] = 0.
        y[0, :self.e] = self.core_coefficients@p[:self.K]
        return z

    def core(self, coefficients):
        c = np.asarray(coefficients, float)
        if self._last_c is None or not np.array_equal(c, self._last_c):
            self._last_core = BalancedCurvatureCore(c, base_kind=self.base_kind, geometry=self.geometry)
            self._last_axes = self._last_core.axis_intercepts_and_jacobian()
            self._last_c = c.copy()
        return self._last_core, self._last_axes

    def tail(self, coefficients):
        return self.tail_class(coefficients=np.asarray(coefficients, float),
            cut_radius=.8, cuff_radius=.32, flat_radius=.34, plane_height=1.25)

    def parameter_domain(self, vector, central_curvature_maximum=None):
        """A chosen geometric search domain, not an existence exclusion.

        Bernstein coefficient bounds are exact sufficient tail bounds.
        The central curvature check is only a finite trial rejection rule;
        any eventual continuous geometry bound is still paid separately.
        """
        _, p = self.unpack(vector)
        if not np.all(np.isfinite(p)) or not 0 < p[-1] < self.profile.model.Tmax:
            return False
        if self.tail_kind == 'positive_bernstein' and (np.min(p[self.K:-1]) < 0 or np.max(p[self.K:-1]) > 1.2):
            return False
        if central_curvature_maximum is not None:
            n = self.seed+self.core_basis@p[:self.K]
            if n.min() <= 0 or n.max() > central_curvature_maximum:
                return False
        return True

    def operators(self, T):
        T = float(T)
        if T in self._operator_cache:
            return self._operator_cache[T]
        self.profile.set_parameter(T)
        jet = self.profile.jet(self.x)
        a, c, scale = [np.asarray(jet[k], float) for k in ('a', 'c', 'radial_scale')]
        inv = 1/(self.coords['u_xi']*a)
        adv = self.coords['advection']
        op = np.zeros((self.N, self.d, self.q))
        for j in range(self.N):
            reaction = scale[j]*c[j]
            op[j, :self.e, :self.e] = self.PE@(adv[:, j, None]*self.Ex)-reaction*np.eye(self.e)
            op[j, :self.e, self.e:self.d] = self.PE@((scale[j]*inv[:, j, None])*self.Ox)
            op[j, :self.e, self.d:] = reaction*np.eye(self.e)
            op[j, self.e:, self.e:self.d] = self.PO@(adv[:, j, None]*self.Ox)-2*reaction*np.eye(self.K)
            op[j, self.e:, self.d:] = self.PO@((scale[j]*inv[:, j, None])*self.Ex)
        value = dict(jet=jet, op=op, inv=inv, adv=adv)
        if len(self._operator_cache) > 4:
            self._operator_cache.clear()
        self._operator_cache[T] = value
        return value

    def lifting(self, T, tail_parameters):
        """Exact function lifting and its actual x/xi derivatives at nodes.

        Tail II is linear in the bending coefficients. Return its full
        coefficient bases too; this gives analytic parameter columns.
        """
        ops = self.operators(T)
        jet = ops['jet']
        a = np.asarray(jet['a'], float)
        ax = np.asarray(jet['a_s']*jet['radial_scale'], float)
        U, Ux, Uxi = self.coords['u'], self.coords['u_s'], self.coords['u_xi']
        sn, cs = np.sin(U), np.cos(U)
        z = a[None, :]*sn
        fam = self.tail(tail_parameters)
        curve = fam.angle_jets(z)
        k = np.asarray(curve['kappa'], float)
        ky = np.asarray(curve['kappa_y'], float)
        kp = np.asarray(curve['kappa_jacobian'], float)
        kyp = np.asarray(curve['kappa_y_jacobian'], float)
        # Component order is n,m,l everywhere in this module.
        v = np.stack((cs*cs, -sn*cs, sn*sn), axis=-1)
        vu = np.stack((-2*sn*cs, sn*sn-cs*cs, 2*sn*cs), axis=-1)
        raw = k[..., None]*v
        raw_x = ky[..., None]*(ax[None, :]*sn+a[None, :]*cs*Ux)[..., None]*v+k[..., None]*Ux[..., None]*vu
        raw_xi = ky[..., None]*(a[None, :]*cs*Uxi)[..., None]*v+k[..., None]*Uxi[..., None]*vu
        raw_p = v[..., None]*kp[..., None, :]
        raw_x_p = (ax[None, :]*sn+a[None, :]*cs*Ux)[..., None, None]*v[..., None]*kyp[..., None, :]+Ux[..., None, None]*vu[..., None]*kp[..., None, :]
        raw_xi_p = (a[None, :]*cs*Uxi)[..., None, None]*v[..., None]*kyp[..., None, :]+Uxi[..., None, None]*vu[..., None]*kp[..., None, :]
        t0, t1 = .42*self.profile.end, self.profile.end
        wt, wtq = step5((self.x-t0)/(t1-t0))
        wtx = wtq/(t1-t0)
        seed_end = min(.55, .4*self.profile.end)
        w0, w0q = step5(self.x/seed_end)
        wc, wcx = 1-w0, -w0q/seed_end
        lift = wt[None, :, None]*raw
        lx = wt[None, :, None]*raw_x+wtx[None, :, None]*raw
        lxi = wt[None, :, None]*raw_xi
        lp = wt[None, :, None, None]*raw_p
        lxp = wt[None, :, None, None]*raw_x_p+wtx[None, :, None, None]*raw_p
        lxip = wt[None, :, None, None]*raw_xi_p
        lift[:, :, 0] += self.seed[:, None]*wc
        lx[:, :, 0] += self.seed[:, None]*wcx
        lxi[:, :, 0] += self.seed_xi[:, None]*wc
        scale = np.asarray(jet['radial_scale'], float)
        c = np.asarray(jet['c'], float)
        def forcing(vv, xx, dd):
            # Extra axes after component are carried through by broadcasting.
            extra = (1,)*(vv.ndim-3)
            sc = scale.reshape((1, self.N)+extra)
            cc = c.reshape((1, self.N)+extra)
            inv = ops['inv'].reshape((self.work, self.N)+extra)
            adv = ops['adv'].reshape((self.work, self.N)+extra)
            fn = sc*(inv*dd[:, :, 1]+cc*(vv[:, :, 2]-vv[:, :, 0]))+adv*dd[:, :, 0]-xx[:, :, 0]
            fm = sc*(inv*dd[:, :, 2]-2*cc*vv[:, :, 1])+adv*dd[:, :, 1]-xx[:, :, 1]
            return np.concatenate((np.einsum('ew,wn...->ne...', self.PE, fn),
                                   np.einsum('kw,wn...->nk...', self.PO, fm)), axis=1)
        return dict(values=lift, x=lx, xi=lxi, parameters=lp,
                    forcing=forcing(lift, lx, lxi),
                    forcing_parameters=forcing(lp, lxp, lxip), tail=fam,
                    alpha=np.asarray(curve['alpha'], float))

    def evaluate(self, vector, *, jacobian=False):
        y, p = self.unpack(vector)
        c, b, T = p[:self.K], p[self.K:-1], p[-1]
        ops = self.operators(T)
        lift = self.lifting(T, b)
        fields = np.stack((self.E@y[:, :self.e].T,
                           self.O@y[:, self.e:self.d].T,
                           self.E@y[:, self.d:].T), axis=-1)+lift['values']
        n, m, l = fields[:, :, 0], fields[:, :, 1], fields[:, :, 2]
        f = np.einsum('ndq,nq->nd', ops['op'], y)+lift['forcing']
        cod = (y[1:, :self.d]-y[:-1, :self.d])/self.h[:, None]-.5*(f[1:]+f[:-1])
        full_gauss = n*l-m*m-np.asarray(ops['jet']['K'], float)[None, :]
        gauss = (self.PE@full_gauss[:, :-1]).T
        _, axes = self.core(c)
        left = y[0, :self.d].copy()
        left[:self.e] -= self.core_coefficients@c
        right = y[-1, :self.d]
        residual = np.r_[cod.ravel(), gauss.ravel(), y[-1, self.d:], left, right,
                         (float(axes['gap'])-self.gap)/self.gap]
        assert len(residual) == self.size
        data = dict(fields=fields, full_gauss=full_gauss, codazzi_cells=cod,
                    projected_gauss=gauss, axes=axes, lift=lift, parameters=p)
        if not jacobian:
            return residual, data
        rr, cc, vv = [], [], []
        def block(row, col, values):
            values = np.atleast_2d(np.asarray(values, float))
            ii, jj = np.nonzero(values)
            rr.append(ii+row); cc.append(jj+col); vv.append(values[ii, jj])
        pcol = self.N*self.q
        eps = min(1e-6*(1+abs(T)), .2*T, .2*(self.profile.model.Tmax-T))
        # T is the sole numerical derivative column; all state and tail
        # parameter derivatives are analytic. It is an outer g design.
        op_plus, op_minus = self.operators(T+eps), self.operators(T-eps)
        lift_plus, lift_minus = self.lifting(T+eps, b), self.lifting(T-eps, b)
        fT = (np.einsum('ndq,nq->nd', op_plus['op']-op_minus['op'], y)+
              lift_plus['forcing']-lift_minus['forcing'])/(2*eps)
        fieldsT = (lift_plus['values']-lift_minus['values'])/(2*eps)
        gaussT = (l*fieldsT[:, :, 0]+n*fieldsT[:, :, 2]-2*m*fieldsT[:, :, 1]-
            ((np.asarray(op_plus['jet']['K'])-np.asarray(op_minus['jet']['K']))/(2*eps))[None, :])
        for j in range(self.N-1):
            row = j*self.d
            block(row, j*self.q, -self.select/self.h[j]-.5*ops['op'][j])
            block(row, (j+1)*self.q, self.select/self.h[j]-.5*ops['op'][j+1])
            block(row, pcol+self.K, -.5*(lift['forcing_parameters'][j]+lift['forcing_parameters'][j+1]))
            block(row, pcol+len(p)-1, -.5*(fT[j]+fT[j+1])[:, None])
        row0 = (self.N-1)*self.d
        gp = lift['parameters']
        for j in range(self.N-1):
            row = row0+j*self.e
            gstate = np.concatenate((self.PE@(l[:, j, None]*self.E),
                                    self.PE@(-2*m[:, j, None]*self.O),
                                    self.PE@(n[:, j, None]*self.E)), axis=1)
            block(row, j*self.q, gstate)
            gparam = l[:, j, None]*gp[:, j, 0]+n[:, j, None]*gp[:, j, 2]-2*m[:, j, None]*gp[:, j, 1]
            block(row, pcol+self.K, self.PE@gparam)
            block(row, pcol+len(p)-1, (self.PE@gaussT[:, j])[:, None])
        row = row0+(self.N-1)*self.e
        block(row, (self.N-1)*self.q+self.d, np.eye(self.e)); row += self.e
        block(row, 0, self.select)
        central = np.zeros((self.d, self.K)); central[:self.e] = -self.core_coefficients
        block(row, pcol, central); row += self.d
        block(row, (self.N-1)*self.q, self.select); row += self.d
        block(row, pcol, np.asarray(axes['gap_jacobian'], float)[None, :]/self.gap)
        matrix = sparse.coo_matrix((np.concatenate(vv), (np.concatenate(rr), np.concatenate(cc))),
                                   shape=(self.size, self.size)).tocsc()
        return residual, matrix, data

    def initializer(self, amplitude=1., prefix_trajectory=None):
        p = np.zeros(self.parameter_count)
        if self.tail_kind == 'positive_bernstein':
            p[self.K:-1] = amplitude
        else:
            p[self.K] = amplitude
        p[-1] = self.profile.reference_T
        ops, lift = self.operators(p[-1]), self.lifting(p[-1], p[self.K:-1])
        a, v, K = [np.asarray(ops['jet'][k], float) for k in ('a', 'a_s', 'K')]
        nr = np.sqrt(np.maximum(0., 1-v*v))/a
        w, _ = step5((self.x-.42*self.profile.end)/(.58*self.profile.end))
        tail_values = self.tail(p[self.K:-1]).cut_port(self.coords['u'], position_jets=False)
        # The rotational normal curvature already vanishes at the flat
        # endpoint. An additional (1-w) factor would incorrectly force it
        # to vanish three orders faster on the unbent angular arcs, and
        # make the Gauss-compatible initial l blow up there.
        n = self.seed[:, None]*(nr[None, :]*float(self.geometry.a0))+w[None, :]*tail_values['n']
        m = w[None, :]*tail_values['m']
        self.initializer_definition = dict(kind='explicit rotational-scaled seed plus exact tail blend',
                                           initializer_only=True)
        if prefix_trajectory is not None:
            from fd2d_flat_prefix_initializer import ActualFlatPrefixInitializer
            source = ActualFlatPrefixInitializer(prefix_trajectory, self.source, geometry=self.geometry)
            if abs(source.T-p[-1]) > 1e-14:
                raise ValueError('The actual prefix initializer binds another physical metric T')
            s = np.asarray(ops['jet']['s'], float)
            end = source.interval[1]
            keep = s <= end
            actual = source.evaluate_material(s[None, keep], self.coords['u'][:, keep])
            n[:, keep], m[:, keep] = actual['n'], actual['m']
            # Explicit extension of only the initial guess: transport the
            # last positive-n angular shape with the rotational curvature
            # and blend m and the exact tail over the remaining domain.
            if np.any(~keep):
                u = self.coords['u'][:, ~keep]
                last = source.evaluate_material(np.full_like(u, end), u)
                aa, ap, _ = source.candidate.profile(np.array([end]))
                nr_last = float(np.sqrt(1-ap[0]*ap[0])/aa[0])
                blend, _ = step5((s[~keep]-end)/(s[-1]-end))
                n[:, ~keep] = last['n']*(nr[None, ~keep]/nr_last)+blend[None, :]*tail_values['n'][:, ~keep]
                m[:, ~keep] = (1-blend[None, :])*last['m']+blend[None, :]*tail_values['m'][:, ~keep]
            self.initializer_definition = dict(kind='actual accepted positive-n prefix plus explicit continuation guess',
                source=source.definition(), trajectory=str(prefix_trajectory),
                extension='last angular n shape times rotational n, quintic blend to exact cut tail; m quintic blend',
                initializer_only=True, no_solution_claim_outside_source_interval=True)
        l = np.divide(K[None, :]+m*m, n, out=np.zeros_like(n), where=np.abs(n)>1e-13)
        total = np.stack((n, m, l), axis=-1)
        total[:, -1] = lift['values'][:, -1]
        correction = total-lift['values']
        y = np.concatenate(((self.PE@correction[:, :, 0]).T,
                            (self.PO@correction[:, :, 1]).T,
                            (self.PE@correction[:, :, 2]).T), axis=1)
        y[0] = 0.; y[-1] = 0.
        return np.r_[y.ravel(), p]

    def diagnostics(self, vector, data=None):
        if data is None:
            residual, data = self.evaluate(vector)
        else:
            residual = self.evaluate(vector)[0]
        fields, p = data['fields'], data['parameters']
        axes = data['axes']
        n, m, l = fields[:, :, 0], fields[:, :, 1], fields[:, :, 2]
        radius = np.sqrt((l-n)**2+4*m*m)
        return dict(residual_maximum=float(np.max(np.abs(residual))),
            residual_rms=float(np.linalg.norm(residual)/np.sqrt(len(residual))),
            full_gauss_node_maximum=float(np.max(np.abs(data['full_gauss']))),
            formal_curvature_node_maximum=float(np.max(np.maximum(np.abs(l+n+radius), np.abs(l+n-radius)))/2),
            A=float(axes['A']), B=float(axes['B']), gap=float(axes['gap']),
            T=float(p[-1]), tail_coefficients=p[self.K:-1].tolist(),
            minimum_n=float(n.min()), maximum_n=float(n.max()),
            minimum_central_curvature=float((self.seed+self.core_basis@p[:self.K]).min()),
            maximum_lifting_alpha=float(np.max(np.abs(data['lift']['alpha']))),
            exact_cut_lifting_function=True, cut_n_mean_omitted=False,
            cut_correction_maximum=float(np.max(np.abs(self.unpack(vector)[0][-1]))),
            actual_field_cut_exact=bool(np.all(self.unpack(vector)[0][-1] == 0.)),
            nonlinear_finite_solution=False, continuous_certificate=False)
