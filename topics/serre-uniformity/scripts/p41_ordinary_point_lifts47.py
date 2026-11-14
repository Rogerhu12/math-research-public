#!/usr/bin/env python3
"""Lift the actual ordinary torsion/evaluation points to precision47^4.

All inversions in the finite etale ring are lifted from its residue field.
The fixed irreducible x-field polynomial defines an unramified integer ring;
division-polynomial roots and the Frobenius map are Hensel lifted there.
"""
import argparse
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path
import time
from flint import nmod_poly,fmpz_mod_poly_ctx,fq_default_ctx
from p41_ordinary_residue_points47 import Curve,gauss,read

P=47
Q=P**4


class Element:
    def __init__(self,K,a):self.K,self.p=K,a%K.h
    def __add__(self,b):return Element(self.K,self.p+self.K(b).p)
    __radd__=__add__
    def __neg__(self):return Element(self.K,-self.p)
    def __sub__(self,b):return self+-self.K(b)
    def __rsub__(self,b):return self.K(b)+-self
    def __mul__(self,b):return Element(self.K,self.p*self.K(b).p)
    __rmul__=__mul__
    def __eq__(self,b):return self.p==self.K(b).p
    def __bool__(self):return bool(self.p)
    def __pow__(self,n):
        if n<0:return self.inverse()**(-n)
        return Element(self.K,self.p.pow_mod(n,self.K.h))
    def inverse(self):
        if self.p.degree()==0:return self.K(pow(int(self.p[0]),-1,Q))
        a=self.K.rf([int(x)%P for x in self.p.coeffs()])
        b=self.K([int(x) for x in a.inverse().to_list()])
        for _ in range(2):b=b*(2-self*b)
        assert self*b==1
        return b
    def __truediv__(self,b):return self*self.K(b).inverse()
    def __rtruediv__(self,b):return self.K(b)*self.inverse()
    def trace(self):return sum(int(v)*self.K.tr[i] for i,v in enumerate(self.p.coeffs()))%Q
    def frobenius(self,e=1):return Element(self.K,self.p.compose_mod(self.K.phi_power(e),self.K.h))
    def to_list(self):return [int(x) for x in self.p.coeffs()]


