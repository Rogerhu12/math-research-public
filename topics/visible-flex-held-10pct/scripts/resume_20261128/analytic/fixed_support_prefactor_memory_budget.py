"""Actual fixed-Flow budget for complete CSR-before-QR and factor mapping.

The complete original partial arrays, CSR construction, hot full matrix/factor
solves and nonlinear work remain paid. Eight-node RHS/Jacobian calls retain
every original node and component. A separate 512 MiB fixed-Flow reserve is
kept rather than claiming equality with design working peaks. Only observed
anonymous RSS is credit; mapped logical bytes are never additional RAM.
"""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'design'))
import complete_prefactor_memory_budget as shared

MIB = shared.MIB
memory = shared.memory


def budget(n, m, k, *, angular, rhs_block, jac_batch,
           grouped_reserve_mib=512., **options):
    if (n != 3*k+1 or angular < 1 or rhs_block != 8 or jac_batch != 8
            or grouped_reserve_mib < 512.):
        raise ValueError('Require the complete fixed-support dimensions, eight-node groups and fixed-Flow reserve')
    result = shared.budget(n, m, k, **options)
    reserve = int(grouped_reserve_mib*MIB)
    previous = dict(result['phase_variable_bytes'])
    result['phase_variable_bytes'] = {name:value+reserve for name,value in previous.items()}
    result['process_peak_estimate_bytes'] = (max(result['phase_variable_bytes'].values())
        +result['non_J_baseline_bytes']+result['miscellaneous_allowance_bytes'])
    result['required_at_new_process_mib'] = (result['process_peak_estimate_bytes']
        +result['external_margin_bytes'])/MIB
    result.update(original_shared_phase_variable_bytes=previous,
        fixed_live_Flow_reserve_bytes=reserve,
        fixed_execution_grouping=dict(rhs=rhs_block,jacobian=jac_batch,angular=angular),
        all_original_nodes_and_components_retained=True,
        fixed_model_uses_one_live_fixed_Flow=True,
        design_peak_claimed_as_fixed_peak=False,
        grouped_reserve_is_scheduling_allowance_not_proven_bound=True,
        fixed_phase_process_peak_bytes={name:value+result['non_J_baseline_bytes']
            +result['miscellaneous_allowance_bytes']
            for name,value in result['phase_variable_bytes'].items()})
    return result


def required_process_peak(estimate, phase):
    if phase == 'complete_nodal_before_original_J':
        return estimate['process_peak_estimate_bytes']
    names = {
        'complete_CSR_before_recursive_QR':'recursive_QR_factorization',
        'retained_QR_original_linear_solve':'complete_streaming_diagnostics',
        'retained_QR_original_nonlinear_evaluation':'retained_QR_and_original_nonlinear_evaluation'}
    if phase not in names:
        raise ValueError('An explicit complete-storage phase is required')
    return estimate['fixed_phase_process_peak_bytes'][names[phase]]
