"""Owned M8 integral-core path, with literal original and R44 endpoint branches.

Zero uses the supplied original cosine class itself. Positive intermediate
lambda keeps the original integral core, full parameter jets and numerical
rho guard, replacing only its seven control functions. One uses the existing
R44 endpoint class. No existing source, profile, guard floor or grid ceiling is
modified. The defining q(lambda) is supplied separately from a BVP's gauge.
"""
import copy
import hashlib
import math
from pathlib import Path
import types
import raw_second_order_core as original
from circle_trace_replacement_core import make_core_class as endpoint_class
from circle_trace_replacement_core import guard_replacements

before='from complementary_moment_basis import ComplementaryMomentBasis'
after='from circle_trace_homotopy_basis import CircleTraceHomotopyBasis as ComplementaryMomentBasis'
text=original.text
if text.count(before)!=1:
    raise RuntimeError('Original basis import is not unique')
text=text.replace(before,after)
for old,new in guard_replacements:
    if text.count(old)!=1:
        raise RuntimeError('The original complete-control guard anchor changed')
    text=text.replace(old,new)
module=types.ModuleType('m3_circle_trace_homotopy_literal')
module.__file__=str(Path(__file__).resolve())
exec(compile(text,str(module.__file__)+'::finite_path','exec'),module.__dict__)


def make_core_factory(reference, original_cosine, settings):
    frozen=copy.deepcopy(settings)
    lam=float(frozen['homotopy'])
    if not 0<=lam<=1 or frozen.get('bimodal_eta')!=0. or not frozen.get('lock_fundamental'):
        raise ValueError('This path is lambda in [0,1], eta zero, with mean/primary locking')
    if float(frozen['center']).hex()!=float(math.pi/3).hex():
        raise ValueError('The exact reflection axis is required')
    if lam==0.:
        # No new core object, integral inverse, guard, or artificial lambda
        # metadata is attached to the original cosine class.
        return original_cosine, dict(branch='literal_original_cosine',lambda_value=0.,
            core_support_guard='The unchanged original cosine guard; the path model also requires its returned rho_lower>1e-5 before using it.',
            exact_core_lift_installed=False)
    if lam==1.:
        Core=endpoint_class(reference)
    else:
        OriginalIntegral=module.make_core_class(reference)
        class Core(OriginalIntegral):
            def summary(self):
                out=super().summary()
                out.update(core_kind='exact_m3_finite_cosine_trace_path_integral',
                    control_family='All seven C_j=(1-lambda)*cos(3j phi)+lambda*E_j, E=B2..B6,T,U',
                    control_homotopy='Finite M8 cosine-to-R44 path',
                    control_path='finite-cosine-trace-synchronous-lift-v1',
                    plateau_radius_at_one=1+self.q*self._circle_constant+float(self.c[-2]),
                    current_curve_is_not_claimed_circular=True,
                    physical_coordinate_scope='The final two coefficients interpolate from old cos21/cos24 to T/U; at intermediate lambda they are not pure radius/centre coordinates.',
                    geometry_scope='The defining integral core is distinct from the partially lifted finite inlet at intermediate lambda. No inherited complete metric or holding/reach conclusion.')
                return out
    def factory(q,corrections=(),base_mode=3):
        if base_mode!=3 or len(corrections)!=7:
            raise ValueError('The declared finite path retains all seven M8 coordinates')
        return Core(q,corrections,base_mode,arc_nodes=1024,**frozen)
    return factory,dict(branch='literal_R44_endpoint' if lam==1. else 'new_finite_seven_column_integral_path',
        lambda_value=lam,core_support_guard='Original numerical triangle/first/C2 guard, floor1e-5 and grid ceiling32768',
        note='This is the defining integral core. For intermediate lambda, the partially lifted finite inlet is a different curve and must pass its own original frame and full metric checks.')


PROVENANCE=dict(original_second_order_guard=original.PROVENANCE,
    new_basis_sha256=hashlib.sha256(Path(__file__).with_name('circle_trace_homotopy_basis.py').read_bytes()).hexdigest(),
    endpoint_core_sha256=hashlib.sha256(Path(__file__).with_name('circle_trace_replacement_core.py').read_bytes()).hexdigest(),
    complete_derived_source_sha256=hashlib.sha256(text.encode()).hexdigest(),
    original_positive_lambda_rho_floor=1e-5,original_grid_ceiling=32768,
    guard_replacements=guard_replacements,scope=__doc__)
