#!/usr/bin/env python3
"""Independent standard-library coarse-ramification and exact F3 audit on SS CM(-27)."""
import argparse,json
from pathlib import Path
from math import comb
from verify_CM11_F3_Laurent47 import P,Q,q,Z,sha,read,add,sub,neg,mul,scale,inv,eq,dot,sum_pairs,sconst,sadd,sscale,smul,sinv,spow,scompose,scalar,scalar_series,row_series,col_series,dotconv,checkseries,elliptic_j

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','branches','polynomial','reference-connections','v-anchor','f2-polynomial','f2-audit','output']:ap.add_argument('--'+k,type=Path,required=True)
 args=ap.parse_args();paths={k:getattr(args,k.replace('-','_')) for k in ['branches','polynomial','reference-connections','v-anchor','f2-polynomial','f2-audit']};br,pol,ref,anchor,f2,audit=[read(paths[k]) for k in paths]
 def edge(d,p):
  vv=[v for k,v in d['input_sha256'].items() if Path(k).name==Path(p).name];assert vv and set(vv)=={sha(p)},p
 for k in ['branches','reference-connections','v-anchor','f2-polynomial','f2-audit']:edge(pol,paths[k])
 edge(br,args.v_anchor);edge(audit,args.f2_polynomial);assert br['source_CM_anchor']==anchor
 folder=Path(__file__).resolve().parent
 for n,d in [('p41_CM27_T3_ramified_branches47.py',br),('p41_CM27_F3_ramified_polynomial47.py',pol)]:p=folder/n;assert sha(p)==d['source_sha256'];paths[n]=p
 paths['standard_library_series_helpers']=folder/'verify_CM11_F3_Laurent47.py'
 def standard(n):p=args.script_dir/'data'/n;paths[n]=p;return read(p)
 hecke=standard('p41_hecke47_full_saved.json.gz')['operators']['3'];globals=standard('p41_global_qc_polynomials47_complete.json.gz');coarse=standard('p41_elliptic_coarse_atlas47_verified.json.gz');nu=standard('p41_second_kind_connection47.json.gz');eta=standard('p41_eta_calibration47_complete.json.gz');global113=standard('p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz')
 J=br['source_projective_jets_0to4'];W=row_series(J['W']);V2=row_series(J['V2']);V3=row_series(J['V3']);H=scalar_series(J['Hc']);iH=scalar_series(J['inverse_Hc']);checkseries(smul(H,iH,Q,5),sconst(1),Q)
 A,Bcm=br['source_true_CM_physical_model'];assert A==1 and br['source_original_model']==[1,32];B=sadd(sconst(Bcm),scalar_series(br['source_physical_B_displacement_coefficients_0to4']),Q,5);j=scalar_series(br['source_true_CM_j_coefficients_0to4']);checkseries(elliptic_j(sconst(A),B,Q,5),j,Q);assert j[0]==(-12288000%Q,0)
 trace=[[Z]*73 for _ in range(4)];base=None;certs=[]
 source_row=br['source_original_row_0based'];target_row=hecke['necklace_transport_1based'][source_row]-1;assert source_row==312 and target_row==104
 for rec in br['branch_records']:
  bi=rec['branch_0based'];assert rec['original_actual_target_W']==[hecke['targets'][bi]['evaluation_matrix'][target_row]];assert rec['original_kernel_root_in_R2']==hecke['targets'][bi]['kernel_x']
  rr=scalar_series(rec['kernel_coefficients_0to4']);r2=spow(rr,2,Q,5);r3=spow(rr,3,Q,5);psi=sadd(sadd(sscale(spow(rr,4,Q,5),3,Q),sscale(r2,6,Q),Q,5),sscale(smul(B,rr,Q,5),12,Q),Q,5);psi[0]=sub(psi[0],(1,0),Q);checkseries(psi,[Z]*5,Q)
  At=sadd(sconst(-9),sscale(r2,-30,Q),Q,5);Bt=sadd(sadd(sscale(B,-27,Q),sscale(rr,-42,Q),Q,5),sscale(r3,-70,Q),Q,5);checkseries(At,scalar_series(rec['target_A_coefficients_0to4']),Q);checkseries(Bt,scalar_series(rec['target_B_coefficients_0to4']),Q)
  ji=elliptic_j(At,Bt,Q,5);checkseries(ji,scalar_series(rec['actual_image_j_coefficients_0to4']),Q);hh=scalar_series(rec['actual_image_parameter_coefficients_0to4']);jt=scalar_series(rec['target_local_j_coefficients_0to4']);checkseries(scompose(jt,hh,Q,5),ji,Q)
  parameter=scalar_series(rec['target_parameter_map_coefficients_0to4']);imageparam=scalar_series(rec['actual_image_parameter_map_coefficients_0to4']);checkseries(scompose(parameter,hh,Q,5),imageparam,Q)
  if rec['unit_target_parameter_type']=='B_over_A_to_three_halves':
   checkseries(spow(imageparam,2,Q,5),smul(spow(Bt,2,Q,5),sinv(spow(At,3,Q,5),Q,5),Q,5),Q)
   checkseries(sscale(sinv(sadd(sconst(4),sscale(spow(parameter,2,Q,5),27,Q),Q,5),Q,5),6912,Q),jt,Q);assert (parameter[1][0]**2+parameter[1][1]**2)%47
  fac=smul([scale(hh[k+1],k+1,Q) for k in range(4)],sinv(scalar_series(rec['actual_image_Hc_coefficients_0to4']),Q,4),Q,4);checkseries(fac,scalar_series(rec['actual_differential_pullback_coefficients_0to3']),Q)
  wi=row_series(rec['actual_image_W_coefficients_0to4'])
  for n in range(4):
   for c in range(73):trace[n][c]=add(trace[n][c],sum_pairs([mul(wi[k][c],fac[n-k],Q) for k in range(n+1)],Q),Q)
  if rec['ramified_degree3_to_b']:
   assert base is None;base=rec;assert all(eq(x,Z,Q) for x in hh[:3]) and (hh[3][0]**2+hh[3][1]**2)%47;assert At[0]==Z
   C=rec['coarse_elliptic_transport'];assert C['kind']=='CM3' and C['original_raw_common_47_valuation']==2
   r0=tuple(rec['original_kernel_root_in_R2']);r02=mul(r0,r0,Q);r03=mul(r02,r0,Q);a0=sub((-9%Q,0),scale(r02,30,Q),Q);b0=sub(sub((-864%Q,0),scale(r0,42,Q),Q),scale(r03,70,Q),Q);u0=mul(mul(mul(a0,a0,Q),a0,Q),inv(mul(b0,b0,Q),Q),Q);factor=mul(mul(a0,a0,Q),inv(b0,Q),Q)
   assert eq(u0,scalar(C['physical_coarse_u_at_original_target']),Q) and eq(factor,scalar(C['physical_raw_stack_factor_at_original_target']),Q)
   cb=next(c for c in coarse['elliptic_charts'] if c['kind']=='CM3');cw=row_series(cb['coarse_values']);up=[(1,0)]
   for _ in range(3):up.append(mul(up[-1],u0,Q))
   reconstructed=[mul(sum_pairs([mul(cw[k][c],up[k],Q) for k in range(4)],Q),factor,Q) for c in range(73)]
   assert all(eq(x,y,Q) for x,y in zip(reconstructed,rec['original_actual_target_W'][0]))
   bf=[x[0] for x in rec['frame']];cc=inv(dot(cw[0],bf,Q),Q);trueb=[mul(x,cc,Q) for x in cw[0]];assert all(eq(x,y,Q) for x,y in zip(trueb,rec['all73_actual_target_at_true_CM'][0]))
   uknown=scalar_series(cb['u_of_projective_coordinate']);jknown=sscale(smul(uknown,sinv(sadd(sscale(uknown,4,Q),sconst(27,4),Q,4),Q,4),Q,4),6912,Q);checkseries(jt[:4],jknown,Q)
   alpha=At[1:5];den=sadd(sscale(spow(At[:4],3,Q,4),4,Q),sscale(spow(Bt[:4],2,Q,4),27,Q),Q,4);lg=sadd(sscale(smul([scale(alpha[k+1],k+1,Q) for k in range(3)],sinv(alpha,Q,3),Q,3),3,Q),sscale(smul([scale(den[k+1],k+1,Q) for k in range(3)],sinv(den,Q,3),Q,3),-1,Q),Q,3);checkseries(lg,scalar_series(rec['log_of_j_target_over_x_cubed_derivative_coefficients_0to2']),Q)
  certs.append({'branch':bi,'all5_kernel_Velu_j_and_parameter_compositions':True,'pullback_factor_recomputed':True,'parameter_type':rec['unit_target_parameter_type']})
 assert base is not None
 T=hecke['weight2_operator']
 for n in range(4):
  source=[sum_pairs([mul(W[k][c],iH[n-k],Q) for k in range(n+1)],Q) for c in range(73)];expected=[dot(source,[T[i][c] for i in range(73)],Q) for c in range(73)]
  assert trace[n]==expected;assert all(eq(x,y,Q) for x,y in zip(expected,row_series(br['full73_pullback_trace_coefficients_0to3'])[n]))
 moving=pol['actual_moving_connection'];qq=col_series(moving['q_linear_coefficients_in_parameter_0to4_mod47four']);ss=col_series(moving['s_quadratic_coefficients_in_parameter_0to3_mod47cubed']);conn=ref['actual_connections']['v_minus_b'];q0=[x[0] for x in conn['denominator_linear_coefficients_mod47four']];s0=[x[0] for x in conn['numerator_quadratic_coefficients_mod47cubed']];assert qq[0]==q0;assert all(eq(x,y,q) for x,y in zip(ss[0],s0));checkseries(dotconv(W,qq,Q,5),[Z]*5,Q)
 vd=[dot(w,[x[0] for x in nu['denominator_linear_section']],Q) for w in W[:3]];idn=sinv(smul(smul(vd,vd,Q,3),H,Q,3),Q,3);nrows=[]
 for n in range(3):nrows.append([sum_pairs([mul(dot(V3[k],[nu['numerator_cubic_sections'][i][c] for i in range(325)],Q),idn[n-k],Q) for k in range(n+1)],Q) for c in range(54)])
 recordednu=[x[0] for x in pol['actual_CM_center_nu_coefficients_0to2_mod47four']];assert all(all(eq(x,y,Q) for x,y in zip(a,b)) for a,b in zip(nrows,recordednu));gc=row_series(moving['gradient_original_nu_coefficients_0to3_mod47cubed']);assert gc[0]==ref['actual_gradients_original_nu_mod47cubed']['v_minus_b'][0]
 for n in range(1,4):assert all(eq(x,scale(y,pow(n,-1,q),q),q) for x,y in zip(gc[n],nrows[n-1]))
 nonbase=[Z]*3
 for rec in pol['actual_three_nonbase_branch_data']:
  bb=next(x for x in br['branch_records'] if x['branch_0based']==rec['branch_0based']);num=smul(dotconv(row_series(bb['actual_image_V2_coefficients_0to4']),ss,q,4),scalar_series(bb['actual_differential_pullback_coefficients_0to3']),q,4);den=dotconv(row_series(bb['actual_image_W_coefficients_0to4']),qq,q,4);val=smul(num,sinv(den,q,4),q,4);checkseries(num,scalar_series(rec['numerator_coefficients_0to3_mod47cubed']),q);checkseries(den,scalar_series(rec['denominator_coefficients_0to3_mod47cubed']),q);checkseries(val,scalar_series(rec['pullback_coefficients_0to3_mod47cubed']),q);nonbase=sadd(nonbase,val[:3],q,3)
 BJ=base['target_local_jets_0to4'];bw=row_series(BJ['W']);bv=row_series(BJ['V2']);bih=scalar_series(BJ['inverse_Hc']);bnum=smul([dot(x,s0,q) for x in bv[:4]],bih,q,4);bden=[dot(x,q0,q) for x in bw];assert bden[0]==Z;bl=smul(bnum,sinv(bden[1:],q,4),q,4);checkseries(bl,scalar_series(pol['eta_v_at_base_Laurent_coefficients_minus1_to2']),q);assert bl[0]==(-1%q,0)
 bj=scalar_series(base['target_local_j_coefficients_0to4']);rb=mul(add(bl[1],mul(bj[2],inv(bj[1],q),q),q),inv(bj[1],q),q);assert eq(rb,scalar(pol['eta_v_at_base_regular_j_coefficient']),q)
 vnum=smul([dot(x,s0,q) for x in V2[:4]],iH,q,4);vden=[dot(x,q0,q) for x in W];assert vden[0]==Z;vl=smul(vnum,sinv(vden[1:],q,4),q,4);checkseries(vl,scalar_series(pol['fixed_eta_v_Laurent_coefficients_minus1_to2']),q);assert vl[0]==(1,0)
 ji=scalar_series(base['actual_image_j_coefficients_0to4']);lg=scalar_series(base['log_of_j_target_over_x_cubed_derivative_coefficients_0to2']);assert all(eq(x,Z,Q) for x in ji[:3]);jpi=[scale(ji[k+1],k+1,q) for k in range(3)];combined=[add(scale(add(neg(lg[k],q),mul(rb,jpi[k],q),q),18,q),scale(vl[k+1],54,q),q) for k in range(3)]
 pieces={'18_three_nonbase_T3_branches':sscale(nonbase,18,q),'18_ramified_base_branch_plus54_eta_v':combined}
 nd=dotconv(V2,ss,q,3);np=dotconv([[scale(x,k+1,q) for x in V2[k+1]] for k in range(3)],ss,q,3);hp=[scale(H[k+1],k+1,q) for k in range(3)];qp=dotconv([[scale(x,k+1,q) for x in W[k+1]] for k in range(3)],qq,q,3);qpp=dotconv([[scale(x,(k+2)*(k+1),q) for x in W[k+2]] for k in range(3)],qq,q,3);checkseries(smul(nd,iH,q,3),qp,q)
 partial=sadd(smul(np,iH,q,3),sscale(smul(smul(nd,hp,q,3),spow(iH,2,q,3),q,3),-1,q),q,3);reg=smul(sadd(partial,sscale(qpp,-pow(2,-1,q),q),q,3),sinv(qp,q,3),q,3);checkseries(reg,scalar_series(pol['actual_self_regular_x_coefficients_mod47cubed']),q);jp=[scale(j[k+1],k+1,q) for k in range(3)];jpp=[scale(j[k+2],(k+2)*(k+1),q) for k in range(3)];pieces['4_self_regular_j']=sadd(sscale(reg,4,q),sscale(smul(jpp,sinv(jp,q,3),q,3),-2,q),q,3)
 for name,weight in [('c11_minus_b',-18),('Z12_minus22b',-9),('Z0fix_minus8b',-9),('D_minus20b',32*pow(3,-1,q))]:
  f=ref['actual_connections'][name];s=[x[0] for x in f['numerator_quadratic_coefficients_mod47cubed']];d=[x[0] for x in f['denominator_linear_coefficients_mod47four']];val=smul(smul([dot(v,s,q) for v in V2[:3]],sinv([dot(w,d,q) for w in W[:3]],q,3),q,3),iH,q,3);pieces[name]=sscale(val,weight,q)
 s=[x[0] for x in eta['numerator_coefficients']];d=[x[0] for x in eta['denominator_coefficients']];pieces['minus_eta_B']=sscale(smul(smul([dot(v,s,q) for v in V3[:3]],sinv([dot(v,d,q) for v in V2[:3]],q,3),q,3),iH,q,3),-1,q);pieces['four_thirds_dlog_j']=sscale(smul(jp,sinv(j,q,3),q,3),4*pow(3,-1,q),q);jm=list(j);jm[0]=sub(jm[0],(1728,0),q);pieces['dlog_j_minus1728']=smul(jp,sinv(jm,q,3),q,3)
 for name,series in pieces.items():checkseries(series,scalar_series(pol['differential_pieces_coefficients_mod47cubed'][name]),q)
 diff=[sum_pairs([v[k] for v in pieces.values()],q) for k in range(3)];checkseries(diff,scalar_series(pol['local_differential_coefficients_0to2_in_x_mod47cubed']),q);assert all(v[1]==0 for v in diff)
 idx=globals['direction_indices'].index(3);D=globals['directions'][idx]['based_C'];coords=anchor['actual_C_v_cyclic_coordinates_mod47cubed'];gv=D['constant_mod47four']+sum(x*y for x,y in zip(D['linear_vector_mod47four'],coords));off=0
 for block in D['quadratic_blocks_mod47four']:
  d=len(block);gv+=sum(coords[off+i]*block[i][j]*coords[off+j] for i in range(d) for j in range(d));off+=d
 assert off==54;gv%=Q;labels=globals['component_order'];targets=[x['QC_defect_target_mod47four'][idx] for x in globals['component_vectors']];scaled=(gv-targets[labels.index(28)])%Q;assert scaled==pol['known_CM_anchor_scaled_by800_height'];lc=scaled*pow(800,-1,Q)%Q
 hw=[lc]+[x[0]*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(diff)];assert hw==pol['canonical_local_sigma_F3_height_coefficients_0to3_in_w_mod47four'];ycm=anchor['actual_original_y_mod47cubed'];assert ycm==75213;hy=[sum(comb(n,k)*hw[n]*pow(-ycm,n-k,Q) for n in range(k,4))%Q for k in range(4)];assert hy==pol['canonical_local_sigma_F3_height_coefficients_0to3_in_y_mod47four']
 center=next(x for x in global113['actual_113_rational_disk_global_polynomials'] if x['disk_id']=='SS_j9_11');gp=next(x for x in center['global_polynomials'] if x['n']==3)['coefficients_0to4_in_y_mod47four'];assert gp==pol['global_F3_coefficients_0to4_in_y_mod47four'];qc=[(gp[k]-800*(hy[k] if k<4 else 0))%Q for k in range(5)];assert qc==pol['actual_QC_F3_coefficients_0to4_in_y_mod47four'];assert all(c%P==0 for c in qc)
 checks=[];survive=[]
 for c in audit['simple_single_F2_root_candidates_to_available_precision']:
  y=c['y_mod47cubed'];assert sum(t*pow(y,k,Q) for k,t in enumerate(f2['actual_QC_F2_coefficients_0to4_in_y_mod47four']))%Q==0;assert c['derivative_mod47']%P;val=sum(t*pow(y,k,Q) for k,t in enumerate(qc))%Q;dd=[(val-t)%Q for t in targets]
  for label,difference in zip(labels,dd):
   if difference==0:survive.append({'y_mod47cubed':y,'bad_component_label':label})
  checks.append({'y_mod47cubed':y,'QC_F3_value':val,'differences_in_component_order':dd})
 assert survive==pol['remaining_F2_F3_candidate_and_component_pairs'];assert all(c['y_mod47cubed']==ycm for c in survive)
 out={'result':'R316','disk_id':'SS_j9_11','standard_library_only':True,'input_sha256':{str(p):sha(p) for p in paths.values()},'actual_branch_checks':certs,'all4x73_actual_Hecke_pullback_coefficients_independently_recomputed':True,'original_raw47square_branch_exact_physical_coarse_reconstruction_all73':True,'true_b_target_and_published_coarse_j_coefficients_checked':True,'degree3_ramification_and_j_over_x_cubed_unit_derivative_recomputed':True,'all54_nu_and_moving_gradient_coefficients_recomputed':True,'actual_base_residue':-1,'base_pullback_weighted_residue':-54,'fixed_v_weighted_residue':54,'all_nonbase_pieces_and_exact_pole_cancellation_recomputed':True,'base_regular_j_coefficient':list(rb),'local_differential':[v[0] for v in diff],'CM_global_value':gv,'CM_scaled_height':scaled,'CM_actual_height':lc,'height_in_w':hw,'height_in_original_y':hy,'global_polynomial':gp,'QC_polynomial':qc,'candidate_checks':checks,'remaining_same_component_pairs':survive,'extra_F2_root_excluded_for_all_four_components':True,'scope':'Independent exact arithmetic on saved genuine kernels, coarse branches, full73 values and actual RR coefficients. Does not rerun torsion generation or moving RR ranks. The CM height is a known reciprocity input.','source_sha256':sha(__file__)}
 args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('PASS CM27 ramified F3 independent audit',sha(args.output),checks)
if __name__=='__main__':main()
