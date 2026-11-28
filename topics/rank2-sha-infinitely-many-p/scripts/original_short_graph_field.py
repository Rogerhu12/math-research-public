#!/usr/bin/env sage-python
"""Exact packed coefficient arithmetic for the original degree-one/two fields."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the named public research Actions.")

import numpy as np
from original_ys_divisor_ideal_tools import finite_field_coordinates


class PackedField:
    """Each array starts with an axis for the actual basis 1[, alpha]."""
    def __init__(self, field):
        self.k = field
        self.p = int(field.characteristic())
        self.f = int(field.degree())
        if self.p not in (29, 41) or self.f not in (1, 2):
            raise ValueError("Unsupported original residue field")
        self.basis = [field.one()]
        self.a = self.b = 0
        if self.f == 2:
            self.basis.append(field.gen())
            self.a, self.b = self.coords(field.gen()**2)
            if field.gen()**2 != field(self.a) + field(self.b)*field.gen():
                raise ArithmeticError("Incorrect original constant-field basis")

    def coords(self, value):
        values = tuple(int(c) for c in finite_field_coordinates(value, self.k))
        if len(values) != self.f or any(c < 0 or c >= self.p for c in values):
            raise ArithmeticError("Invalid original field coordinates")
        return values

    def decode(self, digits):
        return sum((int(c)*b for c,b in zip(digits,self.basis)), self.k.zero())

    def reduced(self, x):
        return np.asarray(x, dtype=np.int64) % self.p

    def scalar_times(self, scalar, values):
        """Exact elementwise product; values can have any trailing dimensions."""
        x = np.asarray(values, dtype=np.int64)
        c = np.asarray(scalar, dtype=np.int64)
        if c.shape != (self.f,) or x.shape[0] != self.f:
            raise ValueError("Invalid packed scalar action")
        if self.f == 1:
            return (c[0]*x) % self.p
        cross = c[1]*x[1]
        return np.stack((c[0]*x[0]+self.a*cross,
                         c[0]*x[1]+c[1]*x[0]+self.b*cross)) % self.p

    def inverse_scalar(self, scalar):
        val = self.decode(scalar)
        if not val:
            raise ZeroDivisionError("A nonzero original scalar was required")
        return self.coords(self.k.one()/val)

    def product(self, left, right):
        """Dense, integer-exact prime-component sums using binary64 BLAS."""
        if left.ndim != 3 or right.ndim != 3 or left.shape[0] != self.f or right.shape[0] != self.f:
            raise ValueError("Invalid packed product shapes")
        if left.shape[2] != right.shape[1]:
            raise ValueError("Incompatible packed product")
        inner = left.shape[2]
        if inner * (self.p-1)**2 >= 2**53:
            raise ArithmeticError("A scalar dot product exceeds the exact binary64 range")
        # Reduce each prime dot BEFORE the quadratic structure constants act.
        def dot(i,j):
            a = np.ascontiguousarray(left[i], dtype=np.float64)
            b = np.ascontiguousarray(right[j], dtype=np.float64)
            return (a @ b).astype(np.int64) % self.p
        if self.f == 1:
            return dot(0,0)[None,...]
        cross = dot(1,1)
        return np.stack(((dot(0,0)+self.a*cross) % self.p,
                         (dot(0,1)+dot(1,0)+self.b*cross) % self.p))

    def row_times(self, row, block):
        return self.product(row[:,None,:], block)[:,0,:]

    def inverse_lower(self, triangular):
        f,n,m = triangular.shape
        if f != self.f or n != m or any(np.any(np.triu(plane,1)) for plane in triangular):
            raise ArithmeticError("Expected an actual lower-triangular block")
        inverse = np.zeros((f,n,n),dtype=np.int64)
        for i in range(n):
            diag = self.inverse_scalar(triangular[:,i,i])
            inverse[:,i,i] = diag
            if i:
                current = self.row_times(triangular[:,i,:i],inverse[:,:i,:i])
                inverse[:,i,:i] = (-self.scalar_times(diag,current)) % self.p
        identity = np.zeros_like(inverse)
        identity[0] = np.eye(n,dtype=np.int64)
        if not np.array_equal(self.product(triangular,inverse),identity):
            raise ArithmeticError("Triangular block inversion failed its complete return")
        return inverse
