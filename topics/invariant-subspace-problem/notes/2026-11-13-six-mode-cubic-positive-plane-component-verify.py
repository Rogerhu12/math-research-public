"""Exact global construction and local nonzero data for a cubic-mean component.

The uniform augmented determinant is verified over Q as a polynomial identity.
The local matrix and cubic are reduced modulo 103 only to prove NONZERO exact
algebraic quantities; no finite-field zero is used to assert a characteristic
zero identity or an exact Hessian rank.
"""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import itertools
import json

folder=Path(__file__).parent
data=json.loads((folder/'2026-11-13-six-mode-cubic-positive-plane-component-data.json').read_text())
path=folder/'2026-11-13-six-mode-cubic-nonzero-moment-anchor-necessity-verify.py'
spec=importlib.util.spec_from_file_location('six_point_exact',path)
six=importlib.util.module_from_spec(spec);spec.loader.exec_module(six)
alg=six.alg
point=six.data['planes'][0]


class Poly:
    def __init__(self,x=0):
        self.d={k:Q(v) for k,v in x.items() if v} if isinstance(x,dict) else ({(0,0,0):Q(x)} if x else {})
    def __add__(self,b):
        if not isinstance(b,Poly):b=Poly(b)
        d=self.d.copy()
        for k,v in b.d.items():
            z=d.get(k,Q(0))+v
            if z:d[k]=z
            elif k in d:del d[k]
        return Poly(d)
    __radd__=__add__
    def __neg__(self):return Poly({k:-v for k,v in self.d.items()})
    def __sub__(self,b):return self+-b if isinstance(b,Poly) else self+-Poly(b)
    def __rsub__(self,b):return -self+b
    def __mul__(self,b):
        if not isinstance(b,Poly):b=Poly(b)
        d={}
        for k,v in self.d.items():
            for l,w in b.d.items():
                m=tuple(x+y for x,y in zip(k,l));d[m]=d.get(m,Q(0))+v*w
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self,n):
        z=Poly(1)
        for _ in range(n):z=z*self
        return z
    def __eq__(self,b):return self.d==(b.d if isinstance(b,Poly) else Poly(b).d)
    def diff(self,j):
        out={}
        for k,v in self.d.items():
            if k[j]:
                l=list(k);l[j]-=1;out[tuple(l)]=v*k[j]
        return Poly(out)
    def evaluate(self,y):
        return sum((v*y[0]**k[0]*y[1]**k[1]*y[2]**k[2] for k,v in self.d.items()),0)


def determinant(A):
    n=len(A);out=0
    for p in itertools.permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        product=sign
        for i in range(n):product=product*A[i][p[i]]
        out=out+product
    return out


def rank(A,prime=None):
    A=[[Q(x) for x in row] for row in A] if prime is None else [[int(x)%prime for x in row] for row in A]
    pos=0
    for k in range(len(A[0])):
        row=next((i for i in range(pos,len(A)) if A[i][k]),None)
        if row is None:continue
        A[pos],A[row]=A[row],A[pos]
        inverse=1/A[pos][k] if prime is None else pow(A[pos][k],-1,prime)
        A[pos]=[x*inverse if prime is None else x*inverse%prime for x in A[pos]]
        for i in range(pos+1,len(A)):
            z=A[i][k]
            if z:A[i]=[x-z*y if prime is None else (x-z*y)%prime for x,y in zip(A[i],A[pos])]
        pos+=1
        if pos==len(A):break
    return pos


