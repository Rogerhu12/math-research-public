#!/usr/bin/env python3
"""R127: exact complete 2-descent over Q(r), r^3-3r-4=0.
Standard library only; no GRH, floating roots, or external algebra system.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ONE=(1,0,0)
ZERO=(0,0,0)
ROOTS=[(82,0,-17),(7,-12,4),(-89,12,13)]
GENS=[(-1,0,0),(-7,1,1),(-2,1,0),(1,1,0),(3,1,-1)]
EPS=GENS[1]
BCOEFF=[(-3,5,-1),(6,-17,6),(3,18,-9),(-6,-1,2),(-3,-5,3)]

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def scale(a,c): return tuple(c*x for x in a)
def mul(a,b):
    t=[0]*5
    for i in range(3):
        for j in range(3): t[i+j]+=a[i]*b[j]
    for i in [4,3]:
        t[i-2]+=3*t[i]
        t[i-3]+=4*t[i]
    return tuple(t[:3])
def norm(a):
    x,y,z=a
    M=[[x,4*z,4*y],[y,x+3*z,3*y+4*z],[z,y,x+3*z]]
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def inv(a):
    cols=[mul(a,e) for e in [ONE,(0,1,0),(0,0,1)]]
    M=[[F(cols[j][i]) for j in range(3)]+[F(i==0)] for i in range(3)]
    for i in range(3):
        k=next(k for k in range(i,3) if M[k][i])
        M[i],M[k]=M[k],M[i]
        a=M[i][i]
        M[i]=[z/a for z in M[i]]
        for k in range(3):
            if k!=i:
                a=M[k][i]
                M[k]=[x-a*y for x,y in zip(M[k],M[i])]
    return tuple(M[i][3] for i in range(3))
def div(a,b): return mul(a,inv(b))
def vp(n,p):
    assert n
    v=0
    while n%p==0:
        n//=p
        v+=1
    return v,n

def padd(a,b):
    return [add(a[i] if i<len(a) else ZERO,b[i] if i<len(b) else ZERO)
            for i in range(max(len(a),len(b)))]
def pneg(a): return [neg(c) for c in a]
def psub(a,b): return padd(a,pneg(b))
def pscale(a,c): return [scale(v,c) for v in a]
def pmul(a,b):
    t=[ZERO]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): t[i+j]=add(t[i+j],mul(x,y))
    return t
def deriv(p): return [scale(p[i],i) for i in range(1,len(p))]
def ev(p,x):
    out=ZERO
    for c in reversed(p): out=add(scale(out,x),c)
    return out

def curve_checks():
    a,b,c,d,e=reversed(BCOEFF)
    I=add(sub(scale(mul(a,e),12),scale(mul(b,d),3)),mul(c,c))
    J=sub(add(scale(mul(mul(a,c),e),72),scale(mul(mul(b,c),d),9)),
          add(add(scale(mul(a,mul(d,d)),27),scale(mul(mul(b,b),e),27)),scale(mul(mul(c,c),c),2)))
    assert I==(369,-36,-54) and J==(5238,-5022,1134)
    zroots=[(-10,1,2),(-1,1,-1),(11,-2,-1)]
    assert [mul(EPS,z) for z in zroots]==ROOTS
    assert add(add(ROOTS[0],ROOTS[1]),ROOTS[2])==ZERO
    for z in zroots:
        assert sub(sub(scale(mul(mul(z,z),z),27),scale(mul(I,z),9)),J)==ZERO
    f=[mul(EPS,c) for c in BCOEFF]
    H=psub(pscale(pmul(f,deriv(deriv(f))),4),pscale(pmul(deriv(f),deriv(f)),3))
    G=psub(pmul(deriv(f),H),pmul(f,deriv(H)))
    prod=[ONE]
    for root in ROOTS:
        prod=pmul(prod,psub(pneg(H),[scale(mul(root,c),12) for c in f]))
    assert all(c==ZERO for c in psub(prod,pscale(pmul(G,G),3)))
    images=[]
    for x,bval in [(1,(1,2,1)),(-1,(1,4,1))]:
        y=mul(EPS,bval)
        assert ev(f,x)==mul(y,y)
        X=div(neg(ev(H,x)),scale(ev(f,x),12))
        Y=div(ev(G,x),scale(mul(mul(y,y),y),24))
        rhs=ONE
        for root in ROOTS: rhs=mul(rhs,sub(X,root))
        assert rhs==mul(Y,Y)
        images.append(dict(quartic_x=x,X=[str(c) for c in X],Y=[str(c) for c in Y]))
    assert images[0]['Y']==['0','0','0']
    assert images[1]['X']==['19','-108','181/4']
    assert images[1]['Y']==['2907/2','14625/8','-1134']
    norms=[norm(g) for g in GENS]
    assert norms==[-1,1,2,2,3]
    diffs=[dict(i=i,j=j,value=list(sub(ROOTS[i],ROOTS[j])),norm=norm(sub(ROOTS[i],ROOTS[j])))
           for i in range(3) for j in range(i)]
    assert [t['norm'] for t in diffs]==[-432,-27,1296]
    return dict(I_B=list(I),J_B=list(J),roots=[list(v) for v in ROOTS],
                generators=[list(v) for v in GENS],generator_norms=norms,
                root_differences=diffs,quartic_map_degree=4,quartic_point_images=images)


def real_checks():
    lo,hi=F(2195823,10**6),F(2195824,10**6)
    assert lo**3-3*lo-4<0<hi**3-3*hi-4 and lo>2
    # e1-e3 is decreasing; e3-e2 is increasing on this interval.
    assert 171-12*hi-30*hi*hi>0
    assert -96+24*lo+9*lo*lo>0
    assert -7+lo+lo*lo>0 and 3+hi-hi*hi>0
    return dict(root_interval=[str(lo),str(hi)],root_order=[2,3,1],
                generator_sign_bits=[1,0,0,0,0])


class LocalClasses:
    def __init__(self,N=48):
        self.N=N
        self.maxv2=0
        self.maxvi=0
        r0=0
        for k in range(1,N+4):
            mod=2**(k+1)
            if (r0**3-3*r0-4)%mod: r0+=2**k
            assert (r0**3-3*r0-4)%mod==0
        assert r0%4==0
        u=3*(r0//2)**2-3
        assert u%8==1
        sols=[1,3,5,7]
        for k in range(3,N+2):
            sols=[v for a in sols for v in [a,a+2**k] if (v*v-u)%2**(k+1)==0]
            assert len(sols)==4
        self.r0=r0
        self.rgi=(-r0//2,min(sols))
        ff=self.gadd(self.gadd(self.gmul(self.gmul(self.rgi,self.rgi),self.rgi),
                              tuple(-3*v for v in self.rgi)),(-4,0))
        assert all(v%2**N==0 for v in ff)
        units=sorted({self.gcanon((a,b)) for a in range(8) for b in range(8) if (a+b)%2})
        assert len(units)==8
        self.unitmap={self.gcanon((1,0)):0}
        self.unitbasis=[]
        for k in units:
            if k not in self.unitmap:
                bit=1<<len(self.unitbasis)
                self.unitbasis.append(k)
                self.unitmap.update({self.gmkey(a,k):v^bit for a,v in list(self.unitmap.items())})
        assert len(self.unitmap)==8
        assert [self.gdecode(k) for k in self.unitbasis]==[(3,0),(0,1),(2,1)]
        sq={self.gcanon(self.gmul((a,b),(a,b))) for a in range(8) for b in range(8) if (a+b)%2}
        # gcanon already identifies multiplication by -1, hence one square class.
        assert sq=={self.gcanon((1,0))}

    @staticmethod
    def gmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    @staticmethod
    def gadd(a,b): return (a[0]+b[0],a[1]+b[1])
    @staticmethod
    def gcanon(a):
        a,b=a[0]%8,a[1]%8
        return min(a+8*b,((-a)%8)+8*((-b)%8),((a+4)%8)+8*((b+4)%8),
                   ((-a+4)%8)+8*((-b+4)%8))
    @staticmethod
    def gdecode(k): return(k%8,k//8)
    def gmkey(self,a,b): return self.gcanon(self.gmul(self.gdecode(a),self.gdecode(b)))
    def at2(self,a):
        v=(a[0]+a[1]*self.r0+a[2]*self.r0*self.r0)%2**self.N
        assert v
        n,t=vp(v,2)
        assert n<self.N-4
        self.maxv2=max(self.maxv2,n)
        t%=8
        return(n%2)|((t in [3,7])<<1)|((t in [3,5])<<2)
    def ati(self,a):
        z=self.gadd(self.gadd((a[0],0),(a[1]*self.rgi[0],a[1]*self.rgi[1])),
                    tuple(a[2]*v for v in self.gmul(self.rgi,self.rgi)))
        v=0
        while (z[0]+z[1])%2==0:
            assert z!=(0,0)
            z=((z[0]+z[1])//2,(z[1]-z[0])//2)
            v+=1
        assert v<2*self.N-6
        self.maxvi=max(self.maxvi,v)
        return self.unitmap[self.gcanon(z)]|((v%2)<<3)
    @staticmethod
    def at3(a):
        n=vp(norm(a),3)[0]
        v=0
        while sum(a)%3==0:
            a=mul(a,(1,1,1))
            assert all(x%3==0 for x in a)
            a=tuple(x//3 for x in a)
            v+=1
            assert v<100
        assert n==v
        return(v%2)|((sum(a)%3==2)<<1)


def span(vs):
    s={0}
    for v in vs: s|={x^v for x in s}
    return s

def xor_mask(mask,vs):
    ans=0
    for j,v in enumerate(vs):
        if mask>>j&1: ans^=v
    return ans


def descent(N=48):
    lc=LocalClasses(N)
    places=[('P0_2',3,lc.at2),('P1_2',4,lc.ati),('P3_3',2,lc.at3)]
    point_specs={'P0_2':[((1,0,-1),4)],
                 'P1_2':[((0,0,-1),1),((0,0,1),1)],'P3_3':[]}
    local={}
    witnesses={}
    localgen={}
    for name,d,cl in places:
        vs=[]
        wi=[]
        for i in [0,1]:
            vals=[sub(ROOTS[i],ROOTS[j]) for j in range(3)]
            vals[i]=mul(vals[(i+1)%3],vals[(i+2)%3])
            keys=[cl(v) for v in vals]
            assert keys[0]^keys[1]^keys[2]==0
            v=keys[0]|(keys[1]<<d)
            vs.append(v)
            wi.append(dict(kind='torsion',index=i+1,three_classes=keys,pair_code=v))
        for coeff,den in point_specs[name]:
            assert den in (1,4)
            vals=[sub(coeff,scale(e,den)) for e in ROOTS]
            keys=[cl(a) for a in vals]
            assert keys[0]^keys[1]^keys[2]==0
            v=keys[0]|(keys[1]<<d)
            vs.append(v)
            wi.append(dict(kind='point',x_numerator=list(coeff),x_denominator=den,
                           three_classes=keys,pair_code=v))
        image=span(vs)
        assert len(image)==2**d
        local[name]=image
        witnesses[name]=wi
        localgen[name]=[cl(g) for g in GENS]
    remaining=[(a,b) for a in range(32) for b in range(32) if not(b&1)]
    counts=[['real',len(remaining)]]
    for name,d,cl in places:
        remaining=[(a,b) for a,b in remaining
                   if (xor_mask(a,localgen[name])|(xor_mask(b,localgen[name])<<d)) in local[name]]
        counts.append([name,len(remaining)])
    assert remaining==[(0,0),(0,18),(2,2),(2,16),(17,2),(17,16),(19,0),(19,18)]
    assert counts==[['real',512],['P0_2',64],['P1_2',8],['P3_3',8]]
    return dict(gaussian_unit_basis=[list(lc.gdecode(k)) for k in lc.unitbasis],
                local_generators=localgen,local_witnesses=witnesses,
                local_images={k:sorted(v) for k,v in local.items()},
                counts=counts,selmer_pairs=[list(v) for v in remaining],
                precision=dict(digits=N,max_v2=lc.maxv2,max_v_pi=lc.maxvi),
                selmer_dimension=3,rank_upper_bound=1)


def torsion_checks():
    cards=[]
    for p,rr in [(7,3),(11,8)]:
        assert (rr**3-3*rr-4)%p==0
        es=[sum(c*rr**i for i,c in enumerate(e))%p for e in ROOTS]
        assert len(set(es))==3
        card=1
        for x in range(p):
            val=1
            for e in es: val=val*(x-e)%p
            card+=1 if val==0 else 2 if pow(val,(p-1)//2,p)==1 else 0
        cards.append(dict(prime=p,r=rr,roots=es,cardinality=card))
    assert [c['cardinality'] for c in cards]==[8,16]
    return dict(reductions=cards,torsion_structure=[2,2],rank=1,
                non_torsion_point=dict(X=['19','-108','181/4'],Y=['2907/2','14625/8','-1134']),
                point_is_not_claimed_to_generate_the_full_free_group=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    a,b=descent(48),descent(24)
    aa,bb=dict(a),dict(b)
    del aa['precision'];del bb['precision']
    assert aa==bb
    payload=dict(curve=curve_checks(),real_place=real_checks(),descent=a,
                 independent_precision=24,torsion_and_rank=torsion_checks(),
                 scope=['complete local Kummer images, not a bounded search assertion',
                        'exact rank one, no assertion of Mordell-Weil saturation',
                        'no complete rational-x point classification'])
    encoded=json.dumps(payload,indent=2,sort_keys=True)+'\n'
    path=Path(__file__).with_name('r127_cubic_cover_rank_certificate.json')
    if args.check:
        assert path.read_text()==encoded
        print('R127 PASS: full local images, eight Selmer classes, exact rank one')
    else:
        path.write_text(encoded)
        print(path.name)
    print('certificate sha256',hashlib.sha256(encoded.encode()).hexdigest())

if __name__=='__main__':main()
