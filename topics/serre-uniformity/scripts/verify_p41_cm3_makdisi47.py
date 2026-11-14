#!/usr/bin/env python3
"""Standard-library verification of the actual coarse CM jets in R105."""
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode=True
from verify_p41_local47_torsion import Ring, Curve
from verify_p41_makdisi47 import index, mm2, inv2, power_traces, qmatmul, qmul, qinv


class FastRing(Ring):
    """Exact Kronecker convolution and reversed monic polynomial division."""
    def __init__(self,f,q):
        super().__init__(f,q)
        self.bits=((self.n+1)*(q-1)**2).bit_length()
        self.mask=(1<<self.bits)-1
        rev=list(reversed(f))
        inverse=[1]
        for k in range(1,self.n-1):
            inverse.append(-sum(rev[j]*inverse[k-j] for j in range(1,k+1))%q)
        self.reciprocal=tuple(inverse)

    @lru_cache(maxsize=4096)
    def packed(self,a):
        return sum(x<<(self.bits*i) for i,x in enumerate(a))

    def convolution(self,a,b,length):
        value=self.packed(tuple(a))*self.packed(tuple(b))
        return [(value>>(self.bits*i)&self.mask)%self.q for i in range(length)]

    def mul(self,a,b):
        if a==self.zero or b==self.zero:return self.zero
        if a==self.one:return b
        if b==self.one:return a
        product=self.convolution(a,b,2*self.n-1)
        high=tuple(reversed(product[self.n:]))
        quotient=list(reversed(self.convolution(high,self.reciprocal,self.n-1)))
        lower=self.convolution(quotient,self.f,self.n)
        return tuple((x-y)%self.q for x,y in zip(product,lower))


class Jets:
    def __init__(self,r,order):
        self.r=r;self.n=order;self.q=r.q
        self.zero=(r.zero,)*order
        self.one=(r.one,)+(r.zero,)*(order-1)
        self.parameter=(r.zero,r.one)+(r.zero,)*(order-2)

    def constant(self,a):return (self.r.element(a),)+(self.r.zero,)*(self.n-1)
    def add(self,a,b):return tuple(self.r.add(x,y) for x,y in zip(a,b))
    def sub(self,a,b):return tuple(self.r.sub(x,y) for x,y in zip(a,b))
    def scale(self,a,c):return tuple(self.r.scale(x,c) for x in a)

    def mul(self,a,b):
        if a==self.zero or b==self.zero:return self.zero
        if a==self.one:return b
        if b==self.one:return a
        out=[self.r.zero]*self.n
        for i,x in enumerate(a):
            if x==self.r.zero:continue
            for j in range(self.n-i):
                if b[j]!=self.r.zero:out[i+j]=self.r.add(out[i+j],self.r.mul(x,b[j]))
        return tuple(out)

    def power(self,a,n):
        out=self.one
        while n:
            if n&1:out=self.mul(out,a)
            n//=2
            if n:a=self.mul(a,a)
        return out

    def inverse(self,a):
        b=self.constant(self.r.inverse(a[0]))
        precision=1
        while precision<self.n:
            b=self.mul(b,self.sub(self.constant(2),self.mul(a,b)))
            precision*=2
        assert self.mul(a,b)==self.one
        return b

    def rescale_parameter(self,a,c):
        power=self.r.one;out=[]
        for coefficient in a:
            out.append(self.r.mul(coefficient,power));power=self.r.mul(power,c)
        return tuple(out)


class JetCurve:
    def __init__(self,jets,A):self.j=jets;self.A=A

    def on_curve(self,P):
        if P is None:return True
        j=self.j;x,y=P
        return j.mul(y,y)==j.add(j.add(j.power(x,3),j.mul(self.A,x)),j.one)

    def add(self,P,Q):
        if P is None:return Q
        if Q is None:return P
        j=self.j;x,y=P;xx,yy=Q
        if x==xx:
            if j.add(y,yy)==j.zero:return None
            assert P==Q
            slope=j.mul(j.add(j.scale(j.mul(x,x),3),self.A),j.inverse(j.scale(y,2)))
        else:slope=j.mul(j.sub(yy,y),j.inverse(j.sub(xx,x)))
        zx=j.sub(j.sub(j.mul(slope,slope),x),xx)
        zy=j.sub(j.mul(slope,j.sub(x,zx)),y)
        return zx,zy

    def mul(self,P,n):
        if n<0:P=(P[0],self.j.scale(P[1],-1));n=-n
        out=None
        while n:
            if n&1:out=self.add(out,P)
            n//=2
            if n:P=self.add(P,P)
        return out


