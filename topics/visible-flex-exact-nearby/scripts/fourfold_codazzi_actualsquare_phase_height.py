"""Exact core/phase/vertical-translation bordered action, in caller units.

The caller supplies the original directed arithmetic and complete graph
actions. No numerical backend, default zero port, or spatial cutoff is used.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class CoreCoordinates:
    low_waist: object
    root_even96: object
    nonmean_phase: object
    exterior_ports: object


def recover_high(coords, metric, *, inverse_high, projected_rhs,
                 projected_KQ, projected_U, projected_g, projected_ports):
    """Recover on the whole original high space, before any physical row."""
    return inverse_high(projected_rhs - projected_KQ(coords.low_waist)
                        - projected_U(coords.root_even96) - projected_g * metric
                        - projected_ports(coords.exterior_ports))


def recover_scalars(phase_at_zero, height_at_zero, phase_rhs, height_rhs,
                    phase_particular, height_particular, excludes_zero):
    """HP/PP on the same strict particular and one free absolute translation."""
    if not excludes_zero(phase_particular):
        raise ValueError("the whole directed phase pivot must exclude zero")
    metric = (phase_rhs - phase_at_zero) / phase_particular
    translation = height_rhs - height_at_zero - height_particular * metric
    return metric, translation


def evaluate_reduced_rows(coords, *, phase_rhs, height_rhs, phase_particular,
                          height_particular, excludes_zero, evaluate_zero,
                          regular_particular, regular_translation):
    """evaluate_zero returns whole residual D z-f and absolute P z,H z.

    The residual includes the low waist, c-Theta u, nonmean raw phase and
    any independent physical/exterior rows. regular_particular includes
    the response of high recovery to the metric column; it and the scalar
    particular readings must refer to exactly the same splitting.
    """
    residual, phase_at_zero, height_at_zero = evaluate_zero(coords)
    metric, translation = recover_scalars(
        phase_at_zero, height_at_zero, phase_rhs, height_rhs,
        phase_particular, height_particular, excludes_zero)
    return residual + regular_particular * metric + regular_translation * translation
