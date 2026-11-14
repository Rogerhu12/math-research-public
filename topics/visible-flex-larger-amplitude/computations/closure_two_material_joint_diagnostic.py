#!/usr/bin/env python3
"""Float-only full641 diagnosis after individually certified material edges.

This retains the old complete common-strip strong problem.  It changes
only explicitly supplied, fully covered centre-quadratic derivative
entries; all perturbation quadratic, mean/inverse and true far terms stay.
No eigenvalue, cycle or test weight printed by this script is a proof.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import json
import math
from pathlib import Path
import resource
import time

import numpy as np
from closure_split_joint_io_v2 import digest, read, iter_array, metadata_without_array, label, validate_common
from closure_split_joint_component_diagnostic import lp, lr, la, ls, rowsum, powlabel


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('low', 'split', 'density', 'low-edge', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--high-edge', type=Path, action='append', required=True)
    parser.add_argument('--physical-domain-log2', type=int, default=-30)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh component diagnostic prefix')
    start = time.monotonic()
    paths = [getattr(args, n) for n in ('low', 'split', 'density', 'low_edge')]+args.high_edge
    hashes = {str(p): digest(p) for p in paths}
    low = read(args.low)
    split = metadata_without_array(args.split, 'gamma_rows')
    density = read(args.density)
    cells = validate_common(low, split, density, hashes, args.density)
    N = len(cells)
    dim, inf, zi = 3*N+2, 3*N, 3*N+1
    G = {f: np.array([[lp(x) for x in row] for row in low['gamma_upper'][f]])
         for f in ('main', 'corr', 'base', 'remainder')}
    F = {f: np.array([lp(x) for x in low['far_z_source_upper'][f]]) for f in G}
    zlog = split['z_log2']
    cdlog = powlabel(low['raw_D_constant'])
    beta = np.array([lr(r['B_low'])+2+cdlog+2*zlog for r in low['rows']])
    beta_z = lr(low['E_B_low'])+2+cdlog+zlog
    del low
    A = np.array([lr(r['V_over_w_upper']) for r in density['rows']])
    gamma = lr(density['gamma_high'])
    del density
    far = {g: np.array([lr(r['far_boundary_'+g]) for r in split['cells']]) for g in ('near', 'rest')}
    deep = lr(split['deep_high_boundary'])
    H = {g: np.full((N, N), -math.inf) for g in ('near', 'rest')}
    band = {g: np.full((N, N), -1, dtype=int) for g in H}
    count = 0
    for k, row in enumerate(iter_array(args.split, 'gamma_rows')):
        if row['output_cell'] != cells[k] or len(row['sources']) != N-k:
            raise ValueError('The complete causal row changed')
        for n, item in enumerate(row['sources'], k):
            if item['source_cell'] != cells[n]:
                raise ValueError('The complete causal source changed')
            for g in H:
                H[g][k,n] = lr(item[g+'_gamma'])
                band[g][k,n] = item[g+'_maximizing_band']
            count += 1
    if count != N*(N+1)//2:
        raise ValueError('Both full causal triangles are required')
    one = math.log2(1+math.exp2(args.physical_domain_log2))
    C = np.logaddexp2(G['main'], G['corr']+math.log2(3))
    E = np.logaddexp2(G['base']+math.log2(3)+args.physical_domain_log2,
                     G['remainder']+math.log2(216)+2*one)
    F0 = np.logaddexp2(F['main'], F['corr']+math.log2(3))-zlog
    FE = np.logaddexp2(F['base']+math.log2(3)+args.physical_domain_log2,
                      F['remainder']+math.log2(216)+2*one)-zlog
    slopes = np.logaddexp2(math.log2(3)+one, math.log2(216)+A+2*one)
    HN, HR, IC = H['near']+slopes[None,:], H['rest']+slopes[None,:], gamma+slopes
    J = np.full((dim, dim), -math.inf)
    for off in (0, N):
        J[:N,off:off+N] = np.logaddexp2(C,E)
    J[:N,2*N:3*N], J[:N,inf], J[:N,zi] = E, rowsum(E), beta
    for off, mat, g in ((N,HN,'near'),(2*N,HR,'rest')):
        for column in (0,N,2*N):
            J[off:off+N,column:column+N] = mat
        J[off:off+N,inf], J[off:off+N,zi] = rowsum(mat), far[g]+2
    for off in (0,N,2*N):
        J[inf,off:off+N] = IC
    J[inf,inf], J[inf,zi] = ls(IC), deep+2
    for off in (0,N):
        J[zi,off:off+N] = np.logaddexp2(F0,FE)
    J[zi,2*N:3*N], J[zi,inf], J[zi,zi] = FE, ls(FE), beta_z
    patches = []
    patch_terms = {}
    edge = read(args.low_edge)
    if not edge['full_low46_window_covered'] or edge['modes'] != list(range(2,93,2)):
        raise ValueError('The independently bounded low source must cover all46 modes')
    for p in (args.low,args.density):
        if hashes[str(p)] not in edge['input_hashes'].values():
            raise ValueError('The actual low-edge source/norm differs')
    k, n = edge['target_cell']-12, edge['source_cell']-12
    for block, key in ((0,'DQ_corr_low_from_low_for_listed_modes'),
                       (N,'DQ_corr_low_from_near_for_listed_modes')):
        row, col = k, block+n
        terms = dict(main=float(G['main'][k,n]),
                     independent_two_material_corr=lr(edge[key]),
                     perturbation_and_complete_remainder=float(E[k,n]))
        candidate = la(*terms.values())
        old = float(J[row,col])
        J[row,col] = min(J[row,col], candidate)
        patches.append(dict(row=row,column=col,old_log2=old,new_log2=float(J[row,col]),
                            reason='Independent full46 radial source plus separate lambda coefficient', terms=terms))
        patch_terms[(row,col)] = terms
    covers = {}
    for p in args.high_edge:
        d = read(p)
        if d['target_density_sha256'] != hashes[str(args.density)]:
            raise ValueError('The true high material uses another norm/source')
        if not d['full_mean_inverse_remainder_unchanged'] or not d['complete_quadratic_new_variation_unchanged']:
            raise ValueError('The supplied material must retain the complete nonlinear remainder')
        for b in d['bands']:
            support = (b['first_mode'], b['last_mode'])
            for r in b['rows']:
                pair = (r['output_cell']-12, r['source_cell']-12)
                if support in covers.setdefault(pair, {}):
                    raise ValueError('A near-band cover was supplied twice')
                covers[pair][support] = lr(r['gamma']['low_to_near_quadratic'])
    expected = {(94,96),(98,104),(106,112),(114,128),(130,192)}
    for (k,n), cover in covers.items():
        if set(cover) != expected:
            raise ValueError('The supplied true near derivative must cover all94..184')
        mixed = max(cover.values())
        remainder = la(math.log2(3)+args.physical_domain_log2,
                       math.log2(216)+A[n]+2*one)+H['near'][k,n]
        candidate = la(mixed,remainder)
        row, col = N+k,n
        old = float(J[row,col])
        J[row,col] = min(J[row,col],candidate)
        terms = dict(independent_centre_DQ=mixed,perturbation_and_complete_remainder=remainder)
        patches.append(dict(row=row,column=col,old_log2=old,new_log2=float(J[row,col]),
            reason='Full five-window independent high material, DQ coefficients already included',terms=terms))
        patch_terms[(row,col)] = terms
    scale = np.zeros(dim)
    history = []
    for iteration in range(128):
        y = rowsum(J+scale[None,:])
        ratios = y-scale
        if iteration in (0,3,15,31,63,127):
            history.append(dict(iteration=iteration+1,
                collatz_log2_lower_float=float(np.min(ratios)),collatz_log2_upper_float=float(np.max(ratios))))
        scale = y-np.max(y)
    scale = np.floor(scale)
    exponents = J+scale[None,:]-scale[:,None]
    if np.max(exponents)>1000:
        raise ArithmeticError('The full641 diagnostic scaling overflows')
    matrix = np.exp2(np.maximum(exponents,-1074))
    matrix[~np.isfinite(exponents)|(exponents < -1074)] = 0
    spectral = float(np.max(np.abs(np.linalg.eigvals(matrix))))
    def components(i,j):
        if (i,j) in patch_terms:
            return dict(patched=True,log2_summands=patch_terms[(i,j)])
        if i<N and j<3*N:
            n=j%N
            terms=dict(perturbation_and_complete_remainder=float(E[i,n]))
            if j<2*N:
                terms.update(main=float(G['main'][i,n]),corr=float(G['corr'][i,n]+math.log2(3)))
            return dict(log2_summands=terms)
        if N<=i<3*N and j<3*N:
            g='near' if i<2*N else 'rest';k=i%N;n=j%N
            return dict(group=g,source_cell=n+12,target_cell=k+12,
                log2_raw_gamma=float(H[g][k,n]),maximizing_band=int(band[g][k,n]),
                log2_full_slope=float(slopes[n]))
        return dict(log2_entry=float(J[i,j]))
    ii,jj=np.triu_indices(dim,1)
    values=J[ii,jj]+J[jj,ii]
    indices=np.argsort(values)[-20:][::-1]
    cycles=[dict(first=dict(index=int(ii[p]),**label(int(ii[p]),N)),
                 second=dict(index=int(jj[p]),**label(int(jj[p]),N)),
                 log2_product_float=float(values[p]),
                 forward=components(int(ii[p]),int(jj[p])),
                 reverse=components(int(jj[p]),int(ii[p]))) for p in indices]
    result=dict(status='Float-only full641 diagnosis; no joint self-map or contraction gate paid',
        full641_dimension=dim, physical_domain_log2=args.physical_domain_log2,
        complete_old_range_preserved=True, matrix_entry_changes=patches,
        spectral_radius_float=spectral,power_history=history,two_cycles=cycles,
        full_mean_inverse_quadratic_far_preserved=True,
        input_hashes=hashes,source_sha256=digest(Path(__file__)),
        helper_hashes={name:digest(Path(__file__).with_name(name)) for name in
            ('closure_split_joint_io.py','closure_split_joint_io_v2.py','closure_split_joint_component_diagnostic.py')},
        elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='done',spectral_radius_float=spectral,
        changed_entries=len(patches),largest_cycle_log2=cycles[0]['log2_product_float'],
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':
    main()
