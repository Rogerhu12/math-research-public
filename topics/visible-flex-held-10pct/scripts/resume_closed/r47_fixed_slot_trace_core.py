"""R47 low-level integral-core factory with fixed T/U coordinate slots.

At M8 this delegates the frozen original factory without constructing a
replacement model. At M>8 and lambda zero it returns the same supplied
original cosine class. Positive lambda uses the original integral geometry,
material inverse, full parameter derivatives and numerical positivity guard;
only the basis import and the existing three combined-bound substitutions
are applied. The high-level state blocks, inlet projection, synchronous lift,
parameter scales, DN dimensions and mean-height integration are not changed
or implemented here. Those must be bound separately under R47/R48.
"""
import copy
import hashlib
import math
from pathlib import Path
import sys
import types

from r47_fixed_slot_trace_basis import M3, DEPENDENCY_SHA256 as BASIS_DEPENDENCIES
from r47_fixed_slot_trace_basis import checked_modes, endpoint_labels, fixed_to_canonical_indices


CORE_DEPENDENCY_SHA256 = {
    'circle_trace_homotopy_core.py': 'acb3e2dffa0f7dc5e811b055da8e582bb19d931b97201ada38acc1f9aa5511ad',
    'circle_trace_replacement_core.py': '4f9351cb356ce33da28d2d4a36a09d14606f3627846b5bf35d7f73478939cb18',
    'raw_second_order_core.py': '79b7ddec4c3721e575816c30f94fb441bb76acb215d3453abe3cdce501850e24',
    'round_raw_lib/large_radius_local_core.py': 'f6b040996f6953fe968b5badf62244ce63f50accac790d5c308dd4543a36a48a',
    'round_raw_lib/fixed_large_radius_core.py': '00f23e03fb736ece6d461ffb082c8bb598a8c4200d3f60b5e8d752731163ffba',
    'round_raw_lib/plateau_core.py': '0db6b2aaf7ecce94eb2f2cda926b5e1f12c3da99656c0e5d0f4b9e3c7dddee34',
}
for _name, _expected in CORE_DEPENDENCY_SHA256.items():
    if hashlib.sha256((M3/_name).read_bytes()).hexdigest() != _expected:
        raise RuntimeError('A frozen defining core source changed: '+_name)
for _directory in (Path(__file__).resolve().parent, M3, M3/'round_raw_lib'):
    if str(_directory) not in sys.path:
        sys.path.insert(0, str(_directory))

import raw_second_order_core as original
from circle_trace_homotopy_core import make_core_factory as original_m8_factory
from circle_trace_replacement_core import guard_replacements


BASIS_IMPORT = (
    'from complementary_moment_basis import ComplementaryMomentBasis',
    'from r47_fixed_slot_trace_basis import make_fixed_slot_basis as ComplementaryMomentBasis')
TRANSFORMS = [BASIS_IMPORT, *guard_replacements]
text = original.text
for _before, _after in TRANSFORMS:
    if text.count(_before) != 1:
        raise RuntimeError('The frozen full-control integral core anchor changed: '+_before)
    text = text.replace(_before, _after)
_reverse = text
for _before, _after in reversed(TRANSFORMS):
    if _reverse.count(_after) != 1:
        raise RuntimeError('The independent core transformation is not uniquely reversible')
    _reverse = _reverse.replace(_after, _before)
if _reverse != original.text:
    raise RuntimeError('The original integral core changed beyond the four declared substitutions')
module = types.ModuleType('m3_r47_fixed_slot_integral_literal')
module.__file__ = str(Path(__file__).resolve())
exec(compile(text, str(module.__file__)+'::fixed_slots', 'exec'), module.__dict__)


