# distutils: libraries = flint
# cython: language_level=3
"""Exact complete polynomial matrix operations over the ORIGINAL quadratic field.

Every coefficient a+b*z uses the actual field generator and its actual
relation z^2=u+v*z.  No prime-subfield projection, reduction of nilpotents,
fraction-field solve, or truncation is performed.
FLINT API: https://flintlib.org/doc/nmod_poly.html
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Compile/use mathematical operations only in public research Actions.")

from libc.stdlib cimport malloc, free
from sage.all import matrix

cdef extern from "flint/nmod_poly.h":
    ctypedef struct nmod_poly_struct:
        pass
    void nmod_poly_init(nmod_poly_struct *, unsigned long)
    void nmod_poly_clear(nmod_poly_struct *)
    void nmod_poly_zero(nmod_poly_struct *)
    void nmod_poly_set(nmod_poly_struct *, const nmod_poly_struct *)
    void nmod_poly_set_coeff_ui(nmod_poly_struct *, long, unsigned long)
    unsigned long nmod_poly_get_coeff_ui(const nmod_poly_struct *, long)
    long nmod_poly_length(const nmod_poly_struct *)
    long nmod_poly_degree(const nmod_poly_struct *)
    int nmod_poly_is_zero(const nmod_poly_struct *)
    int nmod_poly_equal(const nmod_poly_struct *, const nmod_poly_struct *)
    void nmod_poly_mul(nmod_poly_struct *, const nmod_poly_struct *, const nmod_poly_struct *)
    void nmod_poly_add(nmod_poly_struct *, const nmod_poly_struct *, const nmod_poly_struct *)
    void nmod_poly_sub(nmod_poly_struct *, const nmod_poly_struct *, const nmod_poly_struct *)
    void nmod_poly_neg(nmod_poly_struct *, const nmod_poly_struct *)
    void nmod_poly_scalar_mul_nmod(nmod_poly_struct *, const nmod_poly_struct *, unsigned long)
    void nmod_poly_divrem(nmod_poly_struct *, nmod_poly_struct *,
                         const nmod_poly_struct *, const nmod_poly_struct *)

cdef long _degree(const nmod_poly_struct *a, const nmod_poly_struct *b):
    cdef long da=nmod_poly_degree(a), db=nmod_poly_degree(b)
    return da if da >= db else db

cdef bint _zero(const nmod_poly_struct *a, const nmod_poly_struct *b):
    return nmod_poly_is_zero(a) and nmod_poly_is_zero(b)

cdef void _multiply_pair(nmod_poly_struct *c0, nmod_poly_struct *c1,
                        const nmod_poly_struct *a0, const nmod_poly_struct *a1,
                        const nmod_poly_struct *b0, const nmod_poly_struct *b1,
                        unsigned long u, unsigned long v,
                        nmod_poly_struct *s) noexcept:
    # s has four initialized entries; outputs do not alias inputs or s.
    nmod_poly_mul(s, a0, b0)
    nmod_poly_mul(s+1, a1, b1)
    nmod_poly_add(s+2, a0, a1)
    nmod_poly_add(s+3, b0, b1)
    nmod_poly_mul(s+2, s+2, s+3)
    nmod_poly_sub(s+2, s+2, s)
    nmod_poly_sub(s+2, s+2, s+1)
    nmod_poly_scalar_mul_nmod(s+3, s+1, u)
    nmod_poly_add(c0, s, s+3)
    nmod_poly_scalar_mul_nmod(s+3, s+1, v)
    nmod_poly_add(c1, s+2, s+3)

cdef class CompleteQuadraticMatrix:
    cdef nmod_poly_struct *entry
    cdef long initialized, count, nr, nc
    cdef unsigned long p, u, v
    cdef object ring, field, generator

    def __cinit__(self, ring=None, values=None, long rows=0, long columns=0):
        cdef long i,j,e,at
        cdef object polynomial, coefficients, scalar, coords, modulus
        self.entry=NULL
        self.initialized=0
        self.count=0
        self.nr=0
        self.nc=0
        if ring is None:
            return
        self.ring=ring
        self.field=ring.base_ring()
        if int(self.field.degree()) != 2:
            raise ValueError("Use the entire actual degree-two constant field.")
        prime=int(self.field.characteristic())
        if prime<3 or prime>=2**31 or int(self.field.cardinality()) != prime**2:
            raise ValueError("Expected the actual small odd quadratic finite field.")
        self.p=prime
        self.generator=self.field.gen()
        modulus=self.field.modulus()
        if modulus.degree()!=2 or modulus[2]!=1:
            raise ValueError("The original quadratic generator must have a monic relation.")
        self.u=int(-modulus[0]) % prime
        self.v=int(-modulus[1]) % prime
        assert self.generator**2==self.field(self.u)+self.field(self.v)*self.generator
        if values is not None:
            if values.base_ring() is not ring:
                raise ValueError("Do not silently identify different original rings.")
            rows=int(values.nrows())
            columns=int(values.ncols())
        if rows<0 or columns<0:
            raise ValueError("Negative matrix dimensions.")
        self.nr,self.nc=rows,columns
        self.count=2*rows*columns
        if self.count:
            self.entry=<nmod_poly_struct *>malloc(self.count*sizeof(nmod_poly_struct))
            if self.entry==NULL:
                raise MemoryError()
        for at in range(self.count):
            nmod_poly_init(self.entry+at,self.p)
            self.initialized+=1
        if values is not None:
            for i in range(rows):
                for j in range(columns):
                    polynomial=ring(values[i,j])
                    at=2*(i*columns+j)
                    for e,scalar in enumerate(polynomial.list()):
                        coords=list(scalar.polynomial().list())
                        if len(coords)>2:
                            raise ValueError("A coefficient left the exact original field.")
                        a=int(coords[0]) if coords else 0
                        b=int(coords[1]) if len(coords)>1 else 0
                        if not (0<=a<prime and 0<=b<prime):
                            raise ValueError("Noncanonical prime coordinates.")
                        if self.field(a)+self.field(b)*self.generator!=scalar:
                            raise ValueError("The complete original coefficient did not return.")
                        nmod_poly_set_coeff_ui(self.entry+at,e,a)
                        nmod_poly_set_coeff_ui(self.entry+at+1,e,b)

    def __dealloc__(self):
        cdef long at
        if self.entry!=NULL:
            for at in range(self.initialized):
                nmod_poly_clear(self.entry+at)
            free(self.entry)
            self.entry=NULL

    cdef void compatible(self, CompleteQuadraticMatrix other) except *:
        if self.ring is not other.ring or self.p!=other.p or self.u!=other.u or self.v!=other.v:
            raise ValueError("Different complete original quadratic coefficient domains.")

    cdef CompleteQuadraticMatrix copy(self):
        cdef CompleteQuadraticMatrix result=CompleteQuadraticMatrix(self.ring,None,self.nr,self.nc)
        cdef long at
        for at in range(self.count):
            nmod_poly_set(result.entry+at,self.entry+at)
        return result

    cdef bint equal(self, CompleteQuadraticMatrix other) except *:
        cdef long at
        self.compatible(other)
        if self.nr!=other.nr or self.nc!=other.nc:
            return False
        for at in range(self.count):
            if not nmod_poly_equal(self.entry+at,other.entry+at):
                return False
        return True

    def to_matrix(self):
        cdef long i,j,at,e,d
        values=[]
        for i in range(self.nr):
            for j in range(self.nc):
                at=2*(i*self.nc+j)
                d=_degree(self.entry+at,self.entry+at+1)
                values.append(self.ring([
                    self.field(nmod_poly_get_coeff_ui(self.entry+at,e))+
                    self.field(nmod_poly_get_coeff_ui(self.entry+at+1,e))*self.generator
                    for e in range(d+1)]))
        return matrix(self.ring,self.nr,self.nc,values)

cdef CompleteQuadraticMatrix _product(CompleteQuadraticMatrix a, CompleteQuadraticMatrix b):
    cdef CompleteQuadraticMatrix out
    cdef long i,j,k,ia,ib,io,h
    cdef nmod_poly_struct scratch[6]
    a.compatible(b)
    if a.nc!=b.nr:
        raise ValueError("Complete matrix dimensions do not match.")
    out=CompleteQuadraticMatrix(a.ring,None,a.nr,b.nc)
    for h in range(6):
        nmod_poly_init(&scratch[h],a.p)
    try:
        for i in range(a.nr):
            for k in range(a.nc):
                ia=2*(i*a.nc+k)
                if _zero(a.entry+ia,a.entry+ia+1):
                    continue
                for j in range(b.nc):
                    ib=2*(k*b.nc+j)
                    if _zero(b.entry+ib,b.entry+ib+1):
                        continue
                    io=2*(i*b.nc+j)
                    _multiply_pair(&scratch[0],&scratch[1],
                        a.entry+ia,a.entry+ia+1,b.entry+ib,b.entry+ib+1,
                        a.u,a.v,&scratch[2])
                    nmod_poly_add(out.entry+io,out.entry+io,&scratch[0])
                    nmod_poly_add(out.entry+io+1,out.entry+io+1,&scratch[1])
    finally:
        for h in range(6):
            nmod_poly_clear(&scratch[h])
    return out

cdef void _divide_pair(nmod_poly_struct *q0,nmod_poly_struct *q1,
                      nmod_poly_struct *r0,nmod_poly_struct *r1,
                      const nmod_poly_struct *a0,const nmod_poly_struct *a1,
                      const nmod_poly_struct *b0,const nmod_poly_struct *b1,
                      unsigned long u,unsigned long v,
                      nmod_poly_struct *s) except *:
    # s has twelve initialized entries, independent of inputs/outputs.
    cdef long d=_degree(b0,b1)
    if d<0:
        raise ZeroDivisionError("Zero original Hermite diagonal.")
    if nmod_poly_is_zero(b1):
        nmod_poly_divrem(q0,r0,a0,b0)
        nmod_poly_divrem(q1,r1,a1,b0)
    else:
        # bar(b)=(b0+v*b1)-z*b1.  Norm(b) lies in F_p[t].
        nmod_poly_scalar_mul_nmod(s,b1,v)
        nmod_poly_add(s,s,b0)
        nmod_poly_neg(s+1,b1)
        _multiply_pair(s+2,s+3,b0,b1,s,s+1,u,v,s+8)
        if not nmod_poly_is_zero(s+3) or nmod_poly_degree(s+2)!=2*d:
            raise ArithmeticError("Full quadratic norm failed.")
        _multiply_pair(s+4,s+5,a0,a1,s,s+1,u,v,s+8)
        nmod_poly_divrem(q0,s+6,s+4,s+2)
        nmod_poly_divrem(q1,s+7,s+5,s+2)
        _multiply_pair(s+4,s+5,q0,q1,b0,b1,u,v,s+8)
        nmod_poly_sub(r0,a0,s+4)
        nmod_poly_sub(r1,a1,s+5)
    if _degree(r0,r1)>=d:
        raise ArithmeticError("The complete quadratic remainder degree did not decrease.")

cdef tuple _reduce(CompleteQuadraticMatrix source,CompleteQuadraticMatrix H,bint exact):
    cdef CompleteQuadraticMatrix out,C,back
    cdef long i,j,k,at,ht,ct,n=H.nc,h,d
    cdef nmod_poly_struct temp[18]
    source.compatible(H)
    if H.nr!=n or source.nc!=n:
        raise ValueError("Need the entire square Hermite basis and every source column.")
    for i in range(n):
        for j in range(i):
            at=2*(i*n+j)
            if not _zero(H.entry+at,H.entry+at+1):
                raise ValueError("The complete Hermite basis is not upper triangular.")
        at=2*(i*n+i)
        d=_degree(H.entry+at,H.entry+at+1)
        if (d<0 or nmod_poly_get_coeff_ui(H.entry+at,d)!=1 or
                nmod_poly_get_coeff_ui(H.entry+at+1,d)!=0):
            raise ValueError("The full original Hermite diagonal is not monic.")
    out=source.copy()
    C=CompleteQuadraticMatrix(source.ring,None,source.nr,n)
    for h in range(18):
        nmod_poly_init(&temp[h],source.p)
    try:
        for i in range(source.nr):
            for j in range(n):
                at=2*(i*n+j)
                ht=2*(j*n+j)
                _divide_pair(&temp[0],&temp[1],&temp[2],&temp[3],
                    out.entry+at,out.entry+at+1,H.entry+ht,H.entry+ht+1,
                    source.u,source.v,&temp[6])
                nmod_poly_set(C.entry+at,&temp[0])
                nmod_poly_set(C.entry+at+1,&temp[1])
                if not _zero(&temp[0],&temp[1]):
                    for k in range(j,n):
                        ct=2*(i*n+k)
                        ht=2*(j*n+k)
                        if _zero(H.entry+ht,H.entry+ht+1):
                            continue
                        _multiply_pair(&temp[4],&temp[5],
                            &temp[0],&temp[1],H.entry+ht,H.entry+ht+1,
                            source.u,source.v,&temp[6])
                        nmod_poly_sub(out.entry+ct,out.entry+ct,&temp[4])
                        nmod_poly_sub(out.entry+ct+1,out.entry+ct+1,&temp[5])
                if (not nmod_poly_equal(out.entry+at,&temp[2]) or
                        not nmod_poly_equal(out.entry+at+1,&temp[3])):
                    raise ArithmeticError("A complete Hermite row subtraction did not return.")
            for j in range(n):
                at=2*(i*n+j)
                ht=2*(j*n+j)
                if _degree(out.entry+at,out.entry+at+1)>=_degree(H.entry+ht,H.entry+ht+1):
                    raise ArithmeticError("A full output column exceeds its Hermite degree.")
                if exact and not _zero(out.entry+at,out.entry+at+1):
                    raise ArithmeticError("A full polynomial module inclusion failed.")
        if exact:
            back=_product(C,H)
            if not back.equal(source):
                raise ArithmeticError("The full coordinate return C*H=rows failed.")
    finally:
        for h in range(18):
            nmod_poly_clear(&temp[h])
    return out,C

def complete_product(left,right):
    cdef CompleteQuadraticMatrix a=CompleteQuadraticMatrix(left.base_ring(),left)
    cdef CompleteQuadraticMatrix b=CompleteQuadraticMatrix(left.base_ring(),right)
    return _product(a,b).to_matrix()

def complete_remainder_rows(rows,H):
    cdef CompleteQuadraticMatrix a=CompleteQuadraticMatrix(H.base_ring(),rows)
    cdef CompleteQuadraticMatrix b=CompleteQuadraticMatrix(H.base_ring(),H)
    cdef CompleteQuadraticMatrix out
    out,C=_reduce(a,b,False)
    return out.to_matrix()

def complete_hermite_coordinates(H,rows):
    if not H.is_hermite():
        raise ValueError("Need the supplied full certified Hermite basis.")
    cdef CompleteQuadraticMatrix a=CompleteQuadraticMatrix(H.base_ring(),rows)
    cdef CompleteQuadraticMatrix b=CompleteQuadraticMatrix(H.base_ring(),H)
    cdef CompleteQuadraticMatrix C
    out,C=_reduce(a,b,True)
    return C.to_matrix()

def backend_metadata():
    return {"representation":"actual original quadratic generator; two full nmod polynomials",
            "polynomial_struct_bytes":sizeof(nmod_poly_struct),
            "coefficient_projection":False,"nilpotent_truncation":False,
            "fraction_field_or_denominator_clearing":False,
            "all_original_rows_and_columns_retained":True,
            "metadata_call_executes_mathematical_instance":False}
