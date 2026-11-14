#!/usr/bin/env python3
"""New original cells8/7 signed low46 continuation; no repetition of completed cells.

Keep the original 256-bit/order24/remainder100/root160 Taylor algorithm.
Continue the true far-linear projective column from original node10,
reset two trace-zero Cauchy basis columns there, and retain actual
R119+R141 low initial errors as complex radii.  This program certifies
linear/homogeneous contributions and local kernels only.  It does NOT
claim that the outer nonlinear source or the infinite tail is paid.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
import argparse, gzip, hashlib, json, resource, sys, time
from fractions import Fraction as F
from pathlib import Path

BASE=Path('/workspace/scratch/d1aa462cfc02/exact-work')
FROZEN=BASE/'outer9-low46-inputs'
sys.path.insert(0,str(FROZEN/'sources'))
from flint import arb, ctx
from closure_outer_physical_trace_flow import taylor_physical, root_physical, balanced_majorant
from closure_projective_interval_column import ProjectiveColumn
from closure_real_head_source_enclosure import exact_q, power2
from closure_real_linear_head_enclosure import PositiveKernels
from closure_taylor_cut_slope_v2 import (record,ball,endpoint,intersect,rough_radius,
    monotone_parts,column_record,restore_column,add_error)
from tail_r33_middle_ordered_physical import SourceValues
from closure_split_joint_io_v2 import read_field

WRAPPER='bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59'
MANIFEST='e5973f185f1157aaa3743077ec5869ca5bed6fe5ec750142b6b0bec9a861b15f'
MODES=list(range(2,93,2))

def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()

def load(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)

def dump(p,d):
 p=Path(p)
 if p.exists():raise FileExistsError('Preserve previous actual output: '+str(p))
 raw=(json.dumps(d,separators=(',',':'))+'\n').encode()
 if len(raw)>4_900_000:raise MemoryError('Split the complete saved output below5MB')
 if len(raw)>1_000_000 and p.suffix!='.gz':raise MemoryError('Compress data above1MB')
 q=Path(str(p)+'.partial')
 if p.suffix=='.gz':
  with open(q,'wb') as f:
   with gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0) as g:g.write(raw)
 else:q.write_bytes(raw)
 q.replace(p)
 return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,uncompressed_bytes=len(raw))

def upper(d):
 if isinstance(d,list):return arb((int(d[0]),int(d[1])))
 if 'upper' in d:return endpoint(d['upper'])
 return endpoint(d)

def caprec(x):
 x=x.upper()
 if not x.is_finite() or x<0:raise ArithmeticError('A finite nonnegative cap is mandatory')
 a,b=x.man_exp();return [str(a),int(b)]

def resource_gate(d):
 return d['resource_wrapper_sha256']==WRAPPER and d['exitcode']==0 and d['termination_signal'] is None

def raw_cell_identity(ready,n):
 if n not in (8,7):raise ValueError('This raw continuation supports original cells8/7 only')
 p=ready['rationalDeepModel']['physicalParameters']
 row=next(r for r in ready['shallowSourceParameters']['cells'] if r['n']==n)
 if (row['lengthScale']!=1 or p['orientation']!=1 or p['capMode']!='cut-preserving'
  or p['protectCell']!=160 or p['capTransition']!=2 or p['curvatureBound']!=8
  or p.get('flatOuterThroughCell') is not None or p.get('rejoinR20At') is not None):
  raise ValueError('Cell9 must use the frozen original source convention')
 if n<len(p.get('valleyControls',[])) and p['valleyControls'][n]!=0:
  raise ValueError('The original cell9 valley control is not zero')
 for key in ('pulseCaps','valleyCaps','warpWeightLevels'):
  a=p.get(key,[])
  if n<len(a) and a[n] is not None:raise ValueError('A custom cell9 cap/warp is present')
 constants=ready['rationalDeepModel']['exactSourceConstants']
 delta=exact_q(F(constants['delta0']))*power2(-n)
 mu=exact_q(p['epsilonScale'])*(arb(11)/4*delta.log()).exp()
 rc=exact_q(p['rCuff']);R=exact_q(row['R']);alpha=exact_q(row['alpha'])
 rho=(arb(11)/4*arb(2).log()).exp()
 uw=(mu*max(v.upper() for v in [arb(1),R/delta,delta/alpha,1/delta,rho])/rc**7).upper()
 threshold=exact_q(p['slopeCap'])*(-exact_q(p['capTransition'])).exp()
 if not uw<threshold:raise ArithmeticError('Whole original cell9 raw cap inequality failed')
 return dict(cell=n,background_mu=record(mu),R=record(R),alpha=record(alpha),
  whole_cell_raw_w_upper=record(uw),cap_raw_threshold=record(threshold),
  cap_strictly_inactive=True,valley_control_exact_zero=True,warp_weight_exact_one=True,
  chi_and_j0_exact_one=True,no_extension_to_capped_cells_claimed=True)

def partial_flow(h,s,lo,hi,radius):
 rr,unused=rough_radius(h,s,lo,hi,radius)
 dx=exact_q(hi-lo);x=exact_q(lo).union(exact_q(hi))
 src=h.source_point(s,x);w,ell=src['w'],src['log_w_x'];E=1+w*w
 rx=abs(w*ell)/(8*E*E.sqrt())+h.alpha*src['ro_x']/E
 ss=dx*rx/rr;ee=dx*ell;dd=(ee-ss)/2
 B,q,major=balanced_majorant(dd,ss,ee,92)
 err=(q*q/(1-q)).upper()
 rem=[[err,(err/B).upper()],[(err*B).upper(),err]]
 flows=[]
 for m in MODES:
  M=[[dd,-m*ss],[-m*ee,-dd]]
  flows.append([[add_error(arb(0).union(M[i][j])+(1 if i==j else 0),rem[i][j])
    for j in range(2)] for i in range(2)])
 return flows,rr,w,rx,ell,B,q,major

def profile(columns,flow,r,w,F0,lambdas,errors):
 den=(r*w*w*w).sqrt()
 if not den>0:raise ArithmeticError('Wholeleaf physical conversion is not positive')
 rows=[]
 for k,m in enumerate(MODES):
  T=flow[k]
  # Ordinary interval matrix-vector multiplication safely encloses every
  # partial time; a projective pivot is not asserted for the whole time box.
  v=columns[k][0].values();e=columns[k][2].values()
  cent=[lambdas[k]*sum((T[i][j]*v[j] for j in range(2)),arb(0))/den for i in range(2)]
  err=[(F0*errors[k]*abs(sum((T[i][j]*e[j] for j in range(2)),arb(0)))/den).upper() for i in range(2)]
  for a in cent+err:
   if not a.is_finite():raise ArithmeticError('Every centre and error entry must be finite')
  rows.append(dict(mode=m,linear_PK=[record(x) for x in cent],initial_error_PK=[caprec(x) for x in err]))
 return rows

def endpoint_rows(columns,r,w,F0,lambdas,errors):
 den=(r*w*w*w).sqrt();out=[]
 for k,m in enumerate(MODES):
  vals=columns[k][0].values();eb=columns[k][2].values()
  cent=[lambdas[k]*v/den for v in vals]
  er=[(F0*errors[k]*abs(v)/den).upper() for v in eb]
  Phi=[[columns[k][j+1].values()[i] for j in range(2)] for i in range(2)]
  out.append(dict(mode=m,linear_PK=[record(x) for x in cent],initial_error_PK=[caprec(x) for x in er],
    trace0_node10_fundamental_matrix=[[record(x) for x in row] for row in Phi],
    columns=[column_record(c) for c in columns[k]]))
 return out

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--out-prefix',type=Path,required=True)
 p.add_argument('--rss-kib',type=int,default=98304)
 p.add_argument('--cell',type=int,choices=(8,7),required=True)
 p.add_argument('--previous',type=Path,required=True)
 p.add_argument('--previous-resource',type=Path,required=True)
 a=p.parse_args();beg=time.monotonic();ctx.prec=256;ctx.cap=26;ctx.threads=1
 cell=a.cell;prefix=str(a.out_prefix)
 if any(a.out_prefix.parent.glob(a.out_prefix.name+'*')):raise FileExistsError('Use fresh complete run prefix')
 a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
 mp=FROZEN/'manifest.json'
 if sha(mp)!=MANIFEST:raise ValueError('Frozen cell9 input manifest changed')
 manifest=load(mp)
 for r in list(manifest['inputs'].values())+manifest['source_files']:
  if sha(r['path'])!=r['sha256']:raise ValueError('Frozen input/source hash changed '+r['path'])
 I={k:Path(v['path']) for k,v in manifest['inputs'].items()}
 gates={}
 def gate(k,test):
  if not bool(test):raise ArithmeticError('Gate failed: '+k)
  gates[k]=True
 def guard():
  peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  if peak>a.rss_kib:raise MemoryError('Owned RSS exceeds unchanged cap: '+str(peak))
 for name in ('old_physical_resource','signed_geometry_resource','R141_resource'):
  gate(name,resource_gate(load(I[name])))
 mp_new=BASE/f'outer-cell{cell}-material-r1-manifest.json'
 mr_new=BASE/f'outer-cell{cell}-material-r1-resource.json'
 mat=load(mp_new);old=load(I['old_physical_flow']);geom=load(I['signed_geometry'])
 previous=load(a.previous)
 gate('previous_new_cell_formal_zero',resource_gate(load(a.previous_resource)))
 gate('previous_new_cell_complete',previous['all_gates'] and all(previous['gates'].values()) and previous['config']['cell']==cell+1)
 gate('previous_new_cell_original_arithmetic',all(previous['config'][k]==v for k,v in [('precision',256),('order',24),('remainder_bits',100),('root_bits',160)]))
 gate('new_material_formal_zero',resource_gate(load(mr_new)))
 extra_inputs={str(p):sha(p) for p in (mp_new,mr_new,a.previous,a.previous_resource)}
 err119=load(I['R119_errors']);actual=load(I['R141_full_field']);lastsrc=load(I['old_last_source'])
 gate('old_physical_all_gates',old['all_gates'] and all(old['gates'].values()))
 gate('signed_geometry_all_gates',geom['all_gates'] and all(geom['gates'].values()))
 gate('R119_all_gates',err119['all_gates'] and all(err119['gates'].values()))
 gate('R141_actual_field_all_gates',actual['all_gates'] and all(actual['gates'].values()))
 gate('same_expanded_profile',actual['same_parameter_domain']['name']=='expanded_profile')
 domain=actual['same_parameter_domain']
 gate('all46_old_modes',old['config']['modes']==MODES and geom['config']['modes']==MODES)
 gate('original_new_cell_material',mat['cell']==cell and mat['panels']>0 and all(r['complete_cover'] and r['sum_intersects_parent'] for r in mat['parent_constraints']))
 gate('same_new_material_original_ready',manifest['inputs']['ready']['sha256'] in mat['original_metadata']['input_hashes'].values())
 ready=dict(rationalDeepModel=read_field(I['ready'],'rationalDeepModel'),shallowSourceParameters=read_field(I['ready'],'shallowSourceParameters'))
 raw=raw_cell_identity(ready,cell);gate('whole_new_cell_raw_source_identity',raw['cap_strictly_inactive'])
 h=SourceValues(ready);del ready
 kernel=PositiveKernels(h,12,92);h.cells={cell:kernel.source_cell(cell)}
 node10=old['cell_rows'][-1]
 gate('node10_old_entry',node10['cell']==10 and node10['endpoint_physical_node']==10)
 gate('all46_node10_columns',[r['mode'] for r in node10['modes']]==MODES)
 r0=ball(node10['radius']);w0=ball(node10['w'])
 previous_modes=previous.get('endpoint_modes',previous.get('node9_modes'))
 previous_radius=ball(previous.get('endpoint_radius',previous.get('node9_radius')))
 previous_w=ball(previous.get('endpoint_w',previous.get('node9_w')))
 r_entry=intersect(previous_radius,ball(mat['original_metadata']['inner_radius']))
 w_entry=intersect(previous_w,h.source_point(h.cells[cell]['segments'][0],arb(0))['w'])
 gate('previous_node10_initial_identity',intersect(r0,ball(previous['initial_radius'])).is_finite() and intersect(w0,ball(previous['initial_w'])).is_finite())
 gate('same_expanded_parameter_domain',previous['config']['parameter_domain']==domain)
 F0=(r0*w0*w0*w0).sqrt();F0up=F0.upper()
 V=upper(lastsrc['rows'][0]['local_V']);common=upper(err119['common_joint_error_radius'])
 errors=[];lambdas=[];inputrows=[];columns=[]
 for k,m in enumerate(MODES):
  cols=[restore_column(node10['modes'][k]['columns'][0]),ProjectiveColumn([arb(1),arb(0)]),ProjectiveColumn([arb(0),arb(1)])]
  columns.append(cols)
  Q=ball(geom['config']['actual_outer_Q'][str(m)])
  S=intersect(ball(geom['config']['actual_true_S0_Q'][str(m)]),ball(node10['modes'][k]['S0_true_Q']))
  gate('S0_height_nonzero_'+str(m),not S.contains(0))
  lam=Q/S;lambdas.append(lam)
  c=upper(err119['mode_rows'][k]['K_error_cap']);u=upper(actual['low_caps'][24][k])
  gate('Kcaps_finite_nonnegative_'+str(m),c.is_finite() and u.is_finite() and c>=0 and u>=0)
  e=((min(c,common)+u)*V/((1+m)*(arb(m)/64).exp())).upper();errors.append(e)
  # Same exact prescribed height at the node10 outer boundary means
  # P_error=0.  The retained centre column may have interval rounding,
  # but it encloses the same linear state with that exact height.
  p_from_height=-m*r0**3/w0*Q
  p_from_column=lam*cols[0].values()[0]/F0
  intersect(p_from_height,p_from_column)
  gate('true_node10_height_identity_'+str(m),True)
  inputrows.append(dict(mode=m,lambda_true_far_linear=record(lam),outer_Q=record(Q),
    initial_P_error_exact_zero=True,CL_minus_LR_K_normalized_cap=caprec(c),
    u_block24_pair_normalized_cap=caprec(u),complete_initial_K_error=caprec(e),
    initial_linear_PK=[record(lam*v/F0) for v in cols[0].values()]))
 gate('previous_all46_modes',[r['mode'] for r in previous_modes]==MODES)
 columns=[[restore_column(c) for c in row['columns']] for row in previous_modes]
 gate('same_original_initial_error_modes',[r['mode'] for r in previous['input_rows']]==MODES)
 # Consume the saved exact upward radii. Re-encoding an Arb union is not
 # a bit-identity test for the underlying exact datum.
 for k,row in enumerate(previous['input_rows']):
  intersect(lambdas[k],ball(row['lambda_true_far_linear']))
  gate('previous_initial_error_finite_'+str(MODES[k]),upper(row['complete_initial_K_error']).is_finite() and upper(row['complete_initial_K_error'])>=0 and row['initial_P_error_exact_zero'])
 inputrows=previous['input_rows']
 lambdas=[ball(r['lambda_true_far_linear']) for r in inputrows]
 errors=[upper(r['complete_initial_K_error']) for r in inputrows]
 r0=ball(previous['initial_radius']);w0=ball(previous['initial_w'])
 F0up=(r0*w0*w0*w0).sqrt().upper()
 # Exact original R26 widths anchor both sides of all nine source segments.
 widths=[]
 for j in range(9):
  parents=[q for q in mat['parent_constraints'] if q['source_segment']==j]
  gate('source_segment_coverage_'+str(j),parents and parents[0]['left']=='0' and parents[-1]['right']=='1' and all(parents[i]['right']==parents[i+1]['left'] for i in range(len(parents)-1)))
  widths.append(sum((ball(q['original_width']) for q in parents),arb(0)))
 rlast=ball(mat['original_metadata']['outer_radius']);anchors=[r_entry]
 for j in range(9):
  forward=r_entry+sum(widths[:j+1],arb(0));backward=rlast-sum(widths[j+1:],arb(0))
  anchors.append(intersect(forward,backward))
 gate('endpoint_radius_original_identity',intersect(anchors[-1],rlast).is_finite())
 config=dict(cell=cell,modes=MODES,precision=256,order=24,remainder_bits=100,root_bits=160,
  initial_parts=8,rss_kib=a.rss_kib,input_manifest_sha256=MANIFEST,source_sha256=sha(__file__),
  source_hashes={Path(v['path']).name:v['sha256'] for v in manifest['source_files']},
  additional_input_hashes=extra_inputs,previous_actual_cell_primary=str(a.previous),
  previous_actual_cell_sha256=sha(a.previous),
  parameter_domain=domain,source_identity=raw,coordinates='Y=sqrt(r*w^3)*(P_sine,K_cosine)',
  initial_basis='Identity at node10; initial actual error has only K coordinate',
  initial_error_kind='Complex disk radius, not a real interval for all complex parameters',
  strong_input_sigma='1/64',local_V_node10=caprec(V),
  nonlinear_source_paid=False,infinite_modes_paid=False)
 # The large R141 primary is no longer needed during the Taylor computation.
 del old,geom,err119,actual,lastsrc,mat
 counts=dict(taylor=0,root_brackets=0,rejected=0);chunks=[];segments=[]
 worst=arb(0);maxq=arb(0);whole_caps=[[arb(0),arb(0)] for _ in MODES]
 buffer=[];radius=r_entry;completed=[]
 def flush():
  if not buffer:return
  chunks.append(dump(prefix+f'-profiles{len(chunks):04d}.json.gz',dict(schema='original-cell9-signed-low46-steps-v1',rows=buffer)))
  buffer.clear();guard()
 try:
  for j in range(9):
   segment=h.cells[cell]['segments'][j]
   segment['physical_inner_radius']=anchors[j];segment['physical_outer_radius']=anchors[j+1]
   radius=intersect(radius,anchors[j]);segment_caps=[[arb(0),arb(0)] for _ in MODES]
   for left,right,sign in monotone_parts(segment,160):
    segment['_monotone_sign']=sign
    pieces=([(left,right,0)] if sign==0 else [(left+(right-left)*k/8,left+(right-left)*(k+1)/8,0) for k in range(8)])
    stack=list(reversed(pieces))
    while stack:
     lo,hi,level=stack.pop()
     try:
      T,nr,err,q=(root_physical(h,segment,lo,hi,radius,MODES) if sign==0 else taylor_physical(h,segment,lo,hi,radius,MODES,24,power2(-100)))
      partial,rr,ww,rx,ell,B,qp,major=partial_flow(h,segment,lo,hi,radius)
      prof=profile(columns,partial,rr,ww,F0up,lambdas,errors)
      advanced=[]
      for row,t in zip(columns,T):
       new=[]
       for v in row:
        c=restore_column(column_record(v));c.advance(t);new.append(c)
       advanced.append(new)
     except (ArithmeticError,ValueError,ZeroDivisionError) as ex:
      if sign==0 or level>=40:raise ArithmeticError('Unresolved original cell9 panel '+str((j,lo,hi,sign))+': '+str(ex)) from ex
      mid=(lo+hi)/2;stack.extend([(mid,hi,level+1),(lo,mid,level+1)])
      counts['rejected']+=1;continue
     for k,row in enumerate(prof):
      for z in range(2):
       ca=(abs(ball(row['linear_PK'][z])).upper()+upper(row['initial_error_PK'][z])).upper()
       whole_caps[k][z]=max(whole_caps[k][z],ca)
       segment_caps[k][z]=max(segment_caps[k][z],ca)
     buffer.append(dict(cell=cell,segment=j,left=str(lo),right=str(hi),monotone_sign=sign,
       radius_left=record(radius),radius_right=record(nr),whole_radius=record(rr),whole_w=record(ww),
       radius_x=record(rx),log_w_x=record(ell),balance=record(B),integral_norm=record(qp),
       partial_absolute_majorant=[[record(major[x,y]) for y in range(2)] for x in range(2)],
       local_signed_flow=[dict(mode=m,matrix=[[record(x) for x in row] for row in t]) for m,t in zip(MODES,T)],
       whole_homogeneous_profiles=prof))
     columns=advanced;radius=nr
     counts['root_brackets' if sign==0 else 'taylor']+=1
     worst=max(worst,err) if sign else worst;maxq=max(maxq,q,qp)
     if len(buffer)>=12:flush()
     guard()
   radius=intersect(radius,anchors[j+1]);w=h.source_point(segment,arb(1))['w']
   flush()
   erows=endpoint_rows(columns,radius,w,F0up,lambdas,errors)
   strong=sum(((1+m)*(arb(m)/64).exp()*(ca[0]+ca[1]) for m,ca in zip(MODES,segment_caps)),arb(0)).upper()
   out=dict(schema='new-original-raw-cell-signed-low46-segment-v1',cell=cell,segment=j,
     config=config,radius=record(radius),w=record(w),modes=erows,
     homogeneous_whole_segment_strong_mass_at_sigma1over64=caprec(strong),
     whole_component_caps=[dict(mode=m,P=caprec(c[0]),K=caprec(c[1])) for m,c in zip(MODES,segment_caps)],
     counts=dict(counts),no_nonlinear_or_infinite_tail_claim=True)
   segments.append(dump(prefix+f'-completed-segment{j}.json',out));completed.append(j)
   print(json.dumps(dict(event='actual_original_raw_cell_segment_complete',cell=cell,segment=j,counts=counts,
     homogeneous_strong_upper=float(strong),wall_seconds=time.monotonic()-beg,
     peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
  gate('all_nine_original_raw_cell_segments',completed==list(range(9)))
  gate('original_256_24_160_100_gates_unchanged',worst<power2(-100) and maxq<arb(1)/2)
  gate('all_saved_profile_chunks_match',all(sha(r['path'])==r['sha256'] for r in chunks+segments))
  strong=sum(((1+m)*(arb(m)/64).exp()*(ca[0]+ca[1]) for m,ca in zip(MODES,whole_caps)),arb(0)).upper()
  result=dict(schema='new-original-raw-cell-signed-low46-v1',author='exact_closure (GPT-6 Astra Pro, AI-assisted)',
   all_gates=all(gates.values()),gates=gates,config=config,input_manifest=str(mp),
   input_rows=inputrows,initial_radius=record(r0),initial_w=record(w0),endpoint_radius=record(radius),endpoint_w=record(w),
   endpoint_modes=endpoint_rows(columns,radius,w,F0up,lambdas,errors),
   completed_segments=segments,profile_chunks=chunks,counts=counts,
   whole_cell_homogeneous_strong_mass_at_sigma1over64=caprec(strong),
   whole_cell_component_caps=[dict(mode=m,P=caprec(c[0]),K=caprec(c[1])) for m,c in zip(MODES,whole_caps)],
   greatest_balanced_Taylor_remainder=record(worst),greatest_balanced_integral_norm=record(maxq),
   same_original_cauchy_height_and_complex_K_radius=True,
   previous_successful_cells11and10_not_recomputed=True,
   complete_nonlinear_source_or_full_frequency_extension_claimed=False,
   elapsed_seconds=time.monotonic()-beg,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
  dump(prefix+'.json',result);guard()
  print(json.dumps(dict(event='actual_original_raw_cell_complete',cell=cell,all_gates=result['all_gates'],gates=len(gates),counts=counts,
   homogeneous_strong_upper=float(strong),wall_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)
 except Exception as ex:
  flush()
  dump(prefix+'-failure.json',dict(schema='new-original-raw-cell-signed-low46-failure-v1',error=repr(ex),
    config=config,completed_segments=segments,profile_chunks=chunks,counts=counts,
    elapsed_seconds=time.monotonic()-beg,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
  raise

if __name__=='__main__':main()
