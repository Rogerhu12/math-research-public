#!/usr/bin/env python3
"""Actual low46 Green kernels for all25 source/target blocks and three materials.

Consume the frozen original10793 common-strip leaves and10878 signed-geometry
subpanels.  Physical sources are bounded by c_upper V**p exp(-m sigma(y)),
for p=2,1,0.  Return separate component radial suprema in fixed sigma0=1/64
and the actual common sigma(x).  Current-subpanel partial integrals are bounded
by their complete positive contributions; known dyadic prefixes/suffixes are
summed/subtracted exactly. No ODE, new source integral, or feedback closure.
Author: /root/geometry_audit (AI-assisted), 2026-11-13.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib
import json
from pathlib import Path
import resource
import sys
import time

from flint import arb, ctx, fmpq

GEOMETRY_SHA = '7b785c177478d2b960172f85286005bcc6dbdcc2de5eb2cec56bffad6c998e5d'
PARTITION_SHA = 'eefd7f38b217cc8f39801f020afddec0421595eb55ef6b1fd3563406cf45ef3c'
LEAVES_SHA = '5cbb9071fa9ba8d27815f00564b4c0e7c466719f2543867913c61ce98662f901'
AXES_SHA = '7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9'
HELPER_SHA = '987435e9cb25e8bb294623920a6d891f7c346d7762bd06055c1dc184e1950d3f'
ALGEBRA_SHA = '3eeb508e6a865ca3549bd25f2824a580a758a9f55a13a4b15bf016cc917a6bc0'
MODES = list(range(2, 93, 2))
POWERS = [2, 1, 0]
NORMS = ['sigma0', 'common_sigma']
GROUPS = [(cell, segment) for cell in (11, 10) for segment in range(9)]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('geometry', 'partition', 'leaves', 'axes', 'input-root',
                 'frozen-helper-dir', 'out-prefix'):
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--chunk-rows', type=int, default=128)
    args = ap.parse_args()
    began = time.monotonic()
    ctx.prec = 256
    if not 1 <= args.chunk_rows <= 128:
        raise ValueError('Use bounded positive source chunks with at most128 rows')
    args.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'-*')):
        raise FileExistsError('Use a fresh complete kernel output prefix')
    helper_path = args.frozen_helper_dir/'root_outer_full_linear_centre_source.py'
    algebra_path = args.frozen_helper_dir/'root_outer_actual_finite_dn4_v2.py'
    if digest(helper_path) != HELPER_SHA or digest(algebra_path) != ALGEBRA_SHA:
        raise ValueError('Frozen physical geometry/rounding helpers differ')
    sys.path.insert(0, str(args.frozen_helper_dir.resolve()))
    source = importlib.import_module('root_outer_full_linear_centre_source')
    if Path(source.__file__).resolve() != helper_path.resolve():
        raise ValueError('The imported helper must be the private frozen source')
    ids = {str(helper_path): HELPER_SHA, str(algebra_path): ALGEBRA_SHA,
           str(Path(__file__)): digest(__file__)}
    gates = {}

    def gate(name, condition):
        if not condition:
            raise ArithmeticError(name)
        gates[name] = True

    def checked(path, wanted):
        gate('identity_'+path.name, digest(path) == wanted)
        ids[str(path)] = wanted
        return read(path)

    geo = checked(args.geometry, GEOMETRY_SHA)
    comparison = checked(args.partition, PARTITION_SHA)
    axes_record = checked(args.axes, AXES_SHA)
    gate('identity_original_common_strip_leaves', digest(args.leaves) == LEAVES_SHA)
    ids[str(args.leaves)] = LEAVES_SHA
    gate('original_geometry_success', geo['all_gates'] and all(geo['gates'].values()))
    gate('comparison_partition_from_complete_actual_result', comparison['all_gates'])
    gate('original_R100_axes_success', axes_record['all_gates'])
    gate('all46_physical_modes', geo['config']['modes'] == MODES
         and [r['mode'] for r in axes_record['rows']] == MODES)
    gate('original10793_materials', geo['counts']['original_material'] == 10793)
    groups = {(g['cell'], g['segment']): g for g in geo['profile_groups']}
    gate('all18_original_groups', set(groups) == set(GROUPS))
    gate('all10878_geometry_subpanels', sum(g['subpanels'] for g in groups.values()) == 10878)
    partition = comparison['comparison_partition']
    gate('same25_ordered_comparison_blocks', len(partition) == 25)
    block_of = {}
    last_group = -1
    last_panel = 0
    for block, item in enumerate(partition):
        group = item['original_group']
        if group != last_group:
            if group != last_group+1 or item['first_panel'] != 0:
                raise ArithmeticError('Comparison partition omits an original group')
            if last_group >= 0 and last_panel != groups[GROUPS[last_group]]['original_panels']:
                raise ArithmeticError('Comparison partition omits original panels')
            last_panel = 0
            last_group = group
        if ((item['cell'], item['segment']) != GROUPS[group]
                or item['first_panel'] != last_panel
                or item['last_panel_exclusive']-item['first_panel'] != item['panels']):
            raise ArithmeticError('Comparison blocks must cover each original group in order')
        for panel in range(item['first_panel'], item['last_panel_exclusive']):
            key = (*GROUPS[group], panel)
            if key in block_of:
                raise ArithmeticError('A source/target original panel was counted twice')
            block_of[key] = block
        last_panel = item['last_panel_exclusive']
    gate('partition_covers_all_original_parents', last_group == 17
         and last_panel == groups[GROUPS[-1]]['original_panels'] and len(block_of) == 10793)

    rat = source.rat
    exact = lambda x: fmpq(int(x[0]), int(x[1]))
    qrecord = lambda x: [str(x.p), str(x.q)]

    def rounded(q):
        """A finite upward128-bit dyadic, checked against its exact input."""
        if q < 0:
            raise ArithmeticError('Positive kernel arithmetic received a negative value')
        packed = source.upper(arb(q))
        result = rat(packed)
        if result < q:
            raise ArithmeticError('Outward dyadic conversion moved down')
        return result

    def packed(q):
        return source.upper(arb(q))

    leaves = {}
    sigma = fmpq(18, 125)
    floor = fmpq(1, 64)
    leaf_order = []
    original_count = 0
    group_seen = -1
    panel_seen = -1
    x = fmpq(0)
    with gzip.open(args.leaves, 'rt') as stream:
        for line in stream:
            row = json.loads(line)
            gi = row['group']
            if gi != group_seen:
                if gi != group_seen+1 or (group_seen >= 0 and x != 1):
                    raise ArithmeticError('Original common-strip leaf group cover differs')
                group_seen, panel_seen, x = gi, -1, fmpq(0)
            if ((row['cell'], row['segment']) != GROUPS[gi]
                    or row['panel'] != panel_seen+1):
                raise ArithmeticError('Original common-strip parent order differs')
            panel_seen += 1
            dx, V, c = exact(row['dx']), rat(row['V']), rat(row['c_upper'])
            jump, loss = exact(row['common_entry_jump']), exact(row['common_continuous_loss'])
            if not (dx > 0 and 0 < V <= fmpq(1, 2**40) and c > 0
                    and rat(row['s_upper'])+rat(row['abs_ell_upper']) <= c
                    and jump >= 0 and loss >= 0 and x+dx <= 1):
                raise ArithmeticError('Actual material dominance or ordered leaf width failed')
            maximum = sigma-jump
            minimum = maximum-loss
            if not floor < minimum <= maximum <= sigma:
                raise ArithmeticError('The actual complete common strip lost its strict1/64 floor')
            key = (row['cell'], row['segment'], row['panel'])
            if key in leaves or key not in block_of:
                raise ArithmeticError('Common-strip leaf is duplicated or outside the partition')
            leaves[key] = dict(group=gi, left=x, right=x+dx, V=V, c=c,
                               sigma_min=minimum, sigma_max=maximum, block=block_of[key])
            leaf_order.append(key)
            x += dx
            sigma = minimum
            original_count += 1
    gate('all10793_original_leaves_present', original_count == 10793 and x == 1 and group_seen == 17
         and set(leaves) == set(block_of))
    gate('all_original_source_cbg_dominance_checked', original_count == 10793)
    gate('strict_common_sigma_floor_everywhere', sigma > floor)

    axes, wmin = [], []
    for m, row in zip(MODES, axes_record['rows']):
        ax = row['chosen_axis']
        axis = fmpq(int(ax['numerator']), int(ax['denominator']))
        lo, hi = source.endpoints(geo['config']['true_physical_Wronskians'][str(m)])
        if axis <= 0 or lo <= 0 <= hi or lo > hi:
            raise ArithmeticError('An original cut axis or true Wronskian is invalid')
        axes.append(axis)
        wmin.append(min(abs(lo), abs(hi)))
    gate('all46_original_axes_and_true_Wronskians', len(axes) == 46)
    fixed_weights = [rat(source.upper((1+m)*(arb(m)/64).exp()/arb(w)))
                     for m, w in zip(MODES, wmin)]

    def leaf_weights(leaf):
        """Exact common-strip extrema; source lower width and target upper width."""
        low = (-2*arb(leaf['sigma_min'])).exp()
        high = (2*arb(leaf['sigma_max'])).exp()
        pe, te = arb(1), arb(1)
        density = [[], [], []]
        common = []
        for j, m in enumerate(MODES):
            pe *= low
            te *= high
            common.append(rat(source.upper((1+m)*te/arb(wmin[j]))))
            for pi, power in enumerate(POWERS):
                density[pi].append(arb(leaf['c'])*arb(leaf['V'])**power*pe)
        return density, [fixed_weights, common]

    # totals[block][power][mode][phi/chi], with exactly stored dyadic summands.
    totals = [[[[fmpq(0), fmpq(0)] for _ in MODES] for _ in POWERS] for _ in partition]
    # Weighted columns already contain (1+m) exp(m target_width)/min|W| once.
    column_max = [[[[fmpq(0) for _ in range(4)] for _ in MODES]
                   for _ in NORMS] for _ in partition]
    first_records = []
    buffer = []
    buffer_block = None
    per_block_chunks = [[] for _ in partition]
    per_block_subpanels = [0 for _ in partition]
    first_count = 0
    parent_order = []

    def flush():
        nonlocal buffer
        if not buffer:
            return
        block = buffer_block
        number = len(per_block_chunks[block])
        path = str(args.out_prefix)+f'-source-block{block:02d}-part{number:03d}.json.gz'
        rec = source.save(path, dict(schema='low-positive-original-source-summands-v1',
            source_block=block, powers=POWERS, modes=MODES, subpanels=len(buffer), rows=buffer))
        rec.update(source_block=block, subpanels=len(buffer))
        per_block_chunks[block].append(rec)
        first_records.append(rec)
        buffer = []

    for cell, segment in GROUPS:
        last_key = None
        last_x = fmpq(0)
        last_parent = -1
        for gr in source.geometries(groups[(cell, segment)], args.input_root, ids):
            key = (cell, segment, gr['panel'])
            leaf = leaves[key]
            lo, hi = fmpq(gr['x_left']), fmpq(gr['x_right'])
            if key != last_key:
                if (gr['panel'] != last_parent+1 or lo != leaf['left']
                        or (last_key is not None and last_x != leaves[last_key]['right'])):
                    raise ArithmeticError('Physical geometry omitted an original parent interval')
                parent_order.append(key)
                density, weights = leaf_weights(leaf)
                last_parent, last_key = gr['panel'], key
            if lo != last_x or not leaf['left'] <= lo < hi <= leaf['right'] or rat(gr['local_V']) != leaf['V']:
                raise ArithmeticError('Physical geometry/V does not refine the original common-strip leaf')
            last_x = hi
            block = leaf['block']
            if buffer and block != buffer_block:
                flush()
            buffer_block = block
            terms = []
            for j, (m, *cols) in enumerate(gr['modes']):
                if m != MODES[j] or len(cols) != 6:
                    raise ArithmeticError('Complete positive physical Green column schema differs')
                col = [rat(v) for v in cols]
                if any(v < 0 for v in col):
                    raise ArithmeticError('Positive geometry contains a negative coefficient')
                for ni in range(2):
                    for k in range(4):
                        value = rounded(col[k]*weights[ni][j])
                        column_max[block][ni][j][k] = max(column_max[block][ni][j][k], value)
                line = [m]
                for pi in range(3):
                    for branch in range(2):
                        point = source.upper(arb(col[4+branch])*density[pi][j])
                        value = rat(point)
                        totals[block][pi][j][branch] += value
                        line.append(point)
                terms.append(line)
            buffer.append(dict(cell=cell,segment=segment,panel=gr['panel'],subpanel=gr['subpanel'],
                x_left=gr['x_left'],x_right=gr['x_right'],local_V=gr['local_V'],terms=terms))
            first_count += 1
            per_block_subpanels[block] += 1
            if len(buffer) == args.chunk_rows:
                flush()
        if last_x != 1 or last_parent+1 != groups[(cell, segment)]['original_panels']:
            raise ArithmeticError('Physical group cover is incomplete')
        print(json.dumps(dict(event='low_kernel_source_group',cell=cell,segment=segment,
            completed_subpanels=first_count,seconds=time.monotonic()-began)),flush=True)
    flush()
    gate('all_original_parents_and_subpanels_checked_in_order', parent_order == leaf_order and first_count == 10878)

    def stored_rows():
        count = 0
        for ch in first_records:
            if digest(ch['path']) != ch['sha256']:
                raise ArithmeticError('A saved positive source summand changed')
            data = read(ch['path'])
            if (data['source_block'] != ch['source_block'] or data['powers'] != POWERS
                    or data['modes'] != MODES or len(data['rows']) != ch['subpanels']):
                raise ArithmeticError('A saved complete source chunk changed its scope')
            for row in data['rows']:
                count += 1
                yield ch['source_block'], row
        if count != first_count:
            raise ArithmeticError('Saved positive summands have incomplete coverage')

    prefix = [[[[fmpq(0), fmpq(0)] for _ in MODES] for _ in POWERS] for _ in partition]
    suffix = [[[[v[0], v[1]] for v in material] for material in block] for block in totals]
    diagonal = [[[[[fmpq(0),fmpq(0)] for _ in MODES] for _ in NORMS]
                 for _ in POWERS] for _ in partition]
    rows = iter(stored_rows())
    second_count = 0
    for cell, segment in GROUPS:
        last_key = None
        for gr in source.geometries(groups[(cell, segment)], args.input_root, ids):
            block, row = next(rows)
            if (row['cell'],row['segment']) != (cell,segment) or any(row[k] != gr[k] for k in
                    ('panel','subpanel','x_left','x_right','local_V')):
                raise ArithmeticError('Saved summands do not match the original physical geometry')
            key = (cell,segment,gr['panel'])
            leaf = leaves[key]
            if block != leaf['block']:
                raise ArithmeticError('Saved source and target block identities differ')
            if key != last_key:
                _, weights = leaf_weights(leaf)
                last_key = key
            for j, ((m,*cols), terms) in enumerate(zip(gr['modes'],row['terms'])):
                if m != MODES[j] or terms[0] != m or len(terms) != 7:
                    raise ArithmeticError('All46 original positive modes must be retained')
                col = [rat(v) for v in cols[:4]]
                for pi in range(3):
                    vp, vc = rat(terms[1+2*pi]), rat(terms[2+2*pi])
                    after = suffix[block][pi][j][1]-vc
                    if after < 0:
                        raise ArithmeticError('Known exact positive suffix removal failed')
                    left = prefix[block][pi][j][0]+vp
                    right = after+vc
                    for ni in range(2):
                        for component in range(2):
                            value = rounded(weights[ni][j]*(col[2+component]*left+col[component]*right))
                            diagonal[block][pi][ni][j][component] = max(
                                diagonal[block][pi][ni][j][component], value)
                    prefix[block][pi][j][0] += vp
                    suffix[block][pi][j][1] = after
            second_count += 1
        print(json.dumps(dict(event='low_kernel_ordered_diagonal_group',cell=cell,segment=segment,
            completed_subpanels=second_count,seconds=time.monotonic()-began)),flush=True)
    gate('second_complete_geometry_pass', second_count == 10878 and next(rows,None) is None)
    gate('all_exact_dyadic_prefix_suffix_identities', all(
        prefix[b][p][j][0] == totals[b][p][j][0] and suffix[b][p][j][1] == 0
        for b in range(25) for p in range(3) for j in range(46)))

    targets = []
    output_coefficients = 0
    for target in range(25):
        kernels = []
        for origin in range(25):
            for pi, power in enumerate(POWERS):
                modes = []
                combined = [[],[]]
                for j,m in enumerate(MODES):
                    norms = {}
                    for ni,norm in enumerate(NORMS):
                        c = column_max[target][ni][j]
                        if origin < target:
                            pair = [rounded(totals[origin][pi][j][0]*c[2+k]) for k in range(2)]
                        elif origin > target:
                            pair = [rounded(totals[origin][pi][j][1]*c[k]) for k in range(2)]
                        else:
                            coarse = [rounded(totals[origin][pi][j][0]*c[2+k]
                                              +totals[origin][pi][j][1]*c[k]) for k in range(2)]
                            pair = [min(diagonal[target][pi][ni][j][k],coarse[k]) for k in range(2)]
                        norms[norm] = dict(P=packed(pair[0]),K=packed(pair[1]))
                        combined[ni].append(rounded(pair[0]+pair[1]))
                        output_coefficients += 2
                    modes.append(dict(mode=m,**norms))
                aggregates = {norm:dict(
                    max_mode_P_plus_K=packed(max(combined[ni])),
                    sum_modes_P_plus_K=packed(sum(combined[ni],fmpq(0))),
                    max_mode=MODES[max(range(46),key=lambda j:combined[ni][j])])
                    for ni,norm in enumerate(NORMS)}
                kernels.append(dict(source_block=origin,power=power,mode_rows=modes,aggregates=aggregates))
        path = str(args.out_prefix)+f'-target{target:02d}.json.gz'
        out = source.save(path,dict(schema='low46-three-material-block-kernel-v1',
            target_block=target,target_partition=partition[target],norms=NORMS,powers=POWERS,
            modes=MODES,kernels=kernels,
            output_norms=dict(sigma0='sum_m (1+m) exp(m/64) (sup_target |P_m|/V + sup_target |K_m|/V)',
                common_sigma='sum_m (1+m) (sup_target exp(m sigma(x)) |P_m|/V + sup_target exp(m sigma(x)) |K_m|/V)'),
            source_norm='sum_m sup_source exp(m sigma(y)) |f_m^cos(y)|/(c_bg(y) V(y)^power)',
            max_mode_aggregate_requires_common_source_mass=True,
            pointwise_sup_of_mode_sum_is_not_the_required_source_norm=True,
            separate_radial_component_suprema_before_mode_sum=True))
        out.update(target_block=target)
        targets.append(out)
    gate('all_target_source_power_mode_component_norm_entries',output_coefficients == 25*25*3*46*2*2)
    cut = []
    for origin in range(25):
        for pi,power in enumerate(POWERS):
            values = [rounded(totals[origin][pi][j][1]/(wmin[j]*axes[j])) for j in range(46)]
            cut.append(dict(source_block=origin,power=power,
                mode_rows=[dict(mode=m,raw_original_axis_cut=packed(v)) for m,v in zip(MODES,values)],
                S_max_mode=packed(max(values[:6])),T_max_mode=packed(max(values[6:])),
                S_sum_modes=packed(sum(values[:6],fmpq(0))),T_sum_modes=packed(sum(values[6:],fmpq(0))),
                max_mode_requires_source_sum_of_radial_suprema=True))
    cut_record = source.save(str(args.out_prefix)+'-cut.json.gz',dict(
        schema='low46-three-material-original-cut-kernel-v1',modes=MODES,powers=POWERS,
        rows=cut,original_axes_sha256=AXES_SHA,
        formula='Exact positive total_chi[source,power,mode] / (min_abs_true_Wronskian[mode] * original_R100_axis[mode])',
        extra_target_angular_weight=False,physical_F_rx_W_and_frame_paid_once=True))
    totals_record = source.save(str(args.out_prefix)+'-positive-totals.json.gz',dict(
        schema='low46-three-material-exact-positive-sums-v1',modes=MODES,powers=POWERS,
        block_rows=[dict(block=b,subpanels=per_block_subpanels[b],
            totals=[dict(power=power,mode_rows=[dict(mode=m,phi_exact=qrecord(totals[b][pi][j][0]),
              chi_exact=qrecord(totals[b][pi][j][1])) for j,m in enumerate(MODES)]) for pi,power in enumerate(POWERS)])
            for b in range(25)],
        exact_known_dyadic_sums=True,all_prefix_suffix_identities_paid=True))
    result = dict(schema='low46-three-material-two-strip-block-kernels-v1',scope=__doc__,
        all_gates=all(gates.values()),gates=gates,modes=MODES,powers=POWERS,norms=NORMS,
        comparison_partition=partition,original_parent_count=original_count,
        complete_geometry_subpanels=first_count,second_pass_subpanels=second_count,
        fixed_sigma=qrecord(floor),common_sigma_initial=qrecord(fmpq(18,125)),
        common_sigma_final=qrecord(sigma),common_sigma_strict_floor_margin=qrecord(sigma-floor),
        source_width='Original parent leaf minimum after its entry jump and complete continuous loss.',
        target_common_width='Original parent leaf maximum after its entry jump, before its continuous loss.',
        original_source_dominance='c_bg=s+abs(ell) <= s_upper+abs_ell_upper <= c_upper on every original leaf.',
        physical_source_prototypes='c_bg V^p exp(-m sigma(y)); bounds use original c_upper.',
        target_records=targets,cut_record=cut_record,positive_totals_record=totals_record,
        positive_source_summand_chunks=first_records,source_and_input_sha256=ids,
        max_column_scope='Requires sum_m sup_source of the weighted source coefficient masses; not sup_source sum_m.',
        sum_columns_scope='Valid if a separate common cap is assigned to every mode; does not reuse one common mass46 times.',
        offdiagonal_order='source<target uses total_phi*target_chi; source>target uses total_chi*target_phi.',
        diagonal_order='Actual within-block ordered prefix_phi and suffix_chi; each current-subpanel branch pays its full positive contribution.',
        Wronskian_divisions_per_term=1,no_extra_physical_F_or_rx=True,no_extra_balanced_frame_factor=True,
        bounded_output_chunks_below5MB=True,new_ODE_or_Node_calls=0,new_source_integral_calls=0,
        low_feedback_or_new_fixed_point_claimed=False,all_frequency_PDE_or_closed_surface_claimed=False,
        elapsed_seconds=time.monotonic()-began,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    record = source.save(str(args.out_prefix)+'-summary.json',result)
    print(json.dumps(dict(event='low_block_three_material_kernels_complete',all_gates=result['all_gates'],
        output=record,target_files=len(targets),coefficients=output_coefficients,cut_coefficients=25*3*46,
        seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__ == '__main__':
    main()
