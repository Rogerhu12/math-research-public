#!/usr/bin/env python3
"""Finite low/cut feedback using the same actual field's proved wider nonlow caps.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Every bound concerns the already existing real R143 fixed point. Only the
newly proved wide field is lowered; no old infinite tail is widened. All old
complete low sources, means, inverse remainders and shared T terms remain.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
from flint import ctx, fmpq as Q


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--cycles',type=int,default=4)
    a=ap.parse_args()
    if not 1<=a.cycles<=16:raise ValueError('Declare a finite substitution count')
    if list(a.out_prefix.parent.glob(a.out_prefix.name+'-*')):
        raise FileExistsError('Never overwrite an actual calculation')
    ctx.prec,ctx.threads=256,1;started=time.monotonic()
    ids=json.loads(a.inputs.read_text())
    spec=importlib.util.spec_from_file_location('actual_low_support',ids['low_helper']['path'])
    low=importlib.util.module_from_spec(spec);spec.loader.exec_module(low)
    gates={}
    def gate(name,ok):
        gates[name]=bool(ok)
        if not ok:raise ArithmeticError(name)
    for name,r in ids.items():gate('identity_'+name,low.sha(r['path'])==r['sha256'])
    read=lambda name:low.read(ids[name]['path'])
    done=lambda r:r['exitcode']==0 and r['termination_signal'] is None
    old,wide=read('R156'),read('R163')
    gate('same_existing_R156_full_field',old['all_gates'] and all(old['gates'].values())
         and done(read('R156_resource')) and old['same_existing_R127_field']
         and old['complete_mean_inverse_and_infinite_high_retained']
         and old['all186_refinement_and_parent94_constraint_retained'])
    gate('actual_new_width_field_identified',wide['all_gates'] and all(wide['gates'].values())
         and done(read('R163_resource')) and wide['actual_complete_new_width_nonlow_field']
         and wide['same_original_actual_full_field_identified']
         and wide['complete_mean_inverse_far_and_shared_T_retained']
         and not wide['old_unknown_infinite_caps_reweighted'])
    outer=read('original_outer_inputs')
    gate('unchanged_original_operators',old['inputs']['original_outer_inputs']['sha256']==ids['original_outer_inputs']['sha256'])
    original_wide_inputs=low.read(wide['inputs']['R160_inputs']['path'])
    gate('same_actual_R156_seed_in_new_width_proof',
         low.sha(wide['inputs']['R160_inputs']['path'])==wide['inputs']['R160_inputs']['sha256']
         and original_wide_inputs['R156']['sha256']==ids['R156']['sha256'])
    b=low.Bootstrap(outer,defer_products=True)
    gate('all25_comparison_blocks_identical',wide['comparison_partition']==low.checked(outer['nonlow'])['comparison_partition'])
    b.caps=list(map(low.ex,old['all46_finite_centre_caps']))
    u=[[low.ex(z) for z in row] for row in old['low_caps']]
    oldr=list(map(low.ex,old['finite_caps']));oldh=list(map(low.ex,old['high_caps']))
    oldv=[[low.ex(z) for z in row] for row in old['window_caps']]
    oldp=list(map(low.ex,old['retained_parent94_mass_caps']))
    b.windows=old['windows']
    gate('complete_actual186_partition',len(b.windows)==186
         and [m for lo,hi in b.windows for m in range(lo,hi+1,2)]==list(range(94,low.M,2))
         and b.windows[:2]==[[94,94],[96,96]])
    b.window_of={m:w for w,(lo,hi) in enumerate(b.windows) for m in range(lo,hi+1,2)}
    nr=list(map(low.ex,wide['finite_caps']));nh=list(map(low.ex,wide['high_caps']))
    delta=Q(wide['angular_shift'])
    gate('positive_new_full_nonlow_shape',delta==Q(2,5) and len(nr)==len(nh)==25
         and all(z>0 for z in nr+nh) and len(u)==len(oldv)==25
         and all(len(row)==46 for row in u) and all(len(row)==186 for row in oldv))
    downr=[low.up(z*b.exp(-94*delta)) for z in nr]
    downh=[low.up(z*b.exp(-low.M*delta)) for z in nh]
    r=[min(x,y) for x,y in zip(oldr,downr)]
    h=[min(x,y) for x,y in zip(oldh,downh)]
    v=[[min(oldv[j][w],r[j],low.up(nr[j]*b.exp(-lo*delta)))
        for w,(lo,hi) in enumerate(b.windows)] for j in range(25)]
    parent=[min(oldp[j],r[j],v[j][0]+v[j][1]) for j in range(25)]
    gate('only_lower_proved_wide_field_and_intersect',
         all(0<z<=p for z,p in zip(r,oldr)) and all(0<z<=p for z,p in zip(h,oldh))
         and all(0<z<=p for row,prior in zip(v,oldv) for z,p in zip(row,prior)))
    b.r,b.h,b.v,b.parent94=r,h,v,parent
    b.qvv=b.build_vv()
    sys.path.insert(0,str(Path(ids['nonlow_helper']['path']).parent))
    from nonlow_interface import NonlowInterface
    ni=NonlowInterface(low.checked(outer['nonlow']),read('near_interface'))
    def fq(z):return F(int(z.p),int(z.q))
    def physical():return ni.domain(dict(U=[sum(map(fq,row),F(0)) for row in u]),list(map(fq,r)),list(map(fq,h)))
    gate('original_complete_physical_domain_after_lowering',all(z<F(1,2**34) for z in physical()))
    projected=read('R153')
    gate('same_complete_projected_base',projected['all_gates'] and all(projected['gates'].values())
         and old['inputs']['R153_projected']['sha256']==ids['R153']['sha256'])
    def astar(cut):
        rows=[]
        for i,row in enumerate(projected['rows']):
            bound=low.up(low.ex(row['new_projected_map_bound'])+low.ex(cut['mode_caps'][i]))
            bound=min(bound,low.ex(old['same_a_star_bounds']['rows'][i]['same_original_full_fixed_point_coordinate_bound']))
            rows.append(dict(mode=row['mode'],same_original_full_fixed_point_coordinate_bound=low.pack(bound),
                             projected_bound=row['new_projected_map_bound'],complete_nonlow_correction=cut['mode_caps'][i]))
        z=projected['same_original_T_shared_projected_map_bound']['upper']
        base=Q(int(z['mantissa']))*Q(2)**int(z['binary_exponent'])
        shared=min(low.up(base+low.ex(cut['T_l1'])),low.ex(old['same_a_star_bounds']['complete_shared_T_upper']))
        return dict(rows=rows,complete_shared_T_upper=low.pack(shared),same_unique_R143_fixed_point=True,
                    whole_parameter_box_selfmap_claimed=False)
    state_records=[];history=[]
    for cycle in range(a.cycles):
        prior=[row[:] for row in u]
        sources=b.sources(u);image=b.images(sources)
        u=[[min(x,y) for x,y in zip(row,new)] for row,new in zip(u,image)]
        gate('finite_same_field_low_substitution_'+str(cycle),
             all(0<z<=p for row,oldrow in zip(u,prior) for z,p in zip(row,oldrow)))
        gate('complete_physical_domain_'+str(cycle),all(z<F(1,2**34) for z in physical()))
        cut=b.cut(b.sources(u));post=astar(cut)
        rec=low.save(str(a.out_prefix)+f'-cycle{cycle:02d}.json.gz',dict(cycle=cycle,
            low_caps=[[low.pack(z) for z in row] for row in u],complete_low_images=[[low.pack(z) for z in row] for row in image],
            complete_cut=cut,same_a_star_bounds=post,same_existing_actual_field=True,finite_substitution_only=True))
        state_records.append(rec)
        summary=dict(cycle=cycle,low23=float(sum(u[23],Q(0))),middle23=float(r[23]),high23=float(h[23]),
                     mode92=float(low.ex(post['rows'][-1]['same_original_full_fixed_point_coordinate_bound'])),
                     shared_T=float(low.ex(post['complete_shared_T_upper'])),elapsed_seconds=time.monotonic()-started)
        history.append(summary);print(json.dumps(summary),flush=True)
    result=dict(schema='same-R143-actual-wide-nonlow-low-feedback-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',
        all_gates=all(gates.values()),gates=gates,inputs=ids,input_manifest_sha256=low.sha(a.inputs),source_sha256=low.sha(__file__),
        same_existing_R127_field=True,same_unique_R143_fixed_point=True,same_parameter_domain=wide['parameter_domain'],
        actual_scope='Only the same real a*; no new complex-parameter outer box or parameter selfmap.',
        same_original_CL_retained=True,all46_finite_centre_caps=list(map(low.pack,b.caps)),
        low_caps=[[low.pack(z) for z in row] for row in u],finite_caps=list(map(low.pack,r)),high_caps=list(map(low.pack,h)),
        window_caps=[[low.pack(z) for z in row] for row in v],windows=b.windows,retained_parent94_mass_caps=list(map(low.pack,parent)),
        new_width_derived_finite_caps=list(map(low.pack,downr)),new_width_derived_high_caps=list(map(low.pack,downh)),
        final_cut=cut,same_a_star_bounds=post,state_records=state_records,history=history,actual_finite_cycles=a.cycles,
        complete_mean_inverse_infinite_high_and_shared_T_retained=True,all_source_materials_and_original_axes_retained=True,
        old_unknown_infinite_field_widened=False,no_new_ODE_or_source_integral=True,full_closed_surface_claimed=False,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    rec=low.save(str(a.out_prefix)+'-certificate.json.gz',result)
    print(json.dumps(dict(certificate=rec,all_gates=result['all_gates'],last=history[-1])),flush=True)


if __name__=='__main__':main()
