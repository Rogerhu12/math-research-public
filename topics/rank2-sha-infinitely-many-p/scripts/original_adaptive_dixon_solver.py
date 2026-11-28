#!/usr/bin/env sage-python
"""One original polynomial right-hand side, with a factored finite residue operator."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research Actions.")

from itertools import product
import numpy as np
from sage.all import vector
from original_ys_divisor_ideal_tools import finite_field_coordinates, polynomial_digest


def _coeffs(k, c):
    return finite_field_coordinates(c, k)


def _digits(poly, pi):
    while poly:
        poly, digit = poly.quo_rem(pi)
        yield digit


def _join(digits, pi):
    """Balanced evaluation of all little-endian pi-adic digits."""
    if not digits:
        return pi.parent().zero()
    power = pi
    while len(digits) > 1:
        pairs = [digits[i] + power * digits[i+1] for i in range(0, len(digits)-1, 2)]
        if len(digits) % 2:
            pairs.append(digits[-1])
        digits = pairs
        if len(digits) > 1:
            power *= power
    return digits[0]


def _places(R, det_bound):
    k, t = R.base_ring(), R.gen()
    for a in k:
        yield t - a
    h = 1
    while int(k.cardinality())**h <= det_bound:
        h += 1
    for e in range(2, h+1):
        for coefficients in product(k, repeat=e):
            pi = R(list(coefficients) + [k.one()])
            if pi.is_irreducible():
                yield pi


class _PrimeLU:
    """PLU for one finite coefficient array, without a polynomial or constant inverse."""
    def __init__(self, rows, p):
        self.p, self.n = p, rows.shape[0]
        n = self.n
        if rows.shape != (n,n) or n*(p-1)**2 >= (1 << 62):
            raise ValueError("Invalid finite residue matrix dimension or dot-product bound")
        self.a = a = rows.copy() % p
        self.perm = perm = np.arange(n)
        self.inverse_pivots = np.empty(n, dtype=np.int64)
        self.nonsingular = False
        for j in range(n):
            choices = np.flatnonzero(a[j:,j])
            if not len(choices):
                return
            i = j + int(choices[0])
            if j != i:
                a[[j,i],:] = a[[i,j],:]
                perm[[j,i]] = perm[[i,j]]
            inv = pow(int(a[j,j]), -1, p)
            self.inverse_pivots[j] = inv
            multipliers = a[j+1:,j]*inv % p
            a[j+1:,j] = multipliers
            a[j+1:,j+1:] = (a[j+1:,j+1:] - multipliers[:,None]*a[j,j+1:]) % p
        self.nonsingular = True

    def solve_column(self, rhs):
        if not self.nonsingular:
            raise ArithmeticError("Singular finite residue center")
        z = rhs[self.perm].copy()
        for j in range(self.n):
            z[j] = (int(z[j])-int(self.a[j,:j] @ z[:j])) % self.p
        for j in reversed(range(self.n)):
            r = int(z[j])-int(self.a[j,j+1:] @ z[j+1:])
            z[j] = (r*int(self.inverse_pivots[j])) % self.p
        return z


class OneRightHandSide:
    """Row convention x*M=a. Only the constant residue operator is factored.

    Build the original coefficient maps for u*M, where each coordinate of u
    has degree <deg(pi). Its pi-adic digits are linear over the ORIGINAL prime
    field. The same maps serve every lift, including a prime/quadratic k and a
    higher-degree good place. A transposed polynomial-matrix call needs its
    own pack; the graph's main path uses only M_D and actual table columns.
    """
    def __init__(self, M, progress=None, max_pack_bytes=768*1024**2):
        self.M, self.R = M, M.base_ring()
        self.k, self.n = self.R.base_ring(), int(M.nrows())
        self.p, self.f = int(self.k.characteristic()), int(self.k.degree())
        if M.ncols()!=self.n or self.n<1 or self.f not in (1,2) or self.p not in (29,41):
            raise ValueError("Expected a nonempty square matrix over an actual supported field")
        self.d = max((int(pol.degree()) for row in M.rows() for pol in row if pol), default=-1)
        if self.d < 0:
            raise ArithmeticError("The zero matrix has no good place")
        self.scalar_basis = [self.k.one()] if self.f==1 else [self.k.one(),self.k.gen()]
        self.parts = np.zeros((self.d+1,self.f,self.n,self.n),dtype=np.uint8)
        for i,row in enumerate(M.rows()):
            for j,value in enumerate(row):
                for v,coefficient in enumerate(value.list()):
                    self.parts[v,:,i,j] = _coeffs(self.k, coefficient)
        self.rejected = []
        for pi in _places(self.R, self.n*self.d):
            self.pi, self.e = pi, int(pi.degree())
            self.limbs = self.e * self.f
            self.width = self.n * self.limbs
            self.steps = (self.d+self.e-1)//self.e+1
            # The full packed map, its largest dense construction scratch,
            # and the two finite LU copies dominate these explicit arrays.
            estimate = 8*self.width**2*(2*self.steps+7)
            if estimate>max_pack_bytes or self.width*(self.p-1)**2 >= 2**53:
                raise MemoryError("The actual fixed-place native array envelope exceeds its budget")
            test = self._pack(1)
            lu = _PrimeLU(test[:,0,:].T, self.p)
            if lu.nonsingular:
                self.lu = lu
                self.full = self._pack(self.steps).reshape(self.width,-1).astype(np.float64)
                if not np.array_equal(self.full[:,:self.width],test[:,0,:]):
                    raise ArithmeticError("The full packing changed the finite residue operator")
                self.full.setflags(write=False)
                break
            self.rejected.append(polynomial_digest(pi))
        else:
            raise ArithmeticError("No certified good place: the polynomial matrix is singular")
        del self.parts
        self.progress = progress

    def _pack(self, amount):
        """Build digit rows from the actual scalar relation, never an assumed quadratic basis."""
        n, e, f, w, p, R = self.n,self.e,self.f,self.width,self.p,self.R
        a = np.zeros((w,amount,w),dtype=np.int64)
        t = R.gen()
        for v in range(self.d+1):
            for b in range(f):
                input_slice = self.parts[v,b]
                if not np.any(input_slice):
                    continue
                for h in range(e):
                    for c in range(f):
                        scalar = (self.scalar_basis[c]*self.scalar_basis[b])*t**(v+h)
                        for m, digit in enumerate(_digits(scalar,self.pi)):
                            if m>=amount:
                                break
                            for g, coefficient in enumerate(digit.list()):
                                for u, value in enumerate(_coeffs(self.k,coefficient)):
                                    if value:
                                        target = a[h*f+c::e*f,m,g*f+u::e*f]
                                        target += int(value)*input_slice.astype(np.int64)
        a %= p
        return a

    def _flatten(self, source):
        if len(source)!=self.n:
            raise ValueError("Every original coordinate is required")
        out = np.zeros((self.n,self.e,self.f),dtype=np.int64)
        for i, polynomial in enumerate(source):
            if polynomial and polynomial.degree()>=self.e:
                raise ValueError("An unreduced pi digit reached the residue solver")
            for j, c in enumerate(polynomial.list()):
                out[i,j,:] = _coeffs(self.k,c)
        return out.reshape(-1)

    def _unflatten_coordinate(self, flat, i):
        block = flat[i*self.limbs:(i+1)*self.limbs].reshape(self.e,self.f)
        return self.R([sum((self.scalar_basis[b]*int(row[b]) for b in range(self.f)),
                           self.k.zero()) for row in block])

    def solve_residue(self, source):
        rhs = self._flatten([p % self.pi for p in source])
        z = self.lu.solve_column(rhs)
        exact = z.astype(np.float64) @ self.full[:,:self.width]
        if not np.array_equal(exact.astype(np.int64)%self.p,rhs):
            raise ArithmeticError("Finite PLU solution did not return the entire source")
        return vector(self.R,[self._unflatten_coordinate(z,i) for i in range(self.n)])

    def digits(self, source):
        source = vector(self.R,source)
        carries = np.zeros((self.steps,self.width), dtype=np.int64)
        while True:
            remainders = []
            if any(source):
                quotients = []
                for polynomial in source:
                    quotient,remainder = polynomial.quo_rem(self.pi)
                    quotients.append(quotient)
                    remainders.append(remainder)
                source = vector(self.R,quotients)
                carries[0] = (carries[0]+self._flatten(remainders))%self.p
            rhs = carries[0].copy()
            digit = self.lu.solve_column(rhs)
            # Each integer dot has nonnegative terms and total < 2^53. BLAS
            # evaluates integer-exact sums in binary64; no matrix solve uses floats.
            raw = digit.astype(np.float64) @ self.full
            actual = raw.astype(np.int64).reshape(self.steps,self.width) % self.p
            if not np.array_equal(actual[0],rhs):
                raise ArithmeticError("A complete residue digit failed its original return")
            carries[0] = 0
            carries[:-1] = (carries[1:]-actual[1:])%self.p
            carries[-1] = 0
            yield digit

    def reconstruct_row(self, source, numerator_cap, denominator_cap, verify):
        a, b = max(0,int(numerator_cap)), max(0,int(denominator_cap))
        maximum = (a+b)//self.e+1
        target = min(32,maximum)
        digits = []
        stream = self.digits(source)
        while True:
            while len(digits)<target:
                digits.append(next(stream))
            # At early attempts use balanced strict caps. The final attempt
            # uses the proved (possibly unequal) original numerator/denominator bounds.
            degree = self.e*target
            ca, cb = (a,b) if target==maximum else (min(a,(degree-1)//2),min(b,(degree-1)//2))
            modulus = self.pi**target
            if self.progress is not None:
                self.progress('original one-RHS rational reconstruction attempt', residue_degree=self.e,
                    residue_prime_dimension=self.width, actual_pi_digits=target,
                    modulus_total_degree=degree, numerator_cap=ca, denominator_cap=cb)
            coordinates = []
            common = self.R.one()
            for i in range(self.n):
                value = _join([self._unflatten_coordinate(row,i) for row in digits],self.pi)
                if not value:
                    num,den = self.R.zero(),self.R.one()
                else:
                    num,den = self._reconstruct(value,modulus,ca,cb)
                    if den is None:
                        break
                coordinates.append((num,den))
                common = common.lcm(den).monic()
                if common.degree()>b:
                    break
            if len(coordinates)==self.n and common.degree()<=b:
                W = vector(self.R,[num*(common//den) for num,den in coordinates])
                if verify(W,common):
                    return W,common,dict(place_sha256=polynomial_digest(self.pi),
                        residue_degree=self.e, prime_linear_dimension=self.width,
                        rejected_place_sha256=list(self.rejected), lift_digits=target,
                        finite_modulus_degree=degree, numerator_cap=a,denominator_cap=b,
                        whole_original_row_identity_verified=True)
            if target==maximum:
                raise ArithmeticError("The proved rational reconstruction bound did not return the original row")
            target = min(2*target,maximum)

    def _reconstruct(self, value, modulus, a, b):
        # Extended Euclidean rational reconstruction over the original k[t].
        left,right = modulus,value
        old,den = self.R.zero(),self.R.one()
        while right and right.degree()>a:
            quo,rem = left.quo_rem(right)
            left,right = right,rem
            old,den = den,old-quo*den
        if not right or not den:
            return None,None
        g = right.gcd(den).monic()
        num,den = right//g,den//g
        scale = self.k.one()/den.leading_coefficient()
        num,den = scale*num,scale*den
        if den.degree()>b or den.gcd(modulus).degree()>0 or (value*den-num)%modulus:
            return None,None
        return num,den

    def transposed(self):
        """Transpose original module indices only. The coefficient-field digits stay oriented."""
        cls = type(self)
        other = cls.__new__(cls)
        for name in ('R','k','n','p','f','d','scalar_basis','pi','e','limbs',
                     'width','steps','progress','rejected'):
            setattr(other,name,getattr(self,name))
        other.M = self.M.transpose()
        table = self.full.reshape(self.n,self.limbs,self.steps,self.n,self.limbs)
        other.full = table.transpose(3,1,2,0,4).copy().reshape(self.width,-1)
        other.full.setflags(write=False)
        other.lu = _PrimeLU(other.full[:,:self.width].T.astype(np.int64),self.p)
        if not other.lu.nonsingular:
            raise ArithmeticError("A nonsingular original operator acquired a singular transpose")
        return other

    def scaled_polynomial_solution(self, source, q, degree_cap, verify):
        """Construct q*source*M^{-1} when it is a polynomial of the proved degree."""
        cap = max(0,int(degree_cap))
        m = cap//self.e+1
        stream = self.digits(source)
        digits = [next(stream) for unused in range(m)]
        modulus = self.pi**m
        z = vector(self.R,[(q*_join([self._unflatten_coordinate(d,i) for d in digits],self.pi))%modulus
                           for i in range(self.n)])
        if not verify(z):
            raise ArithmeticError("A complete reconstructed original column failed its defining equation")
        return z
