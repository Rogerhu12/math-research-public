"""Include the observed retained-factor/nonlinear-evaluation memory phase.

The original complete CSR/QR accounting remains intact.  The additional
phase retains the full original CSR and every QR factor while the original
line search constructs a new physical core/Flow and evaluates complete
residuals.  Its working allowance is anchored to the actual M48 run, not to
the much smaller first-factor snapshot.  This is a scheduling estimate,
not an explanation of any signal termination or a memory guarantee.
"""
import math

import complete_csr_memory_budget as previous

MIB = previous.MIB
memory = previous.memory

# Actual scalar observations from the closed original .128/M48 run.
REFERENCE_N = 145
REFERENCE_M = 952
REFERENCE_K = 48
REFERENCE_INITIAL_RSS = 189489152
REFERENCE_OBSERVED_PROCESS_PEAK = 2300604*1024
REFERENCE_WORKING_ALLOWANCE = 1024*MIB
REFERENCE_RECORD_SHA256 = '029a2d9916f78b087187d86b851c050bdc6f1963c747ae9af242c232f3d247d5'


def budget(n, m, k, **options):
    result = previous.budget(n, m, k, **options)
    reference = previous.budget(REFERENCE_N, REFERENCE_M, REFERENCE_K,
                               baseline_mib=REFERENCE_INITIAL_RSS/MIB)
    reference_retained = reference['full_sparse_bytes']+reference['final_QR_factor_bytes']
    observed_extra = max(0, REFERENCE_OBSERVED_PROCESS_PEAK-
                         REFERENCE_INITIAL_RSS-reference_retained)
    if REFERENCE_WORKING_ALLOWANCE < observed_extra:
        raise AssertionError('Nonlinear allowance must exceed the observed full-process excess')
    # Original inlet quadrature uses N=max(2048,64M), while the controlled
    # full design uses nt=32M. Parameter/angle and basis/angle products bound
    # the dominant work dimensions; radial batching remains at eight.
    work_scale = max(1., k*max(2048, 64*k)/(REFERENCE_K*3072),
                     n*(32*k)/(REFERENCE_N*1536))
    working = math.ceil(REFERENCE_WORKING_ALLOWANCE*work_scale)
    # Sixteen complete nodal vectors cover the concurrently retained old/new
    # collocation fields and steps. The existing miscellaneous allowance
    # already pays the first part; count only any excess for larger meshes.
    vectors = 16*8*n*m
    vector_excess = max(0, vectors-result['miscellaneous_allowance_bytes'])
    retained = result['full_sparse_bytes']+result['final_QR_factor_bytes']
    result['phase_variable_bytes']['retained_QR_and_original_nonlinear_evaluation'] = (
        retained+working+vector_excess)
    process = (max(result['phase_variable_bytes'].values())+
               result['non_J_baseline_bytes']+result['miscellaneous_allowance_bytes'])
    result.update(process_peak_estimate_bytes=process,
        required_at_new_process_mib=(process+result['external_margin_bytes'])/MIB,
        nonlinear_working_allowance_bytes=working,
        complete_nonlinear_vector_bound_bytes=vectors,
        nonlinear_vector_excess_over_miscellaneous_bytes=vector_excess,
        retained_CSR_and_QR_bytes=retained,
        nonlinear_work_scale=work_scale,
        actual_reference=dict(n=REFERENCE_N, nodes=REFERENCE_M, parameters=REFERENCE_K,
            initial_RSS_bytes=REFERENCE_INITIAL_RSS,
            observed_whole_process_peak_bytes=REFERENCE_OBSERVED_PROCESS_PEAK,
            retained_CSR_and_QR_bytes=reference_retained,
            observed_peak_excess_beyond_initial_RSS_and_retained_matrix_factor_bytes=observed_extra,
            working_allowance_bytes=REFERENCE_WORKING_ALLOWANCE,
            excess_allowance_above_observation_bytes=REFERENCE_WORKING_ALLOWANCE-observed_extra,
            record_sha256=REFERENCE_RECORD_SHA256),
        transient_core_and_Flow_evaluation_counted_with_retained_full_factor=True,
        resource_termination_cause_inferred=False,
        source_baseline='Actual current pre-J RSS plus the original complete CSR/QR phase bounds, explicit original nonlinear working overlap, 64MiB miscellaneous allowance and at least 512MiB external margin. The M48 reference includes all four original factors and line-search evaluations, not only its first solve.',
        estimate_is_not_a_memory_guarantee=True)
    return result
