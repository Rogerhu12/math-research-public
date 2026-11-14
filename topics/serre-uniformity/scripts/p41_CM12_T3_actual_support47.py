#!/usr/bin/env python3
"""Actual full-level T3 targets of the true CM(-12) point via certified SS reference fibres."""
import argparse,gzip,json,hashlib,sys,time
from pathlib import Path

def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','basic-anchors','fixed-support','output']:ap.add_argument('--'+k,type=Path,required=True)
 args=ap.parse_args();scripts=args.script_dir.resolve();sys.path.insert(0,str(scripts))
 from p41_dag_level_transport47 import initialize,FullLevelTransport
 from p41_projective_jet_frames47 import ordinary_physical_jets,install_exact_float_mm
 from p41_coprime_kernel_dag47 import velu_model
 from p41_supersingular_atlas47 import ca,cs,cn,cm,ci,ck,cp
 from p41_actual_differentials47 import save,digest,Q
 start=time.monotonic();at=initialize(scripts);a,r,np=at.a,at.r,at.np;install_exact_float_mm(r);level=FullLevelTransport(at);F=level.F;inputs={}
 def load(p):inputs[str(p)]=sha(p);return read(p)
 anchors=load(args.basic_anchors);anchor=next(x for x in anchors['records'] if x['label']=='P_minus12');fixed=load(args.fixed_support);Wcm=r.from_json([anchor['actual_W_in_original_SS_atlas_frame_mod47four']]);source=next(x for x in fixed['groups']['Z12']['points'] if r.equal(r.from_json([x['W_mod47four']]),Wcm));assert source['reference_key']=='44' and source['necklace_index_1based']==46;idx=45;A,B=(-15%Q,0),(22,0)
 key,c,t=level.match(A,B);assert key=='44' and tuple(source['physical_reference_parameter'])==t
 ref=level.refs[key]
 def scale_point(T,c):return F.mul(T[0],F.embed(cp(c,2,47))),F.mul(T[1],F.embed(cp(c,3,47)))
 P0,Q0=[scale_point(F.point(ref[k]),c) for k in ['P','Q']]
 physical_cache={};physical_certs={};coarsepath=scripts/'data/p41_elliptic_coarse_atlas47_verified.json.gz'
 def physical_values(key,t,c,index):
  if key not in physical_cache:
   obj=ordinary_physical_jets(at,int(key),order=3,coarse_path=coarsepath);physical_cache[key]=obj;physical_certs[key]={'all_coefficients_integral':True,'coefficient_sha256':[digest(r.to_json(x)) for x in obj['W']],'ordinary_indices_0based':obj['ordinary_indices_0based'],'clearing_patches':obj['clearing_patches']}
  obj=physical_cache[key];assert index in obj['ordinary_indices_0based'];assert all(x%47==0 for x in t);out=r.zeros(1,73)
  for coef in reversed(obj['W']):out=r.add(at.matrix_scale(out,t),r.rows(coef,[index]))
  return at.matrix_scale(out,cp(c,2))
 Wraw=physical_values(key,t,c,idx);assert r.equal(r.mul(Wraw,r.inverse_values(r.mm(Wraw,a.fc))),Wcm)
 records=[];sumW=r.zeros(1,73)
 for n,rbar in enumerate([(3,0),(15,0),(38,11),(38,36)]):
  rr=rbar
  for _ in range(2):
   f=cs(ca(ca(ck(cp(rr,4),3),ck(cm(A,cp(rr,2)),6)),ck(cm(B,rr),12)),cp(A,2));df=ca(ca(ck(cp(rr,3),12),ck(cm(A,rr),12)),ck(B,12));rr=cs(rr,cm(f,ci(df)))
  assert cs(ca(ca(ck(cp(rr,4),3),ck(cm(A,cp(rr,2)),6)),ck(cm(B,rr),12)),cp(A,2))==(0,0)
  kernel=[cn(rr),(1,0)];At,Bt=velu_model(3,kernel,A,B);node={'ell':3,'source_A':A,'source_B':B,'A':At,'B':Bt,'kernel':kernel};P1,Q1=level.raw_pair(node,P0,Q0);target=level.record(At,Bt,P1,Q1,3,[idx]);kt=target['reference_key'];assert kt not in ['0','36'];ix=target['image_indices_1based'][0]-1;raw=physical_values(kt,tuple(target['reference_parameter']),tuple(target['homothety']),ix);W=r.mul(raw,r.inverse_values(r.mm(raw,a.fc)));sumW=r.add(sumW,raw)
  horizontal=r.equal(W,Wcm);assert horizontal==(n==0)
  records.append({'branch_0based':n,'kernel_root_in_R2':list(rr),'kernel_polynomial':kernel,'target_curve_A':At,'target_curve_B':Bt,'actual_full_level_transport':target,'W_actual_values_in_R2':r.to_json(raw)[0],'W_fc_normalized_mod47four':r.to_json(W)[0],'horizontal_fixed_point':horizontal,'all_target_full73_physical_transport':True})
  print('PASS true CM12 T3 target',n,'reference',kt,'necklace',ix+1,'horizontal',horizontal,flush=True)
 hecke=load(scripts/'data/p41_hecke47_full_saved.json.gz')['operators']['3'];assert r.equal(a.scale(sumW,pow(3,-1,Q)),r.mm(Wraw,r.from_json(hecke['weight2_operator']))),'actual T3 sum full73 values and physical1/3 scale'
 conjugate=[r.mm(r.conjugate(r.from_json([x['W_fc_normalized_mod47four']])),r.conjugate(a.M['A1'])) for x in records]
 for i,j in enumerate([0,1,3,2]):assert r.equal(conjugate[i],r.from_json([records[j]['W_fc_normalized_mod47four']]))
 out={'result':'R324','level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'source_disk_id':anchor['disk_id'],'source_curve':[-15,22],'source_actual_CM_anchor':anchor,'source_reference_necklace_index_1based':46,'source_reference_model_match':{'reference_key':key,'homothety':c,'physical_parameter':t},'source_physical_raw_W_mod47four':r.to_json(Wraw),'branch_records':records,'complete_actual_T3_support':True,'actual_full73_Hecke_value_sum_verified':True,'all_actual_raw_level_determinants_equal3':True,'actual_full73_Frobenius_permutation':[0,1,3,2],'physical_reference_jets':physical_certs,'actual1681_reference_point_tables':{k:x['certificate'] for k,x in level.lookup_tables.items()},'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),'scope':'Four actual T3 target points at trueCM12; real residue41-torsion maps and fullprecision physical reference transport. No complete localheight yet.','runtime_seconds':round(time.monotonic()-start,3)}
 digest=save(args.output,out);print('PASS all actual CM12 T3 support SHA',digest,flush=True)
if __name__=='__main__':main()
