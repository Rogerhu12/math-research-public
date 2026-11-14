# R150 appendix — the rank-two-mean maximal five-jet section is empty

Author: Astra-ISP-1cf8c51d. Date: 2026-11-13 UTC.

## 1. Theorem and the preceding exact reduction

Retain the original six-mode K and all physical Hankel tensors. Suppose

    rank Cat(y)=2,   ess(T3)=W, dim W=3,
    T3(Kv(z))=0 identically.

The highest identity is a necessary part of the original full critical
system. Let D be the unique length-two mean divisor and u its companion:

    y=a v(s)+b v(t), u=a v(s)-b v(t)       if s != t, ab != 0;
    y=a v(s)+b v'(s), u=v(s)              if D=2s, b != 0.

**Theorem.** ess(V) cannot equal five. Moreover y,H,V have a common
supporting vector space of dimension at most four.

The result includes finite and infinite physical points and all
complex coefficients allowed above. It closes the maximal five-jet
case of
R150-appendix-rank-two-mean-five-dimensional-support-and-doubled-maximal-divisor.md.
It does not classify the remaining common spaces of dimension at most
four or the lower mean-rank/higher third-essential-dimension strata.

The preceding result already proves that the common space has
dimension at most five. If ess(V)=5, it proves

    E=E_g, deg g=5, u in W, g>=2D,

and gives

    M=H-yy^T/4=M_W+u z^T+z u^T,
    E=W+Cy+Cz, dim E=5.                              (1.1)

Here M_W is supported on W. The top local V coefficient at every
point of g is nonzero. Thus V is a Frobenius tensor on the exact
length-five Artin algebra A_g.

## 2. A second annihilating direction gives a parity constraint

Since the classes of y and z in E/W are independent, choose lambda
in ann(W) with

    lambda(y)=1, lambda(z)=0.

Because u belongs to W, (1.1) gives H lambda=y/4. Contracting T3 in
this direction gives exactly

    H=2V lambda,   y=8V lambda^2.                    (2.1)

This is a consequence of the same original tensors, not an independent
choice of a central trace.

At a point of g with local length n, if lambda has order a and
lambda^2 is nonzero, the vector V lambda^2 has exact physical jet
length n-2a. This follows from the nonzero top Frobenius coefficient;
there can be no cancellation with another local block.

Suppose first the mean divisor D consists of two different points.
At each point the exact length of y is one, so (2.1) forces

    n-2a=1.

Hence the two corresponding multiplicities of g are odd. The already
proved inequality g>=2D makes each at least three. Their total would
be at least six, contradicting deg g=5. Thus the reduced mean is
impossible in this maximal case.

Now D=2s. Its exact local mean length is two, so n-2a=2. Also n>=4.
If g=5s this parity is impossible. The only remaining divisor is

    g=4s+t,   t != s,                                (2.2)

with lambda of exact order one at s and zero at the simple point t.

## 3. The remaining four-jet block has an explicit cuspidal third tensor

Choose a nonzero local physical curve representative near s. Since
lambda has order one there, its value on that representative may
itself be used as the local parameter epsilon. Let

    u0,u1,u2,u3

be its Taylor jets through order three. Then, exactly on this local
length-four algebra,

    lambda(u0)=0, lambda(u1)=1,
    lambda(u2)=lambda(u3)=0.

This coordinate change is valid also at infinity. It changes only
the local jet basis, not the original bilinear form.

Write the exact V functional at s as eta_j on epsilon^j. At the
other point let the physical representative be w and the coefficient
be kappa, with kappa nonzero. From y=8V lambda^2 and lambda(y)=1,

    eta3=1/8,   y=a u0+u1,   a=8eta2.

Let h=eta1 and c=eta0. Equations (2.1) give the following complete
tensor polynomials, using x0,x1,x2,x3,w for the corresponding linear
directions:

    y=a x0+x1,

    H=2h x0^2+(a/2)x0 x1+(1/2)x0 x2+(1/4)x1^2,

    V=c x0^3+3h x0^2 x1
        +(3a/8)(x0^2 x2+x0 x1^2)
        +(1/8)(3x0^2 x3+6x0 x1 x2+x1^3)
        +kappa w^3.                                 (3.1)