def eisenstein(j,P,Q):
    curve=JetCurve(j,j.parameter);Ps=[P];Qs=[Q]
    for _ in range(39):Ps.append(curve.add(Ps[-1],P));Qs.append(curve.add(Qs[-1],Q))
    numerators=[];denominators=[]
    for base,multiples in ((P,Ps),(Q,Qs)):
        for k in range(39):
            if k==0:
                numerators.append(j.add(j.scale(j.mul(base[0],base[0]),3),j.parameter))
                denominators.append(j.scale(base[1],2))
            else:
                numerators.append(j.sub(multiples[k][1],base[1]));denominators.append(j.sub(multiples[k][0],base[0]))
    for x,y in Ps:
        for xx,yy in Qs:numerators.append(j.sub(yy,y));denominators.append(j.sub(xx,x))
    prefix=[];product=j.one
    for d in denominators:
        assert any(c%47 for c in d[0])
        prefix.append(product);product=j.mul(product,d)
    inverse=j.inverse(product);slopes=[None]*len(denominators)
    for k in range(len(slopes)-1,-1,-1):
        slopes[k]=j.mul(numerators[k],j.mul(inverse,prefix[k]));inverse=j.mul(inverse,denominators[k])
    assert inverse==j.one
    def total(items):
        out=j.zero
        for item in items:out=j.add(out,item)
        return out
    ep=j.scale(total(slopes[:39]),pow(41,-1,j.q));eq=j.scale(total(slopes[39:78]),pow(41,-1,j.q))
    pe=[ep];qe=[eq]
    for k in range(39):
        pe.append(j.sub(j.add(pe[-1],ep),slopes[k]));qe.append(j.sub(j.add(qe[-1],eq),slopes[k+39]))
    assert pe[-1]==j.scale(ep,-1) and qe[-1]==j.scale(eq,-1)
    values=[j.zero]*1681
    for k in range(1,41):values[index(k,0)]=pe[k-1];values[index(0,k)]=qe[k-1]
    for a in range(1,41):
        for b in range(1,41):values[index(a,b)]=j.sub(j.add(pe[a-1],qe[b-1]),slopes[78+40*(a-1)+b-1])
    for a in range(41):
        for b in range(41):assert values[index(-a,-b)]==j.scale(values[index(a,b)],-1)
    print('All1680 formal weight-one values independently reconstructed.',flush=True)
    return values


