#!/usr/bin/env python3
"""Exact original atlas coordinates and all53 reciprocal anchors at b,u,c7."""
import argparse,gzip,json
from pathlib import Path
from p41_CM27_SS_anchor47 import Q,Q3,read,sha,mul,dot,inv,globalvalue

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--script-dir',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();data=args.script_dir.resolve()/'data';inputs={}
 def load(n):p=data/n;inputs[n]=sha(p);return read(p)
 raw=load('p41_cm_quadratic_jets47_raw.json.gz');atlas=load('p41_rational_SS_residue_atlas47_complete.json.gz');tiny=load('p41_all129_tiny_Abel47_complete.json.gz');known=load('p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz');globaldata=load('p41_global_qc_polynomials47_complete.json.gz');r3=sum((f['r_minus3'] for f in globaldata['fields']),[]);records=[]
 for label,disc,j,fieldkey in [('P_minus3',-3,0,'r_minus3'),('P_minus12',-12,54000,'r_minus12'),('P_minus7',-7,-3375,'r_minus7')]:
  W=next(r for r in raw['records'] if r['label']==label)['normalized_weight2_coefficients'][0]
  if len(W)==1:W=W[0]
  matches=[]
  for ch in atlas['charts']:
   fr=[x[0] for x in ch['frame']];f=dot(W,fr)
   if (f[0]*f[0]+f[1]*f[1])%47==0:continue
   Wp=[list(mul(x,inv(f))) for x in W]
   for row,disk in enumerate(ch['disk_ids']):
    if not all(all((a-b)%47==0 for a,b in zip(x,y)) for x,y in zip(Wp,ch['W_coefficients_0to3'][0][row])):continue
    zz=dot(Wp,[x[0] for x in ch['coordinate']]);assert zz[1]==0;z=(zz[0]-ch['rational_coordinate_at_center_mod47four'][row])%Q;assert z%47==0
    reproduced=[[sum(ch['W_coefficients_0to3'][k][row][i][part]*pow(z,k,Q) for k in range(4))%Q for part in range(2)] for i in range(73)];assert reproduced==Wp;matches.append((ch,row,disk,z,Wp))
  assert len(matches)==1;ch,row,disk,z,Wp=matches[0];y=z//47;ru=sum((f[fieldkey] for f in globaldata['fields']),[]);aa=[(x-z)*pow(20,-1,Q3)%Q3 for x,z in zip(ru,r3)];center=next(r for r in known['actual_113_rational_disk_global_polynomials'] if r['disk_id']==disk);tc=next(c for c in tiny['charts'] if disk in c['disk_ids']);tr=tc['disk_ids'].index(disk);assert tc['origin_chart_0based']==ch['chart_0based']
  delta=[sum(tc['cyclic_coordinate_tiny_coefficients_1to3_in_y_mod47cubed'][k-1][tr][i]*pow(y,k,Q3) for k in range(1,4))%Q3 for i in range(54)];assert [(x+d)%Q3 for x,d in zip(center['actual_center_C_cyclic_coordinates_mod47cubed'],delta)]==aa
  component=j%41;ci=globaldata['component_order'].index(component);heights=[]
  for direction in globaldata['directions']:
   val=globalvalue(direction,aa);gp=next(v for v in center['global_polynomials'] if v['n']==direction['n'])['coefficients_0to4_in_y_mod47four'];assert val==sum(c*pow(y,k,Q) for k,c in enumerate(gp))%Q;target=direction['QC_defect_targets_by_component_order'][ci];scaled=(val-target)%Q;heights.append({'n':direction['n'],'global_value_mod47four':val,'same_component_QC_target_mod47four':target,'scaled_by800_local_height_mod47four':scaled,'canonical_local_sigma_height_mod47four':scaled*pow(800,-1,Q)%Q})
  records.append({'label':label,'discriminant':disc,'j_integer':j,'disk_id':disk,'bad_component_at41':component,'actual_U_cyclic_coordinates_mod47four':ru,'actual_C_cyclic_coordinates_mod47cubed':aa,'actual_raw_CM_W_mod47four':W,'actual_W_in_original_SS_atlas_frame_mod47four':Wp,'atlas_chart_0based':ch['chart_0based'],'atlas_row_0based':row,'frame':ch['frame'],'coordinate':ch['coordinate'],'actual_original_chart_z_mod47four':z,'actual_original_y_mod47cubed':y,'all73_true_point_original_chart_transport_verified':True,'all54_exact_class_equal_actual_SS_constant_plus_tiny':True,'all53_true_point_global_pairing_matches_original_disk_polynomial':True,'all53_local_height_anchors_by_global_reciprocity':heights})
  print('PASS true CM anchor',label,disk,'y',y,'label',component,'F2',heights[0]['canonical_local_sigma_height_mod47four'],flush=True)
 assert len({r['disk_id'] for r in records})==3
 b=next(r for r in records if r['label']=='P_minus3');assert not any(b['actual_C_cyclic_coordinates_mod47cubed']);assert all(h['canonical_local_sigma_height_mod47four']==0 for h in b['all53_local_height_anchors_by_global_reciprocity'])
 inputs['p41_CM27_SS_anchor47.py']=sha(Path(__file__).with_name('p41_CM27_SS_anchor47.py'))
 out={'result':'R321','level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'records':records,'all_three_actual_CM_point_and_53_height_anchors_complete':True,'scope':'Known rational CM point reciprocity anchors and original point transport only; no full-disk local height asserted.','input_sha256':inputs,'source_sha256':sha(__file__)}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(gzip.compress((json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0));print('PASS all three basic SS anchors SHA',sha(args.output))
if __name__=='__main__':main()
