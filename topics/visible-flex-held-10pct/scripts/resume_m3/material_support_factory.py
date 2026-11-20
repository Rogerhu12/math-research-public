"""Adapt the R53 physical support-parameter factory to the portable m3 driver.

The driver detects a factory's jet_parameter_derivatives attribute before
installing its existing analytical lift Jacobian. For positive homotopy the
returned objects implement exactly that method. At zero homotopy the original
support object is returned unchanged and the driver's finite-difference
fallback remains available.
"""
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'resume_transfer'))
from fixed_metric_mode3_core import PlanarSupportCore as OriginalSupportCore
from material_flattened_support_core import (
    MaterialFlattenedSupportCore, make_factory as make_physical_factory)


def make_factory(settings):
    result=make_physical_factory(OriginalSupportCore,settings)
    if float(settings.get('homotopy',0.))>0.:
        result.jet_parameter_derivatives=MaterialFlattenedSupportCore.jet_parameter_derivatives
    return result
