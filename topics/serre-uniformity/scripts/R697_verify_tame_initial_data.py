#!/usr/bin/env python3
"""Exact finite algebra of the fixed six-isogeny and R697 Bell initial data."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import comb
import argparse,json

Z=(F(0),)*6
def q(*a):return tuple(map(F,a))+(F(0),)*(6-len(a))
ONE=q(1);R=q(0,1);RR=q(0,0,1);B=q(0,0,0,1)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def scale(x,c):return tuple(a*F(c) for a in x)
def sub(x,y):return add(x,scale(y,-1))
def mul(x,y):
    z=[F(0)]*6
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            rd=i%3+j%3;bd=i//3+j//3
            z[rd%3+3*(bd%2)]+=a*b*4**(rd//3)*3**(bd//2)
    return tuple(z)
def power(x,n):
    y=ONE
    for _ in range(n):y=mul(y,x)
    return y
def sumq(xs):
    x=Z
    for y in xs:x=add(x,y)
    return x
def conj(x):return x[:3]+tuple(-a for a in x[3:])
def matrix(x):
    cols=[mul(x,q(*([0]*j+[1]))) for j in range(6)]
    return [[cols[j][i] for j in range(6)] for i in range(6)]
def inv(x):
    a=[row+[F(int(i==0))] for i,row in enumerate(matrix(x))]
    for k in range(6):
        j=next(j for j in range(k,6) if a[j][k]);a[j],a[k]=a[k],a[j]
        d=a[k][k];a[k]=[v/d for v in a[k]]
        for i in range(6):
            if i!=k:
                c=a[i][k];a[i]=[v-c*w for v,w in zip(a[i],a[k])]
    return tuple(row[-1] for row in a)
def norm(x):
    a=matrix(x);d=F(1)
    for k in range(6):
        j=next(j for j in range(k,6) if a[j][k])
        if j!=k:a[j],a[k]=a[k],a[j];d=-d
        pivot=a[k][k];d*=pivot
        for i in range(k+1,6):
            c=a[i][k]/pivot
            for j in range(k+1,6):a[i][j]-=c*a[k][j]
    return d
def out(x):return [str(a) for a in x]

def cx(a=Z,b=Z):return(a,b)
def ca(x,y):return(add(x[0],y[0]),add(x[1],y[1]))
def cs(x,y):return(sub(x[0],y[0]),sub(x[1],y[1]))
def cm(x,y):return(sub(mul(x[0],y[0]),mul(x[1],y[1])),add(mul(x[0],y[1]),mul(x[1],y[0])))
def cc(x,n):return(scale(x[0],n),scale(x[1],n))
def ci(x):
    d=inv(add(power(x[0],2),power(x[1],2)))
    return(mul(x[0],d),scale(mul(x[1],d),-1))
def cp(x,n):
    a=cx(ONE)
    for _ in range(n):a=cm(a,x)
    return a

def run():
    a=q(-375,-240,-180);c=q(-5566,-3360,-2100);s=q(5,4,2)
    X=q(2,1,1)
    assert a==scale(add(add(scale(power(X,2),2),scale(RR,2)),ONE),-15)
    assert c==sub(q(69),scale(add(add(scale(power(X,3),2),q(8)),ONE),35))
    xp=q(5,0,2,6,4,2);xm=conj(xp);x0=q(-10,0,-4)
    for x in [xp,xm,x0]:assert add(add(power(x,3),mul(a,x)),c)==Z
    xR=q(-3,-6,-3);yRi=q(-2,6,-3);eRi=q(-1,-1)
    assert add(add(add(power(xR,3),mul(a,xR)),c),power(yRi,2))==Z
    # Evaluate the complete six-isogeny and its derivative at the actual
    # original points (r*zeta,-b), and (zeta,0), without decimal recognition.
    zeta=cx(q(F(-1,2)),scale(B,F(1,2)))
    def phi(P):
        val=P;der=cx(ONE)
        for h,multiplicity in [(X,2),(R,2),(ONE,1)]:
            den=cs(P,cx(h));di=ci(den)
            num=ca(cp(P,3),cx(sub(power(h,3),q(2))))
            val=ca(val,cc(cs(cs(cm(num,cp(di,2)),P),cx(scale(h,2))),multiplicity))
            dn=cs(cm(cc(cp(P,2),3),den),cc(num,2))
            der=ca(der,cc(cs(cm(dn,cp(di,3)),cx(ONE)),multiplicity))
        return val,der
    P=cm(cx(R),zeta);yp=cx(scale(B,-1));ep=cc(cm(cx(mul(B,RR)),cp(zeta,2)),F(1,6))
    px,jac=phi(P)
    slopes=cx()
    for h,multiplicity in [(X,2),(R,2),(ONE,1)]:
        slopes=ca(slopes,cc(ci(cs(P,cx(h))),multiplicity))
    assert px==cx(xR) and cm(jac,yp)==cx(Z,yRi)
    assert ca(cc(ep,6),cm(yp,slopes))==cx(Z,eRi)
    assert phi(zeta)[0]==cx(x0)
    slope=mul(yRi,inv(sub(xR,xm)))
    x2=sub(sub(scale(power(slope,2),-1),xR),xm)
    y2i=add(scale(yRi,-1),mul(slope,sub(xR,x2)))
    e2i=add(eRi,slope)
    assert x2==q(-1,-6,-4,-6,2,1)
    assert y2i==q(12,-24,12,6,12,-9)
    assert e2i==q(1,1,F(-1,2),1,0,F(1,2))
    assert add(add(add(power(x2,3),mul(a,x2)),c),power(y2i,2))==Z
    f4=sub(add(add(scale(power(xp,2),-3),scale(mul(s,xp),6)),scale(power(s,2),3)),scale(a,2))
    assert f4==q(384,240,168,192,144,96)
    assert norm(f4)==2**26*3**10 and norm(e2i)==-648
    assert mul(f4,conj(f4))==scale(q(4,3,2),6912)
    assert mul(e2i,conj(e2i))==q(-6,0,-3)
    roots=[]
    for odd,N in [(False,16),(True,13)]:
        xs=[x2 if odd else xp];ys=[y2i if odd else Z];es=[e2i if odd else Z];fs=[ONE]
        for n in range(N):
            xx=sumq(scale(mul(xs[j],xs[n-j]),comb(n,j)) for j in range(n+1))
            yn=add(scale(xx,3),a if n==0 else Z)
            en=add(xs[n],s if n==0 else Z)
            fn=sumq(scale(mul(es[j],fs[n-j]),comb(n,j)) for j in range(n+1))
            xs.append(scale(ys[n],2));ys.append(scale(yn,-1 if odd else 1))
            es.append(scale(en,1 if odd else -1));fs.append(fn)
        for m in range(1 if odd else 4,N+1,6):
            base=fs[1] if odd else fs[4]
            fac=F((-1)**((m-1)//2),2**((m-1)//2)) if odd else F(6,2**((m-4)//2))
            root=scale(mul(fs[m],inv(base)),fac)
            assert all(x==0 for x in root[1:])
            roots.append({'k':m+1,'A_k':str(root[0])})
    return {'result':'R697','basis':['1','r','r^2','b','rb','r^2b'],
            'curve_and_tame_addition_identities':True,
            'complete_six_isogeny_original_point_evaluations':True,
            'norm_even_base':str(norm(f4)),'norm_odd_base_without_i':str(norm(e2i)),
            'exact_small_root_values':sorted(roots,key=lambda x:x['k']),
            'integrality_at_2_or_3_claimed':False,
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();r=run();a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
