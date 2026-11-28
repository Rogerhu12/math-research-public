"""Scheduling allowance for the original fixed Flow and its unchanged 64/32 groups.

The shared estimator counts every full CSR entry, the complete streamed QR
factorization, and retained-factor/nonlinear overlap. Its 1 GiB nonlinear
working allowance comes from the actual complete M48 design history, whose
radial groups were eight. The fixed model here instead retains its original
RHS64/Jac32 calls and one live fixed Flow. We do not assert that the design
measurement proves a bound for these different calls: add an explicit
512 MiB grouped-evaluation reserve to every phase, retain the full shared
nonlinear allowance, and report the different semantics. This is a resource
estimate, not a memory guarantee, an OOM attribution, or a mathematical gate.
"""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "design"))
import complete_csr_memory_budget_v2 as shared

MIB = shared.MIB
memory = shared.memory


def budget(n, m, k, *, angular, rhs_block, jac_batch,
           grouped_reserve_mib=512., **options):
    if (n != 3*k+1 or min(angular, rhs_block, jac_batch) < 1
            or grouped_reserve_mib < 512.):
        raise ValueError("Require the complete fixed-support dimensions and grouped reserve")
    result = shared.budget(n, m, k, **options)
    grouped = int(grouped_reserve_mib * MIB)
    previous = dict(result["phase_variable_bytes"])
    result["phase_variable_bytes"] = {
        name: value + grouped for name, value in previous.items()}
    process = (max(result["phase_variable_bytes"].values())
               + result["non_J_baseline_bytes"]
               + result["miscellaneous_allowance_bytes"])
    result.update(
        process_peak_estimate_bytes=process,
        required_at_new_process_mib=(process + result["external_margin_bytes"])/MIB,
        original_shared_phase_variable_bytes=previous,
        fixed_grouped_evaluation_reserve_bytes=grouped,
        fixed_original_grouping=dict(rhs=rhs_block, jacobian=jac_batch, angular=angular),
        shared_reference_radial_grouping=8,
        fixed_model_uses_one_live_fixed_Flow=True,
        fixed_model_uses_design_delta_plus_minus_Flows=False,
        reference_grouping_equivalence_claimed=False,
        grouped_reserve_is_scheduling_allowance_not_proven_bound=True,
        fixed_observed_v5_peak_kib=1450012,
        fixed_observed_v5_peak_is_not_final_peak_or_cause=True,
        source_baseline=("Actual current-mesh pre-J RSS; the unchanged shared full "
            "CSR/QR and nonlinear-overlap accounting; an extra 512 MiB or larger "
            "reserve for this fixed Flow's unchanged RHS64/Jac32 groups; 64 MiB "
            "miscellaneous and at least 512 MiB external margin. No equivalence "
            "between fixed and design working peaks or termination causes is inferred."))
    return result
