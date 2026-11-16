#!/usr/bin/env python3
"""R907 division-free norm of a complete rank8 pencil over the full source algebra."""
from R885_whole_Artin_algebra import SourceAlgebra, CorrespondenceAlgebra

P=1000000753
RANK=8
MAX_T=8

class PolynomialRing:
    """The bounded coefficient range required by an 8x8 affine matrix pencil."""
    def __init__(self,A):
        assert isinstance(A,SourceAlgebra) and A.p==P and A.n==272
        self.A=A
        self.zero=tuple(A.zero for _ in range(MAX_T+1))
        self.one=(A.one,)+tuple(A.zero for _ in range(MAX_T))

    def constant(self,a):
        return (a,)+tuple(self.A.zero for _ in range(MAX_T))

    def linear(self,a,b):
        return (a,b)+tuple(self.A.zero for _ in range(MAX_T-1))

    def add(self,a,b):
        return tuple(self.A.add(x,y) for x,y in zip(a,b))

    def neg(self,a):
        return tuple(self.A.neg(x) for x in a)

    def mul(self,a,b):
        A=self.A;out=[A.zero for _ in range(MAX_T+1)]
        for i,x in enumerate(a):
            if x==A.zero:
                continue
            for j,y in enumerate(b[:MAX_T+1-i]):
                if y!=A.zero:
                    out[i+j]=A.add(out[i+j],A.mul(x,y))
        return tuple(out)

    def sum(self,values):
        result=self.zero
        for x in values:
            result=self.add(result,x)
        return result

    def pack(self,value):
        assert len(value)==MAX_T+1
        return [self.A.pack(x) for x in value]

    def unpack(self,raw):
        assert len(raw)==MAX_T+1
        return tuple(self.A.unpack(row) for row in raw)

    def value(self,raw,t):
        answer=self.A.zero
        for x in reversed(raw):
            answer=self.A.add(self.A.scale(answer,int(t)),x)
        return answer

def pencil_characteristic(E,a,b,budget,load_level,save_level):
    """All c_k(T), in X^8+c1(T)X^7+...+c8(T); no inversion or factorization."""
    assert isinstance(E,CorrespondenceAlgebra) and E.n==RANK
    A=E.A;R=PolynomialRing(A)
    left=E.multiplication_matrix(a);right=E.multiplication_matrix(b)
    matrix=[[R.linear(left[i][j],right[i][j]) for j in range(RANK)] for i in range(RANK)]
    coefficients=[R.one]
    for start in range(RANK-1,-1,-1):
        size=RANK-start
        old=load_level(size)
        if old is not None:
            assert old["size"]==size and old["principal_submatrix_start"]==start
            coefficients=[R.unpack(x) for x in old["characteristic_coefficients_over_A_T"]]
            assert len(coefficients)==size+1 and coefficients[0]==R.one
            continue
        budget()
        h=[R.one,R.neg(matrix[start][start])]
        if size>1:
            r=matrix[start][start+1:]
            vector=[matrix[i][start] for i in range(start+1,RANK)]
            for exponent in range(size-1):
                h.append(R.neg(R.sum(R.mul(x,y) for x,y in zip(r,vector))))
                if exponent+1<size-1:
                    vector=[R.sum(R.mul(matrix[i][j],vector[j-start-1])
                                  for j in range(start+1,RANK))
                            for i in range(start+1,RANK)]
        answer=[]
        for degree in range(size+1):
            answer.append(R.sum(R.mul(h[degree-j],coefficients[j])
                for j in range(max(0,degree-len(h)+1),min(degree,len(coefficients)-1)+1)))
        coefficients=answer
        assert coefficients[0]==R.one
        for k,coefficient in enumerate(coefficients):
            assert all(c==A.zero for c in coefficient[k+1:])
        save_level(size,{
            "size":size,"principal_submatrix_start":start,
            "characteristic_coefficients_over_A_T":[R.pack(c) for c in coefficients],
            "all_original_T_degree_bounds_verified":True,
            "division_free_Berkowitz_over_entire_A_T":True})
    assert len(coefficients)==9
    budget()
    # Complete Cayley-Hamilton in E[T], not values at selected parameters.
    value=[E.one]+[E.zero for _ in range(MAX_T)]
    for coefficient in coefficients[1:]:
        new=[E.zero for _ in range(MAX_T+1)]
        for k in range(MAX_T+1):
            if value[k]!=E.zero:
                new[k]=E.add(new[k],E.mul(value[k],a))
                if k<MAX_T:
                    new[k+1]=E.add(new[k+1],E.mul(value[k],b))
        for k in range(MAX_T+1):
            new[k]=E.add(new[k],E.constant(coefficient[k]))
        value=new
    assert all(x==E.zero for x in value)
    proof={
        "matrix_shape":[8,8],"source_algebra_dimension":272,
        "correspondence_scalar_dimension":2176,"T_degree_range":[0,8],
        "left_multiplication_matrix_over_A":[[A.pack(x) for x in row] for row in left],
        "right_multiplication_matrix_over_A":[[A.pack(x) for x in row] for row in right],
        "characteristic_coefficient_order":"X^8,c1(T)*X^7,...,c8(T)",
        "characteristic_coefficients_over_A_T":[R.pack(x) for x in coefficients],
        "norm_polynomial_over_A":R.pack(coefficients[-1]),
        "all_coefficient_degree_bounds_verified":True,
        "complete_E_T_Cayley_Hamilton_verified":True,
        "Cayley_Hamilton_scalar_coordinates_checked":9*8*272,
        "denominator_or_pencil_section_inversion_used":False,
        "nine_separate_determinants_computed":False,
        "source_factors_or_nilpotents_discarded":False}
    return coefficients,proof

def scale_norm_polynomial(A,coefficients,factor):
    assert len(coefficients)==9
    result=[A.mul(factor,c) for c in coefficients]
    values=[]
    for t in range(9):
        x=A.zero
        for c in reversed(result):
            x=A.add(A.scale(x,t),c)
        values.append(x)
    return result,values

