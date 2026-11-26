"""R70 phase controls j=2..M with the original design delta left free.

The q argument is a fixed legacy API value, never a phase unknown.  The
original fixed=False BVP keeps p0 as its additive physical delta offset.
This wrapper reuses v4's phase formula and guard without changing v4.
"""
import copy
import hashlib
import importlib.util
import math
from pathlib import Path
import sys
import numpy as np

KIND = 'warm-full-to-complementary-phase-delta-design-v5'
SCALE_RULE = dict(legacy_power_start=2, legacy_floor=1e-9,
    physical_control='d_j=phase_scale*p_(j-1) for j=2..M',
    first_phase_control='d1_identically_zero',
    parameter_zero='additive_delta_offset_from_original_physical_profile',
    q_api='fixed_original_gauge_not_a_solver_unknown')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checked_provider(settings):
    bindings = settings['implementation_sources']
    required = ('v5_factory', 'v4_factory', 'common_geometry', 'material_geometry')
    if set(bindings) != set(required):
        raise ValueError('The complete declared v5 provider bindings are required')
    for name in required:
        row = bindings[name]
        if sha(row['path']) != row['sha256']:
            raise ValueError('Changed v5 provider dependency: '+name)
    if Path(bindings['v5_factory']['path']).resolve() != Path(__file__).resolve():
        raise ValueError('The active v5 provider differs from the declared source')
    path = Path(bindings['v4_factory']['path']).resolve()
    if (Path(bindings['common_geometry']['path']).resolve() !=
            path.with_name('warm_supported_core_factory.py') or
            Path(bindings['material_geometry']['path']).resolve() !=
            path.parent.parent/'resume_transfer/material_flattened_support_core.py'):
        raise ValueError('The actual indirect geometry dependencies differ')
    name = '_v5_bound_v4_'+bindings['v4_factory']['sha256'][:16]
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        value = importlib.util.module_from_spec(spec)
        sys.modules[name] = value
        spec.loader.exec_module(value)
    return sys.modules[name]


def make_factory(settings, reference_class=None, anchor_baseline=None):
    settings = copy.deepcopy(settings)
    if (settings.get('model_kind') != KIND or
            settings.get('phase_parameter_scale_rule') != SCALE_RULE or
            settings.get('fixed_metric') is not False):
        raise ValueError('Explicit original-delta design semantics are required')
    provider = checked_provider(settings)
    if settings.get('phase_basis') != provider.BASIS_RULE:
        raise ValueError('Use the declared R70 full-to-complementary family')
    gauge = float(settings['gauge_q'])
    scale = float(settings['phase_control_scale'])
    if not (math.isfinite(gauge) and 1e-7 < gauge < .124 and
            math.isfinite(scale) and scale > 0):
        raise ValueError('Finite original gauge and positive phase scale required')
    # Only the private adapter needs v4's old API convention.  Its q input
    # is fixed exactly to gauge below, so its d1 is always exactly zero.
    private = copy.deepcopy(settings)
    private['phase_parameter_scale_rule'] = dict(legacy_power_start=2,
        legacy_floor=1e-9, physical_control='phase_scale_times_p',
        first='log(q_aux/gauge_q)')
    base = provider.make_factory(private, reference_class=reference_class,
                                anchor_baseline=anchor_baseline)

    class DeltaDesignCore(base):
        def __init__(self, q, corrections=(), base_mode=3):
            if not math.isfinite(float(q)) or float(q) != gauge:
                raise FloatingPointError('v5 requires the fixed original q API value')
            super().__init__(q, corrections, base_mode)
            if self.controls[0] != 0.:
                raise ArithmeticError('v5 first phase control must be zero')
            # This API slot is not an allowed parameter direction.  The
            # fixed=False analytic BVP also masks it before constructing J.
            self.input_chain[0] = 0.

        def summary(self):
            value = super().summary()
            for key in ('q_aux', 'q_aux_meaning', 'inherited_auxiliary_q_domain'):
                value.pop(key, None)
            value.update(core_kind=KIND, provider_version=5,
                parameter_zero_meaning=SCALE_RULE['parameter_zero'],
                q_api_meaning=SCALE_RULE['q_api'], first_phase_control=0.,
                phase_parameter_scale_rule=SCALE_RULE,
                physical_controls_equal_phase_scale_times_solver_parameters=False,
                high_phase_controls_equal_phase_scale_times_high_solver_parameters=True,
                correction_meaning='R70 material phase d2..dM; d1=0; p0 is the original physical delta offset',
                fixed_metric=False, fixed_metric_refinement=False)
            return value

    DeltaDesignCore.anchor_definition = settings
    DeltaDesignCore.baseline = base.baseline
    return DeltaDesignCore
