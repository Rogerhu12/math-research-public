#!/usr/bin/env python3
"""Rebootstrap the existing R127 full field with a genuinely sharper head.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
All head-plus-centre constants are rebuilt by positive addition. The original
complete nonlinear source,25 blocks,185 windows and infinite high remain.
Only finitely many bounds on the already existing fixed point are claimed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import fmpq as Q, ctx
import root_refined_window_cut_support as low
from nonlow_interface import NonlowInterface


def fq(x):
    return F(int(x.p),int(x.q)) if isinstance(x,Q) else x


def qf(x):
    return Q(x.numerator,x.denominator) if isinstance(x,F) else low.ex(x)


def exf(x):return fq(low.ex(x))


class Windows:
    def __init__(self,b,primary,records,head,head_windows,window_masses,singletons,frequency):
        self.b=b;self.head=head;self.frequency=frequency;self.rows=[]
        original={tuple(w['window']):w for w in primary['windows']}
        rawrows=[]
        for rec in records:
            if low.sha(rec['path'])!=rec['sha256']:raise ArithmeticError('Changed original actual window kernel')
            with gzip.open(rec['path'],'rt') as f:rawrows.extend(json.loads(line) for line in f)
        rawrows.sort(key=lambda r:r['window'])
        if [r['window'] for r in rawrows]!=b.windows:raise ArithmeticError('All185 original windows required')
        self.original_windows=[r['window'] for r in rawrows]
        def head_mass(window,band):
            if band==2:return head[2]
            total=sum((v for w,v in zip(head_windows,window_masses) if w[0]<=window[1] and window[0]<=w[1]),Q(0))
            if total<=0:raise ArithmeticError('Missing actual inner window head')
            return min(head[band],total)
        def make(row,prior):
            window=tuple(row['window']);band=row['head_band']
            if not(row['common_strip_already_paid'] and band==prior['head_band'] and len(row['rows'])==25):raise ArithmeticError('Original common strip/target shape')
            gains=[];materials=[];fixed=[]
            for i,(target,old) in enumerate(zip(row['rows'],prior['rows'])):
                if target['target_block']!=i or old['target_block']!=i:raise ArithmeticError('Target order changed')
                g,one,zero=[[low.ex(v) for v in target['three_materials'][str(p)]] for p in (2,1,0)]
                if not all(len(v)==i+1 for v in (g,one,zero)):raise ArithmeticError('Missing original causal material')
                cross=[];square=[]
                for j in range(i+1):
                    if j==5:cross.append(b.B*one[j]);square.append(b.B*b.B*zero[j])
                    elif j==21:cross.append(min(b.S*g[j],b.R*one[j]));square.append(min(b.S*b.S*g[j],b.S*b.R*one[j],b.R*b.R*zero[j]))
                    else:cross.append(g[j]);square.append(g[j])
                gains.append(low.ex(target['head_gain']));materials.append((g,cross,square));fixed.append(low.ex(old['complete_fixed_centre_upper']))
            pairs=[(ki,ni,Q(5*k*n+1,4*(1+k)*(1+n))) for ki,k in enumerate(low.MODES) for ni,n in enumerate(low.MODES) if window[0]<=k+n<=window[1]] if window[0]<=184 else []
            return dict(window=window,band=band,gains=gains,materials=materials,fixed=fixed,pairs=pairs,head_mass=head_mass(window,band))
        self.parent=make(rawrows[0],original[(94,96)])
        for row in singletons['rows']:self.rows.append(make(row,original[(94,96)]))
        for row in rawrows[1:]:self.rows.append(make(row,original[tuple(row['window'])]))
        self.partition=[list(r['window']) for r in self.rows]
        if self.partition!=frequency['windows'] or len(self.partition)!=186:raise ArithmeticError('Complete actual refinement identity')
        self.centre=[[low.up(c*b.exp(-m*(low.TAU-a['smax']))) for m,c in zip(low.MODES,b.caps)] for a in b.blocks]
        self.thin=[]
        for j,block in enumerate(frequency['rows']):
            if block['source_block']!=j or block['source_pin']['sha256']!=b.read_records[j]['sha256']:raise ArithmeticError('Source block index')
            if block['sigma_min']!=b.blocks[j]['sigma_min'] or block['sigma_max']!=b.blocks[j]['sigma_max']:raise ArithmeticError('Same real source strip required')
            rows=[]
            for r in block['rows']:
                rows.append(dict(mode=r['mode'],terms=[(x['input_window'],x['low_mode']//2-1,low.ex(x['C_coefficient']),low.ex(x['u_coefficient'])) for x in r['C_and_u_times_middle']],edges=[(x['left_window'],x['right_window'],low.ex(x['coefficient'])) for x in r['middle_difference_edges']],vv=low.ex(r['middle_squared_common_coefficient']),vh=low.ex(r['middle_high_coefficient']),hh=low.ex(r['high_squared_coefficient']),tail=r['middle_high_possible_windows']))
            if [r['mode'] for r in rows]!=[94,96]:raise ArithmeticError('Both actual source outputs required')
            self.thin.append(rows)

    def images(self,u,r,h):
        b=self.b;U=[sum(row,Q(0)) for row in u];KT=270*low.RSTAR;K=Q(23,9)+KT
        lowT=[low.up(KT*(10*v+v*v/2)) for v in U]
        thin=[]
        for j,rows in enumerate(self.thin):
            out=[]
            for row in rows:
                coeff={}
                for w,k,c,a in row['terms']:coeff[w]=max(coeff.get(w,Q(0)),c+a*u[j][k])
                cv=b.block_support(j,list(coeff.items()));by_left={}
                for w,z,a in row['edges']:by_left.setdefault(w,[]).append((z,a))
                vv=b.block_support(j,[(w,b.block_support(j,edges)) for w,edges in by_left.items()]);vv=min(vv,row['vv']*r[j]*r[j])
                tail=min(r[j],sum((b.v[j][w] for w in row['tail']),Q(0)))
                out.append((cv+vv+KT*(10*(U[j]+r[j])+(U[j]+r[j])**2/2),row['vh']*tail*h[j]+KT*(10+U[j]+r[j])*h[j],row['hh']*h[j]*h[j]+KT*h[j]*h[j]/2))
            thin.append(out)
        def one(row,singleton=None):
            pure=[]
            for j in range(25):pure.append(low.up(sum((a*(self.centre[j][k]*u[j][n]+u[j][k]*u[j][n]/2) for k,n,a in row['pairs']),Q(0))))
            out=[]
            for i,(g,c,s) in enumerate(row['materials']):
                base=row['gains'][i]*row['head_mass']+row['fixed'][i];coarse=base;fine=base
                for j in range(i+1):
                    C=10+U[j]
                    coarse+=g[j]*(pure[j]+lowT[j])+K*(g[j]*(C*r[j]+r[j]*r[j]/2)+c[j]*(C+r[j])*h[j]+s[j]*h[j]*h[j]/2)
                    if singleton is not None:
                        a,d,e=thin[j][singleton];fine+=g[j]*(pure[j]+a)+c[j]*d+s[j]*e
                out.append(low.up(coarse if singleton is None else min(coarse,fine)))
            return out
        answer=[[Q(0)]*186 for _ in range(25)]
        for w,row in enumerate(self.rows):
            vals=one(row,w if w<2 else None)
            for i,val in enumerate(vals):answer[i][w]=val
        self.parent_images=one(self.parent)
        return answer


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--cycles',type=int,default=8)
    a=ap.parse_args();ctx.prec=256;started=time.monotonic();gates={};ids=low.read(a.inputs)
    if not 1<=a.cycles<=64:raise ValueError('A stated finite number of cycles is required')
    if list(a.out_prefix.parent.glob(a.out_prefix.name+'-*')):raise FileExistsError('Fresh finite-bootstrap outputs required')
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    def gate(name,value):
        if not value:raise ArithmeticError(name)
        gates[name]=True
    def checked(name):
        r=ids[name];gate('identity_'+name,low.sha(r['path'])==r['sha256']);return low.read(r['path'])
    outer_inputs=checked('original_outer_inputs')
    b=low.Bootstrap(outer_inputs,defer_products=True)
    original=low.checked(outer_inputs['nonlow'])
    primary=low.checked(outer_inputs['window_caps'])
    initial_low=checked('R128_bootstrap')
    gate('same_actual_R128_existing_field',initial_low['same_existing_R127_field']
         and initial_low['all_input_identity_and_domain_gates']
         and initial_low['inputs']['joint1200']['sha256']==outer_inputs['joint1200']['sha256'])
    u=[[low.ex(x) for x in row] for row in initial_low['final_low_caps']]
    gate('R128_low_caps_inside_R127',len(u)==25 and all(len(row)==46 for row in u)
         and all(0<x<=old for row,prior in zip(u,b.u) for x,old in zip(row,prior)))
    head=checked('new_head_export')
    # This normalized export is a separately proved true head, not a low
    # reference source. Preserve its explicit parameter scope and physical
    # head units when changing from a whole-cell to an endpoint readout.
    gate('complete_true_head_export',head['all_gates'] and head['complete_mean_inverse_far']
         and low.ex(head['domain']['S_product_radius'])==Q(3,4)
         and low.ex(head['domain']['T_l1_radius'])==Q(1,32)
         and head['same_original617_units']['sha256']=='617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9'
         and head['same_original617_units']['sha256'] in original['input_hashes'].values()
         and head['head_bands']==[[94,184],[186,8190],[8192,None]])
    head_primary=checked('new_head_primary');head_resource=checked('new_head_resource')
    primary_masses=(head_primary['actual_R100_head_band_masses']
                    if 'actual_R100_head_band_masses' in head_primary else
                    head_primary['checkpoints'][-1]['head_complete_balanced_P_K_by_band'])
    gate('actual_complete_head_primary_and_exit',head_primary['all_gates']
         and all(head_primary['gates'].values()) and head_resource['exitcode']==0
         and head_resource['termination_signal'] is None
         and head['primary']['sha256']==ids['new_head_primary']['sha256']
         and head['resource']['sha256']==ids['new_head_resource']['sha256']
         and head['actual_R100_head_band_masses']==primary_masses
         and head['head_strip']==head_primary['head_strip'])
    profile=checked('restricted_profile_lift');expanded=next(r for r in profile['domains'] if r['name']=='expanded_profile')
    gate('exact_restricted_profile_and_containment',profile['all_gates'] and head['domain']==head_primary['domain'] and 0<low.ex(head['domain']['S_product_radius'])==low.ex(expanded['S_linf_radius'])<=1 and low.ex(head['domain']['T_l1_radius'])==low.ex(expanded['T_l1_radius'])==Q(1,32) and list(map(low.ex,head['domain']['T_coordinate_caps_by_mode']))==list(map(low.ex,expanded['original_normalized_T_coordinate_caps'])))
    gate('complete_actual13_window_head',head['head_windows']==head_primary['windows'] and head['actual_R100_head_window_masses']==head_primary['actual_R100_head_window_masses'] and len(head['head_windows'])==13 and [m for lo,hi in head['head_windows'] for m in range(lo,hi+1,2)]==list(range(94,8191,2)) and head['complete_infinite_repaid'])
    projected=checked('projected_profile');working=next(r for r in profile['domains'] if r['name']=='R133_working')
    def profile_exact(x):
        z=x['upper'];return Q(int(z['mantissa']))*Q(2)**int(z['binary_exponent'])
    gate('same_complete_projected_map_and_exact_working_domain',projected['all_gates'] and projected['same_existing_R124_projected_low_solution'] and projected['same_original_axes_and_parameters'] and projected['complete_mean_inverse_and_true_far_retained'] and profile['inputs']['projected_profile']['sha256']==ids['projected_profile']['sha256'] and low.ex(working['S_linf_radius'])==Q(1,2) and low.ex(working['T_l1_radius'])==Q(1,36) and [r['mode'] for r in projected['rows']]==low.MODES)
    wr=list(map(low.ex,working['original_normalized_T_coordinate_caps']))
    gate('all_original_working_axes_and_expanded_margins',len(wr)==46 and all(wr[i]==2*profile_exact(projected['rows'][i]['projected_map_value'])==profile_exact(projected['rows'][i]['proposed_T_coordinate_radius']) for i in range(6,46)) and all(2*x==low.ex(y) for x,y in zip(wr,expanded['original_normalized_T_coordinate_caps'])))
    def selfmap(cut):
        vals=[];checks={};ratios=[]
        for i,row in enumerate(projected['rows']):
            bound=low.up(profile_exact(row['projected_map_value'])+low.ex(cut['mode_caps'][i]));radius=Q(1,2) if i<6 else wr[i]
            checks['strict_mode_'+str(row['mode'])]=bound<radius;ratios.append(bound/radius)
            vals.append(dict(mode=row['mode'],original_axis_complete_map_upper=low.pack(bound),working_coordinate_radius=low.pack(radius),map_over_radius=low.pack(bound/radius),nonlow_cut_correction=cut['mode_caps'][i]))
        tsum=low.up(profile_exact(projected['T_projected_map'])+low.ex(cut['T_l1']));checks['strict_shared_T']=tsum<Q(1,36)
        return dict(all_strict_selfmap_gates=all(checks.values()),gates=checks,rows=vals,T_complete_shared_map_upper=low.pack(tsum),T_working_exact_radius={'numerator':'1','denominator':'36'},maximum_coordinate_ratio=low.pack(max(ratios)),worst_mode=low.MODES[ratios.index(max(ratios))],finite_dimensional_Brouwer_applicable_if_all_gates=True,uniqueness_or_closed_surface_claimed=False)
    singleton=checked('singleton_kernels');singleton_resource=checked('singleton_resource');frequency=checked('frequency_operators');frequency_resource=checked('frequency_resource')
    gate('actual_complete_new_singletons_and_frequency',singleton['all_gates'] and frequency['all_gates'] and singleton_resource['exitcode']==frequency_resource['exitcode']==0 and singleton_resource['termination_signal'] is None and frequency_resource['termination_signal'] is None and frequency['inputs']['singletons']['sha256']==ids['singleton_kernels']['sha256'] and frequency['inputs']['low_sources']['sha256']==outer_inputs['low_sources']['sha256'] and frequency['inputs']['old_windows']['sha256']==outer_inputs['window_caps']['sha256'] and frequency['inputs']['low_spectrum']['sha256']==outer_inputs['low_spectrum']['sha256'] and frequency['inputs']['nonlow']['sha256']==outer_inputs['nonlow']['sha256'])
    hm=[low.ex(v) for v in head['actual_R100_head_band_masses']]
    oldhm=[low.ex(v) for v in original['actual_R100_head_band_masses']]
    gate('all_three_positive_head_bands_improve',len(hm)==3 and all(0<x<=y for x,y in zip(hm,oldhm)))
    near=checked('near_interface')
    ni=NonlowInterface(original,near)
    finite=checked('original_finite')
    high=checked('original_high')
    balanced=checked('original_balanced')
    gate('same_original_finite_and_high_kernels',finite['all_gates'] and high['all_gates']
         and finite['comparison_partition']==high['comparison_partition']==original['comparison_partition'])
    # Check direct input identities against R126, not just their dimensions.
    for key in ['original_finite','original_high','original_balanced']:
        rec=ids[key]
        gate('R126_identity_'+key,any(v==rec['sha256'] and Path(k).name==Path(rec['path']).name for k,v in original['input_hashes'].items()))
    Bcut=low.ex(balanced['balanced_B_lower'])
    high_source=low.ex(original['complete_high_centre_shared_source'])
    headrows=[]
    for i,(fr,hr,old) in enumerate(zip(finite['rows'],high['rows'],original['rows'])):
        gains=[low.ex(fr['given_band_gains'][band]['gain']) for band in ['near','rest','infinite']]
        centre=low.ex(fr['complete_shared_centre_source'])
        if i==21:
            c=hr['initial_profile_balanced_column_sups'];hg=max(low.ex(c[0])/Bcut,low.ex(c[1]))
        elif i==5:
            c=hr['initial_balanced_column_sups'];hg=max(low.ex(c[0])/Bcut,low.ex(c[1]))
        else:
            c=hr['initial_localV_separate_component_sups']
            hg=max(sum(map(low.ex,c[0]),Q(0))/Bcut,sum(map(low.ex,c[1]),Q(0)))
        hc=high_source*sum((qf(x) for x in ni.A[2][i]),Q(0))
        gate('direct_original_head_plus_centre_identity_'+str(i),
             sum((x*y for x,y in zip(oldhm,gains)),Q(0))+centre==low.ex(old['true_finite_head_and_centre'])
             and oldhm[2]*hg==low.ex(original['high_head_lift_rows'][i])
             and oldhm[2]*hg+hc==low.ex(old['true_high_head_and_complete_centre']))
        finite_exact=sum((x*y for x,y in zip(hm,gains)),Q(0))+centre
        high_exact=hm[2]*hg+hc
        old_finite=low.ex(old['true_finite_head_and_centre'])
        old_high=low.ex(old['true_high_head_and_complete_centre'])
        gate('positive_head_replacement_'+str(i),finite_exact<=old_finite and high_exact<=old_high)
        # A much smaller head may be below the rounding scale of the unchanged
        # fixed-centre term. Both the old exact bound and the new upward-rounded
        # sum remain independently valid, so retain their minimum.
        finite_new=min(old_finite,low.up(finite_exact))
        high_new=min(old_high,low.up(high_exact))
        ni.headf[i]=fq(finite_new);ni.headh[i]=fq(high_new)
        headrows.append(dict(block=i,new_finite_head_plus_centre=low.pack(finite_new),
                             new_high_head_plus_centre=low.pack(high_new),
                             uses_minimum_of_two_independently_valid_upper_bounds=True))
    windows=Windows(b,primary,ids['window_kernel_records'],hm,head['head_windows'],list(map(low.ex,head['actual_R100_head_window_masses'])),singleton,frequency)
    r=b.r[:];h=b.h[:];parent94=[row[0] for row in b.v];v=[[row[0],row[0]]+row[1:] for row in b.v]
    b.windows=windows.partition;b.window_of={m:w for w,(lo,hi) in enumerate(b.windows) for m in range(lo,hi+1,2)}
    if 'previous_full_bootstrap' in ids:
        seed=checked('previous_full_bootstrap')
        seed_resource=checked('previous_full_resource')
        gate('same_existing_field_seed',seed['all_gates'] and all(seed['gates'].values())
             and seed_resource['exitcode']==0 and seed_resource['termination_signal'] is None
             and seed['same_existing_R127_field']
             and seed['same_parameter_domain'] in (b.joint['same_R100_parameter_domain'],head['domain'])
             and seed['complete_mean_inverse_and_infinite_high_retained']
             and seed['all185_windows_and_original_source_materials_retained']
             and seed['inputs']['original_outer_inputs']['sha256']==ids['original_outer_inputs']['sha256'])
        su=[[low.ex(x) for x in row] for row in seed['low_caps']]
        sr=list(map(low.ex,seed['finite_caps']));sh=list(map(low.ex,seed['high_caps']))
        sv=[[low.ex(x) for x in row] for row in seed['window_caps']]
        if all(len(row)==185 for row in sv):
            sp=[row[0] for row in sv];sv=[[row[0],row[0]]+row[1:] for row in sv]
        else:
            gate('same186_seed_partition',seed['windows']==b.windows and seed['all186_refinement_and_parent94_constraint_retained'])
            sp=list(map(low.ex,seed['retained_parent94_mass_caps']))
        parent94=[min(x,y) for x,y in zip(parent94,sp)]
        gate('complete_positive_seed_shape',len(su)==len(sr)==len(sh)==len(sv)==25
             and all(len(row)==46 for row in su) and all(len(row)==186 for row in sv)
             and all(x>0 for row in su+sv for x in row) and min(sr+sh)>0)
        # Both earlier certificates bound this same existing field. Public
        # upward-rounded caps may have different precision; their intersection
        # remains valid without treating that rounding difference as failure.
        u=[[min(x,y) for x,y in zip(row,other)] for row,other in zip(u,su)]
        r=[min(x,y) for x,y in zip(r,sr)];h=[min(x,y) for x,y in zip(h,sh)]
        v=[[min(x,y) for x,y in zip(row,other)] for row,other in zip(v,sv)]
    b.parent94=parent94;b.r,b.h,b.v=r,h,v
    state_records=[];history=[]
    for cycle in range(a.cycles):
        previous=[row[:] for row in u];oldr=r[:];oldh=h[:];oldv=[row[:] for row in v];oldp=parent94[:]
        prepared=ni.prepare([[fq(x) for x in row] for row in u])
        im=ni.images(prepared,list(map(fq,r)),list(map(fq,h)))
        gate('complete_original_physical_domain_'+str(cycle),all(x<F(1,2**34) for x in im['domain']))
        r=[min(x,low.up(qf(y))) for x,y in zip(r,im['finite'])]
        h=[min(x,low.up(qf(y))) for x,y in zip(h,im['high'])]
        b.r,b.h,b.v=r,h,v;b.parent94=parent94
        wi=windows.images(u,r,h)
        v=[[min(old,r[j],new) for old,new in zip(v[j],wi[j])] for j in range(25)]
        parent94=[min(oldp[j],r[j],v[j][0]+v[j][1],windows.parent_images[j]) for j in range(25)]
        b.r,b.h,b.v=r,h,v;b.parent94=parent94
        b.qvv=b.build_vv()
        sources=b.sources(u);ui=b.images(sources)
        u=[[min(x,y) for x,y in zip(row,new)] for row,new in zip(u,ui)]
        gate('finite_monotone_full_bound_'+str(cycle),
             all(0<x<=y for row,prior in zip(u,previous) for x,y in zip(row,prior))
             and all(0<x<=y for x,y in zip(r,oldr)) and all(0<x<=y for x,y in zip(h,oldh))
             and all(0<x<=y for row,prior in zip(v,oldv) for x,y in zip(row,prior)) and all(0<x<=y for x,y in zip(parent94,oldp)))
        cycle_cut=b.cut(b.sources(u));cycle_selfmap=selfmap(cycle_cut)
        body=dict(cycle=cycle,low_caps=[[low.pack(x) for x in row] for row in u],
            finite_caps=list(map(low.pack,r)),high_caps=list(map(low.pack,h)),
            window_caps=[[low.pack(x) for x in row] for row in v],retained_parent94_mass_caps=list(map(low.pack,parent94)),
            complete_nonlow_images=dict(finite=[low.pack(qf(x)) for x in im['finite']],high=[low.pack(qf(x)) for x in im['high']]),
            complete_low_images=[[low.pack(x) for x in row] for row in ui],
            same_existing_R127_field=True,finite_substitution_only=True,complete_cut=cycle_cut,projected_plus_nonlow_selfmap=cycle_selfmap)
        state_records.append(low.save(str(a.out_prefix)+f'-cycle{cycle:02d}.json.gz',body))
        report=dict(cycle=cycle,low23=float(sum(u[23],Q(0))),middle23=float(r[23]),high23=float(h[23]),
            near94_block23=float(v[23][0]),near96_block23=float(v[23][1]),retained_parent94_block23=float(parent94[23]),max_physical_domain=float(max(im['domain'])),strict_selfmap=cycle_selfmap['all_strict_selfmap_gates'],max_axis_ratio=float(low.ex(cycle_selfmap['maximum_coordinate_ratio'])),worst_axis=cycle_selfmap['worst_mode'],correction92=float(low.ex(cycle_cut['mode_caps'][-1])),
            elapsed_seconds=time.monotonic()-started)
        history.append(report);print(json.dumps(report,separators=(',',':')),flush=True)
        if cycle_selfmap['all_strict_selfmap_gates']:break
    b.r,b.h,b.v=r,h,v;b.qvv=b.build_vv()
    final_cut=b.cut(b.sources(u))
    answer=dict(schema='restricted-R127-full-field-186-window-finite-rebootstrap-v1',author='/root (GPT-6 Astra Pro, AI-assisted)',
        source_sha256=low.sha(__file__),low_helper_sha256=low.sha(low.__file__),
        input_manifest_sha256=low.sha(a.inputs),inputs=ids,all_gates=all(gates.values()),gates=gates,
        same_existing_R127_field=True,same_parameter_domain=head['domain'],original_parent_parameter_domain=b.joint['same_R100_parameter_domain'],bounds_apply_only_to_restricted_parameter_domain=True,
        complete_mean_inverse_and_infinite_high_retained=True,all185_windows_and_original_source_materials_retained=True,all186_refinement_and_parent94_constraint_retained=True,retained_parent94_mass_caps=list(map(low.pack,parent94)),
        positive_new_head_and_original_centre=headrows,actual_finite_cycles=len(history),requested_maximum_cycles=a.cycles,state_records=state_records,
        low_caps=[[low.pack(x) for x in row] for row in u],finite_caps=list(map(low.pack,r)),high_caps=list(map(low.pack,h)),
        window_caps=[[low.pack(x) for x in row] for row in v],windows=b.windows,final_cut=final_cut,history=history,
        projected_plus_nonlow_selfmap=selfmap(final_cut),original_two_cell_low46_parameter_selfmap_certified=selfmap(final_cut)['all_strict_selfmap_gates'],full_closed_surface_or_all_outer_cells_claimed=False,full_cut_closed=False,closed_surface_claimed=False,no_new_ODE_or_source_integral=True,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    rec=low.save(str(a.out_prefix)+'-certificate.json.gz',answer)
    summary=dict(certificate=rec,all_gates=True,cycles=len(history),original_two_cell_low46_strict_selfmap=selfmap(final_cut)['all_strict_selfmap_gates'],
        cut_S=float(low.ex(final_cut['S_max'])),cut_T=float(low.ex(final_cut['T_l1'])),
        cut_below_one_over1000=final_cut['norm_below_one_over1000'],
        elapsed_seconds=answer['elapsed_seconds'],peak_rss_kib=answer['peak_rss_kib'])
    low.save(str(a.out_prefix)+'-summary.json',summary);print(json.dumps(summary,separators=(',',':')),flush=True)


if __name__=='__main__':main()