There is no H contribution at t because lambda vanishes there.

Substitution into the original T3=y^3-6yH+4V gives the exact identity

    T3=x0^2[
          (a^3-12ah+4c)x0-(3a/2)x2+(3/2)x3]
        +4kappa w^3.                                (3.2)

In particular all x1^3, x0 x1^2, x0^2 x1, and x0 x1 x2 terms
cancel. The integer certificate supplied below verifies eight times
(3.2) directly from (3.1).

The three directions x0, the bracket in (3.2), and w are independent:
the bracket has a nonzero x3 coefficient, and t is disjoint from the
four-jet block. Thus (3.2) is an irreducible cuspidal plane cubic.
Its cubed direction is the physical point w. Its repeated direction
is the different physical point u0, whose catalecticant rank is one.

The original highest identity would parameterize this cusp by the
three original quintic polars. The degree identity forces a common
quadratic factor and a birational cubic parametrization. The resulting
physical-point/repeated-secant-direction pair is excluded by the
pure original-kernel lemma in
R150-appendix-no-secant-cuspidal-companion-and-outer-mean-rank-drop-exclusion.md.

That lemma's algebraic statement applies to any original physical
point and any nonparallel repeated direction of catalecticant rank
at most two; it does not require a nonsecant mean. Hence its use
with u0 of rank one here is exact. This contradiction excludes (2.2),
and finishes every ess(V)=5 case.

## 4. From the essential V bound to a common four-dimensional support

For clarity, ess(V)<=4 alone would not always imply that y,H,V share
one four-dimensional space. We now prove the needed implication in
the present conormal setting.

The exact minimal common space is

    E0=W+Cy+Ran M.

One inclusion follows from H=M+yy^T/4 and
V=T3/4+y^3/8+(3/2)yM. The reverse inclusion follows because W is
supported by y,H,V and M=H-yy^T/4.

The conormal classification from the preceding appendix gives two
forms. We show that dim E0=5 would force ess(V)=5, already excluded.

If u is outside W, write M=M_W+c u^2. If c=0 then dim E0<=4.
Otherwise, for dim E0=5 the variables y,u,W are independent and

    V=T3(W)/4+y^3/8+(3/2)y M_W+(3c/2)y u^2.

If a constant differentiation direction annihilated V, the u^2
coefficient of its derivative would first force its y-component to
vanish. The yu coefficient would then force its u-component to
vanish. The part independent of y,u is a derivative of T3(W);
because W is essential, its W-component must vanish as well.
Thus V is essential on all five dimensions.

If u belongs to W, write M=M_W+u z^T+z u^T. For dim E0=5,
the variables y,z are independent modulo W and

    V=T3(W)/4+y^3/8+(3/2)y M_W+3yuz.

An annihilating differentiation direction has z coefficient
3[(D y)u+y(D u)]. Independence of y and u forces D y=D u=0.
Its component independent of y,z is then (D T3)/4, forcing its
entire W-component to vanish. The remaining derivative is
3y u(D z), forcing D z=0. Again ess(V)=5.

Both cases contradict the first part of the theorem. Therefore
dim E0<=4, proving the common-support conclusion.

## 5. Exact record and continuing scope

Reproducible author files:

- notes/2026-11-13-rank-two-mean-five-jet-empty-verify.js
- notes/2026-11-13-rank-two-mean-five-jet-empty-certificate.json

The executable checks the four-jet identity (3.2) over the integer
polynomial ring using BigInt arithmetic. The parity argument,
Frobenius support lengths, cusp exclusion, and common-support argument
are proved in the text.

The next part of this stratum is the remaining common dimension at
most four. Neither that classification nor the global vanishing of
the matched Bell cubic, its natural-power Jacobian membership, or
the ordinary Hilbert ISP follows automatically from this support bound.
