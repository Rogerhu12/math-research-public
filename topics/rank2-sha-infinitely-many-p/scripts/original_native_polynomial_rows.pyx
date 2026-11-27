# distutils: libraries = flint
# cython: language_level=3
"""Whole prime-field polynomial rows for the original R975 operations.

The caller must first verify the complete prime-subfield descent.  Each
operation consumes every column, including every attached column.  This
module chooses no pivots, drops no rows, and makes no geometric verdict.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Compile and use only in the named public Actions repository.")

from libc.stdlib cimport malloc, free

cdef extern from "flint/nmod_poly.h":
    ctypedef struct nmod_poly_struct:
        pass
    void nmod_poly_init(nmod_poly_struct *poly, unsigned long modulus)
    void nmod_poly_clear(nmod_poly_struct *poly)
    void nmod_poly_zero(nmod_poly_struct *poly)
    void nmod_poly_set_coeff_ui(nmod_poly_struct *poly, long exponent, unsigned long value)
    unsigned long nmod_poly_get_coeff_ui(const nmod_poly_struct *poly, long exponent)
    long nmod_poly_length(const nmod_poly_struct *poly)
    long nmod_poly_degree(const nmod_poly_struct *poly)
    int nmod_poly_is_zero(const nmod_poly_struct *poly)
    void nmod_poly_set(nmod_poly_struct *result, const nmod_poly_struct *source)
    void nmod_poly_mul(nmod_poly_struct *result, const nmod_poly_struct *a,
                       const nmod_poly_struct *b)
    void nmod_poly_add(nmod_poly_struct *result, const nmod_poly_struct *a,
                       const nmod_poly_struct *b)
    void nmod_poly_scalar_mul_nmod(nmod_poly_struct *result,
                                   const nmod_poly_struct *source, unsigned long value)


cdef class NativePolynomialRow:
    cdef nmod_poly_struct *entries
    cdef long width
    cdef long initialized
    cdef unsigned long modulus
    cdef object ring
    cdef object field

    def __cinit__(self, ring=None, values=None, long length=0):
        cdef long j
        cdef object items
        self.entries = NULL
        self.width = 0
        self.initialized = 0
        self.modulus = 0
        self.ring = ring
        if ring is None:
            return
        self.field = ring.base_ring()
        p = int(self.field.characteristic())
        if int(self.field.cardinality()) != p or p < 2 or p >= 2**63:
            raise ValueError("The entire caller field must be the verified small prime field.")
        self.modulus = p
        if values is None:
            items = None
            self.width = length
        else:
            items = list(values)
            self.width = len(items)
        if self.width < 0:
            raise ValueError("Negative row width")
        if self.width:
            self.entries = <nmod_poly_struct *>malloc(self.width * sizeof(nmod_poly_struct))
            if self.entries == NULL:
                raise MemoryError()
        for j in range(self.width):
            nmod_poly_init(&self.entries[j], self.modulus)
            self.initialized += 1
            if items is not None:
                self._set_polynomial(&self.entries[j], self.ring(items[j]))

    def __dealloc__(self):
        cdef long j
        if self.entries != NULL:
            for j in range(self.initialized):
                nmod_poly_clear(&self.entries[j])
            free(self.entries)
            self.entries = NULL

    cdef void _set_polynomial(self, nmod_poly_struct *target, object value) except *:
        cdef long exponent
        cdef unsigned long coefficient
        nmod_poly_zero(target)
        for exponent, item in enumerate(value.list()):
            integer = int(item)
            if integer < 0 or integer >= self.modulus or self.field(integer) != item:
                raise ValueError("A coefficient left the exact original prime field.")
            coefficient = integer
            nmod_poly_set_coeff_ui(target, exponent, coefficient)

    cdef void _compatible(self, NativePolynomialRow other) except *:
        if (self.ring is not other.ring or self.width != other.width or
                self.modulus != other.modulus):
            raise ValueError("Different complete polynomial row domains")

    def __len__(self):
        return self.width

    def __getitem__(self, long column):
        cdef long e, length
        if column < 0:
            column += self.width
        if column < 0 or column >= self.width:
            raise IndexError(column)
        length = nmod_poly_length(&self.entries[column])
        return self.ring([nmod_poly_get_coeff_ui(&self.entries[column], e)
                          for e in range(length)])

    def to_list(self):
        return [self[j] for j in range(self.width)]

    def is_zero(self):
        cdef long j
        for j in range(self.width):
            if not nmod_poly_is_zero(&self.entries[j]):
                return False
        return True

    def degree(self, long first=0):
        cdef long j, degree, largest = -1
        if first < 0 or first > self.width:
            raise IndexError(first)
        for j in range(first, self.width):
            degree = nmod_poly_degree(&self.entries[j])
            if degree > largest:
                largest = degree
        return largest

    def entry_degree(self, long column):
        if column < 0 or column >= self.width:
            raise IndexError(column)
        return nmod_poly_degree(&self.entries[column])

    def leading(self, long first, shifts):
        cdef long j, degree, weighted, best_degree = -1, best_column = -1
        if first < 0 or first > self.width or len(shifts) != self.width-first:
            raise ValueError("Wrong complete shifted-column range")
        for j in range(first, self.width):
            degree = nmod_poly_degree(&self.entries[j])
            if degree >= 0:
                weighted = degree + shifts[j-first]
                if weighted > best_degree or (weighted == best_degree and j > best_column):
                    best_degree, best_column = weighted, j
        return (best_degree, best_column)

    def largest_reducible(self, long own_row, columns, reducers, degrees, shifts, long first):
        cdef long k, column, reducer, degree, weighted
        cdef long best_degree = -1, best_column = -1, best_reducer = -1
        if len(columns) != len(reducers) or len(columns) != len(degrees):
            raise ValueError("Incomplete pivot list")
        if first < 0 or first > self.width or len(shifts) != self.width-first:
            raise ValueError("Wrong complete shifted-column range")
        for k in range(len(columns)):
            column, reducer = columns[k], reducers[k]
            if column < first or column >= self.width:
                raise IndexError(column)
            if reducer == own_row:
                continue
            degree = nmod_poly_degree(&self.entries[column])
            if degree >= 0 and degree >= degrees[k]:
                weighted = degree + shifts[column-first]
                if weighted > best_degree or (weighted == best_degree and column > best_column):
                    best_degree, best_column, best_reducer = weighted, column, reducer
        if best_column < 0:
            return None
        return (best_degree, best_column, best_reducer)

    def add_scaled(self, NativePolynomialRow source, coefficient):
        cdef long j
        cdef nmod_poly_struct q, product
        self._compatible(source)
        if self is source:
            raise ValueError("An elementary row addition needs two distinct rows.")
        nmod_poly_init(&q, self.modulus)
        nmod_poly_init(&product, self.modulus)
        try:
            self._set_polynomial(&q, self.ring(coefficient))
            if nmod_poly_is_zero(&q):
                raise ValueError("The original recorded row coefficient must be nonzero.")
            for j in range(self.width):
                nmod_poly_mul(&product, &q, &source.entries[j])
                nmod_poly_add(&self.entries[j], &self.entries[j], &product)
        finally:
            nmod_poly_clear(&product)
            nmod_poly_clear(&q)

    def scale(self, coefficient):
        cdef long j
        cdef unsigned long value
        polynomial = self.ring(coefficient)
        if polynomial.degree() != 0:
            raise ValueError("Only nonzero constant unimodular scaling is allowed.")
        integer = int(polynomial[0])
        if integer <= 0 or integer >= self.modulus or self.field(integer) != polynomial[0]:
            raise ValueError("A scale left the exact prime field.")
        value = integer
        for j in range(self.width):
            nmod_poly_scalar_mul_nmod(&self.entries[j], &self.entries[j], value)


def linear_combination(coefficient_a, NativePolynomialRow a,
                       coefficient_b, NativePolynomialRow b):
    cdef long j
    cdef nmod_poly_struct ca, cb, left, right
    cdef NativePolynomialRow result
    a._compatible(b)
    result = NativePolynomialRow(a.ring, None, a.width)
    nmod_poly_init(&ca, a.modulus)
    nmod_poly_init(&cb, a.modulus)
    nmod_poly_init(&left, a.modulus)
    nmod_poly_init(&right, a.modulus)
    try:
        a._set_polynomial(&ca, a.ring(coefficient_a))
        a._set_polynomial(&cb, a.ring(coefficient_b))
        for j in range(a.width):
            nmod_poly_mul(&left, &ca, &a.entries[j])
            nmod_poly_mul(&right, &cb, &b.entries[j])
            nmod_poly_add(&result.entries[j], &left, &right)
    finally:
        nmod_poly_clear(&right)
        nmod_poly_clear(&left)
        nmod_poly_clear(&cb)
        nmod_poly_clear(&ca)
    return result


def backend_metadata():
    return {
        "backend": "complete original polynomial rows through FLINT nmod_poly",
        "nmod_poly_struct_bytes": sizeof(nmod_poly_struct),
        "unsigned_long_bytes": sizeof(unsigned long),
        "pivot_selection_in_backend": False,
        "source_projection_or_fractional_arithmetic": False,
        "metadata_call_executes_mathematical_instance": False,
    }
