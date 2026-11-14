#!/usr/bin/env python3
"""Actual finite94..184 node10 input through saved signed outer9..7 columns.

The input/columns use relative P=h_theta/(r*w), K=h_perp,r/w.  The
node10 prescribed nonlow height is zero.  This is a saved-data budget, not
a new ODE, and it does not assert the nonlinear continuation.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as F
import gzip, hashlib, json, resource, time
from pathlib import Path
from flint import arb, ctx

B=Path('/workspace/scratch/d1aa462cfc02')
PINS={
 'wide':(B/'root-work/r127/R163-actual-wide-nonlow-r1.json.gz','baf59b50716f8fcb5c8283213a27ae3188dc5a4cd86a99e8d05ad20ce337799e'),
 'wide_resource':(B/'root-work/r127/R163-actual-wide-nonlow-r1-resource.json','2e88f057b529a09572fc1b953ec584b5199dd7617d6a99cd0aa0c55a570f84b9'),
 'signed':(B/'exact-work/outer9to7-signed94to184-r1-summary.json.gz','bda654d0d8a4710ba927213e3482958838712c02fafea05bf10df8383de427b4'),
 'signed_resource':(B/'exact-work/outer9to7-signed94to184-run1-resource.json','eb213089a33fb50693929d8288de748fe968d2136e85e4882ba0a54374b81441'),
 'old':(B/'root-work/r127/R156-P-feedback-r1-certificate.json.gz','c9f38a066bcd9b62523acbaa6eb3ff696494883137329b3a58370ef17783a664'),
 'old_resource':(B/'root-work/r127/R156-P-feedback-r1-resource.json','fbbdde91e7b156aad63e73e6e468539012bcac3d777e1b9489b1681f44862829'),
 'node10':(B/'exact-work/outer9-signed-low46-r1.json','c19d33f403f42c0b98ada4572aa58f860f17d922cd5e353d680d477d75640c07'),
}
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 b=Path(p).read_bytes(); return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def ex(z):
 if isinstance(z,(F,int)):return F(z)
 if isinstance(z,dict):
  if 'upper' in z:return ex(z['upper'])
  return F(int(z['numerator']),int(z['denominator']))
 return F(int(z[0]))*F(2)**int(z[1])
def ab(z):
 z=ex(z);return arb(z.numerator)/arb(z.denominator)
def pack(z):
 z=z if isinstance(z,arb) else ab(z)
 if not z.is_finite() or z.upper()<0:raise ArithmeticError('finite nonnegative bound')
 u=z.upper()
 if u==0:return ['0',0]
 m,e=map(int,u.man_exp());s=max(0,m.bit_length()-160)
 if s:m,e=(m+(1<<s)-1)>>s,e+s
 if not arb(m)*arb(2)**e>=u:raise ArithmeticError('outward save')
 return [str(m),e]
def up(z):return ex(pack(z))
def ep(z):return up(ab(z).exp())
def support(a,c,m,p):
 """Nonnegative weights, per-window caps, total mass, first-pair mass."""
 ans=F(0);left=m;pair=p
 for w in sorted(range(len(a)),key=lambda k:a[k],reverse=True):
  take=min(c[w],left,pair if w<2 else left)
  ans+=a[w]*take;left-=take
  if w<2:pair-=take
 return ans
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);o=ap.parse_args()
 if o.out.exists():raise FileExistsError('fresh output required')
 ctx.prec,ctx.threads=256,1;start=time.monotonic();g={};d={}
 def gate(k,b):
  g[k]=bool(b)
  if not b:raise ArithmeticError(k)
 for k,(p,s) in PINS.items():gate('pin_'+k,sha(p)==s);d[k]=read(p)
 for k in ('wide_resource','signed_resource','old_resource'):
  gate('actual0_'+k,d[k]['exitcode']==0 and d[k]['termination_signal'] is None)
 wide,old,signed=d['wide'],d['old'],d['signed']
 gate('same_actual_complete_newwidth_field',wide['all_gates'] and wide['actual_complete_new_width_nonlow_field'] and wide['same_original_actual_full_field_identified'] and not wide['old_unknown_infinite_caps_reweighted'])
 gate('same_original_old_complete_field',old['all_gates'] and old['same_existing_R127_field'] and old['complete_mean_inverse_and_infinite_high_retained'])
 gate('all_saved_signed_modes',signed['all_gates'] and signed['modes']==list(range(94,185,2)))
 gate('actual_node10_block',wide['comparison_partition'][24]['cell']==10 and wide['comparison_partition'][24]['segment']==8)
 delta=F(wide['angular_shift']);gate('translation040',delta==F(2,5))
 V=ex(d['node10']['config']['local_V_node10'])
 windows=[w for w in old['windows'] if w[0]<=184]
 n=len(windows);oldcap=list(map(ex,old['window_caps'][24][:n]))
 oldmass=ex(old['finite_caps'][24]);newmass=ex(wide['finite_caps'][24]);parent=ex(old['retained_parent94_mass_caps'][24])
 gate('partition94to184',sum((list(range(a,b+1,2)) for a,b in windows),[])==list(range(94,185,2)) and windows[:2]==[[94,94],[96,96]])
 newcap=[min(newmass,up(c*ep(b*delta))) for c,(a,b) in zip(oldcap,windows)]
 newparent=min(newmass,up(parent*ep(96*delta)))
 rows=[]
 for cell in signed['cells']:
  cols=cell['homogeneous_whole_component_caps'];gate('all_columns_'+str(cell['cell']),[x['mode'] for x in cols]==list(range(94,185,2)))
  coeff={x['mode']:V*sum(map(ex,x['physical_K_initial']),F(0)) for x in cols}
  a=[max(coeff[m] for m in range(lo,hi+1,2)) for lo,hi in windows]
  b=[max(up(coeff[m]*ep(-m*delta)) for m in range(lo,hi+1,2)) for lo,hi in windows]
  common=up(newmass*max(b));old_only=up(support(a,oldcap,oldmass,parent));combined=up(support(b,newcap,newmass,newparent))
  group=up(sum((min(aa*cc,bb*dd) for aa,bb,cc,dd in zip(a,b,oldcap,newcap)),F(0)))
  best=min(common,old_only,combined,group)
  particular=ex(cell['whole_cell_radial_first_strong_particular'])
  rows.append(dict(cell=cell['cell'],new_common_only=pack(common),old_finite_window_support=pack(old_only),newwidth_finite_window_support=pack(combined),sum_per_window_intersections=pack(group),best_paid_initial=pack(best),fixed_centre_zero_entry_particular=pack(particular),sum_initial_and_fixed_particular=pack(up(best+particular)),window_initial_coefficients=list(map(pack,a)),newwidth_window_coefficients=list(map(pack,b))))
  print(json.dumps(dict(cell=cell['cell'],common=float(common),old=float(old_only),combined=float(combined),best=float(best),sum=float(best+particular))),flush=True)
 gate('rss_under96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 out=dict(schema='same-R163-node10-to-signed94to184-outer9to7-budget-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),inputs={k:dict(path=str(p),sha256=s) for k,(p,s) in PINS.items()},all_gates=all(g.values()),gates=g,gate_count=len(g),precision_bits=ctx.prec,coordinate_units='relative P=h_theta/(r*w), K=h_perp,r/w; original local V; no extra w',node10_P_nonlow_exactly_zero=True,node10_local_V=pack(V),input_angular_translation=str(delta),output_fixed_strip='1/64',windows=windows,old_window_caps=list(map(pack,oldcap)),new_window_caps=list(map(pack,newcap)),old_common_mass=pack(oldmass),new_common_mass=pack(newmass),old_parent94_mass=pack(parent),new_parent94_mass=pack(newparent),rows=rows,finite_input_only=True,unknown_infinite_initial_field_paid=False,nonlinear_feedback_paid=False,no_new_ODE=True,budget_failure_is_not_PDE_obstruction=True,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 o.out.write_text(json.dumps(out,separators=(',',':'))+'\n')
 print(json.dumps(dict(all_gates=True,sha256=sha(o.out),gate_count=len(g))),flush=True)
if __name__=='__main__':main()
