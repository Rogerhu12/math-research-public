#!/usr/bin/env python3
"""Explicit v2 design controls supported inside the nonaxisymmetric prefix.

The zero-control scalar profile is identical to the prior complete profile.
Three distinct prefix supports replace its prefix/turn/coast supports.  This
is a new design family, motivated by the actual coast-control rank failure;
it is not a claim that the new three response columns are independent.
Every support and polynomial convention is serialized so solved controls
cannot later be reconstructed using the old control locations.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import numpy as np

from geometry_20261114_full_scalar_profile import CompleteProfile, FrozenCompleteProfile, ScalarBump
from geometry_20261114_full_dn_readout import exact_profile_formula as legacy_profile_formula


HERE = Path(__file__).resolve().parent
SCHEMA = "complete-prefix-controls-scalar-profile-v2"
SCHEME = "three-nonaxisymmetric-prefix-intervals-v1"
POLYNOMIAL = dict(normalized_coefficients=[0,0,0,64,-192,192,-64],
                  normalized_coordinate="x=(s-left)/(right-left)",
                  prefactor="(right-left)^2",zero_extension=True,continuity_order=2)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class PrefixControlsProfile(CompleteProfile):
    def __init__(self,accepted,port,peak_curvature=2.5,tail_modes=None,*,supports=None):
        super().__init__(accepted,port,peak_curvature,tail_modes)
        if self.parameter_count != 3:
            raise ValueError("This separately named design has exactly three scalar controls")
        if supports is None:
            supports = [[.05*self.prefix_end,.30*self.prefix_end],
                        [.35*self.prefix_end,.60*self.prefix_end],
                        [.65*self.prefix_end,.90*self.prefix_end]]
        supports = np.asarray(supports,float)
        if (supports.shape != (3,2) or not np.all(np.isfinite(supports)) or
                np.any(supports[:,0] <= 0) or np.any(supports[:,1] >= self.prefix_end) or
                np.any(supports[:,1] <= supports[:,0]) or
                np.any(supports[1:,0] <= supports[:-1,1])):
            raise ValueError("Use three ordered, disjoint, interior nonaxisymmetric-prefix supports")
        self.bumps = [ScalarBump(left,right) for left,right in supports]
        self.knots = sorted(set([*self.knots,*supports.ravel().tolist()]))
        self.control_scheme = SCHEME

    def description(self):
        result = super().description()
        result.update(scope=__doc__,control_scheme=SCHEME,control_polynomial=POLYNOMIAL,
                      control_supports_binary64=[[b.left,b.right] for b in self.bumps],
                      zero_control_base_profile_unchanged=True,
                      all_three_control_supports_inside_accepted_nonaxisymmetric_prefix=True,
                      control_response_full_rank_claimed=False,
                      profile_source_sha256=sha(__file__))
        return result


def scalar_spec(profile,port,parameters,accepted_sha256):
    if not isinstance(profile,PrefixControlsProfile):
        raise TypeError("A v2 control specification must be written by its actual profile")
    return dict(schema=SCHEMA,control_scheme=SCHEME,
        accepted_prefix_sha256=accepted_sha256,
        base_prefix_geometry=profile.fixed_geometry,base_prefix_end=profile.prefix_end,
        base_prefix_M=profile.M,peak_curvature=profile.turn.K,tail_modes=profile.tail_modes,
        complete_original_port=port,frozen_design_parameters=np.asarray(parameters).tolist(),
        control_supports_binary64=[[b.left,b.right] for b in profile.bumps],
        control_polynomial=POLYNOMIAL,profile_source_sha256=sha(__file__),
        original_base_profile_source_sha256=sha(HERE/"geometry_20261114_full_scalar_profile.py"),
        canonical_material_metric="ds^2+a(s;this exact frozen control specification)^2*dtheta^2")


def reconstruct_profile(geometry):
    if geometry.get("schema") != SCHEMA:
        return legacy_profile_formula(geometry)
    if (geometry.get("control_scheme") != SCHEME or geometry.get("control_polynomial") != POLYNOMIAL or
            geometry.get("profile_source_sha256") != sha(__file__) or
            geometry.get("original_base_profile_source_sha256") != sha(HERE/"geometry_20261114_full_scalar_profile.py")):
        raise ValueError("The frozen v2 scalar formula/source differs; do not reconstruct it with old supports")
    source = dict(success=True,M=geometry["base_prefix_M"],
                  fixed_scalar_profile=dict(geometry=geometry["base_prefix_geometry"]),
                  mesh=[geometry["base_prefix_end"]])
    designed = PrefixControlsProfile(source,geometry["complete_original_port"],
        geometry["peak_curvature"],geometry["tail_modes"],supports=geometry["control_supports_binary64"])
    return FrozenCompleteProfile(designed,geometry["frozen_design_parameters"])