def main(path):
    data=json.loads(path.read_text());q=data['modulus']
    assert data['level']==41 and data['auxiliary_prime']==47 and q==47**data['precision']
    torsion_bytes=path.with_name(data['torsion_source']).read_bytes()
    model_bytes=path.with_name(data['model_source']).read_bytes()
    assert hashlib.sha256(torsion_bytes).hexdigest()==data['torsion_source_sha256']
    assert hashlib.sha256(model_bytes).hexdigest()==data['model_source_sha256']
    torsion=json.loads(torsion_bytes);model=json.loads(gzip.decompress(model_bytes))
    cm=next(c for c in torsion['curves'] if c['label']=='CM_minus3')
    ref=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')
    f=torsion['field_polynomial_ascending'];r=FastRing(f,q);slow=Ring(f,q)
    ew=r.element(ref['weil_pairing']);ii=r.element(model['sqrt_minus_one_lift'])
    p0=tuple(r.element(v) for v in cm['P']);qold=tuple(r.element(v) for v in cm['Q'])
    for a,b in ((p0[0],p0[1]),(ew,ii),(qold[0],ew)):
        assert r.mul(a,b)==slow.mul(a,b)
    adjustment=data['pairing_adjustment'];assert adjustment==18
    assert r.power(r.element(cm['weil_pairing']),adjustment)==ew
    q0=Curve(r,0,1).mul(qold,adjustment)
    U=cm['CM_matrix'];D=[[1,0],[0,adjustment]];Unew=mm2(mm2(inv2(D),U),D)
    assert Unew==data['CM_unit_matrix']==[[16,19],[18,24]]
    Fnew=mm2(mm2(inv2(D),[[0,35],[1,0]]),D)
    assert Fnew==data['frobenius_torsion_matrix']==[[0,15],[16,0]]
    R=[[(2*Unew[a][b]+int(a==b))%41 for b in range(2)] for a in range(2)]
    scale=pow(R[1][0],-1,41);R=[[c*scale%41 for c in row] for row in R]
    a=R[0][0];e=(a*a+R[0][1])%41
    assert [a,e]==data['CM_necklace']==[18,13]
    cmindex=data['CM_necklace_index_1based']-1
    assert model['necklaces'][cmindex]==[a,e]
    order=3*data['coarse_order'];j=Jets(r,order)
    P=tuple(tuple(r.element(c) for c in coordinate) for coordinate in data['P_jets'])
    Q=tuple(tuple(r.element(c) for c in coordinate) for coordinate in data['Q_jets'])
    assert tuple(c[0] for c in P)==p0 and tuple(c[0] for c in Q)==q0
    curve=JetCurve(j,j.parameter)
    assert curve.on_curve(P) and curve.on_curve(Q)
    assert curve.mul(P,41) is None and curve.mul(Q,41) is None
    phi=r.element(torsion['frobenius_lift'])
    def frobenius(point):return tuple(tuple(r.evaluate(c,phi) for c in coordinate) for coordinate in point)
    assert curve.mul(frobenius(P),adjustment)==Q
    assert frobenius(Q)==curve.mul(P,35*adjustment)
    cmu=r.element(cm['CM_unit']);cmu2=r.mul(cmu,cmu)
    assert r.add(r.add(cmu2,cmu),r.one)==r.zero
    Pscaled=tuple(j.rescale_parameter(c,cmu2) for c in P)
    Qscaled=tuple(j.rescale_parameter(c,cmu2) for c in Q)
    scaledcurve=JetCurve(j,j.mul(j.constant(cmu2),j.parameter))
    for col,T in enumerate((P,Q)):
        expected=scaledcurve.add(scaledcurve.mul(Pscaled,Unew[0][col]),scaledcurve.mul(Qscaled,Unew[1][col]))
        assert expected==(j.mul(j.constant(cmu),T[0]),T[1])
    print('Actual formal41-torsion, the Weil adjustment, Frobenius and CM unit covariance verified.',flush=True)
    values=eisenstein(j,P,Q)
    g=model['sl2_representatives'][cmindex]
    gh=[mm2(g,h) for h in model['sl2_normalizer_mod_signs']]
    traces=[c%q for c in power_traces(f,158)];quarter=pow(4,-1,q);iew=r.mul(ii,ew)
    h0=[sum(ew[k]*traces[n+k] for k in range(80))*quarter%q for n in range(80)]
    h1=[-sum(iew[k]*traces[n+k] for k in range(80))*quarter%q for n in range(80)]
    raw=[[None]*73 for _ in range(order)]
    for k,(v,w) in enumerate(model['basis_pairs']):
        score=j.zero
        for h in gh:
            iv=index(h[0][0]*v[0]+h[0][1]*v[1],h[1][0]*v[0]+h[1][1]*v[1])
            iw=index(h[0][0]*w[0]+h[0][1]*w[1],h[1][0]*w[0]+h[1][1]*w[1])
            score=j.add(score,j.mul(values[iv],values[iw]))
        for n,c in enumerate(score):raw[n][k]=[sum(x*y for x,y in zip(c,h0))%q,sum(x*y for x,y in zip(c,h1))%q]
    W=qmatmul(raw,model['basis_inverse'],q)
    assert W==data['stack_evaluation_coefficients']
    assert all(all(value==[0,0] for value in row) for n,row in enumerate(W) if n%3!=2)
    coarse=W[2::3]
    assert coarse==data['coarse_evaluation_coefficients']
    assert qmatmul(coarse,model['frobenius_basis_matrix'],q)==[[[a,-b%q] for a,b in row] for row in coarse]
    pivot=data['unit_coordinate_1based']-1;assert pivot==0
    denominator=[row[pivot] for row in coarse];inverse=[qinv(denominator[0],q)]
    for n in range(1,len(coarse)):
        x=y=0
        for k in range(1,n+1):
            a,b=qmul(denominator[k],inverse[n-k],q);x+=a;y+=b
        inverse.append(qmul((-x%q,-y%q),inverse[0],q))
    normalized=[[[0,0] for _ in range(73)] for _ in coarse]
    for n in range(len(coarse)):
        for k in range(73):
            x=y=0
            for h in range(n+1):
                a,b=qmul(coarse[h][k],inverse[n-h],q);x+=a;y+=b
            normalized[n][k]=[x%q,y%q]
    assert normalized==data['affine_coordinate_coefficients']
    tangent=data['tangent_coordinate_1based']-1;assert tangent==1
    assert [[a%47,b%47] for a,b in [row[tangent] for row in normalized]]==[[23,5],[34,17],[25,25]]
    assert (34**2+17**2)%47==35
    print('All73 actual coarse CM point/tangent/second-order coordinates verified modulo47^4.',flush=True)
    print('Coordinate2=(23+5i)+(34+17i)t+(25+25i)t^2 mod47; the tangent norm is35.')
    print('These are actual curve jets; no Poincare height or QC common-root claim is made.')


if __name__=='__main__':
    default=Path(__file__).with_name('data')/'p41_cm3_makdisi47_certificate.json'
    main(Path(sys.argv[1]) if len(sys.argv)>1 else default)
