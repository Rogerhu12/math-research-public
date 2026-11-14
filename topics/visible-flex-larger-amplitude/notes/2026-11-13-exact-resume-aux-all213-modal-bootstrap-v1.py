#!/usr/bin/env python3
"""Finite full213 modal substitution for the existing R74 auxiliary family.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All46 actual low modes, original cellwise reference strips, all213 Green
sources, complete mean/inverse remainder, and one shared far mass remain.
No existence, asymptotic convergence, ODE, or new Green computation.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb,arb_mat,arb_poly,ctx


def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ab(v):return arb(int(v[0]))*arb(2)**int(v[1])


def pack(v,bits=160):
    if not v.is_finite():raise ArithmeticError('Every source, matrix value and output must be finite')
    t=v.upper()
    if not t>=0:raise ArithmeticError('Positive finite bootstrap produced a negative upper')
    if t==0:return ['0',0]
    m,e=t.man_exp();m,e=int(m),int(e);shift=max(0,m.bit_length()-bits)
    if shift:m,e=(m+(1<<shift)-1)>>shift,e+shift
    if not ab([m,e])>=t:raise ArithmeticError('Outward dyadic serialization failed')
    return [str(m),e]


def up(x):return ab(pack(x))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('input','input-resource','out-prefix'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--passes',type=int,default=32);p.add_argument('--rss-kib',type=int,default=98304)
    a=p.parse_args();ctx.prec=256;ctx.threads=1;started=time.monotonic();out=Path(str(a.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('Keep original complete modal attempts immutable')
    if not 1<=a.passes<=128:raise ValueError('Declare a finite original pass count')
    d=read(a.input);usage=read(a.input_resource)
    if not(d['schema']=='inner-r74-all213-canonical-modal-bootstrap-input-v1' and d['all_gates'] and all(d['gates'].values())
           and d['cells']==list(range(12,225)) and d['modes']==list(range(2,93,2))
           and usage['exitcode']==0 and usage['termination_signal'] is None):raise ArithmeticError('Complete same-family actual canonical input required')
    A=arb_mat(213,213)
    if len(d['A_upper'])!=213:raise ArithmeticError('All original Green targets required')
    for k,row in enumerate(d['A_upper']):
        if len(row)!=213:raise ArithmeticError('All original Green sources required')
        for n,val in enumerate(row):
            z=ab(val)
            if not(z.is_finite() and z>0):raise ArithmeticError('Every original positive canonical kernel must be finite')
            A[k,n]=z
    linear=[];linear_common=[];original_total=[];rho=[];errors=[];far=[];rphysical=[];corr=[]
    for n,row in enumerate(d['rows']):
        if row['cell']!=12+n:raise ArithmeticError('Canonical input ordering changed')
        linear.append(list(map(ab,row['linear_pair_caps_over_reference'])))
        linear_common.append(ab(row['linear_common_cap_over_reference']))
        original_total.append(ab(row['original_total_field_common_cap_over_reference']))
        rho.append(ab(row['initial_correction_common_cap_over_reference']))
        errors.append(list(map(ab,row['initial_correction_pair_caps_over_reference'])))
        far.append(ab(row['far_correction_common_over_reference']))
        rphysical.append(ab(row['source_Rmax_per_unit_common']))
        corr.append(list(map(ab,row['difference_correlation_upper_by_positive_minimum_mode'])))
        if not(all(len(v)==46 for v in (linear[-1],errors[-1],corr[-1]))
               and all(z.is_finite() and z>=0 for z in linear[-1])
               and all(z.is_finite() and z>0 for z in errors[-1]+corr[-1]+[rho[-1],far[-1],original_total[-1],rphysical[-1]])
               and all(z<=1 for z in corr[-1])):raise ArithmeticError('Complete positive true modal input required')
    initial_rho=list(rho);initial_errors=[list(v) for v in errors]
    history=[];qco=arb(23)/288;rco=arb(13)/16
    final_source=None;final_X=None;final_caps=None;final_rem=None;final_conv=None;final_R=None
    def sources():
        V=arb_mat(213,47);XS=[];caps=[];remainders=[];convs=[];Rs=[]
        for n in range(213):
            ee=min(rho[n],up(sum(errors[n],arb(0))))
            X=min(original_total[n],up(linear_common[n]+ee),up(sum(linear[n],arb(0))+ee))
            cap=[min(X,up(linear[n][j]+errors[n][j])) for j in range(46)]
            poly=arb_poly([arb(0)]+cap)
            diff=arb_poly([up(cap[45-j]*corr[n][45-j]) for j in range(46)])
            sprod=poly*poly;dprod=diff*poly
            conv=[min(up(sprod[j+1]/2+dprod[47+j]),up(X*X)) for j in range(46)]
            # diff reverses degree a to46-a; output m index j+1 is46+j+1.
            R=up(rphysical[n]*X)
            if not R<=arb(1)/64:raise ArithmeticError('Complete R106 mean/inverse remainder domain is unpaid')
            rem=up(rco*R*X*X)
            for j in range(46):V[n,j]=up(qco*conv[j]+rem)
            V[n,46]=up(qco*min(up(sum(conv,arb(0))),up(X*X))+rem)
            XS.append(X);caps.append(cap);remainders.append(rem);convs.append(conv);Rs.append(R)
        return V,XS,caps,remainders,convs,Rs
    for step in range(1,a.passes+1):
        V,XS,caps,rems,convs,Rs=sources();mapped=A*V
        newrho=[];newerrors=[]
        for n in range(213):
            common=min(rho[n],up(mapped[n,46]+far[n]))
            row=[min(errors[n][j],common,up(mapped[n,j]+far[n])) for j in range(46)]
            common=min(common,up(sum(row,arb(0))))
            row=[min(z,common) for z in row]
            if not(common>0 and common<=rho[n] and all(z>0 and z<=errors[n][j] for j,z in enumerate(row))):raise ArithmeticError('A complete monotone finite induction gate failed')
            newrho.append(common);newerrors.append(row)
        rho,errors=newrho,newerrors
        if step&(step-1)==0 or step==a.passes:
            record=dict(step=step,all213_common_error_over_reference=list(map(pack,rho)),
                max_complete_relative_physical=pack(max(Rs)),cell12_error=pack(rho[0]),
                maximum_original_radius_ratio=pack(max(up(rho[n]/initial_rho[n]) for n in range(213))))
            history.append(record)
            print(json.dumps(dict(event='same_aux_all213_modal_finite_pass',step=step,cell12_error_display=str(rho[0]),max_radius_ratio_display=str(max(up(rho[n]/initial_rho[n]) for n in range(213))),elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned actual modal bootstrap RSS guard')
    V,XS,caps,rems,convs,Rs=sources();rows=[]
    for n,row in enumerate(d['rows']):
        rows.append(dict(cell=12+n,reference_x_upper=row['reference_x_upper'],
            final_correction_common_cap_over_reference=pack(rho[n]),final_correction_pair_caps_over_reference=list(map(pack,errors[n])),
            final_complete_common_cap_over_reference=pack(XS[n]),final_complete_pair_caps_over_reference=list(map(pack,caps[n])),
            final_source_Q_pair_convolutions_over_reference_squared=list(map(pack,convs[n])),
            final_source_complete_common_over_B_reference_squared=pack(V[n,46]),
            final_source_complete_pair_caps_over_B_reference_squared=[pack(V[n,j]) for j in range(46)],
            complete_mean_inverse_shared_remainder_over_B_reference_squared=pack(rems[n]),
            full_relative_physical_norm=pack(Rs[n]),positive_shared_far_over_reference=row['far_correction_common_over_reference']))
    result=dict(schema='inner-r74-all213-canonical-modal-finite-bootstrap-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
        all_gates=True,gates=dict(all213_original_cells=True,all46_original_modes=True,all45369_positive_source_target_entries=True,
            complete_R74_existing_complex_family=True,complete_original_cellwise_reference_strips=True,
            actual_positive_true_far_in_every_target=True,complete_mean_and_inverse_shared_remainder=True,
            common_mass_and_modal_caps_simultaneous=True,all_finite_passes_exact_positive_outward=True,
            every_computed_coefficient_finite=True,all_original_physical_domains=True),
        input_identity=dict(path=str(a.input),sha256=sha(a.input)),input_resource_identity=dict(path=str(a.input_resource),sha256=sha(a.input_resource)),
        source_sha256=sha(__file__),passes=a.passes,cells=d['cells'],modes=d['modes'],precision_bits=ctx.prec,
        finite_history=history,rows=rows,
        recurrence='E_km_new=min(E_km, rho_k_new, sum_n A_kn[(23/288)conv_nm+(13/16)R_n X_n^2]+far_k); common uses sum_m conv once, shared remainder andfar once',
        same_existing_auxiliary=True,full_inner_head_claimed=False,new_existence_claimed=False,
        canonical_frequency_weights='Per-cell original tau_n, sum frequency and exact difference correlation exp(-2 min(a,b) tau_n), paired half factors retained',
        no_ODE_or_Green_or_radial_integration=True,elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw=(json.dumps(result,separators=(',',':'))+'\n').encode();out.write_bytes(gzip.compress(raw,mtime=0))
    if out.stat().st_size>=5_000_000:raise ArithmeticError('Split complete all213 modal output')
    print(json.dumps(dict(all_gates=True,path=str(out),sha256=sha(out),bytes=out.stat().st_size,passes=a.passes,elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
