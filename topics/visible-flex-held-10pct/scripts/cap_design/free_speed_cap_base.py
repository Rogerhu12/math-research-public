"""Same physical geometry gates, wider coordinate-speed gauge box."""
from meridian_cap_base import Model as Meridian
from free_speed_envelope_base import Model as Bounded
class Model(Meridian):
 residual_jac=Bounded.residual_jac
 audit=Bounded.audit
