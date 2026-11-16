#!/usr/bin/env python3
"""R885 complete finite Artin algebras; no factor selection or semisimplicity assumption."""
from flint import nmod_poly

P=1000000753
SOURCE_DIMENSION=272
CORRESPONDENCE_RANK=8

class UnitFailure(RuntimeError):
    def __init__(self,label,witness):
        self.label=str(label)
        self.witness=witness
        super().__init__("The required element is not a unit on the entire fibre: "+self.label)

def polynomial_list(value):
    return [int(value[i]) for i in range(max(0,value.degree()+1))]

class SourceAlgebra:
    """Fp[X]/chi(X), including every factor and its full multiplicity."""
    def __init__(self,modulus,prime=P):
        assert prime==P
        assert len(modulus)==SOURCE_DIMENSION+1 and modulus[-1]==1
        assert all(isinstance(c,int) and 0<=c<prime for c in modulus)
        self.p=prime
        self.n=SOURCE_DIMENSION
        self.modulus=nmod_poly(modulus,prime)
        self.zero=nmod_poly([],prime)
        self.one=nmod_poly([1],prime)
        self.X=nmod_poly([0,1],prime)

    def element(self,raw):
        if isinstance(raw,int):
            return nmod_poly([raw],self.p)
        return nmod_poly(raw,self.p)%self.modulus

    def pack(self,a):
        a=a%self.modulus
        return [int(a[i]) for i in range(self.n)]

    def unpack(self,raw):
        assert len(raw)==self.n and all(isinstance(c,int) and 0<=c<self.p for c in raw)
        return nmod_poly(raw,self.p)

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def neg(self,a):
        return -a

    def mul(self,a,b):
        return (a*b)%self.modulus

    def scale(self,a,c):
        return a*int(c)

    def power(self,a,n):
        assert isinstance(n,int) and n>=0
        answer=self.one
        while n:
            if n&1:
                answer=self.mul(answer,a)
            n//=2
            if n:
                a=self.mul(a,a)
        return answer

    def fraction(self,numerator,denominator):
        numerator=int(numerator);denominator=int(denominator)
        residue=denominator%self.p
        if not residue:
            raise UnitFailure("original_rational_denominator",{
                "exact_original_denominator":str(denominator),"prime":self.p,
                "denominator_residue":0,"whole_fibre_retained":True})
        return self.element(numerator*pow(residue,-1,self.p)%self.p)

    def inverse(self,a,label):
        gcd,u,v=a.xgcd(self.modulus)
        assert u*a+v*self.modulus==gcd
        proof={
            "label":str(label),"prime":self.p,"source_algebra_dimension":self.n,
            "input":self.pack(a),"original_complete_modulus":polynomial_list(self.modulus),
            "gcd":polynomial_list(gcd),"bezout_input_coefficient":polynomial_list(u),
            "bezout_modulus_coefficient":polynomial_list(v),
            "full_unreduced_polynomial_Bezout_identity_verified":True,
            "factors_removed_or_squarefree_replacement_used":False}
        if gcd.degree()!=0 or not int(gcd[0]):
            proof["whole_fibre_unit"]=False
            raise UnitFailure(label,proof)
        scalar=pow(int(gcd[0]),-1,self.p)
        inverse=(u*scalar)%self.modulus
        assert self.mul(a,inverse)==self.one
        proof.update({"whole_fibre_unit":True,"inverse":self.pack(inverse),
                      "normalization_scalar":scalar,"complete_original_algebra_product_equals_one":True})
        return inverse,proof

    def evaluate(self,coefficients,x):
        answer=self.zero
        for c in reversed(coefficients):
            answer=self.add(self.mul(answer,x),self.element(int(c)))
        return answer

