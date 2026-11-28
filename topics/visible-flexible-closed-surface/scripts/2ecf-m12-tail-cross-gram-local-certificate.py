#!/usr/bin/env python3
"""Continuous original-M12 cross-Gram with local W norms and slope enclosures.

The original exact target metric is retained. X=B+V on the tail; the
B/W cross terms are combined as complete angular Fourier polynomials
before enclosure. V/W, angular phase, finite Laurent and rounding errors
are separately paid. The V/W and quadratic remainders use a separately
proved local R236 W norm, capped by either a supplied same-field R236
receipt or the already-proved R226 differential l1 bound (which also
bounds the Frobenius norm). No missing R236 receipt is fabricated.
A certified local background derivative range may tighten the original
point-Lipschitz w enclosure; a proposed inverse is never trusted.
All finite Bernstein interiors are covered.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,math,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

BITS=96;S=1<<BITS
PRIMITIVE_SHA='28577da04035f91bcd5dc310094d5844347cbeb78d6213dcba0232b62acf56e9'
CAL_SHA='bcfaba00aec62290b5b29432836c9e76ef6cf0d582b06c046677b0f8688ca9f4'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,path):
 sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
def fq(x):return Q.from_float(float(x))
def floor(q):q=Q(q);return q.numerator*S//q.denominator
def up(q):q=Q(q);return Q(-((-q.numerator*S)//q.denominator),S)
def packet(q):return {'upper_exact':str(up(q)),'display':float(up(q))}

class Poly:
 """Real Laurent or real cosine/sine coefficients, denominator S, l1 error."""
 def __init__(self,c,error=Q(0)):
  self.c={int(k):int(v) for k,v in c.items() if v};self.e=Q(error)
 @classmethod
 def exact(cls,c):
  r={int(k):floor(v) for k,v in c.items() if v}
  return cls(r,sum((abs(v-Q(r.get(k,0),S)) for k,v in c.items()),Q(0)))
 def l1(self):return Q(sum(abs(v) for v in self.c.values()),S)+self.e
 def scale(self,q):
  q=Q(q);return Poly.exact({k:q*Q(v,S) for k,v in self.c.items()}).add_error(abs(q)*self.e)
 def add_error(self,e):return Poly(self.c,self.e+e)
 def __add__(self,b):
  out=self.c.copy()
  for k,v in b.c.items():out[k]=out.get(k,0)+v
  return Poly(out,self.e+b.e)
 def __sub__(self,b):return self+b.scale(-1)
 def times(self,b):
  out={}
  for k,v in self.c.items():
   for j,w in b.c.items():out[k+j]=out.get(k+j,0)+v*w
  p=Poly.exact({k:Q(v,S*S) for k,v in out.items()})
  # Algebraic product enclosure relative to exact underlying polynomials.
  return p.add_error(self.e*Q(sum(abs(v) for v in b.c.values()),S)+b.e*self.l1())
 def cosine(self):
  out={0:self.c.get(0,0)}
  for k in sorted(set(abs(k) for k in self.c if k)):out[k]=self.c.get(k,0)+self.c.get(-k,0)
  return Poly(out,self.e)
 def sine(self):
  out={}
  for k in sorted(set(abs(k) for k in self.c if k)):out[k]=self.c.get(k,0)-self.c.get(-k,0)
  return Poly(out,self.e)

def phase_laurent(beta,degree):
 c={}
 for n in range(degree+1):
  for j in range(n+1):
   k=n-2*j;c[k]=c.get(k,Q(0))+(-1)**j*Q(math.comb(n,j),math.factorial(n))*(beta/2)**n
 remainder=beta**(degree+1)/(math.factorial(degree+1)*(1-beta))
 return Poly.exact(c).add_error(remainder),remainder

class Angular:
 def __init__(self,old,cert,cells,degree):
  self.base=old.AngularBoxes(cert,cells,degree);self.cert=cert;self.cache={}
 def enclose(self,poly,sine=False):
  modes=tuple(sorted(poly.c));key=(modes,sine);A=self.base
  if key not in self.cache:
   boxes=[]
   for cell in range(A.cells):
    derivatives=[]
    for d in range(A.degree):
     terms=[]
     for m in modes:
      sl,sh,cl,ch=A.trig[(m*(2*cell+1))%(4*A.cells)]
      if sine:
       choices=((sl,sh),(cl,ch),(-sh,-sl),(-ch,-cl))
      else:choices=((cl,ch),(-sh,-sl),(-ch,-cl),(sl,sh))
      lo,hi=choices[d%4];terms.append((lo*m**d,hi*m**d))
     derivatives.append(terms)
    boxes.append(derivatives)
   self.cache[key]=boxes
  coeff=[poly.c[m] for m in modes]
  rem=sum(abs(c)*m**A.degree for c,m in zip(coeff,modes))*A.weights[A.degree]
  error=-((-poly.e.numerator*S)//poly.e.denominator)
  out=[]
  for box in self.cache[key]:
   variation=rem;blo=bhi=0
   for d,terms in enumerate(box):
    lo=sum(c*(a if c>=0 else b) for c,(a,b) in zip(coeff,terms));hi=sum(c*(b if c>=0 else a) for c,(a,b) in zip(coeff,terms))
    if d==0:blo,bhi=lo,hi
    else:variation+=-((-max(abs(lo),abs(hi))*A.weights[d])//S)
   out.append((Q((blo-variation)//S-error,S),Q(-((-(bhi+variation))//S)+error,S)))
  return out

def rho_times_sine(poly,e0):
 out={k:Q(v,S) for k,v in poly.c.items()}
 for k,v in poly.c.items():
  for j in (k-1,k+1):
   if j:out[j]=out.get(j,Q(0))-e0*Q(v,2*S)
 return Poly.exact(out).add_error((1+e0)*poly.e)

def row_polys(row,drow,pm,zm,phase,e0,w0,T_h0,r0):
 P=len(pm)
 wp=Poly.exact({(int(m)-1)//3:c for m,c in zip(pm,row[:P])})
 dz=Poly.exact({(int(m)-1)//3:c for m,c in zip(pm,drow[:P])})
 wt=Poly.exact({(int(m)-1)//3:int(m)*c for m,c in zip(pm,row[:P])})
 hz=Poly.exact({int(m)//3:c for m,c in zip(zm,drow[P:])})
 ht=Poly.exact({int(m)//3:-int(m)*c for m,c in zip(zm,row[P:]) if m})
 Rz=phase.times(dz);Rt=phase.times(wt)
 A=Rz.cosine()-hz.scale(w0)
 B=Rt.cosine()
 Ath=Rt.sine().scale(-1)-ht.scale(w0)
 Cz=Rz.sine()
 N=rho_times_sine(Cz,e0).scale(r0)-Ath.scale(T_h0)
 return A,B,N,{'A_theta_upper':Ath.l1(),'C_z_upper':Cz.l1(),'height_z_upper':hz.l1(),'height_theta_upper':ht.l1()}

class TailCross:
 def __init__(self,args,old,cert,metric,change,query,fine):
  self.args,self.old,self.cert,self.metric=args,old,cert,metric
  self.angular=Angular(old,cert,args.angular_cells,args.taylor_degree)
  self.e0=1-Q(change['central_original_chart_rho_lower_exact']);self.rhomin=1-self.e0
  self.phase,self.phase_rem=phase_laurent(self.e0/3,args.phase_degree)
  rho=Poly.exact({0:Q(1),1:-self.e0});self.rhobox=[max(self.rhomin,lo) for lo,hi in self.angular.enclose(rho)]
  arc=change['central_arc_and_partial_primitive_proof'];alo=Q(arc['mean_arc_radius_lower_exact']);ahi=Q(arc['mean_arc_radius_upper_exact'])
  self.phase_error=Q(arc['degree_one_angle_lift_difference_upper'])
  J=Q(change['central_speed_lower_exact']);D=Q(change['central_source_constants']['central_metric_defect_l1']['upper_exact']);H=D/(J+self.rhomin)
  self.angular_scale_error=max(abs(alo-1),abs(ahi-1))/J+H/(J*self.rhomin)
  self.p=(Q(fine['target_orthonormal_differential_Frobenius_upper']['upper_exact']) if fine is not None
          else Q(change['target_orthonormal_differential_l1_upper']))
  self.global_p_source='same-field-R236-Frobenius' if fine is not None else 'same-field-R226-differential-l1-implies-Frobenius'
  self.local_norm_quick=Q(args.local_norm_quick)
  if self.local_norm_quick<=0:raise ValueError('Positive local norm work threshold required')
  order=json.loads(args.grid.read_text())['order']
  self.norm_angular=old.AngularBoxes(cert,args.angular_cells,args.taylor_degree,max_mode=max(48,2*order))
  speed,error=old.central_speed_polynomial(args.data)
  self.norm_denom=[max(old.floorfp(metric.Jmin**2),lo-error) for lo,hi in self.norm_angular.enclose(speed,S)]
  self.Wtheta=Q(change['raw_unit_chart_bounds']['(0, 1)']['upper_exact'])
  cb=query['continuous_original_source_second_jets']['component_bounds'];self.Vr=Q(cb['Vr']['upper_exact']);self.Vu=Q(cb['Vu']['upper_exact'])
  sys.path.insert(0,str(args.scripts))
  self.slope=load('certified_cross_slope_supplier',args.scripts/'db6f-tail-background-point-lipschitz.py')
  cal=args.scripts.parent/'notes/2026-11-09-db6f-tail-finite-source-calibrations.json'
  if sha(args.primitive)!=PRIMITIVE_SHA or sha(cal)!=CAL_SHA:raise ValueError('Different reviewed primitive/background calibration')
  self.bg=self.slope.supplier.Background(args.primitive,cal)
  witness=json.loads((args.scripts.parent/'notes/2026-11-09-db6f-root-tail-m8-point-metric-witness.json').read_text())
  if self.bg.data['inputs']!=witness['background_definition_hashes']:raise ValueError('Different reviewed source definition chain')
  for item in self.bg.data['inputs'].values():
   path=args.scripts.parent/item['file']
   # Historical checkpoint is not needed for source evaluation. All other
   # small defining reports are verified locally against the reviewed chain.
   if item is not self.bg.data['inputs'].get('checkpoint') and path.exists() and sha(path)!=item['sha256']:raise ValueError('Background definition file changed')
 def slope_enclosure(self,rl,rr):
  old,detail=self.slope.point_enclosure(self.bg,rl,rr)
  detail=dict(detail)
  profiles=[p for p in self.bg.profiles if p.n==detail['source_cell'] and p.j==detail['source_segment']]
  if len(profiles)!=1:raise ArithmeticError('Nonunique reviewed source proposal')
  profile=profiles[0];x=detail['source_x'];rp=profile.point(x)
  rlo,rhi=fq(rp.lo),fq(rp.hi)
  # The actual proposal radius and target interval lie in [cuff,cut].
  # Intersect only a known valid domain bound, never a sampled bracket.
  left=max(self.metric.cuff,min(rl,rlo));right=min(self.metric.c,max(rr,rhi))
  if left>right:raise ArithmeticError('Empty exact physical connection')
  # Keep the original exact 601/100 inner bound. The old derivative_range
  # has a binary64 convenience endpoint there; it is not needed here.
  if self.bg.inner_threshold is None or left<Q(self.bg.inner_threshold):
   detail['local_derivative_refinement_used']=False
   return old,detail
  wr=self.bg.derivative_range(left,right)
  K=min(Q(24),max(abs(fq(wr.lo)),abs(fq(wr.hi))))
  distance=max(abs(a-b) for a in [rl,rr] for b in [rlo,rhi])
  value=self.bg.source.evaluate(profile.n,profile.j,self.slope.Jet.variable(self.slope.I(x),0))['w'].c[0]
  error=self.slope.qbounds(K*distance);new=value+self.slope.I(-float(error.hi),float(error.hi))
  low=max(fq(old.lo),fq(new.lo));high=min(fq(old.hi),fq(new.hi))
  if low>high:raise ArithmeticError('Independent valid w enclosures disagree')
  # Every returned endpoint is already binary64 and exactly representable.
  enclosed=self.slope.I(float(low),float(high))
  detail.update(local_derivative_refinement_used=True,
    exact_connection_interval=[str(left),str(right)],
    exact_local_w_r_interval=[str(fq(wr.lo)),str(fq(wr.hi))],
    local_derivative_bound_exact=str(K),
    local_point_distance_exact=str(distance))
  return enclosed,detail
 def scales(self,lo,hi):
  m=self.metric;I=self.cert.I
  if lo*m.Tlo<m.Shi:raise ValueError('Cross-Gram tail piece reaches the prefix; use the full original prefix route')
  a=max(Q(0),(lo*m.h-(1-lo)*m.Shi)/m.h);b=min(Q(1),(hi*m.h-(1-hi)*m.Slo)/m.h)
  R=self.old.interval_polynomial(m.co,a,b,I);r=I(m.c)-m.h*R
  hh=self.old.interval_polynomial(m.first,a,b,I);T=I(m.Tlo,m.Thi);Th=T*hh
  rl=max(m.cuff,r.lower());rr=min(m.c,r.upper())
  if rl>rr or hh.lower()<=0:raise ArithmeticError('Invalid positive exact radial scales')
  supplied,detail=self.slope_enclosure(rl,rr)
  wl=max(Q(0),fq(supplied.lo));wh=min(Q(16,15),fq(supplied.hi))
  if wl>wh:raise ArithmeticError('Background point enclosure misses global range')
  w0=(wl+wh)/2;dw=(wh-wl)/2;r0=(rl+rr)/2;dr=(rr-rl)/2;Th0=(Th.lower()+Th.upper())/2;dTh=(Th.upper()-Th.lower())/2
  return {'rlo':rl,'rhi':rr,'wlo':wl,'whi':wh,'w0':w0,'dw':dw,'r0':r0,'dr':dr,
          'Thlo':Th.lower(),'Thhi':Th.upper(),'Th0':Th0,'dTh':dTh,'slope_receipt':detail}
 def piece(self,c,lo,hi,pm,zm):
  sc=self.scales(lo,hi);d=self.old.elevated_derivative(c,hi-lo);I=self.cert.I
  plocal,preceipt=self.old.one_piece_bound(c,lo,hi,pm,zm,self.metric,self.norm_angular,self.norm_denom,min(self.p,self.local_norm_quick),self.cert)
  p=min(self.p,plocal)
  En=1+sc['wlo']**2;rootE=I(En).sqrt().lower();rlo=sc['rlo'];Thlo=sc['Thlo']
  maxcross=Q(0);worst=None
  for i,(row,drow) in enumerate(zip(c,d)):
   A,B,N,z=row_polys(row,drow,pm,zm,self.phase,self.e0,sc['w0'],sc['Th0'],sc['r0'])
   erA=sc['dw']*z['height_z_upper']
   erN=sc['dr']*(1+self.e0)*z['C_z_upper']+sc['dTh']*z['A_theta_upper']+sc['Thhi']*sc['dw']*z['height_theta_upper']
   # Correlated Fourier numerators are formed before any angle enclosure.
   aa=self.angular.enclose(A);bb=self.angular.enclose(B);nn=self.angular.enclose(N,True)
   for j,(abox,bbox,nbox,rho) in enumerate(zip(aa,bb,nn,self.rhobox)):
    ee=2*(max(map(abs,abox))+erA)/(Thlo*En)
    gg=2*max(map(abs,bbox))/(rlo*rho)
    ff=(max(map(abs,nbox))+erN)/(Thlo*rlo*rho*rootE)
    cross=max(ee,gg)+ff
    if cross>maxcross:maxcross=cross;worst={'control':i,'angular_box':j,'E_upper':str(up(ee)),'F_upper':str(up(ff)),'G_upper':str(up(gg))}
  v=I(self.Vr**2+(self.Vu/rlo)**2).sqrt().upper()
  source_cross_remainder=2*v*p
  phase_remainder=2*self.phase_error*p+2*self.angular_scale_error*self.Wtheta/rlo
  eps=Q(257212,10**13)+maxcross+source_cross_remainder+p*p+phase_remainder
  return up(eps),{'unit_interval':[str(lo),str(hi)],'relative_metric_upper':str(up(eps)),
       'rotational_cross_Gram_operator_upper':str(up(maxcross)),'source_V_cross_remainder':str(up(source_cross_remainder)),
       'true_material_angle_and_speed_remainder':str(up(phase_remainder)),'quadratic_W_remainder':str(up(p*p)),
       'local_W_differential_upper':str(up(p)),'local_R236_W_receipt':preceipt,
       'radial_range':[str(sc['rlo']),str(sc['rhi'])],'slope_range':[str(sc['wlo']),str(sc['whi'])],
       'slope_receipt':sc['slope_receipt'],'worst_control_angle':worst}

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ('scripts','data','field','grid','result','correction-bounds','query-report','primitive','out'):
  ap.add_argument('--'+k,type=Path,required=True)
 ap.add_argument('--fine-metric',type=Path);ap.add_argument('--local-norm-quick',default='0.00001')
 ap.add_argument('--elements',type=int,nargs='+');ap.add_argument('--radial-depth',type=int,default=2)
 ap.add_argument('--full-surface',action='store_true');ap.add_argument('--max-radial-depth',type=int,default=7);ap.add_argument('--target',default='0.000001')
 ap.add_argument('--angular-cells',type=int,default=128);ap.add_argument('--taylor-degree',type=int,default=8);ap.add_argument('--phase-degree',type=int,default=18)
 args=ap.parse_args();began=time.monotonic()
 if args.out.exists():raise FileExistsError('Fresh continuous proof output required')
 old=load('cross_R236',args.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py');cert=load('cross_R220',args.scripts/'6a65-m12-r137-continuous-domain.py')
 if cert.BITS!=BITS:raise ValueError('Wrong fixed point precision')
 grid,result,change,query=[json.loads(p.read_text()) for p in (args.grid,args.result,args.correction_bounds,args.query_report)]
 fine=json.loads(args.fine_metric.read_text()) if args.fine_metric else None
 field_sha=sha(args.field);grid_sha=sha(args.grid)
 for r in [result,change]+([fine] if fine is not None else []):
  if r['field_sha256']!=field_sha or r['grid_sha256']!=grid_sha:raise ValueError('Different saved field')
 if sha(args.data)!=old.DATA_SHA or change['script_sha256']!=old.R226_SHA:raise ValueError('Wrong original source/R226 input')
 if result['query_report_sha256']!=sha(args.query_report) or query['endpoint_cache_sha256']!=result['query_cache_sha256']:raise ValueError('Different actual tail')
 if query.get('source_regularization') or query['manifest_sha256']!=old.MANIFEST_SHA:raise ValueError('This consumer is for the original X+C source only')
 if (not all(change['exact_zero_endpoint_jets']) or not change['continuous_all_knots_and_all_angles']
     or change['reference_only'] or not result['original_exact_metric_unchanged'] or not result['true_flat_cuff_included']
     or (fine is not None and not fine['continuous_all_basis_pieces_and_all_angles'])):
  raise ValueError('Missing original complete continuous field facts')
 notes=args.scripts.parent/'notes';paths=[notes/'2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json',notes/'2026-11-09-db6f-root-exact-bridge-m12.json',notes/'2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json']
 for p,s in zip(paths,[old.META_SHA,old.BRIDGE_SHA,old.MANIFEST_SHA]):
  if sha(p)!=s:raise ValueError('Changed original definition')
 metric=old.LocalMetric(*[json.loads(p.read_text()) for p in paths],change,cert)
 engine=TailCross(args,old,cert,metric,change,query,fine)
 with np.load(args.field,allow_pickle=False) as f:
  knots=list(map(fq,f['unit_knots']));coeff=[[fq(x) for x in row] for row in f['coefficients']];pm=f['planar_modes'].copy();zm=f['vertical_modes'].copy()
 if not np.array_equal(pm,np.arange(-grid['order'],grid['order']+1)*3+1) or not np.array_equal(zm,np.arange(grid['order']+1)*3):raise ValueError('Wrong original full D3 basis')
 pieces=old.extract_bezier(knots,coeff);saved=[]
 if args.full_surface==bool(args.elements):raise ValueError('Choose a complete surface or explicitly listed elements')
 elements=list(range(len(pieces))) if args.full_surface else args.elements
 threshold=Q(args.target);d0=Q(257212,10**13);quick=(threshold-d0)/(2*(1+d0))
 if quick<=0:raise ValueError('Target must leave positive original-source metric margin')
 pangular=old.AngularBoxes(cert,args.angular_cells,args.taylor_degree,max_mode=max(48,2*grid['order']))
 speed,error=old.central_speed_polynomial(args.data);denom=[max(old.floorfp(metric.Jmin**2),lo-error) for lo,hi in pangular.enclose(speed,S)]
 for element in elements:
  lo,hi,c=pieces[element];stack=[(lo,hi,c,0)]
  while stack:
   lo,hi,c,depth=stack.pop()
   split=not args.full_surface and depth<args.radial_depth
   if not split:
    if lo*metric.Tlo>=metric.Shi:
     eps,row=engine.piece(c,lo,hi,pm,zm);row['route']='exact-full-angular-background-cross-Gram'
    else:
     p,pr=old.one_piece_bound(c,lo,hi,pm,zm,metric,pangular,denom,quick,cert)
     eps=up(d0+2*(1+d0)*p+p*p)
     row={'unit_interval':[str(lo),str(hi)],'relative_metric_upper':str(eps),'route':'original-R236-local-prefix-transfer','prefix_receipt':pr}
    split=args.full_surface and eps>=threshold and depth<args.max_radial_depth
   if split:
    left,right=old.split_bezier(c);mid=(lo+hi)/2;stack.extend(((mid,hi,right,depth+1),(lo,mid,left,depth+1)));continue
   row.update(element=element,depth=depth);saved.append((eps,row))
   if not args.full_surface or len(saved)%20==0 or eps>=threshold:
    print(json.dumps({'element':element,'subpieces':len(saved),'last_relative_metric_upper':float(eps),'route':row['route'],'seconds':time.monotonic()-began}),flush=True)
 worst=max(saved,key=lambda x:x[0]);out={'schema':'2ecf-M12-actual-tail-cross-Gram-local-W-slope-R226-cap-continuous-budget-v4','script_sha256':sha(__file__),
  'field_sha256':field_sha,'grid_sha256':grid_sha,'solver_result_sha256':sha(args.result),'fine_metric_sha256':sha(args.fine_metric) if args.fine_metric else None,
  'global_p_budget_source':engine.global_p_source,'global_p_cap':packet(engine.p),'local_norm_quick_exact':str(engine.local_norm_quick),
  'correction_bounds_sha256':sha(args.correction_bounds),'query_report_sha256':sha(args.query_report),
  'primitive_sha256':sha(args.primitive),'original_target_metric_retained':True,'original_source_X_plus_C_retained':True,
  'Q_source_regularization_included':False,'all_angles_and_all_points_in_listed_intervals':True,
  'full_angular_B_W_cross_Gram_cancellation':True,'source_V_cross_terms_bounded_separately':True,'local_W_norm_used_for_V_cross_and_quadratic_terms':True,'certified_local_background_derivative_used_when_available':True,
  'R252_first_consumer_sha256':'197a6696eae4f14723ef92a09c9543f102c789fef95d02fe1a751075e9d8e28d',
  'full_surface_certificate':args.full_surface,'covers_complete_moving_half_and_fixed_cuffs_caps_by_original_identity':args.full_surface,'phase_Laurent_degree':args.phase_degree,'phase_Laurent_uniform_remainder':packet(engine.phase_rem),
  'material_phase_error':packet(engine.phase_error),'reciprocal_speed_error':packet(engine.angular_scale_error),
  'radial_elements':elements,'subpieces':len(saved),'angular_cells':args.angular_cells,'angular_Taylor_degree':args.taylor_degree,
  'relative_metric_upper':packet(worst[0]),'below_requested_metric_target':worst[0]<threshold,'requested_metric_target_exact':str(threshold),'worst_subpiece':worst[1],'all_subpieces':[r for e,r in saved],
  'exact_isometry_proved':False,'README_completion_claim':False,'seconds':time.monotonic()-began}
 args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps({'report':str(args.out),'metric_upper':float(worst[0]),'seconds':out['seconds']},indent=2))
if __name__=='__main__':main()
