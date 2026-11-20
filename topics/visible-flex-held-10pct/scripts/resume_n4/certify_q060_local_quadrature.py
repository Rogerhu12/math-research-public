#!/usr/bin/env python3
"""Certify a uniform true-integrand primitive error for the literal G16 rule.

Cap jumps, approximate source critical splits, all initial panels, arbitrary
adaptive refinements, and the unchanged deep remainder are included. The
finite-constant algebra and IEEE/elementary evaluation of the original JS
program are separate unpaid layers, not silently identified with this rule.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,json,math,sys,time,types
import mpmath as mp
ap=argparse.ArgumentParser();ap.add_argument('--kernel',type=Path,required=True);ap.add_argument('--constants',type=Path,required=True)
ap.add_argument('--cache',type=Path,required=True);ap.add_argument('--peano',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
ap.add_argument('--normalization-certificate',type=Path,required=True)
ap.add_argument('--inspect-cells',type=int,default=32)
args=ap.parse_args();started=time.monotonic()
assert args.inspect_cells==32,'The complete published certificate uses exactly 32 explicit cells.'
src=args.kernel.read_text();assert hashlib.sha256(src.encode()).hexdigest()=='b7a8dc501dc3dbbe4ccb14d6b4ea2b4b85849d14b9551a94f5c23798d7985806'
src=src.split('\nstarted=time.monotonic()\n')[0]
src=src.replace('range(1,5)','range(1,ORDER+1)').replace('range(5)','range(ORDER+1)')
src=src.replace('J([x,Z,Z,Z,Z])','J([x]+[Z]*ORDER)').replace('J([x,ONE,Z,Z,Z])','J([x,ONE]+[Z]*(ORDER-1))')
mod=types.ModuleType('_q060_high_jet');mod.__dict__.update(ORDER=9,__file__=str(args.kernel))
saved=sys.argv;sys.argv=[str(args.kernel),'--input',str(args.constants),'--out','/dev/null','--cells','32']
exec(compile(src,str(args.kernel),'exec'),mod.__dict__);sys.argv=saved
iv=mod.iv;J=mod.J;Z=mod.Z;ONE=mod.ONE;lo=mod.lo;hi=mod.hi;I=mod.I;mag=mod.mag
def qi(t):
 t=Q(t);return iv.mpf(t.numerator)/t.denominator
def qi_range(l,r):return I(lo(qi(l)),hi(qi(r)))
def clampmax(x):return max(abs(lo(x)),abs(hi(x)))
pc=json.loads(args.peano.read_text());cache=json.loads(args.cache.read_text())
assert mod.cfg['warpSteps']==16
assert cache['parameters']==mod.cfg
assert cache['port_sha256']==mod.data['checkpoint_sha256']
assert cache['factory_sha256']==mod.data['factory_sha256']
mu=[qi(Q(x))for x in pc['moment_defects_exact']]
pk={r['order']:{'l1':qi(Q(r['l1_upper_exact'])),'sup':qi(Q(r['sup_upper_exact']))}for r in pc['peano_bounds']}
K=8
# Use the exact monotonicity of S5' on either side of 1/2.  This is a range
# improvement, not a derivative approximation or a new physical profile.
old_smooth=mod.smooth
def sharp_smooth(x):
 y=old_smooth(x);a,b=lo(x.c[0]),hi(x.c[0])
 vals=[30*mod.point(t)**2*(1-mod.point(t))**2 for t in(a,b)]
 low=min(lo(t)for t in vals);high=max(hi(t)for t in vals)
 if a<=mp.mpf('.5')<=b:high=max(high,mp.mpf(15)/8)
 y.c[1]=I(max(mp.mpf(0),low),high)
 return y
mod.smooth=sharp_smooth
old_zjet=mod.Piece.zjet
def stable_zjet(piece,x):
 z,S=old_zjet(piece,x)
 if piece.n==0 and piece.j==7:
  raw=S*piece.zs+x*piece.zx+piece.z0
  capped=mod.cap(raw,S*piece.caps+piece.cap0)
  delta=raw.c[0]-capped.c[0]
  delta=I(max(mp.mpf(0),lo(delta)),max(mp.mpf(0),hi(delta)))
  xx=x.c[0];P=10-15*xx+6*xx*xx
  # The source uses raw+(1-S5)*(cap-raw). Factor x^2 before
  # testing its derivative, so the exact flat endpoint is retained.
  z.c[1]=(1-S.c[0])*capped.c[1]+xx*xx*(xx*P*raw.c[1]+30*(1-xx)**2*delta)
 return z,S
mod.Piece.zjet=stable_zjet

def critical_coverage(piece,points):
 # Every possible absolute-value cusp must lie in one of these small
 # neighborhoods of an actual source split; cap plateaux are harmless.
 d=Q(1,10**10);bands=[];original_bands=[]
 for p in points:
  c=Q.from_float(p);a,b=max(Q(0),c-d),min(Q(1),c+d)
  original_bands.append((a,b))
  if bands and a<=bands[-1][1]:bands[-1]=(bands[-1][0],max(b,bands[-1][1]))
  else:bands.append((a,b))
 components=[];left=Q(0)
 for a,b in bands:
  if a>left:components.append((left,a))
  left=b
 if left<1:components.append((left,Q(1)))
 evals=0
 for a,b in components:
  stack=[(a,b,0)];signs=set()
  while stack:
   l,r,depth=stack.pop();evals+=1
   dz=piece.zjet(J.var(qi_range(l,r)))[0].c[1]
   if lo(dz)>=0:
    if hi(dz)>0:signs.add(1)
   elif hi(dz)<=0:
    if lo(dz)<0:signs.add(-1)
   else:
    if depth>=60:raise ArithmeticError('Uncovered critical neighborhood '+str((piece.n,piece.j,str(l),str(r))))
    m=(l+r)/2;stack.extend([(l,m,depth+1),(m,r,depth+1)])
  if len(signs)>1:raise ArithmeticError('Source misses a sign change '+str((piece.n,piece.j,str(a),str(b))))
 tau=qi(Q(pc['minimum_endpoint_node_distance_exact']))
 weights=qi(Q(pc['weight_sum_exact']))
 errors=[Z,Z,Z,Z]
 for l,r in original_bands:
  ff=fields(piece,J.var(qi_range(l,r)))
  # Wrong-sign strips have width at most d on each side of the source
  # split. Positive quadrature mass in one such strip is at most
  # W*d*(1+1/tau), independent of the subsequent adaptive partition.
  for ch in(0,2):errors[ch]+=4*abs(ff[ch].c[0])*qi(d)*(1+weights*(1+1/tau))
 return errors,evals,len(bands)
def fields(piece,x,z=None):
 if z is None:z,S=piece.zjet(x)
 else:_,S=piece.zjet(x)
 w=z.exp();E=1+w*w
 rx=(x*piece.rd).exp()*(piece.r0*piece.rd)
 weight=(S*piece.weights).exp()*piece.weight0
 B=rx*E.power(-1)*weight
 if piece.outer:
  chi=1-S;j0=S*(mod.cut/mod.oldcut-1)+1
  A=rx*j0*S+chi*(-piece.zx/8)*w*E.power(mod.q(-1.5));B=chi*B
 else:
  zp=J([(i+1)*z.c[i+1]for i in range(9)]+[Z])
  A=zp*w*E.power(mod.q(-1.5))/8
 return [A,B,w*A,w*B]
def poly_iv(c,x):
 v=Z
 for t in c[::-1]:v=v*x+t
 return v
def bernstein_iv(c,l,r):
 n=len(c)-1;aa=qi(l);h=qi(r-l)
 power=[sum((c[j]*math.comb(j,k)*aa**(j-k)*h**k for j in range(k,n+1)),Z)for k in range(n+1)]
 return [sum((power[j]*qi(Q(math.comb(k,j),math.comb(n,j)))for j in range(k+1)),Z)for k in range(n+1)]
def root_possible(c,l,r):
 b=bernstein_iv(c,l,r)
 return not(all(lo(x)>0 for x in b)or all(hi(x)<0 for x in b))
def root_boxes(c,l,r):
 stack=[(l,r)];boxes=[]
 while stack:
  a,b=stack.pop()
  if not root_possible(c,a,b):continue
  if b-a<Q(1,10**15):boxes.append((a,b));continue
  t=(a+b)/2;stack.extend([(a,t),(t,b)])
 # Adjacent unresolved boxes represent one root neighborhood. Retain a
 # conservative count bound of degree 5 if multiple roots coalesce.
 merged=[]
 for a,b in sorted(boxes):
  if merged and a<=merged[-1][1]:merged[-1]=(merged[-1][0],b)
  else:merged.append((a,b))
 return merged
def cap_jump(piece,side,l,r):
 x=J.var(qi_range(l,r));S=mod.smooth(x)
 raw=S*piece.zs+x*piece.zx+piece.z0
 cp=S*piece.caps+piece.cap0;L=mod.q(mod.cfg['capTransition'])
 raw.c[0]=cp.c[0]+side*L
 t=(raw-cp+L)/(2*L);t.c[0]=mod.point(0 if side<0 else 1)
 soft=cp-L+(t-t**5*(7+t*(-14+t*(10-t*mod.q(2.5)))))*(2*L)
 other=raw if side<0 else cp
 if piece.n==0 and piece.j==7:
  soft=raw+(1-S)*(soft-raw);other=raw+(1-S)*(other-raw)
 a,b=fields(piece,x,soft),fields(piece,x,other)
 # Both one-sided dlogw agree at the root. If its sign cannot be resolved
 # the sum is a valid bound for either choice made by the absolute value.
 dz=mod.hull([soft.c[1],other.c[1]])
 sign_resolved=lo(dz)>=0 or hi(dz)<=0
 out=[]
 for channel,(aa,bb)in enumerate(zip(a,b)):
  row=[]
  for j in range(K):
   if j<(4 if channel in(0,2)else 5):row.append(Z);continue
   if channel in(0,2)and not sign_resolved:
    row.append(abs(aa.c[j])+abs(bb.c[j]))
   else:row.append(abs(aa.c[j]-bb.c[j]))
  out.append(row)
 return out
total=[Z]*4;max_partial=[Z]*4;rows=[];cap_count=0;critical_total=[Z]*4
for n in range(args.inspect_cells):
 offset=Z
 for j in range(9):
  piece=mod.Piece(n,j,offset);offset+=piece.length
  crit=cache['rows'][n]['entries'][j]['breakpoints']
  assert crit==sorted(set(crit)) and all(0<t<1 for t in crit)
  critical_error,critical_evals,critical_bands=critical_coverage(piece,crit)
  grid=sorted(set([Q(k,16)for k in range(17)]+[Q.from_float(t)for t in crit]))
  caproots=[]
  if not piece.outer:
   rels=piece.zs-piece.caps
   for side in(-1,1):
    c=[piece.z0-piece.cap0-side*mod.q(mod.cfg['capTransition']),piece.zx,Z,10*rels,-15*rels,6*rels]
    for l,r in root_boxes(c,Q(0),Q(1)):
     caproots.append((side,l,r,cap_jump(piece,side,l,r)))
  errors=[Z]*4;remainder=[Z]*4;jump=[Z]*4
  for l,r in zip(grid,grid[1:]):
   h=qi(r-l);ff=fields(piece,J.var(qi_range(l,r)))
   for ch,v in enumerate(ff):
    err=sum((abs(mu[k])*h**(k+1)*abs(v.c[k])for k in range(K)),Z)
    err+=pk[K]['l1']*math.factorial(K)*h**(K+1)*abs(v.c[K])
    remainder[ch]+=I(0,hi(err));ee=err
    for side,a,b,diffs in caproots:
     if b<l or a>r:continue
     # A degree-five threshold polynomial has at most five roots in
     # any unresolved neighborhood; this deliberately allows overcount.
     ex=5*sum((pk[k+1]['sup']*math.factorial(k)*h**(k+1)*diffs[ch][k]for k in range(4 if ch in(0,2)else 5,K)),Z)
     jump[ch]+=I(0,hi(ex));ee+=ex
    errors[ch]+=I(0,hi(ee))
    max_partial[ch]=I(0,max(hi(max_partial[ch]),hi(ee)))
  total=[a+b+c for a,b,c in zip(total,errors,critical_error)]
  critical_total=[a+b for a,b in zip(critical_total,critical_error)];cap_count+=len(caproots)
  row={'n':n,'j':j,'cap_root_boxes':len(caproots),'source_critical_splits':len(crit),
   'remainder_upper':[float(hi(e))for e in remainder],'cap_jump_upper':[float(hi(e))for e in jump],
   'critical_displacement_upper':[float(hi(e))for e in critical_error],'critical_coverage_evaluations':critical_evals,
   'sum_initial_panels_upper':[float(hi(e))for e in errors]}
  rows.append(row)
  print(json.dumps(dict(stage='piece',**row,seconds=time.monotonic()-started)),flush=True)
# The unchanged tail is capped nowhere at n>=32.  Positivity and a sharp
# small-log-radius variation bound enclose every adaptive positive-rule
# partial integral, independently of the implementation's tolerance test.
deep=None
if args.inspect_cells==32:
 W=256*mod.two**(-56);H=mod.point(17)+mod.point(7*32)/5
 rr=mod.point(3)/10;ws=qi(Q(pc['weight_sum_exact']))
 radius32,radius159,radius160=[mod.source_radius(n)for n in(32,159,160)]
 span=radius32-radius159;last=radius159-radius160
 tv=W*((4*H+1)/(1-rr)+(mod.point(28)/5)*rr/(1-rr)**2)
 qa=ws*W/8*((mod.point(15)/2*H+1)/(1-rr)+(mod.point(21)/2)*rr/(1-rr)**2)
 lengthmax=mod.d0*mod.two**(-32)/mod.sqrt12
 qb_ratio=mod.hull([ws*iv.exp(-lengthmax)/(1+W*W)-1,ws*iv.exp(lengthmax)*(1+W*W)-1])
 deep=[tv/8+qa+(1+ws*iv.exp(lengthmax))*last,
       abs(qb_ratio)*span+(1+ws*iv.exp(lengthmax))*last,
       W*(tv/8+qa+(1+ws*iv.exp(lengthmax))*last),
       W*(1+ws*iv.exp(lengthmax))*(span+last)]
 total=[a+I(0,hi(b))for a,b in zip(total,deep)]
def upper_bound(v):
 h=math.nextafter(float(hi(v)),math.inf)
 return {'upper':h,'upper_exact':str(Q.from_float(h))}
normalization=json.loads(args.normalization_certificate.read_text())
assert normalization['input_sha256']==hashlib.sha256(args.constants.read_bytes()).hexdigest()
alpha=mod.q(mod.data['physicalStats']['alpha'])
radial_value_error=total[0]+alpha*total[1]
height_value_error=total[2]+alpha*total[3]
relative_r=radial_value_error/mod.aa
quadrature_metric_error=2*relative_r+relative_r**2
normalization_metric_error=qi(Q(normalization['normalization_only_metric_gap']['upper_exact']))
combined_metric_error=(1+quadrature_metric_error)*(1+normalization_metric_error)-1
result={'status':'uniform_real_integrand_quadrature_bound'if deep is not None else'piecewise_peano_terms_evaluated','complete_oracle_bound':False,
 'unpaid':['IEEE node formation, cached arithmetic and variable elementary evaluations','finite source-constant algebra versus the same true coefficient definition'],
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'constants_sha256':hashlib.sha256(args.constants.read_bytes()).hexdigest(),
 'inspect_cells':args.inspect_cells,'cap_root_boxes':cap_count,'sum_initial_panels_upper':[float(hi(e))for e in total],
 'critical_displacement_total_upper':[float(hi(e))for e in critical_total],
 'deep_remainder_upper':None if deep is None else[float(hi(e))for e in deep],
 'certified_primitive_errors':{key:upper_bound(value)for key,value in zip(['A','B','wA','wB'],total)},
 'fixed_binary_alpha_radius_value_error':upper_bound(radial_value_error),
 'fixed_binary_alpha_height_value_error':upper_bound(height_value_error),
 'quadrature_only_relative_metric_error':upper_bound(quadrature_metric_error),
 'quadrature_and_prior_normalization_relative_metric_error':upper_bound(combined_metric_error),
 'metric_comparison_scope':'Same source x and material angle; the exact hand derivative remains A+alpha B. This compares value/hand-jet oracles, not derivatives of the adaptive branch program.',
 'cache_sha256':hashlib.sha256(args.cache.read_bytes()).hexdigest(),
 'peano_sha256':hashlib.sha256(args.peano.read_bytes()).hexdigest(),
 'normalization_certificate_sha256':hashlib.sha256(args.normalization_certificate.read_bytes()).hexdigest(),
 'maximum_partial_panel_upper':[float(hi(e))for e in max_partial],
 'rows':rows,'seconds':time.monotonic()-started}
args.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='rows'}),flush=True)
