#!/usr/bin/env python3
"""Outward true-integral background enclosure using monotone variation and C4 Simpson."""
import argparse, hashlib, json, math, time
from fractions import Fraction
from pathlib import Path
import mpmath as mp
p=argparse.ArgumentParser()
p.add_argument('--input',type=Path,required=True)
p.add_argument('--out',type=Path,required=True)
p.add_argument('--cells',type=int,default=32)
p.add_argument('--tol',default='1e-12')
p.add_argument('--variation-tol',default='1e-18')
p.add_argument('--max-depth',type=int,default=40)
args=p.parse_args()
mp.mp.dps=90
iv=mp.iv
iv.dps=60
data=json.loads(args.input.read_text())
cfg=data['parameters']
N=args.cells
assert 16<=N<=128 and cfg['protectCell']==160
assert cfg['orientation']==1 and cfg['curvatureBound']==8
assert cfg['prefixEnd']==15 and cfg['rejoinR20At'] is None
assert cfg['R']==64 and cfg['capMode']=='cut-preserving' and cfg['slopeCap']>0
assert all(c['R']==64 for c in data['cells'][16:])
assert not cfg.get('flatOuterThroughCell',False)
assert cfg['a']==2.75 and cfg['etaPower']==1.5
assert all(c['lengthScale']==1 for c in data['cells'])
assert all(.5<=c['calibrationAlpha']<=2 for c in data['cells'])
assert all(v==0 for v in cfg['valleyControls'][16:])
assert all(all(v==1 for v in row)for row in cfg.get('warpWeightLevels',[])[1:])
assert len(cfg.get('pulseCaps',[]))<=1 and len(cfg.get('valleyCaps',[]))<=1
Z=iv.mpf(0)
ONE=iv.mpf(1)
def lo(x):return mp.make_mpf(x._mpi_[0])
def hi(x):return mp.make_mpf(x._mpi_[1])
def I(a,b):
    assert a<=b
    return iv.mpf([a,b])
def point(x):return iv.mpf(x)
def q(x):
    f=Fraction(x) if isinstance(x,int) else Fraction.from_float(float(x))
    return iv.mpf(f.numerator)/f.denominator
def hull(xs):return I(min(lo(x)for x in xs),max(hi(x)for x in xs))
def clip(x,a,b):
    l,h=max(lo(x),mp.mpf(a)),min(hi(x),mp.mpf(b))
    if l>h:raise ArithmeticError('empty intersection')
    return I(l,h)
def mag(x):return max(abs(lo(x)),abs(hi(x)))
def width(x):return hi(x)-lo(x)
def symmetric(x):return I(-x,x)
def powi(x,n):
    y=ONE
    for _ in range(n):y*=x
    return y

class J:
    """Interval Taylor coefficients: j[k] encloses f^(k)/k! pointwise."""
    __slots__=('c',)
    def __init__(self,c):self.c=c
    @staticmethod
    def constant(x):return J([x,Z,Z,Z,Z])
    @staticmethod
    def var(x):return J([x,ONE,Z,Z,Z])
    def __add__(a,b):
        if not isinstance(b,J):b=J.constant(b)
        return J([a.c[k]+b.c[k] for k in range(5)])
    __radd__=__add__
    def __neg__(a):return J([-x for x in a.c])
    def __sub__(a,b):return a+-b
    def __rsub__(a,b):return -a+b
    def __mul__(a,b):
        if not isinstance(b,J):return J([x*b for x in a.c])
        return J([sum((a.c[k]*b.c[n-k]for k in range(n+1)),Z)for n in range(5)])
    __rmul__=__mul__
    def __truediv__(a,b):
        return a*b.power(-1) if isinstance(b,J) else J([x/b for x in a.c])
    def __pow__(a,n):
        if n==0:return J.constant(ONE)
        if n<0:return a.power(n)
        y=J.constant(ONE)
        for _ in range(n):y=y*a
        return y
    def exp(a):
        y=[iv.exp(a.c[0])]
        for n in range(1,5):
            y.append(sum((k*a.c[k]*y[n-k]for k in range(1,n+1)),Z)/n)
        return J(y)
    def power(a,p):
        assert lo(a.c[0])>0
        y=[a.c[0]**p]
        for n in range(1,5):
            y.append(sum((((p+1)*k-n)*a.c[k]*y[n-k]for k in range(1,n+1)),Z)/(n*a.c[0]))
        return J(y)
    def restrict_value(a,l,h):
        return J([clip(a.c[0],l,h)]+a.c[1:])

