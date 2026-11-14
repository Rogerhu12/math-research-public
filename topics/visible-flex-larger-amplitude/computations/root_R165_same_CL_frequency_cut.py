#!/usr/bin/env python3
"""Replace only old C-dependent cut coefficients using the proved finite CL spectrum.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This is a finite posterior for the same real fixed point. The full saved
quadratic/high/mean/inverse/T contributions remain; no ODE is recomputed.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time
from flint import ctx, fmpq as Q


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise FileExistsError('Preserve each actual result')
    ctx.prec,ctx.threads=256,1;started=time.monotonic();ids=json.loads(a.inputs.read_text())
    spec=importlib.util.spec_from_file_location('low_support',ids['low_helper']['path'])
    low=importlib.util.module_from_spec(spec);spec.loader.exec_module(low)
    gates={}
    def gate(name,ok):
        gates[name]=bool(ok)
        if not ok:raise ArithmeticError(name)
    for name,r in ids.items():gate('identity_'+name,low.sha(r['path'])==r['sha256'])
    read=lambda name:low.read(ids[name]['path'])
    done=lambda r:r['exitcode']==0 and r['termination_signal'] is None
    seed,old,centre=read('R164'),read('R156'),read('R155')
    gate('complete_same_field_posterior',seed['all_gates'] and all(seed['gates'].values())
         and done(read('R164_resource')) and seed['same_unique_R143_fixed_point']
         and seed['complete_mean_inverse_infinite_high_and_shared_T_retained']
         and seed['inputs']['R156']['sha256']==ids['R156']['sha256'])
    gate('same_actual_CL_not_redefined',old['all_gates'] and all(old['gates'].values())
         and centre['all_gates'] and all(centre['gates'].values())
         and done(read('R155_resource')) and centre['same_CL_as_R101_R124_R127_and_R153']
         and centre['no_centre_redefinition'] and not centre['unknown_field_or_unknown_infinite_tail_widened']
         and old['inputs']['R155_centre_source']['sha256']==ids['R155']['sha256'])
    outer=read('original_outer_inputs')
    gate('same_original_source_and_cut_inputs',seed['inputs']['original_outer_inputs']['sha256']==ids['original_outer_inputs']['sha256'])
    b=low.Bootstrap(outer,defer_products=True)
    b.windows=seed['windows'];b.window_of={m:w for w,(lo,hi) in enumerate(b.windows) for m in range(lo,hi+1,2)}
    b.v=[[low.ex(z) for z in row] for row in seed['window_caps']]
    b.r=list(map(low.ex,seed['finite_caps']));b.h=list(map(low.ex,seed['high_caps']))
    b.parent94=list(map(low.ex,seed['retained_parent94_mass_caps']))
    u=[[low.ex(z) for z in row] for row in seed['low_caps']]
    caps=list(map(low.ex,seed['all46_finite_centre_caps']))
    truecaps=[low.ex(z['same_CL_new_tau_pair_cap']) for z in centre['rows']]
    gate('same_all46_finite_centre_spectrum', [z['mode'] for z in centre['rows']]==low.MODES
         and all(0<c<=p for c,p in zip(truecaps,caps)))
    caps=[min(x,y) for x,y in zip(caps,truecaps)]
    # R116: ||B(X,Y)/c_bg|| <= (23/18)||X||||Y||. Two signs
    # and two in DQ=2B give the coefficient23/18 below for pair masses.
    weighted={m:low.up(c*b.exp(-m*low.TAU)) for m,c in zip(low.MODES,caps)}
    source_rows=[];matrix_hash=hashlib.sha256();counts={'low':0,'middle':0};oldcut=seed['final_cut']
    newC=[Q(0)]*46;newCV=[Q(0)]*46
    for j,block in enumerate(b.blocks):
        ef={}
        def coefficient(m,n):
            d=m-n
            if d not in ef:ef[d]=b.exp(d*(block['smax'] if d>=0 else block['smin']))
            return low.up(Q(23,18)*ef[d]*sum((weighted[k] for k in [abs(d),m+n] if k in weighted),Q(0)))
        cl=[];cv=[];changed_low=changed_middle=0
        for mi,m in enumerate(low.MODES):
            lc=Q(0)
            for ni,n in enumerate(low.MODES):
                original=block['C_times_u'][mi][ni];fresh=min(original,coefficient(m,n))
                if fresh<original:changed_low+=1
                matrix_hash.update(f'L:{j}:{m}:{n}:{fresh.p}/{fresh.q}\n'.encode())
                lc+=fresh*u[j][ni]
            co={}
            for ni,n in enumerate(block['middle_inputs']):
                k=n-m
                if not 2<=k<=92:continue
                original=block['C_times_middle'][mi][ni];fresh=min(original,coefficient(m,n))
                if fresh<original:changed_middle+=1
                matrix_hash.update(f'V:{j}:{m}:{n}:{fresh.p}/{fresh.q}\n'.encode())
                c=fresh+block['u_times_middle'][mi][ni]*u[j][k//2-1]
                w=b.window_of[n];co[w]=max(co.get(w,Q(0)),c)
            cl.append(low.up(lc));cv.append(b.block_support(j,list(co.items())))
        g=b.cut_kernels[j][0]
        for mi in range(46):newC[mi]+=g[mi]*cl[mi];newCV[mi]+=g[mi]*cv[mi]
        counts['low']+=changed_low;counts['middle']+=changed_middle
        gate('whole_source_block_'+str(j),all(z>=0 for z in cl+cv))
        source_rows.append(dict(source_block=j,source_identity=b.read_records[j],
            new_CL_times_low_caps=list(map(low.pack,cl)),new_low_times_middle_caps=list(map(low.pack,cv)),
            improved_C_low_coefficients=changed_low,improved_C_middle_coefficients=changed_middle))
    components={k:list(map(low.ex,v)) for k,v in oldcut['component_mode_caps'].items()}
    components['C_low']=[min(old,low.up(new)) for old,new in zip(components['C_low'],newC)]
    components['low_middle']=[min(old,low.up(new)) for old,new in zip(components['low_middle'],newCV)]
    modes=[min(low.ex(oldcut['mode_caps'][i]),low.up(sum((v[i] for v in components.values()),Q(0)))) for i in range(46)]
    shared=low.ex(oldcut['complete_T_shared'])
    T=min(low.ex(oldcut['T_l1']),low.up(sum((sum(v[6:],Q(0)) for k,v in components.items() if k!='complete_T'),Q(0))+shared))
    S=min(low.ex(oldcut['S_max']),max(modes[:6]))
    gate('same_cut_components_only_tightened',all(0<=z<=low.ex(p) for k,v in components.items() for z,p in zip(v,oldcut['component_mode_caps'][k])))
    projected=read('R153')
    gate('same_complete_projected_map',projected['all_gates'] and all(projected['gates'].values())
         and old['inputs']['R153_projected']['sha256']==ids['R153']['sha256'])
    astar=[]
    for i,row in enumerate(projected['rows']):
        v=min(low.ex(seed['same_a_star_bounds']['rows'][i]['same_original_full_fixed_point_coordinate_bound']),
              low.up(low.ex(row['new_projected_map_bound'])+modes[i]))
        astar.append(dict(mode=row['mode'],same_original_full_fixed_point_coordinate_bound=low.pack(v),
                          projected_bound=row['new_projected_map_bound'],complete_nonlow_correction=low.pack(modes[i])))
    z=projected['same_original_T_shared_projected_map_bound']['upper']
    base=Q(int(z['mantissa']))*Q(2)**int(z['binary_exponent'])
    fullT=min(low.ex(seed['same_a_star_bounds']['complete_shared_T_upper']),low.up(base+T))
    result=dict(schema='same-CL-finite-frequency-cut-posterior-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',
        all_gates=all(gates.values()),gates=gates,inputs=ids,input_manifest_sha256=low.sha(a.inputs),source_sha256=low.sha(__file__),
        same_existing_real_R143_fixed_point=True,same_CL_not_redefined=True,finite_C_spectrum_only=True,
        original_full_T_mean_inverse_and_positive_infinite_remainders_retained=True,
        parameter_domain=seed['same_parameter_domain'],new_C_coefficients=counts,new_C_matrix_exact_payload_sha256=matrix_hash.hexdigest(),
        source_rows=source_rows,all46_finite_C_caps=list(map(low.pack,caps)),
        final_cut=dict(mode_caps=list(map(low.pack,modes)),S_max=low.pack(S),T_l1=low.pack(T),
            complete_T_shared=oldcut['complete_T_shared'],component_mode_caps={k:list(map(low.pack,v)) for k,v in components.items()}),
        same_a_star_bounds=dict(rows=astar,complete_shared_T_upper=low.pack(fullT)),
        no_new_ODE_or_source_integral=True,closed_surface_claimed=False,elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    rec=low.save(a.out,result)
    print(json.dumps(dict(primary=rec,all_gates=result['all_gates'],improved=counts,
        mode92=float(low.ex(astar[-1]['same_original_full_fixed_point_coordinate_bound'])),
        low_middle92=float(components['low_middle'][-1]),C_low92=float(components['C_low'][-1]),
        elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
