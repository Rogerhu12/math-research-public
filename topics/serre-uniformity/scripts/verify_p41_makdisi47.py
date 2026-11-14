#!/usr/bin/env python3
"""Verify the complete actual level-41 evaluation model using Python's standard library."""
from array import array
from fractions import Fraction
import gzip
import hashlib
import json
from math import comb
from pathlib import Path
import sys

sys.dont_write_bytecode=True
from verify_p41_local47_torsion import Ring, Curve, main as verify_torsion
from verify_p41_cm_height_ratios import multiply, divide


def index(i,j):
    return i%41+41*(j%41)


def power_traces(f,degree):
    """Newton sums for a monic polynomial in ascending coefficient order."""
    n=len(f)-1
    assert f[-1]==1
    out=[n]
    for k in range(1,degree+1):
        value=sum(f[n-j]*out[k-j] for j in range(1,min(k,n)+1) if j<k)
        if k<=n:value+=k*f[n-k]
        out.append(-value)
    return out


def mm2(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2))%41 for j in range(2)] for i in range(2)]


def det2(a):
    return (a[0][0]*a[1][1]-a[0][1]*a[1][0])%41


def inv2(a):
    d=pow(det2(a),-1,41)
    return [[a[1][1]*d%41,-a[0][1]*d%41],[-a[1][0]*d%41,a[0][0]*d%41]]


def geometry(data):
    nonsquares=[e for e in range(1,41) if pow(e,20,41)==40]
    necklaces=[[a,e] for a in range(41) for e in nonsquares]
    assert data['necklaces']==necklaces
    H=[]
    for a in range(41):
        for b in range(41):
            if index(a,b)>index(-a,-b):continue
            norm=(a*a-35*b*b)%41
            if norm==1:H.append([[a,35*b%41],[b,a]])
            if norm==40:H.append([[a,-35*b%41],[b,-a%41]])
    assert H==data['sl2_normalizer_mod_signs'] and len(H)==42
    F=[[0,35],[1,0]]
    permutation=[]
    for (a,e),g in zip(necklaces,data['sl2_representatives']):
        assert det2(g)==1
        t=mm2(mm2(g,F),inv2(g));c=pow(t[1][0],-1,41)
        assert [[x*c%41 for x in row] for row in t]==[[a,(e-a*a)%41],[1,-a%41]]
        R=[[a,(e-a*a)%41],[1,-a%41]]
        t=mm2(mm2(F,R),inv2(F));c=pow(t[1][0],-1,41)
        t=[[x*c%41 for x in row] for row in t]
        aa=t[0][0];ee=(aa*aa+t[0][1])%41
        permutation.append(20*aa+nonsquares.index(ee))
    assert [n+1 for n in permutation]==data['frobenius_permutation_1based']
    assert sum(i==j for i,j in enumerate(permutation))==22
    assert all(permutation[permutation[i]]==i for i in range(820))
    return [[mm2(g,h) for h in H] for g in data['sl2_representatives']],permutation


def weight_one(r,P,Q):
    curve=Curve(r,1,32)
    Ps=[P];Qs=[Q]
    for _ in range(39):
        Ps.append(curve.add(Ps[-1],P));Qs.append(curve.add(Qs[-1],Q))
    numerator=[];denominator=[]
    for base,multiples in ((P,Ps),(Q,Qs)):
        for k in range(39):
            if k==0:
                numerator.append(r.add(r.scale(r.mul(base[0],base[0]),3),r.one))
                denominator.append(r.scale(base[1],2))
            else:
                numerator.append(r.sub(multiples[k][1],base[1]))
                denominator.append(r.sub(multiples[k][0],base[0]))
    for x,y in Ps:
        for xx,yy in Qs:
            numerator.append(r.sub(yy,y));denominator.append(r.sub(xx,x))
    prefix=[];product=r.one
    for d in denominator:
        assert any(x%47 for x in d)
        prefix.append(product);product=r.mul(product,d)
    backwards=r.inverse(product)
    slopes=[None]*len(numerator)
    for k in range(len(numerator)-1,-1,-1):
        inverse=r.mul(backwards,prefix[k]);backwards=r.mul(backwards,denominator[k])
        slopes[k]=r.mul(numerator[k],inverse)
    assert backwards==r.one
    def total(items):
        answer=r.zero
        for item in items:answer=r.add(answer,item)
        return answer
    ep=r.scale(total(slopes[:39]),pow(41,-1,r.q))
    eq=r.scale(total(slopes[39:78]),pow(41,-1,r.q))
    pe=[ep];qe=[eq]
    for k in range(39):
        pe.append(r.sub(r.add(pe[-1],ep),slopes[k]))
        qe.append(r.sub(r.add(qe[-1],eq),slopes[k+39]))
    assert pe[-1]==r.scale(ep,-1) and qe[-1]==r.scale(eq,-1)
    values=[r.zero]*1681
    for k in range(1,41):values[index(k,0)]=pe[k-1];values[index(0,k)]=qe[k-1]
    for i in range(1,41):
        for j in range(1,41):values[index(i,j)]=r.sub(r.add(pe[i-1],qe[j-1]),slopes[78+40*(i-1)+j-1])
    for i in range(41):
        for j in range(41):assert values[index(-i,-j)]==r.scale(values[index(i,j)],-1)
    print('All1680 actual weight-one evaluations independently reconstructed.',flush=True)
    return values


