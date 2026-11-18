"""Independent lambda-one integral core with two raw columns replaced.

The original large-radius integral construction, parameter derivatives,
Frenet equations and the existing numerical positivity guard are retained.
Replacing the last two raw controls by T=SA-SB and U=SB changes the finite
physical space.  Physical coordinates (t,u) give (A,B)=(t,u-t).
No existing source or active solver is modified by this module.
"""
import hashlib
from pathlib import Path
import types
import raw_second_order_core as original


before='from complementary_moment_basis import ComplementaryMomentBasis'
after='from circle_trace_replacement_basis import CircleTraceReplacementBasis as ComplementaryMomentBasis'
text=original.text
if text.count(before)!=1:raise RuntimeError('The original basis import is not unique')
text=text.replace(before,after)
guard_replacements=[
    ('triangle=float(np.sum(abs(self.c)*rb))',
     'combined_bounds=(0.,0.,0.) if self.basis is None else self.basis.combined_control_rho_bounds(self.c,self.lam)\n            triangle=float(combined_bounds[0])'),
    ('float(np.sum(abs(self.c)*db))','float(combined_bounds[1])'),
    ('float(np.sum(abs(self.c)*ddb))','float(combined_bounds[2])')]
for old,new in guard_replacements:
    if text.count(old)!=1:raise RuntimeError('Original complete-control budget occurrence changed: '+old)
    text=text.replace(old,new)
module=types.ModuleType('m3_circle_trace_replacement_literal')
module.__file__=str(Path(__file__).resolve())
exec(compile(text,str(module.__file__)+'::new_endpoint_space','exec'),module.__dict__)


def make_core_class(reference):
    Base=module.make_core_class(reference)
    class CircleTraceReplacementCore(Base):
        def __init__(self,*args,**kwargs):
            if kwargs.get('homotopy',1.)!=1.:
                raise ValueError('This new finite control space is defined only at lambda one')
            super().__init__(*args,**kwargs)
            if self.base_mode!=3 or len(self.c)<3:
                raise ValueError('The declared trace replacement requires n3 and at least three controls')

        def summary(self):
            out=super().summary()
            t,u=map(float,self.c[-2:]);A,B=t,u-t
            out.update(core_kind='exact_m3_circle_trace_replacement_integral',
                control_family='Retained raw B2..B(M-2), then T=SA-SB and U=SB',
                control_homotopy='lambda-one new finite space only',
                control_path='circle-trace-replace-last-two-v1',
                plateau_radius_at_one=1+self.q*self._circle_constant+A,
                circle_radius_trace_A=A,circle_center_trace_B=B,
                physical_trace_coordinates=dict(t=t,u=u),
                nominal_last_two_frequency_labels_are_not_harmonics=True,
                geometry_scope='R44 fixes radius/centre signs. Old holding, reach, positivity and metric constants do not transfer to this new core.')
            return out
    return CircleTraceReplacementCore


PROVENANCE=dict(original_second_order_guard=original.PROVENANCE,
    new_basis_source_sha256=hashlib.sha256(Path(__file__).with_name('circle_trace_replacement_basis.py').read_bytes()).hexdigest(),
    derived_core_source_sha256=hashlib.sha256(text.encode()).hexdigest(),
    scope=__doc__,unchanged_rho_floor=1e-5,unchanged_grid_ceiling=32768,
    control_guard_budget_scope='Combine the physical trace seed and low projection before analytic absolute bounds; no sampled derivative maxima',
    guard_replacements=guard_replacements)
