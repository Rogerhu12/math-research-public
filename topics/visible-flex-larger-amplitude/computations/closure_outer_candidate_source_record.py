#!/usr/bin/env python3
"""Record full original outer-candidate sources at their true radial panels.

The frozen candidate/residual entry point is executed unchanged except for
a read-only callback. Every original aggregate mathematical field must
reproduce the paid package exactly. Selected cosine source coefficients
use their finite quadratic polynomial plus a rigorous complete mean and
Wiener-inverse remainder. No source integration or ODE is started.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

from flint import acb, arb

from closure_real_head_source_enclosure import exact_q
from closure_split_joint_io_v2 import digest, iter_array
from closure_shared_slope_cut_interface import record
import tail_outer_candidate_defect as original_entry


EXPECTED_SOURCES = {
    'tail_outer_candidate_defect.py': '241104402884d7988df2af8d3881c889cfc4e3d70486de6b3ef6ab76645a45bf',
    'tail_outer_full_mean_residual_bounds.py': '16f9d2d5c2e858686aff9d332df4cc565606481ab45a46d6a9080db29317c8af',
    'tail_outer_candidate_domain.py': '17d6b7d85be80f8f40b3eec411ae49a73c51c6b624d030df57b94202a7d08690',
}


def signed_source_bounds(H, K, full, *, modes, radius, radius_x, w,
                         log_w_x, norms, tau, selected):
    """Exact selected quadratic coefficients, and a full W1 remainder.

