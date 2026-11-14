#!/usr/bin/env python3
"""Construct actual 54 second-kind variational Poincare connection forms.

The double poles are the R141 second Abel family, the calibration is the
actual R141 Hecke correction in exactly the R145 two-family frame.
"""
import argparse,gzip,hashlib,json,random,sys,time
from pathlib import Path

def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--script-dir',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--work-dir',type=Path,required=True)
 args=ap.parse_args();sys.path.insert(0,str(args.script_dir.resolve()));args.work_dir.mkdir(parents=True,exist_ok=True)
 import numpy as np
 import p41_r2_matrix as r
 from p41_projective_jet_frames47 import install_exact_float_mm
 install_exact_float_mm(r)
 from p41_actual_differentials47 import ActualModel,save
 from p41_hecke3_hessian47 import section_jets
 a=ActualModel(args.script_dir);M=a.M;q=r.Q;start=time.monotonic()
 def vcat(*xs):return tuple(np.concatenate([x[k] for x in xs],axis=0) for k in range(2))
 def scale(x,k):return tuple(y*(k%q)%q for y in x)
 def transpose(x):return tuple(y.T.copy() for y in x)
 def kernel(x,want):
  rr,cc=r.rank_pivots(x);assert len(rr)==want,(len(rr),want)
  out,free,block=r.kernel_from_rows(r.rows(x,rr),rr,cc);assert r.iszero(r.mm(x,out));return out,rr,cc
 bases=a.read('p41_hecke3_abel_bases_checkpoint.json.gz');hessian=a.read('p41_hecke3_hessian47_compact.json.gz');jets=a.read('p41_source_cubic47_full_saved.json.gz')
 I1,I2=[[i-1 for i in f['points_1based']] for f in bases['families']]
 assert [f['points_1based'] for f in bases['families']]==[f['points_1based'] for f in hessian['families']]
 W=[r.from_json(x) for x in jets['evaluation_coefficients'][:3]];assert r.equal(W[0],M['W'])
 V2,V3=section_jets(W,[a.model,a.cusp,a.cm4,a.group],M,r)
 assert r.equal(V2[0],M['V2']) and r.equal(V3[0],M['V3'])
 v=r.from_json(bases['families'][1]['v_coefficients']);vv=[r.mm(w,v) for w in W]
 assert r.iszero(r.rows(vv[0],I2)) and np.all(r.units(r.rows(vv[1],I2)))
 other=[i for i in range(820) if i not in set(I2)];assert len(other)==766 and np.all(r.units(r.rows(vv[0],other)))
 # Actual sections vanishing to order two at every pole.
 H2,pr,pc=kernel(vcat(r.rows(V2[0],I2),r.rows(V2[1],I2)),108);assert H2[0].shape==(199,91)
 hv=r.mm(M['V2'],H2);H2inv=r.inverse_matrix(r.rows(H2,r.rank_pivots(H2)[0]))
 hr=r.rank_pivots(H2)[0];AH2=r.mm(H2inv,r.rows(r.mm(M['A2'],r.conjugate(H2)),hr));assert r.equal(r.mm(H2,AH2),r.mm(M['A2'],r.conjugate(H2)))
 E=r.rows(M['V3'],other);er,ec=r.rank_pivots(E);assert len(er)==325 and ec==list(range(325))
 Einv=r.inverse_matrix(r.rows(E,er));iv2=r.inverse_values(r.mul(r.rows(vv[0],other),r.rows(vv[0],other)))
 rng=random.Random(4104724001);history=[];constraint=r.zeros(0,325);tests=[]
 for k in range(6):
  seed,hsmall=r.rational_trace(AH2,rng);hc=r.mm(H2,hsmall);hh=r.rows(r.mm(M['V2'],hc),other)
  scaled=r.mul(r.mul(hh,iv2),E);res=r.sub(scaled,r.mm(E,r.mm(Einv,r.rows(scaled,er))))
  joined=vcat(constraint,res);rr,cc=r.rank_pivots(joined);history.append(len(rr));assert len(rr)<=144
  constraint=r.rows(joined,rr);tests.append(r.to_json(hc));print('Actual double-residual colon',k+1,len(rr),flush=True)
  if len(rr)==144:break
 else:raise AssertionError(('colon did not saturate',history))
 S0,rr,cc=kernel(constraint,144);assert S0[0].shape==(325,181)
 for hcj in tests:
  hh=r.rows(r.mm(M['V2'],r.from_json(hcj)),other);scaled=r.mul(r.mul(hh,iv2),r.mm(E,S0))
  assert r.equal(scaled,r.mm(E,r.mm(Einv,r.rows(scaled,er))))
 # Cusps removed in their two complete R80 fields, not only by total residue.
 cusp_rows=[]
 for index in [0,11]:
  _,CV3=a.cusp_evaluations(index);cusp_rows.append(r.mm(CV3,S0))
 C=vcat(*cusp_rows);KS,csr,csc=kernel(C,20);S=r.mm(S0,KS);assert S[0].shape==(325,161)
 print('Actual second-kind candidate space rank161; full cusp fields vanish',flush=True)
 # Principal double poles in the actual B=32+t parameter.
 beta0=-3*pow(27652,-1,q)%q;beta1=3*1728*pow(27652,-2,q)%q
 v1=r.rows(vv[1],I2);v2=r.rows(vv[2],I2);Sval=r.mm(r.rows(V3[0],I2),S);Sd=r.mm(r.rows(V3[1],I2),S)
 principal=r.mul(scale(r.inverse_values(r.mul(v1,v1)),beta0),Sval)
 ratio=r.sub(r.column([[beta1*pow(beta0,-1,q)%q,0]]*54),scale(r.mul(v2,r.inverse_values(v1)),2))
 residue=r.mul(scale(r.inverse_values(r.mul(v1,v1)),beta0),r.add(Sd,r.mul(ratio,Sval)))
 poles=vcat(principal,residue);assert len(r.rank_pivots(poles)[0])==107
 assert r.iszero((np.sum(residue[0],axis=0,keepdims=True)%q,np.sum(residue[1],axis=0,keepdims=True)%q))
 Omega1=scale(r.mm(r.rows(W[0],I1),a.K1),beta0);Omega2=scale(r.mm(r.rows(W[0],I2),a.K1),beta0)
 assert len(r.rank_pivots(Omega1)[0])==54 and len(r.rank_pivots(Omega2)[0])==54
 from p41_poincare_norms47 import determinant
 omega_dets=[determinant(Omega1),determinant(Omega2)]
 assert omega_dets==[f['abel_tangent_determinant'] for f in hessian['families']]
 B=r.from_json(hessian['hecke_correction_matrix']);target=r.mm(r.mm(Omega1,B),transpose(Omega2))
 vcal=r.rows(vv[0],I1);assert np.all(r.units(vcal))
 calibration=r.mul(scale(r.inverse_values(r.mul(vcal,vcal)),beta0),r.mm(r.rows(V3[0],I1),S))
 A=vcat(principal,residue,calibration);rhs=vcat(r.eye(54),r.zeros(54,54),target)
 ar,ac=r.rank_pivots(A);assert len(ar)==161 and ac==list(range(161))
 co=r.mm(r.inverse_matrix(r.rows(A,ar)),r.rows(rhs,ar));assert r.equal(r.mm(A,co),rhs)
 numerator=r.mm(S,co)
 perm=[I2.index(M['tau'][i]) for i in I2];assert r.equal(r.mm(M['A3'],r.conjugate(numerator)),r.cols(numerator,perm))
 assert r.equal(r.mm(M['A1'],r.conjugate(v)),v)
 out={'level':41,'auxiliary_prime':47,'precision':4,'modulus':q,
 'all54_actual_variational_second_kind_forms_complete':True,'complete_local_QC_heights':False,'complete_common_roots':False,
 'pole_family':'R141/R145 second Abel family, exact t=B-32 parameters',
 'pole_indices_1based':[i+1 for i in I2],'calibration_indices_1based':[i+1 for i in I1],
 'denominator_linear_section':r.to_json(v),'denominator_power':2,'numerator_cubic_sections':r.to_json(numerator),
 'form_convention':'nu_j=beta(t)*s_j(W(t))/v(W(t))^2 dt; actual KS normalization',
 'double_principal_coefficients':r.to_json(r.mm(principal,co)),
 'residues':r.to_json(r.mm(residue,co)),'calibration_parameter_matrix':r.to_json(target),
 'pole_Frobenius_permutation_0based':perm,'candidate_dimension':161,'principal_part_rank':107,'final_rank':161,
 'second_kind_holomorphic_residue_pairing':r.to_json(r.neg(Omega2)),
 'actual_Abel_tangent_determinants':omega_dets,'integral_de_Rham_basis_dimension':108,
 'final_unit_minor_rows_0based':ar,'equations_checked':162*54,'colon_rank_history':history,'colon_test_section_coefficients':tests,
 'candidate_cubic_basis':r.to_json(S),'candidate_solution_coordinates':r.to_json(co),
 'input_sha256':a.inputs,'source_sha256':sha(__file__),
 'runtime_seconds':round(time.monotonic()-start,3)}
 outsha=save(args.output,out);print('PASS all54 normalized variational second-kind forms; 8748 equations and Frobenius',outsha,flush=True)
if __name__=='__main__':main()