def jhull(xs):return J([hull([x.c[k]for x in xs])for k in range(5)])
def poly5(x):return x*x*x*(10+x*(-15+6*x))
def smooth(x):
    y=poly5(x)
    # Monotonicity of S5 supplies an exact value-range improvement.
    y.c[0]=clip(hull([poly5(point(lo(x.c[0]))),poly5(point(hi(x.c[0])))]),0,1)
    assert lo(x.c[1])==hi(x.c[1])==1 and all(lo(t)==hi(t)==0 for t in x.c[2:])
    v=x.c[0]
    y.c[1]=30*v*v*(1-v)*(1-v)
    y.c[2]=30*v*(1-v)*(1-2*v)
    y.c[3]=60*(v-q(.5))**2-5
    y.c[4]=30*v-15
    return y
def cap(raw,caplog):
    L=q(cfg['capTransition'])
    rel=raw-caplog
    out=[]
    if lo(rel.c[0])<=-lo(L):out.append(raw)
    if hi(rel.c[0])>=lo(L):out.append(caplog)
    if hi(rel.c[0])>=-hi(L) and lo(rel.c[0])<=hi(L):
        t=(rel+L)/(2*L)
        if lo(t.c[0])<=mp.mpf('.5') and hi(t.c[0])>=0:
            u=t.restrict_value(0,mp.mpf('.5'))
            v=u-u**5*(7+u*(-14+u*(10-u*q(2.5))))
            z=v*(2*L)+caplog-L
            def ds(t):return 1-t**4*(35+t*(-84+t*(70-20*t)))
            dd=clip(hull([ds(point(lo(u.c[0]))),ds(point(hi(u.c[0])))]),0,1)
            z.c[1]=dd*raw.c[1]+(1-dd)*caplog.c[1]
            out.append(z)
        if hi(t.c[0])>=mp.mpf('.5') and lo(t.c[0])<=1:
            u=1-t.restrict_value(mp.mpf('.5'),1)
            v=-(u**5*(7+u*(-14+u*(10-u*q(2.5)))))+q(.5)
            z=v*(2*L)+caplog-L
            def ds(t):return t**4*(35+t*(-84+t*(70-20*t)))
            dd=clip(hull([ds(point(lo(u.c[0]))),ds(point(hi(u.c[0])))]),0,1)
            z.c[1]=dd*raw.c[1]+(1-dd)*caplog.c[1]
            out.append(z)
    y=jhull(out)
    # Its actual pointwise value never exceeds the local cap.
    y.c[0]=I(lo(y.c[0]),min(hi(y.c[0]),hi(caplog.c[0])))
    return y

d0,c0=q(cfg['delta0']),q(cfg['etaRatioAtN0'])
eta0=d0*c0
aa=q(cfg['rCuff'])
cut,wcut=q(cfg['rCut']),q(cfg['wCut'])
ae=q(cfg['a'])
sqrt12=iv.sqrt(12)
two=iv.mpf(2)
etaratio=two**(-q(1.5))
Y=6*d0+6*eta0/(1-etaratio)
oldcut=aa*iv.exp(Y/sqrt12)
assert lo(aa)>mp.mpf(1)/25 and 0<lo(wcut)<=hi(wcut)<mp.mpf(1)/10
assert lo(d0)>=mp.mpf(1)/200 and hi(d0)<=mp.mpf(1)/160
assert lo(c0)>=mp.mpf(1)/25 and hi(c0)<=mp.mpf(1)/16
def source_radius(n):
    yy=6*d0*two**(-n)+6*eta0*two**(-q(1.5)*n)/(1-etaratio)
    return aa*iv.exp(yy/sqrt12)

