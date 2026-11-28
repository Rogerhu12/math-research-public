"""Directed interval transfer of two real end lines, with all valley parameters on each face."""
import hashlib
import math
from fractions import Fraction as F
from r734_true_dyadic_tail import I,D,ONE,ZERO,hull,sym,NEAR,monotone_trans,matrix_product,matrix_norm
from r735_paid_tail_beta_envelope import mv

hh=F('.56');rr=F('.018');tt=F('.006');e=F('.0002')
starts=tuple(map(F,('.081','.124','.167')))
mids=tuple(map(F,('.102','.145','.188')))
rim={-1:F('.075'),1:F('.22')};rho={-1:F(15,44),1:F(1)}
ed={-1:F(1,64),1:F(1,128)}
cut={s:rim[s]-s*rho[s]*ed[s] for s in (-1,1)}
iden=(ONE,ZERO,ZERO,ONE)


def iv(x):return I(x.numerator)/x.denominator


def exact_ramp(x):
    if x<=-e:return F(0)
    if x>=e:return x
    t=(x+e)/(2*e)
    return 280*e*t**5*(F(1,20)+t*(-F(1,10)+t*(F(1,14)-t/56)))


def central(r):
    for s in starts:
        if s-e<r<s+2*rr+tt+e:
            x=min(r-s,2*rr+tt-r+s)
            return hh/rr*(exact_ramp(x)-exact_ramp(x-rr))
    return F(0)


def weight(r,valley):
    h=iv(central(r));H=iv(hh)
    if mids[0]<=r<=mids[2]:v=valley[int(r>mids[1])]
    else:
        s=-1 if r<mids[0] else 1
        t=max(F(0),min(F(1),(abs(r-rim[s])-rho[s]*ed[s])/e))
        y=rho[s]*ed[s]+e*(t-t**4*(F(5,2)-3*t+t*t))
        w=iv((y/rho[s])**4/2);v=w/monotone_trans(1+w*w,'sqrt')
    a=v+(1-v/H)*h
    return a/monotone_trans(1-a*a,'sqrt')


def knots(s):
    a=[*cut.values(),cut[-1]+e,cut[1]-e,*mids]
    for t in starts:
        for c in (t,t+rr,t+rr+tt,t+2*rr+tt):a.extend((c-e,c+e))
    return sorted({z for z in a if (z<=mids[1] if s==-1 else z>=mids[1])},reverse=s==1)


def middle(q):return I(NEAR.divide(NEAR.add(q.hi,q.lo),D(2)))


def encode(a):
    return dict(c=[z.bounds() for z in a[0]],Q=[z.bounds() for z in a[1]],h=[z.bounds() for z in a[2]])


def decode(a):
    return tuple(tuple(I(*z) for z in a[key]) for key in ('c','Q','h'))


def pointbox(c,Q,h):
    w=mv(Q,h)
    return c[0]+w[0],c[1]+w[1]


def propagate(T,box):
    c,Q,h=box
    z=mv(T,c);p=tuple(middle(v) for v in z);A=matrix_product(T,Q)
    cols=[tuple(middle(A[i]) for i in ix) for ix in ((0,2),(1,3))]
    best=max(range(2),key=lambda t:max((a*I(h[t].norm())).norm() for a in cols[t]))
    u,v=cols[best];norm=max(u.norm(),v.norm())
    if not norm:u,v=ONE,ZERO
    else:u=middle(u/I(norm));v=middle(v/I(norm))
    B=(u,-v,v,u);d=u*u+v*v
    bi=tuple(t/d for t in (u,v,-v,u))
    eccentric=mv(bi,(z[0]-p[0],z[1]-p[1]));img=mv(matrix_product(bi,A),h)
    rad=tuple(sym((a+b).norm()) for a,b in zip(eccentric,img))
    return p,B,rad