def make_core_factory(reference, original_cosine, settings, *, modes=8):
    M = checked_modes(modes)
    if M == 8:
        return original_m8_factory(reference, original_cosine, settings)
    frozen = copy.deepcopy(settings)
    lam = float(frozen['homotopy'])
    if (not math.isfinite(lam) or not 0 <= lam <= 1 or
            frozen.get('bimodal_eta') != 0. or not frozen.get('lock_fundamental')):
        raise ValueError('The R47 path keeps lambda in [0,1], eta zero and both low constraints')
    if float(frozen['center']).hex() != float(math.pi/3).hex():
        raise ValueError('The same literal reflection axis is required')
    description = dict(modes=M, controls=M-1, lambda_value=lam,
        coordinate_scheme='R47-fixed-trace-slots-5-and-6-v1',
        physical_trace_indices=[5, 6], parameter_indices_if_delta_first=[6, 7],
        fixed_to_canonical_indices=list(fixed_to_canonical_indices(M)),
        columns_at_one=endpoint_labels(M),
        physical_control_scope='Pass all physical c directly; a caller must separately preserve c when pscales change',
        representation_scope='Zero extension preserves the defining core only. Inlet/state/lift/mean transfer belongs to the separate R48 high-level implementation')
    if lam == 0.:
        # The returned legacy class is not wrapped. As in the old factory,
        # the high-level model is responsible for the declared dimension.
        return original_cosine, dict(**description, branch='literal_original_cosine',
            exact_core_lift_installed=False,
            core_support_guard='Unchanged original cosine constructor; the high-level path retains its separate rho_lower>1e-5 check')

    OriginalIntegral = module.make_core_class(reference)

    class FixedSlotIntegralCore(OriginalIntegral):
        def summary(self):
            out = super().summary()
            t, u = float(self.c[5]), float(self.c[6])
            out.update(core_kind='exact_m3_R47_fixed_slot_trace_integral',
                control_path='R47-fixed-trace-slots-5-and-6-v1',
                control_family='B2..B6,T,U,B7..B(M-2) at one; cos6..cos(3M) at zero',
                control_homotopy='The fixed-slot finite path of R47',
                physical_trace_indices=[5, 6], physical_trace_coordinates=dict(t=t, u=u),
                plateau_radius_at_one=1+self.q*self._circle_constant+t,
                circle_radius_trace_A=t, circle_center_trace_B=u-t,
                trace_radius_center_formula_applies_to_current_curve=self.lam == 1.,
                nominal_frequency_labels_are_not_endpoint_support_harmonics=True,
                defining_core_scope='R47 exact defining-integral nesting, with the original numerical evaluator and guard',
                geometry_scope='No finite inlet identity, whole-surface metric, holding, reach, or mean-height conclusion is transferred by this core factory')
            return out

    def factory(q, corrections=(), base_mode=3):
        if base_mode != 3 or len(corrections) != M-1:
            raise ValueError('The complete declared fixed-slot physical vector is required')
        return FixedSlotIntegralCore(q, corrections, base_mode, arc_nodes=1024, **frozen)

    return factory, dict(**description,
        branch='R47_fixed_slot_R44_endpoint' if lam == 1. else 'R47_fixed_slot_finite_integral_path',
        core_support_guard='Original numerical triangle/first/C2 guard, floor1e-5 and grid ceiling32768',
        full_parameter_derivatives='Inherited original fixed-material integral derivatives in the declared fixed-slot order')


PROVENANCE = dict(
    source_sha256={str(M3/name): value for name, value in {**BASIS_DEPENDENCIES, **CORE_DEPENDENCY_SHA256}.items()},
    new_basis_sha256=hashlib.sha256(Path(__file__).with_name('r47_fixed_slot_trace_basis.py').read_bytes()).hexdigest(),
    original_second_order_guard=original.PROVENANCE,
    complete_derived_source_sha256=hashlib.sha256(text.encode()).hexdigest(),
    transforms=TRANSFORMS, original_positive_lambda_rho_floor=1e-5,
    original_grid_ceiling=32768, scope=__doc__)
