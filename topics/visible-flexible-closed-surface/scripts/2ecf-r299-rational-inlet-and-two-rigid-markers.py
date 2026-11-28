#!/usr/bin/env python3
"""Rational comparison of the true nonanalytic circular-arc inlet and two actual material marker tips."""
import argparse,json,math
from fractions import Fraction as F
from pathlib import Path
lo,hi=F(103993,33102),F(355,113);k0=F(1,5);h=d=F(1,2);mean=2*h+d;k=lambda p:(p-k0*mean)/(p-mean);kl,ku=k(hi),k(lo);scale=2**44
def rough(a,b):return F(math.floor(a*scale),scale),F(math.ceil(b*scale),scale)
def phase(v,kk):
    x=min(F(1),max(F(0),(v-h)/d));z=sum((-1)**i*math.comb(7,i)*x**(i+9)/((i+8)*(i+9)) for i in range(8))*51480
    return k0*v+(kk-k0)*(d*z+max(F(0),v-h-d))
def tr(t,c):
    z=sum((-1)**j*t**(2*j+(not c))/math.factorial(2*j+(not c)) for j in range(9));err=t**(18+(not c))/math.factorial(18+(not c));return rough(z-err,z)
def root(x,up):
    g=math.isqrt(x.numerator*scale**2//x.denominator);return F(g+(1 if up else 0),scale)
ap=argparse.ArgumentParser();ap.add_argument('--cells',type=int,default=256);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();N=a.cells;sn=[];cs=[]
for j in range(N+1):
    if j==0:sn.append((0,0));cs.append((1,1));continue
    if j==N:sn.append((1,1));cs.append((0,0));continue
    pl,ph=phase(lo*j/(2*N),kl),phase(hi*j/(2*N),ku);sn.append((tr(pl,False)[0],tr(ph,False)[1]));cs.append((tr(ph,True)[0],tr(pl,True)[1]))
AL=lo/(2*N)*sum(x[0] for x in sn[:-1]);AH=hi/(2*N)*sum(x[1] for x in sn[1:]);BL=lo/(2*N)*sum(x[0] for x in cs[1:]);BH=hi/(2*N)*sum(x[1] for x in cs[:-1])
def positive_interval_mul(a,b):return a[0]*b[0],a[1]*b[1]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def square(a):
    assert a[0]>0;return a[0]**2,a[1]**2
L=F(2);radius=(1/ku,1/kl);cc=tr(F(1,20),True);ss=tr(F(1,20),False);c1=(tr(ku/4,True)[0],tr(kl/4,True)[1]);s1=(tr(kl/4,False)[0],tr(ku/4,False)[1]);x=add((AL-5,AH-5),positive_interval_mul((7,7),cc));y=positive_interval_mul((7,7),ss);w=positive_interval_mul(add(radius,(L,L)),s1);v=add(sub((BL,BH),radius),positive_interval_mul(add(radius,(L,L)),c1))
xp=add(x,w);xm=sub(x,w);yp=sub(v,y);ym=add(v,y);dp=add(square(xp),square(yp));dm=add(square(xm),square(ym));initial=(root(dp[0],False),root(dp[1],True));end=(root(dm[0],False),root(dm[1],True));diff=sub(initial,end)
assert F(62,100)<AL<AH<F(64,100) and F(123,100)<BL<BH<F(125,100) and diff[0]>F(85,100)
pack=lambda q:list(map(str,q));out=dict(schema='R299-rational-closed-unit-speed-circular-arc-inlet-and-two-material-marker-distance',cells=N,centerA=pack((AL,AH)),centerB=pack((BL,BH)),highCurvature=pack((kl,ku)),relativeAngleHalfPhase=pack(((kl-k0)/2,(ku-k0)/2)),normalTipLength=str(L),initialMarkerPairDistance=pack(initial),finalMarkerPairDistance=pack(end),changeInMarkerPairDistance=pack(diff))
with a.out.open('x') as o:json.dump(out,o,indent=2);o.write('\n')
print([(k,list(map(lambda x:float(F(x)),v))) for k,v in out.items() if isinstance(v,list)])
