#!/usr/bin/env python3
"""Actual CM(-7) F3 height from four true branches and the completed R323 moving connection."""
import argparse
import gzip
import hashlib
import json
from math import comb
from pathlib import Path
import sys
import time

def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ['script-dir','branches','f2-branches','f2-polynomial','f2-audit','reference-connections','cm-anchors','work-dir','output']:
        ap.add_argument('--'+n,type=Path,required=True)
    args=ap.parse_args();s=args.script_dir.resolve();sys.path.insert(0,str(s));start=time.monotonic()
    import numpy as np
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel,save
    from p41_projective_jet_frames47 import install_exact_float_mm
    from p41_elliptic_coarse_atlas47 import Series
    install_exact_float_mm(r);a=ActualModel(s);Q,q=r.Q,47**3;inputs={}
    def load(p):inputs[str(p)]=sha(p);return read(p)
    def standard(n):return load(s/'data'/n)
    def red(x):return a.reduce(x,q)
    def scalar(n):return r.column([[n%q,0]])
    def mul(x,y,L=3):
        out=[]
        for n in range(L):
            z=r.zeros(*x[0][0].shape)
            for k in range(n+1):
                if k<len(x) and n-k<len(y):z=r.add(z,r.mul(x[k],y[n-k],q),q)
            out.append(z)
        return out
    def inverse(x,L=3):
        out=[r.inverse_values(x[0],q)]
        for n in range(1,L):
            v=r.zeros(*x[0][0].shape)
            for k in range(1,min(n,len(x)-1)+1):v=r.add(v,r.mul(x[k],out[n-k],q),q)
            out.append(r.neg(r.mul(out[0],v,q),q))
        return out
    def conv(x,y,L=3):
        out=[]
        for n in range(L):
            z=r.zeros(x[0][0].shape[0],y[0][0].shape[1])
            for k in range(n+1):
                if k<len(x) and n-k<len(y):z=r.add(z,r.mm(x[k],y[n-k],q),q)
            out.append(z)
        return out
    br=load(args.branches);oldbr=load(args.f2_branches);f2=load(args.f2_polynomial)
    audit=load(args.f2_audit);ref=load(args.reference_connections);anchors=load(args.cm_anchors)
    anchor=next(x for x in anchors['records'] if x['label']=='P_minus7')
    assert br['disk_id']==f2['disk_id']==audit['disk_id']=='SS_j9_19'
    assert br['source_CM_anchor']==oldbr['source_CM_anchor']==anchor
    assert br['source_projective_jets_0to4']==oldbr['source_projective_jets_0to4']
    assert br['source_true_CM_j_coefficients_0to4']==oldbr['source_CM_j_coefficients_0to4']
    assert br['no_actual_branch_lands_on_true_basepoint_b']
    assert br['all4x73_actual_Hecke_pullback_coefficients_verified'] and br['all4x54_canonical_Hecke_pullback_coefficients_verified']
    assert sha(args.f2_polynomial) in [v for k,v in audit['input_sha256'].items() if Path(k).name==args.f2_polynomial.name]
    J={k:[r.from_json(x) for x in vals] for k,vals in br['source_projective_jets_0to4'].items()}
    moving=f2['actual_moving_connection'];assert moving['all_four_coefficient_equations'] and moving['Frobenius']
    qq=[red(r.from_json(x)) for x in moving['q_linear_coefficients_in_parameter_0to4_mod47four']]
    ss=[r.from_json(x,q) for x in moving['s_quadratic_coefficients_in_parameter_0to3_mod47cubed']]
    t3=[r.zeros(1,1) for _ in range(3)];branches=[]
    for record in br['branch_records']:
        W=[red(r.from_json(x)) for x in record['actual_image_W_coefficients_0to4']]
        V2=[red(r.from_json(x)) for x in record['actual_image_V2_coefficients_0to4']]
        factor=[red(r.from_json(x)) for x in record['actual_differential_pullback_coefficients_0to3']]
        num=mul(conv(V2,ss),factor);den=conv(W,qq)
        assert np.all(r.units(den[0])),('actual T3 auxiliary denominator',record['branch_0based'])
        values=mul(num,inverse(den));t3=[r.add(x,y,q) for x,y in zip(t3,values)]
        branches.append({'branch_0based':record['branch_0based'],
            'numerator_coefficients_0to2_mod47cubed':[r.to_json(x) for x in num],
            'denominator_coefficients_0to2_mod47cubed':[r.to_json(x) for x in den],
            'pulled_connection_coefficients_0to2_mod47cubed':[r.to_json(x) for x in values]})
    regular=[r.from_json(x,q) for x in f2['actual_self_regular_x_coefficients_mod47cubed']]
    j=[red(r.from_json(x)) for x in br['source_true_CM_j_coefficients_0to4']]
    jp=[a.scale(j[k+1],k+1,q) for k in range(3)]
    jpp=[a.scale(j[k+2],(k+2)*(k+1),q) for k in range(3)]
    assert np.all(r.units(jp[0]))
    pieces={'18_T3_eta_C':[a.scale(x,18,q) for x in t3],
        '4_self_regular_j':[r.sub(a.scale(x,4,q),a.scale(y,2,q),q) for x,y in zip(regular,mul(jpp,inverse(jp)))]}
    ih=[red(x) for x in J['inverse_Hc'][:3]]
    for name,weight in [('v_minus_b',54),('c11_minus_b',-18),('Z12_minus22b',-9),('Z0fix_minus8b',-9),('D_minus20b',32*pow(3,-1,q))]:
        f=ref['actual_connections'][name]
        numerator=r.from_json(f['numerator_quadratic_coefficients_mod47cubed'],q)
        denominator=r.from_json(f['denominator_linear_coefficients_mod47four'],q)
        nv=[r.mm(red(x),numerator,q) for x in J['V2'][:3]]
        dv=[r.mm(red(x),denominator,q) for x in J['W'][:3]]
        assert np.all(r.units(dv[0])),('actual fixed F3 denominator',name)
        pieces[name]=[a.scale(x,weight,q) for x in mul(mul(nv,inverse(dv)),ih)]
    eta=standard('p41_eta_calibration47_complete.json.gz')
    sb=r.from_json(eta['numerator_coefficients'],q);qb=r.from_json(eta['denominator_coefficients'],q)
    nv=[r.mm(red(x),sb,q) for x in J['V3'][:3]];dv=[r.mm(red(x),qb,q) for x in J['V2'][:3]]
    assert np.all(r.units(dv[0]))
    pieces['minus_eta_B']=[r.neg(x,q) for x in mul(mul(nv,inverse(dv)),ih)]
    pieces['four_thirds_dlog_j']=[a.scale(x,4*pow(3,-1,q),q) for x in mul(jp,inverse(j[:3]))]
    jm=list(j[:3]);jm[0]=r.sub(jm[0],scalar(1728),q)
    pieces['dlog_j_minus1728']=mul(jp,inverse(jm))
    differential=[r.zeros(1,1) for _ in range(3)]
    for values in pieces.values():differential=[r.add(x,y,q) for x,y in zip(differential,values)]
    assert all(not np.any(x[1]) for x in differential)
    a3=next(x for x in anchor['all53_local_height_anchors_by_global_reciprocity'] if x['n']==3)
    constant=a3['canonical_local_sigma_height_mod47four'];ycm=anchor['actual_original_y_mod47cubed']
    assert ycm==57595 and 800*constant%Q==a3['scaled_by800_local_height_mod47four']
    hw=[constant]+[int(x[0][0,0])*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(differential)]
    hy=[sum(comb(n,k)*hw[n]*pow(-ycm,n-k,Q) for n in range(k,4))%Q for k in range(4)]
    known=standard('p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz')
    record=next(x for x in known['actual_113_rational_disk_global_polynomials'] if x['disk_id']=='SS_j9_19')
    gp=next(x for x in record['global_polynomials'] if x['n']==3)['coefficients_0to4_in_y_mod47four']
    assert sum(c*pow(ycm,k,Q) for k,c in enumerate(gp))%Q==a3['global_value_mod47four']
    qc=[(gp[k]-800*(hy[k] if k<4 else 0))%Q for k in range(5)];assert all(c%47==0 for c in qc)
    globals=standard('p41_global_qc_polynomials47_complete.json.gz');idx=globals['direction_indices'].index(3)
    labels=globals['component_order'];targets=[x['QC_defect_target_mod47four'][idx] for x in globals['component_vectors']]
    assert labels==[0,3,28,32] and targets[labels.index(anchor['bad_component_at41'])]==a3['same_component_QC_target_mod47four']
    checks=[];survivors=[]
    for candidate in audit['simple_single_F2_root_candidates_to_available_precision']:
        y=candidate['y_mod47cubed'];assert candidate['derivative_mod47']%47
        assert sum(c*pow(y,k,Q) for k,c in enumerate(f2['actual_QC_F2_coefficients_0to4_in_y_mod47four']))%Q==0
        value=sum(c*pow(y,k,Q) for k,c in enumerate(qc))%Q;diffs=[(value-t)%Q for t in targets]
        for label,d in zip(labels,diffs):
            if d==0:survivors.append({'y_mod47cubed':y,'bad_component_label':label})
        checks.append({'y_mod47cubed':y,'QC_F3_value_mod47four':value,'differences_in_component_order':diffs})
    out={'result':'R325','disk_id':'SS_j9_19','level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
        'source_CM_anchor':anchor,'same_exact_CM_source_jets_as_completed_R323':True,
        'completed_R323_moving_RR_certificate_reused_without_altering_any_coefficient':True,
        'actual_four_T3_branch_connection_pullbacks':branches,
        'all_actual_T3_and_fixed_F3_denominators_are_units':True,
        'differential_pieces_coefficients_mod47cubed':{k:[r.to_json(x) for x in v] for k,v in pieces.items()},
        'local_differential_coefficients_0to2_in_x_mod47cubed':[r.to_json(x) for x in differential],
        'known_CM_anchor':a3,'source_CM_original_y_mod47cubed':ycm,
        'canonical_local_sigma_F3_height_coefficients_0to3_in_w_mod47four':hw,
        'canonical_local_sigma_F3_height_coefficients_0to3_in_y_mod47four':hy,
        'global_F3_coefficients_0to4_in_y_mod47four':gp,'actual_QC_F3_coefficients_0to4_in_y_mod47four':qc,
        'bad_component_labels':labels,'F3_bad_targets_in_same_component_order':targets,
        'actual_F2_candidates_checked_at_full_available_precision':checks,
        'remaining_F2_F3_candidate_and_component_pairs':survivors,
        'extra_F2_root_excluded_in_all_four_components':all(v['y_mod47cubed']==ycm for v in survivors),
        'complete_actual_local_sigma_F3_polynomial_on_disk':True,'complete_common_roots':False,
        'tail_bound':'Actual T3 branch parameters and denominators are integral units. The completed R323 C family has the same unique nu primitive; height coefficient x^n has valuation at least -floor(log_47(n))-v47(n). All n>=4 vanish after x=47w modulo47^4; w=y-yCM is an exact integral translation.',
        'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),'runtime_seconds':round(time.monotonic()-start,3)}
    digest=save(args.output,out);print('PASS actual CM7 F3',hy,'SHA',digest,flush=True)
    print('PASS same-component actual candidates',checks,'remaining',survivors,flush=True)

if __name__=='__main__':main()
