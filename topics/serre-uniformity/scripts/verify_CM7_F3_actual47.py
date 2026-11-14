#!/usr/bin/env python3
"""Independent standard-library audit of four actual CM7 T3 branches and F3."""
import argparse
import json
from math import comb
from pathlib import Path
from verify_CM7_F2_Laurent47 import (
    P,Q,q,Z,sha,read,add,sub,mul,scale,inv,dot,sconst,sadd,sscale,smul,
    sum_pairs,sinv,spow,scompose,scalar_series,row_series,col_series,dotconv,
    checkseries,elliptic_j,eq,
)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ['script-dir','branches','f2-branches','f2-polynomial','f2-audit','polynomial','reference-connections','cm-anchors','output']:
        ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args();names=['branches','f2-branches','f2-polynomial','f2-audit','polynomial','reference-connections','cm-anchors']
    paths={k:getattr(args,k.replace('-','_')) for k in names}
    br,oldbr,f2,audit,pol,ref,anchors=[read(paths[k]) for k in names]
    def edge(d,p):
        vv=[v for k,v in d['input_sha256'].items() if Path(k).name==Path(p).name]
        assert vv and set(vv)=={sha(p)},p
    for k in names:
        if k!='polynomial':edge(pol,paths[k])
    edge(br,args.cm_anchors);edge(audit,args.f2_polynomial)
    folder=Path(__file__).resolve().parent
    for name,data in [('p41_CM7_T3_actual_branches47.py',br),('p41_CM7_F3_polynomial47.py',pol)]:
        path=folder/name;assert sha(path)==data['source_sha256'];paths[name]=path
    paths['standard_library_arithmetic']=folder/'verify_CM7_F2_Laurent47.py'
    def standard(name):
        path=args.script_dir/'data'/name;paths[name]=path;return read(path)
    assert br['disk_id']==pol['disk_id']==f2['disk_id']=='SS_j9_19'
    anchor=next(x for x in anchors['records'] if x['label']=='P_minus7')
    assert anchor==br['source_CM_anchor']==oldbr['source_CM_anchor']==pol['source_CM_anchor']
    assert br['source_projective_jets_0to4']==oldbr['source_projective_jets_0to4']
    J=br['source_projective_jets_0to4'];W=row_series(J['W']);V2=row_series(J['V2']);V3=row_series(J['V3'])
    H=scalar_series(J['Hc']);iH=scalar_series(J['inverse_Hc']);checkseries(smul(H,iH,Q,5),sconst(1),Q)
    j=scalar_series(br['source_true_CM_j_coefficients_0to4'])
    assert br['source_true_CM_j_coefficients_0to4']==oldbr['source_CM_j_coefficients_0to4']
    AA,BB=br['source_true_CM_physical_model'];assert AA==1
    B=sadd(sconst(BB),scalar_series(br['source_physical_B_displacement_coefficients_0to4']),Q,5)
    checkseries(elliptic_j(sconst(AA),B,Q,5),j,Q);assert j[0]==(anchor['j_integer']%Q,0)
    hecke=standard('p41_hecke47_full_saved.json.gz')['operators']['3']
    atlas=standard('p41_rational_SS_residue_atlas47_complete.json.gz')
    chart=next(c for c in atlas['charts'] if 'SS_j9_19' in c['disk_ids']);row=chart['disk_ids'].index('SS_j9_19')
    source_row=chart['original_input_rows_0based'][row];assert source_row==br['source_original_row_0based']
    target_row=hecke['necklace_transport_1based'][source_row]-1
    trace=[[Z]*73 for _ in range(4)];branch_checks=[]
    for rec in br['branch_records']:
        index=rec['branch_0based'];assert rec['original_target_source_row_0based']==target_row
        assert rec['original_actual_target_W']==[hecke['targets'][index]['evaluation_matrix'][target_row]]
        rr=scalar_series(rec['kernel_coefficients_0to4']);r2=spow(rr,2,Q,5);r3=spow(rr,3,Q,5)
        psi=sadd(sadd(sscale(spow(rr,4,Q,5),3,Q),sscale(r2,6*AA,Q),Q,5),sscale(smul(B,rr,Q,5),12,Q),Q,5)
        psi[0]=sub(psi[0],(AA*AA%Q,0),Q);checkseries(psi,[Z]*5,Q)
        At=sadd(sconst(-9*AA),sscale(r2,-30,Q),Q,5)
        Bt=sadd(sadd(sscale(B,-27,Q),sscale(rr,-42*AA,Q),Q,5),sscale(r3,-70,Q),Q,5)
        checkseries(At,scalar_series(rec['target_A_coefficients_0to4']),Q)
        checkseries(Bt,scalar_series(rec['target_B_coefficients_0to4']),Q)
        ji=elliptic_j(At,Bt,Q,5);checkseries(ji,scalar_series(rec['actual_image_j_coefficients_0to4']),Q)
        ht=scalar_series(rec['actual_image_parameter_coefficients_0to4']);assert ht[0]==Z and (ht[1][0]**2+ht[1][1]**2)%47
        jt=scalar_series(rec['target_local_j_coefficients_0to4']);checkseries(scompose(jt,ht,Q,5),ji,Q)
        ip=scalar_series(rec['actual_image_parameter_map_coefficients_0to4'])
        tp=scalar_series(rec['target_parameter_map_coefficients_0to4']);checkseries(scompose(tp,ht,Q,5),ip,Q)
        kind=rec['unit_target_parameter_type']
        if kind=='j':checkseries(ip,ji,Q);checkseries(tp,jt,Q)
        elif kind=='A_over_B_to_two_thirds':
            checkseries(smul(spow(ip,3,Q,5),spow(Bt,2,Q,5),Q,5),spow(At,3,Q,5),Q)
            t3=spow(tp,3,Q,5);jtp=sscale(smul(t3,sinv(sadd(sscale(t3,4,Q),sconst(27),Q,5),Q,5),Q,5),6912,Q)
            checkseries(jtp,jt,Q)
        else:
            assert kind=='B_over_A_to_three_halves'
            checkseries(smul(spow(ip,2,Q,5),spow(At,3,Q,5),Q,5),spow(Bt,2,Q,5),Q)
            jtp=sscale(sinv(sadd(sconst(4),sscale(spow(tp,2,Q,5),27,Q),Q,5),Q,5),6912,Q)
            checkseries(jtp,jt,Q)
        HH=scalar_series(rec['actual_image_Hc_coefficients_0to4'])
        factor=smul([scale(ht[k+1],k+1,Q) for k in range(4)],sinv(HH,Q,4),Q,4)
        checkseries(factor,scalar_series(rec['actual_differential_pullback_coefficients_0to3']),Q)
        wi=row_series(rec['actual_image_W_coefficients_0to4'])
        for n in range(4):
            for c in range(73):trace[n][c]=add(trace[n][c],sum_pairs([mul(wi[k][c],factor[n-k],Q) for k in range(n+1)],Q),Q)
        assert not rec['ramified_degree3_to_b']
        branch_checks.append({'branch':index,'actual_saved_level_row':target_row,'unit_parameter':kind,
            'all5_kernel_Velu_j_and_parameter_equations_verified':True,'actual_pullback_factor_recomputed':True})
    T=hecke['weight2_operator']
    for n in range(4):
        source=[sum_pairs([mul(W[k][c],iH[n-k],Q) for k in range(n+1)],Q) for c in range(73)]
        expected=[dot(source,[T[i][j] for i in range(73)],Q) for j in range(73)]
        assert trace[n]==expected
        assert all(eq(x,y,Q) for x,y in zip(expected,row_series(br['full73_pullback_trace_coefficients_0to3'])[n]))
    moving=f2['actual_moving_connection']
    qq=col_series(moving['q_linear_coefficients_in_parameter_0to4_mod47four'])
    ss=col_series(moving['s_quadratic_coefficients_in_parameter_0to3_mod47cubed'])
    t3=[Z]*3
    for rec,stored in zip(br['branch_records'],pol['actual_four_T3_branch_connection_pullbacks']):
        assert rec['branch_0based']==stored['branch_0based']
        wi=row_series(rec['actual_image_W_coefficients_0to4']);v2=row_series(rec['actual_image_V2_coefficients_0to4'])
        factor=scalar_series(rec['actual_differential_pullback_coefficients_0to3'])
        num=smul(dotconv(v2,ss,q,3),factor,q,3);den=dotconv(wi,qq,q,3);value=smul(num,sinv(den,q,3),q,3)
        checkseries(num,scalar_series(stored['numerator_coefficients_0to2_mod47cubed']),q)
        checkseries(den,scalar_series(stored['denominator_coefficients_0to2_mod47cubed']),q)
        checkseries(value,scalar_series(stored['pulled_connection_coefficients_0to2_mod47cubed']),q)
        t3=sadd(t3,value,q,3)
    regular=scalar_series(f2['actual_self_regular_x_coefficients_mod47cubed'])
    jp=[scale(j[k+1],k+1,q) for k in range(3)];jpp=[scale(j[k+2],(k+2)*(k+1),q) for k in range(3)]
    pieces={'18_T3_eta_C':sscale(t3,18,q),
        '4_self_regular_j':sadd(sscale(regular,4,q),sscale(smul(jpp,sinv(jp,q,3),q,3),-2,q),q,3)}
    for name,weight in [('v_minus_b',54),('c11_minus_b',-18),('Z12_minus22b',-9),('Z0fix_minus8b',-9),('D_minus20b',32*pow(3,-1,q))]:
        f=ref['actual_connections'][name];ns=[x[0] for x in f['numerator_quadratic_coefficients_mod47cubed']]
        ds=[x[0] for x in f['denominator_linear_coefficients_mod47four']]
        pieces[name]=sscale(smul(smul([dot(v,ns,q) for v in V2[:3]],sinv([dot(w,ds,q) for w in W[:3]],q,3),q,3),iH,q,3),weight,q)
    eta=standard('p41_eta_calibration47_complete.json.gz');sb=[x[0] for x in eta['numerator_coefficients']];db=[x[0] for x in eta['denominator_coefficients']]
    pieces['minus_eta_B']=sscale(smul(smul([dot(v,sb,q) for v in V3[:3]],sinv([dot(v,db,q) for v in V2[:3]],q,3),q,3),iH,q,3),-1,q)
    pieces['four_thirds_dlog_j']=sscale(smul(jp,sinv(j,q,3),q,3),4*pow(3,-1,q),q)
    jm=list(j);jm[0]=sub(jm[0],(1728,0),q);pieces['dlog_j_minus1728']=smul(jp,sinv(jm,q,3),q,3)
    for name,values in pieces.items():checkseries(values,scalar_series(pol['differential_pieces_coefficients_mod47cubed'][name]),q)
    diff=[sum_pairs([p[k] for p in pieces.values()],q) for k in range(3)];assert all(x[1]==0 for x in diff)
    checkseries(diff,scalar_series(pol['local_differential_coefficients_0to2_in_x_mod47cubed']),q)
    globals=standard('p41_global_qc_polynomials47_complete.json.gz');idx=globals['direction_indices'].index(3)
    D=globals['directions'][idx]['based_C'];coords=anchor['actual_C_cyclic_coordinates_mod47cubed']
    gv=D['constant_mod47four']+sum(x*y for x,y in zip(D['linear_vector_mod47four'],coords));off=0
    for block in D['quadratic_blocks_mod47four']:
        n=len(block);gv+=sum(coords[off+i]*block[i][j]*coords[off+j] for i in range(n) for j in range(n));off+=n
    assert off==54;gv%=Q;labels=globals['component_order'];targets=[x['QC_defect_target_mod47four'][idx] for x in globals['component_vectors']]
    a3=next(x for x in anchor['all53_local_height_anchors_by_global_reciprocity'] if x['n']==3)
    assert a3==pol['known_CM_anchor'] and gv==a3['global_value_mod47four']
    scaled=(gv-targets[labels.index(anchor['bad_component_at41'])])%Q;assert scaled==a3['scaled_by800_local_height_mod47four']
    lc=scaled*pow(800,-1,Q)%Q;assert lc==a3['canonical_local_sigma_height_mod47four']
    hw=[lc]+[x[0]*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(diff)]
    assert hw==pol['canonical_local_sigma_F3_height_coefficients_0to3_in_w_mod47four']
    ycm=anchor['actual_original_y_mod47cubed'];hy=[sum(comb(n,k)*hw[n]*pow(-ycm,n-k,Q) for n in range(k,4))%Q for k in range(4)]
    assert hy==pol['canonical_local_sigma_F3_height_coefficients_0to3_in_y_mod47four']
    known=standard('p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz');record=next(x for x in known['actual_113_rational_disk_global_polynomials'] if x['disk_id']=='SS_j9_19')
    gp=next(x for x in record['global_polynomials'] if x['n']==3)['coefficients_0to4_in_y_mod47four']
    assert gp==pol['global_F3_coefficients_0to4_in_y_mod47four'];qc=[(gp[k]-800*(hy[k] if k<4 else 0))%Q for k in range(5)]
    assert qc==pol['actual_QC_F3_coefficients_0to4_in_y_mod47four'] and all(x%47==0 for x in qc)
    checks=[];survivors=[]
    for candidate in audit['simple_single_F2_root_candidates_to_available_precision']:
        y=candidate['y_mod47cubed'];assert candidate['derivative_mod47']%47
        assert sum(c*pow(y,k,Q) for k,c in enumerate(f2['actual_QC_F2_coefficients_0to4_in_y_mod47four']))%Q==0
        value=sum(c*pow(y,k,Q) for k,c in enumerate(qc))%Q;differences=[(value-t)%Q for t in targets]
        for label,difference in zip(labels,differences):
            if difference==0:survivors.append({'y_mod47cubed':y,'bad_component_label':label})
        checks.append({'y_mod47cubed':y,'QC_F3_value_mod47four':value,'differences_in_component_order':differences})
    assert checks==pol['actual_F2_candidates_checked_at_full_available_precision']
    assert survivors==pol['remaining_F2_F3_candidate_and_component_pairs'] and all(x['y_mod47cubed']==ycm for x in survivors)
    out={'result':'R325','disk_id':'SS_j9_19','standard_library_only':True,
        'actual_four_branch_checks':branch_checks,'all4x73_actual_T3_pullback_coefficients_recomputed':True,
        'same_completed_R323_moving_connection_used':True,'all_actual_T3_connection_fractions_recomputed':True,
        'all_fixed_self_and_log_differential_pieces_recomputed':True,'local_derivative':[x[0] for x in diff],
        'CM_global_value_from_actual54_coordinates':gv,'CM_scaled_height':scaled,'CM_local_height':lc,
        'local_height_in_w':hw,'local_height_in_y':hy,'global_polynomial':gp,'QC_polynomial':qc,
        'F2_candidate_checks':checks,'remaining_same_component_pairs':survivors,
        'extra_F2_root_excluded_in_all_four_components':True,
        'scope':'Independent standard-library exact arithmetic and full saved level-row checks; completed R323 RR and CM reciprocity anchor are explicit inputs.',
        'input_sha256':{str(p):sha(p) for p in paths.values()},'source_sha256':sha(__file__)}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('PASS CM7 actual F3 independent audit',checks,'SHA',sha(args.output))

if __name__=='__main__':main()
