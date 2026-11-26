"""New R68 complementary-arc phase family, with a literal zero-control anchor.

This is not a finite change of basis of v2. Its declared frequencies are
the true constants P=2*pi/3, L=P/2-S, omega_j=j*pi/L for every truncation.
The binary64 values below evaluate that definition numerically; they do not
define fitted frequencies or a different target at different M.
"""
import importlib.util
import math
from pathlib import Path
import sys
import numpy as np

BASIS_RULE=dict(family='complementary_arc_sine_v1',period='2*pi/3',
    complementary_halfwidth='period/2-S',frequency='j*pi/(period/2-S)',
    coordinate='u for u<period/2, u-period otherwise; periodic extension',
    S='exact frozen binary-rational anchor halfwidth',
    b='exact frozen binary-rational anchor transition',
    basis='W(u)*sin(omega_j*v)/(omega_j+630/(256*b))',
    truncation='first M members of one infinite family; no frequency fitting',
    numerical_evaluation='binary64 evaluation of the declared true constants',
    global_phase_basis_regular_order_at_least=4)


def _base_provider():
    name='_warm_complement_v3_geometry_base'
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
        raise ValueError('The new true complementary-arc phase family must be declared explicitly')
    scale_rule=dict(legacy_power_start=2,legacy_floor=1e-9,
        physical_control='phase_scale_times_p',first='log(q_aux/gauge_q)')
    if settings.get('phase_parameter_scale_rule')!=scale_rule:
        raise ValueError('The actual inherited warped-BVP control scaling changed')
    old=_base_provider()
    anchor=old.make_factory(settings,reference_class=reference_class,
                            anchor_baseline=anchor_baseline).baseline
    gauge=float(settings['gauge_q'])
    scale=float(settings['phase_control_scale'])

    class ComplementCore(old.SupportedIncrementCore):
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
            # Same real curvature floor/guard, with the actual new omega.
            super()._set_guard()

        def _basis(self,local):
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
            value.update(core_kind='warm-complementary-arc-phase-v3',provider_version=3,
                phase_basis=BASIS_RULE,numerical_complement_halfwidth=float(self.complement_halfwidth),
                numerical_frequencies=self.omega.tolist(),actual_legacy_scales=self.actual_legacy_scales.tolist(),
                physical_controls_equal_phase_scale_times_solver_parameters=True,
                same_finite_span_as_v2=False,
                global_phase_basis_regular_order_at_least=4,
                global_curve_regular_order_at_least=5)
            return value

    ComplementCore.anchor_definition=settings
    ComplementCore.baseline=anchor
    return ComplementCore