class Piece:
    def __init__(self,n,j,offset):
        self.n,self.j=n,j
        self.transition=(j%2==1)
        self.k=(j-1)//2 if self.transition else j//2
        cell=data['cells'][n]
        delta=d0*two**(-n)
        c=c0*two**(-iv.mpf(n)/2)
        self.length=delta*(c if self.transition or j in(0,8)else 1)
        after=3*d0*two**(-n)+6*eta0*two**(-q(1.5)*(n+1))/(1-etaratio)
        ld=iv.ln(delta)
        values=[ld,iv.ln(q(cell['R'])),2*ld-iv.ln(q(cell['calibrationAlpha'])),Z,ld+ae*iv.ln(2)]
        self.z0=iv.ln(wcut)-ae*iv.ln(2*d0)+(ae-1)*ld+values[self.k]+7*(Y-after-offset)/sqrt12
        self.zs=(values[self.k+1]-values[self.k])if self.transition else Z
        beta=q(cfg['valleyControls'][n])
        if j==3:self.zs+=beta
        if j==4:self.z0+=beta
        if j==5:self.z0+=beta;self.zs-=beta
        self.zx=-7*self.length/sqrt12
        caps=[q(cfg['slopeCap'])]*5
        if n<len(cfg.get('pulseCaps',[])):
            caps[1],caps[3]=[q(t)for t in cfg['pulseCaps'][n]]
        if n<len(cfg.get('valleyCaps',[])):caps[2]=q(cfg['valleyCaps'][n])
        self.cap0=iv.ln(caps[self.k])
        self.caps=iv.ln(caps[self.k+1]/caps[self.k])if self.transition else Z
        weights=cfg.get('warpWeightLevels',[])
        levels=weights[n]if n<len(weights)else[1]*5
        self.weight0=q(levels[self.k])
        self.weights=iv.ln(q(levels[self.k+1])/self.weight0)if self.transition else Z
        self.r0=aa*iv.exp((after+offset)/sqrt12)
        self.rd=self.length/sqrt12
        self.outer=(n==0 and j==8)
        self.evals=0
    def zjet(self,x):
        S=smooth(x)
        raw=S*self.zs+x*self.zx+self.z0
        if self.outer:return raw,S
        capped=cap(raw,S*self.caps+self.cap0)
        if self.n==0 and self.j==7:return raw+(1-S)*(capped-raw),S
        return capped,S
    def fields(self,x):
        self.evals+=1
        z,S=self.zjet(x)
        w=z.exp()
        E=1+w*w
        rx=(x*self.rd).exp()*(self.r0*self.rd)
        weight=(S*self.weights).exp()*self.weight0
        B=rx*E.power(-1)*weight
        if self.outer:
            chi=1-S
            j0=S*(cut/oldcut-1)+1
            A=rx*j0*S+chi*(-self.zx/8)*w*E.power(q(-1.5))
            return [A,chi*B,w*A,chi*w*B]
        return [B,w*B]
    def primitive(self,x):
        z,_=self.zjet(J.var(point(x)))
        w=iv.exp(z.c[0]);root=iv.sqrt(1+w*w)
        return [w/root/8,-1/root/8]
    def variation(self,l,r,tol,depth=0):
        z,_=self.zjet(J.var(I(l,r)))
        dz=z.c[1]
        if lo(dz)>=0 or hi(dz)<=0:
            a,b=self.primitive(l),self.primitive(r)
            if lo(dz)>=0:return [b[k]-a[k]for k in range(2)]
            return [a[k]-b[k]for k in range(2)]
        w=iv.exp(z.c[0]);E=1+w*w
        upper=hi(abs(w*dz/(8*E*iv.sqrt(E)))*point(r-l))
        if upper<=tol or depth>=args.max_depth:
            if depth>=args.max_depth and upper>tol:raise ArithmeticError('variation depth exhausted')
            return [I(0,upper),I(0,hi(w*point(upper)))]
        m=(l+r)/2
        a=self.variation(l,m,tol,depth+1)
        b=self.variation(m,r,tol,depth+1)
        return [a[k]+b[k]for k in range(2)]
    def simpson(self,l,r,tol,depth=0):
        full=self.fields(J.var(I(l,r)))
        aa_=self.fields(J.var(point(l)))
        bb_=self.fields(J.var(point((l+r)/2)))
        cc_=self.fields(J.var(point(r)))
        h=r-l
        base=[(a.c[0]+4*b.c[0]+c.c[0])*h/6 for a,b,c in zip(aa_,bb_,cc_)]
        err=[hi(abs(v.c[4])*point(h)**5/120) for v in full]
        # Positive integrands; both range and Simpson enclosures are valid.
        padded=[b+symmetric(e)for b,e in zip(base,err)]
        ranges=[v.c[0]*point(h)for v in full]
        bounds=[I(max(mp.mpf(0),lo(b),lo(v)),min(hi(b),hi(v)))for b,v in zip(padded,ranges)]
        if max(width(b)for b in bounds)<=tol:return bounds
        if depth>=args.max_depth:raise ArithmeticError('Simpson depth exhausted')
        m=(l+r)/2
        a=self.simpson(l,m,tol/2,depth+1)
        b=self.simpson(m,r,tol/2,depth+1)
        return [a[k]+b[k]for k in range(len(a))]