N=(Q+delta_Q)/(1+c+K+E*T), |c|<=4*R^2. Thus
||N-Q||_1 <= (||delta_Q||_1 + l*||Q||_1)/(1-l),
l=|c|+||K+E*T||_1. The two mean terms of delta_Q are
ell*(2*c*(K+T)+c^2+2*w^2*c*T); all mean/inverse modes remain.
"""
    r, rx, ell = radius, radius_x, log_w_x
    z, E, s = w*w, 1+w*w, rx/r
    c = full['complete_mean_abs']
    Pn, Kn = norms['P_tau'], norms['K_tau']
    Tn, Un = full['P_theta_W1'], full['K_theta_minus_P_W1']
    l = (c+norms['nonmean_L_tau']).upper()
    if not l < 1:
        raise ArithmeticError('The actual complete analytic leading inverse is unavailable')
    Qnorm = (E.upper()*s.upper()*Un*Un+abs(ell).upper()*
             ((Kn+Tn)**2+z.upper()*(2*Kn*Tn+Tn*Tn+Pn*Pn))).upper()
    mean_numerator = (abs(ell).upper()*
                      (2*c*(Kn+Tn)+c*c+2*z.upper()*c*Tn)).upper()
    remainder = ((mean_numerator+l*Qnorm)/(1-l)).upper()
    keys = sorted(H)
    if set(H) != set(K) or keys != sorted(sign*m for m in modes for sign in (-1, 1)):
        raise ValueError('The full signed actual M20 candidate spectrum is required')
    P = {m:acb(0,m)*H[m]/(r*w) for m in keys}
    T = {m:acb(0,m)*P[m] for m in keys}
    U = {m:acb(0,m)*K[m]-P[m] for m in keys}
    C = {m:K[m]+T[m] for m in keys}
    def conv(a,b,m):
        return sum((a[j]*b[m-j] for j in keys if m-j in b),acb(0))
    rows=[]
    for m in selected:
        q = E*s*conv(U,U,m)+ell*(conv(C,C,m)+z*
             (2*conv(K,T,m)+conv(T,T,m)-conv(P,P,m)))
        if not q.imag.contains(0):
            raise ArithmeticError('The actual even real source lost its cosine symmetry')
        qcos = 2*q.real
        # Divide by the LOWER enclosure of the TRUE analytic weight.
        # The rounded-up weights used to bound input norms are not used
        # as an unjustified larger denominator in coefficient estimates.
        weight = ((1+m)*(exact_q(tau)*m).exp()).lower()
        if not weight > 0:
            raise ArithmeticError('A true Fourier weight is not positive')
        error = (remainder/weight).upper()
        total_cap = (full['complete_nonlinear_source_W1']/weight).upper()
        raw = qcos+(-error).union(error)
        lo,hi=max(raw.lower(),-total_cap),min(raw.upper(),total_cap)
        if not lo <= hi:
            raise ArithmeticError('The two true source coefficient enclosures are disjoint')
        rows.append(dict(mode=m,quadratic_cosine=record(qcos),
            complete_remainder_cosine_radius=record(error),
            complete_source_cosine=record(lo.union(hi))))
    return dict(quadratic_W1_upper=record(Qnorm),
        complete_mean_numerator_change_W1_upper=record(mean_numerator),
        leading_nonconstant_plus_mean_W1_upper=record(l),
        complete_source_minus_quadratic_W1_upper=record(remainder),
        selected_cosine_sources=rows)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('cell-manifest','port-candidates','response','ready','reference-defect','out-prefix'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--tau',default='1/64')
    p.add_argument('--inverse-degree',type=int,default=8)
    p.add_argument('--rss-kib',type=int,default=40960)
    a=p.parse_args()
    began=time.monotonic()
    replay=Path(str(a.out_prefix)+'-domain-replay.json')
    summary=Path(str(a.out_prefix)+'-summary.json')
    if replay.exists() or summary.exists():
        raise FileExistsError('Use a fresh complete source-recorder prefix')
    for name,expected in EXPECTED_SOURCES.items():
        if digest(Path(__file__).with_name(name)) != expected:
            raise ValueError('The actually paid candidate or residual source changed: '+name)
    data=json.loads(a.cell_manifest.read_text())
    reference=json.loads(a.reference_defect.read_text())
    if (not all(data['checks'].values()) or not all(reference['gates'].values())
            or data['cell'] != reference['cell'] or data['cell'] not in (10,11)
            or reference['tau'] != a.tau or reference['inverse_degree'] != a.inverse_degree):
        raise ValueError('The complete same actual small-root outer candidate is required')
    paths=[getattr(a,k) for k in ('cell_manifest','port_candidates','response','ready','reference_defect')]
    hashes={str(path):digest(path) for path in paths}
    for path in paths[:-1]:
        if reference['input_hashes'].get(str(path)) != hashes[str(path)]:
            raise ValueError('A frozen mathematical candidate input changed')
    groups=sorted(data['groups'],key=lambda x:x['source_segment'])
    if [g['source_segment'] for g in groups] != list(range(9)):
        raise ValueError('All nine real source segments are required')
    def panels():
        for group in groups:
            path=Path(group['path'])
            if digest(path)!=group['sha256']:
                raise ValueError('A complete true material source group changed')
            for i,g in enumerate(iter_array(path,'panels')):
                yield group,i,g
    panel_iterator=iter(panels())
    owned=[]
    active=None
    active_segment=None
    active_count=0
    active_path=None
    count=0
    tau=Fraction(a.tau)
    raw_callback=original_entry.full_mean_residual_bounds
    max_remainder=arb(0)
    def close_group():
        nonlocal active,active_count,active_path
        if active is None:
            return
        active.write('\n]}\n')
        active.close()
        active=None
        expected=groups[active_segment]['panels']
        if active_count!=expected:
            raise ValueError('An original complete material segment was not fully recorded')
        if active_path.stat().st_size>5*1024*1024:
            raise ValueError('A reproducible source group exceeds the repository file cap')
        item=dict(segment=active_segment,panels=active_count,path=str(active_path),
            bytes=active_path.stat().st_size,sha256=digest(active_path))
        owned.append(item)
        print(json.dumps(dict(event='complete_source_group',cell=data['cell'],**item,
            seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    def callback(H,K,Kx,**kw):
        nonlocal active,active_segment,active_count,active_path,count,max_remainder
        full=raw_callback(H,K,Kx,**kw)
        group,i,g=next(panel_iterator)
        segment=group['source_segment']
        if segment!=active_segment:
            close_group()
            active_segment=segment
            active_count=0
            active_path=Path(str(a.out_prefix)+f'-segment{segment}.json.gz')
            if active_path.exists():
                raise FileExistsError('A recorded complete source segment would be overwritten')
            active=gzip.open(active_path,'wt',compresslevel=9)
            active.write('{"cell":'+str(data['cell'])+',"segment":'+str(segment)+
                ',"tau":'+json.dumps(a.tau)+',"original_material_sha256":'+
                json.dumps(group['sha256'])+',"panels":[\n')
        if i!=active_count or g['segment']!=segment:
            raise ValueError('The actual residual callback order differs from its material panels')
        signed=signed_source_bounds(H,K,full,modes=kw['modes'],radius=kw['radius'],
            radius_x=kw['radius_x'],w=kw['w'],log_w_x=kw['log_w_x'],
            norms=kw['norms'],tau=tau,selected=[2,4])
        from closure_shared_slope_cut_interface import ball
        max_remainder=max(max_remainder,ball(signed['complete_source_minus_quadratic_W1_upper']).upper())
        row={key:g[key] for key in ('segment','x_left','x_right','original_parent','radius_left',
            'radius_right','radius','radius_x','w','log_w_x','width')}
        row.update(panel=i,complete_nonlinear_source_W1=record(full['complete_nonlinear_source_W1']),
            complete_nonmean_source_residual_W1=record(full['complete_nonmean_source_residual_W1']),
            physical_nonmean_second_source_W1=record(full['physical_nonmean_second_source_W1']),
            complete_mean_abs=record(full['complete_mean_abs']),**signed)
        if active_count:
            active.write(',\n')
        active.write(json.dumps(row,separators=(',',':')))
        active_count+=1
        count+=1
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:
            raise MemoryError('The owned source recorder exceeded its RSS observation threshold')
        return full
    original_entry.full_mean_residual_bounds=callback
    original_argv=sys.argv
    sys.argv=[str(Path(original_entry.__file__)),
        '--cell-manifest',str(a.cell_manifest),'--port-candidates',str(a.port_candidates),
        '--response',str(a.response),'--ready',str(a.ready),'--out',str(replay),
        '--tau',a.tau,'--inverse-degree',str(a.inverse_degree),
        '--rss-limit-mib',str(a.rss_kib//1024)]
    try:
        original_entry.main()
        close_group()
        if next(panel_iterator,None) is not None or count!=data['panels'] or len(owned)!=9:
            raise ValueError('The actual complete source range was not exhausted')
        check=json.loads(replay.read_text())
        excluded={'elapsed_seconds','peak_RSS_KiB'}
        old={k:v for k,v in reference.items() if k not in excluded}
        new={k:v for k,v in check.items() if k not in excluded}
        if old!=new:
            changed=[k for k in sorted(set(old)|set(new)) if old.get(k)!=new.get(k)]
            raise ValueError('The original mathematical output failed exact reproduction: '+str(changed))
        gates=dict(original_candidate_and_all20_modes_unchanged=True,
            original_aggregate_mathematics_bitwise_reproduced=True,
            all_original_true_material_panels_recorded=True,
            complete_mean_and_inverse_remainder_in_selected_signed_sources=True,
            true_angular_weight_lower_used_for_coefficient_caps=True,
            same_background_and_same_source_coordinate=True,
            no_new_source_integrals_or_ODE=True)
        result=dict(status='Complete position-resolved actual candidate N and selected signed coefficients',
            cell=data['cell'],panels=count,tau=a.tau,selected_cosine_modes=[2,4],
            original_candidate_modes=reference['modes'],groups=owned,gates=gates,all_gates=True,
            original_aggregate_replay_path=str(replay),original_aggregate_replay_sha256=digest(replay),
            maximum_complete_source_minus_quadratic_W1=record(max_remainder),
            source_units='N_perp in Kbar_x=-ell(2Kbar+P_theta)+N_perp. Multiply by (r/rc)^u*r^4*w^2/(sqrt12*mu11) for the fixed-global-gauge v_x forcing.',
            signed_source_proof='N=(Q+deltaQ)/(1+c+K+E*T); |c|<=4R^2, l=|c|+||K+E*T||_1<1, ||N-Q||_1<=(||deltaQ||_1+l||Q||_1)/(1-l). Full mean and every inverse-generated mode retained.',
            actual_forced_Schur_integral_paid=False,complete_outer_solution_claimed=False,
            input_hashes=hashes,source_hashes=EXPECTED_SOURCES,entrypoint_sha256=digest(Path(__file__)),
            elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        summary.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(dict(event='complete_source_recorder',summary=str(summary),panels=count,
            all_gates=True,seconds=result['elapsed_seconds'],peak_RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    except Exception as error:
        if active is not None:
            active.close()
        failure=Path(str(a.out_prefix)+'-failure.json')
        failure.write_text(json.dumps(dict(status='Incomplete source recorder, no complete source claim',
            error=repr(error),completed_groups=owned,recorded_panels=count,input_hashes=hashes,
            entrypoint_sha256=digest(Path(__file__)),elapsed_seconds=time.monotonic()-began),indent=2)+'\n')
        raise
    finally:
        original_entry.full_mean_residual_bounds=raw_callback
        sys.argv=original_argv


if __name__=='__main__':
    main()
