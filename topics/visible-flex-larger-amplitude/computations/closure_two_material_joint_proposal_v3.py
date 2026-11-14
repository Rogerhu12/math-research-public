# Frozen v2 source SHA256 3dbe2f2f74d309960bdea8ee94d042d9b39e7bcf805b8d67e0998abd33981546; v3 applies the complete radial source column and general near material, then proposes exact dyadic test radii.
# Frozen v1 source SHA256 f50ef629864d27e342452e3f4680313a84ef43479c61431080f51caf8a80213d; v2 adds exact support zeros and complete positive-matrix contribution diagnostics.
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
from closure_split_joint_component_diagnostic import lp, lr, la, ls, rowsum, powlabel, proposal_dyadic


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('low', 'split', 'density', 'low-edge', 'low-column', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--high-edge', type=Path, action='append', required=True)
    parser.add_argument('--physical-domain-log2', type=int, default=-30)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh component diagnostic prefix')
    start = time.monotonic()
    paths = [getattr(args, n) for n in ('low', 'split', 'density', 'low_edge', 'low_column')]+args.high_edge
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
    radial_column = read(args.low_column)
    if not radial_column['full46_and_all_deeper_targets'] or radial_column['modes'] != list(range(2,93,2)):
        raise ValueError('The full actual radial source column is required')
    if radial_column['target_cells'] != cells[1:] or radial_column['source_cell'] != 12:
        raise ValueError('The complete deeper source12 range differs')
    for p in (args.low,args.density):
        if radial_column['input_hashes'].get(str(p)) != hashes[str(p)]:
            raise ValueError('The radial column uses another actual norm/source')
    if radial_column['input_hashes'].get(str(args.low_edge)) != hashes[str(args.low_edge)]:
        raise ValueError('The radial column is not based on the supplied true psi integrals')
    for r in radial_column['rows']:
        k,n=r['output_cell']-12,r['source_cell']-12
        for block,key in ((0,'DQ_corr_from_low'),(N,'DQ_corr_from_near')):
            row,col=k,block+n
            terms=dict(main=float(G['main'][k,n]),independent_two_material_corr=lr(r[key]),
                       perturbation_and_complete_remainder=float(E[k,n]))
            candidate=la(*terms.values());old=float(J[row,col])
            if candidate < old:
                J[row,col]=candidate;patch_terms[(row,col)]=terms
            patches.append(dict(row=row,column=col,old_log2=old,new_log2=float(J[row,col]),
                reason='Complete source12 independent radial column, actual strong norm and all46 target caps',terms=terms))
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
        for block in (0,N,2*N):
            row,col=N+k,block+n
            old=float(J[row,col])
            terms=dict(independent_centre_DQ=mixed,perturbation_and_complete_remainder=remainder)
            if candidate < old:
                J[row,col]=candidate;patch_terms[(row,col)]=terms
            patches.append(dict(row=row,column=col,old_log2=old,new_log2=float(J[row,col]),
                reason='R57 general near-output material: supplied2/279 also bounds high-input2/285; DQ coefficients already included',terms=terms))
    # R50 exact support: a low centre and a low variation cannot produce
    # rest>=186 or infinity>=8192 in DQ. Keep Q(variation) and the complete
    # mean/inverse derivative in those entries.
    previous_rest_low = J[2*N:3*N,:N].copy()
    previous_infinite_low = J[inf,:N].copy()
    previous_near_infinite = J[N:2*N,inf].copy()
    previous_infinite_near = J[inf,N:2*N].copy()
    high_variation_slope = np.logaddexp2(math.log2(3)+args.physical_domain_log2,
                                       math.log2(216)+A+2*one)
    J[2*N:3*N,:N] = H['rest']+high_variation_slope[None,:]
    J[inf,:N] = gamma+high_variation_slope
    J[N:2*N,inf] = rowsum(H['near']+high_variation_slope[None,:])
    J[inf,N:2*N] = gamma+high_variation_slope
    support_zero_entry_count = N*N+3*N
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
        if (2*N<=i<3*N and j<N) or (i==inf and j<2*N) or (N<=i<2*N and j==inf):
            return dict(exact_support_zero_centre_DQ=True,
                retained='Quadratic new variation and complete216 mean/inverse derivative',
                log2_complete_retained_entry=float(J[i,j]))
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
    def case_matrix(logs):
        ex = logs+scale[None,:]-scale[:,None]
        out = np.exp2(np.maximum(ex,-1074))
        out[~np.isfinite(ex)|(ex < -1074)] = 0
        return out
    def case_spectrum(logs):
        return float(np.max(np.abs(np.linalg.eigvals(case_matrix(logs)))))
    blocks = dict(low=list(range(N)), near=list(range(N,2*N)),
                  rest=list(range(2*N,3*N)), infinite=[inf], far=[zi])
    block_spectra = {}
    for name, indices in [('LL',blocks['low']),('high',list(range(N,3*N+1))),
                          ('finite_low_near',list(range(2*N))),
                          ('without_far',list(range(zi)))]:
        principal = matrix[np.ix_(indices,indices)]
        block_spectra[name] = float(np.max(np.abs(np.linalg.eigvals(principal))))
    diagnostics = {}
    candidate = J.copy()
    candidate[2*N:3*N,:N] = previous_rest_low
    candidate[inf,:N] = previous_infinite_low
    candidate[N:2*N,inf] = previous_near_infinite
    candidate[inf,N:2*N] = previous_infinite_near
    diagnostics['before_exact_rest_and_infinite_low_support_zeros'] = case_spectrum(candidate)
    candidate = J.copy(); candidate[:N,:N] = -math.inf
    diagnostics['omit_LL_for_diagnosis_only'] = case_spectrum(candidate)
    candidate = J.copy(); candidate[:N,N:3*N+1] = -math.inf
    diagnostics['omit_high_to_low_for_diagnosis_only'] = case_spectrum(candidate)
    candidate = J.copy(); candidate[N:3*N+1,:N] = -math.inf
    diagnostics['omit_low_to_high_for_diagnosis_only'] = case_spectrum(candidate)
    candidate = J.copy()
    for off in (0,N): candidate[:N,off:off+N] = np.logaddexp2(G['main'],E)
    for off in (0,N): candidate[zi,off:off+N] = np.logaddexp2(F['main']-zlog,FE)
    diagnostics['omit_low_and_far_corr_for_diagnosis_only'] = case_spectrum(candidate)
    candidate = J.copy()
    for off in (0,N): candidate[:N,off:off+N] = np.logaddexp2(G['corr']+math.log2(3),E)
    for patch in patches:
        if patch['row']<N:
            i,j=patch['row'],patch['column']
            candidate[i,j] = la(patch['terms']['independent_two_material_corr'],E[i,j%N])
    for off in (0,N): candidate[zi,off:off+N] = np.logaddexp2(F['corr']+math.log2(3)-zlog,FE)
    diagnostics['omit_low_and_far_main_for_diagnosis_only'] = case_spectrum(candidate)
    low_family_spectra = {}
    for f in G:
        addition = (0 if f=='main' else math.log2(3) if f=='corr' else
                    math.log2(3)+args.physical_domain_log2 if f=='base' else math.log2(216)+2*one)
        logs = G[f]+addition+scale[:N][None,:]-scale[:N][:,None]
        a = np.exp2(np.maximum(logs,-1074));a[~np.isfinite(logs)|(logs < -1074)] = 0
        low_family_spectra[f] = float(np.max(np.abs(np.linalg.eigvals(a))))
    del candidate
    values,vectors=np.linalg.eig(matrix)
    p=int(np.argmax(values.real));lambda_right=values[p]
    rv=vectors[:,p].real.copy();rv*=1 if rv.sum()>=0 else -1
    right_negative_count=int(np.count_nonzero(rv < -1e-10*np.max(abs(rv))))
    right=abs(rv);right/=right.sum();del vectors,values,rv
    values,vectors=np.linalg.eig(matrix.T)
    p=int(np.argmax(values.real));lambda_left=values[p]
    lv=vectors[:,p].real.copy();lv*=1 if lv.sum()>=0 else -1
    left_negative_count=int(np.count_nonzero(lv < -1e-10*np.max(abs(lv))))
    left=abs(lv);left/=left.sum();del vectors,values,lv
    pairing=float(left@right)
    if not pairing>0:raise ArithmeticError('Diagnostic Perron pairing vanished')
    flux=left[:,None]*matrix*right[None,:]/(spectral*pairing)
    stationary=left*right/pairing
    top_nodes=np.argsort(stationary)[-32:][::-1]
    flat=np.argsort(flux.ravel())[-64:][::-1]
    perron_edges=[]
    for ix in flat:
        i,j=divmod(int(ix),dim)
        perron_edges.append(dict(output=dict(index=i,**label(i,N)),input=dict(index=j,**label(j,N)),
            flux_float=float(flux[i,j]),log2_entry=float(J[i,j]),components=components(i,j)))
    block_flux={out:{inp:float(flux[np.ix_(oi,ij)].sum()) for inp,ij in blocks.items()}
                for out,oi in blocks.items()}
    perron=dict(eigenvalue_right=[float(lambda_right.real),float(lambda_right.imag)],
        eigenvalue_left=[float(lambda_left.real),float(lambda_left.imag)],
        right_negative_count=right_negative_count,left_negative_count=left_negative_count,
        right_residual_float=float(np.max(abs(matrix@right-spectral*right))),
        left_residual_float=float(np.max(abs(matrix.T@left-spectral*left))),
        total_flux=float(flux.sum()),block_flux=block_flux,
        nodes=[dict(index=int(i),**label(int(i),N),stationary_mass_float=float(stationary[i])) for i in top_nodes],
        edges=perron_edges)
    # A positive floating solve only proposes exact dyadic test objects.
    # The next strict verifier must re-evaluate all original641 rows.
    target=31/32
    pure_factor=math.log2(27/16)+float(np.max(A))
    b=np.full(dim,-math.inf)
    b[N:2*N]=np.logaddexp2(np.array([lr(r['pure_low_residual_near']) for r in split['cells']]),far['near'])
    b[2*N:3*N]=np.logaddexp2(np.array([lr(r['pure_low_residual_rest']) for r in split['cells']])+pure_factor,far['rest'])
    b[inf]=la(lr(split['pure_low_infinite_residual'])+pure_factor,deep)
    proposal=dict(status='No positive proposal has been computed',target_logical_fraction=[31,32],
        independent_far_z_log2=zlog,physical_domain_log2=args.physical_domain_log2)
    if spectral < target:
        seed=np.logaddexp2(b,rowsum(J+b[None,:]))
        if not np.isfinite(seed).all():
            raise ArithmeticError('A positive complete-coordinate proposal seed is missing')
        rhs_log=seed-scale
        shift=float(np.max(rhs_log))
        # The floor is merely a larger positive proposal seed. It changes
        # no mathematical bound and is independently checked downstream.
        rhs=np.exp2(np.maximum(rhs_log-shift,-1000))
        sol=np.linalg.solve(target*np.eye(dim)-matrix,rhs)
        bad=np.flatnonzero(sol<=0).tolist()
        proposal.update(nonpositive_coordinates=bad,floating_rhs_floor_log2=-1000,
            solve_residual_float=float(np.max(abs((target*np.eye(dim)-matrix)@sol-rhs))))
        if not bad:
            Wlog=np.log2(sol)+scale+shift
            s_log=int(math.ceil(1+float(np.max(b-Wlog))-math.log2(1-target)))
            W=[proposal_dyadic(float(v)) for v in Wlog]
            radius=[[v[0],v[1]+s_log] for v in W]
            rt=np.array([lp(v) for v in radius])
            totals=np.logaddexp2(np.logaddexp2(np.logaddexp2(rt[:N],rt[N:2*N]),rt[2*N:3*N]),rt[inf])
            proposal.update(status='Positive exact-dyadic proposal only; all641 strict gates remain to be checked',
                all_coordinates_positive=True,radius_multiple_of_metric_log2=s_log,
                max_total_state_log2_float=float(np.max(totals)),far_radius_log2_float=float(rt[zi]),
                floating_physical_domain_test=bool(np.max(totals)<args.physical_domain_log2),
                rows=[dict(index=i,**label(i,N),metric_weight=W[i],radius=radius[i]) for i in range(dim)])
        else:
            proposal['all_coordinates_positive']=False
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
        exact_support_zero_entries_applied=support_zero_entry_count,
        support_scope='DQ(low centre)low -> rest/infinite, near -> infinite and infinite -> near are zero. New quadratic and all216 mean/inverse terms retained.',
        pure_rest_and_infinite_source_improvement=dict(log2_uniform_factor=math.log2(27/16)+float(np.max(A)),
            factor_scope='The old pure-low16*d wide-strip source may be replaced by27*Amax*d for actual rest>=186 and infinite>=8192, because Q(C_low) has support<=184. This diagnostic does not alter boundary D(z) or execute a map check.',
            required='Complete centre wide-strip norm<=1, unchanged same V and tau_ref, complete mean/inverse cubic remainder<=A*(4*d1+27*d_lambda), a*X<=1/32.'),
        block_spectral_diagnostics=block_spectra, low_family_spectral_diagnostics=low_family_spectra,
        omission_spectral_diagnostics=diagnostics,perron_contribution_diagnostic=perron,
        positive_dyadic_proposal=proposal,
        omission_warning='Removing a positive family is a sensitivity diagnosis, not a valid bound or a contraction proof.',
        input_hashes=hashes,source_sha256=digest(Path(__file__)),
        helper_hashes={name:digest(Path(__file__).with_name(name)) for name in
            ('closure_split_joint_io.py','closure_split_joint_io_v2.py','closure_split_joint_component_diagnostic.py')},
        elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='done',spectral_radius_float=spectral,
        changed_entries=len(patches),positive_proposal=proposal.get('all_coordinates_positive',False),
        max_total_state_log2_float=proposal.get('max_total_state_log2_float'),largest_cycle_log2=cycles[0]['log2_product_float'],
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':
    main()
