#!/usr/bin/env python3
"""Independent standard-library audit of actual CM(-7) branch jets and merged Laurent height."""
import argparse,gzip,hashlib,json
from pathlib import Path
from math import comb
P,Q,q=47,47**4,47**3
Z=(0,0)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def add(a,b,m):return ((a[0]+b[0])%m,(a[1]+b[1])%m)
def neg(a,m):return (-a[0]%m,-a[1]%m)
def sub(a,b,m):return add(a,neg(b,m),m)
def mul(a,b,m):return ((a[0]*b[0]-a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
def scale(a,n,m):return (a[0]*n%m,a[1]*n%m)
def inv(a,m):
 u=pow((a[0]*a[0]+a[1]*a[1])%m,-1,m);return (a[0]*u%m,-a[1]*u%m)
def eq(a,b,m):return tuple(x%m for x in a)==tuple(x%m for x in b)
def dot(a,b,m):
 out=Z
 for x,y in zip(a,b):out=add(out,mul(x,y,m),m)
 return out
def sconst(n,L=5):return [(n%Q,0)]+[Z]*(L-1)
def sadd(a,b,m,L=None):
 L=L or max(len(a),len(b));return [add(a[i] if i<len(a) else Z,b[i] if i<len(b) else Z,m) for i in range(L)]
def sscale(a,c,m):return [scale(x,c,m) for x in a]
def smul(a,b,m,L):return [sum_pairs([mul(a[i],b[n-i],m) for i in range(n+1) if i<len(a) and n-i<len(b)],m) for n in range(L)]
def sum_pairs(xs,m):
 v=Z
 for x in xs:v=add(v,x,m)
 return v
def sinv(a,m,L):
 out=[inv(a[0],m)]
 for n in range(1,L):out.append(neg(mul(out[0],sum_pairs([mul(a[k],out[n-k],m) for k in range(1,min(n,len(a)-1)+1)],m),m),m))
 return out
def spow(a,e,m,L):
 out=[(1,0)]+[Z]*(L-1)
 for _ in range(e):out=smul(out,a,m,L)
 return out
def scompose(a,b,m,L):
 assert eq(b[0],Z,m);out=[Z]*L;power=[(1,0)]+[Z]*(L-1)
 for c in a:
  out=sadd(out,[mul(c,x,m) for x in power],m,L);power=smul(power,b,m,L)
 return out
def scalar(data):return tuple(data[0][0])
def scalar_series(data):return [scalar(x) for x in data]
def row_series(data):return [x[0] for x in data]
def col_series(data):return [[row[0] for row in x] for x in data]
def dotconv(rows,cols,m,L):return [sum_pairs([dot(rows[k],cols[n-k],m) for k in range(n+1) if k<len(rows) and n-k<len(cols)],m) for n in range(L)]
def checkseries(a,b,m):assert len(a)==len(b) and all(eq(x,y,m) for x,y in zip(a,b)),(a,b,m)
def elliptic_j(A,B,m,L):
 a3=spow(A,3,m,L);den=sadd(sscale(a3,4,m),sscale(spow(B,2,m,L),27,m),m,L)
 return sscale(smul(a3,sinv(den,m,L),m,L),6912,m)
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','branches','polynomial','reference-connections','cm-anchors','output']:ap.add_argument('--'+k,type=Path,required=True)
 args=ap.parse_args();paths={k:getattr(args,k.replace('-','_')) for k in ['branches','polynomial','reference-connections','cm-anchors']}
 br,pol,ref,anchors=[read(paths[k]) for k in paths]
 def edge(d,p):
  vv=[v for k,v in d['input_sha256'].items() if Path(k).name==Path(p).name];assert vv and set(vv)=={sha(p)},p
 for k in ['branches','reference-connections','cm-anchors']:edge(pol,paths[k])
 edge(br,args.cm_anchors)
 folder=Path(__file__).resolve().parent
 for name,data in [('p41_CM7_T2_local_branches47.py',br),('p41_CM7_F2_Laurent_polynomial47.py',pol)]:
  p=folder/name;assert sha(p)==data['source_sha256'];paths[name]=p
 def standard(name):
  p=args.script_dir/'data'/name;paths[name]=p;return read(p)
 hecke=standard('p41_hecke47_full_saved.json.gz')['operators']['2']
 globals=standard('p41_global_qc_polynomials47_complete.json.gz')
 original=standard('p41_second_kind_connection47.json.gz')
 eta=standard('p41_eta_calibration47_complete.json.gz')
 anchor=next(x for x in anchors['records'] if x['label']=='P_minus7')
 assert anchor==br['source_CM_anchor'];assert anchor['discriminant']==-7 and anchor['bad_component_at41']==28
 J=br['source_projective_jets_0to4'];W=row_series(J['W']);V2=row_series(J['V2']);V3=row_series(J['V3']);H=scalar_series(J['Hc']);iH=scalar_series(J['inverse_Hc'])
 checkseries(smul(H,iH,Q,5),sconst(1),Q)
 j=scalar_series(br['source_CM_j_coefficients_0to4']);AA,BB=-35,-98;B=sadd(sconst(BB),scalar_series(br['source_physical_B_displacement_coefficients_0to4_in_x']),Q,5)
 checkseries(elliptic_j(sconst(AA),B,Q,5),j,Q);assert j[0]==(anchor['j_integer']%Q,0)
 horizontal=[];trace=[[Z]*73 for _ in range(4)];branchchecks=[]
 for r in br['branch_records']:
  rr=scalar_series(r['kernel_root_coefficients_0to4_in_source_CM_x']);r2=spow(rr,2,Q,5);r3=spow(rr,3,Q,5)
  psi=sadd(sadd(r3,sscale(rr,AA,Q),Q,5),B,Q,5);checkseries(psi,[Z]*5,Q)
  At=sadd(sconst(-4*AA),sscale(r2,-15,Q),Q,5);Bt=sadd(sadd(sscale(B,-13,Q),sscale(rr,-21*AA,Q),Q,5),sscale(r3,-35,Q),Q,5)
  ji=elliptic_j(At,Bt,Q,5);checkseries(ji,scalar_series(r['image_j_coefficients_0to4_in_source_CM_x']),Q)
  hh=scalar_series(r['target_parameter_coefficients_0to4_in_source_CM_x']);jt=scalar_series(r['target_j_coefficients_0to4_in_its_chart']);checkseries(scompose(jt,hh,Q,5),ji,Q)
  ht=scalar_series(r['target_Hc_at_image_coefficients_0to4']);factor=smul([scale(hh[k+1],k+1,Q) for k in range(4)],sinv(ht,Q,4),Q,4);checkseries(factor,scalar_series(r['actual_differential_pullback_factor_coefficients_0to3']),Q)
  wi=row_series(r['actual_image_W_coefficients_0to4'])
  for n in range(4):
   for c in range(73):trace[n][c]=add(trace[n][c],sum_pairs([mul(wi[k][c],factor[n-k],Q) for k in range(n+1)],Q),Q)
  if r['horizontal_fixed_point']:
   assert wi[0]==W[0];assert r['all73_actual_target_coordinates_at_true_CM']==J['W'][0];horizontal.append(r)
  branchchecks.append({'branch':r['branch_0based'],'all5_kernel_equations_and_j_composition':True,'pullback_factor_recomputed':True})
 assert len(horizontal)==2
 hslopes=[scalar_series(r['target_parameter_coefficients_0to4_in_source_CM_x'])[1] for r in horizontal];assert mul(*hslopes,Q)==(1,0)
 fractions=[mul(h,inv(sub(h,(1,0),Q),Q),Q) for h in hslopes];assert add(*fractions,Q)==(1,0)
 T=hecke['weight2_operator'];K=hecke['canonical_operator']
 # Full73 trace is an independent standard-library matrix product, not the stored boolean.
 for n in range(4):
  source=[sum_pairs([mul(W[k][c],iH[n-k],Q) for k in range(n+1)],Q) for c in range(73)]
  expected=[dot(source,[T[i][j] for i in range(73)],Q) for j in range(73)]
  assert trace[n]==expected;assert all(eq(x,y,Q) for x,y in zip(expected,row_series(br['full73_T2_pullback_trace_coefficients_0to3'])[n]))
 moving=pol['actual_moving_connection'];qq=col_series(moving['q_linear_coefficients_in_parameter_0to4_mod47four']);ss=col_series(moving['s_quadratic_coefficients_in_parameter_0to3_mod47cubed'])
 c7=ref['actual_connections']['c7_minus_b'];q0=[x[0] for x in c7['denominator_linear_coefficients_mod47four']];s0=[x[0] for x in c7['numerator_quadratic_coefficients_mod47cubed']]
 assert qq[0]==q0;assert all(eq(x,y,q) for x,y in zip(ss[0],s0));checkseries(dotconv(W,qq,Q,5),[Z]*5,Q)
 snu=original['numerator_cubic_sections'];vn=[x[0] for x in original['denominator_linear_section']]
 vd=[dot(w,vn,Q) for w in W[:3]];nuden=smul(smul(vd,vd,Q,3),H,Q,3);idn=sinv(nuden,Q,3)
 nurows=[]
 for n in range(3):nurows.append([sum_pairs([mul(dot(V3[k],[snu[i][c] for i in range(325)],Q),idn[n-k],Q) for k in range(n+1)],Q) for c in range(54)])
 assert [[list(x) for x in row] for row in nurows]==[x[0] for x in pol['actual_CM_center_nu_coefficients_0to2_mod47four']]
 gc=row_series(moving['gradient_original_nu_coefficients_0to3_mod47cubed']);g0=ref['actual_gradients_original_nu_mod47cubed']['c7_minus_b'][0];assert gc[0]==g0
 for n in range(1,4):assert all(eq(x,scale(y,pow(n,-1,q),q),q) for x,y in zip(gc[n],nurows[n-1]))
 values=[];residue=Z
 for r,rec in zip(br['branch_records'],pol['actual_branch_Laurent_data']):
  assert r['branch_0based']==rec['branch_0based'];wi=row_series(r['actual_image_W_coefficients_0to4']);v2=row_series(r['actual_image_V2_coefficients_0to4']);factor=scalar_series(r['actual_differential_pullback_factor_coefficients_0to3'])
  num=smul(dotconv(v2,ss,q,4),factor,q,4);den=dotconv(wi,qq,q,5);checkseries(num,scalar_series(rec['numerator_coefficients_0to3_mod47cubed']),q);checkseries(den,scalar_series(rec['denominator_coefficients_0to4_mod47cubed']),q)
  if rec['horizontal']:
   assert den[0]==Z;val=smul(num,sinv(den[1:],q,4),q,4);hh=scalar_series(r['target_parameter_coefficients_0to4_in_source_CM_x'])[1];assert val[0]==mul(hh,inv(sub(hh,(1,0),q),q),q);residue=add(residue,val[0],q)
  else:val=smul(num,sinv(den,q,4),q,4)
  checkseries(val,scalar_series(rec['coefficients_mod47cubed']),q);values.append(val)
 cnum=smul([dot(v,s0,q) for v in V2[:4]],iH,q,4);cden=[dot(w,q0,q) for w in W];assert cden[0]==Z
 checkseries(cnum,scalar_series(pol['actual_fixed_eta_c7_numerator_coefficients_0to3_mod47cubed']),q);checkseries(cden,scalar_series(pol['actual_fixed_eta_c7_denominator_coefficients_0to4_mod47cubed']),q)
 cv=smul(cnum,sinv(cden[1:],q,4),q,4);checkseries(cv,scalar_series(pol['actual_fixed_eta_c7_Laurent_coefficients_minus1_to2_mod47cubed']),q);assert cv[0]==residue==(1,0)
 combined=[sub(sum_pairs([v[k+int(r['horizontal'])] for v,r in zip(values,pol['actual_branch_Laurent_data'])],q),cv[k+1],q) for k in range(3)]
 pieces={'54_T2_eta_C_minus_eta_c7':sscale(combined,54,q)}
 nd=dotconv(V2,ss,q,3);np=dotconv([[scale(x,k+1,q) for x in V2[k+1]] for k in range(3)],ss,q,3);hp=[scale(H[k+1],k+1,q) for k in range(3)]
 qp=dotconv([[scale(x,k+1,q) for x in W[k+1]] for k in range(3)],qq,q,3);qpp=dotconv([[scale(x,(k+2)*(k+1),q) for x in W[k+2]] for k in range(3)],qq,q,3)
 checkseries(smul(nd,iH,q,3),qp,q)
 partial=sadd(smul(np,iH,q,3),sscale(smul(smul(nd,hp,q,3),spow(iH,2,q,3),q,3),-1,q),q,3)
 regular=smul(sadd(partial,sscale(qpp,-pow(2,-1,q),q),q,3),sinv(qp,q,3),q,3);checkseries(regular,scalar_series(pol['actual_self_regular_x_coefficients_mod47cubed']),q)
 jp=[scale(j[k+1],k+1,q) for k in range(3)];jpp=[scale(j[k+2],(k+2)*(k+1),q) for k in range(3)]
 pieces['8_self_regular_j']=sadd(sscale(regular,8,q),sscale(smul(jpp,sinv(jp,q,3),q,3),-4,q),q,3)
 for name,weight in [('u_minus_b',162),('Z8_minus20b',-27),('D_minus20b',64*pow(3,-1,q))]:
  f=ref['actual_connections'][name];s=[x[0] for x in f['numerator_quadratic_coefficients_mod47cubed']];d=[x[0] for x in f['denominator_linear_coefficients_mod47four']]
  val=smul(smul([dot(v,s,q) for v in V2[:3]],sinv([dot(w,d,q) for w in W[:3]],q,3),q,3),iH,q,3);pieces[name]=sscale(val,weight,q)
 sB=[x[0] for x in eta['numerator_coefficients']];qB=[x[0] for x in eta['denominator_coefficients']]
 pieces['minus2_eta_B']=sscale(smul(smul([dot(v,sB,q) for v in V3[:3]],sinv([dot(v,qB,q) for v in V2[:3]],q,3),q,3),iH,q,3),-2,q)
 pieces['eight_thirds_dlog_j']=sscale(smul(jp,sinv(j,q,3),q,3),8*pow(3,-1,q),q);jm=list(j);jm[0]=sub(jm[0],(1728,0),q);pieces['two_dlog_j_minus1728']=sscale(smul(jp,sinv(jm,q,3),q,3),2,q)
 for name,series in pieces.items():checkseries(series,scalar_series(pol['differential_pieces_coefficients_mod47cubed'][name]),q)
 diff=[sum_pairs([p[k] for p in pieces.values()],q) for k in range(3)];assert all(x[1]==0 for x in diff);checkseries(diff,scalar_series(pol['local_differential_coefficients_0to2_in_x_mod47cubed']),q)
 idx=globals['direction_indices'].index(2);D=globals['directions'][idx]['based_C'];coords=anchor['actual_C_cyclic_coordinates_mod47cubed'];gv=D['constant_mod47four']+sum(x*y for x,y in zip(D['linear_vector_mod47four'],coords));off=0
 for block in D['quadratic_blocks_mod47four']:
  n=len(block);gv+=sum(coords[off+i]*block[i][j]*coords[off+j] for i in range(n) for j in range(n));off+=n
 assert off==54;gv%=Q;labels=globals['component_order'];targets=[x['QC_defect_target_mod47four'][idx] for x in globals['component_vectors']];assert labels==[0,3,28,32]
 scaled=(gv-targets[labels.index(anchor['bad_component_at41'])])%Q;assert scaled==next(x for x in anchor['all53_local_height_anchors_by_global_reciprocity'] if x['n']==2)['scaled_by800_local_height_mod47four']==pol['known_CM_anchor_scaled_by800_height'];lc=scaled*pow(800,-1,Q)%Q
 hw=[lc]+[x[0]*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(diff)];assert hw==pol['canonical_local_sigma_F2_height_coefficients_0to3_in_w_mod47four']
 ycm=anchor['actual_original_y_mod47cubed'];assert ycm==57595
 hy=[sum(comb(n,k)*hw[n]*pow(-ycm,n-k,Q) for n in range(k,4))%Q for k in range(4)];assert hy==pol['canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four']
 known=standard('p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz');record=next(x for x in known['actual_113_rational_disk_global_polynomials'] if x['disk_id']=='SS_j9_19');gp=next(x for x in record['global_polynomials'] if x['n']==2)['coefficients_0to4_in_y_mod47four'];assert gp==pol['global_F2_coefficients_0to4_in_y_mod47four'];qc=[(gp[k]-800*(hy[k] if k<4 else 0))%Q for k in range(5)];assert qc==pol['actual_QC_F2_coefficients_0to4_in_y_mod47four'];assert all(x%P==0 for x in qc)
 assert targets==[0,0,0,0]
 divided=[x//47 for x in qc];reduction=[x%47 for x in divided]
 roots=[t for t in range(47) if sum(c*pow(t,k,47) for k,c in enumerate(reduction))%47==0]
 lifts=[]
 for root in roots:
  derivative=sum(k*c*pow(root,k-1,47) for k,c in enumerate(divided) if k)%47;assert derivative
  y=root;mod=47;digits=[root]
  for _ in range(2):
   newmod=47*mod;v=sum(c*pow(y,k,newmod) for k,c in enumerate(divided))%newmod;assert v%mod==0
   digit=-(v//mod)*pow(derivative,-1,47)%47;y+=digit*mod;mod=newmod;digits.append(digit)
  assert sum(c*pow(y,k,Q) for k,c in enumerate(qc))%Q==0
  lifts.append({'y_mod47cubed':y,'z_mod47four':47*y,'y_base47_digits':digits,'derivative_mod47':derivative})
 assert lifts==pol['simple_single_F2_root_candidates_to_available_precision'] and ycm in [c['y_mod47cubed'] for c in lifts]
 atlas=standard('p41_rational_SS_residue_atlas47_complete.json.gz');ch=next(c for c in atlas['charts'] if 'SS_j9_19' in c['disk_ids']);row=ch['disk_ids'].index('SS_j9_19');zcm=47*ycm
 recovered=[[sum(ch['W_coefficients_0to3'][k][row][i][part]*pow(zcm,k,Q) for k in range(4))%Q for part in range(2)] for i in range(73)]
 assert recovered==W[0]==anchor['actual_W_in_original_SS_atlas_frame_mod47four']
 oldcm=standard('p41_cm7_q2_support47_verified.json.gz');oldw=oldcm['weight2_evaluation_coefficients'][0][0];frame=[x[0] for x in ch['frame']];den=dot(oldw,frame,Q)
 assert [list(mul(x,inv(den,Q),Q)) for x in oldw]==W[0]
 nonself=next(x for x in standard('p41_t2_cm_targets47_verified.json.gz')['records'] if x['label']=='CM28')['weight2_values'][0]
 rec=next(x for x in br['branch_records'] if not x['horizontal_fixed_point']);tframe=[x[0] for x in rec['frame']];den=dot(nonself,tframe,Q)
 assert [list(mul(x,inv(den,Q),Q)) for x in nonself]==rec['all73_actual_target_coordinates_at_true_CM'][0]
 out={'result':'R323','disk_id':'SS_j9_19','standard_library_only':True,'input_sha256':{str(p):sha(p) for p in paths.values()},'actual_branch_kernel_j_and_pullback_checks':branchchecks,'all4x73_actual_Hecke_trace_coefficients_independently_verified':True,'both_actual_horizontal_full73_CM_points_verified':True,'horizontal_slopes_mod47four':[list(x) for x in hslopes],'horizontal_Laurent_residues_mod47four':[list(x) for x in fractions],'residue_sum':list(residue),'all_branch_numerators_denominators_and_Laurent_divisions_recomputed':True,'all54_actual_nu_and_moving_gradient_coefficients_recomputed':True,'all_self_regular_fixed_and_j_dlog_pieces_recomputed':True,'no_nonunit_47_division':True,'local_differential_coefficients_mod47cubed':[x[0] for x in diff],'known_CM_global_value':gv,'known_CM_scaled_height':scaled,'known_CM_actual_height':lc,'height_in_w':hw,'height_in_original_y':hy,'global_polynomial':gp,'QC_polynomial':qc,'QC_div47_reduction':reduction,'residual_F2_roots':roots,'simple_single_F2_root_candidates_to_available_precision':lifts,'all73_original_SS_point_and_true_nonself_target_verified':True,'scope':'Independent exact arithmetic from saved genuine branch jets and actual RR coefficients; does not rerun original torsion calculation or RR rank construction. CM height is a reciprocity input.','source_sha256':sha(__file__)}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('PASS independent CM7 Laurent audit',sha(args.output),lifts)
if __name__=='__main__':main()