def transfer(a,b,vals,j,inside=False):
    # Each elementary interval lies between exact monotonicity breakpoints.
    ws=hull(weight(a,vals),weight(b,vals));r=hull(iv(a),iv(b))
    if ws.lo<=0:raise ArithmeticError('Unresolved positive physical valley.')
    scale=middle(monotone_trans(I(ws.lo)*I(ws.hi),'sqrt'))
    h=iv(b-a)
    k=j*j;M=tuple(q*h/r for q in (I(k),scale/ws,-k*(k-1)*ws/scale,I(1-k)))
    z=I(matrix_norm(M))
    if z.hi>D('.22'):return None
    def polynomial(m):
        v=iden;t=iden
        for i in range(1,11):
            t=tuple(y/i for y in matrix_product(m,t));v=tuple(x+y for x,y in zip(v,t))
        tail=z**11/math.factorial(11)/(1-z/12)
        tt=tuple(a+sym(tail.hi) for a in v)
        return tt[0],tt[1]/scale,tt[2]*scale,tt[3]
    full=polynomial(M)
    return (full,polynomial(tuple(hull(ZERO,v) for v in M)),ws,r) if inside else full


def ray(ports,s,j,vals):
    d=I(*ports[s,j]['f_0_1_2'][1]);w=weight(cut[s],vals)
    v=w*(iv(cut[s])*d-j*j);m=middle(v)
    return (ONE,m),iden,(ZERO,sym((v-m).norm()))


def integral(X,Y,w,r):
    f,v=X;g,u=Y
    # r f'-4f=v/w, r g'-9g=u/w. Exact cancellation removes three large terms.
    return -(v*u/w**2-24*f*g)/(2*w*r**3)


def enc_state(book,ports,s,vals,depth,capture,modes):
    label=hashlib.sha256(repr([[(str(q.lo),str(q.hi)) for q in vals],s,depth,capture,modes]).encode()).hexdigest()[:24]
    states={j:ray(ports,s,j,vals) for j in modes};beta=ZERO
    fn=knots(s)
    def advance(a,b,d):
        nonlocal beta
        transfer_pair=[transfer(a,b,vals,j,capture) for j in modes]
        if any(v is None for v in transfer_pair):
            if d>=36:raise ArithmeticError('Could not enclose a single positive valley step.')
            c=(a+b)/2;advance(a,c,d+1);advance(c,b,d+1);return
        if capture:
            current=[mv(v[1],pointbox(*states[j])) for j,v in zip(modes,transfer_pair)]
            beta=beta+iv(abs(b-a))*integral(*current,transfer_pair[0][2],transfer_pair[0][3])
        for j,q in zip(modes,transfer_pair):
            states[j]=propagate(q[0] if capture else q,states[j])
    for i,(a,b) in enumerate(zip(fn,fn[1:])):
        # A full actual elementary piece at the requested bisection level is durable.
        for k in range(2**depth):
            l=a+(b-a)*F(k,2**depth);r=a+(b-a)*F(k+1,2**depth)
            key=f'enc_{label}_p{i}_z{k}'
            def step():
                advance(l,r,depth)
                return dict(states={str(j):encode(z) for j,z in states.items()},beta=beta.bounds())
            v=book.once(key,'directed_cell',step)
            states={j:decode(v['states'][str(j)]) for j in modes};beta=I(*v['beta'])
    return {j:pointbox(*z) for j,z in states.items()},beta


def paired(book,ports,vals,depth,capture,modes=(2,3)):
    if capture and tuple(modes)!=(2,3):raise ValueError('Signed mixed beta requires modes 2 and 3.')
    L,bb=enc_state(book,ports,-1,vals,depth,capture,modes);R,cc=enc_state(book,ports,1,vals,depth,capture,modes)
    W=iv(hh)/monotone_trans(1-iv(hh)**2,'sqrt')
    residual=[];ratio=[]
    for j in modes:
        a,b=L[j];c,d=R[j];b=b/W;d=d/W
        l2=a*a+b*b;r2=c*c+d*d
        if min(l2.lo,r2.lo)<=0:return None
        residual.append((a*d-b*c)/monotone_trans(l2*r2,'sqrt'))
        ratio.append((a*c+b*d)/r2)
    return dict(residual=residual,ratio=ratio,bulk_beta=(bb+ratio[0]*ratio[1]*cc if capture else ZERO))
