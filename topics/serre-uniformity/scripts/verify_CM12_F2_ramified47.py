#!/usr/bin/env python3
"""Independent exact CM12 T2/coarse pole-cancellation and complete simple-root audit."""
import argparse,json
from pathlib import Path
from math import comb
from verify_CM11_F3_Laurent47 import P,Q,q,Z,sha,read,add,sub,neg,mul,scale,inv,eq,dot,sum_pairs,sconst,sadd,sscale,smul,sinv,spow,scompose,scalar,scalar_series,row_series,col_series,dotconv,checkseries,elliptic_j

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','branches','polynomial','reference-connections','basic-anchors','output']:ap.add_argument('--'+k,type=Path,required=True)
 args=ap.parse_args();paths={k:getattr(args,k.replace('-','_')) for k in ['branches','polynomial','reference-connections','basic-anchors']};br,pol,ref,anchors=[read(paths[k]) for k in paths];anchor=next(x for x in anchors['records'] if x['label']=='P_minus12');assert br['source_CM_anchor']==anchor
 def edge(d,p):
  vv=[v for k,v in d['input_sha256'].items() if Path(k).name==Path(p).name];assert vv and set(vv)=={sha(p)},p
 for k in ['branches','reference-connections','basic-anchors']:edge(pol,paths[k])
 edge(br,args.basic_anchors);folder=Path(__file__).resolve().parent
 for n,d in [('p41_CM12_T2_ramified_branches47.py',br),('p41_CM12_F2_ramified_polynomial47.py',pol)]:p=folder/n;assert sha(p)==d['source_sha256'];paths[n]=p
 paths['standard_library_series_helpers']=folder/'verify_CM11_F3_Laurent47.py'
 def standard(n):p=args.script_dir/'data'/n;paths[n]=p;return read(p)
 hecke=standard('p41_hecke47_full_saved.json.gz')['operators']['2'];globals=standard('p41_global_qc_polynomials47_complete.json.gz');coarse=standard('p41_elliptic_coarse_atlas47_verified.json.gz');nu=standard('p41_second_kind_connection47.json.gz');eta=standard('p41_eta_calibration47_complete.json.gz');global113=standard('p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz');oldtargets=standard('p41_t2_cm_targets47_verified.json.gz')
 J=br['source_projective_jets_0to4'];W=row_series(J['W']);V2=row_series(J['V2']);V3=row_series(J['V3']);H=scalar_series(J['Hc']);iH=scalar_series(J['inverse_Hc']);checkseries(smul(H,iH,Q,5),sconst(1),Q)
 A,Bcm=br['source_true_CM_physical_model'];assert [A,Bcm]==[-15,22];B=sadd(sconst(Bcm),scalar_series(br['source_physical_B_displacement_coefficients_0to4']),Q,5);j=scalar_series(br['source_true_CM_j_coefficients_0to4']);checkseries(elliptic_j(sconst(A),B,Q,5),j,Q);assert j[0]==(54000%Q,0)
 trace=[[Z]*73 for _ in range(4)];base=None;certs=[]
 for rec in br['branch_records']:
  bi=rec['branch_0based'];rr=scalar_series(rec['kernel_coefficients_0to4']);psi=sadd(sadd(spow(rr,3,Q,5),sscale(rr,A,Q),Q,5),B,Q,5);checkseries(psi,[Z]*5,Q);v=sadd(sscale(spow(rr,2,Q,5),3,Q),sconst(A),Q,5);At=sadd(sconst(A),sscale(v,-5,Q),Q,5);Bt=sadd(B,sscale(smul(rr,v,Q,5),-7,Q),Q,5);checkseries(At,scalar_series(rec['target_A_coefficients_0to4']),Q);checkseries(Bt,scalar_series(rec['target_B_coefficients_0to4']),Q)
  ji=elliptic_j(At,Bt,Q,5);checkseries(ji,scalar_series(rec['actual_image_j_coefficients_0to4']),Q);hh=scalar_series(rec['actual_image_parameter_coefficients_0to4']);jt=scalar_series(rec['target_local_j_coefficients_0to4']);checkseries(scompose(jt,hh,Q,5),ji,Q);parameter=scalar_series(rec['target_parameter_map_coefficients_0to4']);imageparam=scalar_series(rec['actual_image_parameter_map_coefficients_0to4']);checkseries(scompose(parameter,hh,Q,5),imageparam,Q)
  if rec['unit_target_parameter_type']=='B_over_A_to_three_halves':
   checkseries(spow(imageparam,2,Q,5),smul(spow(Bt,2,Q,5),sinv(spow(At,3,Q,5),Q,5),Q,5),Q);checkseries(sscale(sinv(sadd(sconst(4),sscale(spow(parameter,2,Q,5),27,Q),Q,5),Q,5),6912,Q),jt,Q);assert (parameter[1][0]**2+parameter[1][1]**2)%47
  fac=smul([scale(hh[k+1],k+1,Q) for k in range(4)],sinv(scalar_series(rec['actual_image_Hc_coefficients_0to4']),Q,4),Q,4);checkseries(fac,scalar_series(rec['actual_differential_pullback_coefficients_0to3']),Q);wi=row_series(rec['actual_image_W_coefficients_0to4'])
  for n in range(4):
   for c in range(73):trace[n][c]=add(trace[n][c],sum_pairs([mul(wi[k][c],fac[n-k],Q) for k in range(n+1)],Q),Q)
  if rec['ramified_degree3_to_b']:
   assert base is None;base=rec;assert rr[0]==(2,0) and At[0]==Z and Bt[0]==(64,0);assert all(eq(x,Z,Q) for x in hh[:3]) and (hh[3][0]**2+hh[3][1]**2)%47
   cb=next(c for c in coarse['elliptic_charts'] if c['kind']=='CM3');cw=row_series(cb['coarse_values']);bf=[x[0] for x in rec['frame']];cc=inv(dot(cw[0],bf,Q),Q);trueb=[mul(x,cc,Q) for x in cw[0]];assert all(eq(x,y,Q) for x,y in zip(trueb,rec['all73_actual_target_at_true_CM'][0]))
   uknown=scalar_series(cb['u_of_projective_coordinate']);jknown=sscale(smul(uknown,sinv(sadd(sscale(uknown,4,Q),sconst(27,4),Q,4),Q,4),Q,4),6912,Q);checkseries(jt[:4],jknown,Q)
   dual=br['actual_ascending_dual_level_return'];assert dual['return_basis_matrix_mod41']==[[2,0],[0,21]];nx,ne=dual['target_pair_before_matrix'];assert [4*nx%41,16*ne%41]==dual['actual_return_pair']==[18,13];assert dual['target_necklace_label_before_matrix']==516 and dual['actual_return_necklace_label']==366
   alpha=At[1:5];den=sadd(sscale(spow(At[:4],3,Q,4),4,Q),sscale(spow(Bt[:4],2,Q,4),27,Q),Q,4);lg=sadd(sscale(smul([scale(alpha[k+1],k+1,Q) for k in range(3)],sinv(alpha,Q,3),Q,3),3,Q),sscale(smul([scale(den[k+1],k+1,Q) for k in range(3)],sinv(den,Q,3),Q,3),-1,Q),Q,3);checkseries(lg,scalar_series(rec['log_of_j_target_over_x_cubed_derivative_coefficients_0to2']),Q)
  else:
   ot=next(t for t in oldtargets['records'] if t['label']==rec['label']);assert At[0]==(ot['curve_A'],0) and Bt[0]==(ot['curve_B'],0);ow=ot['weight2_values'][0];scale0=inv(dot(ow,[x[0] for x in rec['frame']],Q),Q);assert all(eq(mul(x,scale0,Q),y,Q) for x,y in zip(ow,rec['all73_actual_target_at_true_CM'][0]))
  certs.append({'branch':bi,'all5_kernel_Velu_j_and_parameter_compositions':True,'pullback_factor_recomputed':True,'parameter_type':rec['unit_target_parameter_type']})
 assert base is not None;T=hecke['weight2_operator']
 for n in range(4):
  source=[sum_pairs([mul(W[k][c],iH[n-k],Q) for k in range(n+1)],Q) for c in range(73)];expected=[dot(source,[T[i][c] for i in range(73)],Q) for c in range(73)];assert trace[n]==expected;assert all(eq(x,y,Q) for x,y in zip(expected,row_series(br['full73_pullback_trace_coefficients_0to3'])[n]))
 moving=pol['actual_moving_connection'];qq=col_series(moving['q_linear_coefficients_in_parameter_0to4_mod47four']);ss=col_series(moving['s_quadratic_coefficients_in_parameter_0to3_mod47cubed']);conn=ref['actual_connections']['u_minus_b'];q0=[x[0] for x in conn['denominator_linear_coefficients_mod47four']];s0=[x[0] for x in conn['numerator_quadratic_coefficients_mod47cubed']];assert qq[0]==q0;assert all(eq(x,y,q) for x,y in zip(ss[0],s0));checkseries(dotconv(W,qq,Q,5),[Z]*5,Q)
 vd=[dot(w,[x[0] for x in nu['denominator_linear_section']],Q) for w in W[:3]];idn=sinv(smul(smul(vd,vd,Q,3),H,Q,3),Q,3);nrows=[]
 for n in range(3):nrows.append([sum_pairs([mul(dot(V3[k],[nu['numerator_cubic_sections'][i][c] for i in range(325)],Q),idn[n-k],Q) for k in range(n+1)],Q) for c in range(54)])
 recordednu=[x[0] for x in pol['actual_CM_center_nu_coefficients_0to2_mod47four']];assert all(all(eq(x,y,Q) for x,y in zip(a,b)) for a,b in zip(nrows,recordednu));gc=row_series(moving['gradient_original_nu_coefficients_0to3_mod47cubed']);assert gc[0]==ref['actual_gradients_original_nu_mod47cubed']['u_minus_b'][0]
 for n in range(1,4):assert all(eq(x,scale(y,pow(n,-1,q),q),q) for x,y in zip(gc[n],nrows[n-1]))
 nonbase=[Z]*3
 for rec in pol['actual_two_nonbase_branch_data']:
  bb=next(x for x in br['branch_records'] if x['branch_0based']==rec['branch_0based']);num=smul(dotconv(row_series(bb['actual_image_V2_coefficients_0to4']),ss,q,4),scalar_series(bb['actual_differential_pullback_coefficients_0to3']),q,4);den=dotconv(row_series(bb['actual_image_W_coefficients_0to4']),qq,q,4);val=smul(num,sinv(den,q,4),q,4);checkseries(num,scalar_series(rec['numerator_coefficients_0to3_mod47cubed']),q);checkseries(den,scalar_series(rec['denominator_coefficients_0to3_mod47cubed']),q);checkseries(val,scalar_series(rec['pullback_coefficients_0to3_mod47cubed']),q);nonbase=sadd(nonbase,val[:3],q,3)
 BJ=base['target_local_jets_0to4'];bw=row_series(BJ['W']);bv=row_series(BJ['V2']);bih=scalar_series(BJ['inverse_Hc']);bnum=smul([dot(x,s0,q) for x in bv[:4]],bih,q,4);bden=[dot(x,q0,q) for x in bw];assert bden[0]==Z;bl=smul(bnum,sinv(bden[1:],q,4),q,4);checkseries(bl,scalar_series(pol['eta_u_at_base_Laurent_coefficients_minus1_to2']),q);assert bl[0]==(-1%q,0)
 bj=scalar_series(base['target_local_j_coefficients_0to4']);rb=mul(add(bl[1],mul(bj[2],inv(bj[1],q),q),q),inv(bj[1],q),q);assert eq(rb,scalar(pol['eta_u_at_base_regular_j_coefficient']),q)
 vnum=smul([dot(x,s0,q) for x in V2[:4]],iH,q,4);vden=[dot(x,q0,q) for x in W];assert vden[0]==Z;vl=smul(vnum,sinv(vden[1:],q,4),q,4);checkseries(vl,scalar_series(pol['fixed_eta_u_Laurent_coefficients_minus1_to2']),q);assert vl[0]==(1,0)
 ji=scalar_series(base['actual_image_j_coefficients_0to4']);lg=scalar_series(base['log_of_j_target_over_x_cubed_derivative_coefficients_0to2']);assert all(eq(x,Z,Q) for x in ji[:3]);jpi=[scale(ji[k+1],k+1,q) for k in range(3)];combined=[add(scale(add(neg(lg[k],q),mul(rb,jpi[k],q),q),54,q),scale(vl[k+1],162,q),q) for k in range(3)]
 pieces={'54_two_nonbase_T2_branches':sscale(nonbase,54,q),'54_ramified_base_branch_plus162_eta_u':combined}
 nd=dotconv(V2,ss,q,3);np=dotconv([[scale(x,k+1,q) for x in V2[k+1]] for k in range(3)],ss,q,3);hp=[scale(H[k+1],k+1,q) for k in range(3)];qp=dotconv([[scale(x,k+1,q) for x in W[k+1]] for k in range(3)],qq,q,3);qpp=dotconv([[scale(x,(k+2)*(k+1),q) for x in W[k+2]] for k in range(3)],qq,q,3);checkseries(smul(nd,iH,q,3),qp,q)
 partial=sadd(smul(np,iH,q,3),sscale(smul(smul(nd,hp,q,3),spow(iH,2,q,3),q,3),-1,q),q,3);reg=smul(sadd(partial,sscale(qpp,-pow(2,-1,q),q),q,3),sinv(qp,q,3),q,3);checkseries(reg,scalar_series(pol['actual_self_regular_x_coefficients_mod47cubed']),q);jp=[scale(j[k+1],k+1,q) for k in range(3)];jpp=[scale(j[k+2],(k+2)*(k+1),q) for k in range(3)];pieces['8_self_regular_j']=sadd(sscale(reg,8,q),sscale(smul(jpp,sinv(jp,q,3),q,3),-4,q),q,3)
 for name,weight in [('Z8_minus20b',-27),('c7_minus_b',-54),('D_minus20b',64*pow(3,-1,q))]:
  f=ref['actual_connections'][name];s=[x[0] for x in f['numerator_quadratic_coefficients_mod47cubed']];d=[x[0] for x in f['denominator_linear_coefficients_mod47four']];val=smul(smul([dot(v,s,q) for v in V2[:3]],sinv([dot(w,d,q) for w in W[:3]],q,3),q,3),iH,q,3);pieces[name]=sscale(val,weight,q)
 s=[x[0] for x in eta['numerator_coefficients']];d=[x[0] for x in eta['denominator_coefficients']];pieces['minus_two_eta_B']=sscale(smul(smul([dot(v,s,q) for v in V3[:3]],sinv([dot(v,d,q) for v in V2[:3]],q,3),q,3),iH,q,3),-2,q);pieces['eight_thirds_dlog_j']=sscale(smul(jp,sinv(j,q,3),q,3),8*pow(3,-1,q),q);jm=list(j);jm[0]=sub(jm[0],(1728,0),q);pieces['two_dlog_j_minus1728']=sscale(smul(jp,sinv(jm,q,3),q,3),2,q)
 for name,series in pieces.items():checkseries(series,scalar_series(pol['differential_pieces_coefficients_mod47cubed'][name]),q)
 diff=[sum_pairs([v[k] for v in pieces.values()],q) for k in range(3)];checkseries(diff,scalar_series(pol['local_differential_coefficients_0to2_in_x_mod47cubed']),q);assert all(v[1]==0 for v in diff)
 idx=globals['direction_indices'].index(2);D=globals['directions'][idx]['based_C'];coords=anchor['actual_C_cyclic_coordinates_mod47cubed'];gv=D['constant_mod47four']+sum(x*y for x,y in zip(D['linear_vector_mod47four'],coords));off=0
 for block in D['quadratic_blocks_mod47four']:
  d=len(block);gv+=sum(coords[off+i]*block[i][j]*coords[off+j] for i in range(d) for j in range(d));off+=d
 assert off==54;gv%=Q;labels=globals['component_order'];targets=[x['QC_defect_target_mod47four'][idx] for x in globals['component_vectors']];scaled=(gv-targets[labels.index(3)])%Q;assert scaled==pol['known_CM_anchor_scaled_by800_height'];lc=scaled*pow(800,-1,Q)%Q
 hw=[lc]+[x[0]*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(diff)];assert hw==pol['canonical_local_sigma_F2_height_coefficients_0to3_in_w_mod47four'];ycm=anchor['actual_original_y_mod47cubed'];assert ycm==96923;hy=[sum(comb(n,k)*hw[n]*pow(-ycm,n-k,Q) for n in range(k,4))%Q for k in range(4)];assert hy==pol['canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four']
 center=next(x for x in global113['actual_113_rational_disk_global_polynomials'] if x['disk_id']=='SS_j44_02');gp=next(x for x in center['global_polynomials'] if x['n']==2)['coefficients_0to4_in_y_mod47four'];assert gp==pol['global_F2_coefficients_0to4_in_y_mod47four'];qc=[(gp[k]-800*(hy[k] if k<4 else 0))%Q for k in range(5)];assert qc==pol['actual_QC_F2_coefficients_0to4_in_y_mod47four'];assert all(c%P==0 for c in qc)
 def value(c,y,mod):return sum(a*pow(y,k,mod) for k,a in enumerate(c))%mod
 rootchecks=[];remaining=[]
 for label,target,record in zip(labels,targets,pol['componentwise_full_precision_F2_roots']):
  cc=list(qc);cc[0]=(cc[0]-target)%Q;assert all(c%P==0 for c in cc);cc=[c//P for c in cc];roots=[i for i in range(P) if value(cc,i,P)==0];derivative=[(i+1)*cc[i+1] for i in range(4)];lifted=[]
  for root in roots:
   assert value(derivative,root,P);y=root
   for step in [1,2]:
    choices=[y+d*P**step for d in range(P) if value(cc,y+d*P**step,P**(step+1))==0];assert len(choices)==1;y=choices[0]
   lifted.append(y);remaining.append({'y_mod47cubed':y,'bad_component_label':label})
  assert lifted==[x['y_mod47cubed'] for x in record['simple_roots_lifted_mod47cubed']];rootchecks.append({'component':label,'residual_roots':roots,'actual_simple_roots_mod47cubed':lifted,'derivative_mod47':[value(derivative,y,P) for y in lifted]})
 assert remaining==pol['remaining_F2_candidate_and_component_pairs'];assert {'y_mod47cubed':96923,'bad_component_label':3} in remaining
 out={'result':'R321','disk_id':'SS_j44_02','standard_library_only':True,'input_sha256':{str(p):sha(p) for p in paths.values()},'actual_branch_checks':certs,'all4x73_actual_Hecke_pullback_coefficients_independently_recomputed':True,'both_old_CM48_all73_targets_and_actual_dual_necklace_return_verified':True,'true_b_target_and_published_coarse_j_coefficients_checked':True,'degree3_ramification_and_j_over_x_cubed_unit_derivative_recomputed':True,'all54_nu_and_moving_gradient_coefficients_recomputed':True,'actual_base_residue':-1,'base_pullback_weighted_residue':-162,'fixed_u_weighted_residue':162,'all_nonbase_pieces_and_exact_pole_cancellation_recomputed':True,'base_regular_j_coefficient':list(rb),'local_differential':[v[0] for v in diff],'CM_global_value':gv,'CM_scaled_height':scaled,'CM_actual_height':lc,'height_in_w':hw,'height_in_original_y':hy,'global_polynomial':gp,'QC_polynomial':qc,'componentwise_independent_digit_lift_root_checks':rootchecks,'remaining_F2_candidate_and_component_pairs':remaining,'scope':'Independent exact arithmetic on genuine kernels, old actual targets, coarse branch and RR coefficients; roots lifted one base47 digit at a time, without rerunning torsion or RR.','source_sha256':sha(__file__)}
 args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('PASS independent CM12 F2 ramification and fullroots',sha(args.output),rootchecks)
if __name__=='__main__':main()
