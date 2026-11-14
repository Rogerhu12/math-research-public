#!/usr/bin/env python3
"""Assemble a true CM8-collision F2 disk from actual principal center and Laurent differential."""
import argparse,gzip,hashlib,json
from pathlib import Path
from math import comb
P,Q,q=47,47**4,47**3
def read(p):
 p=Path(p);return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 b=gzip.compress((json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0);Path(p).write_bytes(b);return hashlib.sha256(b).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','center','difference','branches','abel','multiply','output']:ap.add_argument('--'+k,type=Path,required=True)
 args=ap.parse_args();inputs={}
 def load(p):inputs[str(p)]=sha(p);return read(p)
 def standard(n):return load(args.script_dir/'data'/n)
 center=load(args.center);diff=load(args.difference);br=load(args.branches);ab=load(args.abel);mult=load(args.multiply)
 disk=center['disk_id'];assert all(x['disk_id']==disk for x in [diff,br,ab,mult])
 assert center['complete_actual_local_sigma_F2_center_height']
 assert diff['complete_actual_local_sigma_F2_differential_and_height_difference'] and not diff['actual_height_constant_computed']
 assert not diff['CM_global_reciprocity_anchor_used']
 branch_hashes=[v for k,v in diff['input_sha256'].items() if Path(k).name==args.branches.name]
 assert branch_hashes and set(branch_hashes)=={sha(args.branches)}
 assert br['source_original_y_mod47cubed']==diff['source_CM_original_y_mod47cubed']
 difference=diff['actual_F2_height_difference_from_original_center_coefficients_0to3_in_y_mod47four'];assert difference[0]==0
 ycm=diff['source_CM_original_y_mod47cubed']
 dcoeff=[x[0][0][0] for x in diff['local_differential_coefficients_0to2_in_x_mod47cubed']]
 hw=[0]+[x*47**(k+1)*pow(k+1,-1,Q)%Q for k,x in enumerate(dcoeff)]
 assert hw==diff['actual_F2_height_difference_from_CM_coefficients_0to3_in_w_mod47four']
 shifted=[sum(comb(n,k)*hw[n]*pow(-ycm,n-k,Q) for n in range(k,4))%Q for k in range(4)]
 assert difference==[0]+shifted[1:]
 hp=[center['actual_local_sigma_F2_height_mod47four']]+difference[1:]
 holo=standard('p41_all129_tiny_Abel47_complete.json.gz');globaldata=standard('p41_global_qc_polynomials47_complete.json.gz')
 known=standard('p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz')
 atlas=standard('p41_rational_SS_residue_atlas47_complete.json.gz')
 old=standard('p41_abel_coordinates_and_tiny47_complete.json.gz')
 assert holo['input_sha256']['p41_abel_coordinates_and_tiny47_complete.json.gz']==sha(args.script_dir/'data/p41_abel_coordinates_and_tiny47_complete.json.gz')
 assert old['input_sha256']['p41_rational_SS_residue_atlas47_complete.json.gz']==sha(args.script_dir/'data/p41_rational_SS_residue_atlas47_complete.json.gz')
 hc=next(x for x in holo['charts'] if disk in x['disk_ids']);hi=hc['disk_ids'].index(disk)
 ac=next(x for x in atlas['charts'] if disk in x['disk_ids'])
 assert ac['coordinate']==br['source_coordinate'] and ac['frame']==br['source_frame']
 assert hc['origin']=='R230_SS' and hc['origin_chart_0based']==ac['chart_0based'] and hc['disk_ids']==ac['disk_ids']
 assert ab['complete_actual_center_Abel_constant'] and ab['input_sha256'][args.multiply.name]==sha(args.multiply)
 assert ab['input_sha256']['p41_all129_tiny_Abel47_complete.json.gz']==sha(args.script_dir/'data/p41_all129_tiny_Abel47_complete.json.gz')
 assert mult['bits_done']==mult['target_bits']==304 and mult['point_sha256']==ab['actual_multiple_point_sha256']
 aa=[ab['actual_center_C_cyclic_coordinates_mod47cubed']]+[x[hi] for x in hc['cyclic_coordinate_tiny_coefficients_1to3_in_y_mod47cubed']]
 kr=next(x for x in known['actual_113_rational_disk_global_polynomials'] if x['disk_id']==disk)
 assert aa[0]==kr['actual_center_C_cyclic_coordinates_mod47cubed']
 F=next(x for x in globaldata['directions'] if x['n']==2);assert F['F_Tn_coefficient']==27 and F['F_identity_coefficient']==4
 based=F['based_C'];gp=[0]*7
 assert all(v%47==0 for v in based['linear_vector_mod47four'])
 for k in range(4):gp[k]+=sum(u*v for u,v in zip(based['linear_vector_mod47four'],aa[k]))
 gp[0]+=based['constant_mod47four'];off=0
 for block in based['quadratic_blocks_mod47four']:
  n=len(block);assert all(v%47==0 for row in block for v in row)
  for k in range(4):
   for ell in range(4):gp[k+ell]+=sum(aa[k][off+i]*block[i][j]*aa[ell][off+j] for i in range(n) for j in range(n))
  off+=n
 assert off==54;gp=[v%Q for v in gp];assert gp[5:]==[0,0];gp=gp[:5]
 assert gp==next(x for x in kr['global_polynomials'] if x['n']==2)['coefficients_0to4_in_y_mod47four']
 qc=[(v-800*(hp[k] if k<4 else 0))%Q for k,v in enumerate(gp)]
 assert all(v%47==0 for v in qc)
 divided=[v//47 for v in qc];reduction=[v%47 for v in divided]
 roots=[t for t in range(47) if sum(c*pow(t,k,47) for k,c in enumerate(reduction))%47==0]
 lifts=[]
 for root in roots:
  derivative=sum(k*c*pow(root,k-1,47) for k,c in enumerate(divided) if k)%47;assert derivative
  y=root;mod=47;digits=[root]
  for _ in range(2):
   nm=mod*47;v=sum(c*pow(y,k,nm) for k,c in enumerate(divided))%nm;assert v%mod==0
   digit=-(v//mod)*pow(derivative,-1,47)%47;y+=mod*digit;mod=nm;digits.append(digit)
  assert sum(c*pow(y,k,Q) for k,c in enumerate(qc))%Q==0
  lifts.append({'y_mod47cubed':y,'z_mod47four':47*y,'y_base47_digits':digits,'derivative_mod47':derivative})
 index=globaldata['direction_indices'].index(2);labels=globaldata['component_order']
 targets=[row['QC_defect_target_mod47four'][index] for row in globaldata['component_vectors']];assert labels==[0,3,28,32] and targets==[0,0,0,0]
 out={'result':center['result'],'disk_id':disk,'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,
  'complete_actual_local_sigma_F2_polynomial_on_disk':True,
  'canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four':hp,
  'actual_original_center_height_from_principal_Norm':hp[0],
  'height_difference_from_exact_joint_Laurent_connection':difference,
  'actual_cyclic_C_coefficients_0to3_in_y_mod47cubed':aa,
  'global_F2_coefficients_0to4_in_y_mod47four':gp,
  'actual_QC_F2_coefficients_0to4_in_y_mod47four':qc,
  'QC_divided_by47_reduction_coefficients_mod47':reduction,'residual_QC_roots':roots,
  'simple_single_F2_root_candidates_to_available_precision':lifts,
  'bad_component_labels':labels,'F2_bad_targets_in_same_component_order':targets,
  'all_four_bad_components_have_same_F2_roots':True,
  'entire_disk_excluded_for_all_four_bad_components':not roots,
  'CM8_point_used_only_for_parameter_and_pole_cancellation':True,
  'no_CM_global_reciprocity_anchor_used':True,
  'complete_all53_local_QC_heights':False,'complete_common_roots':not roots,
  'tail_bound':diff['tail_bound'],
  'global_tail_bound':'Each global quadratic and linear coefficient is divisible by47; discarded Abel terms and total degrees>=5 vanish modulo47^4.',
  'input_sha256':inputs,'source_sha256':sha(__file__)}
 digest=save(args.output,out)
 print('PASS actual CM8-collision F2 full disk',disk,'height',hp,'QC/47',reduction,'roots',lifts,'SHA',digest,flush=True)
if __name__=='__main__':main()
