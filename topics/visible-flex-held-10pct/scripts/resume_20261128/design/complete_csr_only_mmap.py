"""Checked CSR-before-QR mapping with every original QR factor anonymous.

This narrow composition omits only the post-construction factor mapper from
the independently checked complete-mapping composition. The same complete CSR
copy, single original zero compaction, view-prune, and QR storage callback run.
The same original recursive QR and complete solve methods retain every factor
array in anonymous memory. No factor-page release is claimed or required.
"""
import hashlib
import inspect
import textwrap

import complete_csr_prefactor_mmap as complete
from complete_csr_prefactor_mmap import BlockQR, MIB, PAGE, process_memory


def full_backing_upper_bound(n, m, k):
    bound = complete.full_backing_upper_bound(n,m,k)
    sparse = bound['full_CSR_backing_upper_bytes']
    padding = 3*(PAGE-1)
    manifest = 8*MIB
    return dict(kind='complete_CSR_before_QR_with_original_anonymous_factors',
        full_CSR_backing_upper_bytes=sparse,
        CSR_alignment_padding_upper_bytes=padding,
        CSR_manifest_allowance_bytes=manifest,
        factor_backing_bytes=0,
        complete_original_QR_factors_remain_anonymous=True,
        total_backing_and_manifest_upper_bytes=sparse+padding+manifest,
        logical_mapped_bytes_are_not_an_RSS_credit=True)


_CSR_ORIGINAL_INIT = textwrap.dedent(inspect.getsource(complete.CompleteCSRBeforeQRStore.__init__))
_FACTOR_RESERVATION = "    factor_bound = backing_upper_bound(n, m, k, 'factor-only')\n"
if _CSR_ORIGINAL_INIT.count(_FACTOR_RESERVATION) != 1:
    raise RuntimeError('The checked complete CSR allocation contract changed')
_CSR_ONLY_INIT = _CSR_ORIGINAL_INIT.replace(_FACTOR_RESERVATION,
    '    factor_bound = dict(total_backing_and_manifest_upper_bytes=0, '
    'complete_original_QR_factors_remain_anonymous=True)\n')
_CSR_NAMESPACE = dict(complete.CompleteCSRBeforeQRStore.__init__.__globals__)
exec(compile(_CSR_ONLY_INIT, '<complete-CSR-only-actual-backing-reservation>', 'exec'), _CSR_NAMESPACE)


class CompleteCSRStoreOnly(complete.CompleteCSRBeforeQRStore):
    __init__ = _CSR_NAMESPACE['__init__']


_QR_ORIGINAL_INIT = textwrap.dedent(inspect.getsource(complete.BeforeQRMappedBlockQR.__init__))
_POST_FACTOR_MAPPING = """    self._complete_store = CompleteFactorStore(self, storage_directory,
        disk_margin_bytes=disk_margin_bytes, chunk_bytes=chunk_bytes, map_scope='factor-only')
    self._complete_csr_store.stats['after_both_complete_stores'] = process_memory()
"""
if _QR_ORIGINAL_INIT.count(_POST_FACTOR_MAPPING) != 1:
    raise RuntimeError('The checked complete post-QR factor storage location changed')
_QR_CSR_ONLY_INIT = _QR_ORIGINAL_INIT.replace(_POST_FACTOR_MAPPING,
    "    self._complete_csr_store.stats['all_original_QR_factor_arrays_remain_anonymous'] = True\n"
    "    self._complete_csr_store.stats['after_CSR_mapping_with_original_anonymous_QR'] = process_memory()\n")
_QR_NAMESPACE = dict(complete.BeforeQRMappedBlockQR.__init__.__globals__)
_QR_NAMESPACE['CompleteCSRBeforeQRStore'] = CompleteCSRStoreOnly
exec(compile(_QR_CSR_ONLY_INIT, '<complete-CSR-mapped-original-QR-anonymous>', 'exec'), _QR_NAMESPACE)


class CSRBeforeQRAnonymousFactors(BlockQR):
    __init__ = _QR_NAMESPACE['__init__']

    def solve(self, rhs):
        try:
            return super().solve(rhs)
        finally:
            self._complete_csr_store.discard_after_solve()


SOURCE_CONTRACT = dict(
    checked_CSR_constructor_sha256=hashlib.sha256(_CSR_ORIGINAL_INIT.encode()).hexdigest(),
    CSR_only_reservation_constructor_sha256=hashlib.sha256(_CSR_ONLY_INIT.encode()).hexdigest(),
    checked_complete_mapping_constructor_sha256=hashlib.sha256(_QR_ORIGINAL_INIT.encode()).hexdigest(),
    omitted_post_QR_factor_mapping_constructor_sha256=hashlib.sha256(_QR_CSR_ONLY_INIT.encode()).hexdigest(),
    original_recursive_QR_constructor_unchanged=True,
    original_complete_solve_unchanged=True,
    original_apply_implementation_retained=CSRBeforeQRAnonymousFactors._apply is BlockQR._apply,
    original_triangular_solve_implementation_retained=CSRBeforeQRAnonymousFactors._solve is BlockQR._solve,
    post_QR_factor_mapping_omitted=True,
    factor_arrays_not_approximated_or_removed=True,
    anonymous_factor_pages_never_claimed_released=True)