started=time.monotonic()
tot=[Z,Z,Z,Z]
rows=[]
for n in range(N):
    row=[Z,Z,Z,Z]
    offset=Z
    for j in range(9):
        piece=Piece(n,j,offset)
        print(json.dumps(dict(stage='piece-start',n=n,j=j,seconds=time.monotonic()-started)),flush=True)
        tol=mp.mpf(args.tol)*mp.power(2,-n)/9
        if piece.outer:vals=piece.simpson(mp.mpf(0),mp.mpf(1),tol)
        else:
            va=piece.variation(mp.mpf(0),mp.mpf(1),mp.mpf(args.variation_tol)/9)
            print(json.dumps(dict(stage='variation-complete',n=n,j=j,widths=[float(width(x))for x in va],seconds=time.monotonic()-started)),flush=True)
            vb=piece.simpson(mp.mpf(0),mp.mpf(1),tol)
            vals=[va[0],vb[0],va[1],vb[1]]
        row=[a+b for a,b in zip(row,vals)]
        offset+=piece.length
        print(json.dumps(dict(n=n,j=j,evals=piece.evals,widths=[float(width(x))for x in vals],seconds=time.monotonic()-started)),flush=True)
    rows.append(row)
    tot=[a+b for a,b in zip(tot,row)]
# The unmodified deep tail, N<=n<160, uses no valley or weight edits.
WN=256*two**(-iv.mpf(7*N)/4)
HN=17+iv.mpf(7*N)/5
qq=iv.mpf(3)/10
TV=WN*((4*HN+1)/(1-qq)+(iv.mpf(28)/5)*qq/(1-qq)**2)
rN,r159,r160=source_radius(N),source_radius(159),source_radius(160)
# The only chi!=1 segment in this remainder lies in cell 159.
Arest=TV/8+(r159-r160)
Blo=(rN-r159)/(1+WN*WN)
Bhi=rN-r160
rem=[I(0,hi(Arest)),I(lo(Blo),hi(Bhi)),I(0,hi(WN*Arest)),I(0,hi(WN*Bhi))]
complete=[a+b for a,b in zip(tot,rem)]
normal=(cut-r160-complete[0])/complete[1]
deepheight=256*two**(-280)*(r160-aa)
height=complete[2]+normal*complete[3]+I(0,hi(deepheight))
inner=[sum((r[i]for r in rows[1:]),Z)+rem[i]for i in range(4)]
r1=r160+inner[0]+normal*inner[1]
def bound(z):
    l=0.0 if lo(z)==0 else math.nextafter(float(lo(z)),-math.inf)
    h=0.0 if hi(z)==0 else math.nextafter(float(hi(z)),math.inf)
    return dict(lower=l,upper=h,lower_exact=str(Fraction.from_float(l)),upper_exact=str(Fraction.from_float(h)),width=float(width(z)))
delta_alpha=point(mag(normal-q(data['physicalStats']['alpha'])))
rel_rx=delta_alpha/normal
rel_r=delta_alpha*complete[1]/r160
metric_gap=max(hi(2*rel_rx+rel_rx**2),hi(2*rel_r+rel_r**2))
res=dict(scope=__doc__,input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cells=N,tol=args.tol,variation_tol=args.variation_tol,interval_digits=iv.dps,complete_integrals={k:bound(x)for k,x in zip(['A','B','AH','BH'],complete)},exact_normalization=bound(normal),exact_height=bound(height),cell0_inner_radius=bound(r1),remainder={k:bound(x)for k,x in zip(['A','B','AH','BH'],rem)},js_reported_normalization=data['physicalStats']['alpha'],js_reported_height=data['physicalStats']['heightSpan'],normalization_error=bound(normal-q(data['physicalStats']['alpha'])),height_error=bound(height-q(data['physicalStats']['heightSpan'])),normalization_only_metric_gap=bound(I(0,metric_gap)),normalization_only_metric_scope='Same real A,B,w and deep anchor; replaces only exact normalization by the saved binary scalar. All pointwise profile quadrature/libm errors are excluded.',seconds=time.monotonic()-started)
args.out.write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res),flush=True)

