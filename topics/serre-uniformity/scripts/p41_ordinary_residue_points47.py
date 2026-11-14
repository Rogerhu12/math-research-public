#!/usr/bin/env python3
"""Actual F47 points of the ordinary fibres in the fixed level41 model.

The x-coordinate field has degree 120,280,840.  All y-coordinates and
weight-one values are y0 times elements of this field.  No full degree
240,560,1680 extension needs to be constructed.  This computes residue
coordinates, not yet Q47 lifts or Abel constants.
"""
import argparse
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time

from flint import nmod_poly, fmpz_mod_poly_ctx, fq_default_ctx

P=47
N=41


def read(path):
    b=Path(path).read_bytes()
    return json.loads(gzip.decompress(b) if str(path).endswith('.gz') else b)


def division_polynomial(A,B):
    x=nmod_poly([0,1],P)
    f=x**3+A*x+B
    first={0:x*0,1:x*0+1,2:x*0+1,
           3:3*x**4+6*A*x*x+12*B*x-A*A,
           4:2*(x**6+5*A*x**4+20*B*x**3-5*A*A*x*x-4*A*B*x-8*B*B-A**3)}
    @lru_cache(None)
    def q(n):
        if n in first:return first[n]
        m=n//2
        if n%2:
            left=q(m+2)*q(m)**3
            right=q(m-1)*q(m+1)**3
            if m%2:right*=16*f*f
            else:left*=16*f*f
            return left-right
        return q(m)*(q(m+2)*q(m-1)**2-q(m-2)*q(m+1)**2)
    out=q(N)
    assert out.degree()==840 and int(out[840])==41
    return out


