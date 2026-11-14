#!/usr/bin/env python3
"""Generate complete dyadic covers of every cusp and real q phase.

A leaf is proved by an integer-free modular-unit coordinate, an integer-free
j interval, or a j interval containing only one explicitly saved integer.
The last case creates a candidate for the separate exact arithmetic check.
"""
import sys,math,time,json,argparse,gzip,hashlib
from pathlib import Path
from fractions import Fraction
from flint import arb,arb_poly,fmpq,ctx
import numpy as np
from small_levels_real_unit_series import UnitCurve
def ab(x):return arb(fmpq(x.numerator,x.denominator)) if isinstance(x,Fraction) else arb(x)
def ilow(x):return int(x.lower().ceil().unique_fmpz())
def ihigh(x):return int(x.upper().floor().unique_fmpz())
def jball(I,negative):
 q=(-I).exp();r=q
 if negative:q=-q
 N=24
 E=arb(1)
 for n in range(1,N+1):E+=240*sum(d**3 for d in range(1,n+1) if n%d==0)*q**n
 # n^3 <= (N+1)^3 (n-N)^3 for n>=N+1.
 t=arb(r.upper());errE=480*(N+1)**3*t**(N+1)*(1+4*t+t*t)/(1-t)**4
 E+=arb(0,errE.upper())
 P=arb(1)
 for n in range(1,N+1):P*=(1-q**n)**(-24)
 errlog=24*t**(N+1)/(1-t)**2
 P*=arb(0,errlog.upper()).exp()
 return E**3*P/q

def cover(C,h):
 C.phase(h);p=C.p
 endpoint=arb.pi()*(arb(3).sqrt() if h%2 else 2)
 lower=Fraction(int((endpoint.lower()*2**64).floor().unique_fmpz()),2**64);upper=Fraction({41:246,47:282,59:354,83:508}[p])
 origin=lower;span=upper-lower
 stack=[(0,0,lower,upper)];leaves=[];cands=[];count=0;maxdepth=0;failed=0;start=time.time()
 while stack:
  depth,pos,a,b=stack.pop();width=float(b-a);mid=(a+b)/2
  count+=1;maxdepth=max(maxdepth,depth)

  values=C.value(float(mid));ders=C.derivative(float(mid))
  distances=abs(values-np.rint(values));order=sorted(range(1,C.d),key=lambda j:distances[j]/(abs(ders[j])*width/2+0.00001),reverse=True)
  I=ab(a).union(ab(b));t=(-I/p).exp();err=C.tail(ab(a));done=False
  # Use a few likely separating coordinates. The choice has no proof role.
  for j in order[:min(5,C.d-1)]:
   value=C.delta[j]*I+C.theta[j]+C.polys[j](t)+arb(0,err.upper())
   if ilow(value)>ihigh(value):leaves.append([depth,pos,j]);done=True;break
  if done:continue
  if width<1:
   J=jball(I,bool(h%2));lo,hi=ilow(J),ihigh(J)
   if lo>hi:leaves.append([depth,pos,-1]);continue
   if lo==hi:
    leaves.append([depth,pos,-2,str(lo)]);cands.append((lo,float(a),float(b)));continue
  if depth>=150:
   raise RuntimeError(('unresolved interval',p,C.c,h,depth,str(a),str(b)))
  stack.append((depth+1,2*pos+1,mid,b));stack.append((depth+1,2*pos,a,mid))
 return {'h':h,'endpoint_numerator':str(lower.numerator),'endpoint_denominator':str(lower.denominator),'upper':int(upper),'leaves':leaves}


def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--levels',default='41,47,59,83')
 parser.add_argument('--precision',type=int,default=256)
 parser.add_argument('--output-dir',type=Path,default=Path(__file__).with_name('data'))
 args=parser.parse_args();assert args.precision>=256
 data=Path(__file__).with_name('data')
 first=hashlib.sha256((data/'small_levels_archimedean_reduction.json').read_bytes()).hexdigest()
 tail=hashlib.sha256((data/'small_levels_archimedean_tail.json').read_bytes()).hexdigest()
 levels=list(map(int,args.levels.split(',')));assert levels and all(p in (41,47,59,83) for p in levels)
 args.output_dir.mkdir(parents=True,exist_ok=True)
 for p in levels:
  started=time.time()
  out={'version':1,'p':p,'precision_bits':args.precision,'terms':12*p,'first_reduction_sha256':first,'tail_sha256':tail,'cusps':[]}
  for c in range(1,(p-1)//2+1):
   curve=UnitCurve(p,c,bits=args.precision)
   branches=[cover(curve,h) for h in range(p+1)]
   out['cusps'].append({'c':c,'matrix':curve.matrix,'branches':branches})
   print(f'p={p}, cusp {c}/{(p-1)//2}: {sum(len(r["leaves"]) for r in branches)} proved leaves',flush=True)
  raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode()
  packed=gzip.compress(raw,mtime=0)
  destination=args.output_dir/f'small_levels_real_cover_p{p}.json.gz'
  destination.write_bytes(packed)
  print('COMPLETE',p,'bytes',len(packed),'SHA256',hashlib.sha256(packed).hexdigest(),'seconds',time.time()-started,flush=True)

if __name__=='__main__':main()
