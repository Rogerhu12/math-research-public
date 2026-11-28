"""Explicit conservative storage estimate for complete CSC and streamed QR.

This is a resource scheduling estimate, not a memory guarantee or a
mathematical acceptance test. Full stored sparsity, including zeros, bounds
every CSR copy. The recursive factor estimate counts the previous edge list,
the new edge list and all accumulated factors at their simultaneous peak.
"""
from pathlib import Path


MIB = 2**20


def budget(n, m, k, *, baseline_mib=640., misc_mib=64., external_mib=512.,
           diagnostics="streamed", assembly_block=16, diagnostic_rows=2048):
    if min(n, k) < 1 or m < 2 or min(baseline_mib, misc_mib) < 0 or external_mib < 512:
        raise ValueError("Complete design dimensions and at least 512 MiB external margin required")
    if diagnostics not in ("streamed", "full"):
        raise ValueError("Unknown complete QR diagnostic storage")
    total = n*m+k
    nnz = 2*(m-1)*n*n+2*(n+k)*n+(m-1)*n*k+(n+k)*k
    index_bytes = 4 if max(total, nnz) <= 2**31-1 else 8
    sparse = (8+index_bytes)*nnz+index_bytes*(total+1)
    partials = 8*(2*m-1)*(n*n+n*k)
    boundary = 8*(n+k)*(2*n+k)
    # The exact stored factor arrays in BlockQR; pivots have int32 dtype.
    one_factor = 8*(4*n*n+n*k)+12*n
    one_edge = 8*(2*n*n+n*k)
    edges, retained, recursive_peak = m-1, 0, (m-1)*one_edge
    while edges > 1:
        pairs, remaining = edges//2, (edges+1)//2
        recursive_peak = max(recursive_peak,
            retained+edges*one_edge+pairs*one_factor+remaining*one_edge)
        retained += pairs*one_factor
        edges = remaining
    if retained != (m-2)*one_factor:
        raise AssertionError("Complete interior-node count differs")
    # Both a yielded CSR diagnostic block and its successor can be live.
    diagnostic_blocks = 2*((8+index_bytes)*min(total, diagnostic_rows)*(2*n+k)
                           +index_bytes*(min(total, diagnostic_rows)+1))
    assembly_temporaries = 8*assembly_block*(8*n*n+4*n*k)+boundary+8*n*n
    baseline = int(baseline_mib*MIB*(n/121.)**2)
    miscellaneous = int(misc_mib*MIB)
    phases = {
        "full_partial_arrays": partials+boundary,
        "direct_CSC_assembly": partials+sparse+assembly_temporaries,
        # Conservative extra CSR during conversion/eliminate_zeros/prune.
        "CSR_conversion_and_pruning": 3*sparse,
        "recursive_QR_factorization": 2*sparse+recursive_peak,
    }
    if diagnostics == "streamed":
        phases["complete_streaming_diagnostics"] = 2*sparse+retained+diagnostic_blocks
    else:
        phases["complete_full_absolute_diagnostics"] = 3*sparse+retained+8*nnz
    process = max(phases.values())+baseline+miscellaneous
    return dict(n=n, nodes=m, parameters=k, unknowns=total, stored_entries=nnz,
        index_bytes=index_bytes, full_sparse_bytes=sparse,
        all_node_midpoint_partials_bytes=partials, final_QR_factor_bytes=retained,
        recursive_edge_and_factor_peak_bytes=recursive_peak,
        diagnostic_block_bound_bytes=diagnostic_blocks,
        assembly_temporary_bound_bytes=assembly_temporaries,
        phase_variable_bytes=phases, non_J_baseline_bytes=baseline,
        miscellaneous_allowance_bytes=miscellaneous,
        process_peak_estimate_bytes=process, external_margin_bytes=int(external_mib*MIB),
        required_at_new_process_mib=(process+external_mib*MIB)/MIB,
        diagnostics=diagnostics, all_stored_zeros_counted=True,
        old_factor_released_before_new_J=True,
        partial_arrays_released_before_QR=True,
        source_baseline="M40 original full-loader peak 510832 KiB and actual 16-node all-column check peak 534108 KiB; round upward to 640 MiB then scale the entire allowance by (n/121)^2",
        miscellaneous_scope="64 MiB for small LAPACK blocks, Python containers, field vectors, sparse conversion indices and allocator uncertainty, in addition to the explicit arrays",
        estimate_is_not_a_memory_guarantee=True,
        changes_mathematical_acceptance=False)


def memory():
    values = {line.split(":")[0]:int(line.split()[1]) for line in
              Path("/proc/meminfo").read_text().splitlines() if ":" in line}
    status = {line.split(":")[0]:line.split()[1:] for line in
              Path("/proc/self/status").read_text().splitlines() if ":" in line}
    return dict(available_bytes=values["MemAvailable"]*1024,
                total_bytes=values["MemTotal"]*1024,
                current_process_rss_bytes=int(status["VmRSS"][0])*1024)