class CorrespondenceAlgebra:
    """A[U]/monic P(U), free rank8 over the entire original source algebra A."""
    def __init__(self,A,monic_coefficients):
        assert isinstance(A,SourceAlgebra)
        assert len(monic_coefficients)==CORRESPONDENCE_RANK+1
        assert monic_coefficients[-1]==A.one
        self.A=A;self.n=CORRESPONDENCE_RANK
        self.coefficients=tuple(monic_coefficients)
        self.zero=tuple(A.zero for _ in range(self.n))
        self.one=(A.one,)+tuple(A.zero for _ in range(self.n-1))
        self.U=(A.zero,A.one)+tuple(A.zero for _ in range(self.n-2))

    def element(self,coefficients):
        assert len(coefficients)<=self.n
        return tuple(coefficients)+tuple(self.A.zero for _ in range(self.n-len(coefficients)))

    def constant(self,a):
        return (a,)+tuple(self.A.zero for _ in range(self.n-1))

    def scalar(self,c):
        return self.constant(self.A.element(int(c)))

    def pack(self,x):
        assert len(x)==self.n
        return [self.A.pack(a) for a in x]

    def unpack(self,raw):
        assert len(raw)==self.n
        return tuple(self.A.unpack(row) for row in raw)

    def flat(self,x):
        return [c for a in x for c in self.A.pack(a)]

    def from_flat(self,raw):
        assert len(raw)==self.n*self.A.n
        return tuple(self.A.unpack(raw[i*self.A.n:(i+1)*self.A.n]) for i in range(self.n))

    def add(self,x,y):
        return tuple(self.A.add(a,b) for a,b in zip(x,y))

    def sub(self,x,y):
        return tuple(self.A.sub(a,b) for a,b in zip(x,y))

    def neg(self,x):
        return tuple(self.A.neg(a) for a in x)

    def scale(self,x,c):
        return tuple(self.A.scale(a,c) for a in x)

    def scale_A(self,x,a):
        return tuple(self.A.mul(v,a) for v in x)

    def mul_U(self,x):
        leading=x[-1]
        shifted=(self.A.zero,)+tuple(x[:-1])
        return tuple(self.A.sub(shifted[i],self.A.mul(leading,self.coefficients[i]))
                     for i in range(self.n))

    def mul(self,x,y):
        A=self.A
        product=[A.zero for _ in range(2*self.n-1)]
        for i,a in enumerate(x):
            if a==A.zero:
                continue
            for j,b in enumerate(y):
                if b!=A.zero:
                    product[i+j]=A.add(product[i+j],A.mul(a,b))
        for degree in range(2*self.n-2,self.n-1,-1):
            leading=product[degree]
            if leading!=A.zero:
                for j in range(self.n):
                    product[degree-self.n+j]=A.sub(
                        product[degree-self.n+j],A.mul(leading,self.coefficients[j]))
        return tuple(product[:self.n])

    def power(self,x,n):
        assert isinstance(n,int) and n>=0
        result=self.one
        while n:
            if n&1:
                result=self.mul(result,x)
            n//=2
            if n:
                x=self.mul(x,x)
        return result

    def evaluate_A(self,coefficients,x):
        value=self.zero
        for c in reversed(coefficients):
            value=self.add(self.mul(value,x),self.constant(c))
        return value

    def multiplication_matrix(self,x):
        columns=[]
        value=x
        for j in range(self.n):
            columns.append(value)
            if j+1<self.n:
                value=self.mul_U(value)
        return [[columns[j][i] for j in range(self.n)] for i in range(self.n)]

    def characteristic(self,x):
        """Division-free Berkowitz, coefficient order T^8,d1*T^7,...,d8."""
        A=self.A
        matrix=self.multiplication_matrix(x)
        coefficients=[A.one]
        for start in range(self.n-1,-1,-1):
            size=self.n-start
            h=[A.one,A.neg(matrix[start][start])]
            if size>1:
                right=matrix[start][start+1:]
                vector=[matrix[i][start] for i in range(start+1,self.n)]
                for exponent in range(size-1):
                    value=A.zero
                    for a,b in zip(right,vector):
                        value=A.add(value,A.mul(a,b))
                    h.append(A.neg(value))
                    if exponent+1<size-1:
                        vector=[
                            sum_A(A,[A.mul(matrix[i][j],vector[j-start-1])
                                     for j in range(start+1,self.n)])
                            for i in range(start+1,self.n)]
            result=[]
            for degree in range(size+1):
                result.append(sum_A(A,[
                    A.mul(h[degree-j],coefficients[j])
                    for j in range(max(0,degree-len(h)+1),min(degree,len(coefficients)-1)+1)]))
            coefficients=result
        assert len(coefficients)==self.n+1 and coefficients[0]==A.one
        value=self.one
        for c in coefficients[1:]:
            value=self.add(self.mul(value,x),self.constant(c))
        assert value==self.zero
        proof={"prime":A.p,"base_dimension":A.n,"extension_rank":self.n,
               "coefficient_order":"T^8,d1*T^7,...,d8",
               "multiplication_matrix_over_entire_A":[[A.pack(a) for a in row] for row in matrix],
               "characteristic_coefficients_over_A":[A.pack(a) for a in coefficients],
               "division_free_Berkowitz_used":True,
               "all8_Cayley_Hamilton_coordinates_verified":True,
               "norm_is_last_coefficient_because_rank8_even":True,
               "squarefree_factorization_or_geometric_point_selection_used":False}
        return coefficients,proof

    def inverse(self,x,label):
        coefficients,proof=self.characteristic(x)
        proof["label"]=str(label);proof["input"]=self.pack(x)
        norm=coefficients[-1]
        try:
            norm_inverse,norm_proof=self.A.inverse(norm,str(label)+"_complete_norm")
        except UnitFailure as exc:
            proof.update({"whole_fibre_unit":False,"base_norm_unit_witness":exc.witness})
            raise UnitFailure(label,proof) from None
        candidate=self.one
        for c in coefficients[1:-1]:
            candidate=self.add(self.mul(candidate,x),self.constant(c))
        inverse=self.neg(self.scale_A(candidate,norm_inverse))
        assert self.mul(x,inverse)==self.one
        proof.update({"whole_fibre_unit":True,"base_norm_unit_witness":norm_proof,
                      "inverse":self.pack(inverse),"complete2176_scalar_product_equals_one":True})
        return inverse,proof

def sum_A(A,values):
    answer=A.zero
    for value in values:
        answer=A.add(answer,value)
    return answer