def uniform_component():
    mon=[tuple(x) for x in data['cubic_monomials']];where={m:i for i,m in enumerate(mon)}
    Y=[Poly({tuple(int(i==j) for i in range(3)):1}) for j in range(3)]
    rec=list(map(Q,point['recurrence']))
    def tail(head,n):
        out=list(head)
        while len(out)<n:out.append(sum(rec[j]*out[-j-1] for j in range(3)))
        return out
    bases=[tail([Q(i==j) for i in range(3)],7) for j in range(3)]
    C=point['conic_matrix']
    const=[[Q(0)]*6 for _ in mon]
    hcols=[[Poly() for _ in range(3)] for _ in mon]
    rhs=[Poly() for _ in mon]
    for i,j,k in itertools.product(range(3),repeat=3):
        exponent=tuple(int(i==n)+int(j==n)+int(k==n) for n in range(3));row=where[exponent]
        rhs[row]=rhs[row]+Y[i]*Y[j]*Y[k]
        for h in range(3):
            const[row][h]+=4*bases[h][i+j+k]
            hcols[row][h]=hcols[row][h]-6*Y[i]*bases[h][j+k]
        const[row][3+k]+=C[i][j]
    N=[[Q(x) for x in row] for row in data['projector']]
    assert rank(const)==6 and rank(N)==4
    assert [row[6:] for row in N]==[[Q(i==j) for j in range(4)] for i in range(4)]
    assert all(sum(N[i][k]*const[k][j] for k in range(10))==0 for i in range(4) for j in range(6))
    H=[[sum((N[i][k]*hcols[k][j] for k in range(10)),Poly()) for j in range(3)] for i in range(4)]
    b=[sum((N[i][k]*rhs[k] for k in range(10)),Poly()) for i in range(4)]
    augmented=determinant([row+[value] for row,value in zip(H,b)])
    mean=tail(Y,5)
    mean_hankel=determinant([[mean[i+j] for j in range(3)] for i in range(3)])
    cubic=Poly(dict(zip(mon,data['new_mean_cubic_coefficients'])))
    assert augmented==Q(data['augmented_determinant_factor'])*mean_hankel*cubic
    head_minor=determinant(H[:3])
    polynomial=[Q(x) for x in point['parameter_polynomial_integer_ascending']]
    polynomial=[x/polynomial[-1] for x in polynomial]
    Exact=six.quotient_class(polynomial[:3])
    y=[Exact(x) for x in point['mean_head']]
    h=[Exact(x) for x in point['second_moment_head']]
    assert not cubic.evaluate(y)
    assert head_minor.evaluate(y)
    assert mean_hankel.evaluate(y)
    assert all(not (sum((H[i][j].evaluate(y)*h[j] for j in range(3)),Exact())+b[i].evaluate(y)) for i in range(4))
    # Rank 15 means every quartic lies in the ideal of the three partials.
    mon2=[(a,b,2-a-b) for a in range(2,-1,-1) for b in range(2-a,-1,-1)]
    mon4=[(a,b,4-a-b) for a in range(4,-1,-1) for b in range(4-a,-1,-1)]
    matrix=[]
    for i in range(3):
        for m in mon2:
            row=Poly({m:1})*cubic.diff(i)
            matrix.append([int(row.d.get(n,0))%103 for n in mon4])
    assert rank(matrix,103)==15
    return dict(exact_constant_rank=6,exact_projector_rank=4,
                exact_augmented_determinant_factor=data['augmented_determinant_factor'],
                exact_augmented_determinant_identity=True,
                chosen_mean_cubic_zero=True,chosen_three_by_three_head_minor_nonzero=True,
                chosen_mean_hankel_determinant_nonzero=True,
                chosen_point_satisfies_all_four_head_equations=True,
                smooth_mean_cubic_quartic_matrix_rank_mod103=15)


PRIME=103
RELATION=[97,11,96]
def mod(x):
    x=Q(x);assert x.denominator%PRIME
    return x.numerator%PRIME*pow(x.denominator%PRIME,-1,PRIME)%PRIME


class Field:
    def __init__(self,x=0):
        self.a=x.a if isinstance(x,Field) else tuple(mod(z) for z in x) if isinstance(x,(list,tuple)) else (mod(x),0,0)
    def __add__(self,b):b=Field(b);return Field([(x+y)%PRIME for x,y in zip(self.a,b.a)])
    __radd__=__add__
    def __neg__(self):return Field([-x for x in self.a])
    def __sub__(self,b):return self+-Field(b)
    def __rsub__(self,b):return Field(b)+-self
    def __mul__(self,b):
        b=Field(b);c=[0]*5
        for i in range(3):
            for j in range(3):c[i+j]+=self.a[i]*b.a[j]
        for k in [4,3]:
            for j in range(3):c[k-3+j]-=c[k]*RELATION[j]
        return Field([x%PRIME for x in c[:3]])
    __rmul__=__mul__
    def __pow__(self,n):
        out=Field(1);base=self
        while n:
            if n%2:out=out*base
            base=base*base;n//=2
        return out
    def __truediv__(self,b):
        b=Field(b);assert b
        return self*b**(PRIME**3-2)
    def __bool__(self):return any(self.a)
    def __eq__(self,b):return self.a==Field(b).a