def trace_gram(r,values,ew,ii):
    representatives=[];signed=[0]*1681
    for j in range(1,1681):
        neg=index(-(j%41),-(j//41))
        if j<neg:
            representatives.append(j);signed[j]=len(representatives);signed[neg]=-len(representatives)
    assert len(representatives)==840
    E=[values[j] for j in representatives]
    traces=[x%r.q for x in power_traces(r.f,237)]
    weighted_i=r.mul(ii,ew);quarter=pow(4,-1,r.q)
    h0=[sum(ew[j]*traces[k+j] for j in range(80))*quarter%r.q for k in range(159)]
    h1=[-sum(weighted_i[j]*traces[k+j] for j in range(80))*quarter%r.q for k in range(159)]
    eh0=[[sum(e[k]*h0[j+k] for k in range(80))%r.q for j in range(80)] for e in E]
    eh1=[[sum(e[k]*h1[j+k] for k in range(80))%r.q for j in range(80)] for e in E]
    b0=array('I',[0])*(840*840);b1=array('I',[0])*(840*840)
    for i in range(840):
        x,y=eh0[i],eh1[i]
        for j in range(i,840):
            e=E[j]
            a=sum(u*v for u,v in zip(x,e))%r.q
            b=sum(u*v for u,v in zip(y,e))%r.q
            b0[i*840+j]=b0[j*840+i]=a
            b1[i*840+j]=b1[j*840+i]=b
    print('The two full relative-trace Gram matrices verified by Newton sums.',flush=True)
    return signed,b0,b1


def qmul(a,b,q):
    return ((a[0]*b[0]-a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)


def qinv(a,q):
    inverse=pow((a[0]*a[0]+a[1]*a[1])%q,-1,q)
    return (a[0]*inverse%q,-a[1]*inverse%q)


def qdet(matrix,q):
    a=[[tuple(c) for c in row] for row in matrix];n=len(a);det=(1,0)
    for k in range(n):
        pivot=next(i for i in range(k,n) if a[i][k]!=(0,0))
        if pivot!=k:a[pivot],a[k]=a[k],a[pivot];det=(-det[0]%q,-det[1]%q)
        det=qmul(det,a[k][k],q);inverse=qinv(a[k][k],q)
        for i in range(k+1,n):
            c=qmul(a[i][k],inverse,q)
            for j in range(k+1,n):
                d=qmul(c,a[k][j],q)
                a[i][j]=((a[i][j][0]-d[0])%q,(a[i][j][1]-d[1])%q)
    return det


def qmatmul(a,b,q):
    columns=list(zip(*b));out=[]
    for row in a:
        outrow=[]
        for column in columns:
            real=sum(x[0]*y[0]-x[1]*y[1] for x,y in zip(row,column))%q
            imaginary=sum(x[0]*y[1]+x[1]*y[0] for x,y in zip(row,column))%q
            outrow.append([real,imaginary])
        out.append(outrow)
    return out


def local_factor(hecke):
    i47=hecke['indices'].index(47)-1
    total=[1]
    for record in hecke['fields']:
        f=[Fraction(x) for x in reversed(record['factor_descending'])]
        denominator,desc=record['directions'][i47][0]
        a=[Fraction(x,denominator) for x in reversed(desc)]
        n=len(f)-1;htraces=power_traces(f,n-1);apower=[Fraction(1)];atraces=[n]
        for k in range(1,n+1):
            apower=divide(multiply(apower,a),f)[1]
            atraces.append(sum(c*htraces[j] for j,c in enumerate(apower)))
        characteristic=[Fraction(1)]
        for k in range(1,n+1):
            characteristic.append(-sum(characteristic[k-j]*atraces[j] for j in range(1,k+1))/k)
        assert all(c.denominator==1 for c in characteristic)
        factor=[0]*(2*n+1)
        for k,c in enumerate(characteristic):
            for j in range(n-k+1):factor[2*n-k-2*j]+=int(c)*comb(n-k,j)*47**j
        total=multiply(total,factor)
    return list(reversed(total))


def main(path):
    data=json.loads(gzip.decompress(path.read_bytes()))
    assert (data['level'],data['auxiliary_prime'],data['genus'],data['cusp_count'],
            data['line_bundle_degree'],data['dimension'],data['evaluation_point_count'])==(41,47,54,20,126,73,820)
    assert data['residue_degree']==2 and data['quadratic_polynomial_ascending']==[1,0,1]
    assert data['relative_trace_degree']==20 and data['cyclotomic_weight']==1
    q=47**data['precision'];assert q==data['modulus'] and data['precision'] in (1,2,3,4)
    torsion_path=path.with_name(data['torsion_source']);source=torsion_path.read_bytes()
    assert hashlib.sha256(source).hexdigest()==data['torsion_source_sha256']
    verify_torsion(torsion_path)
    torsion=json.loads(source);curve=next(c for c in torsion['curves'] if c['label']=='Makdisi_j9_fibre')
    r=Ring(torsion['field_polynomial_ascending'],q)
    P=tuple(r.element(c) for c in curve['P']);Q=tuple(r.element(c) for c in curve['Q'])
    ew=r.element(curve['weil_pairing']);ii=r.element(data['sqrt_minus_one_lift'])
    assert r.mul(ii,ii)==r.element(-1)
    assert r.evaluate(ii,r.element(torsion['frobenius_lift']))==r.scale(ii,-1)
    first=next(x%47 for x in ii if x%47);assert first<24
    gh,permutation=geometry(data)
    values=weight_one(r,P,Q)
    signed,b0,b1=trace_gram(r,values,ew,ii)
    pairs=data['basis_pairs'];assert len(pairs)==73
    assert pairs==[data['candidate_pairs'][k-1] for k in data['basis_columns_1based']]
    M=[]
    for row in gh:
        out=[]
        for v,w in pairs:
            real=imaginary=0
            for g in row:
                j1=signed[index(g[0][0]*v[0]+g[0][1]*v[1],g[1][0]*v[0]+g[1][1]*v[1])]
                j2=signed[index(g[0][0]*w[0]+g[0][1]*w[1],g[1][0]*w[0]+g[1][1]*w[1])]
                sign=1 if j1*j2>0 else -1
                j=(abs(j1)-1)*840+abs(j2)-1
                real+=sign*b0[j];imaginary+=sign*b1[j]
            out.append([real%q,imaginary%q])
        M.append(out)
    rows=[k-1 for k in data['pivot_rows_1based']];assert len(set(rows))==73
    PV=[M[k] for k in rows]
    minor=qdet([[[a%47,b%47] for a,b in row] for row in PV],47)
    assert list(minor)==data['unit_minor_mod47']==[43,17]
    identity=[[[int(i==j),0] for j in range(73)] for i in range(73)]
    C=data['basis_inverse']
    assert qmatmul(PV,C,q)==identity
    W=qmatmul(M,C,q)
    assert W==data['evaluation_matrix']
    assert [W[k] for k in rows]==identity
    print('All820x73 actual evaluations and the unit minor43+17i verified modulo47^'+str(data['precision'])+'.',flush=True)
    Y=[[[a,-b%q] for a,b in W[permutation[n]]] for n in range(820)]
    F=data['frobenius_basis_matrix']
    assert F==[Y[k] for k in rows]
    assert qmatmul(W,F,q)==Y
    assert qmatmul(F,[[[a,-b%q] for a,b in row] for row in F],q)==identity
    source=path.with_name(data['hecke_source']).read_bytes()
    assert hashlib.sha256(source).hexdigest()==data['hecke_source_sha256']
    hecke=json.loads(gzip.decompress(source));L=local_factor(hecke)
    assert L==data['local_factor_descending']
    assert len(L)==109 and L[0]==1 and L[1]==81 and L[-1]==47**54
    assert all(L[108-k]==47**(54-k)*L[k] for k in range(55))
    print('The complete Frobenius descent and the actual degree108 local factor verified.',flush=True)
    print('This is an actual evaluation model, not a computation of local QC functions or common roots.')


if __name__=='__main__':
    default=Path(__file__).with_name('data')/'p41_makdisi47_certificate.json.gz'
    main(Path(sys.argv[1]) if len(sys.argv)>1 else default)
