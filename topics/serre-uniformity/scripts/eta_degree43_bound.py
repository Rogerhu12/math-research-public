import argparse,json,pathlib,math,time,sys
sys.set_int_max_str_digits(0)
from fractions import Fraction as F
import mpmath as mp
P=pathlib.Path(__file__).resolve().parents[1]/'notes'
ap=argparse.ArgumentParser(description='Independent exact coefficient bound for R207')
ap.add_argument('--input',type=pathlib.Path,default=P/'eta_degree43_checkpoint_inputs.json')
ap.add_argument('--output',type=pathlib.Path,required=True)
args=ap.parse_args()
C=json.loads(args.input.read_text())
f=[0]*43
for j,c in enumerate(C['fEven']):f[2*j]=c
g=list(reversed(list(map(int,C['gDesc']))))
mp.mp.dps=120
bits=220;den=1<<bits
def ev(a,x):
 y=F(0)
 for c in reversed(a):y=y*x+c
 return y
def interval_mul(a,b):
 v=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]]
 return min(v),max(v)
def interval_eval(a,I):
 v=(F(0),F(0))
 for c in reversed(a):
  v=interval_mul(v,I);v=(v[0]+c,v[1]+c)
 return v
def ceil_log2(v):
 assert v>0
 n,d=v.numerator,v.denominator;k=n.bit_length()-d.bit_length()
 if k>=0:
  if n>d*(1<<k): k+=1
 else:
  if n*(1<<(-k))>d:k+=1
 return k
k=1;intervals=[];powers=[]
for j in range(42):
 x=2*mp.cos(2*mp.pi*k/172);n=int(mp.floor(x*den));I=(F(n,den),F(n+1,den))
 assert ev(f,I[0])*ev(f,I[1])<0
 a,b=interval_eval(g,I);J=((2-I[1])**22,(2-I[0])**22);a,b=interval_mul((a,b),J);upper=max(abs(a),abs(b));u=ceil_log2(upper)
 intervals.append({'index':j,'angle_index':k,'lo_num':str(n),'denominator_power':bits,'h_log2_upper':u});powers.append(u)
 k=(3*k+86)%172
assert k==1
s=sorted(int(r['lo_num']) for r in intervals);assert all(a+1<b for a,b in zip(s,s[1:]))
e=[x%43 for x in C['e']];assert sorted(e)==list(range(1,43))
loga=[sum(e[j]*powers[(i+j)%42] for j in range(42)) for i in range(42)]
alpha=[(n+42)//43 for n in loga]
R=sum(1<<n for n in alpha)
B=(R+1)**43
out={'scope':'R191 positive-exponent Gaussian trace theta, exact integer coefficient bound','intervals':intervals,'positive_exponents':e,'log2_a_upper':loga,'log2_alpha_upper':alpha,'theta_root_bound':str(R),'uniform_coefficient_bound':str(B),'bound_bits':B.bit_length(),'required_crt_bits':(2*B).bit_length()}
args.output.write_text(json.dumps(out,indent=2)+'\n')
print({'h_log2_bounds':powers,'alpha_bounds_range':[min(alpha),max(alpha)],'theta_bound_bits':R.bit_length(),'coefficient_bound_bits':B.bit_length()},flush=True)

