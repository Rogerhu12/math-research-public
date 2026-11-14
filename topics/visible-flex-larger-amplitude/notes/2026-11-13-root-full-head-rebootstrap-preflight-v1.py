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
import root_window_frequency_cut_bootstrap as low
from nonlow_interface import NonlowInterface


def fq(x):
    return F(int(x.p),int(x.q)) if isinstance(x,Q) else x


def qf(x):
    return Q(x.numerator,x.denominator) if isinstance(x,F) else low.ex(x)


def exf(x):return fq(low.ex(x))


class Windows:
    def __init__(self,b,primary,records,head):
        self.b=b;self.primary=primary;self.head=head
        original={tuple(w['window']):w for w in primary['windows']}
        self.rows=[]
        for rec in records:
            if low.sha(rec['path'])!=rec['sha256']:
                raise ArithmeticError('A complete actual window kernel changed')
            with gzip.open(rec['path'],'rt') as stream:
                for line in stream:
                    row=json.loads(line);window=tuple(row['window']);old=original[window]
                    if not(row['common_strip_already_paid'] and row['head_band']==old['head_band'] and len(row['rows'])==25):
                        raise ArithmeticError('Same common-strip window and all25 targets required')
                    gains=[];materials=[];fixed=[]
                    for i,(target,prior) in enumerate(zip(row['rows'],old['rows'])):
                        if target['target_block']!=i or prior['target_block']!=i:
                            raise ArithmeticError('Original window target order differs')
                        g,one,zero=[[low.ex(v) for v in target['three_materials'][str(p)]] for p in (2,1,0)]
                        if not all(len(v)==i+1 for v in [g,one,zero]):
                            raise ArithmeticError('All original causal source columns required')
                        cross=[];square=[]
                        for j in range(i+1):
                            if j==5:
                                cross.append(b.B*one[j]);square.append(b.B*b.B*zero[j])
                            elif j==21:
                                cross.append(min(b.S*g[j],b.R*one[j]))
                                square.append(min(b.S*b.S*g[j],b.S*b.R*one[j],b.R*b.R*zero[j]))
                            else:cross.append(g[j]);square.append(g[j])
                        materials.append((g,cross,square))
                        gains.append(low.ex(target['head_gain']))
                        fixed.append(low.ex(prior['complete_fixed_centre_upper']))
                    pairs=[]
                    if window[0]<=184:
                        for ki,k in enumerate(low.MODES):
                            for ni,n in enumerate(low.MODES):
                                if window[0]<=k+n<=window[1]:
                                    pairs.append((ki,ni,Q(5*k*n+1,4*(1+k)*(1+n))))
                    self.rows.append(dict(window=window,band=row['head_band'],gains=gains,materials=materials,fixed=fixed,pairs=pairs))
        self.rows.sort(key=lambda r:r['window'])
        if [list(r['window']) for r in self.rows]!=b.windows:
            raise ArithmeticError('All185 actual windows must be retained exactly once')
        self.centre=[[low.up(c*b.exp(-m*(low.TAU-a['smax']))) for m,c in zip(low.MODES,b.caps)] for a in b.blocks]

    def images(self,u,r,h):
        b=self.b;U=[sum(row,Q(0)) for row in u]
        KT=270*low.RSTAR;K=Q(23,9)+KT
        lowT=[low.up(KT*(10*v+v*v/2)) for v in U]
        answer=[[Q(0)]*185 for _ in range(25)]
        for w,row in enumerate(self.rows):
            pureQ=[]
            for j in range(25):
                value=sum((alpha*(self.centre[j][ki]*u[j][ni]+u[j][ki]*u[j][ni]/2)
                           for ki,ni,alpha in row['pairs']),Q(0))
                pureQ.append(low.up(value))
            for i,(g,c,s) in enumerate(row['materials']):
                value=row['gains'][i]*self.head[row['band']]+row['fixed'][i]
                for j in range(i+1):
                    C=10+U[j]
                    value+=g[j]*(pureQ[j]+lowT[j])+K*(g[j]*(C*r[j]+r[j]*r[j]/2)
                            +c[j]*(C+r[j])*h[j]+s[j]*h[j]*h[j]/2)
                answer[i][w]=low.up(value)
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
    b=low.Bootstrap(outer_inputs)
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
         and low.ex(head['domain']['S_product_radius'])==1
         and low.ex(head['domain']['T_l1_radius'])==Q(1,32)
         and head['same_original617_units']=='617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9'
         and head['same_original617_units'] in original['input_hashes'].values()
         and head['head_bands']==[[94,184],[186,8190],[8192,None]])
    head_primary=checked('new_head_primary');head_resource=checked('new_head_resource')
    gate('actual_complete_head_primary_and_exit',head_primary['all_gates']
         and all(head_primary['gates'].values()) and head_resource['exitcode']==0
         and head_resource['termination_signal'] is None
         and head['primary']['sha256']==ids['new_head_primary']['sha256']
         and head['resource']['sha256']==ids['new_head_resource']['sha256']
         and head['actual_R100_head_band_masses']==head_primary['checkpoints'][-1]['head_complete_balanced_P_K_by_band']
         and head['head_strip']==head_primary['head_strip'])
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
        finite_new=low.up(sum((x*y for x,y in zip(hm,gains)),Q(0))+centre)
        high_new=low.up(hm[2]*hg+hc)
        gate('positive_head_replacement_'+str(i),finite_new<=low.ex(old['true_finite_head_and_centre'])
             and high_new<=low.ex(old['true_high_head_and_complete_centre']))
        ni.headf[i]=fq(finite_new);ni.headh[i]=fq(high_new)
        headrows.append(dict(block=i,new_finite_head_plus_centre=low.pack(finite_new),
                             new_high_head_plus_centre=low.pack(high_new)))
    windows=Windows(b,primary,ids['window_kernel_records'],hm)
    r=b.r[:];h=b.h[:];v=[row[:] for row in b.v]
    state_records=[];history=[]
    for cycle in range(a.cycles):
        previous=[row[:] for row in u];oldr=r[:];oldh=h[:];oldv=[row[:] for row in v]
        prepared=ni.prepare([[fq(x) for x in row] for row in u])
        im=ni.images(prepared,list(map(fq,r)),list(map(fq,h)))
        gate('complete_original_physical_domain_'+str(cycle),all(x<F(1,2**34) for x in im['domain']))
        r=[min(x,low.up(qf(y))) for x,y in zip(r,im['finite'])]
        h=[min(x,low.up(qf(y))) for x,y in zip(h,im['high'])]
        wi=windows.images(u,r,h)
        v=[[min(old,r[j],new) for old,new in zip(v[j],wi[j])] for j in range(25)]
        b.r,b.h,b.v=r,h,v
        b.qvv=b.build_vv()
        sources=b.sources(u);ui=b.images(sources)
        u=[[min(x,y) for x,y in zip(row,new)] for row,new in zip(u,ui)]
        gate('finite_monotone_full_bound_'+str(cycle),
             all(0<x<=y for row,prior in zip(u,previous) for x,y in zip(row,prior))
             and all(0<x<=y for x,y in zip(r,oldr)) and all(0<x<=y for x,y in zip(h,oldh))
             and all(0<x<=y for row,prior in zip(v,oldv) for x,y in zip(row,prior)))
        body=dict(cycle=cycle,low_caps=[[low.pack(x) for x in row] for row in u],
            finite_caps=list(map(low.pack,r)),high_caps=list(map(low.pack,h)),
            window_caps=[[low.pack(x) for x in row] for row in v],
            complete_nonlow_images=dict(finite=[low.pack(qf(x)) for x in im['finite']],high=[low.pack(qf(x)) for x in im['high']]),
            complete_low_images=[[low.pack(x) for x in row] for row in ui],
            same_existing_R127_field=True,finite_substitution_only=True)
        state_records.append(low.save(str(a.out_prefix)+f'-cycle{cycle:02d}.json.gz',body))
        report=dict(cycle=cycle,low23=float(sum(u[23],Q(0))),middle23=float(r[23]),high23=float(h[23]),
            near94_block23=float(v[23][0]),max_physical_domain=float(max(im['domain'])),
            elapsed_seconds=time.monotonic()-started)
        history.append(report);print(json.dumps(report,separators=(',',':')),flush=True)
    b.r,b.h,b.v=r,h,v;b.qvv=b.build_vv()
    final_cut=b.cut(b.sources(u))
    answer=dict(schema='existing-R127-full-field-true-head-finite-rebootstrap-v1',author='/root (GPT-6 Astra Pro, AI-assisted)',
        source_sha256=low.sha(__file__),low_helper_sha256=low.sha(low.__file__),
        input_manifest_sha256=low.sha(a.inputs),inputs=ids,all_gates=all(gates.values()),gates=gates,
        same_existing_R127_field=True,same_parameter_domain=b.joint['same_R100_parameter_domain'],
        complete_mean_inverse_and_infinite_high_retained=True,all185_windows_and_original_source_materials_retained=True,
        positive_new_head_and_original_centre=headrows,actual_finite_cycles=a.cycles,state_records=state_records,
        low_caps=[[low.pack(x) for x in row] for row in u],finite_caps=list(map(low.pack,r)),high_caps=list(map(low.pack,h)),
        window_caps=[[low.pack(x) for x in row] for row in v],final_cut=final_cut,history=history,
        full_cut_closed=False,closed_surface_claimed=False,no_new_ODE_or_source_integral=True,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    rec=low.save(str(a.out_prefix)+'-certificate.json.gz',answer)
    summary=dict(certificate=rec,all_gates=True,cycles=a.cycles,
        cut_S=float(low.ex(final_cut['S_max'])),cut_T=float(low.ex(final_cut['T_l1'])),
        cut_below_one_over1000=final_cut['norm_below_one_over1000'],
        elapsed_seconds=answer['elapsed_seconds'],peak_rss_kib=answer['peak_rss_kib'])
    low.save(str(a.out_prefix)+'-summary.json',summary);print(json.dumps(summary,separators=(',',':')),flush=True)


if __name__=='__main__':main()
