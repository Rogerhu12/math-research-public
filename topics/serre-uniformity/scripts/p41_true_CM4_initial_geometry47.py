#!/usr/bin/env python3
"""R552: actual original-fc based divisors on the two rational CM4 coarse disks.

The original R329 point constructor is called with every existing unit,
complete-colon and evaluation-separation assertion retained. No moving divisor
or new frame is introduced unless an actual assertion first demands one.
"""
import argparse,gzip,hashlib,json,sys,time
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for n in ['script-dir','work-dir','based-points','output']:ap.add_argument('--'+n,type=Path,required=True)
 args=ap.parse_args();S=args.script_dir.resolve();D=S/'data';W=args.work_dir.resolve();W.mkdir(parents=True,exist_ok=True);sys.path.insert(0,str(S))
 import p41_r2_matrix as r
 from p41_actual_differentials47 import ActualModel,save,digest
 from p41_projective_jet_frames47 import ProjectiveJetFrames,install_exact_float_mm
 from p41_native_r2_linear47 import install
 from p41_formal47_multiply import point_hash
 import p41_SS_Abel_multiply47 as frozen
 install_exact_float_mm(r);linear=install(r,W/'native');a=ActualModel(S);a.linear_manifest=linear;np=a.np;frames=ProjectiveJetFrames(a)
 atlas_path=D/'p41_rational_SS_residue_atlas47_complete.json.gz';common_path=D/'p41_all19_based_points47.json.gz'
 atlas=read(atlas_path);common=read(common_path);fb=r.from_json(common['f_b_coefficients']);DB=r.from_json(common['colon_coordinates'])
 ids=['SS_j36_06','SS_j36_02'];probes=[]
 WW=r.mul(a.M['W'],r.inverse_values(r.mm(a.M['W'],a.fc)))
 for d in ids:
  rec=next(x for x in atlas['SS_disk_records'] if x['disk_id']==d);ch=atlas['charts'][rec['chart_0based']];row=rec['chart_row_0based'];P=r.from_json([ch['W_coefficients_0to3'][0][row]])
  frame=r.from_json(ch['frame']);fcp=r.mm(P,a.fc);fbp=r.mm(P,fb)
  probes.append({'disk_id':d,'original_chart_0based':rec['chart_0based'],'original_chart_row_0based':row,'chosen_reference':rec['chosen_reference'],'original_frame_kind':ch['frame_kind'],'frame_equals_original_fc':r.equal(frame,a.fc),'actual_fc_value':r.to_json(fcp),'actual_fb_value':r.to_json(fbp),'fc_unit':bool(np.all(r.units(fcp))),'fb_unit':bool(np.all(r.units(fbp)))})
 probe=W/'actual_point_value_probe47.json';probe.write_text(json.dumps({'result':'R552','records':probes,'source_sha256':sha(__file__)},indent=2)+'\n')
 for row in probes:print('ACTUAL_POINT_VALUES',row,flush=True)
 # This exact frozen call keeps every original rank, unit and 820-row assertion.
 if args.based_points.exists():
  points=frozen.read(args.based_points);assert points['selected_disks']==ids and points['source_sha256']==sha(frozen.__file__)
 else:points=frozen.based_points(a,atlas_path,common_path,ids,args.based_points)
 assert points['complete_selected_SS_actual_based_points']
 records=[]
 for d,probe in zip(ids,probes):
  point=next(x for x in points['records'] if x['disk_id']==d);rec=next(x for x in atlas['SS_disk_records'] if x['disk_id']==d);ch=atlas['charts'][rec['chart_0based']];row=rec['chart_row_0based']
  P=r.from_json(point['actual_center_W_fc_normalized_mod47four']);assert r.equal(r.mm(P,a.fc),r.column([[1,0]]))
  E=r.from_json(point['point_coordinates']);AE=r.from_json(point['point_frobenius'])
  assert point_hash(E,AE)==point['point_sha256'] and E[0].shape==(199,73)
  J=frames.local_jets(P,r.from_json(ch['frame']),r.from_json(ch['coordinate']),order=2)
  assert r.equal(J['frame'],a.fc)
  for n in range(3):assert r.equal(J['W'][n],r.from_json([ch['W_coefficients_0to3'][n][row]]))
  V2P=J['V2'][0];restriction=r.mm(V2P,DB);rr,cc=r.rank_pivots(restriction);assert len(rr)==1
  assert r.iszero(r.mm(V2P,E)) and np.any(r.units(r.mm(J['V2'][1],E)))
  values=r.mm(a.M['V2'],E);assert np.all(np.any(r.units(values),axis=1))
  units=[int(np.flatnonzero(r.units(values)[i,:])[0]) for i in range(820)]
  assert r.equal(r.mm(E,AE),r.mm(a.M['A2'],r.conjugate(E))) and r.equal(r.mm(AE,r.conjugate(AE)),r.eye(73))
  hits=np.flatnonzero(np.all((WW[0]-P[0])%47==0,axis=1)&np.all((WW[1]-P[1])%47==0,axis=1)).tolist();assert hits==[]
  initial=r.mul(r.mm(P,fb),r.inverse_values(r.mm(P,a.fc)));assert np.all(r.units(initial))
  records.append(dict(probe,point_sha256=point['point_sha256'],original_V2_point_coordinates=point['point_coordinates'],point_frobenius=point['point_frobenius'],normalization_rows_1based=point['normalization_rows_1based'],actual_E_V2_values_sha256=digest(r.to_json(values)),all820_E_ideal_unit_witness_columns_0based=units,actual_V2_point_restriction=r.to_json(restriction),point_restriction_rank=1,common_colon_dimension=74,actual_point_space_dimension=73,all73_exact_point_vanishing_equations=True,simple_point_in_coarse_parameter=True,actual_V2_derivative_at_P_on_all73_basis=r.to_json(r.mm(J['V2'][1],E)),actual_W_jets_0to2=[r.to_json(v) for v in J['W']],actual_V2_jets_0to2=[r.to_json(v) for v in J['V2']],frame=r.to_json(J['frame']),coordinate=r.to_json(J['coordinate']),complete_point_space_Frobenius_compatible=True,all820_evaluation_rows_disjoint_mod47=True,actual_source_matching_rows_0based=hits,initial_principal_function='f_b/f_c',initial_principal_function_order_at_P=0,initial_principal_function_value_at_P=r.to_json(initial),actual_divisor_relation='E_P=div(f_b)-b+P; E_P-L=C+div(f_b/f_c)',additional_moving_flips_required=False))
  print('PASS actual original-fc complete V2 based geometry',d,'fb(P)',probe['actual_fb_value'],'rank1 / dim73; original820 disjoint',flush=True)
 out={'result':'R552','level':41,'auxiliary_prime':47,'precision':4,'modulus':r.Q,'disk_ids':ids,'complete_actual_two_original_fc_based_geometries':True,'no_extra_moving_divisor_or_frame_change_required':True,'all_original_R329_unit_rank_and_evaluation_separation_assertions_retained':True,'original_common_degree125_divisor_reused':True,'f_b_coefficients':common['f_b_coefficients'],'f_c_coefficients':r.to_json(a.fc),'records':records,'based_points_sha256':sha(args.based_points),'input_sha256':dict(a.inputs,**{atlas_path.name:sha(atlas_path),common_path.name:sha(common_path),args.based_points.name:sha(args.based_points)}),'dependency_sources_sha256':{Path(frozen.__file__).name:sha(frozen.__file__),'p41_projective_jet_frames47.py':sha(S/'p41_projective_jet_frames47.py')},'source_sha256':sha(__file__),'all_Abel_constants_complete':False,'local_heights_complete':False,'scope':'Only actual initial based divisors and original coarse-chart point conditions; no304-bit completion or new local-height claim.'}
 print('PASS R552',save(args.output,out),flush=True)
if __name__=='__main__':main()
