"""R53 anchored phase homotopy from full-period to complementary controls.

At lambda<1 the control columns may change the protected arc. At lambda=1
this is the exact v3 complementary-arc family. This changes the intermediate
finite family; it is not a coordinate relabeling of an accepted v3 solution.
Zero controls delegate the same complete R53 baseline literally. The true
P, L and omega constants have the same meaning as in R68.
"""
import importlib.util
import math
from pathlib import Path
import sys
import numpy as np

BASIS_RULE=dict(family='full_to_complementary_arc_sine_homotopy_v1',period='2*pi/3',
    complementary_halfwidth='period/2-S',frequency='j*pi/(period/2-S)',
    full_frequency='3*j',
    coordinate='u for u<period/2, u-period otherwise; periodic extension',
    S='exact frozen binary-rational anchor halfwidth',
    b='exact frozen binary-rational anchor transition',
    full_basis='sin(3*j*u)/(3*j)',
    complementary_basis='W(u)*sin(omega_j*v)/(omega_j+630/(256*b))',
    basis='(1-lambda)*full_basis+lambda*complementary_basis',
    homotopy='same declared lambda as the complete R53 anchor baseline',
    lambda_derivative='complementary_basis-full_basis; include sum(d_j*d_lambda_basis) when d is nonzero',
    endpoint_family='complementary_arc_sine_v1 exactly at lambda=1',
    truncation='first M members of one infinite family; no frequency fitting',
    numerical_evaluation='binary64 evaluation of the declared true constants',
    global_phase_basis_regular_order_at_least=4)


def _base_provider():
    name='_warm_homotopy_v4_geometry_base'
    if name in sys.modules:
        return sys.modules[name]
    path=Path(__file__).with_name('warm_supported_core_factory.py')
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value
    spec.loader.exec_module(value)
    return value


def make_factory(settings,reference_class=None,anchor_baseline=None):
    settings=dict(settings)
    if settings.get('phase_basis')!=BASIS_RULE:
        raise ValueError('The full-to-complementary phase homotopy must be declared explicitly')
    scale_rule=dict(legacy_power_start=2,legacy_floor=1e-9,
        physical_control='phase_scale_times_p',first='log(q_aux/gauge_q)')
    if settings.get('phase_parameter_scale_rule')!=scale_rule:
        raise ValueError('The actual inherited warped-BVP control scaling changed')
    old=_base_provider()
    anchor=old.make_factory(settings,reference_class=reference_class,
                            anchor_baseline=anchor_baseline).baseline
    gauge=float(settings['gauge_q'])
    scale=float(settings['phase_control_scale'])

    class HomotopyCore(old.SupportedIncrementCore):
        def _set_guard(self):
            # The parent sets sizes and physical controls before invoking
            # this hook; all subsequent integrals use this new basis.
            self.complement_halfwidth=self.halfperiod-self.halfwidth
            if not self.complement_halfwidth>self.transition>0:
                raise ValueError('The original protection/transition must fit in the true complementary arc')
            self.phase_harmonics=np.arange(1,len(self.controls)+1)
            self.omega=math.pi*self.phase_harmonics/self.complement_halfwidth
            self.frequencies=self.omega.copy()
            D1=630./(256.*self.transition)
            self.denominators=self.omega+D1
            self.norms=self.denominators/self.omega
            self.phase_basis_kind=BASIS_RULE['family']
            # Each mixed curvature column has sup norm <= 1. The old
            # complement third-derivative bound C_j >= omega_j**2 >= (3*j)**2
            # also bounds the convex mixture, so the same conservative guard
            # applies at every lambda. See the v4 derivation note.
            super()._set_guard()

        def _complement_basis(self,local):
            local=np.asarray(local,float).reshape(-1)
            _,W,W1,W2,_=self.baseline._window(local)
            t=np.clip((abs(local-self.halfperiod)-self.halfwidth)/self.transition,0.,1.)
            W3=(7560*t*t*(1-t)**2*(1-2*t)**2-5040*t**3*(1-t)**3)
            W3*=np.sign(local-self.halfperiod)/self.transition**3
            v=np.where(local<self.halfperiod,local,local-self.period)
            w=self.omega[:,None];den=self.denominators[:,None]
            sn,cs=np.sin(w*v[None,:]),np.cos(w*v[None,:])
            phase=W[None,:]*sn/den
            first=(w*W[None,:]*cs+W1[None,:]*sn)/den
            second=(2*w*W1[None,:]*cs+(W2[None,:]-w*w*W[None,:])*sn)/den
            third=((3*w*W2[None,:]-w*w*w*W[None,:])*cs+
                   (W3[None,:]-3*w*w*W1[None,:])*sn)/den
            return phase,first,second,third

        def _full_basis(self,local):
            local=np.asarray(local,float).reshape(-1)
            w=(self.base_mode*self.phase_harmonics)[:,None]
            sn,cs=np.sin(w*local[None,:]),np.cos(w*local[None,:])
            return sn/w,cs,-w*sn,-w*w*cs

        def _basis(self,local):
            complement=self._complement_basis(local)
            if self.homotopy==1.:
                return complement
            full=self._full_basis(local)
            lam=self.homotopy
            return tuple((1.-lam)*a+lam*b for a,b in zip(full,complement))

        def _basis_lambda_derivative(self,local):
            """Partial lambda at fixed u, controls and frozen window/anchor."""
            return tuple(b-a for a,b in zip(self._full_basis(local),
                                            self._complement_basis(local)))

        def __init__(self,q,corrections=(),base_mode=3):
            if base_mode!=3:
                raise ValueError('Only the declared threefold core is supported')
            legacy=np.asarray(corrections,float)
            if not np.isfinite(q) or q<=0 or not np.all(np.isfinite(legacy)):
                raise FloatingPointError('Finite positive auxiliary coordinate and controls required')
            scales=np.maximum(gauge**np.arange(2,len(legacy)+2),1e-9)
            controls=np.r_[scale*math.log(float(q)/gauge),scale*legacy/scales]
            chain=np.r_[scale/float(q),scale/scales]
            super().__init__(anchor,controls,input_chain=chain,q_aux=q,gauge_q=gauge)
            self.phase_control_scale=scale
            self.actual_legacy_scales=scales

        def summary(self):
            value=super().summary()
            value.update(core_kind='warm-full-to-complementary-arc-phase-v4',provider_version=4,
                phase_basis=BASIS_RULE,numerical_complement_halfwidth=float(self.complement_halfwidth),
                numerical_frequencies=self.omega.tolist(),actual_legacy_scales=self.actual_legacy_scales.tolist(),
                physical_controls_equal_phase_scale_times_solver_parameters=True,
                correction_meaning='full-to-complementary material phase controls d2...dM; may change the protected arc for lambda<1; not support Fourier coefficients',
                same_finite_span_as_v2=False,
                same_finite_span_as_v3_before_lambda_one=False,
                endpoint_basis_is_v3=bool(self.homotopy==1.),
                numerical_full_frequencies=(3*self.phase_harmonics).tolist(),
                curvature_column_sup_bound=1.,
                complement_third_derivative_bound_reused=True,
                global_phase_basis_regular_order_at_least=4,
                global_curve_regular_order_at_least=5)
            return value

    HomotopyCore.anchor_definition=settings
    HomotopyCore.baseline=anchor
    return HomotopyCore
