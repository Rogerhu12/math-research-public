#!/usr/bin/env sage-python
"""Complete ordinary, column-reduced Popov with the actual paired block."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the named public research Actions.")

import hashlib
import numpy as np
from sage.all import GF, PolynomialRing, matrix, vector
from original_ys_divisor_ideal_tools import canonical, polynomial_matrix_digest
from original_short_graph_field import PackedField


def change_coefficients(A, ring):
    field = ring.base_ring()
    return matrix(ring,[[
        ring([field(c) for c in q.list()]) for q in row] for row in A.rows()])


def admit_compact_pair(Y, X, try_prime=True):
    """Only the stated compact polynomial inputs descend. Recheck in their original ring."""
    R,k = Y.base_ring(),Y.base_ring().base_ring()
    if X is not None and (X.base_ring() is not R or X.dimensions()!=Y.dimensions()):
        raise ValueError("The complete attached input must retain the original ring and shape")
    f=PackedField(k)
    rec = dict(scope="compact projection and its actual attached block only",
               original_projection_sha256=polynomial_matrix_digest(Y),
               original_attached_sha256=None if X is None else polynomial_matrix_digest(X),
               applied=False, prime_admission_enabled=bool(try_prime))
    if f.f==1 or not try_prime:
        return Y,X,rec
    tested=0
    for name,block in (("projection",Y),("attached",X)):
        if block is None:
            continue
        for i,row in enumerate(block.rows()):
            for j,poly in enumerate(row):
                for a,value in enumerate(poly.list()):
                    tested+=1
                    if f.coords(value)[1]:
                        rec.update(coefficients_examined=tested, first_nondescending=[name,i,j,a])
                        return Y,X,rec
    R0=PolynomialRing(GF(f.p),R.variable_name())
    def down(A):
        if A is None:
            return None
        return matrix(R0,[[R0([f.coords(c)[0] for c in poly.list()])
                           for poly in row] for row in A.rows()])
    y,x=down(Y),down(X)
    if change_coefficients(y,R)!=Y or (x is not None and change_coefficients(x,R)!=X):
        raise ArithmeticError("Prime admission failed the full original paired round-trip")
    rec.update(applied=True,coefficients_examined=tested,
               full_projection_and_attached_roundtrip=True)
    return y,x,rec


class PackedRow:
    """Actual original polynomial coefficients, planes x powers x coordinates."""
    def __init__(self, ring, arithmetic, source):
        self.R,self.field=ring,arithmetic
        self.n=len(source)
        depth=max((int(q.degree())+1 for q in source if q),default=1)
        self.data=np.zeros((arithmetic.f,depth,self.n),dtype=np.uint8)
        for j,poly in enumerate(source):
            for i,c in enumerate(poly.list()):
                self.data[:,i,j]=arithmetic.coords(c)

    def _trim(self, values):
        nz=np.flatnonzero(np.any(values,axis=(0,2)))
        end=int(nz[-1])+1 if len(nz) else 1
        self.data=np.ascontiguousarray(values[:,:end,:],dtype=np.uint8)

    def degrees(self):
        mask=np.any(self.data,axis=0)
        return np.where(np.any(mask,axis=0),len(mask)-1-np.argmax(mask[::-1],axis=0),-1)

    def leading(self):
        mask=np.any(self.data[:,-1,:],axis=0)
        nz=np.flatnonzero(mask)
        return (self.data.shape[1]-1,int(nz[-1])) if len(nz) else (-1,-1)

    def polynomial(self,j):
        v=self.data[:,:,j]
        live=np.flatnonzero(np.any(v,axis=0))
        if not len(live):
            return self.R.zero()
        return self.R([self.field.decode(v[:,a]) for a in range(int(live[-1])+1)])

    def as_vector(self):
        return vector(self.R,[self.polynomial(i) for i in range(self.n)])

    def scale(self,c):
        if not c:
            raise ArithmeticError("Row normalization requires a unit scalar")
        self._trim(self.field.scalar_times(self.field.coords(c),self.data))

    def add_scaled(self,other,poly):
        if other.R is not self.R or other.n!=self.n or self is other or not poly:
            raise ValueError("Invalid complete elementary row operation")
        width=max(self.data.shape[1],int(poly.degree())+other.data.shape[1])
        result=np.zeros((self.field.f,width,self.n),dtype=np.int64)
        result[:,:self.data.shape[1],:]=self.data
        for a,c in enumerate(poly.list()):
            if c:
                result[:,a:a+other.data.shape[1],:]+=self.field.scalar_times(
                    self.field.coords(c),other.data)
        self._trim(result % self.field.p)


def divide_into_rows(source, rows, pivots):
    """One exact source, its full polynomial coordinates, and its actual remainder."""
    R,field=rows[0].R,rows[0].field
    current=PackedRow(R,field,source)
    q=[R.zero() for _ in rows]
    while True:
        deg,j=current.leading()
        if j<0:
            return vector(R,q)
        if deg<pivots[j]:
            raise ArithmeticError("The original source has a nonzero full Popov remainder")
        quo,rem=current.polynomial(j).quo_rem(rows[j].polynomial(j))
        if not quo:
            raise ArithmeticError("A leading division failed to lower the actual monomial")
        q[j]+=quo
        current.add_scaled(rows[j],-quo)
        if current.polynomial(j)!=rem or current.leading()>=(deg,j):
            raise ArithmeticError("The complete source Popov return did not descend")


def complete_popov(Y, X=None):
    n=int(Y.nrows())
    if not n or int(Y.ncols())!=n or (X is not None and (X.base_ring() is not Y.base_ring()
            or X.dimensions()!=Y.dimensions())):
        raise ValueError("Expected a nonempty square original graph projection")
    R,k=Y.base_ring(),Y.base_ring().base_ring()
    field=PackedField(k)
    rows=[PackedRow(R,field,row) for row in Y.rows()]
    side=None if X is None else [PackedRow(R,field,row) for row in X.rows()]
    leaders=[row.leading() for row in rows]
    cap=max(d for d,j in leaders)
    operation_counts=dict(add=0,scale=0)
    stream=hashlib.sha256()
    def add(i,j,q):
        rows[i].add_scaled(rows[j],q)
        if side is not None:
            side[i].add_scaled(side[j],q)
        operation_counts["add"]+=1
        stream.update(canonical(["add",i,j,[field.coords(c) for c in q.list()]]).encode()+b"\n")
    buckets=[set() for _ in range(n)]
    for i,(d,j) in enumerate(leaders):
        if j<0:
            raise ArithmeticError("A whole graph projection is singular")
        buckets[j].add(i)
    pending=[j for j,b in enumerate(buckets) if len(b)>1]
    while pending:
        j=pending.pop()
        if len(buckets[j])<2:
            continue
        pivot,target=sorted(buckets[j],key=lambda i:(leaders[i][0],i))[:2]
        before=leaders[target]
        quo,_=rows[target].polynomial(j).quo_rem(rows[pivot].polynomial(j))
        if not quo:
            raise ArithmeticError("A promised weak-Popov leading division is zero")
        add(target,pivot,-quo)
        after=rows[target].leading()
        if after[1]<0 or after>=before or after[0]>cap:
            raise ArithmeticError("A complete projected row did not strictly descend")
        buckets[j].remove(target)
        buckets[after[1]].add(target)
        leaders[target]=after
        for col in sorted({j,after[1]}):
            if len(buckets[col])>1:
                pending.append(col)
    if any(len(b)!=1 for b in buckets):
        raise ArithmeticError("The true projection did not produce all leading coordinates")
    order=[next(iter(b)) for b in buckets]
    rows=[rows[i] for i in order]
    if side is not None:
        side=[side[i] for i in order]
    stream.update(canonical(["sort",order]).encode()+b"\n")
    pivots=[int(row.polynomial(i).degree()) for i,row in enumerate(rows)]
    for i,row in enumerate(rows):
        c=k.one()/row.polynomial(i).leading_coefficient()
        row.scale(c)
        if side is not None:
            side[i].scale(c)
        stream.update(canonical(["scale",i,field.coords(c)]).encode()+b"\n")
        operation_counts["scale"]+=1
    for i,row in enumerate(rows):
        last=(pivots[i],i)
        while True:
            degrees=row.degrees()
            bad=[(int(d),j) for j,d in enumerate(degrees) if j!=i and d>=pivots[j]]
            if not bad:
                break
            current=max(bad)
            if current>=last:
                raise ArithmeticError("The largest reducible Popov tail did not strictly descend")
            d,j=current
            q,rem=row.polynomial(j).quo_rem(rows[j].polynomial(j))
            if not q:
                raise ArithmeticError("A reducible tail produced a zero quotient")
            add(i,j,-q)
            if row.polynomial(j)!=rem or row.leading()!=(pivots[i],i):
                raise ArithmeticError("A whole-column reduction changed its row pivot")
            last=(d,j)
    B=matrix(R,[row.as_vector() for row in rows])
    C=None if side is None else matrix(R,[row.as_vector() for row in side])
    for i,row in enumerate(rows):
        if row.leading()!=(pivots[i],i) or B[i,i].leading_coefficient()!=1 or any(
                B[i,j] and B[i,j].degree()>=pivots[j] for j in range(n) if j!=i):
            raise ArithmeticError("The returned entire column Popov matrix is invalid")
    # Elementary admitted operations prove B is in the original row module.
    # Independently return every original row/attached row from the final B/C.
    for i,source in enumerate(Y.rows()):
        coeff=divide_into_rows(source,rows,pivots)
        if coeff*B!=source or (C is not None and coeff*C!=X.row(i)):
            raise ArithmeticError("The original complete coupled graph did not return")
    return B,C,dict(canonical_popov_sha256=polynomial_matrix_digest(B),
        attached_sha256=None if C is None else polynomial_matrix_digest(C),
        pivot_degrees=pivots,all_original_rows_returned=True,
        every_elementary_operation_paired=(side is not None),
        original_row_count=n,operations=operation_counts,
        operation_stream_sha256=stream.hexdigest(),polynomial_operation_transcript_retained=False)
