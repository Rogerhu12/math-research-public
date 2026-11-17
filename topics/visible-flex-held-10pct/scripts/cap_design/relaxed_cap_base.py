"""Longer 10% window: A1 B.65 rc.30, y<=.70, r<=1.05, z<=.85."""
from meridian_cap_base import Model as Meridian
from relaxed_envelope_base import Model as Bounded
class Model(Meridian):
 residual_jac=Bounded.residual_jac
 audit=Bounded.audit
