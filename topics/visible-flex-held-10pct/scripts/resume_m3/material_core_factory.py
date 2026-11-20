"""Insert the material-curvature core into the legacy m3 BVP interface.

The fixed numerical gauge determines the legacy parameter scales; a diagonal
coordinate transformation makes each Newton control act at ``control_scale``
in actual material curvature.  Both position and jet parameter derivatives
include that exact chain rule.  This is not the old support-coefficient family.
"""
from pathlib import Path
import sys
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'resume_transfer'))
from material_curvature_core import MaterialCurvatureCore


def make_factory(settings):
    settings = dict(settings)
    gauge = float(settings.pop('gauge_q', .02))
    scale = float(settings.pop('control_scale', .01))
    if not 0 < gauge < .124 or not scale > 0:
        raise ValueError('Positive fixed gauge and control scale required')

    class ConfiguredCore(MaterialCurvatureCore):
        def __init__(self,q,corrections=(),base_mode=3):
            count = len(corrections)
            legacy_scales = np.maximum(gauge**np.arange(2,count+2),1e-9)
            self.input_chain = np.r_[1.,scale/legacy_scales]
            super().__init__(q,np.asarray(corrections)*self.input_chain[1:],base_mode,**settings)

        def parameter_derivatives(self,theta):
            return super().parameter_derivatives(theta)*self.input_chain[:,None,None]

        def jet_parameter_derivatives(self,theta):
            return tuple(v*self.input_chain[:,None,None]
                         for v in super().jet_parameter_derivatives(theta))

        def summary(self):
            value = super().summary()
            value.update(legacy_gauge=gauge,physical_curvature_control_scale=scale,
                         original_parameter_chain=self.input_chain.tolist())
            return value

    return ConfiguredCore
