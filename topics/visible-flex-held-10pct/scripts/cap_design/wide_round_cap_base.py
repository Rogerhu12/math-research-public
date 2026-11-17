"""Rounder transition window: R1.3, witness .30, support .08, K12.5."""
from meridian_cap_base import Model as Meridian
from wide_round_envelope_base import Model as Bounded
class Model(Meridian):
 residual_jac=Bounded.residual_jac
 audit=Bounded.audit
