"""R65 phase family with the actual warped-BVP parameter scale contract.

The v1 mathematical core evaluator is retained. This version changes only
the parameter-to-control diagonal: the original warped BVP really uses
max(gauge**j,1e-9), so d_j=phase_scale*p_(j-1) for every j. The whole
anchor, gauge, window, lambda and finite core guards keep their meanings.
"""
import importlib.util
import math
from pathlib import Path
import sys
import numpy as np


def _base_provider():
    name='_warm_supported_v2_geometry_base'
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
    rule=settings.get('phase_parameter_scale_rule')
    required=dict(legacy_power_start=2,legacy_floor=1e-9,
                  physical_control='phase_scale_times_p',first='log(q_aux/gauge_q)')
    if rule!=required:
        raise ValueError('The explicit actual warped-BVP scale rule is required')
    old=_base_provider()
    anchor=old.make_factory(settings,reference_class=reference_class,
                            anchor_baseline=anchor_baseline).baseline
    gauge=float(settings['gauge_q'])
    scale=float(settings['phase_control_scale'])

    class ConfiguredCore(old.SupportedIncrementCore):
        def __init__(self,q,corrections=(),base_mode=3):
            if base_mode!=3:
                raise ValueError('Only the declared threefold phase family is supported')
            legacy=np.asarray(corrections,float)
            if not np.isfinite(q) or q<=0 or not np.all(np.isfinite(legacy)):
                raise FloatingPointError('Finite positive auxiliary coordinate and controls required')
            scales=np.maximum(gauge**np.arange(2,len(legacy)+2),1e-9)
            physical=np.r_[scale*math.log(float(q)/gauge),scale*legacy/scales]
            chain=np.r_[scale/float(q),scale/scales]
            super().__init__(anchor,physical,input_chain=chain,q_aux=q,gauge_q=gauge)
            self.phase_control_scale=scale
            self.actual_legacy_scales=scales

        def summary(self):
            result=super().summary()
            result.update(provider_version=2,
                phase_parameter_scale_rule=rule,
                actual_legacy_scales=self.actual_legacy_scales.tolist(),
                physical_controls_equal_phase_scale_times_solver_parameters=True)
            return result

    ConfiguredCore.anchor_definition=settings
    ConfiguredCore.baseline=anchor
    return ConfiguredCore
