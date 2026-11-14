#!/usr/bin/env python3
"""Actual T2 branches at true CM(-12), including the cubic coarse return to b."""
import argparse,gzip,hashlib,json,sys,time
from pathlib import Path
from types import SimpleNamespace

def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','basic-anchors','output']:ap.add_argument('--'+k,type=Path,required=True)
 args=ap.parse_args();scripts=args.script_dir.resolve();sys.path.insert(0,str(scripts));start=time.monotonic()
 import numpy as np
 import p41_r2_matrix as r
 from p41_actual_differentials47 import ActualModel,save
 from p41_projective_jet_frames47 import ProjectiveJetFrames,install_exact_float_mm
 from p41_elliptic_coarse_atlas47 import Series,ClassicalInvariants
 install_exact_float_mm(r);a=ActualModel(scripts);frames=ProjectiveJetFrames(a);Q=r.Q;N=5;S=Series(a,N);inputs={}
 def load(p):inputs[str(p)]=sha(p);return read(p)
 def standard(n):return load(scripts/'data'/n)
 anchors=load(args.basic_anchors);anchor=next(x for x in anchors['records'] if x['label']=='P_minus12');assert anchor['disk_id']=='SS_j44_02' and anchor['discriminant']==-12
 atlas=standard('p41_rational_SS_residue_atlas47_complete.json.gz');chart=next(c for c in atlas['charts'] if anchor['disk_id'] in c['disk_ids']);row=chart['disk_ids'].index(anchor['disk_id']);frame,coordinate=r.from_json(chart['frame']),r.from_json(chart['coordinate']);Wcm=r.from_json([anchor['actual_W_in_original_SS_atlas_frame_mod47four']]);assert r.equal(frame,a.fc)
 Jsource=frames.local_jets(Wcm,frame,coordinate,order=4)
 derivative=standard('p41_cleared_serre_derivative47_complete.json.gz');inv=ClassicalInvariants(SimpleNamespace(a=a,r=r,v=r.from_json(derivative['chosen_clearing_section']),G=r.from_json(derivative['cleared_derivative_coefficients'])))
 hecke=standard('p41_hecke47_full_saved.json.gz')['operators']['2'];targets=standard('p41_t2_cm_targets47_verified.json.gz');cm12=standard('p41_cm12_hecke47_verified.json.gz');cm3cert=standard('p41_cm3_makdisi47_certificate.json');coarse=standard('p41_elliptic_coarse_atlas47_verified.json.gz');cm3=next(x for x in coarse['elliptic_charts'] if x['kind']=='CM3')
 assert 'independent' in targets['status']
 for n,h in targets['verification_source_sha256'].items():assert sha(scripts/n)==h;inputs[n]=h
 for n,h in targets['source_sha256'].items():assert sha(scripts/'data'/n)==h
 braw=r.from_json(cm3['coarse_values'][0]);b=r.mul(braw,r.inverse_values(r.mm(braw,a.fc)))
 # The verified dual returns basis(2P,21Q) after the2-homothety.
 targetlabel=next(x for x in targets['cases'] if x[0]=='CM48_plus')[-1];nx,ne=a.model['necklaces'][targetlabel-1];basepair=a.model['necklaces'][cm3cert['CM_necklace_index_1based']-1];assert [4*nx%41,16*ne%41]==basepair;assert cm12['source_CM_necklace_index_1based']==cm3cert['CM_necklace_index_1based']
 def const(c,n=N):
  first=r.column([c if isinstance(c,(list,tuple)) else [c%Q,0]]);return [first]+[r.zeros(1,1) for _ in range(n-1)]
 def centered(v):return [r.zeros(*v[0][0].shape)]+list(v[1:])
 def ellj(AA,BB):
  a3=S.power(AA,3);return S.scale(S.mul(a3,S.inverse(S.add(S.scale(a3,4),S.scale(S.power(BB,2),27)))),6912)
 def jmap(J,etale=True):
  iv=inv.series(J['W']);num=S.mul(S.power(iv['Av'],3),S.power(iv['v'],3));den=S.add(S.scale(num,4),S.scale(S.power(iv['Bv3'],2),27));assert np.all(r.units(den[0]));out=S.scale(S.mul(num,S.inverse(den)),6912);assert not etale or np.all(r.units(out[1]));return out
 def dumpJ(J):return {k:[r.to_json(x) for x in J[k]] for k in ['W','V2','V3','Hc','inverse_Hc']}
 def sqrtunit(value):
  ar,ai=int(value[0][0,0])%47,int(value[1][0,0])%47;candidates=[(x,y) for x in range(47) for y in range(47) if (x*x-y*y-ar)%47==0 and (2*x*y-ai)%47==0];assert candidates;rr=r.column([list(candidates[0])])
  for _ in range(2):rr=a.scale(r.add(rr,r.mul(value,r.inverse_values(rr))),pow(2,-1,Q))
  assert r.equal(r.mul(rr,rr),value);return rr
 def sqrtseries(values,root):
  out=[root]+const(0)[1:]
  for _ in range(3):out=S.scale(S.add(out,S.mul(values,S.inverse(out))),pow(2,-1,Q))
  assert all(r.equal(x,y) for x,y in zip(S.power(out,2),values));return out
 def Bparameter(J,root):
  iv=inv.series(J['W']);Av=S.mul(iv['Av'],S.inverse(iv['v']));Bv=S.mul(iv['Bv3'],S.inverse(S.power(iv['v'],3)));out=S.mul(Bv,S.inverse(S.power(sqrtseries(Av,root),3)));assert np.all(r.units(out[1]));return out
 A,Bcm=-15,22;jsource=jmap(Jsource);assert r.equal(jsource[0],const(54000)[0]);pb=const(Bcm);pb[1]=const(1)[0];pj=ellj(const(A),pb);source_t=S.compose(S.reversion(centered(pj),N),centered(jsource));Bofx=S.add(const(Bcm),source_t);assert all(r.equal(x,y) for x,y in zip(ellj(const(A),Bofx),jsource))
 # True coarse b chart: v=zV and Bv3=zB1 are canceled symbolically.
 bc=r.from_json(cm3['projective_coordinate']);BJ=frames.local_jets(b,a.fc,bc,order=4);iv=inv.series(BJ['W']);assert r.iszero(iv['v'][0]) and r.iszero(iv['Bv3'][0]);U=Series(a,4);uu=U.mul(U.mul(U.power(iv['Av'][:4],3),U.power(iv['v'][1:5],3)),U.inverse(U.power(iv['Bv3'][1:5],2)));u=[r.zeros(1,1)]+uu;bj=S.scale(S.mul(u,S.inverse(S.add(S.scale(u,4),const(27)))),6912);assert np.all(r.units(bj[1]));assert all(r.equal(x,r.from_json(y)) for x,y in zip(u,cm3['u_of_projective_coordinate']))
 source_records=[{'label':'CM3_ascending','kernel':2,'target':None}]
 for label in ['CM48_plus','CM48_minus']:
  c=next(c for c in targets['cases'] if c[0]==label);assert c[1:3]==[A,Bcm];source_records.append({'label':label,'kernel':c[6],'target':next(t for t in targets['records'] if t['label']==label)})
 records=[]
 for index,sr in enumerate(source_records):
  root=const(sr['kernel'])[0];assert r.iszero(r.add(r.add(r.mul(r.mul(root,root),root),a.scale(root,A)),const(Bcm)[0]));rs=[root]+const(0)[1:]
  for _ in range(3):
   f=S.add(S.add(S.power(rs,3),S.scale(rs,A)),Bofx);df=S.add(S.scale(S.power(rs,2),3),const(A));rs=S.sub(rs,S.mul(f,S.inverse(df)))
  assert all(r.iszero(x) for x in S.add(S.add(S.power(rs,3),S.scale(rs,A)),Bofx))
  vv=S.add(S.scale(S.power(rs,2),3),const(A));As=S.sub(const(A),S.scale(vv,5));Bs=S.sub(Bofx,S.scale(S.mul(rs,vv),7));jimage=ellj(As,Bs)
  ramified=index==0;ptype='j';modelroot=None
  if ramified:
   assert r.iszero(As[0]) and r.equal(Bs[0],const(64)[0]);targetCM=b;JT=BJ;tframe=a.fc;tc=bc;jt=bj;tmap=bj;rawpoint=const(0)[0]
  else:
   target=sr['target'];assert r.equal(As[0],const(target['curve_A'])[0]) and r.equal(Bs[0],const(target['curve_B'])[0]);rawpoint=r.from_json(target['weight2_values']);CJ=next(frames.iter_charts(rawpoint,order=4,max_points=1,label='CM12_T2_'+sr['label']));JT=CJ;tframe=CJ['frame'];tc=CJ['coordinate'];targetCM=CJ['W'][0];jt=jmap(JT,etale=False);assert r.equal(jt[0],const(target['j_mod47four'])[0]);tmap=jt
   if not np.all(r.units(jt[1])):
    assert r.iszero(tuple(x%47 for x in r.sub(jt[0],const(1728)[0])));ptype='B_over_A_to_three_halves';modelroot=sqrtunit(As[0]);tmap=Bparameter(JT,r.mul(modelroot,r.inverse_values(r.mm(rawpoint,tframe))))
  if ptype=='j':imageparam=jimage
  else:imageparam=S.mul(Bs,S.inverse(S.power(sqrtseries(As,modelroot),3)))
  assert r.equal(imageparam[0],tmap[0]);hh=S.compose(S.reversion(centered(tmap),N),centered(imageparam));assert all(r.equal(x,y) for x,y in zip(S.compose(jt,hh),jimage))
  if ramified:assert all(r.iszero(x) for x in hh[:3]) and np.all(r.units(hh[3])) and np.all(r.units(As[1]))
  Wi=S.compose(JT['W'],hh);V2i=S.compose(JT['V2'],hh);V3i=S.compose(JT['V3'],hh);Hi=S.compose(JT['Hc'],hh);fac=Series(a,4).mul([a.scale(hh[k+1],k+1) for k in range(4)],Series(a,4).inverse(Hi[:4]))
  rec={'branch_0based':index,'label':sr['label'],'ramified_degree3_to_b':ramified,'kernel_x_at_true_CM':sr['kernel'],'kernel_coefficients_0to4':[r.to_json(x) for x in rs],'target_A_coefficients_0to4':[r.to_json(x) for x in As],'target_B_coefficients_0to4':[r.to_json(x) for x in Bs],'actual_source_of_target':'published verified dual and actual necklace return' if ramified else 'published direct torsion Velu and all73 evaluation','all73_actual_target_at_true_CM':r.to_json(targetCM),'frame':r.to_json(tframe),'coordinate':r.to_json(tc),'target_local_jets_0to4':dumpJ(JT),'target_local_j_coefficients_0to4':[r.to_json(x) for x in jt],'unit_target_parameter_type':ptype,'target_parameter_map_coefficients_0to4':[r.to_json(x) for x in tmap],'actual_image_parameter_map_coefficients_0to4':[r.to_json(x) for x in imageparam],'actual_image_parameter_coefficients_0to4':[r.to_json(x) for x in hh],'actual_image_j_coefficients_0to4':[r.to_json(x) for x in jimage],'actual_image_W_coefficients_0to4':[r.to_json(x) for x in Wi],'actual_image_V2_coefficients_0to4':[r.to_json(x) for x in V2i],'actual_image_V3_coefficients_0to4':[r.to_json(x) for x in V3i],'actual_image_Hc_coefficients_0to4':[r.to_json(x) for x in Hi],'actual_differential_pullback_coefficients_0to3':[r.to_json(x) for x in fac]}
  if ramified:
   T=Series(a,3);U4=Series(a,4);alpha=As[1:5];den=U4.add(U4.scale(U4.power(As[:4],3),4),U4.scale(U4.power(Bs[:4],2),27));lg=T.sub(T.scale(T.mul([a.scale(alpha[k+1],k+1) for k in range(3)],T.inverse(alpha[:3])),3),T.mul([a.scale(den[k+1],k+1) for k in range(3)],T.inverse(den[:3])));rec['log_of_j_target_over_x_cubed_derivative_coefficients_0to2']=[r.to_json(x) for x in lg];rec['coarse_u_coefficients_0to4_in_target_chart']=[r.to_json(x) for x in u]
  records.append(rec);print('PASS true CM12 T2 branch',sr['label'],'parameter',ptype,'ramified_to_b',ramified,flush=True)
 lhs=[r.zeros(1,73) for _ in range(4)]
 for rec in records:
  values=Series(a,4).mul([r.from_json(x) for x in rec['actual_image_W_coefficients_0to4'][:4]],[r.from_json(x) for x in rec['actual_differential_pullback_coefficients_0to3']]);lhs=[r.add(x,y) for x,y in zip(lhs,values)]
 source=Series(a,4).mul(Jsource['W'][:4],Jsource['inverse_Hc'][:4]);assert all(r.equal(x,r.mm(y,r.from_json(hecke['weight2_operator']))) for x,y in zip(lhs,source)),'actual T2 full73 differential pullbacks'
 assert all(r.equal(r.mm(x,a.K1),r.mm(r.mm(y,a.K1),r.from_json(hecke['canonical_operator']))) for x,y in zip(lhs,source))
 out={'result':'R321','level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'disk_id':anchor['disk_id'],'source_CM_anchor':anchor,'source_frame':r.to_json(frame),'source_coordinate':r.to_json(coordinate),'source_true_CM_physical_model':[A,Bcm],'source_projective_jets_0to4':dumpJ(Jsource),'source_true_CM_j_coefficients_0to4':[r.to_json(x) for x in jsource],'source_physical_B_displacement_coefficients_0to4':[r.to_json(x) for x in source_t],'parameter':'x=z_R228-z_CM; w=x/47=y_R228-96923','branch_records':records,'actual_ascending_dual_level_return':{'target_homothety':2,'return_basis_matrix_mod41':[[2,0],[0,21]],'target_necklace_label_before_matrix':targetlabel,'target_pair_before_matrix':[nx,ne],'actual_return_pair':basepair,'actual_return_necklace_label':cm3cert['CM_necklace_index_1based'],'full_actual_torsion_dual_source':targets['verification_source_sha256']},'complete_actual3_T2_local_branches':True,'actual_ramification_degree3_to_true_b_verified':True,'all4x73_actual_Hecke_pullback_coefficients_verified':True,'all4x54_canonical_Hecke_pullback_coefficients_verified':True,'full73_pullback_trace_coefficients_0to3':[r.to_json(x) for x in lhs],'complete_actual_local_F2_height':False,'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),'runtime_seconds':round(time.monotonic()-start,3)}
 digest=save(args.output,out);print('PASS true CM12 all actual T2 branches',digest,flush=True)
if __name__=='__main__':main()
