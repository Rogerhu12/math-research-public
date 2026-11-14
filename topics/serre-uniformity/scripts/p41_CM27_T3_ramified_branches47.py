#!/usr/bin/env python3
"""Actual T3 branches at true CM(-27), including the degree-three coarse branch to b."""
import argparse,gzip,hashlib,json,sys,time
from pathlib import Path
from types import SimpleNamespace
from math import comb

def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','v-anchor','output']:ap.add_argument('--'+k,type=Path,required=True)
 args=ap.parse_args();scripts=args.script_dir.resolve();sys.path.insert(0,str(scripts));start=time.monotonic()
 import numpy as np
 import p41_r2_matrix as r
 from p41_actual_differentials47 import ActualModel,save
 from p41_projective_jet_frames47 import ProjectiveJetFrames,install_exact_float_mm
 from p41_elliptic_coarse_atlas47 import Series,ClassicalInvariants
 install_exact_float_mm(r);a=ActualModel(scripts);frames=ProjectiveJetFrames(a);Q=r.Q;N=5;S=Series(a,N);inputs={}
 def load(p):inputs[str(p)]=sha(p);return read(p)
 def standard(n):return load(scripts/'data'/n)
 anchor=load(args.v_anchor);assert anchor['disk_id']=='SS_j9_11' and anchor['discriminant']==-27
 atlas=standard('p41_rational_SS_residue_atlas47_complete.json.gz');chart=next(c for c in atlas['charts'] if anchor['disk_id'] in c['disk_ids']);row=chart['disk_ids'].index(anchor['disk_id']);source_row=chart['original_input_rows_0based'][row];assert source_row==312 and chart['reference_key']=='9'
 frame,coordinate=r.from_json(chart['frame']),r.from_json(chart['coordinate']);Wcm=r.from_json([anchor['actual_W_in_original_SS_atlas_frame_mod47four']]);assert r.equal(frame,a.fc)
 initial=r.rows(r.from_json(chart['W_coefficients_0to3'][0]),[row]);raw=r.rows(a.M['W'],[source_row]);assert r.equal(initial,r.mul(raw,r.inverse_values(r.mm(raw,frame))))
 Jsource=frames.local_jets(Wcm,frame,coordinate,order=4)
 derivative=standard('p41_cleared_serre_derivative47_complete.json.gz');inv=ClassicalInvariants(SimpleNamespace(a=a,r=r,v=r.from_json(derivative['chosen_clearing_section']),G=r.from_json(derivative['cleared_derivative_coefficients'])))
 hecke=standard('p41_hecke47_full_saved.json.gz')['operators']['3'];target_row=hecke['necklace_transport_1based'][source_row]-1
 coarse=standard('p41_elliptic_coarse_atlas47_verified.json.gz');cm3=next(c for c in coarse['elliptic_charts'] if c['kind']=='CM3');cm4=next(c for c in coarse['elliptic_charts'] if c['kind']=='CM4')
 braw=r.from_json(cm3['coarse_values'][0]);b=r.mul(braw,r.inverse_values(r.mm(braw,a.fc)))
 def const(c,n=N):
  first=r.column([c if isinstance(c,(list,tuple)) else [c%Q,0]]);return [first]+[r.zeros(1,1) for _ in range(n-1)]
 def centered(v):return [r.zeros(*v[0][0].shape)]+list(v[1:])
 def evaluate(v,t):
  out=r.zeros(*v[0][0].shape)
  for x in reversed(v):out=r.add(r.mul(out,t),x)
  return out
 def ellj(AA,BB):
  a3=S.power(AA,3);den=S.add(S.scale(a3,4),S.scale(S.power(BB,2),27));return S.scale(S.mul(a3,S.inverse(den)),6912)
 def jmap(J,etale=True):
  v=inv.series(J['W']);num=S.mul(S.power(v['Av'],3),S.power(v['v'],3));den=S.add(S.scale(num,4),S.scale(S.power(v['Bv3'],2),27));assert np.all(r.units(den[0]));out=S.scale(S.mul(num,S.inverse(den)),6912);assert not etale or np.all(r.units(out[1]));return out
 def dumpJ(J):return {k:[r.to_json(x) for x in J[k]] for k in ['W','V2','V3','Hc','inverse_Hc']}
 jsource=jmap(Jsource);assert r.equal(jsource[0],const(anchor['j_integer'])[0]);A=1;B0=32;jint=anchor['j_integer']%Q;Bcm=B0
 for _ in range(2):Bcm=(Bcm-(27*jint*Bcm*Bcm+4*(jint-1728))*pow(54*jint*Bcm,-1,Q))%Q
 assert (27*jint*Bcm*Bcm+4*(jint-1728))%Q==0
 pb=const(Bcm);pb[1]=const(1)[0];pj=ellj(const(A),pb);source_t=S.compose(S.reversion(centered(pj),N),centered(jsource));Bofx=S.add(const(Bcm),source_t);assert all(r.equal(x,y) for x,y in zip(ellj(const(A),Bofx),jsource))
 def sqrt_unit(value,initial=None):
  if initial is None:
   ar,ai=int(value[0][0,0])%47,int(value[1][0,0])%47
   candidates=[(x,y) for x in range(47) for y in range(47) if (x*x-y*y-ar)%47==0 and (2*x*y-ai)%47==0];assert candidates
   initial=r.column([list(candidates[0])])
  root=initial
  for _ in range(2):root=a.scale(r.add(root,r.mul(value,r.inverse_values(root))),pow(2,-1,Q))
  assert r.equal(r.mul(root,root),value);return root
 def sqrt_series(values,root):
  out=[root]+const(0)[1:]
  for _ in range(3):out=S.scale(S.add(out,S.mul(values,S.inverse(out))),pow(2,-1,Q))
  assert all(r.equal(x,y) for x,y in zip(S.power(out,2),values));return out
 def B_parameter(J,root):
  iv=inv.series(J['W']);Av=S.mul(iv['Av'],S.inverse(iv['v']));Bv=S.mul(iv['Bv3'],S.inverse(S.power(iv['v'],3)));rt=sqrt_series(Av,root);out=S.mul(Bv,S.inverse(S.power(rt,3)));assert np.all(r.units(out[1]));return out,rt
 elliptic_cache={}
 def actual_elliptic_chart(rawpoint,target_jcm,index,originalA,originalB):
  # A true coarse chart, with exact cancellation of the v and Bv3 zeros.
  candidates=[]
  valuation=0
  while valuation<4 and all(np.all(x%(47**(valuation+1))==0) for x in rawpoint):valuation+=1
  assert valuation<4
  residue_only=tuple(x//(47**valuation) for x in rawpoint)
  for kind,entry in [('CM3',cm3),('CM4',cm4)]:
   allW=r.from_json(entry['coarse_values'][0]);allW=r.mul(allW,r.inverse_values(r.mm(allW,a.fc)))
   wr=r.mul(residue_only,r.inverse_values(r.mm(residue_only,a.fc)))
   for ii in range(allW[0].shape[0]):
    if r.iszero(tuple(x%47 for x in r.sub(wr,r.rows(allW,[ii])))):candidates.append((kind,entry,ii,r.rows(allW,[ii])))
  assert len(candidates)==1,('elliptic actual full73 match',index,len(candidates))
  kind,entry,ii,W0=candidates[0];key=(kind,ii)
  if key not in elliptic_cache:
   H=7;shift=1 if kind=='CM3' else 2;c=r.from_json(entry['projective_coordinate']);baseJ=frames.local_jets(W0,a.fc,c,order=H+shift-1)
   iv=inv.series(baseJ['W']);vv,av,bv=iv['v'],iv['Av'],iv['Bv3'];assert r.iszero(vv[0]) and all(r.iszero(x) for x in bv[:shift]);assert np.all(r.units(vv[1])) and np.all(r.units(av[0])) and np.all(r.units(bv[shift]))
   U=Series(a,H);unit_v=vv[1:H+1];unit_b=bv[shift:shift+H];unit_a=av[:H]
   if kind=='CM3':unit=U.mul(U.mul(U.power(unit_a,3),U.power(unit_v,3)),U.inverse(U.power(unit_b,2)))
   else:unit=U.mul(U.power(unit_b,2),U.inverse(U.mul(U.power(unit_a,3),U.power(unit_v,3))))
   us=[r.zeros(1,1)]+unit;SS=Series(a,H+1)
   if kind=='CM3':js=SS.scale(SS.mul(us,SS.inverse(SS.add(SS.scale(us,4),const(27,H+1)))),6912)
   else:js=SS.scale(SS.inverse(SS.add(const(4,H+1),SS.scale(us,27))),6912)
   assert np.all(r.units(js[1]));knownu=[r.rows(r.from_json(x),[ii]) for x in entry['u_of_projective_coordinate']];assert all(r.equal(x,y) for x,y in zip(us,knownu))
   elliptic_cache[key]={'kind':kind,'coarse_row':ii,'J':baseJ,'frame':a.fc,'coordinate':c,'u':us,'j':js}
  E=elliptic_cache[key];JJ=E['J'];c=E['coordinate']
  if kind=='CM3':
   u0=r.mul(r.mul(r.mul(originalA,originalA),originalA),r.inverse_values(r.mul(originalB,originalB)));physical_factor=r.mul(r.mul(originalA,originalA),r.inverse_values(originalB))
  else:
   u0=r.mul(r.mul(originalB,originalB),r.inverse_values(r.mul(r.mul(originalA,originalA),originalA)));physical_factor=r.mul(originalB,r.inverse_values(originalA))
  physical_coarse=evaluate([r.rows(r.from_json(x),[ii]) for x in entry['coarse_values']],u0)
  assert r.equal(r.mul(physical_coarse,physical_factor),rawpoint),'all73 old raw target agrees after exact coarse stack factor'
  wr=r.mul(physical_coarse,r.inverse_values(r.mm(physical_coarse,a.fc)))
  z0=r.sub(r.mm(wr,c),r.mm(JJ['W'][0],c));assert all(not np.any(x%47) for x in z0);assert r.equal(evaluate(JJ['W'],z0),wr)
  deltaj=r.sub(target_jcm,E['j'][0]);assert all(not np.any(x%47) for x in deltaj);zcm=evaluate(Series(a,8).reversion(centered(E['j']),8),deltaj);assert r.equal(evaluate(E['j'],zcm),target_jcm)
  Wtarget=evaluate(JJ['W'],zcm);assert r.equal(r.mm(Wtarget,a.fc),const(1)[0]);JT=frames.local_jets(Wtarget,a.fc,c,order=4)
  # j has integral coefficients. Terms above degree7 contribute multiples of47^4 to every translated degree<=4.
  jt=[]
  for k in range(5):
   value=r.zeros(1,1)
   for n in range(k,8):value=r.add(value,a.scale(r.mul(E['j'][n],evaluate([r.zeros(1,1)]*(n-k)+[const(1)[0]],zcm)),comb(n,k)))
   jt.append(value)
  assert r.equal(jt[0],target_jcm)
  cert={'kind':kind,'original_raw_common_47_valuation':valuation,'raw_division_used_only_to_identify_residue_point':True,'physical_coarse_u_at_original_target':r.to_json(u0),'physical_raw_stack_factor_at_original_target':r.to_json(physical_factor),'all73_raw_target_reconstructed_with_exact_symbolic_stack_factor':True,'coarse_row_0based':ii,'initial_target_parameter_from_exact_elliptic_center':r.to_json(z0),'true_CM_target_parameter_from_exact_elliptic_center':r.to_json(zcm),'coarse_W_jets':dumpJ(JJ),'coarse_u_coefficients_0to7':[r.to_json(x) for x in E['u']],'coarse_j_coefficients_0to7':[r.to_json(x) for x in E['j']],'exact_v_and_Bv3_factors_removed_before_any_inverse':True,'translated_j_coefficients_through4_have_full_precision_by_integral_order7_tail':True,'all73_initial_target_and_true_target_transport_verified':True}
  return Wtarget,JT,jt,a.fc,c,cert
 records=[];ascending=[]
 for index,target in enumerate(hecke['targets']):
  root=r.column([target['kernel_x']]);rawpoint=r.rows(r.from_json(target['evaluation_matrix']),[target_row])
  for _ in range(2):
   r2=r.mul(root,root);r3=r.mul(r2,root);f=r.sub(r.add(r.add(a.scale(r.mul(r2,r2),3),a.scale(r2,6*A)),a.scale(root,12*Bcm)),const(A*A)[0]);df=r.add(r.add(a.scale(r3,12),a.scale(root,12*A)),const(12*Bcm)[0]);root=r.sub(root,r.mul(f,r.inverse_values(df)))
  r2=r.mul(root,root);r3=r.mul(r2,root);ta=r.sub(const(-9*A)[0],a.scale(r2,30));tb=r.sub(r.sub(const(-27*Bcm)[0],a.scale(root,42*A)),a.scale(r3,70));jcm=ellj([ta]+const(0)[1:],[tb]+const(0)[1:])[0]
  rinitial=r.column([target['kernel_x']]);ri2=r.mul(rinitial,rinitial);ri3=r.mul(ri2,rinitial);initialA=r.sub(const(-9*A)[0],a.scale(ri2,30));initialB=r.sub(r.sub(const(-27*B0)[0],a.scale(rinitial,42*A)),a.scale(ri3,70))
  elliptic_cert=None;parameter_type='j';parameter_model_root=None;target_parameter_map=None
  if not np.any(r.units(rawpoint)):
   targetCM,JT,jt,tframe,tc,elliptic_cert=actual_elliptic_chart(rawpoint,jcm,index,initialA,initialB)
  else:
   basechart=next(frames.iter_charts(rawpoint,order=4,max_points=1,label='CM27_T3_'+str(index)));tframe,tc=basechart['frame'],basechart['coordinate'];jb=jmap(basechart,etale=False)
   if np.all(r.units(jb[1])):
    delta=r.sub(jcm,jb[0]);assert all(not np.any(x%47) for x in delta);displacement=evaluate(S.reversion(centered(jb),N),delta);targetCM=evaluate(basechart['W'],displacement);JT=frames.local_jets(targetCM,tframe,tc,order=4);jt=jmap(JT)
   else:
    assert r.iszero(tuple(x%47 for x in r.sub(jb[0],const(1728)[0])))
    parameter_type='B_over_A_to_three_halves';modelroot0=sqrt_unit(initialA);chartroot0=r.mul(modelroot0,r.inverse_values(r.mm(rawpoint,tframe)));map0,root0=B_parameter(basechart,chartroot0)
    parameter_model_root=sqrt_unit(ta,modelroot0);targetvalue=r.mul(tb,r.inverse_values(r.mul(r.mul(parameter_model_root,parameter_model_root),parameter_model_root)))
    assert r.equal(map0[0],r.mul(initialB,r.inverse_values(r.mul(r.mul(modelroot0,modelroot0),modelroot0))))
    delta=r.sub(targetvalue,map0[0]);assert all(not np.any(x%47) for x in delta);displacement=evaluate(S.reversion(centered(map0),N),delta);targetCM=evaluate(basechart['W'],displacement);JT=frames.local_jets(targetCM,tframe,tc,order=4);jt=jmap(JT,etale=False);target_parameter_map,_=B_parameter(JT,evaluate(root0,displacement));assert r.equal(target_parameter_map[0],targetvalue)
   assert r.equal(jt[0],jcm)
  ramified_to_b=r.iszero(ta)
  if ramified_to_b:
   assert r.iszero(jcm);tob=r.mul(targetCM,r.inverse_values(r.mm(targetCM,a.fc)));assert r.equal(tob,b);ascending.append(index)
  rs=[root]+const(0)[1:]
  for _ in range(3):
   r2s=S.power(rs,2);r3s=S.mul(r2s,rs);f=S.sub(S.add(S.add(S.scale(S.power(rs,4),3),S.scale(r2s,6*A)),S.scale(S.mul(Bofx,rs),12)),const(A*A));df=S.add(S.add(S.scale(r3s,12),S.scale(rs,12*A)),S.scale(Bofx,12));rs=S.sub(rs,S.mul(f,S.inverse(df)))
  r2s=S.power(rs,2);r3s=S.mul(r2s,rs);f=S.sub(S.add(S.add(S.scale(S.power(rs,4),3),S.scale(r2s,6*A)),S.scale(S.mul(Bofx,rs),12)),const(A*A));assert all(r.iszero(x) for x in f)
  As=S.sub(const(-9*A),S.scale(r2s,30));Bs=S.sub(S.sub(S.scale(Bofx,-27),S.scale(rs,42*A)),S.scale(r3s,70));jimage=ellj(As,Bs)
  if parameter_type=='j':image_parameter=jimage;target_parameter_map=jt
  else:image_parameter=S.mul(Bs,S.inverse(S.power(sqrt_series(As,parameter_model_root),3)))
  h=S.compose(S.reversion(centered(target_parameter_map),N),centered(image_parameter));assert all(r.equal(x,y) for x,y in zip(S.compose(jt,h),jimage))
  if ramified_to_b:assert all(r.iszero(x) for x in h[:3]) and np.all(r.units(h[3])) and r.iszero(As[0]) and np.all(r.units(As[1]))
  Wi=S.compose(JT['W'],h);V2i=S.compose(JT['V2'],h);V3i=S.compose(JT['V3'],h);Hi=S.compose(JT['Hc'],h);factor=Series(a,4).mul([a.scale(h[k+1],k+1) for k in range(4)],Series(a,4).inverse(Hi[:4]))
  rec={'branch_0based':index,'unit_target_parameter_type':parameter_type,'target_parameter_map_coefficients_0to4':[r.to_json(x) for x in target_parameter_map],'actual_image_parameter_map_coefficients_0to4':[r.to_json(x) for x in image_parameter],'ramified_degree3_to_b':ramified_to_b,'original_target_source_row_0based':target_row,'original_kernel_root_in_R2':target['kernel_x'],'original_actual_target_W':r.to_json(rawpoint),'kernel_root_at_true_CM':r.to_json(root),'kernel_coefficients_0to4':[r.to_json(x) for x in rs],'target_A_coefficients_0to4':[r.to_json(x) for x in As],'target_B_coefficients_0to4':[r.to_json(x) for x in Bs],'all73_actual_target_at_true_CM':r.to_json(targetCM),'frame':r.to_json(tframe),'coordinate':r.to_json(tc),'target_local_j_coefficients_0to4':[r.to_json(x) for x in jt],'target_local_jets_0to4':dumpJ(JT),'actual_image_j_coefficients_0to4':[r.to_json(x) for x in jimage],'actual_image_parameter_coefficients_0to4':[r.to_json(x) for x in h],'actual_image_W_coefficients_0to4':[r.to_json(x) for x in Wi],'actual_image_V2_coefficients_0to4':[r.to_json(x) for x in V2i],'actual_image_V3_coefficients_0to4':[r.to_json(x) for x in V3i],'actual_image_Hc_coefficients_0to4':[r.to_json(x) for x in Hi],'actual_differential_pullback_coefficients_0to3':[r.to_json(x) for x in factor],'coarse_elliptic_transport':elliptic_cert}
  if ramified_to_b:
   U=Series(a,4);alpha=As[1:5];den4=U.add(U.scale(U.power(As[:4],3),4),U.scale(U.power(Bs[:4],2),27));T=Series(a,3);alpha_prime=[a.scale(alpha[k+1],k+1) for k in range(3)];den_prime=[a.scale(den4[k+1],k+1) for k in range(3)];unitlog=T.sub(T.scale(T.mul(alpha_prime,T.inverse(alpha[:3])),3),T.mul(den_prime,T.inverse(den4[:3])));rec['log_of_j_target_over_x_cubed_derivative_coefficients_0to2']=[r.to_json(x) for x in unitlog];rec['j_target_div_x_cubed_unit_formula']='6912*(A_target/x)^3/(4*A_target^3+27*B_target^2)';rec['leading_j_target_degree3_coefficient']=r.to_json(jimage[3])
  records.append(rec);print('PASS CM27 actual T3 branch',index,'to_b',ramified_to_b,'coarse',None if elliptic_cert is None else elliptic_cert['kind'],flush=True)
 assert len(ascending)==1
 lhs=[r.zeros(1,73) for _ in range(4)]
 for rec in records:
  vals=Series(a,4).mul([r.from_json(x) for x in rec['actual_image_W_coefficients_0to4'][:4]],[r.from_json(x) for x in rec['actual_differential_pullback_coefficients_0to3']]);lhs=[r.add(x,y) for x,y in zip(lhs,vals)]
 source_values=Series(a,4).mul(Jsource['W'][:4],Jsource['inverse_Hc'][:4]);rhs=[r.mm(x,r.from_json(hecke['weight2_operator'])) for x in source_values];assert all(r.equal(x,y) for x,y in zip(lhs,rhs)),'full73 actual pullback traces'
 assert all(r.equal(r.mm(x,a.K1),r.mm(r.mm(v,a.K1),r.from_json(hecke['canonical_operator']))) for x,v in zip(lhs,source_values))
 out={'result':'R316','level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'disk_id':anchor['disk_id'],'source_CM_anchor':anchor,'source_frame':r.to_json(frame),'source_coordinate':r.to_json(coordinate),'source_original_model':[1,32],'source_true_CM_physical_model':[A,Bcm],'source_original_row_0based':source_row,'source_projective_jets_0to4':dumpJ(Jsource),'source_true_CM_j_coefficients_0to4':[r.to_json(x) for x in jsource],'source_physical_B_displacement_coefficients_0to4':[r.to_json(x) for x in source_t],'parameter':'x=z_original-z_CM; w=x/47=y_original-75213','branch_records':records,'ascending_ramified_to_b_branch_indices_0based':ascending,'complete_actual4_T3_local_branches':True,'actual_ramification_degree3_to_true_b_verified':True,'all4x73_actual_Hecke_pullback_coefficients_verified':True,'all4x54_canonical_Hecke_pullback_coefficients_verified':True,'full73_pullback_trace_coefficients_0to3':[r.to_json(x) for x in lhs],'complete_actual_local_F3_height':False,'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),'runtime_seconds':round(time.monotonic()-start,3)}
 digest=save(args.output,out);print('PASS actual CM27 ramified branches',ascending,digest,flush=True)
if __name__=='__main__':main()
