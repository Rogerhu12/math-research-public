#!/usr/bin/env python3
"""Independently replay R552 original-fc point spaces and actual negative flips.

Uses the original bounded integer matrix arithmetic, without installing the
native/BLAS accelerators. It checks the two short executed prefixes, not an
unexecuted scalar chain or any local height.
"""
import argparse,gzip,hashlib,json,sys
from pathlib import Path
def read(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for n in ['script-dir','geometry','based-points','prefix-work','transports','output']:ap.add_argument('--'+n,type=Path,required=True)
 args=ap.parse_args();S=args.script_dir.resolve();D=S/'data';sys.path.insert(0,str(S))
 import numpy as np
 import p41_r2_matrix as r
 from p41_actual_differentials47 import ActualModel,digest
 from p41_projective_jet_frames47 import ProjectiveJetFrames
 from p41_formal47_multiply import point_hash
 assert not getattr(r.mm,'exact_nonnegative_float64',False)
 a=ActualModel(S);M=a.M;frames=ProjectiveJetFrames(a,exact_blas=False)
 cert=read(args.geometry);based=read(args.based_points);common=read(D/'p41_all19_based_points47.json.gz');atlas=read(D/'p41_rational_SS_residue_atlas47_complete.json.gz')
 assert cert['result']=='R552' and cert['based_points_sha256']==sha(args.based_points)
 assert based['source_sha256']==sha(S/'p41_SS_Abel_multiply47.py') and based['selected_disks']==['SS_j36_06','SS_j36_02']
 for name,h in a.inputs.items():assert based['input_sha256'][name]==h
 DB=r.from_json(common['colon_coordinates']);free=[i for i in range(199) if i not in {j-1 for j in common['colon_rank_columns_1based']}]
 assert r.equal(r.rows(DB,free),r.eye(74));fb=r.from_json(common['f_b_coefficients']);fbv=r.mm(M['W'],fb);assert np.all(r.units(fbv))
 constraints=[]
 for coeff in common['colon_test_section_coefficients']:
  ratio=r.mul(r.mm(M['W'],r.from_json(coeff)),r.inverse_values(fbv));scaled=r.mul(ratio,M['V2']);R=r.sub(scaled,r.mm(M['V2'],r.rows(scaled,M['P2'])));assert r.iszero(r.mm(R,DB));constraints.append(R)
 def unit_minor(X,rows,cols,n):
  Y=r.cols(r.rows(X,rows),cols);assert Y[0].shape==(n,n);Yp=tuple(c%47 for c in Y);inv=r.inverse_matrix(Yp,47);assert r.equal(r.mm(Yp,inv,47),r.eye(n))
 stacked=tuple(np.vstack([x[k] for x in constraints]) for k in range(2))
 unit_minor(stacked,[j-1 for j in common['colon_rank_rows_1based']],[j-1 for j in common['colon_rank_columns_1based']],125)
 WW=r.mul(M['W'],r.inverse_values(a.f));records=[];inputs={str(p):sha(p) for p in [args.geometry,args.based_points,D/'p41_all19_based_points47.json.gz',D/'p41_rational_SS_residue_atlas47_complete.json.gz',args.transports/'run_manifest47.json']}
 for disk in based['selected_disks']:
  p=next(x for x in based['records'] if x['disk_id']==disk);c=next(x for x in cert['records'] if x['disk_id']==disk);ar=next(x for x in atlas['SS_disk_records'] if x['disk_id']==disk);ch=atlas['charts'][ar['chart_0based']];row=ar['chart_row_0based']
  P=r.from_json([ch['W_coefficients_0to3'][0][row]]);assert r.equal(r.from_json(ch['frame']),a.fc) and r.equal(r.mm(P,a.fc),r.column([[1,0]]));assert np.all(r.units(r.mm(P,fb)))
  assert r.to_json(r.mm(P,fb))==c['actual_fb_value'] and r.to_json(r.mm(P,a.fc))==c['actual_fc_value']
  assert not np.any(np.all((WW[0]-P[0])%47==0,axis=1)&np.all((WW[1]-P[1])%47==0,axis=1))
  E=r.from_json(p['point_coordinates']);AE=r.from_json(p['point_frobenius']);assert point_hash(E,AE)==p['point_sha256']==c['point_sha256']
  assert r.equal(r.rows(E,[i-1 for i in p['normalization_rows_1based']]),r.eye(73)) and r.equal(E,r.mm(DB,r.rows(E,free)))
  J=frames.local_jets(P,r.from_json(ch['frame']),r.from_json(ch['coordinate']),order=2)
  assert [r.to_json(v) for v in J['W']]==c['actual_W_jets_0to2'] and [r.to_json(v) for v in J['V2']]==c['actual_V2_jets_0to2']
  VP=J['V2'][0];restriction=r.mm(VP,DB);assert np.any(r.units(restriction)) and r.to_json(restriction)==c['actual_V2_point_restriction']
  assert r.iszero(r.mm(VP,E)) and np.any(r.units(r.mm(J['V2'][1],E)))
  ES=r.mm(M['V2'],E);assert digest(r.to_json(ES))==c['actual_E_V2_values_sha256']
  for i,j in enumerate(c['all820_E_ideal_unit_witness_columns_0based']):assert r.units(ES)[i,j]
  assert r.equal(r.mm(E,AE),r.mm(M['A2'],r.conjugate(E))) and r.equal(r.mm(AE,r.conjugate(AE)),r.eye(73))
  mp=args.prefix_work/(disk+'_multiply47.json.gz');fp=args.transports/disk/('function_'+disk+'_initial_negative.json.gz');mult=read(mp);fun=read(fp);inputs[str(mp)]=sha(mp);inputs[str(fp)]=sha(fp)
  assert mult['input_sha256']==sha(args.based_points) and mult['input_point_sha256']==p['point_sha256'];assert mult['bits_done']==1 and mult['steps']==[]
  F=r.from_json(mult['negative_input_coordinates']);AF=r.from_json(mult['negative_input_frobenius']);witness=mult['negative_input_witness']
  assert F[0].shape==(199,73) and r.equal(r.mm(F,AF),r.mm(M['A2'],r.conjugate(F))) and r.equal(r.mm(AF,r.conjugate(AF)),r.eye(73))
  f=r.mm(E,r.column(witness['f_coefficients']));g=r.mm(E,r.column(witness['g_coefficients']));fv=r.mm(M['V2'],f);gv=r.mm(M['V2'],g);assert np.all(r.units(fv))
  assert fun['line_bundle_power']==2 and fun['numerator_coefficients']==r.to_json(f)
  assert fun['input_nodes']==[{'point_sha256':p['point_sha256'],'scalar_coefficient_of_C':1}]
  assert fun['output_node']=={'point_sha256':point_hash(F,AF),'scalar_coefficient_of_C':-1}
  ratio=r.mul(gv,r.inverse_values(fv));scaled=r.mul(ratio,M['V2']);RR=r.sub(scaled,r.mm(M['V2'],r.rows(scaled,M['P2'])))
  unit_minor(RR,[i-1 for i in witness['rank_rows_1based']],[i-1 for i in witness['rank_columns_1based']],126)
  assert r.iszero(r.mm(RR,F)) and r.equal(r.rows(F,[i-1 for i in witness['free_columns_1based']]),r.eye(73))
  FS=r.mm(M['V2'],F);assert np.all(np.any(r.units(FS),axis=1));qcoef=r.rows(r.mm(scaled,F),M['P2']);qvalues=r.mm(M['V2'],qcoef)
  assert r.equal(r.mul(fv,qvalues),r.mul(gv,FS))
  initial=r.mul(r.mm(P,fb),r.inverse_values(r.mm(P,a.fc)));assert r.to_json(initial)==c['initial_principal_function_value_at_P']
  records.append({'disk_id':disk,'actual_fc_value':c['actual_fc_value'],'actual_fb_value':c['actual_fb_value'],'complete_common_rank125_and_point_rank1_verified':True,'complete_V2_point_dimension':73,'all73_point_equations_and_simple_coarse_derivative':True,'all820_original_and_negative_divisor_unit_rows_verified':True,'initial_function':'f_b/f_c','initial_function_order_at_P':0,'initial_function_value_at_P':c['initial_principal_function_value_at_P'],'negative_flip_complete_rank126_verified':True,'all820_by73_negative_flip_global_cross_products':820*73,'saved_actual_V2_negative_function_sha256':sha(fp),'actual_prefix_bits':1,'scalar_double_or_add_operations_executed':0,'no_extra_initial_moving_flips':True})
  print('PASS independent bounded-integer CM4 initial geometry and actual negative flip',disk,flush=True)
 out={'result':'R552','complete_two_initial_geometry_and_prefix_independent_arithmetic_audit':True,'records':records,'input_sha256':dict(a.inputs,**inputs),'source_sha256':sha(__file__),'arithmetic':'Original bounded integer NumPy matrix arithmetic; no native or float-BLAS accelerators installed.','all_Abel_constants_complete':False,'local_heights_complete':False,'scope':'Two complete original-fc based spaces and both actually executed initial negative flips; no scalar-chain completion or local-height claim.'}
 args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('PASS R552 independent audit',sha(args.output),flush=True)
if __name__=='__main__':main()
