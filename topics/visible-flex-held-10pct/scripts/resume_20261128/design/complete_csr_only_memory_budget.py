"""Complete CSR mapping, with every anonymous QR factor paid during nonlinear work.

Only actual CSR mapped pages can be released. All original QR arrays stay
anonymous in every solve and original nonlinear trial. Neither factor-cold
residency nor a factor-page-release flag is used. This is a conservative phase
estimate with at least 512MiB external RAM/disk margins, not a memory guarantee.
"""
import complete_prefactor_memory_budget as previous
from complete_csr_only_mmap import full_backing_upper_bound

MIB = previous.MIB
memory = previous.memory


def budget(n, m, k, **options):
    result = previous.budget(n,m,k,**options)
    phases = result['phase_variable_bytes']
    del phases['post_factor_mapping_copy_overlap']
    phases['retained_QR_and_original_nonlinear_evaluation'] = (
        result['final_QR_factor_bytes']+result['nonlinear_working_allowance_bytes']+
        result['nonlinear_vector_excess_over_miscellaneous_bytes'])
    result['process_peak_estimate_bytes'] = (max(phases.values())+
        result['non_J_baseline_bytes']+result['miscellaneous_allowance_bytes'])
    result['required_at_new_process_mib'] = (
        result['process_peak_estimate_bytes']+result['external_margin_bytes'])/MIB
    result.update(storage_scope='complete_CSR_before_QR_with_original_anonymous_factors',
        complete_original_QR_factors_remain_anonymous=True,
        anonymous_QR_factors_paid_in_every_original_nonlinear_trial=True,
        nonlinear_phase_requires_actual_CSR_and_factor_page_release=False,
        nonlinear_phase_requires_actual_CSR_page_release=True,
        factor_page_release_claimed=False,
        mapped_logical_bytes_are_never_RSS_credit=True,
        disk_backing=full_backing_upper_bound(n,m,k),
        source_baseline='Actual pre-J RSS plus complete original partial/CSR assembly and warm solve, all original anonymous QR factors simultaneously retained during the observed original nonlinear working allowance, explicit miscellaneous allowance, and at least 512MiB external margin. Only CSR clean pages may be released, and only observed RssAnon can be credited.',
        estimate_is_not_a_memory_guarantee=True)
    return result