class Jet:
    def __init__(self,x=0):
        if isinstance(x,Jet):self.a=x.a
        elif isinstance(x,dict):self.a=tuple(Field(x.get(i,0)) for i in range(4))
        else:self.a=(Field(x),Field(),Field(),Field())
    def __add__(self,b):b=Jet(b);return Jet({i:x+y for i,(x,y) in enumerate(zip(self.a,b.a))})
    __radd__=__add__
    def __neg__(self):return Jet({i:-x for i,x in enumerate(self.a)})
    def __sub__(self,b):return self+-Jet(b)
    def __rsub__(self,b):return Jet(b)+-self
    def __mul__(self,b):
        b=Jet(b)
        return Jet({k:sum((self.a[i]*b.a[k-i] for i in range(k+1)),Field()) for k in range(4)})
    __rmul__=__mul__
    def __truediv__(self,b):return Jet({i:x/Field(b) for i,x in enumerate(self.a)})
    def __pow__(self,n):
        out=Jet(1)
        for _ in range(n):out=out*self
        return out


def eliminate_field(A,b=None):
    A=[row[:]+([b[i]] if b is not None else []) for i,row in enumerate(A)]
    determinant=Field(1)
    for k in range(len(A)):
        row=next(i for i in range(k,len(A)) if A[i][k])
        if row!=k:A[row],A[k]=A[k],A[row];determinant=-determinant
        v=A[k][k];determinant=determinant*v
        A[k]=[x/v for x in A[k]]
        for i in range(len(A)):
            if i==k:continue
            v=A[i][k]
            if v:A[i]=[x-v*y for x,y in zip(A[i],A[k])]
    return determinant,([row[-1] for row in A] if b is not None else None)


def local_nonzero_data():
    assert all((t**3+96*t*t+11*t+97)%103 for t in range(103))
    rec=[Field(Q(x)) for x in point['recurrence']]
    def tail(head,n):
        out=[Field(x) for x in head]
        while len(out)<n:out.append(sum((rec[j]*out[-j-1] for j in range(3)),Field()))
        return out
    base=tail(point['mean_head'],6)+tail(point['second_moment_head'],11)
    alg.P=Jet;alg.QH=[[Jet(x) for x in row] for row in six.original_qh]
    qindices=[2,4,5]+list(range(6,17))
    A=[[Field(int(i==j)+(5 if j==2 and i==3 else 0)) for j in qindices] for i in range(17)]
    def qgradient(g):return [g[2]+5*g[3]]+[g[i] for i in qindices[1:]]
    M=[[Field() for _ in range(14)] for _ in range(14)]
    for j in range(14):
        x=[Jet({0:z,1:A[i][j]}) for i,z in enumerate(base)]
        _,gradient,_=alg.formula(x)
        assert all(not z.a[0] for z in gradient)
        for i,z in enumerate(qgradient(gradient)):M[i][j]=z.a[1]
    assert M==[list(row) for row in zip(*M)]
    det,_=eliminate_field(M)
    assert list(det.a)==data['fourteen_block_determinant_mod103cubed']
    norm_exponent=103**2+103+1
    assert det**norm_exponent==data['fourteen_block_norm_mod103']
    x=[Jet({0:z,1:int(i==3)}) for i,z in enumerate(base)]
    for order in [1,2]:
        _,gradient,_=alg.formula(x)
        _,correction=eliminate_field(M,[-z.a[order] for z in qgradient(gradient)])
        for i in range(17):
            x[i]=x[i]+Jet({order:sum((A[i][j]*correction[j] for j in range(14)),Field())})
    R,gradient,_=alg.formula(x)
    assert all(not z.a[j] for z in qgradient(gradient) for j in range(3))
    beta=x[3]-5*x[2]+Q(32,5)*x[1]-Q(8,5)*x[0]
    assert beta.a==(Field(),Field(1),Field(),Field())
    coefficient=R.a[3]
    assert list(coefficient.a)==data['reduced_normal_cubic_mod103cubed']
    assert coefficient**norm_exponent==data['reduced_normal_cubic_norm_mod103']
    return dict(parameter_cubic_irreducible_mod103=True,
                fourteen_block_determinant_mod103cubed=list(det.a),
                fourteen_block_norm_mod103=data['fourteen_block_norm_mod103'],
                reduced_normal_cubic_mod103cubed=list(coefficient.a),
                reduced_normal_cubic_norm_mod103=data['reduced_normal_cubic_norm_mod103'],
                q_indices_zero_based=qindices,
                beta='y3 - 5*y2 + 32/5*y1 - 8/5*y0',
                fourteen_eliminated_gradient_jets_verified=True,
                scope='Only nonzero exact local quantities are inferred from this reduction; no exact Hessian rank is claimed.')


def verify():
    return dict(all_pass=True,uniform=uniform_component(),local=local_nonzero_data(),
                scope='The exact uniform identity constructs an irreducible two-dimensional critical graph. The two nonzero local quantities support the ordinary local-algebra proof J^3 subset I subset J and radical(I)=J near the three specified algebraic points. No global Jacobian power certificate or new actual operator inverse is claimed.')


if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
