"""Initial negative-curvature meridian; wider enclosing ball R1.15."""
from meridian_cap_base import Model as Meridian
from negative_entry_envelope_base import Model as Bounded
class Model(Meridian):
 residual_jac=Bounded.residual_jac
 audit=Bounded.audit
