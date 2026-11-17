"""Analytic negative-curvature seed, free mean meridian metric within bounds."""
from meridian_cap_base import Model as Meridian
from half_cap_homotopy_base import Model as Bounded
class Model(Meridian):
 residual_jac=Bounded.residual_jac
 audit=Bounded.audit
