#!/usr/bin/env python3
"""Actual finite collar geometry with centered finite trigonometric jets.

This changes only the enclosure of known phase functions on angle cells.
The root coordinate functions, actual object, radial Taylor budgets, and
exact source identities are identical to the base finite-collar engine.
"""
from flint import acb
from fourfold_phase_canonical_collar_finite import PhysicalRootGeometry
from fourfold_phase_canonical_root_jets import real_jet
from fourfold_phase_root_potential_complex_strip import ComplexRootModel


class CenteredPhysicalRootGeometry(PhysicalRootGeometry):
    def phases(self, angle):
        beta, gamma = ComplexRootModel.complex_phases(self, acb(angle))
        # The true phase and every retained mixed derivative are real for
        # real theta, real r, and the shared real parameter interval.
        return real_jet(beta), real_jet(gamma)
