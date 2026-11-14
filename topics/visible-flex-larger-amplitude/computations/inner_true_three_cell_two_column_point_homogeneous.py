#!/usr/bin/env python3
"""Saved canonical matrices to exact physical two-column point readouts.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
At a single port the actual physical input is U+V=|B_next*p|+|kappa|.
The two positive columns share that one mass, so their maximum is used.
No extra whole-cell separate-sup factor2 or duplicate frame jump is added.
All generated source remains outside this homogeneous-only packet.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path
import resource
import time
from flint import arb,ctx
from closure_split_joint_io_v2 import iter_array,metadata_without_array
from inner_true_cell13_endpoint_window_kernels import (
    sha,read,exact,aq,ab,pack,up,lower_pack,Gates,closed_port_w,WINDOWS)
from inner_cell12_canonical_forced_endpoint_kernels_v2 import PINS,SOURCE_PINS

PANELS13_SHA='7397ebc436ae5c4cd396ae2e6d5d27c4f2b45e17fae5e75f94eb0acb9e95dc22'


def endpoints(path,expected,check):
    first=last=None;segment=0;end=F(0);count=0
    for row in iter_array(path,'panels'):
        j=row['segment'];left,right=F(*row['x_left']),F(*row['x_right'])
        if j==segment:check('original_physical_panel_order',left==end)
        else:check('complete_original_panel_segment',j==segment+1 and end==1 and left==0);segment=j
        check('strict_original_panel_range',0<=left<right<=1);end=right;count+=1
        if first is None:first=row
        last=row
    check('complete_original_endpoint_source',count==expected and segment==8 and end==1)
    return first['radius_left'],last['radius_right']


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('inputs','panels13','out-prefix'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--rss-kib',type=int,default=98304);a=p.parse_args();ctx.prec=256;ctx.threads=1
    start=time.monotonic();g=Gates();check=g.check;out=Path(str(a.out_prefix)+'.json')
    if out.exists():raise FileExistsError('Fresh point readout required')
    paths={};ids={}
    for name in ('density','positive','ready','panels'):
        base,wanted=PINS[name];pth=a.inputs/base;check('all_original_input_sha256',sha(pth)==wanted)
        paths[name]=pth;ids[name]={'path':str(pth),'sha256':wanted}
    check('all_original_cell13_panels_sha256',sha(a.panels13)==PANELS13_SHA)
    ids['panels13']={'path':str(a.panels13),'sha256':PANELS13_SHA}
    for name,wanted in SOURCE_PINS.items():check('all_original_helper_sources',sha(Path(__file__).parent/name)==wanted)
    density,ready=read(paths['density']),read(paths['ready']);check('complete_original_density',all(density['gates'].values()))
    rr={r['cell']:r for r in density['rows']};pm=metadata_without_array(paths['positive'],'cell_rows')
    check('same_ready_positive_geometry',PINS['ready'][1] in pm['input_hashes'].values())
    for name in ('closure_positive_linear_band_enclosure.py','closure_real_linear_head_enclosure.py','closure_real_head_source_enclosure.py'):
        check('same_positive_comparison_generator',pm['source_hashes'][name]==SOURCE_PINS[name])
    mats={r['cell']:r['positive_cell_matrices'] for r in iter_array(paths['positive'],'cell_rows') if r['cell'] in (12,13,14)}
    check('all_actual_three_cell_matrices',sorted(mats)==[12,13,14])
    in12,out12=endpoints(paths['panels'],1873,check);in13,out13=endpoints(a.panels13,1975,check)
    rc=aq(ready['rationalDeepModel']['physicalParameters']['rCuff']);R=rc*257/256;S=arb(257)/256;sq12=arb(12).sqrt()
    lo13=max(ab(in12,'lower'),ab(out13,'lower'));hi13=min(ab(in12),ab(out13))
    check('same_actual_node13_radius_intersection',0<lo13<=hi13)
    ports={12:(ab(out12,'lower'),ab(out12)),13:(lo13,hi13),14:(ab(in13,'lower'),ab(in13)),15:(rc,R)}
    for lo,hi in ports.values():check('same_original_positive_radius_domain',rc<=lo<=hi<=R)
    cells=[]
    for n in (12,13,14):
        r,rnext=rr[n],rr[n+1];rinlo,rinhi=ports[n+1];routlo,routhi=ports[n]
        check('same_adjacent_actual_strip',exact(r['tau_inner'])==exact(r['tau_inner'],'lower')==exact(rnext['tau_outer'])==exact(rnext['tau_outer'],'lower'))
        wi,wo=closed_port_w(ready,n+1),closed_port_w(ready,n)
        winlo,winhi=wi['w'].lower(),wi['w'].upper();woutlo=wo['w'].lower()
        mulo=min(ab(r['mu_lower'],'lower'),wi['mu'].lower());muhi=max(ab(r['mu_upper']),wi['mu'].upper())
        Bnextlo=ab(rnext['B'],'lower');Bhi=ab(r['B']);drop=(ab(r['tau_inner'],'lower')-ab(r['tau_outer'])).lower()
        check('all_actual_positive_point_denominators',winlo>0 and woutlo>0 and mulo>0 and Bnextlo>=120 and drop>0)
        # Vstrong of the INPUT cell at this particular port. Its mu index is
        # n+1, unlike the current canonical system's mu_n.
        Xnext=ab(rnext['canonical_total_envelope']);anext=ab(rnext['Q_coefficient']);munext=ab(rnext['mu_upper'])
        Vnext=up(S*Xnext*(anext*rinhi**3+sq12*munext/(rinlo**4*winlo)))
        whole=up(S*Xnext*(anext*R**3+sq12*munext/(rc**4*ab(rnext['w_lower'],'lower'))))
        check('actual_boundary_Vprime_below_wholecell',0<Vnext<=whole)
        rows=[];uncovered=[]
        for lo,hi in WINDOWS:
            js=[j for j,b in enumerate(pm['bands']) if b['first_mode']<=lo and hi<=b['last_mode']]
            if not js:uncovered.append([lo,hi]);continue
            j=js[0];A=[[ab(z) for z in line] for line in mats[n][j]]
            check('complete_positive_canonical_matrix',all(z>=0 for line in A for z in line))
            nulo=arb(lo*lo*(lo*lo-1))/12;nuhi=arb(hi*hi*(hi*hi-1))/12
            z=up(rinhi**4*winhi/(sq12*mulo*nulo))
            columns={'B_p':[up(1/(Bnextlo*lo*rinlo**3)),up(z*hi/Bnextlo)],'kappa':[arb(0),z]}
            cout=[up((Bhi*hi+hi*hi)*routhi**3),up(sq12*muhi*nuhi/(routlo**4*woutlo))]
            decay=up((-lo*drop).exp());ratio=(arb(1)+hi)/(1+lo)
            outcols={}
            for kind,v in columns.items():
                prop=[up(A[i][0]*v[0]+A[i][1]*v[1]) for i in range(2)]
                outcols[kind]=up(ratio*decay*sum((cout[i]*prop[i] for i in range(2)),arb(0)))
            K=max(outcols.values());Kcut=up(K/woutlo);KN=up(K*Vnext);KNcut=up(KN/woutlo)
            check('common_one_mass_maximum_of_two_columns',K==max(outcols['B_p'],outcols['kappa']) and K>0)
            rows.append({'window':[lo,hi],'original_matrix_window':[pm['bands'][j]['first_mode'],pm['bands'][j]['last_mode']],
                'whole_cell_positive_matrix_upper':[[pack(v) for v in line] for line in A],
                'input_physical_to_canonical_columns_upper':{k:list(map(pack,v)) for k,v in columns.items()},
                'canonical_to_output_physical_covector_upper':list(map(pack,cout)),
                'full_strip_multiplier_upper':pack(decay),'strong_weight_ratio_upper':pack(ratio),
                'input_physical_pair_columns_to_absolute_endpoint':{k:pack(v) for k,v in outcols.items()},
                'input_absolute_mass_to_absolute_endpoint':pack(K),'input_absolute_mass_to_cut':pack(Kcut),
                'input_nextcell_Vprime_mass_to_absolute_endpoint':pack(KN),'input_nextcell_Vprime_mass_to_cut':pack(KNcut)})
        check('only_original_nine_windows_used',len(rows)==11 and uncovered==[[2050,4096],[4098,8190]])
        cells.append({'cell':n,'input_cell':n+1,'input_physical_radius':[lower_pack(rinlo),pack(rinhi)],
            'output_physical_radius':[lower_pack(routlo),pack(routhi)],'input_radius_has_original_panels':n+1 in (13,14),
            'true_w_in_lower':lower_pack(winlo),'true_w_in_upper':pack(winhi),'true_w_out_lower':lower_pack(woutlo),'true_w_out_upper':pack(wo['w']),
            'current_canonical_mu_bounds':[lower_pack(mulo),pack(muhi)],'input_Vprime_mu_index':n+1,
            'tau_input':rnext['tau_outer'],'tau_inner':r['tau_inner'],'tau_output':r['tau_outer'],
            'input_frame_B_lower':lower_pack(Bnextlo),'output_frame_B_upper':pack(Bhi),
            'input_Vprime_kind':'actual-port-upper','nextcell_Vprime_boundary_upper':pack(Vnext),
            'nextcell_Vprime_wholecell_upper_for_comparison':pack(whole),
            'nextcell_Vprime_boundary_definition':'S*X_next*(Q_coefficient_next*r_port_hi^3+sqrt(12)*mu_next_hi/(r_port_lo^4*w_port_lo)), with S=257/256.',
            'absolute_input_units':'sum_m(1+m)exp(m*tau_input)(abs(B_input*p_m)+abs(kappa_m)) at the actual port.',
            'absolute_output_units':'sum_m(1+m)exp(m*tau_output)(abs(B_output*p_m)+abs(kappa_m)) at the actual port.',
            'cut_output_units':'The corresponding absolute output divided by this cell true_w_out_lower; only cell12 is the final original head cut.',
            'source_terms_not_in_this_homogeneous_packet':True,'uncovered_windows_keep_original_kernels':uncovered,'rows':rows})
    check('small_owned_RSS',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=a.rss_kib)
    result={'schema':'inner-true-three-cell-two-column-point-homogeneous-v1','author':'geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        'all_gates':True,'gate_count':g.count,'gates':{k:True for k in g.by_name},'gate_multiplicities':g.by_name,
        'source_sha256':sha(__file__),'input_identities':ids,'frozen_reference_source_sha256':SOURCE_PINS,
        'normalization_S':'257/256','input_mass_definition':'A single U+V mass, U=abs(B_next*p_m), V=abs(kappa_m). Prior strong radial-sup-then-Fourier-sum bounds imply this at the port.',
        'two_column_proof':'Q<=U/(B_next*m*r_in^3); abs(Xi/nu)<=r_in^4*w_in/(sqrt(12)*mu_current*nu)*(m*U/B_next+V). Propagate the two columns by the same positive A and sum the two output components via c_out. max(K_U,K_V) consumes U+V exactly once.',
        'no_extra_factor_two_or_frame_jump':'This is a single point readout. The output physical two-component sum is already in c_out, and B_next appears directly in the input columns. No independent per-component unit source is substituted.',
        'boundary_normalization_is_only_a_point_upper_not_a_wholecell_lower':True,
        'all_original_cell_sources_far_infinite_mean_inverse_still_required':True,
        'new_fixedpoint_or_truecut_consistency_claimed':False,'new_ODE_radial_quadrature_or_matrix_replay_Node_calls':0,
        'cells':cells,'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    data=(json.dumps(result,indent=2)+'\n').encode()
    if len(data)>=1000000:raise ValueError('Small point packet required')
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(data)
    print(json.dumps({'all_gates':True,'gate_count':g.count,'path':str(out),'sha256':sha(out),
        'first_mode':{str(c['cell']):{'Vprime_port':str(ab(c['nextcell_Vprime_boundary_upper'])),'absolute_column':str(ab(c['rows'][0]['input_absolute_mass_to_absolute_endpoint']))} for c in cells},
        'elapsed_seconds':result['elapsed_seconds'],'peak_rss_kib':result['peak_rss_kib']}),flush=True)


if __name__=='__main__':main()
