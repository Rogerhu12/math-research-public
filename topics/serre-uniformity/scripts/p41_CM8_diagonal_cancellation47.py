#!/usr/bin/env python3
"""Actual CM(-8) level branches and chart divided differences for joint Norm cancellation.

This certifies the algebraic unit that replaces the cancelling nonunit
Weierstrass factors. It does not execute a new scalar chain or assign a
height constant on either special disk.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
from types import SimpleNamespace


def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def j_coefficients(a,invariants,W):
 from p41_elliptic_coarse_atlas47 import Series
 r=a.r;S=Series(a,len(W));iv=invariants.series(W)
 A3v3=S.mul(S.power(iv['Av'],3),S.power(iv['v'],3))
 denominator=S.add(S.scale(A3v3,4),S.scale(S.power(iv['Bv3'],2),27))
 assert a.np.all(r.units(denominator[0])), 'The chosen invariant denominator is not a unit; an actual alternative frame is required.'
 return S.scale(S.mul(A3v3,S.inverse(denominator)),6912)


def divided_difference(a,frames,invariants,WX,WP,frame,coordinate,jets=None):
 """Compute (j(P)-j(X))/(z(P)-z(X)) as an integral power series, not a p-division."""
 r,np=a.r,a.np
 assert np.all(r.units(r.mm(WP,frame))) and np.all(r.units(r.mm(WX,frame)))
 WX=r.mul(WX,r.inverse_values(r.mm(WX,frame)));WP=r.mul(WP,r.inverse_values(r.mm(WP,frame)))
 J=jets if jets is not None else frames.local_jets(WX,frame,coordinate,order=4)
 assert len(J['W'])>=5 and r.equal(J['W'][0],WX)
 zeta=r.sub(r.mm(WP,coordinate),r.mm(WX,coordinate));assert all(not np.any(x%47) for x in zeta)
 recovered=r.zeros(1,73)
 for coeff in reversed(J['W'][:5]):recovered=r.add(r.mul(recovered,zeta),coeff)
 assert r.equal(recovered,WP)
 jj=j_coefficients(a,invariants,J['W'][:5]);assert np.all(r.units(jj[1]))
 D=r.zeros(1,1)
 for coeff in reversed(jj[1:]):D=r.add(r.mul(D,zeta),coeff)
 assert np.all(r.units(D))
 source_j=j_coefficients(a,invariants,[WP])[0]
 assert r.equal(r.add(jj[0],r.mul(zeta,D)),source_j)
 return {'W_center':r.to_json(WX),'W_source_in_same_frame':r.to_json(WP),'frame':r.to_json(frame),'coordinate':r.to_json(coordinate),
         'source_coordinate_displacement':r.to_json(zeta),'W_coefficients_0to4':[r.to_json(x) for x in J['W'][:5]],
         'j_coefficients_0to4':[r.to_json(x) for x in jj],
         'j_source_mod47four':r.to_json(source_j),'j_divided_difference_unit_mod47four':r.to_json(D),
         'all73_source_coordinates_recovered_in_same_chart':True,'unit_obtained_without_dividing_by_47':True}


def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','work-dir','support06','support18','horizontal-unit','output']:ap.add_argument('--'+k,type=Path,required=True)
 args=ap.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
 from p41_actual_differentials47 import ActualModel,save
 from p41_projective_jet_frames47 import ProjectiveJetFrames,install_exact_float_mm
 from p41_native_r2_linear47 import install
 from p41_elliptic_coarse_atlas47 import ClassicalInvariants
 from p41_miller_unit_atlas47 import mul,inv,log_unit
 import p41_r2_matrix as r
 install_exact_float_mm(r);install(r,args.work_dir/'native');a=ActualModel(folder);frames=ProjectiveJetFrames(a);np=a.np
 D=folder/'data';paths=[D/'p41_rational_SS_residue_atlas47_complete.json.gz',D/'p41_cm_quadratic_jets47_raw.json.gz',D/'p41_cleared_serre_derivative47_complete.json.gz',args.support06,args.support18,args.horizontal_unit]
 atlas,cm,derivative,s06,s18,unit=[read(p) for p in paths]
 invariants=ClassicalInvariants(SimpleNamespace(a=a,r=r,v=r.from_json(derivative['chosen_clearing_section']),G=r.from_json(derivative['cleared_derivative_coefficients'])))
 assert unit['formal_t_factor_removed_before_evaluation'] and unit['horizontal_derivative_in_j_at_CM8']==-1
 records=[]
 for support,label in [(s06,'Z_minus8_679'),(s18,'Z_minus8_16')]:
  disk=support['source_disk_id'];ch=next(x for x in atlas['charts'] if disk in x['disk_ids']);row=ch['disk_ids'].index(disk)
  frame=r.from_json(ch['frame']);coordinate=r.from_json(ch['coordinate']);assert r.equal(frame,a.fc)
  WP=r.from_json([support['actual_source_W_fc_normalized']]);assert r.equal(WP,r.rows(r.from_json(ch['W_coefficients_0to3'][0]),[row]))
  raw=next(x for x in cm['records'] if x['label']==label);WC=r.from_json([raw['normalized_weight2_coefficients'][0]])
  assert r.equal(r.mm(WC,a.fc),r.column([[1,0]])) and r.equal(r.mm(WC,a.M['A1']),r.conjugate(WC))
  assert all(not np.any((x-y)%47) for x,y in zip(WC,WP))
  branches=support['same_source_residue_disk_target_branches_0based'];assert len(branches)==1
  br=branches[0];record=support['branch_records'][br];WT=r.from_json([record['W_actual_values_in_R2']])
  assert record['target_vertex_0based']==support['source_vertex_0based'] and record['actual_saved_full_level_record']['determinant_mod41']==2
  assert r.equal(r.mm(WT,a.M['A1']),r.conjugate(WT))
  assert support['no_actual_target_equals_source_mod47four'] and not r.equal(WT,WP)
  charts={name:divided_difference(a,frames,invariants,W,WP,frame,coordinate) for name,W in [('CM8_fixed',WC),('horizontal_target',WT)]}
  scalar=lambda raw:tuple(raw[0][0])
  jcm=scalar(charts['CM8_fixed']['j_coefficients_0to4'][0]);jt=scalar(charts['horizontal_target']['j_coefficients_0to4'][0]);js=scalar(charts['CM8_fixed']['j_source_mod47four'])
  assert jcm==(8000,0) and js==(unit['source_j_mod47four'],0)
  assert jt==(unit['independent_six_digit_Newton_checks'][0]['target_j_mod47six']%r.Q,0)
  assert scalar(charts['horizontal_target']['j_source_mod47four'])==js
  dc,dt=[scalar(charts[k]['j_divided_difference_unit_mod47four']) for k in ['CM8_fixed','horizontal_target']]
  common=mul((unit['U_mod47four'],0),mul(dc,inv(dt)))
  logcommon=log_unit(common)
  assert common[1]==logcommon[1]==0
  records.append({'disk_id':disk,'exact_CM8_label':label,'source_vertex_0based':support['source_vertex_0based'],'actual_same_disk_branch_0based':br,
   'source_W_fc_normalized':r.to_json(WP),'actual_CM8_W_fc_normalized':r.to_json(WC),'actual_horizontal_target_W_fc_normalized':r.to_json(WT),
   'CM8_point_and_horizontal_target_are_actual_Frobenius_fixed':True,'actual_CM8_j_is_8000':True,
   'same_level_branch_fixes_exact_CM8_point_by_unit_j_Hensel_uniqueness':True,'charts':charts,
   'actual_j_horizontal_ratio_unit_mod47four':unit['U_mod47four'],'combined_distinguished_chart_ratio_unit_mod47four':common,
   'combined_distinguished_chart_ratio_log_mod47four':logcommon,
   'combined_log_formula':'27*(log U_Phi(T)-log U_Phi(CM8))+27*m*log(U_j*D_CM8/D_T), where D_X=(j(P)-j(X))/(z(P)-z(X)) is computed by the integral divided difference.',
   'no_four_digit_nonunit_quotient_used':True,'actual_chain_or_height_complete':False})
  print('PASS actual CM8 diagonal joint unit',disk,'branch',br,'jT',jt[0],'Uchart',common[0],'log',logcommon[0],flush=True)
 out={'result':'R367','level':41,'auxiliary_prime':47,'modulus':r.Q,'precision':4,
  'complete_two_actual_CM8_diagonal_level_and_unit_cancellations':True,'records':records,
  'algebraic_horizontal_unit':unit,'input_sha256':dict(a.inputs,**{str(p):sha(p) for p in paths}),
  'source_sha256':sha(__file__),'complete_actual_local_heights':False,
  'scope':'Actual true level branch and full-precision unit interface for cancelling the matching CM(-8) zero factors; no scalar chain, principal Norm or height on these disks has been newly executed.'}
 print('PASS complete actual joint CM8 geometric cancellation',save(args.output,out),flush=True)
if __name__=='__main__':main()