class Curve:
    """Points (x,b) mean (x,y0*b), with y0^2=f0."""
    def __init__(self,K,A,B,x):
        self.K,self.A,self.B=K,A,B
        self.f=x**3+A*x+B
        assert not self.f.is_square()
        self.P=(x,K(1))
        self.Q=(x**P,self.f**((P-1)//2))

    def on_curve(self,V):
        return V is None or self.f*V[1]*V[1]==V[0]**3+self.A*V[0]+self.B

    def neg(self,V):return None if V is None else (V[0],-V[1])

    def slope(self,V,W):
        x,b=V;y,c=W
        if x==y:
            assert V==W and b
            return (3*x*x+self.A)/(2*self.f*b)
        return (c-b)/(y-x)

    def add(self,V,W):
        if V is None:return W
        if W is None:return V
        if V[0]==W[0] and V[1]+W[1]==0:return None
        s=self.slope(V,W)
        x=self.f*s*s-V[0]-W[0]
        return x,s*(V[0]-x)-V[1]

    def mul(self,V,n):
        if n<0:return self.mul(self.neg(V),-n)
        Z=None
        while n:
            if n&1:Z=self.add(Z,V)
            n>>=1
            if n:V=self.add(V,V)
        return Z

    def frob(self,V):
        if V is None:return None
        return V[0]**P,V[1]**P*self.f**((P-1)//2)

    def miller(self,V,T):
        val=self.K(1);parity=0;Z=V
        def times_line(val,parity,Z,W):
            R=self.add(Z,W)
            if R is None:
                return val*(T[0]-Z[0]),parity,R
            s=self.slope(Z,W)
            u=(T[1]-Z[1]-s*(T[0]-Z[0]))/(T[0]-R[0])
            val*=u
            if parity:val*=self.f
            return val,1-parity,R
        for bit in bin(N)[3:]:
            val=val*val*(self.f if parity else 1);parity=0
            val,parity,Z=times_line(val,parity,Z,Z)
            if bit=='1':val,parity,Z=times_line(val,parity,Z,V)
        assert Z is None
        return val,parity

    def pairing(self):
        a,j=self.miller(self.P,self.Q)
        b,k=self.miller(self.Q,self.P)
        assert j==k
        z=-a/b
        assert z!=1 and z**N==1
        return z

    def eisenstein(self):
        axes=[];den=[];num=[]
        for V in (self.P,self.Q):
            multiples=[V]
            for _ in range(39):multiples.append(self.add(multiples[-1],V))
            assert multiples[-1]==self.neg(V)
            axes.append(multiples)
            for j in range(39):
                if j==0:
                    num.append(3*V[0]*V[0]+self.A)
                    den.append(2*self.f*V[1])
                else:
                    num.append(multiples[j][1]-V[1]);den.append(multiples[j][0]-V[0])
        for V in axes[0]:
            for W in axes[1]:
                num.append(W[1]-V[1]);den.append(W[0]-V[0])
        prefix=[];total=self.K(1)
        for x in den:prefix.append(total);total*=x
        rev=total.inverse();inverse=[None]*len(den)
        for k in range(len(den)-1,-1,-1):
            inverse[k]=rev*prefix[k];rev*=den[k]
        assert rev==1
        slopes=[a*b for a,b in zip(num,inverse)]
        axis_values=[]
        for k in (0,39):
            ep=sum(slopes[k:k+39],self.K(0))/41
            values=[ep]
            for j in range(39):values.append(values[-1]+ep-slopes[k+j])
            assert values[-1]==-ep
            axis_values.append(values)
        ev=[self.K(0) for _ in range(1681)]
        for i in range(1,41):
            ev[i]=axis_values[0][i-1]
            ev[41*i]=axis_values[1][i-1]
        for i in range(1,41):
            for j in range(1,41):
                ev[i+41*j]=axis_values[0][i-1]+axis_values[1][j-1]-slopes[78+40*(i-1)+j-1]
        for i in range(41):
            for j in range(41):assert ev[i+41*j]==-ev[(-i)%41+41*((-j)%41)]
        return ev


def gauss(z):
    out=z-z
    for k in range(1,41):out+=(1 if pow(k,20,41)==1 else -1)*z**k
    assert out*out==41
    return out


def pairmul(a,b):return ((a[0]*b[0]-a[1]*b[1])%P,(a[0]*b[1]+a[1]*b[0])%P)


def rowmul(v,M):
    out=[]
    for j in range(len(M[0])):
        a=b=0
        for k,w in enumerate(v):
            c,d=pairmul(w,M[k][j]);a+=c;b+=d
        out.append([a%P,b%P])
    return out


def point(model,rec,gauss_scale):
    stamp=time.time();A=rec['curve_A'];B=rec['curve_B'];a=rec['elliptic_frobenius_trace'];j=rec['j_mod47']
    psi=division_polynomial(A,B)
    unit,fac=psi.factor();expected=rec['full_41_torsion_residue_degree']//2
    assert int(unit)==41 and all(f.degree()==expected and e==1 for f,e in fac)
    h=min((f for f,e in fac),key=lambda f:tuple(int(v) for v in f.coeffs()))
    K=fq_default_ctx(modulus=fmpz_mod_poly_ctx(P)([int(v) for v in h.coeffs()]),fq_type='FQ_NMOD',check_modulus=False)
    C=Curve(K,A,B,K.gen())
    assert C.on_curve(C.P) and C.on_curve(C.Q)
    assert C.mul(C.P,41) is None and C.mul(C.Q,41) is None
    assert C.frob(C.Q)==C.add(C.mul(C.Q,a),C.mul(C.P,-P))
    zeta=C.pairing();ii=gauss(zeta)/gauss_scale
    assert ii*ii==-1 and ii**P==-ii
    print('ordinary j',j,'x-field',expected,'factor and torsion',round(time.time()-stamp,3),flush=True)
    ev=C.eisenstein()
    na=(-a*pow(2,-1,41))%41;ne=(na*na+35)%41
    label=model['necklaces'].index([na,ne]);g=model['sl2_representatives'][label]
    gh=[]
    for h0 in model['sl2_normalizer_mod_signs']:
        gh.append([[sum(g[s][u]*h0[u][t] for u in range(2))%41 for t in range(2)] for s in range(2)])
    # Tr_{k/1}(z)=(k/40)*Tr_{40/1}(z)=(k/20)*A.
    scale=20*pow(expected,-1,P)%P
    values=[]
    for v,w in model['basis_pairs']:
        total=K(0)
        for gh0 in gh:
            def index(v):
                u=(gh0[0][0]*v[0]+gh0[0][1]*v[1])%41
                t=(gh0[1][0]*v[0]+gh0[1][1]*v[1])%41
                return u+41*t
            total+=ev[index(v)]*ev[index(w)]
        total*=C.f*zeta
        assert total.frobenius(40)==total
        values.append([int(total.trace())*scale%P,-int((ii*total).trace())*scale%P])
    W=rowmul(values,model['basis_inverse'])
    assert rowmul(W,model['frobenius_basis_matrix'])==[[u,-v%P] for u,v in W]
    assert any(u or v for u,v in W)
    print('ordinary j',j,'complete actual weight2/Frobenius',round(time.time()-stamp,3),flush=True)
    return {'j_mod47':j,'curve_A':A,'curve_B':B,'elliptic_frobenius_trace':a,
            'x_coordinate_field_degree':expected,'full_41_torsion_degree':2*expected,
            'psi41_factors_degrees':[f.degree() for f,e in fac],
            'x_field_polynomial_ascending':[int(v) for v in h.coeffs()],
            'P_representation':'(x,y0), y0^2=x^3+A*x+B; Q=Frob47(P)',
            'weil_pairing_coefficients':[int(v) for v in zeta.to_list()],
            'sqrt_minus_one_coefficients':[int(v) for v in ii.to_list()],
            'gauss_scale_mod47':gauss_scale,'necklace_1based':label+1,'necklace':[na,ne],
            'trace_coordinate_scale_mod47':scale,'basis_values_mod47':values,
            'W_mod47':W,'actual_torsion_and_pairing_verified':True,
            'Frobenius_semilinear_descent_verified':True}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--j',type=int,nargs='*')
    args=ap.parse_args();folder=args.script_dir/'data'
    model=read(folder/'p41_makdisi47_certificate.json.gz')
    tor=read(folder/'p41_local47_torsion_certificate.json')
    inventory=read(folder/'p41_residue47_inventory.json')
    K0=fq_default_ctx(modulus=fmpz_mod_poly_ctx(P)(tor['field_polynomial_ascending']),fq_type='FQ_NMOD')
    source=next(c for c in tor['curves'] if c['label']=='Makdisi_j9_fibre')
    alpha=gauss(K0(source['weil_pairing']))/K0(model['sqrt_minus_one_lift'])
    assert alpha**P==alpha
    gauss_scale=int(alpha.to_list()[0]);assert alpha==gauss_scale
    print('original cyclotomic quadratic orientation',gauss_scale,flush=True)
    records=read(args.output)['points'] if args.output.exists() else []
    done={r['j_mod47'] for r in records}
    for rec in inventory['fibres']:
        if rec['coarse_F47_points']!=1:continue
        rec=dict(rec,j_mod47=rec['j'])
        if args.j and rec['j_mod47'] not in args.j:continue
        if rec['j_mod47'] in done:continue
        records.append(point(model,rec,gauss_scale))
        out={'level':41,'auxiliary_prime':47,'precision':1,'points':records,
             'scope':'Actual ordinary F47 residue coordinates, not yet Q47 lifts or Abel constants',
             'complete_ordinary_residue_coordinates':len(records)==19,
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
        args.output.write_bytes(gzip.compress((json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0))
    print('saved ordinary residue points',len(records),flush=True)


if __name__=='__main__':main()
