#!/usr/bin/env python3
"""Actual cell14 endpoint via its original full positive canonical matrix.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only saved R42 density and original positive matrices are consumed. No
cell14 panels are invented. Full cell15 physical Vprime and full cell14
source material are retained, with absolute and true-w units separate.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import resource
import time
from flint import arb,ctx

from closure_split_joint_io_v2 import iter_array,metadata_without_array
from inner_true_cell13_endpoint_window_kernels import (
    sha,read,exact,aq,ab,pack,up,lower_pack,Gates,closed_port_w,WINDOWS,MATERIALS)
from inner_cell12_canonical_forced_endpoint_kernels_v2 import PINS,SOURCE_PINS


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs',type=Path,required=True);p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--rss-kib',type=int,default=98304);a=p.parse_args();ctx.prec=256;ctx.threads=1
    start=time.monotonic();g=Gates();check=g.check;out=Path(str(a.out_prefix)+'.json')
    if out.exists():raise FileExistsError('Fresh immutable cell14 output required')
    for name,wanted in SOURCE_PINS.items():check('all_original_source_helpers',sha(Path(__file__).parent/name)==wanted)
    ids={};paths={}
    for k in ('density','positive','ready'):
        name,wanted=PINS[k];path=a.inputs/name;check('all_original_geometry_sha256',sha(path)==wanted)
        ids[k]={'path':str(path),'sha256':wanted,'bytes':path.stat().st_size};paths[k]=path
    density,ready=read(paths['density']),read(paths['ready'])
    check('all_original_density_gates',all(density['gates'].values()))
    pm=metadata_without_array(paths['positive'],'cell_rows')
    check('same_ready_positive_geometry',PINS['ready'][1] in pm['input_hashes'].values())
    for key in ('closure_positive_linear_band_enclosure.py','closure_real_linear_head_enclosure.py','closure_real_head_source_enclosure.py'):
        check('same_original_positive_generator',pm['source_hashes'][key]==SOURCE_PINS[key])
    rr={r['cell']:r for r in density['rows']};r=rr[14];rnext=rr[15]
    Arows=next(row for row in iter_array(paths['positive'],'cell_rows') if row['cell']==14)['positive_cell_matrices']
    check('adjacent_actual_strip_identity',exact(r['tau_inner'])==exact(r['tau_inner'],'lower')==exact(rnext['tau_outer'])==exact(rnext['tau_outer'],'lower'))
    check('exact_output_strip',exact(r['tau_outer'])==exact(r['tau_outer'],'lower'))
    rc=aq(ready['rationalDeepModel']['physicalParameters']['rCuff']);R=rc*257/256;S=arb(257)/256;sq12=arb(12).sqrt()
    wi,wo=closed_port_w(ready,15),closed_port_w(ready,14)
    win_hi=wi['w'].upper();wout_lo=wo['w'].lower();mu_lo=ab(r['mu_lower'],'lower');mu_hi=ab(r['mu_upper'])
    check('same_actual_mu_source_constant',mu_lo<=wi['mu'].upper() and wi['mu'].lower()<=mu_hi)
    mu_lo=min(mu_lo,wi['mu'].lower());mu_hi=max(mu_hi,wi['mu'].upper())
    B_lo=ab(r['B'],'lower');B_hi=ab(r['B']);Bnext_lo=ab(rnext['B'],'lower')
    check('strict_complete_physical_conversion_domain',rc>0 and wout_lo>0 and win_hi>0 and mu_lo>0 and B_lo>=120 and Bnext_lo>=120)
    jump=up(max(arb(1),B_hi/Bnext_lo));drop=(ab(r['tau_inner'],'lower')-ab(r['tau_outer'])).lower()
    check('positive_complete_cell_strip_drop',drop>0)
    def vmax(row):
        X=ab(row['canonical_total_envelope']);alpha=ab(row['Q_coefficient']);mu=ab(row['mu_upper']);wl=ab(row['w_lower'],'lower')
        check('complete_positive_original_V_row',X>0 and alpha>0 and mu>0 and wl>0)
        return up(X*(alpha*R**3+sq12*mu/(rc**4*wl)))
    V14=vmax(r);V15=vmax(rnext);Vprime15=up(S*V15)
    width=ab(r['normalized_width_upper']);TV=ab(r['TV_log_w_upper'])
    check('complete_positive_original_material_totals',width>0 and TV>0)
    pref=up(R**4*V14**2/(sq12*mu_lo));I={'d1':up(pref*width),'d_lambda':up(pref*TV)}
    rows=[];uncovered=[]
    for lo,hi in WINDOWS:
        cover=[j for j,b in enumerate(pm['bands']) if b['first_mode']<=lo and hi<=b['last_mode']]
        if not cover:uncovered.append([lo,hi]);continue
        j=cover[0];A=[[ab(v) for v in line] for line in Arows[j]]
        check('complete_positive_cell14_matrix',all(z>=0 for line in A for z in line) and A[0][0]>=1 and A[1][1]>=1)
        nulo=arb(lo*lo*(lo*lo-1))/12;nuhi=arb(hi*hi*(hi*hi-1))/12
        cin=[up(1/(B_lo*lo*rc**3)),up(R**4*win_hi/(sq12*mu_lo*nulo)*max(arb(1),arb(hi)/B_lo))]
        cout=[up((B_hi*hi+hi*hi)*R**3),up(sq12*mu_hi*nuhi/(rc**4*wout_lo))]
        propagated=[up(A[i][0]*cin[0]+A[i][1]*cin[1]) for i in range(2)]
        decay=up((-lo*drop).exp());check('actual_positive_full_homogeneous_strip_loss',0<decay<1)
        Kabs=up(2*jump*(arb(1)+hi)/(1+lo)*decay*sum((cout[i]*propagated[i] for i in range(2)),arb(0)))
        Kcut=up(Kabs/wout_lo);Knorm=up(Kabs*Vprime15);Knormcut=up(Knorm/wout_lo)
        source_gain=up(2*(1+hi)*S**2/nulo*(cout[0]*A[0][1]+cout[1]*A[1][1]))
        source_abs={mat:up(source_gain*I[mat]) for mat in MATERIALS}
        source_cut={mat:up(source_abs[mat]/wout_lo) for mat in MATERIALS}
        rows.append({'window':[lo,hi],'original_matrix_window':[pm['bands'][j]['first_mode'],pm['bands'][j]['last_mode']],
            'whole_cell_positive_matrix_upper':[[pack(z) for z in line] for line in A],
            'input_absolute_to_canonical_covector_bounds':list(map(pack,cin)),
            'canonical_to_output_absolute_covector_bounds':list(map(pack,cout)),
            'full_homogeneous_strip_multiplier_upper':pack(decay),
            'input_absolute_mass_to_absolute_endpoint':pack(Kabs),'input_absolute_mass_to_cut':pack(Kcut),
            'input_cell15_Vprime_mass_to_absolute_endpoint':pack(Knorm),'input_cell15_Vprime_mass_to_cut':pack(Knormcut),
            'source_absolute_gain_upper':pack(source_gain),
            'source_two_material_to_absolute_endpoint':{mat:pack(source_abs[mat]) for mat in MATERIALS},
            'source_two_material_to_cut':{mat:pack(source_cut[mat]) for mat in MATERIALS},
            'source_common_to_cut':pack(source_cut['d1']+source_cut['d_lambda'])})
    check('only_original_nine_matrix_windows_used',len(rows)==11 and uncovered==[[2050,4096],[4098,8190]])
    check('owned_RSS_guard',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=a.rss_kib)
    result={'schema':'inner-true-cell14-whole-canonical-endpoint-two-material-v1','author':'geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        'all_gates':True,'gate_count':g.count,'gates':{k:True for k in g.by_name},'gate_multiplicities':g.by_name,
        'source_sha256':sha(__file__),'input_identities':ids,'frozen_reference_source_sha256':SOURCE_PINS,
        'cell':14,'input_cell':15,'no_saved_cell14_panels_assumed':True,'global_physical_radius_bounds':[lower_pack(rc),pack(R)],
        'source_mu_bounds':[lower_pack(mu_lo),pack(mu_hi)],'true_w_in_lower':lower_pack(wi['w']),'true_w_in_upper':pack(wi['w']),
        'true_w_out_lower':lower_pack(wout_lo),'true_w_out_upper':pack(wo['w']),
        'frame_jump_upper':pack(jump),'tau_input':rnext['tau_outer'],'tau_cell_inner':r['tau_inner'],'tau_output':r['tau_outer'],
        'normalization_S':'257/256','source_scale_squared_upper':pack(S**2),
        'cell14_complete_Vstrong_upper':pack(V14),'cell15_complete_Vstrong_upper':pack(V15),'cell15_complete_Vprime_upper':pack(Vprime15),
        'whole_cell_canonical_source_integrals_before_S_squared_upper':{mat:pack(I[mat]) for mat in MATERIALS},
        'original_material_totals':{'normalized_width_upper':r['normalized_width_upper'],'TV_log_w_upper':r['TV_log_w_upper']},
        'source_units':'Original moving-tau weak Fourier pair coefficient of physical kappa source d1=Vprime14^2/(r*w), d_lambda=abs(w_r/w)*Vprime14^2/w. Vprime14=(257/256)*Vstrong14; S^2 is already paid once.',
        'absolute_input_units':'Sum(1+m)*exp(m*tau15_out)*(abs(B15*p_m)+abs(kappa_m)) at the actual cell15 outer port; frame jump to B14 is paid.',
        'normalized_input_units':'Same cell15 strong mass divided by its full original Vprime15 envelope; the full-cell upper Vprime15 is explicitly multiplied, never treated as a pointwise lower denominator.',
        'absolute_output_units':'Sum(1+m)*exp(m*tau14_out)*(abs(B14*p_m)+abs(kappa_m)) at the actual cell14 outer port.',
        'cut_output_units':'The corresponding absolute output divided by the true w14_out. This is not cell12 cut unless the remaining original cells are separately propagated.',
        'positive_source_proof':'The original nonnegative comparison generator makes each saved whole-cell A bound every suffix. All cell14 I_mat/nu_lo source is multiplied by A[:,1], with no free whole-cell strip decay.',
        'complete_cell15_input_and_complete_cell14_source_required':True,'factor_two_retained':True,
        'uncovered_windows_keep_original_kernels':uncovered,'infinite_far_mean_inverse_source_bounds_changed':False,
        'new_fixedpoint_or_truecut_consistency_claimed':False,'new_ODE_radial_quadrature_source_field_evaluation_Node_calls':0,
        'rows':rows,'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    data=(json.dumps(result,indent=2)+'\n').encode()
    if len(data)>=1000000:raise ValueError('Small endpoint packet required')
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(data)
    print(json.dumps({'all_gates':True,'path':str(out),'sha256':sha(out),'gate_count':g.count,'first_row':{k:str(ab(v)) for k,v in rows[0].items() if k in ('input_absolute_mass_to_absolute_endpoint','input_cell15_Vprime_mass_to_absolute_endpoint')},'elapsed_seconds':result['elapsed_seconds'],'peak_rss_kib':result['peak_rss_kib']}),flush=True)


if __name__=='__main__':main()
