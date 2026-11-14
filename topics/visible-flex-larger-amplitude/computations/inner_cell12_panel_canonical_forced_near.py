#!/usr/bin/env python3
"""Ordered canonical forced near columns from all original cell12 panels.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All 1873 original physical panels are consumed without subdivision, new
quadrature or ODE. The two modes share the same comparison matrix at 96.
Each generated source pays its complete current-panel positive suffix;
only source from earlier panels receives the whole next-panel strip loss.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx

from closure_split_joint_io_v2 import iter_array, metadata_without_array
from closure_positive_linear_band_enclosure import positive_peano
from inner_true_cell13_endpoint_window_kernels import (
    sha, read, exact, aq, ab, ball, pack, up, lower_pack, Gates,
    closed_port_w, MATERIALS)
from inner_cell12_canonical_forced_endpoint_kernels_v2 import PINS, SOURCE_PINS

BASE_SHA='5e03915b960e6ebdfa6847d155a82af5e54866e2bd0fde3e177815d7ea821133'
BASE_SOURCE='edaca1021dd6d0118ca50e71b5900f270e8c2987e8899fdedd2578bade0d43e6'
BASE_RESOURCE='d3cccd1b2087bbe2cdef501dff641063677000bbf4a8b80233f6f9823298e672'


def matvec(A,v):return [up(A[i][0]*v[0]+A[i][1]*v[1]) for i in range(2)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('inputs','base','base-resource','out-prefix'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--rss-kib',type=int,default=98304);a=p.parse_args()
    ctx.prec=256;ctx.threads=1;started=time.monotonic();g=Gates();check=g.check
    out=Path(str(a.out_prefix)+'.json')
    if out.exists():raise FileExistsError('Fresh ordered canonical certificate required')
    base,usage=read(a.base),read(a.base_resource)
    check('actual_complete_base_certificate',sha(a.base)==BASE_SHA and sha(a.base_resource)==BASE_RESOURCE and base['all_gates'] and all(base['gates'].values()) and usage['wait4_observed'] and usage['exitcode']==0 and usage['termination_signal'] is None)
    src=Path(__file__).parent
    check('frozen_complete_base_producer',sha(src/'inner_cell12_canonical_forced_endpoint_kernels_v2.py')==BASE_SOURCE)
    for name,wanted in SOURCE_PINS.items():check('all_original_comparison_sources',sha(src/name)==wanted)
    paths={k:a.inputs/v[0] for k,v in PINS.items()};ids={}
    for k,pth in paths.items():
        check('all_original_physical_inputs',sha(pth)==PINS[k][1]);ids[k]={'path':str(pth),'sha256':PINS[k][1]}
    meta=metadata_without_array(paths['panels'],'panels');ready=read(paths['ready'])
    mu_lo=ab(meta['mu'],'lower');mu_hi=ab(meta['mu']);sq12=arb(12).sqrt()
    # These bounds come from the original complete source and all original
    # panels. The matching r2 packet already paid both normalizations.
    scale2=ab(base['source_scale_squared_upper']);wlo=ab(base['true_w_out_lower'])
    tau_drop=ab(meta['tau_inner'],'lower')-ab(meta['tau_outer'])
    total_btau=ab(meta['btau_total']);B=ab(meta['B'])
    check('strict_original_denominators',mu_lo>0 and wlo>0 and total_btau>0 and tau_drop>0)
    upper_mode=96;nu_max=arb(upper_mode**2*(upper_mode**2-1))/12
    states={m:{z:[arb(0),arb(0)] for z in MATERIALS} for m in (94,96)}
    hom={m:[[arb(1),arb(0)],[arb(0),arb(1)]] for m in (94,96)}
    max_product=arb(0);max_witness=None;count=0;segment=0;end=F(0);counts=[0]*9
    sum_diagonal=arb(0);sum_strip_lower=arb(0);last=None
    for item in iter_array(paths['panels'],'panels'):
        j=item['segment'];left,right=F(*item['x_left']),F(*item['x_right'])
        if j==segment:check('original_panel_order',left==end)
        else:
            check('whole_original_segment_cover',j==segment+1 and end==1 and left==0);segment=j
        check('strict_original_panel',0<=left<right<=1);end=right;counts[j]+=1;count+=1;last=item
        rlo,rhi=ab(item['radius'],'lower'),ab(item['radius'])
        wlow,whigh=ab(item['w'],'lower'),ab(item['w'])
        V=ab(item['V']);J=ab(item['radial_log_increment']);TV=ab(item['log_w_variation'])
        check('complete_positive_panel_geometry',rlo>0 and rhi>=rlo and wlow>0 and whigh>=wlow and V>0 and J>0 and TV>=0)
        # Exact a dr = sqrt(12)*mu*r^-8 dr/w and
        # b0 dr = sqrt(12)/mu*r^6*w dr. dr=r*dlogr.
        Aoff=up(nu_max*sq12*mu_hi/(rlo**7*wlow)*J)
        Boff=up(sq12/mu_lo*rhi**7*whigh*J)
        product=up(Aoff*Boff);check('original_positive_Peano_domain',0<=product<1)
        if product>max_product:max_product=product;max_witness={'panel':count-1,'segment':j,'x_left':item['x_left'],'x_right':item['x_right']}
        P,_=positive_peano(Aoff,Boff)
        diagonal=up((upper_mode**2-4)*J);E=up(diagonal.exp());sum_diagonal=up(sum_diagonal+diagonal)
        A=[[up(E*z) for z in line] for line in P]
        check('every_panel_complete_cooperative_matrix',all(z>=0 for line in A for z in line) and A[0][0]>=1 and A[1][1]>=1)
        dtau=(tau_drop*ab(item['btau_integral'],'lower')/total_btau).lower()
        check('actual_panel_strip_loss_positive',dtau>=0);sum_strip_lower+=dtau
        rawpref=up(rhi**4*V**2/(sq12*mu_lo));common=ab(item['canonical_source_integral'])
        material={'d1':up(min(rawpref*J,common)),'d_lambda':up(min(rawpref*TV,common))}
        for m in (94,96):
            nu=arb(m*m*(m*m-1))/12;decay=up((-m*dtau).exp())
            check('actual_panel_strip_multiplier',0<decay<=1)
            for mat in MATERIALS:
                propagated=matvec(A,states[m][mat]);emission=[up(A[i][1]*material[mat]/nu) for i in range(2)]
                states[m][mat]=[up(decay*propagated[i]+emission[i]) for i in range(2)]
            H=hom[m]
            hom[m]=[[up(decay*(A[i][0]*H[0][k]+A[i][1]*H[1][k])) for k in range(2)] for i in range(2)]
        if count%256==0:
            check('small_owned_RSS',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=a.rss_kib)
            print(json.dumps({'event':'original_ordered_Peano_panel','count':count,'max_product':str(max_product),'elapsed_seconds':time.monotonic()-started}),flush=True)
    check('complete_original_1873_panels',count==1873 and segment==8 and end==1 and all(z>0 for z in counts))
    check('strip_loss_not_increased',sum_strip_lower<=tau_drop)
    rlo,rhi=ab(last['radius_right'],'lower'),ab(last['radius_right']);rows=[]
    for m in (94,96):
        nu=arb(m*m*(m*m-1))/12
        cout=[up((B*m+m*m)*rhi**3),up(sq12*mu_hi*nu/(rlo**4*wlo))]
        absolute={mat:up(2*(1+m)*scale2*sum((cout[i]*states[m][mat][i] for i in range(2)),arb(0))) for mat in MATERIALS}
        relative={mat:up(absolute[mat]/wlo) for mat in MATERIALS}
        old=next(row for row in base['rows'] if row['window']==[m,m])
        chosen={mat:min(relative[mat],ab(old['source_two_material_to_cut'][mat])) for mat in MATERIALS}
        rows.append({'window':[m,m],'comparison_matrix_upper_mode':upper_mode,
            'canonical_forced_endpoint_state_upper':{mat:list(map(pack,states[m][mat])) for mat in MATERIALS},
            'complete_weighted_homogeneous_matrix_upper':[[pack(z) for z in line] for line in hom[m]],
            'physical_output_covector_upper':list(map(pack,cout)),
            'source_two_material_to_absolute_endpoint':{mat:pack(absolute[mat]) for mat in MATERIALS},
            'source_two_material_to_cut':{mat:pack(relative[mat]) for mat in MATERIALS},
            'previous_full_cell_source_two_material_to_cut':old['source_two_material_to_cut'],
            'chosen_same_material_to_cut':{mat:pack(chosen[mat]) for mat in MATERIALS},
            'source_common_to_cut':pack(relative['d1']+relative['d_lambda'])})
    check('final_small_owned_RSS',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=a.rss_kib)
    result={'schema':'inner-cell12-ordered-physical-panel-canonical-forced-near-v1','author':'geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        'all_gates':True,'gate_count':g.count,'gates':{k:True for k in g.by_name},'gate_multiplicities':g.by_name,
        'source_sha256':sha(__file__),'input_identities':ids,'base_primary_sha256':BASE_SHA,'base_resource_sha256':BASE_RESOURCE,
        'frozen_reference_source_sha256':{**SOURCE_PINS,'inner_cell12_canonical_forced_endpoint_kernels_v2.py':BASE_SOURCE},
        'cell':12,'original_panels':count,'segment_panel_counts':counts,'upper_comparison_mode':upper_mode,
        'maximum_positive_Peano_product_upper':pack(max_product),'maximum_product_witness':max_witness,
        'sum_diagonal_exponents_upper':pack(sum_diagonal),'sum_actual_panel_strip_loss_lower':lower_pack(sum_strip_lower),
        'source_scale_squared_upper':base['source_scale_squared_upper'],'true_w_out_lower':base['true_w_out_lower'],
        'true_w_out_upper':base['true_w_out_upper'],'source_mu':meta['mu'],'physical_output_radius':last['radius_right'],
        'source_units':base['source_units'],'output_units':base['output_units'],
        'cooperative_coefficients':'Aoff=nu96*sqrt(12)*mu_hi*r_lo^-7*w_lo^-1*DeltaLogr; Boff=sqrt(12)*mu_lo^-1*r_hi^7*w_hi*DeltaLogr. d=(96^2-4)*DeltaLogr.',
        'original_tau_definition':'tau=inner-drop*btau_prefix/btau_total. Each actual drop>=drop*panel_btau.lower/cell_btau.upper.',
        'positive_source_recurrence':'Y_next<=exp(-m*DeltaTau_lower)*A_panel*Y_previous+A_panel*(0,I_mat/nu_m). The complete positive current-panel source has no free whole-panel strip damping.',
        'source_scale_and_strong_weight_paid_once':True,'factor_two_retained':True,
        'not_independent_single_mode_original_ODE_matrices':True,
        'old_higher_windows_far_infinite_mean_inverse_kept':True,'new_fixedpoint_or_truecut_consistency_claimed':False,
        'new_ODE_radial_quadrature_subdivision_source_evaluation_Node_calls':0,
        'rows':rows,'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    data=(json.dumps(result,indent=2)+'\n').encode()
    if len(data)>=1000000:raise ValueError('Small complete endpoint packet required')
    out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(data)
    print(json.dumps({'all_gates':True,'gate_count':result['gate_count'],'path':str(out),'sha256':sha(out),
        'source_columns':{str(row['window']):{k:str(ab(v)) for k,v in row['source_two_material_to_cut'].items()} for row in rows},
        'elapsed_seconds':result['elapsed_seconds'],'peak_rss_kib':result['peak_rss_kib']}),flush=True)


if __name__=='__main__':main()
