#!/usr/bin/env python3
"""Independent integer audit of the actual confluent basepoint connection and F2."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
from verify_CM7_F2_Laurent47 import (P,Q,q,Z,sha,read,add,sub,mul,scale,inv,eq,
    smul,spow,sinv,sadd,sscale,sum_pairs,scalar_series,row_series,col_series,
    dotconv,checkseries)


def dot(a,b,m):
    re=im=0
    for (ar,ai),(br,bi) in zip(a,b):
        re+=ar*br-ai*bi
        im+=ar*bi+ai*br
    return re%m,im%m


def matrow(v,A,m):
    return [dot(v,c,m) for c in zip(*A)]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ['script-dir','connection','polynomial','reference-connections','cm-anchors','output']:
        ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args()
    paths={k:getattr(args,k.replace('-','_')) for k in ['connection','polynomial','reference-connections','cm-anchors']}
    C,F,ref,anchors=[read(paths[k]) for k in paths]
    def edge(data,path):
        hs=[v for k,v in data['input_sha256'].items() if Path(k).name==Path(path).name]
        assert hs and set(hs)=={sha(path)},path
    edge(F,args.connection);edge(F,args.reference_connections);edge(F,args.cm_anchors);edge(C,args.cm_anchors)
    folder=Path(__file__).resolve().parent
    for name,data in [('p41_basepoint_confluent_connection47.py',C),('p41_basepoint_F2_polynomial47.py',F)]:
        path=folder/name;assert sha(path)==data['source_sha256'];paths[name]=path
    paths['arithmetic_helper']=folder/'verify_CM7_F2_Laurent47.py'
    def standard(name):
        path=args.script_dir/'data'/name;paths[name]=path;return read(path)
    model=standard('p41_makdisi47_certificate.json.gz')
    cusp=standard('p41_cusp_divisors47_certificate.json.gz')
    group=standard('p41_group47_checkpoint.json.gz')
    original=standard('p41_second_kind_connection47.json.gz')
    eta=standard('p41_eta_calibration47_complete.json.gz')
    hecke=standard('p41_hecke47_full_saved.json.gz')['operators']['2']
    globals=standard('p41_global_qc_polynomials47_complete.json.gz')
    anchor=next(x for x in anchors['records'] if x['label']=='P_minus3')
    assert C['actual_source_CM_anchor']==anchor and anchor['actual_original_y_mod47cubed']==0
    assert not any(anchor['actual_C_cyclic_coordinates_mod47cubed'])
    assert all(x['canonical_local_sigma_height_mod47four']==0 for x in anchor['all53_local_height_anchors_by_global_reciprocity'])
    J=C['actual_source_projective_jets_0to6']
    W=row_series(J['W']);V2=row_series(J['V2']);V3=row_series(J['V3'])
    H=scalar_series(J['Hc']);iH=scalar_series(J['inverse_Hc']);HV=row_series(J['H'])
    frame=[x[0] for x in C['source_frame']];coordinate=[x[0] for x in C['source_coordinate']]
    assert W[0]==anchor['actual_W_in_original_SS_atlas_frame_mod47four']
    assert all(eq(dot(w,frame,Q),(int(k==0),0),Q) for k,w in enumerate(W))
    checkseries(smul(H,iH,Q,7),[(1,0)]+[Z]*6,Q)
    cm3=standard('p41_cm3_makdisi47_certificate.json')['coarse_evaluation_coefficients'][0]
    fd=dot(cm3,frame,Q);assert [list(mul(x,inv(fd,Q),Q)) for x in cm3]==W[0]
    qq=col_series(C['q_linear_coefficients_in_parameter_0to5_mod47four'])
    shat=col_series(C['s_div_x_quadratic_coefficients_0to3_mod47cubed'])
    ss=col_series(C['s_quadratic_coefficients_0to4_mod47cubed'])
    assert all(eq(x,Z,q) for x in ss[0]) and ss[1:]==shat
    assert all(dot(W[0],v,Q)==Z for v in qq)
    checkseries(dotconv(W,qq,Q,6),[Z]*6,Q)
    assert dot(W[1],qq[0],Q)==Z and dot(W[2],qq[0],47)!=Z
    resP=dotconv(HV,qq,q,6);resb=[scale(dot(HV[0],v,q),-1,q) for v in qq]
    assert resP[0]==resb[0]==Z
    rd=[sub(x,y,q) for x,y in zip(resP,resb)]
    assert rd[0]==rd[1]==Z
    checkseries(resb[1:5],scalar_series(C['confluent_residue_at_b_div_x']),q)
    checkseries(rd[2:6],scalar_series(C['confluent_divided_difference_residue_rhs']),q)
    checkseries(dotconv(V2,ss,q,5),resP[:5],q)
    checkseries([dot(V2[0],v,q) for v in ss],resb[:5],q)
    checkseries(dotconv(V2[1:],shat,q,4),rd[2:6],q)
    double_num=smul([dot(v,shat[0],q) for v in V2[:2]],iH,q,2)
    double_den=[dot(v,qq[0],q) for v in W[2:4]]
    checkseries(smul(double_num,sinv(double_den,q,2),q,2),[(1,0),Z],q)
    print('PASS independent confluent residues, exact double pole and zero residue',flush=True)

    # Rebuild the evaluation basis using integer arithmetic only.
    MW=model['evaluation_matrix'];pairs2=[(i-1,j-1) for i,j in cusp['square_basis_monomials_1based']]
    C2=cusp['square_basis_inverse'];C2cols=list(zip(*C2))
    P2=[i-1 for i in cusp['square_pivot_rows_1based']]
    P3=[i-1 for i in group['cubic_pivot_rows_1based']]
    cpairs=[(i-1,j-1) for i,j in group['cubic_selected_pairs_1based']]
    E3=group['cubic_extra_inverse'];E3cols=list(zip(*E3))
    newrows=[i-1 for i in group['cubic_extra_rows_1based']]
    source_f=[dot(w,frame,Q) for w in MW]
    source_v2=[]
    for w in MW:
        products=[mul(w[i],w[j],Q) for i,j in pairs2]
        source_v2.append([dot(products,c,Q) for c in C2cols])
    assert all(all(eq(x,(int(i==j),0),Q) for j,x in enumerate(source_v2[row])) for i,row in enumerate(P2))
    invf=[inv(source_f[row],Q) for row in P2]
    lam=[mul(MW[P2[j]][i],invf[j],Q) for i,j in cpairs]
    CC=[[mul(mul(source_f[row],source_v2[row][j],Q),invf[j],Q) for j in range(199)] for row in newrows]
    CCcols=list(zip(*CC))
    def eval_v3(w,v2,m=q):
        f=dot(w,frame,m)
        raw=[mul(v2[j],sub(w[i],mul(f,lam[k],m),m),m) for k,(i,j) in enumerate(cpairs)]
        extra=[dot(raw,c,m) for c in E3cols]
        first=[sub(mul(mul(f,v2[j],m),invf[j],m),dot(extra,CCcols[j],m),m) for j in range(199)]
        return first+extra
    source_v3=[eval_v3(w,v) for w,v in zip(MW,source_v2)]
    assert all(all(eq(x,(int(i==j),0),q) for j,x in enumerate(source_v3[row])) for i,row in enumerate(P3))
    # All saved source section jets come from the original polynomial basis.
    for n in range(7):
        raw2=[sum_pairs([mul(W[k][i],W[n-k][j],Q) for k in range(n+1)],Q) for i,j in pairs2]
        assert all(eq(x,y,Q) for x,y in zip([dot(raw2,c,Q) for c in C2cols],V2[n]))
        raw3=[]
        for k,(i,j) in enumerate(cpairs):
            v=sum_pairs([mul(V2[h][j],W[n-h][i],Q) for h in range(n+1)],Q)
            raw3.append(sub(v,mul(V2[n][j],lam[k],Q),Q))
        extra=[dot(raw3,c,Q) for c in E3cols]
        computed=[sub(mul(V2[n][j],invf[j],Q),dot(extra,CCcols[j],Q),Q) for j in range(199)]+extra
        assert all(eq(x,y,Q) for x,y in zip(computed,V3[n]))
    print('PASS independent original V2/V3 model, all source and projective jets',flush=True)
    snu=original['numerator_cubic_sections'];vn=[x[0] for x in original['denominator_linear_section']]
    vd=[dot(w,vn,Q) for w in W[:4]];nd=smul(smul(vd,vd,Q,4),H,Q,4);indi=sinv(nd,Q,4)
    nurows=[]
    for n in range(4):
        nurows.append([sum_pairs([mul(dot(V3[k],[snu[i][c] for i in range(325)],Q),indi[n-k],Q) for k in range(n+1)],Q) for c in range(54)])
    assert all(all(eq(x,y,Q) for x,y in zip(v,z)) for v,z in zip(nurows,row_series(C['original_nu_coefficients_0to3_mod47four'])))
    ghat=row_series(C['gradient_div_x_original_nu_coefficients_0to3_mod47cubed'])
    for k in range(4):assert all(eq(x,scale(y,pow(k+1,-1,q),q),q) for x,y in zip(ghat[k],nurows[k]))
    bases=standard('p41_hecke3_abel_bases_checkpoint.json.gz');I2=[i-1 for i in bases['families'][1]['points_1based']]
    beta=-3*pow(27652,-1,q)%q
    for i,row in enumerate(I2):
        qvals=[dot(MW[row],x,q) for x in qq[:4]]
        rhs=smul(qvals,[v[i] for v in ghat],q,4)
        checkseries([scale(dot(source_v2[row],x,q),beta,q) for x in shat],rhs,q)
    print('PASS independent all54 original nu, integrated gradient and calibration',flush=True)

    # Independently reconstruct every faithful T2 evaluation identity.
    trace=F['actual_T2_trace'];pairs4=trace['V4_selected_W_V3_product_pairs_0based']
    tc=col_series(trace['actual_T2_eta_div_x_coefficients_0to2_in_V4_mod47cubed'])
    qT=[x[0] for x in trace['qT_linear_coefficients_mod47four']]
    UJ=trace['u_projective_jets_0to4'];UW=row_series(UJ['W'])
    assert all(dot(w,qT,Q)==Z for w in UW[:4]) and dot(UW[4],qT,47)!=Z and dot(W[0],qT,47)!=Z
    uanchor=next(x for x in anchors['records'] if x['label']=='P_minus12');assert UW[0]==uanchor['actual_W_in_original_SS_atlas_frame_mod47four']
    permutation=[i-1 for i in hecke['necklace_transport_1based']]
    # Contract each quadratic numerator into the original degree-two monomials.
    numerator_monomials=[[dot(row,s,q) for row in C2] for s in shat[:3]]
    totals=[[Z]*3 for _ in MW];goodmask=[True]*820;counts=[]
    for target in hecke['targets']:
        TW=target['evaluation_matrix'];values=[];hits=0
        for w in TW:
            qv=[dot(w,x,q) for x in qq[:3]]
            if qv[0][0]%47==0 and qv[0][1]%47==0:
                values.append(None);continue
            products=[mul(w[i],w[j],q) for i,j in pairs2]
            sv=[dot(products,c,q) for c in numerator_monomials]
            values.append(smul(sv,sinv(qv,q,3),q,3));hits+=1
        counts.append(hits)
        for row,p in enumerate(permutation):
            if values[p] is None:goodmask[row]=False;continue
            totals[row]=[add(x,y,q) for x,y in zip(totals[row],values[p])]
    good=[i for i,x in enumerate(goodmask) if x]
    assert good==trace['actual_T2_common_good_rows'] and counts==trace['actual_T2_branch_good_counts'] and len(good)>504
    for row in good:
        v4=[mul(MW[row][i],source_v3[row][j],q) for i,j in pairs4]
        qt=dot(MW[row],qT,q);qt3=mul(mul(qt,qt,q),qt,q)
        for k in range(3):
            assert dot(v4,tc[k],q)==mul(qt3,scale(totals[row][k],pow(2,-1,q),q),q),(row,k)
    V4P=[]
    for n in range(3):V4P.append([sum_pairs([mul(W[k][i],V3[n-k][j],q) for k in range(n+1)],q) for i,j in pairs4])
    tv=dotconv(V4P,tc,q,3);qtp=[dot(w,qT,q) for w in W[:3]]
    t2hat=smul(smul(tv,sinv(spow(qtp,3,q,3),q,3),q,3),iH,q,3)
    checkseries(t2hat,scalar_series(trace['actual_T2_eta_div_x_diagonal_coefficients_0to2']),q)
    print('PASS independent T2',len(good),'x3 faithful global V4 identities',flush=True)

    nd=dotconv(V2,ss,q,5)
    np=dotconv([[scale(x,k+1,q) for x in V2[k+1]] for k in range(4)],ss,q,4)
    hp=[scale(H[k+1],k+1,q) for k in range(4)]
    qp=dotconv([[scale(x,k+1,q) for x in W[k+1]] for k in range(5)],qq,q,5)
    qpp=dotconv([[scale(x,(k+2)*(k+1),q) for x in W[k+2]] for k in range(4)],qq,q,4)
    checkseries(smul(nd,iH,q,5),qp,q);assert qp[0]==Z
    partial=sadd(smul(np,iH,q,4),sscale(smul(smul(nd,hp,q,4),spow(iH,2,q,4),q,4),-1,q),q,4)
    reg=smul(sadd(partial,sscale(qpp,-pow(2,-1,q),q),q,4),sinv(qp[1:],q,4),q,4)
    checkseries(reg,scalar_series(F['actual_self_regular_Laurent_minus1_to2_mod47cubed']),q);assert reg[0]==(q-1,0)
    j=scalar_series(F['source_coarse_j_coefficients_0to4_mod47four']);assert j[0]==Z and j[1][0]%47
    jp=[scale(j[k+1],k+1,q) for k in range(4)];jpp=[scale(j[k+2],(k+2)*(k+1),q) for k in range(3)]
    ratio=smul(jpp,sinv(jp,q,3),q,3)
    pieces={'54_T2_eta_C':[Z,Z]+sscale(t2hat[:2],54,q),
      '8_self_regular_j':[scale(reg[0],8,q)]+[sub(scale(reg[k+1],8,q),scale(ratio[k],4,q),q) for k in range(3)]}
    for name,weight,residue in [('u_minus_b',162,-1),('c7_minus_b',-54,-1),('Z8_minus20b',-27,-20),('D_minus20b',64*pow(3,-1,q),-20)]:
        f=ref['actual_connections'][name];s=[x[0] for x in f['numerator_quadratic_coefficients_mod47cubed']];d=[x[0] for x in f['denominator_linear_coefficients_mod47four']]
        num=smul([dot(v,s,q) for v in V2[:4]],iH,q,4);den=[dot(w,d,q) for w in W[:5]];assert den[0]==Z
        vals=smul(num,sinv(den[1:],q,4),q,4);assert vals[0]==(residue%q,0)
        recorded=F['fixed_connection_Laurent_certificates'][name]
        checkseries(num,scalar_series(recorded['numerator_0to3']),q);checkseries(den,scalar_series(recorded['denominator_0to4']),q);checkseries(vals,scalar_series(recorded['Laurent_minus1_to2']),q)
        pieces[name]=sscale(vals,weight,q)
    sB=[x[0] for x in eta['numerator_coefficients']];qB=[x[0] for x in eta['denominator_coefficients']]
    B=smul(smul([dot(v,sB,q) for v in V3[:3]],sinv([dot(v,qB,q) for v in V2[:3]],q,3),q,3),iH,q,3)
    pieces['minus2_eta_B']=[Z]+sscale(B,-2,q)
    dlog=smul(jp,sinv(j[1:],q,4),q,4);assert dlog[0]==(1,0)
    pieces['eight_thirds_dlog_j']=sscale(dlog,8*pow(3,-1,q),q)
    jm=list(j);jm[0]=sub(jm[0],(1728,0),q)
    pieces['two_dlog_j_minus1728']=[Z]+sscale(smul(jp,sinv(jm,q,3),q,3),2,q)
    for name,values in pieces.items():checkseries(values,scalar_series(F['all_Laurent_pieces_minus1_to2_mod47cubed'][name]),q)
    total=[sum_pairs([v[k] for v in pieces.values()],q) for k in range(4)];assert total[0]==Z and all(x[1]==0 for x in total)
    diff=total[1:];checkseries(diff,scalar_series(F['local_differential_coefficients_0to2_in_x_mod47cubed']),q)
    height=[0]+[x[0]*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(diff)]
    assert height==F['canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four']
    known=standard('p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz')
    gd=next(x for x in known['actual_113_rational_disk_global_polynomials'] if x['disk_id']=='SS_j0_10')
    gp=next(x for x in gd['global_polynomials'] if x['n']==2)['coefficients_0to4_in_y_mod47four'];assert gp==F['global_F2_coefficients_0to4_in_y_mod47four']
    qc=[(gp[k]-800*(height[k] if k<4 else 0))%Q for k in range(5)];assert qc==F['actual_QC_F2_coefficients_0to4_in_y_mod47four']
    assert qc[0]==0 and all(x%47==0 for x in qc)
    red=[x//47%47 for x in qc];assert red==[0,44,0,0,0]
    assert F['lifted_root_records']==[{'y_mod47cubed':0,'z_mod47four':0,'y_base47_digits':[0,0,0],'derivative_mod47':44,'simple':True}]
    idx=globals['direction_indices'].index(2)
    assert globals['component_order']==[0,3,28,32] and [v['QC_defect_target_mod47four'][idx] for v in globals['component_vectors']]==[0,0,0,0]
    out={'result':'R328','disk_id':'SS_j0_10','standard_library_only':True,
      'independent_confluent_double_pole_and_residue_conditions':True,'all54_nu_and_calibration_recomputed':True,
      'original_V2_V3_polynomial_basis_and_source_jets_recomputed':True,
      'actual_T2_faithful_global_V4_identities_recomputed':3*len(good),
      'all_Laurent_pieces_recomputed_and_total_residue_zero':True,
      'local_differential_coefficients_mod47cubed':[x[0] for x in diff],
      'height_coefficients':height,'global_coefficients':gp,'QC_coefficients':qc,'QC_div47_reduction':red,
      'only_simple_root_y_mod47cubed':0,'derivative_mod47':44,
      'scope':'Recomputes actual integer algebra from published monomial bases and saved true confluent coefficients; core RR ranks and source j homogeneous-invariant construction remain separately checked in the generating core.',
      'input_sha256':{str(p):sha(p) for p in paths.values()},'source_sha256':sha(__file__)}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('PASS independent basepoint audit',sha(args.output),'only simple root y=0',flush=True)


if __name__=='__main__':main()
