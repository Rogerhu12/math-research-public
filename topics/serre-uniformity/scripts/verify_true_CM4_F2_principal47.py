#!/usr/bin/env python3
"""Explicit-source principal audit plus independent degree3L and degree5L removable-fraction checks.

This does not claim a second RR, 41-torsion or 304-bit group-chain execution.
It independently combines the actual saved sections, integral exponents,
Norm factors, regularized tangents, all108 integral constants and QC roots.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

P,Q,q=47,47**4,47**3
O,Z=(1,0),(0,0)
def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def add(a,b):return ((a[0]+b[0])%Q,(a[1]+b[1])%Q)
def neg(a):return((-a[0])%Q,(-a[1])%Q)
def mul(a,b):return((a[0]*b[0]-a[1]*b[1])%Q,(a[0]*b[1]+a[1]*b[0])%Q)
def scale(a,k):return(a[0]*k%Q,a[1]*k%Q)
def inv(a):
 d=pow((a[0]*a[0]+a[1]*a[1])%Q,-1,Q);return(a[0]*d%Q,-a[1]*d%Q)
def power(a,n):
 if n<0:a,n=inv(a),-n
 v=O
 while n:
  if n&1:v=mul(v,a)
  a,n=mul(a,a),n//2
 return v
def log(a):
 z=add(power(a,47**2-1),neg(O));assert all(x%47==0 for x in z)
 return scale(add(add(z,scale(mul(z,z),-pow(2,-1,Q))),scale(power(z,3),pow(3,-1,Q))),pow(47**2-1,-1,Q))
def pmul(a,b):
 v=[Z]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[i+j]=add(v[i+j],mul(x,y))
 return v
def quotient(a,b):
 a=[tuple(x) for x in a];b=[tuple(x) for x in b];assert b[-1]==O and len(a)>=len(b)
 v=[Z]*(len(a)-len(b)+1)
 for k in range(len(v)-1,-1,-1):
  v[k]=a[k+len(b)-1]
  for j,x in enumerate(b):a[k+j]=add(a[k+j],neg(mul(v[k],x)))
 assert all(x==Z for x in a)
 return v
def flatten(x):
 return [v for a in x for v in flatten(a)] if isinstance(x,list) else [x]
def expadd(a,b,k=1):
 for x,e in b.items():
  a[x]=a.get(x,0)+k*e
  if not a[x]:del a[x]
 return a

def replay_split(cert, functions, manifest, expression):
 total=O;checks=0
 for chart in cert['charts']:
  sections={}
  for group in chart['groups'].values():
   nonunits={(x['point_0based'],x['column_0based']):[tuple(v) for v in x['W']] for x in group['nonunit_Weierstrass']}
   for c,label in enumerate(group['labels']):
    sections[label]=[(tuple(row[c]),nonunits.get((i,c),[O])) for i,row in enumerate(group['unit_values'])]
    assert [log(v[0]) for v in sections[label]]==[tuple(row[c]) for row in group['unit_logs']]
  for i,row in enumerate(chart['rows']):
   get=lambda k:sections[k][i][0]
   W=lambda k:sections[k][i][1]
   ideals={k:[tuple(y) for y in v] for k,v in row['four_complete73_ideal_Weierstrass'].items()}
   assert ideals['initial']==W('fb') and ideals['family1']==W('v1')
   init=manifest['initial_node']['point_sha256'];end=manifest['final_node']['point_sha256']
   ws={init:ideals['initial']};us={init:mul(get('fb'),inv(get('fc')))}
   for f in functions:
    v=mul(get(f['label']),power(get('fc'),-f['line_bundle_power']));w=[O]
    for parent in f['input_nodes']:
     key=parent['point_sha256'];w=pmul(w,ws[key]);v=mul(v,inv(us[key]))
    key=f['output_node']['point_sha256'];ws[key]=quotient(W(f['label']),w);us[key]=v;checks+=1
    if f['phase']=='initial_negative':assert ws[key]==ideals['negative']
   assert ws[end]==ideals['final']
   assert pmul(W('v1'),W('FP'))==pmul(ideals['final'],W('GQ'))
   phi=mul(inv(us[end]),mul(mul(get('v1'),inv(get('fc'))),mul(get('FP'),inv(get('GQ')))))
   independent=O
   for key,e in expression.items():independent=mul(independent,power(get(key),e))
   assert independent==phi==tuple(row['actual_Phi_value'])
   assert log(phi)==tuple(row['actual_log_Phi_value'])
   total=mul(total,phi)
 return total,checks

def audit_fractions(args,center,poly):
 """Recheck saved global fraction identities using separate Python integer dots.

 The faithful published model is reconstructed once; no new RR or group chain.
 """
 import sys
 replacements=poly.get('fixed_connection_fraction_replacements',{})
 if not replacements:return {'replacements':[], 'scope':'No replacement present.'}
 sys.path.insert(0,str(args.script_dir.resolve()))
 from p41_actual_differentials47 import ActualModel
 a=ActualModel(args.script_dir,derivatives=False)
 M={k:a.r.to_json(a.M[k]) for k in ['W','V2','A1','A2']}
 atlaspath=args.script_dir/'data'/'p41_rational_SS_residue_atlas47_complete.json.gz'
 atlas=read(atlaspath)
 ch=next(c for c in atlas['charts'] if args.disk_id in c['disk_ids'])
 idx=ch['disk_ids'].index(args.disk_id)
 W0=ch['W_coefficients_0to3'][0][idx]
 def m(a,b,n):return ((a[0]*b[0]-a[1]*b[1])%n,(a[0]*b[1]+a[1]*b[0])%n)
 def dot(row,col,n):
  terms=[m(x,y,n) for x,y in zip(row,col)]
  return (sum(x[0] for x in terms)%n,sum(x[1] for x in terms)%n)
 def unit(x):return x[0]%47!=0 or x[1]%47!=0
 def rk(rows):
  x=[[tuple(vv%47 for vv in v) for v in row] for row in rows];piv=[];rr=0
  for j in range(len(x[0])):
   i=next((i for i in range(rr,len(x)) if unit(x[i][j])),None)
   if i is None:continue
   x[rr],x[i]=x[i],x[rr];z=x[rr][j];norm=pow((z[0]*z[0]+z[1]*z[1])%47,-1,47);iv=(z[0]*norm%47,-z[1]*norm%47)
   x[rr]=[m(v,iv,47) for v in x[rr]]
   for ii in range(rr+1,len(x)):
    c=x[ii][j]
    if not unit(c):continue
    x[ii]=[((v[0]-t[0])%47,(v[1]-t[1])%47) for v,t in zip(x[ii],[m(c,w,47) for w in x[rr]])]
   piv.append(j);rr+=1
   if rr==len(x):break
  return rr,piv
 result=[]
 for name,rec in replacements.items():
  f=center['actual_connections'][name]
  assert rec['original_numerator_quadratic_mod47cubed']==f['numerator_quadratic_coefficients_mod47cubed']
  assert rec['original_denominator_linear_mod47four']==f['denominator_linear_coefficients_mod47four']
  assert rec['actual_unchanged_pole_support']==f['finite_pole_coordinates_fc_normalized']
  olds=[v[0] for v in rec['original_numerator_quadratic_mod47cubed']]
  oldq=[v[0] for v in rec['original_denominator_linear_mod47four']]
  news=[v[0] for v in rec['new_numerator_quadratic_mod47cubed']]
  newq=[v[0] for v in rec['new_denominator_linear_mod47four']]
  WZ=rec['actual_unchanged_pole_support']
  rank,piv=rk(WZ+[W0]);assert rank==len(WZ)+1
  assert not unit(dot(W0,oldq,Q)) and unit(dot(W0,newq,Q))
  assert all(dot(row,newq,Q)==Z for row in WZ)
  cross=[];good=[]
  for i,(w,v2) in enumerate(zip(M['W'],M['V2'])):
   oq,nq,os,ns=dot(w,oldq,q),dot(w,newq,q),dot(v2,olds,q),dot(v2,news,q)
   assert m(ns,oq,q)==m(os,nq,q),(name,i)
   cross.append([oq,nq,os,ns])
   if unit(oq):good.append(i)
  assert len(cross)==820 and len(good)>378 and good==rec['old_expression_unit_source_rows']
  for A,vec,mod in [(M['A1'],newq,Q),(M['A2'],news,q)]:
   cv=[(x[0],-x[1]%mod) for x in vec]
   assert [dot(row,cv,mod) for row in A]==[tuple(x) for x in vec]
  encoded=json.dumps(cross,separators=(',',':')).encode()
  result.append({'connection':name,'all820_exact_integer_cross_products_checked':True,
   'evaluation_cross_values_sha256':hashlib.sha256(encoded).hexdigest(),
   'old_unit_rows':len(good),'pole_plus_center_rank_mod47':rank,'unit_minor_columns_0based':piv,
   'new_denominator_at_center_mod47four':dot(W0,newq,Q),
   'true_support_vanishing_mod47four':True,'Frobenius_sections_exact':True,'faithful_degree_bound':378})
 return {'replacements':result,'faithful_model_input_sha256':a.inputs,
         'atlas_sha256':sha(atlaspath),'scope':'Independent Python-integer evaluations of all820 cross identities and source unit/support/rationality checks on the published faithfully reconstructed section model; not a second RR or chain execution.'}


def audit_eta_B_fraction(args,poly):
 rec=poly.get('eta_B_fraction_replacement')
 if rec is None:return {'replacement':False}
 import sys
 sys.path.insert(0,str(args.script_dir.resolve()))
 from p41_actual_differentials47 import ActualModel
 a=ActualModel(args.script_dir,derivatives=False);r=a.r
 M={k:r.to_json(a.M[k]) for k in ['V2','V3','A2','A3']}
 atlaspath=args.script_dir/'data'/'p41_rational_SS_residue_atlas47_complete.json.gz'
 atlas=read(atlaspath);ch=next(c for c in atlas['charts'] if args.disk_id in c['disk_ids']);idx=ch['disk_ids'].index(args.disk_id)
 W0=ch['W_coefficients_0to3'][0][idx];V20=ch['V2_coefficients_0to3'][0][idx]
 etapath=args.script_dir/'data'/'p41_eta_calibration47_complete.json.gz';eta=read(etapath)
 assert any(Path(k).name==etapath.name and h==sha(etapath) for k,h in poly['input_sha256'].items())
 assert rec['original_numerator_cubic_mod47cubed']==eta['numerator_coefficients']
 assert rec['original_denominator_quadratic_mod47cubed']==eta['denominator_coefficients']
 def m(x,y,n):return ((x[0]*y[0]-x[1]*y[1])%n,(x[0]*y[1]+x[1]*y[0])%n)
 def dot(row,col,n):
  vals=[m(x,y,n) for x,y in zip(row,col)]
  return (sum(x[0] for x in vals)%n,sum(x[1] for x in vals)%n)
 def unit(x):return x[0]%47 or x[1]%47
 def rk(rows):
  x=[[tuple(vv%47 for vv in v) for v in row] for row in rows];piv=[];rr=0
  for j in range(len(x[0])):
   i=next((i for i in range(rr,len(x)) if unit(x[i][j])),None)
   if i is None:continue
   x[rr],x[i]=x[i],x[rr];z=x[rr][j];norm=pow((z[0]*z[0]+z[1]*z[1])%47,-1,47);iv=(z[0]*norm%47,-z[1]*norm%47)
   x[rr]=[m(v,iv,47) for v in x[rr]]
   for ii in range(rr+1,len(x)):
    c=x[ii][j]
    if not unit(c):continue
    x[ii]=[((v[0]-t[0])%47,(v[1]-t[1])%47) for v,t in zip(x[ii],[m(c,w,47) for w in x[rr]])]
   piv.append(j);rr+=1
   if rr==len(x):break
  return rr,piv
 WZ=r.from_json(a.cm4['coarse_point_values']);WZ=r.mul(WZ,r.inverse_values(r.mm(WZ,a.fc)))
 assert r.to_json(WZ)==rec['actual20_CM4_pole_coordinates_fc_normalized']
 V2Z=r.to_json(a.evaluate(WZ)[0]);rank,piv=rk(V2Z+[V20]);assert rank==21
 fc=[x[0] for x in r.to_json(a.fc)];assert dot(W0,fc,Q)==O
 oldq=[x[0] for x in eta['denominator_coefficients']];olds=[x[0] for x in eta['numerator_coefficients']]
 newq=[x[0] for x in rec['new_denominator_quadratic_mod47four']];news=[x[0] for x in rec['new_numerator_cubic_mod47cubed']]
 assert not unit(dot(V20,oldq,q)) and unit(dot(V20,newq,Q))
 assert all(dot(row,newq,Q)==Z for row in V2Z)
 cross=[];good=[]
 for i,(v2,v3) in enumerate(zip(M['V2'],M['V3'])):
  oq,nq,os,ns=dot(v2,oldq,q),dot(v2,newq,q),dot(v3,olds,q),dot(v3,news,q)
  assert m(ns,oq,q)==m(os,nq,q),i
  cross.append([oq,nq,os,ns])
  if unit(oq):good.append(i)
 assert len(cross)==820 and len(good)>630 and good==rec['old_expression_unit_source_rows']
 for A,vec,mod in [(M['A2'],newq,Q),(M['A3'],news,q)]:
  cv=[(x[0],-x[1]%mod) for x in vec]
  assert [dot(row,cv,mod) for row in A]==[tuple(v) for v in vec]
 return {'replacement':True,'all820_exact_integer_degree5L_cross_products_checked':True,
  'evaluation_cross_values_sha256':hashlib.sha256(json.dumps(cross,separators=(',',':')).encode()).hexdigest(),
  'old_unit_rows':len(good),'actual20_CM4_plus_source_rank_mod47':rank,'unit_minor_columns_0based':piv,
  'source_fc_value_mod47four':O,'new_denominator_at_source_mod47four':dot(V20,newq,Q),
  'all20_CM4_new_denominator_values_zero_mod47four':True,'Frobenius_sections_exact':True,
  'faithful_degree_bound':630,'eta_certificate_sha256':sha(etapath),'atlas_sha256':sha(atlaspath),
  'faithful_model_input_sha256':a.inputs,'scope':'Independent Python-integer full820 degree5L cross identities, all actual CM4 zeros, source separation and Frobenius; shared published model reconstruction, no RR rerun.'}


def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','qc-dir','source-dir','poly-source','polynomial','chain-dir','transport-dir','based-points','output','norm-source','center-source','derivative','ramified-j-certificate','ramified-j-audit']:ap.add_argument('--'+k,type=Path,required=True)
 ap.add_argument('--disk-id',required=True);ap.add_argument('--result-id',required=True);args=ap.parse_args();d=args.disk_id;w=args.qc_dir;data=args.script_dir/'data'
 names={'center_source':args.center_source,'norm_source':args.norm_source,'poly_source':args.poly_source,'clearing':args.derivative,
 'center':w/(d+'_actual_canonical_F2_height47.json.gz'),'polynomial':args.polynomial,
 'full_norm':w/(d+'_actual_F2_first_variable_norm47.json.gz'),'T2_support':w/(d+'_actual_T2_support47.json.gz'),
 'T2_norm':w/(d+'_actual_T2_principal_norm47.json.gz'),'principal':w/(d+'_principal_expression47.json.gz'),
 'second':w/(d+'_actual_second_kind_integrals47.json.gz'),'Abel':args.chain_dir/(d+'_Abel47.json.gz'),
 'multiply':args.chain_dir/(d+'_multiply47.json.gz'),'based':args.based_points,
 'known_Abel':data/'p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz',
 'known_nu':data/'p41_rational_SS_second_kind_integrals47_complete.json.gz',
 'transport_manifest':args.transport_dir/'transport_manifest47.json',
 'ramified_j_certificate':args.ramified_j_certificate,'ramified_j_audit':args.ramified_j_audit}
 x={k:read(p) for k,p in names.items() if not k.endswith('_source')};h=x['center'];poly=x['polynomial'];fn=x['full_norm'];flat=x['principal'];second=x['second'];manifest=x['transport_manifest']
 assert h['source_sha256']==sha(names['center_source']) and poly['source_sha256']==sha(names['poly_source'])
 assert fn['source_sha256']==sha(names['norm_source'])
 assert x['clearing']['result']=='R554' and x['clearing']['both_true_rational_CM4_disks_complete']
 for k in ['center','polynomial','full_norm','T2_norm','principal','second','Abel','multiply']:assert x[k]['disk_id']==d
 assert x['T2_support']['source_disk_id']==d
 edges=[]
 for s,t in [('center','second'),('center','principal'),('center','T2_support'),('center','full_norm'),('polynomial','center'),('polynomial','Abel'),('polynomial','multiply'),('Abel','multiply'),('second','Abel'),('second','multiply'),('second','based'),('principal','second'),('T2_norm','principal'),('T2_norm','T2_support'),('full_norm','T2_norm'),('full_norm','principal'),('full_norm','second'),('full_norm','multiply'),('full_norm','based'),('full_norm','clearing'),('center','clearing'),('polynomial','clearing')]:
  a=[v for k,v in x[s]['input_sha256'].items() if Path(k).name==names[t].name];assert a and set(a)=={sha(names[t])},(s,t);edges.append([s,t])
 assert x['multiply']['input_sha256']==sha(names['based'])
 assert x['multiply']['bits_done']==x['multiply']['target_bits']==304 and len(x['multiply']['steps'])==454
 assert manifest['completed_Abel_sha256']==sha(names['Abel']) and len(manifest['functions'])==457
 for rec in manifest['functions']:
  fp=args.transport_dir/rec['filename'];assert sha(fp)==rec['sha256'] and fp.stat().st_size==rec['bytes']
 m=h['actual_integer_scale'];assert m==fn['actual_integer_scale']==x['Abel']['target_multiplier'] and m%47==9
 assert x['multiply']['point_sha256']==x['Abel']['actual_multiple_point_sha256']
 functions=[]
 for f in flat['section_factors']:
  fp=args.transport_dir/f['source_function_filename'];assert sha(fp)==f['source_function_sha256'];functions.append(read(fp))
 assert len(functions)==455
 init=manifest['initial_node']['point_sha256'];end=manifest['final_node']['point_sha256']
 exponents={init:{'fb':1,'fc':-1}};scalars={init:1}
 for f in functions:
  e={f['label']:1,'fc':-f['line_bundle_power']};s=0
  for node in f['input_nodes']:
   k=node['point_sha256'];assert scalars[k]==node['scalar_coefficient_of_C'];s-=scalars[k];expadd(e,exponents[k],-1)
  k=f['output_node']['point_sha256'];assert s==f['output_node']['scalar_coefficient_of_C'];exponents[k]=e;scalars[k]=s
 assert scalars[end]==m
 expression=expadd({'v1':1,'FP':1,'GQ':-1,'fc':-1},exponents[end],-1)
 expected={f['label']:f['signed_integer_exponent'] for f in flat['section_factors']}
 ep=flat['combined_function_to_actual_A1_t'];expadd(expected,{'fb':ep['f_b_integer_exponent'],'fc':ep['f0_integer_exponent'],'v1':1,'FP':1,'GQ':-1})
 expected={k:v for k,v in expected.items() if v};assert expression==expected and expression.get('fc',0)==0
 weights={f['label']:f['line_bundle_power'] for f in functions};weights.update(fb=1,fc=1,v1=1,FP=2,GQ=2)
 assert sum(weights[k]*e for k,e in expression.items())==0
 t2,count=replay_split(x['T2_norm'],functions,manifest,expression)
 assert t2==(x['T2_norm']['actual_norm_Phi_T2_P_mod47four'],0)
 assert log(t2)==(x['T2_norm']['actual_log_norm_Phi_T2_P_mod47four'],0)
 vals={v['label']:v['norm_mod47four'] for v in fn['full106_canonical_part']['all460_evaluated_section_polynomials_and_norms']}
 assert len(vals)==460;cn=1
 for k,e in expression.items():cn=cn*pow(vals[k],e,Q)%Q
 assert cn==fn['full106_canonical_part']['norm_mod47four']
 cl=log((cn,0))[0];assert cl==fn['full_canonical_degree106_log_norm']==fn['full106_canonical_part']['log_norm_mod47four']
 fixed=fn['fixed_and_collision_part'];rows={r['label']:r for r in fixed['rows']}
 fl=Z
 for row in rows.values():
  val=row.get('log_leading_unit_in_prescribed_parameter_mod47four',row.get('log_value_mod47four'))
  fl=add(fl,scale(val,row['second_divisor_weight']))
 assert fl==tuple(fixed['weighted_actual_log_in_prescribed_parameters'])
 normlog=(fl[0]+4*cl+27*log(t2)[0])%Q
 assert normlog==fn['actual_log_norm_Phi_on_F2_second_divisor_mod47four']==h['first_variable_principal_log_norm_mod47four']
 ab,apoint=[rows[k]['parameter_tangent']['g1_differential_over_parameter'] for k in ['P_minus3',d]]
 assert ab[1]==apoint[1]==0 and [ab[0],apoint[0]]==h['actual_g1_over_prescribed_parameters_at_base_and_center']
 sigma=pow(ab[0]*pow(apoint[0],-1,Q)%Q,4,Q);logsigma=log((sigma,0))[0]
 assert sigma==h['canonical_sigma_fibre_coordinate_mod47four'] and logsigma==h['canonical_sigma_coordinate_log_mod47four']
 parameters=[tuple(v) for v in h['physical_family1_parameters'][0]];tiny={}
 for name,coeff in h['integrand_coefficients_0to2'].items():
  ans=Z
  for n,cs in enumerate(coeff,1):
   for t,c in zip(parameters,cs):ans=add(ans,scale(mul(power(t,n),c[0]),pow(n,-1,Q)))
  assert ans[1]==0;tiny[name]=ans[0]
 assert tiny==h['all_actual_tiny_integrals_mod47four']
 ws={'T2C':27,'C':4,'u_minus_b':162,'Z8_minus20b':-27,'c7_minus_b':-54,'K_g1_minus106b':4}
 tinyd=sum(ws[k]*tiny[k] for k in ws)%Q;assert tinyd==h['second_divisor_tiny_integral_mod47four']
 height=(logsigma+pow(m,-1,Q)*(normlog+tinyd))%Q;assert height==h['actual_local_sigma_F2_height_mod47four']
 assert rows[d]['parameter_tangent']['parameter']=='original_R228_z'
 assert rows[d]['parameter_tangent']['dz_over_parameter']==[1,0]
 assert rows['P_minus3']['parameter_tangent']['parameter']=='j_minus_jb'
 assert h['center_parameter']=='original_R228_z' and h['base_parameter']=='j_minus_jb'
 sourcechart=next(c for c in fixed['charts'] if rows[d]['indices_0based'] in c['indices_0based'])
 assert sourcechart['frame']==h['original_center_frame'] and sourcechart['coordinate']==h['original_center_coordinate']
 # Change only the source parameter from z to t=2z; both changes must cancel.
 c=2;ap_t=apoint[0]*pow(c,-1,Q)%Q
 sigma_t=pow(ab[0]*pow(ap_t,-1,Q)%Q,4,Q)
 norm_t=(normlog-4*m*log((c,0))[0])%Q
 assert (log((sigma_t,0))[0]+pow(m,-1,Q)*(norm_t+tinyd))%Q==height
 rc=x['ramified_j_certificate'];ra=x['ramified_j_audit']
 assert rc['result']==ra['result']=='R554'
 assert ra['certificate_sha256']==sha(args.ramified_j_certificate)
 for key in ['all876_projective_ODE_entries_replayed','all7336_V2_V3_section_entries_reconstructed','all_homogeneous_invariants_reconstructed_by_exact_directional_derivative','both_actual_coarse_j_series_and_unit_tangents_replayed','both_actual_eta_B_simple_poles_and_joint_cancellation_replayed','both_all54_tiny_differentials_match_original_coordinate']:
  assert ra[key],key
 assert sha(args.derivative)==sha(args.ramified_j_certificate)
 assert rc['both_true_rational_CM4_disks_complete']
 assert poly['true_CM4_Laurent_regularization']['certificate_sha256']==sha(args.ramified_j_certificate)
 jc=next(c for c in rc['charts'] if d in c['disk_ids']);jr=jc['disk_ids'].index(d)
 assert jc['frame']==h['original_center_frame'] and jc['coordinate']==h['original_center_coordinate']
 assert jc['actual_eta_B_simple_pole_and_residue_one'] and jc['no_nonunit_inversion_or_division_by47']
 # R554's saved independent integer audit recombines the original residue-one
 # eta_B and j-1728 Laurent pieces. Bind that exact certified triple here.
 expectedC=[[[list(v[jr][0])]] for v in jc['regular_F2_combination_coefficients_0to2_mod47cubed']]
 auditrow=next(v for v in ra['records'] if v['disk_id']==d)
 assert auditrow['actual_residue_eta_B']==1 and auditrow['joint_polar_coefficient']==0
 assert auditrow['regular_F2_combination_coefficients']==[v[0][0] for v in expectedC]
 pieces=poly['differential_pieces_coefficients_mod47cubed']
 assert pieces['combined_regular_true_CM4_j_and_eta_B_correction']==expectedC
 assert all(key not in pieces for key in ['minus2_eta_B','two_dlog_j_minus1728','eight_thirds_dlog_j','8_self_regular_j','combined_regular_ramified_j_correction'])
 diff=[]
 for k in range(3):
  z=Z
  for terms in pieces.values():z=add(z,terms[k][0][0])
  diff.append((z[0]%q,z[1]%q))
 assert [list(z) for z in diff]==[v[0][0] for v in poly['local_differential_coefficients_0to2_in_z_mod47cubed']]
 assert all(z[1]==0 for z in diff)
 assert poly['canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four'][1:]==[z[0]*47**(k+1)*pow(k+1,-1,Q)%Q for k,z in enumerate(diff)]
 actualnu=flatten(second['actual54_second_kind_integrals_of_C_mod47four'])
 knownnu=next(z for z in x['known_nu']['rational_SS_center_integrals'] if z['disk_id']==d)
 assert [v%q for v in actualnu]==flatten(knownnu['C_original_nu_coordinates_mod47cubed'])
 knownabel=next(z for z in x['known_Abel']['actual_113_rational_disk_global_polynomials'] if z['disk_id']==d)
 assert flatten(x['Abel']['actual_center_C_cyclic_coordinates_mod47cubed'])==flatten(knownabel['actual_center_C_cyclic_coordinates_mod47cubed'])
 principal_gradient=flatten(ep['log_norm_derivative_at_family2_mod47four'])
 endpoint_tiny=flatten(second['endpoint']['actual_second_kind_tiny_integrals_at_family1_mod47four'])
 assert [(v+w)%Q for v,w in zip(principal_gradient,endpoint_tiny)]==[m*v%Q for v in actualnu]
 hp=poly['canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four'];assert hp[0]==height
 gp=poly['global_F2_coefficients_0to4_in_y_mod47four'];qc=[(v-800*(hp[k] if k<4 else 0))%Q for k,v in enumerate(gp)]
 assert qc==poly['actual_QC_F2_coefficients_0to4_in_y_mod47four'] and all(v%47==0 for v in qc)
 divided=[v//47 for v in qc];red=[v%47 for v in divided];assert red==poly['QC_divided_by47_reduction_coefficients_mod47']
 roots=[y for y in range(47) if sum(c*pow(y,k,47) for k,c in enumerate(red))%47==0];assert roots==poly['residual_QC_roots']
 lifted=[];singular_branches=[]
 for y0 in roots:
  derivative=sum(k*c*pow(y0,k-1,47) for k,c in enumerate(divided) if k)%47
  if not derivative:
   value=sum(c*pow(y0,k,47**2) for k,c in enumerate(divided))%(47**2)
   assert value%47==0
   possible=[y0+47*t for t in range(47) if sum(c*pow(y0+47*t,k,47**2) for k,c in enumerate(divided))%(47**2)==0]
   singular_branches.append({'root_mod47':y0,'derivative_mod47':0,'QC_div47_value_mod47square':value,'all47_second_digits_checked':True,'lifts_mod47square':possible,'excluded':not possible})
   # A surviving multiple root needs an explicit further lifting calculation;
   # it must never be silently discarded as if it were a simple Hensel root.
   assert not possible, ('unresolved multiple F2 root',y0,possible)
   continue
  y=y0;mod=47;digits=[y0]
  for _ in range(2):
   val=sum(c*pow(y,k,mod*47) for k,c in enumerate(divided))%(mod*47);assert val%mod==0
   digit=-(val//mod)*pow(derivative,-1,47)%47;y+=mod*digit;digits.append(digit);mod*=47
  assert sum(c*pow(y,k,Q) for k,c in enumerate(qc))%Q==0
  lifted.append({'y_mod47cubed':y,'z_mod47four':47*y,'y_base47_digits':digits,'derivative_mod47':derivative})
 out={'result':args.result_id,'disk_id':d,'input_sha256':{str(p):sha(p) for p in names.values()},'source_sha256':sha(__file__),
 'same_actual_clearing_frame_in_Norm_center_polynomial_verified':True,
 'checked_nested_hash_edges':edges,'all457_actual_principal_function_hashes_verified':True,'all455_integer_divisor_SLP_relations_replayed':True,
 'exact_final_f0_exponent_zero_and_total_weight_zero':True,'T2_saved_Weierstrass_relations_independently_replayed':count,
 'all460_full106_norm_values_recombined_by_exact_integer_exponents':True,'all108_actual_integrals_match_independent_SS_Hecke_solutions':True,
 'all54_principal_norm_derivatives_plus_terminal_tiny_equal_m_times_original_nu':True,
 'all_actual_family1_integrals_independently_reassembled':tiny,'actual_unit_z_to_2z_tangent_change_cancels_in_height':True,
 'true_CM4_joint_Laurent_correction_bound_to_independent_R554':True,
 'actual_g1_over_prescribed_parameters_base_center':[ab[0],apoint[0]],'canonical_sigma':sigma,'canonical_sigma_log':logsigma,
 'signed_actual_scale':m,'second_divisor_tiny':tinyd,'full_first_norm_log':normlog,'actual_center_height':height,
 'local_polynomial':hp,'global_polynomial':gp,'QC_polynomial':qc,'QC_div47_reduction':red,'residual_roots':roots,
 'simple_single_F2_root_candidates_to_available_precision':lifted,
 'multiple_F2_residual_branch_certificates':singular_branches,
 'all_F2_residual_branches_accounted_for':len(lifted)+len(singular_branches)==len(roots),
 'entire_disk_excluded_by_F2_after_exact_lifting':not lifted,
 'fixed_fraction_cross_audit':audit_fractions(args,h,poly),
 'eta_B_fraction_cross_audit':audit_eta_B_fraction(args,poly),
 'scope':'Independent exact saved-section DAG/Weierstrass/unit Norm arithmetic, 108 independent Hecke matches, actual tangent and tiny integration scalars, and complete simple or obstructed-multiple Hensel branches; no duplicate RR, torsion or long group-chain execution.'}
 args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print('PASS independent actual SS F2 principal audit',d,'height',height,'roots',lifted,'SHA',sha(args.output))

if __name__=='__main__':main()
