#!/usr/bin/env python3
"""True cell12 near-singleton endpoint kernels by constant-logr comparison.

Use all1873 original panels. In t=log(r), bound the original cooperative
canonical generator pointwise by one constant nonnegative matrix per
panel, then use its exact cosh/sinh exponential. No Peano-product<1 gate
is needed for this different proven comparison. Current-panel sources
pay the entire positive suffix; only incoming state receives strip loss.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted),2026-11-13.
"""
import argparse,json,resource,sys,time
from pathlib import Path
from fractions import Fraction as F
B=Path('/workspace/scratch/d1aa462cfc02');G=B/'geometry-work';HELP=G/'computations'
sys.path.insert(0,str(HELP))
from flint import arb,ctx
from closure_split_joint_io_v2 import iter_array,metadata_without_array
from inner_true_cell13_endpoint_window_kernels import sha,read,exact,ab,pack,up,lower_pack,Gates,MATERIALS
from inner_cell12_canonical_forced_endpoint_kernels_v2 import PINS,SOURCE_PINS
MODES=list(range(94,185,2))
FIXED={
 'base':(G/'inner-cell12-canonical-forced-r1/r2-kernels.json','5e03915b960e6ebdfa6847d155a82af5e54866e2bd0fde3e177815d7ea821133'),
 'base_resource':(G/'inner-cell12-canonical-forced-r1/r2-resource.json','d3cccd1b2087bbe2cdef501dff641063677000bbf4a8b80233f6f9823298e672'),
 'point':(G/'inner-three-cell-point-homogeneous-r1/kernels.json','c10a92c818833595c55682655bd9ac5ca2e628fd6a1f48d975270d2fdfbc927f'),
 'point_resource':(G/'inner-three-cell-point-homogeneous-r1/resource.json','0ac54f2ba028e2a34d099cc48d99676e3b2ba49c9d78d994700399eda1062061'),
}
def mv(A,v):return [up(A[i][0]*v[0]+A[i][1]*v[1]) for i in range(2)]
def completed(r):return r.get('exitcode',r.get('exit_code'))==0 and r.get('termination_signal') is None

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.out.exists():raise FileExistsError('Fresh actual endpoint required')
 ctx.prec,ctx.threads=256,1;start=time.monotonic();g=Gates();gate=g.check;ids={};docs={}
 for k,(path,pin) in FIXED.items():gate('fixed_successful_input_pin',sha(path)==pin);ids[k]=dict(path=str(path),sha256=pin);docs[k]=read(path)
 for k in ('base_resource','point_resource'):gate('complete_owned_input',completed(docs[k]))
 base,point=docs['base'],docs['point'];gate('complete_original_kernels',base['all_gates'] and point['all_gates'])
 for name,pin in SOURCE_PINS.items():gate('original_helper_pin',sha(HELP/name)==pin)
 helper_base=HELP/'inner_cell12_canonical_forced_endpoint_kernels_v2.py';gate('same_base_helper',sha(helper_base)=='edaca1021dd6d0118ca50e71b5900f270e8c2987e8899fdedd2578bade0d43e6')
 paths={k:G/'inner-cell12-canonical-forced-r1/inputs'/v[0] for k,v in PINS.items()}
 for k,path in paths.items():gate('complete_original_geometry_pin',sha(path)==PINS[k][1]);ids[k]=dict(path=str(path),sha256=PINS[k][1])
 meta=metadata_without_array(paths['panels'],'panels');port=next(c for c in point['cells'] if c['cell']==12)
 gate('actual_adjacent_point_norm',port['input_cell']==13 and port['input_Vprime_kind']=='actual-port-upper' and exact(port['tau_input'])==exact(port['tau_inner']) and exact(port['tau_inner'])==exact(meta['tau_inner']) and exact(port['tau_output'])==exact(meta['tau_outer']))
 mu_lo=min(ab(meta['mu'],'lower'),ab(port['current_canonical_mu_bounds'][0]));mu_hi=max(ab(meta['mu']),ab(port['current_canonical_mu_bounds'][1]));sq12=arb(12).sqrt()
 winhi=ab(port['true_w_in_upper']);woutlo=min(ab(port['true_w_out_lower']),ab(base['true_w_out_lower']))
 rinlo,rinhi=map(ab,port['input_physical_radius']);routlo,routhi=map(ab,port['output_physical_radius']);Bnext=ab(port['input_frame_B_lower']);Bout=ab(port['output_frame_B_upper']);Vnext=ab(port['nextcell_Vprime_boundary_upper'])
 scale2=ab(base['source_scale_squared_upper']);drop=ab(meta['tau_inner'],'lower')-ab(meta['tau_outer']);bt=ab(meta['btau_total'])
 gate('all_actual_denominators_positive',mu_lo>0 and winhi>0 and woutlo>0 and rinlo>0 and routlo>0 and Bnext>=120 and Bout>=120 and bt>0 and drop>0 and scale2>0 and Vnext>0)
 nu={m:arb(m*m*(m*m-1))/12 for m in MODES}
 states={m:{z:[arb(0),arb(0)] for z in MATERIALS} for m in MODES};hom={m:[[arb(1),arb(0)],[arb(0),arb(1)]] for m in MODES}
 count=0;segment=0;end=F(0);counts=[0]*9;sumdt=arb(0);maxproduct=arb(0);last=None;first=None
 for item in iter_array(paths['panels'],'panels'):
  j=item['segment'];lo,hi=F(*item['x_left']),F(*item['x_right'])
  if j==segment:gate('every_original_panel_order',lo==end)
  else:gate('whole_original_segment_cover',j==segment+1 and end==1 and lo==0);segment=j
  gate('strict_original_panel_range',0<=lo<hi<=1);end=hi;count+=1;counts[j]+=1;last=item
  if first is None:first=item
  rlo,rhi=ab(item['radius'],'lower'),ab(item['radius']);wl,wh=ab(item['w'],'lower'),ab(item['w']);J=ab(item['radial_log_increment']);TV=ab(item['log_w_variation']);V=ab(item['V'])
  gate('strict_positive_original_logr_geometry',0<rlo<=rhi and 0<wl<=wh and J>0 and TV>=0 and V>0)
  # a0 excludes nu. The original canonical system in log(r) has off-
  # diagonal entries nu*a(t), b(t), each bounded pointwise by these.
  a0=up(sq12*mu_hi/(rlo**7*wl)*J);b0=up(sq12/mu_lo*rhi**7*wh*J)
  dt=(drop*ab(item['btau_integral'],'lower')/bt).lower();gate('same_panel_strip_lower',dt>=0);sumdt+=dt
  pref=up(rhi**4*V**2/(sq12*mu_lo));common=ab(item['canonical_source_integral']);mat={'d1':up(min(pref*J,common)),'d_lambda':up(min(pref*TV,common))}
  for m in MODES:
   aa=up(nu[m]*a0);z=up(aa*b0);q=up(z.sqrt());gate('finite_positive_exponential_argument',q.is_finite() and q>0)
   maxproduct=max(maxproduct,z);c=up(q.cosh());s=up(q.sinh()/q);diag=up(((m*m-4)*J).exp())
   A=[[up(diag*c),up(diag*aa*s)],[up(diag*b0*s),up(diag*c)]]
   gate('complete_positive_constant_logr_exponential',all(v.is_finite() and v>=0 for row in A for v in row) and A[0][0]>=1 and A[1][1]>=1)
   decay=up((-m*dt).exp());gate('actual_paid_strip_multiplier',0<decay<=1)
   for material in MATERIALS:
    carried=mv(A,states[m][material]);emitted=[up(A[i][1]*mat[material]/nu[m]) for i in range(2)]
    states[m][material]=[up(decay*carried[i]+emitted[i]) for i in range(2)]
   H=hom[m];hom[m]=[[up(decay*(A[i][0]*H[0][k]+A[i][1]*H[1][k])) for k in range(2)] for i in range(2)]
  if count%256==0:
   gate('same96MiB_resource_gate',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
   print(json.dumps(dict(event='actual_logr_singleton_panel',count=count,max_nuAB=str(maxproduct),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
 gate('all1873_original_panels',count==1873 and segment==8 and end==1 and all(n>0 for n in counts));gate('no_extra_strip_loss',sumdt<=drop)
 gate('same_actual_input_output_ports',max(rinlo,ab(first['radius_left'],'lower'))<=min(rinhi,ab(first['radius_left'])) and max(routlo,ab(last['radius_right'],'lower'))<=min(routhi,ab(last['radius_right'])))
 rows=[]
 for m in MODES:
  cout=[up((Bout*m+m*m)*routhi**3),up(sq12*mu_hi*nu[m]/(routlo**4*woutlo))]
  zz=up(rinhi**4*winhi/(sq12*mu_lo*nu[m]));cin={'B_p':[up(1/(Bnext*m*rinlo**3)),up(zz*m/Bnext)],'kappa':[arb(0),zz]}
  cols={k:up(sum((cout[i]*mv(hom[m],v)[i] for i in range(2)),arb(0))) for k,v in cin.items()};Habs=max(cols.values());Hcut=up(Habs/woutlo)
  source_abs={k:up(2*(1+m)*scale2*sum((cout[i]*states[m][k][i] for i in range(2)),arb(0))) for k in MATERIALS};source_cut={k:up(source_abs[k]/woutlo) for k in MATERIALS}
  oldsrc=next(r for r in base['rows'] if r['window'][0]<=m<=r['window'][1]);oldhom=next(r for r in port['rows'] if r['window'][0]<=m<=r['window'][1])
  chosen_h=min(Hcut,ab(oldhom['input_absolute_mass_to_cut']));chosen_s={k:min(source_cut[k],ab(oldsrc['source_two_material_to_cut'][k])) for k in MATERIALS}
  gate('all_actual_singleton_endpoint_entries_finite',all(x.is_finite() and x>0 for x in list(source_cut.values())+[Habs,Hcut,chosen_h]+list(chosen_s.values())))
  rows.append(dict(window=[m,m],source_two_material_to_cut={k:pack(v) for k,v in source_cut.items()},source_two_material_to_absolute_endpoint={k:pack(v) for k,v in source_abs.items()},chosen_source_two_material_to_cut={k:pack(v) for k,v in chosen_s.items()},previous_parent_source_window=oldsrc['window'],previous_source_two_material_to_cut=oldsrc['source_two_material_to_cut'],complete_weighted_homogeneous_matrix_upper=[[pack(v) for v in row] for row in hom[m]],canonical_forced_endpoint_state_upper={k:list(map(pack,v)) for k,v in states[m].items()},physical_input_columns={k:list(map(pack,v)) for k,v in cin.items()},physical_output_covector=list(map(pack,cout)),input_physical_pair_columns_to_absolute_endpoint={k:pack(v) for k,v in cols.items()},input_absolute_mass_to_absolute_endpoint=pack(Habs),input_absolute_mass_to_cut=pack(Hcut),input_nextcell_Vprime_mass_to_cut=pack(up(Hcut*Vnext)),chosen_input_absolute_mass_to_cut=pack(chosen_h),chosen_input_nextcell_Vprime_mass_to_cut=pack(up(chosen_h*Vnext)),previous_parent_homogeneous_window=oldhom['window'],previous_input_absolute_mass_to_cut=oldhom['input_absolute_mass_to_cut']))
 gate('same96MiB_resource_gate',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 result=dict(schema='inner-cell12-true-singleton-logr-exponential-endpoint-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gate_count=g.count,gates={k:True for k in g.by_name},gate_multiplicities=g.by_name,source_sha256=sha(__file__),input_identities=ids,source_helper_pins=SOURCE_PINS,base_helper_sha256=sha(helper_base),cell=12,modes=MODES,original_panels=count,segment_panel_counts=counts,maximum_nu_a_b_integral_product=pack(maxproduct),not_using_geometric_Peano_product_gate=True,constant_logr_exponential_proof='In t=log r, each cooperative entry is pointwise bounded by a constant. A0 and B0 below exclude/retain nu exactly as stated; exp([[d,nu*A0],[B0,d]]) bounds every full panel and suffix since the constant generator is nonnegative. No source receives a free current-panel strip multiplier.',source_a0_definition='sqrt12*mu_upper*r_lower^-7*w_lower^-1*DeltaLogr_upper, excludes nu',source_b0_definition='sqrt12/mu_lower*r_upper^7*w_upper*DeltaLogr_upper',source_diagonal_definition='(m^2-4)*DeltaLogr_upper',source_scale_squared_upper=base['source_scale_squared_upper'],true_w_out_lower=pack(woutlo),input_nextcell_Vprime_boundary_upper=pack(Vnext),sum_actual_panel_strip_loss_lower=lower_pack(sumdt),input_strip_original=port['tau_input'],output_strip_original=port['tau_output'],uniform_angular_translation_invariant=True,complete_current_panel_sources_paid=True,complete_source_two_materials_retained=True,source_factor_two_kept=True,point_input_is_single_shared_two_component_mass=True,homogeneous_extra_factor_two_or_frame_jump=False,source_units=base['source_units'],output_units=base['output_units'],full_source_mean_inverse_far_required_in_consumer=True,old_rest_and_complete_infinite_kept_separate=True,no_new_ODE_radial_quadrature_or_physical_subdivision=True,rows=rows,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 raw=(json.dumps(result,separators=(',',':'))+'\n').encode();gate('small_complete_output',len(raw)<1000000);a.out.write_bytes(raw)
 print(json.dumps(dict(all_gates=True,path=str(a.out),sha256=sha(a.out),gate_count=g.count,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,sample={str(m):{'homogeneous':str(ab(rows[(m-94)//2]['chosen_input_nextcell_Vprime_mass_to_cut'])),'source':{k:str(ab(v)) for k,v in rows[(m-94)//2]['chosen_source_two_material_to_cut'].items()}} for m in (94,166,168,184)})),flush=True)
if __name__=='__main__':main()
