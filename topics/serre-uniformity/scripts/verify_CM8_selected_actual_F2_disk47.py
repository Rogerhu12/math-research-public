#!/usr/bin/env python3
"""Independent standard-library scalar, principal-DAG and saved Weierstrass audit.

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

def replay_CM8_split(cert, functions, manifest, expression):
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
   expected=W('fb')
   if row['source_collision']:
    linear=[tuple(x) for x in row['source_collision']['actual_source_linear_factor_ascending']]
    assert linear[-1]==O and all(v%47==0 for v in linear[0])
    expected=pmul(expected,linear)
   assert ideals['initial']==expected and ideals['family1']==W('v1')
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
   assert independent==phi==tuple(row['actual_Phi_unit_part_mod47four'])
   assert log(phi)==tuple(row['actual_log_Phi_unit_part_mod47four'])
   total=mul(total,phi)
 return total,checks

def replay_CM8_fixed(cert,functions,manifest,expression,disk,m):
 checks=0;weighted=Z
 for chart in cert['charts']:
  labels=chart['cubic_labels_in_order'];cols={label:i for i,label in enumerate(labels)}
  nonunits={(v['point_0based_in_chart'],v['column_0based']):[tuple(y) for y in v['W']] for v in chart['cubic_nonunit_Weierstrass']}
  for i,row in enumerate(chart['rows']):
   logs={k:tuple(v) for k,v in row['fixed_unit_logs'].items()}
   ws0={k:[tuple(y) for y in v] for k,v in row['fixed_Weierstrass'].items()}
   for f in functions:
    label=f['label']
    if f['phase']=='initial_negative':
     logs[label]=tuple(row['negative_unit_log']);ws0[label]=[tuple(y) for y in row['negative_Weierstrass']]
    else:
     j=cols[label];logs[label]=tuple(chart['cubic_unit_log_constants'][i][j]);ws0[label]=nonunits.get((i,j),[O])
   ideals={k:[tuple(y) for y in v] for k,v in row['four_full73_ideal_Weierstrass'].items()}
   expected=ws0['fb']
   if row['source_collision']:
    assert row['source_collision']['actual_integer_exponent']==m
    linear=[tuple(y) for y in row['source_collision']['actual_source_linear_factor_ascending']]
    assert linear[-1]==O and all(v%47==0 for v in linear[0]);expected=pmul(expected,linear)
   elif row['label']==disk:expected=pmul(expected,[Z,O])
   elif row['label']=='P_minus3':expected=quotient(expected,[Z,O])
   assert ideals['initial']==expected and ideals['family1']==ws0['v1']
   initial=manifest['initial_node']['point_sha256'];end=manifest['final_node']['point_sha256']
   nodeW={initial:ideals['initial']};nodeL={initial:add(logs['fb'],neg(logs['fc']))}
   for f in functions:
    w=[O];v=add(logs[f['label']],scale(logs['fc'],-f['line_bundle_power']))
    for parent in f['input_nodes']:
     key=parent['point_sha256'];w=pmul(w,nodeW[key]);v=add(v,neg(nodeL[key]))
    key=f['output_node']['point_sha256'];nodeW[key]=quotient(ws0[f['label']],w);nodeL[key]=v;checks+=1
    if f['phase']=='initial_negative':assert nodeW[key]==ideals['negative']
   assert nodeW[end]==ideals['final']
   assert pmul(ws0['v1'],ws0['FP'])==pmul(ideals['final'],ws0['GQ'])
   value=add(neg(nodeL[end]),add(add(logs['v1'],neg(logs['fc'])),add(logs['FP'],neg(logs['GQ']))))
   independent=Z
   for label,e in expression.items():independent=add(independent,scale(logs[label],e))
   assert value==independent==tuple(row['log_leading_unit_in_chart_z_mod47four'])
   order=m if row['label']==disk else -m if row['label']=='P_minus3' else 0
   assert row['Phi_actual_order']==order
   if row['source_collision']:
    assert row['Phi_distinguished_factor']['integer_exponent']==m
    assert row['Phi_distinguished_factor']['linear']==row['source_collision']['actual_source_linear_factor_ascending']
    assert value==tuple(row['log_Phi_unit_part_mod47four'])
   elif order:
    assert row['Phi_distinguished_factor']=={'z_integer_exponent':order}
    tangent=row['j_tangent'];alpha=tuple(tangent['dz_over_dj']);assert log(alpha)==tuple(tangent['log_dz_over_dj'])
    value=add(value,scale(log(alpha),order));assert value==tuple(row['log_leading_unit_in_j_mod47four'])
   else:assert value==tuple(row['log_value_mod47four'])
   weighted=add(weighted,scale(value,row['second_divisor_weight']))
 assert weighted==tuple(cert['weighted_unit_and_tangent_log_pending_joint_factor'])
 return weighted,checks

def scalar_pair(x):
 while isinstance(x,list) and len(x)==1:x=x[0]
 assert isinstance(x,(tuple,list)) and len(x)==2 and all(isinstance(v,int) for v in x)
 return tuple(x)

def audit_collision_unit(collision):
 delta=scalar_pair(collision['source_coordinate_displacement']);assert all(v%47==0 for v in delta)
 assert [neg(delta),O]==[tuple(x) for x in collision['actual_source_linear_factor_ascending']]
 js=[scalar_pair(x) for x in collision['j_coefficients_0to4']]
 D=Z
 for k in range(1,5):D=add(D,mul(js[k],power(delta,k-1)))
 assert D==scalar_pair(collision['j_divided_difference_unit_mod47four'])
 assert add(js[0],mul(delta,D))==scalar_pair(collision['j_source_mod47four'])
 W=collision['W_coefficients_0to4'];source=collision['W_source_in_same_frame'][0]
 for i in range(73):
  value=Z
  for k in range(5):value=add(value,mul(tuple(W[k][0][i]),power(delta,k)))
  assert value==tuple(source[i])
 return D

def audit_laurent(diff,branches,reference,hecke,eta):
 # Reconstruct every scalar branch division by independent integer pair arithmetic.
 mod=q
 def a(x,y):return ((x[0]+y[0])%mod,(x[1]+y[1])%mod)
 def n(x):return (-x[0]%mod,-x[1]%mod)
 def t(x,c):return (x[0]*c%mod,x[1]*c%mod)
 def m(x,y):return ((x[0]*y[0]-x[1]*y[1])%mod,(x[0]*y[1]+x[1]*y[0])%mod)
 def iv(x):
  z=pow((x[0]*x[0]+x[1]*x[1])%mod,-1,mod);return (x[0]*z%mod,-x[1]*z%mod)
 def pair(x):return tuple(v%mod for v in scalar_pair(x))
 def dot(row,col):
  out=Z
  for x,y in zip(row,col):out=a(out,m(tuple(x),tuple(y[0])))
  return out
 def conv(x,y,N):
  out=[]
  for k in range(N):
   v=Z
   for j in range(k+1):
    if j<len(x) and k-j<len(y):v=a(v,m(x[j],y[k-j]))
   out.append(v)
  return out
 def invs(x,N):
  out=[iv(x[0])]
  for k in range(1,N):
   v=Z
   for j in range(1,min(k,len(x)-1)+1):v=a(v,m(x[j],out[k-j]))
   out.append(n(m(out[0],v)))
  return out
 def cross(xs,ys,N):
  out=[]
  for k in range(N):
   v=Z
   for j in range(k+1):
    if j<len(xs) and k-j<len(ys):v=a(v,dot(xs[j][0],ys[k-j]))
   out.append(v)
  return out
 mov=diff['actual_moving_connection'];qj=mov['q_linear_coefficients_in_parameter_0to4_mod47four'];sj=mov['s_quadratic_coefficients_in_parameter_0to3_mod47cubed']
 J=branches['source_true_CM_projective_jets_0to4'];coordinate=branches['source_coordinate']
 allvalues=[];residue=Z
 for br,record in zip(branches['branch_records'],diff['actual_branch_Laurent_data']):
  assert br['branch_0based']==record['branch_0based']
  denominator=cross(br['actual_image_W_coefficients_0to4'],qj,5)
  num=conv(cross(br['actual_image_V2_coefficients_0to4'],sj,4),[pair(x) for x in br['actual_differential_pullback_coefficients_0to3']],4)
  assert num==[pair(x) for x in record['numerator_coefficients_0to3_mod47cubed']]
  assert denominator==[pair(x) for x in record['denominator_coefficients_0to4_mod47cubed']]
  if br['horizontal_fixed_point']:
   assert denominator[0]==Z
   tau=dot(br['actual_image_W_coefficients_0to4'][1][0],coordinate);assert tau==(mod-1,0)
   values=conv(num,invs(denominator[1:],4),4)
   expected=m(tau,iv(a(tau,(-1%mod,0))));assert values[0]==expected==(pow(2,-1,mod),0)
   residue=a(residue,values[0])
  else:values=conv(num,invs(denominator,4),4)
  assert values==[pair(x) for x in record['coefficients_mod47cubed']]
  allvalues.append((br['horizontal_fixed_point'],values))
 fixed=reference['actual_connections']['Z8_minus20b'];zq=fixed['denominator_linear_coefficients_mod47four'];zs=fixed['numerator_quadratic_coefficients_mod47cubed']
 zn=conv([dot(w[0],zs) for w in J['V2'][:4]],[pair(x) for x in J['inverse_Hc'][:4]],4)
 zd=[dot(w[0],zq) for w in J['W']];assert zd[0]==Z
 zl=conv(zn,invs(zd[1:],4),4)
 assert zl==[pair(x) for x in diff['actual_fixed_eta_Z8_Laurent_coefficients_minus1_to2_mod47cubed']]
 assert zl[0]==O and a(t(residue,54),t(zl[0],-27))==Z
 combined=[]
 for k in range(3):
  value=t(zl[k+1],-27)
  for hor,vals in allvalues:value=a(value,t(vals[k+int(hor)],54))
  combined.append(value)
 assert combined==[pair(x) for x in diff['differential_pieces_coefficients_mod47cubed']['54_T2_eta_C_minus27_eta_Z8']]
 def scale_matrix(x,c):return [[t(tuple(z),c) for z in row] for row in x]
 ih=[pair(x) for x in J['inverse_Hc'][:3]]
 nd=cross(J['V2'][:3],sj[:3],3)
 ndp=cross([scale_matrix(J['V2'][k+1],k+1) for k in range(3)],sj[:3],3)
 hcp=[t(pair(J['Hc'][k+1]),k+1) for k in range(3)]
 apart=[a(v,n(w)) for v,w in zip(conv(ndp,ih,3),conv(conv(nd,hcp,3),conv(ih,ih,3),3))]
 qp=cross([scale_matrix(J['W'][k+1],k+1) for k in range(3)],qj[:3],3)
 qpp=cross([scale_matrix(J['W'][k+2],(k+2)*(k+1)) for k in range(3)],qj[:3],3)
 assert conv(nd,ih,3)==qp
 regular=conv([a(v,t(w,-pow(2,-1,mod))) for v,w in zip(apart,qpp)],invs(qp,3),3)
 assert regular==[pair(v) for v in diff['actual_self_regular_x_coefficients_mod47cubed']]
 j=[pair(v) for v in branches['source_true_CM_j_coefficients_0to4']]
 jp=[t(j[k+1],k+1) for k in range(3)];jpp=[t(j[k+2],(k+2)*(k+1)) for k in range(3)]
 selfpiece=[a(t(v,8),t(w,-4)) for v,w in zip(regular,conv(jpp,invs(jp,3),3))]
 pieces=diff['differential_pieces_coefficients_mod47cubed']
 assert selfpiece==[pair(v) for v in pieces['8_self_regular_j']]
 for name,weight in [('u_minus_b',162),('c7_minus_b',-54),('D_minus20b',64*pow(3,-1,mod))]:
  form=reference['actual_connections'][name]
  ss=form['numerator_quadratic_coefficients_mod47cubed'];qq=form['denominator_linear_coefficients_mod47four']
  replacement=diff['fixed_fraction_replacements'].get(name)
  if replacement:ss=replacement['new_numerator_quadratic_mod47cubed'];qq=replacement['new_denominator_linear_mod47four']
  v=conv(conv([dot(w[0],ss) for w in J['V2'][:3]],invs([dot(w[0],qq) for w in J['W'][:3]],3),3),ih,3)
  assert [t(x,weight) for x in v]==[pair(x) for x in pieces[name]]
 sb,qb=eta['numerator_coefficients'],eta['denominator_coefficients']
 eb=diff['eta_B_fraction_replacement']
 if eb:sb,qb=eb['new_numerator_cubic_mod47cubed'],eb['new_denominator_quadratic_mod47four']
 vb=conv(conv([dot(w[0],sb) for w in J['V3'][:3]],invs([dot(w[0],qb) for w in J['V2'][:3]],3),3),ih,3)
 assert [t(v,-2) for v in vb]==[pair(v) for v in pieces['minus2_eta_B']]
 assert [t(v,8*pow(3,-1,mod)) for v in conv(jp,invs(j[:3],3),3)]==[pair(v) for v in pieces['eight_thirds_dlog_j']]
 jm=j[:3];jm[0]=a(jm[0],(-1728%mod,0))
 assert [t(v,2) for v in conv(jp,invs(jm,3),3)]==[pair(v) for v in pieces['two_dlog_j_minus1728']]
 gc=mov['gradient_original_nu_coefficients_0to3_mod47cubed'];nu=reference['actual_CM_nu_coefficients_0to2_mod47four']
 assert gc[0]==reference['actual_gradients_original_nu_mod47cubed']['C_at_CM8']
 for k in range(1,4):assert [pair(v) for v in gc[k][0]]==[t(pair(v),pow(k,-1,mod)) for v in nu[k-1][0]]
 total=[Z]*3
 for vals in diff['differential_pieces_coefficients_mod47cubed'].values():
  total=[a(x,pair(y)) for x,y in zip(total,vals)]
 assert total==[pair(x) for x in diff['local_differential_coefficients_0to2_in_x_mod47cubed']]
 # All 4x73 actual Hecke trace coefficients, with the actual branch differential factors.
 mod=Q
 trace=[[Z]*73 for _ in range(4)]
 for br in branches['branch_records']:
  for j in range(73):
   xs=[tuple(w[0][j]) for w in br['actual_image_W_coefficients_0to4'][:4]]
   values=conv(xs,[pair(x) for x in br['actual_differential_pullback_coefficients_0to3']],4)
   for k in range(4):trace[k][j]=a(trace[k][j],values[k])
 source=[[Z]*73 for _ in range(4)]
 for j in range(73):
  vals=conv([tuple(w[0][j]) for w in J['W'][:4]],[pair(x) for x in J['inverse_Hc'][:4]],4)
  for k in range(4):source[k][j]=vals[k]
 op=hecke['operators']['2']['weight2_operator']
 for k in range(4):
  for j in range(73):assert trace[k][j]==dot(source[k],[[row[j]] for row in op])
 return {'actual_horizontal_residue': [pow(2,-1,q),0], 'actual_weighted_residues':[27,-27], 'all3_actual_Laurent_or_unit_branch_divisions_replayed':True,'all4x73_Hecke_differential_trace_scalars_replayed':True,'joint_pole_cancellation_and_all_differential_piece_sums_replayed':True,'all_self_regular_fixed_and_logarithmic_differential_pieces_reconstructed':True,'moving_gradient_is_actual_nu_primitive':True}

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','qc-dir','chain-dir','transport-dir','based-points','output']:ap.add_argument('--'+k,type=Path,required=True)
 ap.add_argument('--disk-id',required=True);args=ap.parse_args();d=args.disk_id;w=args.qc_dir;data=args.script_dir/'data'
 names={'center_source':w/'p41_CM8_selected_SS_F2_connection47.py','poly_source':w/'p41_CM8_assemble_selected_actual_F2_disk47.py',
 'center':w/(d+'_actual_canonical_F2_height47.json.gz'),'polynomial':w/(d+'_actual_canonical_F2_polynomial47.json.gz'),
 'full_norm':w/(d+'_actual_F2_joint_first_variable_norm47.json.gz'),'T2_support':w/(d+'_actual_T2_diagonal_support47.json.gz'),
 'T2_norm':w/(d+'_actual_T2_principal_unit_parts47.json.gz'),'principal':w/(d+'_principal_expression47.json.gz'),
 'second':w/(d+'_actual_second_kind_integrals47.json.gz'),'Abel':args.chain_dir/(d+'_Abel47.json.gz'),
 'multiply':args.chain_dir/(d+'_multiply47.json.gz'),'based':args.based_points,
 'known_Abel':data/'p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz',
 'known_nu':data/'p41_rational_SS_second_kind_integrals47_complete.json.gz',
 'transport_manifest':args.transport_dir/'transport_manifest47.json',
 'difference':w/(d+'_actual_CM8_F2_height_difference47.json.gz'),
 'branches':w/(d+'_actual_CM8_T2_local_branches47.json.gz'),
 'CM_connection':w/(d+'_actual_CM8_C_and_fixed_connections47.json.gz'),
 'horizontal_unit':w/'p41_CM8_horizontal_j_unit47.json.gz',
 'hecke':data/'p41_hecke47_full_saved.json.gz',
 'eta_B':data/'p41_eta_calibration47_complete.json.gz',
 'difference_source':w/'p41_CM8_selected_F2_Laurent_height_difference47.py',
 'T2_source':w/'p41_CM8_T2_principal_unit_parts47.py',
 'full_norm_source':w/'p41_CM8_joint_F2_principal_norm47.py'}
 x={k:read(p) for k,p in names.items() if not k.endswith('_source')};h=x['center'];poly=x['polynomial'];fn=x['full_norm'];flat=x['principal'];second=x['second'];manifest=x['transport_manifest']
 assert h['source_sha256']==sha(names['center_source']) and poly['source_sha256']==sha(names['poly_source'])
 for k in ['center','polynomial','full_norm','T2_norm','principal','second','Abel','multiply']:assert x[k]['disk_id']==d
 assert x['T2_support']['source_disk_id']==d
 edges=[]
 for s,t in [('center','second'),('center','principal'),('center','T2_support'),('center','full_norm'),('polynomial','center'),('polynomial','Abel'),('polynomial','multiply'),('Abel','multiply'),('second','Abel'),('second','multiply'),('second','based'),('principal','second'),('T2_norm','principal'),('T2_norm','T2_support'),('full_norm','T2_norm'),('full_norm','principal'),('full_norm','second'),('full_norm','multiply'),('full_norm','based')]:
  a=[v for k,v in x[s]['input_sha256'].items() if Path(k).name==names[t].name];assert a and set(a)=={sha(names[t])},(s,t);edges.append([s,t])
 for s,t in [('difference','difference_source'),('T2_norm','T2_source'),('full_norm','full_norm_source')]:assert x[s]['source_sha256']==sha(names[t])
 for s,t in [('polynomial','difference'),('polynomial','branches'),('difference','branches'),('difference','CM_connection'),('full_norm','horizontal_unit')]:
  vals=[v for k,v in x[s]['input_sha256'].items() if Path(k).name==names[t].name];assert vals and set(vals)=={sha(names[t])};edges.append([s,t])
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
 t2,count=replay_CM8_split(x['T2_norm'],functions,manifest,expression)
 assert t2==(x['T2_norm']['actual_T2_product_of_Phi_unit_parts_mod47four'],0)
 assert log(t2)==(x['T2_norm']['actual_T2_sum_of_Phi_unit_part_logs_mod47four'],0)
 vals={v['label']:v['norm_mod47four'] for v in fn['full106_canonical_part']['all460_evaluated_section_polynomials_and_norms']}
 assert len(vals)==460;cn=1
 for k,e in expression.items():cn=cn*pow(vals[k],e,Q)%Q
 assert cn==fn['full106_canonical_part']['norm_mod47four']
 cl=log((cn,0))[0];assert cl==fn['full_canonical_degree106_log_norm']==fn['full106_canonical_part']['log_norm_mod47four']
 fixed=fn['fixed_and_collision_part'];rows={r['label']:r for r in fixed['rows']}
 fl,fixed_count=replay_CM8_fixed(fixed,functions,manifest,expression,d,m)
 target=next(v for v in x['T2_norm']['rows'] if v['source_collision'])
 fixedrow=next(v for v in fixed['rows'] if v['source_collision'])
 dT=audit_collision_unit(target['source_collision']);dQ=audit_collision_unit(fixedrow['source_collision'])
 Udata=x['horizontal_unit'];delta=Udata['source_Delta_j_mod47four']
 U=sum(v*pow(delta,k,Q) for k,v in enumerate(Udata['U_coefficients_0to3_in_Delta_j_mod47four']))%Q
 assert U==Udata['U_mod47four'] and log((U,0))==(Udata['log_U_mod47four'],0)
 gamma=mul((U,0),mul(dQ,inv(dT)));lg=log(gamma);correction=scale(lg,27*m)
 joint=fn['actual_joint_CM8_distinguished_factor_cancellation']
 assert gamma==tuple(joint['combined_chart_ratio_unit_mod47four']) and lg==tuple(joint['combined_chart_ratio_log_mod47four'])
 assert correction==tuple(joint['weighted_distinguished_factor_correction_mod47four']) and joint['actual_integer_scale']==m
 assert dT==tuple(joint['actual_target_chart_divided_difference_unit_mod47four']) and dQ==tuple(joint['actual_fixed_chart_divided_difference_unit_mod47four'])
 normlog=(fl[0]+4*cl+27*log(t2)[0]+correction[0])%Q
 assert normlog==fn['actual_log_norm_Phi_on_F2_second_divisor_mod47four']==h['first_variable_principal_log_norm_mod47four']
 ab,apoint=[rows[k]['j_tangent']['g1_differential_over_dj'] for k in ['P_minus3',d]]
 assert ab[1]==apoint[1]==0 and [ab[0],apoint[0]]==h['actual_g1_over_dj_at_base_and_center']
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
 alpha=tuple(rows[d]['j_tangent']['dz_over_dj']);assert alpha[1]==0
 sigma_z=pow(ab[0]*pow(apoint[0]*pow(alpha[0],-1,Q)%Q,-1,Q)%Q,4,Q)
 norm_z=(normlog-4*m*log(alpha)[0])%Q
 assert (log((sigma_z,0))[0]+pow(m,-1,Q)*(norm_z+tinyd))%Q==height
 actualnu=flatten(second['actual54_second_kind_integrals_of_C_mod47four'])
 knownnu=next(z for z in x['known_nu']['rational_SS_center_integrals'] if z['disk_id']==d)
 assert [v%q for v in actualnu]==flatten(knownnu['C_original_nu_coordinates_mod47cubed'])
 knownabel=next(z for z in x['known_Abel']['actual_113_rational_disk_global_polynomials'] if z['disk_id']==d)
 assert flatten(x['Abel']['actual_center_C_cyclic_coordinates_mod47cubed'])==flatten(knownabel['actual_center_C_cyclic_coordinates_mod47cubed'])
 principal_gradient=flatten(ep['log_norm_derivative_at_family2_mod47four'])
 endpoint_tiny=flatten(second['endpoint']['actual_second_kind_tiny_integrals_at_family1_mod47four'])
 assert [(v+w)%Q for v,w in zip(principal_gradient,endpoint_tiny)]==[m*v%Q for v in actualnu]
 laurent_audit=audit_laurent(x['difference'],x['branches'],x['CM_connection'],x['hecke'],x['eta_B'])
 diff=x['difference'];ycm=diff['source_CM_original_y_mod47cubed']
 dc=[scalar_pair(z)[0] for z in diff['local_differential_coefficients_0to2_in_x_mod47cubed']]
 hw=[0]+[c*47**(k+1)*pow(k+1,-1,Q)%Q for k,c in enumerate(dc)]
 from math import comb
 shifted=[sum(comb(n,k)*hw[n]*pow(-ycm,n-k,Q) for n in range(k,4))%Q for k in range(4)]
 hp=poly['canonical_local_sigma_F2_height_coefficients_0to3_in_y_mod47four'];assert hp==[height]+shifted[1:]
 assert not diff['CM_global_reciprocity_anchor_used'] and not diff['actual_height_constant_computed']
 gp=poly['global_F2_coefficients_0to4_in_y_mod47four'];assert gp==next(z for z in knownabel['global_polynomials'] if z['n']==2)['coefficients_0to4_in_y_mod47four'];qc=[(v-800*(hp[k] if k<4 else 0))%Q for k,v in enumerate(gp)]
 assert qc==poly['actual_QC_F2_coefficients_0to4_in_y_mod47four'] and all(v%47==0 for v in qc)
 divided=[v//47 for v in qc];red=[v%47 for v in divided];assert red==poly['QC_divided_by47_reduction_coefficients_mod47']
 roots=[y for y in range(47) if sum(c*pow(y,k,47) for k,c in enumerate(red))%47==0];assert roots==poly['residual_QC_roots']
 lifted=[]
 for y0 in roots:
  derivative=sum(k*c*pow(y0,k-1,47) for k,c in enumerate(divided) if k)%47;assert derivative
  y=y0;mod=47;digits=[y0]
  for _ in range(2):
   val=sum(c*pow(y,k,mod*47) for k,c in enumerate(divided))%(mod*47);assert val%mod==0
   digit=-(val//mod)*pow(derivative,-1,47)%47;y+=mod*digit;digits.append(digit);mod*=47
  assert sum(c*pow(y,k,Q) for k,c in enumerate(qc))%Q==0
  lifted.append({'y_mod47cubed':y,'z_mod47four':47*y,'y_base47_digits':digits,'derivative_mod47':derivative})
 out={'result':h['result'],'disk_id':d,'input_sha256':{str(p):sha(p) for p in names.values()},'source_sha256':sha(__file__),
 'checked_nested_hash_edges':edges,'all457_actual_principal_function_hashes_verified':True,'all455_integer_divisor_SLP_relations_replayed':True,
 'exact_final_f0_exponent_zero_and_total_weight_zero':True,'T2_saved_Weierstrass_relations_independently_replayed':count,
 'fixed24_saved_Weierstrass_and_log_DAG_relations_independently_replayed':fixed_count,
 'joint_CM8_unit':gamma,'joint_CM8_log':lg,'actual_joint_weighted_correction':correction,
 'actual_Laurent_and_Hecke_scalar_audit':laurent_audit,
 'CM8_points_not_used_as_global_reciprocity_anchors':True,
 'all460_full106_norm_values_recombined_by_exact_integer_exponents':True,'all108_actual_integrals_match_independent_SS_Hecke_solutions':True,
 'all54_principal_norm_derivatives_plus_terminal_tiny_equal_m_times_original_nu':True,
 'all_actual_family1_integrals_independently_reassembled':tiny,'actual_j_to_z_tangent_change_cancels_in_height':True,
 'actual_g1_over_dj_base_center':[ab[0],apoint[0]],'canonical_sigma':sigma,'canonical_sigma_log':logsigma,
 'signed_actual_scale':m,'second_divisor_tiny':tinyd,'full_first_norm_log':normlog,'actual_center_height':height,
 'local_polynomial':hp,'global_polynomial':gp,'QC_polynomial':qc,'QC_div47_reduction':red,'residual_roots':roots,
 'simple_single_F2_root_candidates_to_available_precision':lifted,
 'scope':'Independent standard-library exact saved-section DAG/Weierstrass/unit Norm arithmetic including both genuine collision factors, all3 Laurent divisions and4x73 Hecke trace, 108 independent Hecke matches, actual tangent/tiny scalars, unit translation and simple Hensel roots; no duplicate RR, torsion or long group-chain execution.'}
 args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print('PASS independent actual SS F2 principal audit',d,'height',height,'roots',lifted,'SHA',sha(args.output))

if __name__=='__main__':main()
