#!/usr/bin/env python3
"""Independent Fraction check of the complete conditional nonlow interface.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Direct ordered frequency pairs are used independently of the producer's
window-grouped quadratic masses. A nonconstant1150-direction Jw is checked.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time


def read(p):
    raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def ex(v):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    return F(int(v['numerator']),int(v['denominator']))


def rec(v):return dict(numerator=str(v.numerator),denominator=str(v.denominator),display_only=float(v))


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ('joint','near','candidate','conditional','interface','out'):
        ap.add_argument('--'+n,type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh independent exact certificate required')
    joint,near,candidate,done=[read(getattr(a,n)) for n in ('joint','near','candidate','conditional')]
    if not done['all_gates']:raise ArithmeticError('Only an actual successful conditional ball is checked here')
    spec=importlib.util.spec_from_file_location('checked_nonlow_interface',a.interface);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    model=mod.NonlowInterface(a.joint,a.near)
    caps=[[ex(v) for v in row] for row in done['low_mode_radii']];U=[sum(row,F(0)) for row in caps]
    modes=list(range(2,93,2));scale=ex(done['low_scale'])
    gates=dict(all1150_actual_twice_candidate_modes=caps==[[scale*ex(v) for v in row['separate_mode_caps']] for row in candidate['rows']],
        same_actual_frozen_inputs=done['source_sha256']==sha(a.interface) and all(sha(getattr(a,n)) in done['input_hashes'].values() for n in ('joint','near')),
        no_low_equation_or_full_joint_claim=not done['low_equation_closed'] and not done['full1200_component_fixed_point_claimed'])
    rs=[ex(r['finite_radius']) for r in done['rows']];hs=[ex(r['high_radius']) for r in done['rows']]
    wf=[ex(r['finite_distance_weight']) for r in done['rows']];wh=[ex(r['high_distance_weight']) for r in done['rows']]
    du=[[u*F(1+n,95) for n,u in zip(modes,row)] for row in caps]
    dr=[r/F(i+1) for i,r in enumerate(rs)];dh=[h*F(i+2,29) for i,h in enumerate(hs)];dU=[sum(row,F(0)) for row in du]
    actual=model.action(model.prepare(caps),rs,hs,du,dr,dh)
    winof={m:w for w in near['actual_near_windows'] for m in range(w['window'][0],w['window'][1]+1,2)}
    KT=270*F(2)**-34;K=F(23,9)+KT;B=F(18555);D=F(257);Rmax=ex(joint['profile_physical_upper'])
    rows=[];slacks=[];action_bounds=[]
    for i,row in enumerate(joint['rows']):
        imagef=ex(row['true_finite_head_and_centre']);imageh=ex(row['true_high_head_and_complete_centre'])
        distancef=F(0);distanceh=F(0);actionf=F(0);actionh=F(0);saved_actionf=F(0);saved_actionh=F(0)
        for j in range(i+1):
            G={p:ex(row['all_finite_source_materials'][str(p)][j]) for p in (2,1,0)}
            A={p:ex(row['all_high_source_materials']['physical_source'][str(p)][j]) for p in (2,1,0)}
            Q={p:ex(row['all_high_source_materials']['already_divided_by_frame'][str(p)][j]) for p in (2,1,0)}
            g,a0=G[2],A[2]
            if j==21:
                p=row['profile_source21_kernels'];c,s,d,t=[ex(p[n]) for n in ('finite_cross','finite_square','high_cross','high_square')]
            elif j==5:c,s,d,t=B*G[1],B*B*G[0],D*Q[1],D*B*Q[0]
            else:c=s=g;d=t=a0
            lc=[ex(v['coefficient']) for v in near['rows'][i]['source_rows'][j]['pure_DQ_centre_to_middle_by_low_input']]
            qimage=sum((v*u for v,u in zip(lc,caps[j])),F(0));qaction=sum((v*u for v,u in zip(lc,du[j])),F(0))
            for ki,k in enumerate(modes):
                for ni,n in enumerate(modes):
                    if k+n<94:continue
                    gamma=ex(winof[k+n]['source_rows'][i][j]);alpha=F(5*k*n+1,4*(1+k)*(1+n))
                    qimage+=gamma*alpha*caps[j][ki]*caps[j][ni]/2
                    qaction+=gamma*alpha*caps[j][ki]*du[j][ni]
            u,r,h=U[j],rs[j],hs[j];C=10+u
            tm=KT*(10*u+u*u/2)
            imagef+=qimage+g*tm+K*(g*(C*r+r*r/2)+c*(C+r)*h+s*h*h/2)
            imageh+=a0*tm+K*(a0*(C*r+r*r/2)+d*(C+r)*h+t*h*h/2)
            nn=(K*(g*(C+r)+c*h),K*(c*(C+r)+s*h),K*(a0*(C+r)+d*h),K*(d*(C+r)+t*h))
            distancef+=nn[0]*wf[j]+nn[1]*wh[j];distanceh+=nn[2]*wf[j]+nn[3]*wh[j]
            lowf=qaction+(g*KT*(10+u)+K*(g*r+c*h))*dU[j]
            lowh=(a0*KT*(10+u)+K*(a0*r+d*h))*dU[j]
            actionf+=lowf+nn[0]*dr[j]+nn[1]*dh[j];actionh+=lowh+nn[2]*dr[j]+nn[3]*dh[j]
            saved=done['rows'][i]['complete_causal_nonlow_derivative'][j]
            savedlow=done['rows'][i]['complete_low_input_derivative_columns'][j]
            if not all(ex(v)>=n for v,n in zip(saved,nn)):raise ArithmeticError('A saved complete NN matrix entry was rounded down')
            saved_actionf+=sum((ex(v)*dd for v,dd in zip(savedlow['finite_by_low_input'],du[j])),F(0))+ex(saved[0])*dr[j]+ex(saved[1])*dh[j]
            saved_actionh+=ex(savedlow['high_same_for_each_low_input'])*dU[j]+ex(saved[2])*dr[j]+ex(saved[3])*dh[j]
        domain=(10+U[i]+rs[i])*ex(row['V_max'])+hs[i]*(Rmax if i==21 else B if i==5 else ex(row['V_max']))
        rr=dict(finite_selfmap=imagef<rs[i],high_selfmap=imageh<hs[i],full_complex_domain=domain<F(2)**-34,
            finite_distance=distancef<F(1,2)*wf[i],high_distance=distanceh<F(1,2)*wh[i],
            exact_saved_distance_rows=distancef/wf[i]==ex(done['rows'][i]['finite_distance_exact']) and distanceh/wh[i]==ex(done['rows'][i]['high_distance_exact']),
            displayed_image_records_are_true_upper=ex(done['rows'][i]['finite_image'])>=imagef and ex(done['rows'][i]['high_image'])>=imageh,
            full_1150_nonconstant_Jw_identity=actionf==actual['finite'][i] and actionh==actual['high'][i],
            saved_positive_columns_bound_action=saved_actionf>=actionf and saved_actionh>=actionh)
        if not all(rr.values()):raise ArithmeticError('Independent actual interface check failed '+str((i,rr)))
        rows.append(dict(target_block=i,gates=rr));slacks.extend((rs[i]-imagef,hs[i]-imageh,F(1,2)-distancef/wf[i],F(1,2)-distanceh/wh[i]))
        action_bounds.append(dict(finite=rec(actionf),high=rec(actionh)))
        print(json.dumps(dict(event='independent_complete_mode_row',target=i,all_gates=True)),flush=True)
    gates['all25_rows_all225_gates']=len(rows)==25 and all(all(r['gates'].values()) for r in rows)
    if not all(gates.values()):raise ArithmeticError(str(gates))
    out=dict(schema='visible-flex-independent-complete-lowmode-nonlow-interface-certificate-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gates=gates,
        rows=rows,minimum_positive_selfmap_or_distance_slack=rec(min(slacks)),nonconstant_direction_is_full1150=True,
        low_equation_closed=False,full1200_fixed_point_claimed=False,complete_mean_and_inverse_retained=True,
        checked_source_sha256=sha(a.interface),source_sha256=sha(__file__),input_hashes={str(getattr(a,n)):sha(getattr(a,n)) for n in ('joint','near','candidate','conditional','interface')},
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(all_gates=True,elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
