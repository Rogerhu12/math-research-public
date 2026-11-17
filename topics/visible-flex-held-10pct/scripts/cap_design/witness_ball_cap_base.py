"""Ball diameter envelope and witness-ball exclusion for a 10% cap design."""
from meridian_cap_base import Model as Meridian
from witness_ball_envelope_base import Model as Bounded
class Model(Meridian):
 residual_jac=Bounded.residual_jac
 audit=Bounded.audit
