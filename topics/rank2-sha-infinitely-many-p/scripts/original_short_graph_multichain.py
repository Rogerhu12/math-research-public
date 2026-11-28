#!/usr/bin/env sage-python
"""Complete column-ordered Krylov chains for the original finite polynomial module."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the named public research Actions.")

import numpy as np
from sage.all import identity_matrix, matrix
from original_ys_divisor_ideal_tools import _hermite_remainder_rows, polynomial_matrix_digest
from original_short_graph_field import PackedField
from original_short_graph_popov import PackedRow, divide_into_rows


class StandardQuotient:
    def __init__(self, B):
        self.R=B.base_ring()
        self.field=field=PackedField(self.R.base_ring())
        self.n=n=int(B.nrows())
        if not n or B.ncols()!=n:
            raise ValueError("Expected a complete nonempty square Popov projection")
        self.degrees=degrees=[]
        for i in range(n):
            pivot=B[i,i]
            if not pivot or pivot.leading_coefficient()!=1:
                raise ArithmeticError("A complete Popov pivot is not monic")
            d=int(pivot.degree())
            lead=max((int(B[i,j].degree()),j) for j in range(n) if B[i,j])
            if lead!=(d,i):
                raise ArithmeticError("A complete original row has a different leading position")
            degrees.append(d)
        self.offset=[]
        length=0
        for d in degrees:
            self.offset.append(length)
            length+=d
        self.length=length
        self.active=[j for j,d in enumerate(degrees) if d]
        active_at={j:i for i,j in enumerate(self.active)}
        self.boundaries=np.zeros((field.f,len(self.active),length),dtype=np.float64)
        self.units=np.zeros((field.f,n,length),dtype=np.float64)
        shift_from=[]
        shift_to=[]
        t=self.R.gen()
        for j in range(n):
            own=degrees[j]
            if own:
                self.units[0,j,self.offset[j]]=1
                shift_from.extend(self.offset[j]+a for a in range(own-1))
                shift_to.extend(self.offset[j]+a for a in range(1,own))
                dest=self.boundaries[:,active_at[j],:]
            else:
                dest=self.units[:,j,:]
            for i,block_degree in enumerate(degrees):
                tail=B[j,i]-(t**own if j==i else self.R.zero())
                if tail and tail.degree()>=block_degree:
                    raise ArithmeticError("A true column tail is not a standard remainder")
                for a,c in enumerate(tail.list()):
                    dest[:,self.offset[i]+a]=field.coords(-c)
        self.shift_from=np.asarray(shift_from,dtype=np.intp)
        self.shift_to=np.asarray(shift_to,dtype=np.intp)
        self.top=np.asarray([self.offset[j]+degrees[j]-1 for j in self.active],dtype=np.intp)

    def next(self, value):
        if value.shape!=(self.field.f,self.length):
            raise ValueError("Standard quotient vector has the wrong original degree")
        out=self.field.row_times(np.take(value,self.top,axis=1),self.boundaries)
        out[:,self.shift_to]=(out[:,self.shift_to]+value[:,self.shift_from].astype(np.int64))%self.field.p
        return out


class OriginalChains:
    def __init__(self, quotient, block_size=32):
        self.quotient=quotient
        self.field=field=quotient.field
        f,n,L=field.f,quotient.n,quotient.length
        if block_size<1:
            raise ValueError("A positive pivot block size is required")
        self.block_size=int(block_size)
        self.A=np.zeros((f,L,L),dtype=np.float64)
        self.B=np.zeros((f,L,L),dtype=np.float64)
        self.K=np.zeros((f,L,L),dtype=np.float64)
        self.targets=np.zeros((f,n,L),dtype=np.float64)
        self.S=np.zeros((f,n,L),dtype=np.float64)
        self.pivots=[]
        self.labels=[]
        self.closed=[None]*n
        self.inverse_blocks=[]

    def insert(self, current, j, a):
        field=self.field
        r=len(self.pivots)
        remaining=np.asarray(current,dtype=np.int64).copy()
        coefficients=np.zeros((field.f,r+1),dtype=np.int64)
        lo=0
        for inverse in self.inverse_blocks:
            hi=lo+self.block_size
            columns=self.pivots[lo:hi]
            reduced_pivots=np.take(remaining,columns,axis=1)
            multiplier=field.row_times(reduced_pivots,inverse)
            coefficients[:,lo:hi]=multiplier
            remaining=(remaining-field.row_times(multiplier,self.B[:,lo:hi,:]))%field.p
            if np.any(np.take(remaining,columns,axis=1)):
                raise ArithmeticError("Complete pivot block elimination did not return zero")
            lo=hi
        for i in range(lo,r):
            c=remaining[:,self.pivots[i]].copy()
            coefficients[:,i]=c
            if np.any(c):
                remaining=(remaining-field.scalar_times(c,self.B[:,i,:]))%field.p
        if np.any(np.take(remaining,self.pivots,axis=1)):
            raise ArithmeticError("A prior original pivot was not eliminated")
        nz=np.flatnonzero(np.any(remaining,axis=0))
        if not len(nz):
            self.S[:,j,:r]=coefficients[:,:r]
            self.targets[:,j,:]=current
            self.closed[j]=(a,r)
            return False
        if r>=self.quotient.length:
            raise ArithmeticError("More accepted vectors than the complete original quotient")
        position=int(nz[0])
        value=remaining[:,position].copy()
        self.A[:,r,:]=current
        self.B[:,r,:]=field.scalar_times(field.inverse_scalar(value),remaining)
        self.K[:,r,:r]=coefficients[:,:r]
        self.K[:,r,r]=value
        self.pivots.append(position)
        self.labels.append((j,a))
        if len(self.pivots)%self.block_size==0:
            hi=len(self.pivots)
            lo=hi-self.block_size
            block=np.take(self.B[:,lo:hi,:],self.pivots[lo:hi],axis=2)
            if not np.all(np.diagonal(block[0])==1) or any(
                    np.any(np.diagonal(plane)) for plane in block[1:]):
                raise ArithmeticError("The actual insertion pivots are not normalized")
            inverse=field.inverse_lower(block.transpose(0,2,1)).transpose(0,2,1)
            self.inverse_blocks.append(np.ascontiguousarray(inverse,dtype=np.float64))
        return True

    def solve_dependencies(self):
        f,n,L=self.S.shape
        left=self.S.copy()
        answer=np.zeros((f,n,L),dtype=np.float64)
        hi=L
        while hi:
            lo=max(0,hi-self.block_size)
            diagonal=self.K[:,lo:hi,lo:hi]
            coeff=self.field.product(left[:,:,lo:hi],self.field.inverse_lower(diagonal))
            answer[:,:,lo:hi]=coeff
            left[:,:,lo:hi]-=self.field.product(coeff,diagonal)
            left[:,:,lo:hi]%=self.field.p
            if lo:
                left[:,:,:lo]-=self.field.product(coeff,self.K[:,lo:hi,:lo])
                left[:,:,:lo]%=self.field.p
            hi=lo
        if np.any(left):
            raise ArithmeticError("Triangular dependency solve left a nonzero full residual")
        for lo in range(0,L,self.block_size):
            hi=min(L,lo+self.block_size)
            if not np.array_equal(self.field.product(self.K[:,lo:hi,:hi],self.B[:,:hi,:]),
                                  self.A[:,lo:hi,:]):
                raise ArithmeticError("The full original accepted Krylov vectors did not return")
        if not np.array_equal(self.field.product(answer,self.K),self.S):
            raise ArithmeticError("Dependency coordinates did not return the full normalized basis")
        if not np.array_equal(self.field.product(answer,self.A),self.targets):
            raise ArithmeticError("Dependency coordinates did not return the full original targets")
        return answer


def multichain_hermite(B, degree_bound=None, progress=None, block_size=32):
    Q=StandardQuotient(B)
    R,field,n,L=Q.R,Q.field,Q.n,Q.length
    if degree_bound is not None and L>degree_bound:
        raise ArithmeticError("The actual quotient exceeds its caller-proved ideal degree bound")
    if L==0:
        H=identity_matrix(R,n)
        if B!=H:
            raise ArithmeticError("A zero-length reduced complete projection was not the unit ideal")
        return H,dict(complete_quotient_length=0,accepted_classes=0,first_dependencies=n,
                      hermite_pivot_degrees=[0]*n,all_original_rows_returned=True,
                      both_original_row_module_inclusions_verified=True,
                      full_hermite_sha256=polynomial_matrix_digest(H))
    chain=OriginalChains(Q,block_size)
    for j in reversed(range(n)):
        v=Q.units[:,j,:].copy()
        a=0
        while chain.insert(v,j,a):
            v=Q.next(v)
            a+=1
        if progress is not None and (j%16==0 or j+1==n):
            progress("original full quotient coordinate chain closed",
                     original_coordinate=j,actual_degree=a,accepted_classes=len(chain.labels),
                     complete_quotient_length=L)
    if len(chain.labels)!=L or len(set(chain.pivots))!=L or any(e is None for e in chain.closed):
        raise ArithmeticError("The complete multi-chain quotient failed to span all classes")
    coeff=chain.solve_dependencies()
    eta=[item[0] for item in chain.closed]
    if sum(eta)!=L:
        raise ArithmeticError("Closed complete chain lengths do not sum to the whole quotient")
    rows=[]
    for j in range(n):
        terms=[[field.k.zero() for _ in range(eta[i])] for i in range(n)]
        for r,(i,a) in enumerate(chain.labels):
            c=field.decode(coeff[:,j,r])
            if c:
                if r>=chain.closed[j][1] or i<j or a>=eta[i]:
                    raise ArithmeticError("A dependency used an unavailable or unreduced original class")
                terms[i][a]=-c
        row=[R(values) for values in terms]
        row[j]+=R.gen()**eta[j]
        rows.append(row)
    H=matrix(R,rows)
    if not H.is_hermite() or any(H[j,j].degree()!=eta[j] for j in range(n)):
        raise ArithmeticError("The full original first dependencies did not give the canonical Hermite basis")
    P=[PackedRow(R,field,row) for row in B.rows()]
    for row in H.rows():
        source=divide_into_rows(row,P,Q.degrees)
        if source*B!=row:
            raise ArithmeticError("A returned canonical row missed the actual original module")
    if not _hermite_remainder_rows(B,H).is_zero():
        raise ArithmeticError("The canonical rows missed part of the original full Popov projection")
    return H,dict(complete_quotient_length=L,original_popov_pivots=Q.degrees,
                  accepted_classes=L,first_dependencies=n,hermite_pivot_degrees=eta,
                  complete_target_coordinates_verified=True,
                  every_accepted_original_class_reconstructed=True,
                  both_original_row_module_inclusions_verified=True,
                  last_original_unit_assumed_cyclic=False,
                  complete_constant_degree=field.f,
                  full_hermite_sha256=polynomial_matrix_digest(H))