class Ring:
    def __init__(self,poly):
        self.h=nmod_poly(poly,Q);self.k=self.h.degree()
        self.rf=fq_default_ctx(modulus=fmpz_mod_poly_ctx(P)(poly),fq_type='FQ_NMOD',check_modulus=False)
        self.phi_cache={0:nmod_poly([0,1],Q)}
        self.tr=[self.k%Q]
        c=[int(x) for x in self.h.coeffs()]
        for n in range(1,self.k):
            self.tr.append((-n*c[self.k-n]-sum(c[self.k-i]*self.tr[n-i] for i in range(1,n)))%Q)
        self.phi_cache[1]=self.hensel(self.h,self.gen()**P).p
    def __call__(self,a):
        if isinstance(a,Element):assert a.K is self;return a
        if isinstance(a,int):a=[a]
        return Element(self,a if isinstance(a,nmod_poly) else nmod_poly(a,Q))
    def gen(self):return self([0,1])
    def hensel(self,f,x):
        derivative=f.derivative()
        for _ in range(2):
            val=self(f.compose_mod(x.p,self.h))
            der=self(derivative.compose_mod(x.p,self.h))
            x=x-val/der
        assert f.compose_mod(x.p,self.h)==0
        return x
    def phi_power(self,n):
        if n not in self.phi_cache:
            if n%2:
                self.phi_cache[n]=self.phi_power(n-1).compose_mod(self.phi_cache[1],self.h)
            else:
                a=self.phi_power(n//2);self.phi_cache[n]=a.compose_mod(a,self.h)
        return self.phi_cache[n]


def division_polynomial(A,B):
    x=nmod_poly([0,1],Q);f=x**3+A*x+B
    first={0:x*0,1:x*0+1,2:x*0+1,3:3*x**4+6*A*x*x+12*B*x-A*A,
           4:2*(x**6+5*A*x**4+20*B*x**3-5*A*A*x*x-4*A*B*x-8*B*B-A**3)}
    @lru_cache(None)
    def q(n):
        if n in first:return first[n]
        m=n//2
        if n%2:
            left=q(m+2)*q(m)**3;right=q(m-1)*q(m+1)**3
            if m%2:right*=16*f*f
            else:left*=16*f*f
            return left-right
        return q(m)*(q(m+2)*q(m-1)**2-q(m-2)*q(m+1)**2)
    ans=q(41);assert ans.degree()==840 and ans[840]==41
    return ans


class LiftedCurve(Curve):
    def __init__(self,K,A,B):
        self.K,self.A,self.B=K,A,B
        psi=division_polynomial(A,B)
        px=K.hensel(psi,K.gen())
        self.f=px**3+A*px+B
        self.P=px,K(1)
        qx=px.frobenius()
        qb0=(K.rf.gen()**3+A*K.rf.gen()+B)**23
        qb=K([int(x) for x in qb0.to_list()])
        target=qx**3+A*qx+B
        for _ in range(2):qb=qb-(self.f*qb*qb-target)/(2*self.f*qb)
        self.Q=qx,qb
        assert self.on_curve(self.P) and self.on_curve(self.Q)
    def frob(self,V):
        if V is None:return None
        return V[0].frobenius(),V[1].frobenius()*self.Q[1]


def rowmul(v,M):
    out=[]
    for j in range(len(M[0])):
        a=b=0
        for k,(u,w) in enumerate(v):
            x,y=M[k][j];a+=u*x-w*y;b+=u*y+w*x
        out.append([a%Q,b%Q])
    return out


def point(model,rec,alpha):
    start=time.time();j=rec['j_mod47'];A=rec['curve_A'];B=rec['curve_B'];a=rec['elliptic_frobenius_trace']
    K=Ring(rec['x_field_polynomial_ascending']);C=LiftedCurve(K,A,B)
    assert C.mul(C.P,41) is None and C.mul(C.Q,41) is None
    assert C.frob(C.Q)==C.add(C.mul(C.Q,a),C.mul(C.P,-47))
    zeta=C.pairing();ii=gauss(zeta)/alpha
    assert ii*ii==-1 and ii.frobenius()==-ii
    assert [x%P for x in zeta.to_list()]==rec['weil_pairing_coefficients']
    print('lift j',j,'field',K.k,'actual torsion/Frob',round(time.time()-start,3),flush=True)
    ev=C.eisenstein();g=model['sl2_representatives'][rec['necklace_1based']-1]
    gh=[]
    for h in model['sl2_normalizer_mod_signs']:
        gh.append([[sum(g[s][u]*h[u][t] for u in range(2))%41 for t in range(2)] for s in range(2)])
    values=[];scale=20*pow(K.k,-1,Q)%Q
    for v,w in model['basis_pairs']:
        total=K(0)
        for h in gh:
            def index(v):return (h[0][0]*v[0]+h[0][1]*v[1])%41+41*((h[1][0]*v[0]+h[1][1]*v[1])%41)
            total+=ev[index(v)]*ev[index(w)]
        total*=C.f*zeta
        assert total.frobenius(40)==total
        values.append([total.trace()*scale%Q,-(ii*total).trace()*scale%Q])
    W=rowmul(values,model['basis_inverse'])
    assert rowmul(W,model['frobenius_basis_matrix'])==[[u,-v%Q] for u,v in W]
    assert [[u%P,v%P] for u,v in W]==rec['W_mod47']
    print('lift j',j,'all73 actual values and descent',round(time.time()-start,3),flush=True)
    return {'j_mod47':j,'curve_A':A,'curve_B':B,'elliptic_frobenius_trace':a,
            'x_coordinate_field_degree':K.k,'x_field_polynomial_ascending':rec['x_field_polynomial_ascending'],
            'necklace_1based':rec['necklace_1based'],'necklace':rec['necklace'],
            'P_x':C.P[0].to_list(),'Q_x':C.Q[0].to_list(),'Q_y_over_P_y':C.Q[1].to_list(),
            'unramified_frobenius':K(K.phi_cache[1]).to_list(),
            'weil_pairing':zeta.to_list(),'sqrt_minus_one':ii.to_list(),
            'gauss_scale':alpha,'trace_coordinate_scale':scale,
            'basis_values_mod47four':values,'W_mod47four':W,
            'actual_torsion_pairing_and_Frobenius_verified':True,
            'all73_cyclotomic40_descent_verified':True,
            'all73_original_semilinear_Frobenius_verified':True,
            'residue_coordinates_match_original_certificate':True}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--residue-input',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--j',type=int,nargs='*')
    args=ap.parse_args();model=read(args.script_dir/'data/p41_makdisi47_certificate.json.gz')
    residue=read(args.residue_input)
    alpha=10
    for _ in range(2):alpha=(alpha-(alpha*alpha+41)*pow(2*alpha,-1,Q))%Q
    assert (alpha*alpha+41)%Q==0
    records=read(args.output)['points'] if args.output.exists() else []
    done={r['j_mod47'] for r in records}
    for rec in residue['points']:
        if args.j and rec['j_mod47'] not in args.j:continue
        if rec['j_mod47'] in done:continue
        records.append(point(model,rec,alpha))
        out={'level':41,'auxiliary_prime':47,'precision':4,'modulus':Q,'points':records,
             'complete_all19_ordinary_reference_values':len(records)==19,
             'complete_local_QC_functions':False,'complete_common_roots':False,
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'residue_input_sha256':hashlib.sha256(args.residue_input.read_bytes()).hexdigest()}
        args.output.write_bytes(gzip.compress((json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0))
    print('saved actual precision4 ordinary references',len(records),flush=True)


if __name__=='__main__':main()
