#!/usr/bin/env python3
"""Rational bounds for the physical short-meridian central radius and true cuff height, and exact stadium width of a nonzero field."""
import argparse,hashlib,json,math
from pathlib import Path
from fractions import Fraction as F
from math import comb

def trig(x,cos):
    # All inputs are in [-2,2]. The Lagrange remainder after degree 21 is at most 2^22/22!.
    assert abs(x)<=2
    q=sum(((-1)**k*x**(2*k+(not cos))/math.factorial(2*k+(not cos)) for k in range(11)),F(0))
    e=F(2**22,math.factorial(22));return q-e,q+e

def b(t,e):
    if t<e:return t*t/(2*e*(1-e))
    if t>1-e:return 1-(1-t)**2/(2*e*(1-e))
    return (t-e/2)/(1-e)

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser()
    for k in ('meridian','buffer','tail','manifest','state','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();mer=json.loads(a.meridian.read_bytes());buf=json.loads(a.buffer.read_bytes());tail=json.loads(a.tail.read_bytes());orig=json.loads(a.manifest.read_bytes());d=json.loads(a.state.read_bytes());row=mer['selected'][d['index']];assert d['meridianSHA256']==sha(a.meridian) and d['bufferSHA256']==sha(a.buffer) and mer['bufferSHA256']==sha(a.buffer);assert tail['oldManifest']==sha(a.manifest);assert F(tail['exactNewCuff'])==F(8,25);assert buf['protectedInputSHA256']==sha(a.tail);par=orig['parameters'];assert len(par['pulseCaps'])<=2 and len(par['valleyCaps'])<=2
    # The checked original quarter-radius plateau belongs to raw profile n2/j6. Further inward n>=2 all have the same cap.
    assert tail['finite'][0]['anchors'][0]['cell']==2 and tail['finite'][0]['anchors'][0]['profile']==6
    val=buf['choices'][0];e=F(mer['phaseEasing']);ph=list(map(F,row['phases']));ell=list(map(F,row['lengths']));co=list(map(F,d['correctedCoasts']));w=F(val['levels'][-1]);pl,pu=ph[-1]-F(1,2**44),ph[-1]+F(1,2**44)
    # cos(phi)+w sin(phi) is strictly increasing here and vanishes at phi=-atan(1/w).
    sl=trig(pl,False);cl=trig(pl,True);su=trig(pu,False);cu=trig(pu,True);assert cl[1]+w*sl[1]<0<cu[0]+w*su[0]
    N=128;rc=F(buf['outerRadius']);rad=[rc,rc];z=[F(0),F(0)]
    for j,L in enumerate(ell):
        da=ph[j+1]-ph[j];sv=cv=F(0);es=ec=F(0)
        for i in range(N):
            ang=ph[j]+da*b(F(2*i+1,2*N),e);sl,sh=trig(ang,False);cl,ch=trig(ang,True);sv+=(sl+sh)/2;cv+=(cl+ch)/2;es+=(sh-sl)/2;ec+=(ch-cl)/2
        # The real cut angle above may differ from the stored numerical proposal by 2^-44.
        q=abs(da)/(4*N*(1-e))+F(1,2**44);mid=L*sv/N;err=L*(es/N+q);rad=[rad[0]-mid-err,rad[1]-mid+err];mid=L*cv/N;err=L*(ec/N+q);z=[z[0]+mid-err,z[1]+mid+err]
        if j<len(co):
            sl,sh=trig(ph[j+1],False);cl,ch=trig(ph[j+1],True);rad=[rad[0]-co[j]*sh,rad[1]-co[j]*sl];z=[z[0]+co[j]*cl,z[1]+co[j]*ch]
    L=list(map(F,val['lengths']));ws=list(map(F,val['levels']));a0=F(tail['exactInnerSeam']);normalize=(rc-a0)/sum(L);buflo=normalize*sum(l*min(w1,w2) for l,w1,w2 in zip(L,ws,ws[1:]));bufhi=normalize*sum(l*max(w1,w2) for l,w1,w2 in zip(L,ws,ws[1:]));deep=F(par['slopeCap'])*(a0-F(8,25));Z=[z[0]+buflo,z[1]+bufhi+deep]
    power=d['stadiumPower'];mix=F(d['stadiumMix']);eps=F(d['epsilon']);bb=[F(2*(-1)**j*comb(2*power,power-j),comb(2*power,power)*(1-4*j*j)) for j in range(1,power+1)];D=sum(bb[::2]);cc=[mix*eps*v/D for v in bb];cc[0]+=(1-mix)*eps
    A=[q+sum(cc) for q in rad];B=[q+sum((-1)**j*v for j,v in enumerate(cc,1)) for q in rad];rh=[q-(1-mix)*3*eps-mix*eps/D for q in rad];assert A[0]>F(7,5) and B[1]<F(895,1000) and F(1,2)<Z[0]<Z[1]<F(61,100) and rh[0]>F(1,2)
    def pair(x):return [str(F(math.floor(q*10**10) if i==0 else math.ceil(q*10**10),10**10)) for i,q in enumerate(x)]
    out=dict(schema='rational-true-cuff-short-positive-m2-meridian-and-nonzero-stadium-central-dimensions',entry=sha(Path(__file__)),inputs={k:sha(getattr(a,k)) for k in ('meridian','buffer','tail','manifest','state')},centralRadius=pair(rad),cutHeight=pair(z),bufferHeight=pair([buflo,bufhi]),deepHeight=pair([F(0),deep]),actualCuffHeight=pair(Z),actualFlatRadius='8/25',centerMajorHalfWidth=pair(A),centerMinorHalfWidth=pair(B),centerRadiusOfCurvatureLower=pair(rh),exactWidthDifference=str(2*eps),centralMaxCurvatureUpper=str(F(1)/F(pair(rh)[0])),wholeSlabCertified=False,wholeReachCertified=False)
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print([(k,list(map(lambda q:float(F(q)),v))) for k,v in out.items() if isinstance(v,list)])
if __name__=='__main__':main()
