"""Full CSR-before-QR mapped storage, with complete warm-solve residency paid.

The original direct CSR assembly and its full partial arrays remain in RAM.
All original matrix/factor bytes are still counted together for complete warm
diagnostics and solves. Only explicitly released clean pages are absent from
the following recursive-QR or nonlinear phase. This phase model does not count
mapped logical bytes as available memory, does not infer a termination cause,
and is not a memory guarantee. Runtime credits use observed RssAnon only.
"""
import complete_csr_memory_budget_v2 as original
from complete_mapped_memory_budget import memory
from complete_csr_prefactor_mmap import full_backing_upper_bound

MIB = original.MIB


def budget(n, m, k, **options):
    result = original.budget(n, m, k, **options)
    if result['diagnostics'] != 'streamed':
        raise ValueError('The CSR-before-QR storage contract uses complete streamed diagnostics')
    sparse = result['full_sparse_bytes']
    factor = result['final_QR_factor_bytes']
    vectors = result['nonlinear_vector_excess_over_miscellaneous_bytes']
    initial_edges = (m-1)*8*(2*n*n+n*k)
    endpoint = 8*(n+k)*(2*n+k)
    phases = result['phase_variable_bytes']
    # Copy+byte-check uses bounded chunks. The original zero compaction writes
    # mapped storage, and the checked instance-prune policy retains its views.
    phases['CSR_conversion_and_pruning'] = sparse+24*MIB
    phases['complete_CSR_and_initial_edges_before_page_release'] = sparse+initial_edges+endpoint
    phases['recursive_QR_factorization'] = result['recursive_edge_and_factor_peak_bytes']
    # No assumption that file-backed pages stay absent during a complete solve.
    phases['complete_streaming_diagnostics'] = (sparse+factor+
        result['diagnostic_block_bound_bytes']+vectors)
    # Pay even a warm CSR during this bounded copy. The composed driver checks
    # its constructor-release observation before permitting a complete solve.
    phases['post_factor_mapping_copy_overlap'] = sparse+factor+24*MIB
    # The new complete solve wrapper requires successful DONTNEED on both
    # stores before the unchanged nonlinear code can use the returned answer.
    phases['retained_QR_and_original_nonlinear_evaluation'] = (
        result['nonlinear_working_allowance_bytes']+vectors)
    result['process_peak_estimate_bytes'] = (max(phases.values())+
        result['non_J_baseline_bytes']+result['miscellaneous_allowance_bytes'])
    result['required_at_new_process_mib'] = (
        result['process_peak_estimate_bytes']+result['external_margin_bytes'])/MIB
    result.update(storage_scope='complete_CSR_before_QR_and_all_factors_after_QR',
        complete_original_CSR_remains_anonymous=False,
        original_CSR_assembly_peak_unchanged=True,
        recursive_factor_phase_requires_actual_CSR_page_release=True,
        nonlinear_phase_requires_actual_CSR_and_factor_page_release=True,
        all_CSR_and_factor_pages_counted_in_complete_warm_solve=True,
        anonymous_RSS_is_the_only_MemAvailable_credit=True,
        mapped_logical_bytes_are_never_RSS_credit=True,
        actual_initial_edge_array_bound_bytes=initial_edges,
        actual_endpoint_array_bound_bytes=endpoint,
        disk_backing=full_backing_upper_bound(n,m,k),
        source_baseline='Actual pre-J RSS plus unchanged complete partial/CSR assembly, all matrix and factor bytes during complete warm solves, the observed nonlinear working allowance after verified clean-page release, explicit miscellaneous allowance, and at least 512MiB external margin. Only observed RssAnon can be a credit; no logical mapped byte is credited.',
        estimate_is_not_a_memory_guarantee=True,
        changes_mathematical_acceptance=False)
    return result
