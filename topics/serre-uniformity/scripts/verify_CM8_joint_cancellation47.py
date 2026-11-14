#!/usr/bin/env python3
"""Independent exact-rational and standard-library audit of the CM(-8) joint unit."""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path

Q=47**4;Q6=47**6;N=5
O,Z=(1,0),(0,0)
def read(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def padd(a,b,n=N):return [(a[k] if k<len(a) else F(0))+(b[k] if k<len(b) else F(0)) for k in range(n)]
def pscale(a,c,n=N):return [(a[k] if k<len(a) else F(0))*c for k in range(n)]
def pmul(a,b,n=N):return [sum((a[i]*b[k-i] for i in range(k+1) if i<len(a) and k-i<len(b)),F(0)) for k in range(n)]
def ppow(a,e,n=N):
 v=[F(1)]+[F(0)]*(n-1)
 for _ in range(e):v=pmul(v,a,n)
 return v
def pinv(a,n=N):
 v=[1/a[0]]
 for k in range(1,n):v.append(-v[0]*sum(a[i]*v[k-i] for i in range(1,k+1) if i<len(a)))
 return v
def compose(a,b,n=N):
 out=[F(0)]*n
 for c in reversed(a):out=pmul(out,b,n);out[0]+=c
 return out
def residue(x):return x.numerator*pow(x.denominator,-1,Q)%Q
def js(A,B):
 a=ppow(A,3);return pscale(pmul(a,pinv(padd(pscale(a,4),pscale(ppow(B,2),27)))),6912)
def add(a,b):return((a[0]+b[0])%Q,(a[1]+b[1])%Q)
def mul(a,b):return((a[0]*b[0]-a[1]*b[1])%Q,(a[0]*b[1]+a[1]*b[0])%Q)
def scale(a,k):return(a[0]*k%Q,a[1]*k%Q)
def inv(a):
 u=pow((a[0]*a[0]+a[1]*a[1])%Q,-1,Q);return(a[0]*u%Q,-a[1]*u%Q)
def power(a,n):
 v=O
 while n:
  if n&1:v=mul(v,a)
  a,n=mul(a,a),n//2
 return v
def log(a):
 t=add(power(a,2208),(-1,0));assert t[0]%47==t[1]%47==0
 return scale(add(add(t,scale(mul(t,t),-pow(2,-1,Q))),scale(power(t,3),pow(3,-1,Q))),pow(2208,-1,Q))
def evaluate(coeff,t):
 v=Z
 for c in reversed(coeff):v=add(mul(v,t),tuple(c))
 return v
def dot(row,column):
 v=Z
 for a,b in zip(row,column):v=add(v,mul(a,b[0]))
 return v

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['geometry','unit','support06','support18','cm-source','output']:ap.add_argument('--'+k,type=Path,required=True)
 args=ap.parse_args();geo=read(args.geometry);unit=read(args.unit);supports=[read(args.support06),read(args.support18)]
 assert geo['complete_two_actual_CM8_diagonal_level_and_unit_cancellations'] and not geo['complete_actual_local_heights']
 # Closed rational coefficients from 18u+12u^2+u^3+t=0, u=r-4.
 r=[F(4),-F(1,18),-F(1,486),-F(5,34992),-F(35,2834352)]
 A=[F(-30)]+[F(0)]*4;B=[F(56),F(1),F(0),F(0),F(0)]
 assert padd(padd(ppow(r,3),pmul(A,r)),B)==[F(0)]*5
 At=padd(A,pscale(padd(pscale(ppow(r,2),3),A),-5))
 Bt=padd(B,pscale(padd(padd(pscale(ppow(r,3),5),pscale(pmul(A,r),3)),pscale(B,2)),-7))
 source,target=js(A,B),js(At,Bt);assert source[0]==target[0]==8000 and target[1]==-source[1]
 U=pmul(padd(source,pscale(target,-1))[1:],pinv(source[1:],4),4)
 tj=[F(0),1/source[1],F(0),F(0),F(0)];delta=list(source);delta[0]=0
 for k in range(2,5):tj[k]=-compose(delta,tj)[k]/source[1]
 assert compose(delta,tj)==[F(0),F(1),F(0),F(0),F(0)]
 Uj=compose(U,tj,4)
 assert [residue(c) for c in r]==unit['kernel_r_coefficients_0to4_mod47four']
 assert [residue(c) for c in source]==unit['source_j_coefficients_0to4_in_t_mod47four']
 assert [residue(c) for c in target]==unit['target_j_coefficients_0to4_in_t_mod47four']
 assert [residue(c) for c in Uj]==unit['U_coefficients_0to3_in_Delta_j_mod47four']
 s=unit['source_Delta_j_mod47four'];uv=sum(residue(c)*pow(s,k,Q) for k,c in enumerate(Uj))%Q
 assert uv==unit['U_mod47four'] and log((uv,0))==(unit['log_U_mod47four'],0)
 for check in unit['independent_six_digit_Newton_checks']:
  A0,b,rr=check['A'],check['B_mod47six'],check['kernel_root_mod47six'];j=check['chosen_j_lift_mod47six']
  assert (rr**3+A0*rr+b)%Q6==0
  assert 6912*pow(A0,3,Q6)*pow((4*pow(A0,3,Q6)+27*b*b)%Q6,-1,Q6)%Q6==j
  aa=(A0-5*(3*rr*rr+A0))%Q6;bb=(b-7*(5*rr**3+3*A0*rr+2*b))%Q6
  jt=6912*pow(aa,3,Q6)*pow((4*pow(aa,3,Q6)+27*bb*bb)%Q6,-1,Q6)%Q6
  assert jt==check['target_j_mod47six']
  quotient=check['quotient_mod47five'];assert quotient*(j-8000)%Q6==(j-jt)%Q6 and quotient%Q==uv
 cm=read(args.cm_source)
 z8={v['label']:v['normalized_weight2_coefficients'][0] for v in cm['records'] if v['label'].startswith('Z_minus8_')}
 assert len(z8)==20
 key=lambda row:tuple(int(v)%47 for pair in row for v in pair)
 assert len({key(v) for v in z8.values()})==20
 checked=[]
 for rec,support in zip(geo['records'],supports):
  assert [label for label,W in z8.items() if key(W)==key(rec['source_W_fc_normalized'][0])]==[rec['exact_CM8_label']]
  assert z8[rec['exact_CM8_label']]==rec['actual_CM8_W_fc_normalized'][0]
  assert rec['disk_id']==support['source_disk_id'];br=rec['actual_same_disk_branch_0based'];raw=support['branch_records'][br]['actual_saved_full_level_record']
  assert raw['ell']==raw['degree']==raw['determinant_mod41']==2
  mat=raw['raw_level_matrix_mod41'];assert (mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0])%41==2
  aa,bb=map(tuple,[raw['source_A'],raw['source_B']]);kr=scale(raw['kernel'][0],-1)
  assert add(add(power(kr,3),mul(aa,kr)),bb)==Z
  at=add(scale(aa,-4),scale(power(kr,2),-15));bt=add(scale(bb,22),scale(mul(aa,kr),14))
  assert at==tuple(raw['A']) and bt==tuple(raw['B'])
  jt=scale(mul(power(at,3),inv(add(scale(power(at,3),4),scale(power(bt,2),27)))),6912)
  chartunits={};zetas={}
  for name,c in rec['charts'].items():
   wx=c['W_center'][0];wp=c['W_source_in_same_frame'][0];frame=c['frame'];coordinate=c['coordinate']
   assert dot(wx,frame)==dot(wp,frame)==O
   zeta=add(dot(wp,coordinate),scale(dot(wx,coordinate),-1));assert zeta==tuple(c['source_coordinate_displacement'][0][0]) and all(x%47==0 for x in zeta)
   WW=[v[0] for v in c['W_coefficients_0to4']]
   for k in range(73):assert evaluate([v[k] for v in WW],zeta)==tuple(wp[k])
   for k in range(1,5):assert dot(WW[k],frame)==Z and dot(WW[k],coordinate)==(O if k==1 else Z)
   jj=[tuple(v[0][0]) for v in c['j_coefficients_0to4']];dd=evaluate(jj[1:],zeta)
   assert dd==tuple(c['j_divided_difference_unit_mod47four'][0][0]) and (dd[0]*dd[0]+dd[1]*dd[1])%47
   assert add(jj[0],mul(zeta,dd))==(unit['source_j_mod47four'],0)
   assert jj[0]==((8000,0) if name=='CM8_fixed' else jt)
   chartunits[name]=dd;zetas[name]=zeta
  combined=mul((uv,0),mul(chartunits['CM8_fixed'],inv(chartunits['horizontal_target'])))
  assert combined==tuple(rec['combined_distinguished_chart_ratio_unit_mod47four'])
  assert log(combined)==tuple(rec['combined_distinguished_chart_ratio_log_mod47four'])
  assert mul(combined,zetas['CM8_fixed'])==zetas['horizontal_target']
  checked.append({'disk_id':rec['disk_id'],'actual_diagonal_branch':br,'actual_target_j_mod47four':jt[0],'four_digit_chart_ratio':combined[0],'four_digit_chart_ratio_log':log(combined)[0],'all73_jet_reconstructions_and_integral_divided_differences':True})
 out={'result':'R367','input_sha256':{str(p):sha(p) for p in [args.geometry,args.unit,args.support06,args.support18,args.cm_source]},'source_sha256':sha(__file__),
 'independent_exact_rational_kernel_coefficients':[[v.numerator,v.denominator] for v in r],
 'independent_exact_rational_U_coefficients_in_Delta_j':[[v.numerator,v.denominator] for v in Uj],
 'four_digit_series_equal_exact_rational_reduction':True,'two_distinct_six_digit_j_lifts_verified':True,
 'records':checked,'complete_independent_algebraic_unit_audit':True,'all20_Z8_points_distinct_mod47_and_exactly_one_in_each_selected_disk':True,'actual_height_computation_claimed':False,
 'scope':'Independent exact-rational formal series, six-digit finite-ring identities, actual saved det2/kernel/model branch, all73 chart reconstructions, unit divided differences and symbolic joint factor; no group chain or height evaluation.'}
 args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('PASS independent actual CM8 joint-unit audit',sha(args.output),flush=True)
if __name__=='__main__':main()
