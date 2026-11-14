#!/usr/bin/env python3
"""Actual CM(-28) point, five CM SS disk deduplication, and all53 reciprocal anchors."""
import argparse,gzip,json,sys
from pathlib import Path
from p41_CM27_SS_anchor47 import Q,Q3,read,sha,mul,dot,inv,fieldmul,globalvalue

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','v-anchor','output']:ap.add_argument('--'+k,type=Path,required=True)
 args=ap.parse_args();data=args.script_dir.resolve()/'data';inputs={}
 def load(p):inputs[str(p)]=sha(p);return read(p)
 targets=load(data/'p41_t2_cm_targets47_verified.json.gz');c7=load(data/'p41_cm7_q2_support47_verified.json.gz');rawcm=load(data/'p41_cm_quadratic_jets47_raw.json.gz')
 for n,h in targets['source_sha256'].items():assert sha(data/n)==h
 for n,h in targets['verification_source_sha256'].items():assert sha(args.script_dir/n)==h
 assert 'independent' in targets['status'] and 'independent' in c7['status']
 target=next(r for r in targets['records'] if r['label']=='CM28');assert target['j_mod47four']==16581375%Q
 sourcecase=next(r for r in targets['cases'] if r[0]=='CM28');assert sourcecase[1:3]==[-35,-98] and sourcecase[6]==7
 A,B=target['curve_A'],target['curve_B'];assert A==(-35-5*(3*7**2-35))%Q and B==(-98-7*(5*7**3+3*(-35)*7+2*(-98)))%Q
 assert 6912*A**3*pow((4*A**3+27*B**2)%Q,-1,Q)%Q==16581375%Q
 atlas=load(data/'p41_rational_SS_residue_atlas47_complete.json.gz');known=load(data/'p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz');tiny=load(data/'p41_all129_tiny_Abel47_complete.json.gz');globals=load(data/'p41_global_qc_polynomials47_complete.json.gz');vanchor=load(args.v_anchor)
 def locate(W):
  matches=[]
  for chart in atlas['charts']:
   frame=[r[0] for r in chart['frame']];fv=dot(W,frame)
   if (fv[0]*fv[0]+fv[1]*fv[1])%47==0:continue
   Wp=[list(mul(x,inv(fv))) for x in W]
   for row,disk in enumerate(chart['disk_ids']):
    if not all(all((a-b)%47==0 for a,b in zip(x,y)) for x,y in zip(Wp,chart['W_coefficients_0to3'][0][row])):continue
    coordinate=[r[0] for r in chart['coordinate']];zz=dot(Wp,coordinate);assert zz[1]==0
    z=(zz[0]-chart['rational_coordinate_at_center_mod47four'][row])%Q;assert z%47==0
    recovered=[[sum(chart['W_coefficients_0to3'][k][row][j][p]*pow(z,k,Q) for k in range(4))%Q for p in range(2)] for j in range(73)]
    assert recovered==Wp
    matches.append((chart,row,disk,z,Wp))
  assert len(matches)==1,[(x[2],x[3]) for x in matches]
  return matches[0]
 W=target['weight2_values'][0];chart,row,disk,z,Wp=locate(W);y=z//47
 oldW=next(r for r in rawcm['records'] if r['label']=='CM28')['normalized_weight2_coefficients'][0]
 if len(oldW)==1:oldW=oldW[0]
 assert locate(oldW)[2:4]==(disk,z)
 j=16581375;component=j%41;assert component==32
 rw=[];r3=[];fields=[];F2=next(r for r in globals['directions'] if r['n']==2)
 for field,F in zip(globals['fields'],F2['F_field_coefficients_ascending_mod47four']):
  T=[x*pow(27,-1,Q)%Q for x in F];T[0]=(T[0]-4*pow(27,-1,Q))%Q
  Tminus2=list(T);Tminus2[0]=(Tminus2[0]-2)%Q
  rr=fieldmul(Tminus2,field['r_minus7'],field['factor_descending']);left=fieldmul(T,field['r_minus7'],field['factor_descending']);assert left==[(2*x+y)%Q for x,y in zip(field['r_minus7'],rr)]
  rw+=rr;r3+=field['r_minus3'];fields.append({'factor_descending':field['factor_descending'],'T2_ascending_mod47four':T,'r_w_ascending_mod47four':rr,'T2_r_minus7_equals2r_minus7_plus_r_w':True})
 aw=[(x-y)*pow(20,-1,Q3)%Q3 for x,y in zip(rw,r3)];assert len(aw)==54
 center=next(c for c in known['actual_113_rational_disk_global_polynomials'] if c['disk_id']==disk);tc=next(c for c in tiny['charts'] if disk in c['disk_ids']);ti=tc['disk_ids'].index(disk);assert tc['origin_chart_0based']==chart['chart_0based']
 delta=[sum(tc['cyclic_coordinate_tiny_coefficients_1to3_in_y_mod47cubed'][k-1][ti][c]*pow(y,k,Q3) for k in range(1,4))%Q3 for c in range(54)]
 assert [(x+d)%Q3 for x,d in zip(center['actual_center_C_cyclic_coordinates_mod47cubed'],delta)]==aw
 labels=globals['component_order'];assert labels==[0,3,28,32];ci=labels.index(component);heights=[]
 for direction in globals['directions']:
  value=globalvalue(direction,aw);polynomial=next(p for p in center['global_polynomials'] if p['n']==direction['n'])['coefficients_0to4_in_y_mod47four'];assert value==sum(c*pow(y,k,Q) for k,c in enumerate(polynomial))%Q
  targetv=direction['QC_defect_targets_by_component_order'][ci];scaled=(value-targetv)%Q
  heights.append({'n':direction['n'],'global_value_mod47four':value,'same_component_QC_target_mod47four':targetv,'scaled_by800_local_height_mod47four':scaled,'canonical_local_sigma_height_mod47four':scaled*pow(800,-1,Q)%Q})
 dedup=[]
 for label,disc,jj in [('P_minus3',-3,0),('P_minus12',-12,54000),('P_minus7',-7,-3375),('CM28',-28,16581375)]:
  ww=next(r for r in rawcm['records'] if r['label']==label)['normalized_weight2_coefficients'][0]
  if len(ww)==1:ww=ww[0]
  ch,ro,di,zz,pp=locate(ww);dedup.append({'label':label,'discriminant':disc,'j_integer':jj,'bad_component_at41':jj%41,'disk_id':di,'atlas_chart_0based':ch['chart_0based'],'atlas_row_0based':ro,'actual_original_chart_z_mod47four':zz,'actual_original_y_mod47cubed':zz//47,'all73_original_chart_transport_verified':True})
 vc,vr,vd,vz,vp=locate(vanchor['actual_fc_normalized_W_mod47four']);assert vd==vanchor['disk_id'] and vz==vanchor['actual_original_chart_z_mod47four'];dedup.append({'label':'v_minus27','discriminant':-27,'j_integer':-12288000,'bad_component_at41':28,'disk_id':vd,'atlas_chart_0based':vc['chart_0based'],'atlas_row_0based':vr,'actual_original_chart_z_mod47four':vz,'actual_original_y_mod47cubed':vz//47,'all73_original_chart_transport_verified':True})
 assert len({r['disk_id'] for r in dedup})==5
 # Use the original canonical section, independently built from the published cusp kernel.
 sys.path.insert(0,str(args.script_dir.resolve()))
 from p41_actual_differentials47 import ActualModel
 from p41_projective_jet_frames47 import install_exact_float_mm
 import p41_r2_matrix as r
 install_exact_float_mm(r);a=ActualModel(args.script_dir,derivatives=False);inputs.update(a.inputs)
 Wmat=r.from_json([W]);fcvalue=r.mm(Wmat,a.fc);assert bool(r.units(fcvalue)[0,0]);Wfc=r.mul(Wmat,r.inverse_values(fcvalue))
 assert r.equal(r.mm(r.conjugate(Wfc),r.conjugate(a.M['A1'])),Wfc)
 assert r.equal(r.mul(r.from_json([oldW]),r.inverse_values(r.mm(r.from_json([oldW]),a.fc))),Wfc)
 inputs[str(Path(__file__).resolve().parent/'p41_CM27_SS_anchor47.py')]=sha(Path(__file__).resolve().parent/'p41_CM27_SS_anchor47.py')
 out={'result':'R314','discriminant':-28,'j_integer':j,'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'disk_id':disk,'bad_component_at41':component,'complete_actual_CM_point_and_all53_height_anchors':True,'point_source':'Published independently verified actual CM28 nonself T2 image of c7; no new torsion computation','actual_elliptic_model_mod47four':[A,B],'actual_source_kernel_x':7,'source_CM7_necklace_index_1based':c7['fixed_necklace_indices_1based'][0],'actual_target_necklace_index_1based':target['necklace_index_1based'],'actual_target_frobenius_torsion_matrix':target['frobenius_torsion_matrix'],'exact_Jacobian_class_formula':'U_w=(T2-2)U_minus7; C_w=(U_w-U_minus3)/20','fields':fields,'actual_U_w_cyclic_coordinates_mod47four':rw,'actual_C_w_cyclic_coordinates_mod47cubed':aw,'actual_fc_normalized_W_mod47four':r.to_json(Wfc)[0],'actual_W_in_original_SS_atlas_frame_mod47four':Wp,'atlas_chart_0based':chart['chart_0based'],'atlas_row_0based':row,'frame':chart['frame'],'coordinate':chart['coordinate'],'actual_original_chart_z_mod47four':z,'actual_original_y_mod47cubed':y,'all73_actual_point_coordinates_recovered_from_original_chart':True,'all54_exact_Hecke_class_coordinates_equal_actual_SS_constant_plus_tiny':True,'all53_global_values_match_actual_disk_polynomial_evaluation':True,'five_rational_CM_SS_points_in_distinct_disks':dedup,'all53_local_height_anchors_by_global_reciprocity':heights,'anchor_method':'Exact rational CM point plus proven global heights and fixed bad label; no independent local Norm claim','complete_local_disk_QC_heights':False,'complete_common_roots':False,'input_sha256':inputs,'source_sha256':sha(__file__)}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(gzip.compress((json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0));print('PASS true CM28 SS anchor',disk,'z',z,'y',y,'component',component,'F2 height',heights[0]['canonical_local_sigma_height_mod47four'],'SHA',sha(args.output));print('PASS five CM SS disks',[(r['label'],r['disk_id']) for r in dedup])
if __name__=='__main__':main()
