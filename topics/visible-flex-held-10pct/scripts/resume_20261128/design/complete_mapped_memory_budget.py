"""Explicit factor-only scratch-backed full-J and nonlinear storage phases.

Full original CSR/QR construction is unchanged and remains in the RAM
budget. The complete anonymous CSR remains live in every solve and nonlinear
trial. Only after the inherited complete solve returns are all mapped QR
pages advised DONTNEED; the following original nonlinear evaluation therefore
does not require all factor pages to remain resident. Warm solve residency
and copying overlap are still budgeted separately. Clean mapped bytes never
become an RSS credit against MemAvailable. This is not a memory guarantee.
"""
from pathlib import Path

import complete_csr_memory_budget_v2 as previous
from complete_factor_mmap import backing_upper_bound, MIB


def memory():
    result = previous.memory()
    status = {line.split(':')[0]:line.split()[1:] for line in
              Path('/proc/self/status').read_text().splitlines() if ':' in line}
    if 'RssAnon' not in status:
        raise MemoryError('Anonymous RSS is required for the mapped-storage credit')
    result['current_process_anonymous_RSS_bytes'] = int(status['RssAnon'][0])*1024
    result['current_process_file_RSS_bytes'] = int(status.get('RssFile', ['0'])[0])*1024
    return result


def budget(n, m, k, **options):
    result = previous.budget(n, m, k, **options)
    sparse = result['full_sparse_bytes']
    factor = result['final_QR_factor_bytes']
    working = result['nonlinear_working_allowance_bytes']
    vectors = result['nonlinear_vector_excess_over_miscellaneous_bytes']
    result['phase_variable_bytes']['retained_QR_and_original_nonlinear_evaluation'] = (
        sparse+working+vectors)
    # The original constructor and complete warm-residency diagnostics remain
    # untouched in the existing phase map. Bounded copy+byte-check work is extra.
    result['phase_variable_bytes']['post_factor_mapping_copy_overlap'] = sparse+factor+24*MIB
    result['process_peak_estimate_bytes'] = (max(result['phase_variable_bytes'].values())+
        result['non_J_baseline_bytes']+result['miscellaneous_allowance_bytes'])
    result['required_at_new_process_mib'] = (
        result['process_peak_estimate_bytes']+result['external_margin_bytes'])/MIB
    result.update(map_scope='factor-only', original_CSR_remains_complete_and_anonymous=True,
        original_J_and_QR_construction_peak_unchanged=True,
        warm_full_mapped_factor_residency_remains_budgeted=True,
        mapped_pages_released_before_original_nonlinear_trial=True,
        anonymous_RSS_is_the_only_MemAvailable_credit=True,
        mapped_logical_bytes_are_never_RSS_credit=True,
        disk_backing=backing_upper_bound(n,m,k,'factor-only'),
        source_baseline='Actual current pre-J RSS. Only observed RssAnon may be credited; mapped logical bytes and clean mapped residency are not credited against MemAvailable. All original construction and complete warm solve phases remain included, plus nonlinear work after explicit page release.',
        estimate_is_not_a_memory_guarantee=True)
    return result
