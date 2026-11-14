#!/usr/bin/env python3
"""Verify the same-field domain restriction before reusing parent e/DQ caps.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All parent bytes and provenance remain unchanged. This proves domination,
not newly computed old kernels or field bounds. DQ majors are positive
linear expressions in the centre Fourier caps followed by maxima/supports.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == '.gz' else b)


def ex(v):
    if isinstance(v, list):
        return F(int(v[0])) * F(2)**int(v[1])
    if 'upper' in v:
        return ex(v['upper'])
    if 'mantissa' in v:
        return F(int(v['mantissa'])) * F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']), int(v['denominator']))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Keep every completed restriction bridge')
    t0 = time.monotonic()
    ids = read(a.inputs)
    counts = {}

    def check(k, b):
        if not b:
            raise ArithmeticError('Parent restriction bridge: ' + k)
        counts[k] = counts.get(k, 0) + 1

    def checked(k):
        r = ids[k]
        check('immutable_' + k, sha(r['path']) == r['sha256'])
        return read(r['path'])

    new, old, window, low, lowparent, dq = [checked(k) for k in
        ('new_modal', 'parent_modal', 'parent_window', 'parent_low', 'parent_low_window', 'parent_dq')]
    for k in ('new_resource', 'parent_modal_resource', 'parent_window_resource',
              'parent_low_resource', 'parent_low_window_resource', 'parent_dq_resource'):
        obj = checked(k)
        check('formal_success_' + k, obj['exitcode'] == 0 and obj.get('termination_signal') is None)
    for k, obj in [('new', new), ('old', old), ('window', window), ('low', low), ('lowparent', lowparent), ('dq', dq)]:
        check('completed_' + k, obj['all_gates'] and all(obj['gates'].values()))
    check('same_original_full_modal', new['restriction_provenance']['modal_input']['sha256']
          == old['restriction_provenance']['modal_input']['sha256']
          == '0816e8e7d62bb5df1df58848dfe8ab1c9a3699210f5df9b9da7e5e31e6a18d93')
    check('same_original_axes_and_physical_norm', new['R100_axes'] == old['R100_axes']
          and new['normalization'] == old['normalization']
          and new['exact_original_continuous_strip_origin'] == old['exact_original_continuous_strip_origin']
          and ex(new['R100_envelope_scale']) == ex(old['R100_envelope_scale']) == F(257, 256))
    dn, do = new['domain'], old['domain']
    check('both_domains_simultaneous', dn['simultaneous_original_coordinates'] and do['simultaneous_original_coordinates'])
    for k in ('S_product_radius', 'T_l1_radius'):
        check('new_radius_within_parent_' + k, 0 < ex(dn[k]) <= ex(do[k]))
    check('complete_46_domain_axes', len(dn['T_coordinate_caps_by_mode']) == len(do['T_coordinate_caps_by_mode']) == 46)
    for x, y in zip(dn['T_coordinate_caps_by_mode'], do['T_coordinate_caps_by_mode']):
        check('each_new_T_axis_within_parent', 0 <= ex(x) <= ex(y))
    check('parent_field_domains_match', window['domain'] == low['domain'] == lowparent['domain'] == do)
    for obj in (window, low, lowparent):
        check('parent_field_keeps_original_modal_provenance', obj['input_identities']['modal_input']['sha256'] == ids['parent_modal']['sha256'])
    check('parent_low_keeps_its_actual_source_window', low['input_identities']['window_field']['sha256'] == ids['parent_low_window']['sha256'])
    check('parent_dq_keeps_its_actual_centre', dq['input_identities']['input']['sha256'] == ids['parent_modal']['sha256'])
    check('same_213_cells_46_modes', new['cells'] == old['cells'] == list(range(12, 225))
          and new['modes'] == old['modes'] == list(range(2, 93, 2)))
    check('same_all13_windows', window['windows'] == lowparent['windows'] == dq['windows_out'])
    check('same_positive_full_infinite_and_far', ex(window['complete_infinite_cap']) > 0
          and ex(window['fixed_far_cap']) > 0 and 0 < ex(new['far_common_on_domain']) <= ex(old['far_common_on_domain']))
    centre_summary = []
    for i, (nr, pr, dr, wr, lr) in enumerate(zip(new['rows'], old['rows'], dq['rows'], window['rows'], low['rows'])):
        check('all213_original_cell_identities', nr['cell'] == pr['cell'] == dr['cell'] == wr['cell'] == lr['cell'] == i+12)
        check('parent_DQ_common_exactly_parent_centre', ex(dr['reference_common_cap']) == ex(pr['Cs_plus_Lambda_common_cap']))
        for k in ('Cs_complete_pair_caps', 'Lambda_pair_caps_on_domain', 'Cs_plus_Lambda_pair_caps'):
            check('all46_pair_coverage_' + k, len(nr[k]) == len(pr[k]) == 46)
            for x, y in zip(nr[k], pr[k]):
                check('every_new_pair_dominated_' + k, 0 <= ex(x) <= ex(y))
        for k in ('Cs_common_cap', 'Lambda_common_cap_on_domain', 'Cs_plus_Lambda_common_cap'):
            check('each_common_dominated_' + k, 0 < ex(nr[k]) <= ex(pr[k]))
        check('all46_saved_low_and13_windows', len(lr['low_mode_caps']) == 46 and len(wr['window_caps']) == 13)
        centre_summary.append(dict(cell=i+12, new_common=nr['Cs_plus_Lambda_common_cap'],
                                   parent_common=pr['Cs_plus_Lambda_common_cap']))
    check('all213_rows_covered', len(centre_summary) == len(new['rows']) == len(old['rows'])
          == len(dq['rows']) == len(window['rows']) == len(low['rows']) == 213)
    ans = dict(schema='R150-same-R100-parent-domain-and-positive-DQ-restriction-v1',
               author='/root (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
               input_manifest_sha256=sha(a.inputs), inputs=ids, all_gates=True,
               gates={k: True for k in counts}, gate_count=sum(counts.values()), gate_categories=counts,
               new_domain=dn, parent_domain=do, centre_common_rows=centre_summary,
               pointwise_field_decomposition_unchanged='The same F(a), Cs(a), Lambda(d), and e(a)=F(a)-Cs(a)-Lambda(d) are restricted to a subset of their original simultaneous complex parameter domain.',
               parent_DQ_reuse_reason='Every original positive centre Fourier cap and common cap dominates the restricted cap. The saved positive DQ coefficients, maxima, and shared-mass supports therefore remain upper bounds on the same restricted field.',
               parent_window_low_infinite_far_bounds_restricted_without_recomputing=True,
               original_parent_bytes_and_provenance_preserved=True,
               no_parent_modal_or_source_hash_relabelled=True,
               no_new_ODE_source_integral_or_Green_kernel=True,
               no_new_source_or_complete_beta_claimed_by_bridge=True,
               elapsed_seconds=time.monotonic()-t0, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(ans, separators=(',', ':'))+'\n')
    print(json.dumps(dict(all_gates=True, gates=ans['gate_count'], sha256=sha(a.out),
                         elapsed_seconds=ans['elapsed_seconds'], peak_rss_kib=ans['peak_rss_kib'])), flush=True)


if __name__ == '__main__':
    main()
