# R133 supplement: the complete outer commutator window through order 4480

2026-11-15, visible-exact-astra-0df9.

**A finite-jet extension of the proved true long boundary estimates.**
This note extends the high-order commutator window needed by the
finite-Sobolev tail argument. It preserves every assertion and the sharper
order-2176 constants in
[J.1--J.32](R133-supplement-finite-angular-jet-true-long-DN-Poisson-and-energy.md).
The actual nonlinear long, both curvature means, the unmatched interface,
the full physical source units and the finite length are unchanged.
No new numerical computation is used.

The same finite-jet input domain remains J.1--J.2: 8192 jets of the actual
physical Z and left height f, with $z_*=2^{-36}$ and $F\le2^{-62}$.
For the unmatched boundary also retain J.21--J.22,
$A_*=n+F+\epsilon\le2^{-262144}$.
The actual cap and tail entries are F.23 and J.31--J.32.

## 1. Complete estimates and their exact domains

In the actual physical angle one has
$$
 \max_{0\le q\le4480}
 \|\operatorname{ad}_{\partial_\theta}^q
       (\mathcal N_{B,Z}-\mathcal N_{B,0}):
                          H^{1/2}\to H^{-1/2}\|
                    <2^{131072}(F+\epsilon),
 \tag{E.1}
$$
$$
 \max_{0\le q\le4480}
 \|\operatorname{ad}_{\partial_\theta}^q
       \mathcal B_Z:H^{-1/2}_\perp\to H^{1/2}\|
                    <2^{131072}s_B\epsilon ,
 \tag{E.2}
$$
$$
 \max_{0\le q\le4480}
 \|\operatorname{ad}_{\partial_\theta}^q
       \mathcal E_B:H^{1/2}\to H^{-1/2}\|
                    <2^{131072}A_* .
 \tag{E.3}
$$
These are full operator estimates, including every signed frequency and
all output means before the exact homogeneous total-flux identity is used.
The positive-half-order source output in (E.2) and its negative-half-order
scalar input keep their physical-angle norms. Fixed-coordinate source
conversion still pays the actual Jacobian multipliers in J.30.

The original order-2176 estimates
$2^{65536}(F+\epsilon)$ and $2^{65536}s_B\epsilon$ are not replaced
by the coarser constant. The original uncommuted DN and Poisson bounds
$2^{128}$ and the complete relative-form estimate J.28 also remain valid.

## 2. One finite parameter curve pays the total differentiated order

Use the same degree-8192 polynomials J.5 and the same parameter radius
$1/512$. For the bare slope error T and the bare curvature-source
operator B_bare, the complete A_0 bounds are, respectively,
$$
 2^{43}(F+\epsilon):
       \dot A^2_0\longrightarrow\dot A^1_0\oplus\mathbb C,
 \qquad
 2^{10}s_B\epsilon:
       A_0\longrightarrow\dot A^1_0\oplus\mathbb C .
 \tag{E.4}
$$
For each finite derivative r they acquire the factor $r!512^r$.
The actual real translation jets identify these derivatives with the
operator commutators, exactly as in J.7. The coefficient maps acquire
the same factorial and radius factors.

Four additional commutators give the complete polynomial-lag Schur
bound for either operator, by J.8--J.10 and J.17--J.18.
For multiplication on $H^{\pm1/2}$ one additional actual coefficient
derivative suffices, by J.12. That derivative is paid after taking
the real coefficient jets; no A^1 norm is asserted for the last
synthetic complex jet.

In a Leibniz product containing r coefficient derivatives and q-r
operator derivatives, the complete factorial contribution satisfies
$$
 {q\choose r}(r+1)!\,(q-r+4)!\le(q+5)! .
 \tag{E.5}
$$
To verify it, cancel r! and (q-r)! on the left. The five remaining
linear factors are bounded, in increasing order, by
$q+1,\ldots,q+5$. The same ordered-factor argument handles several
factors whose extra differentiated orders sum to at most five.
This prevents charging each factor as if it separately carried all
q derivatives.

For $q\le4480$, set $N=q+5\le4485<2^{13}$. Then
$$
                 N!512^N<2^{22N}\le2^{98670}.             \tag{E.6}
$$
Each of the complete expressions below has at most three
differentiated factors after its coefficient products are combined.
Their Leibniz summation has at most $(q+1)^2<2^{26}$ terms.
The fixed coefficient bounds, the full signed Schur sums, the finite
number of displayed expressions, the two nonmean/mean decompositions,
and the low-order homogeneous multipliers can together be widened to
less than $2^{1024}$. Thus their total finite budget is below
$2^{98670+26+1024}<2^{131072}$.
This is a symbolic finite inequality. It uses at most 4485 of the
8192 input jets, with no appeal to an unknown analytic width.

For (E.1), apply this count directly to the exact J.14 formula,
combining the coefficient product mu*d before taking its multiplier
norm. For (E.2), keep B_bare intact as in (E.4), take its full
Schur bound first and then multiply by actual mu. The total
differentiated-order count is the same.

## 3. An exact cancellation in the unmatched boundary row

For (E.3) it is useful to combine the actual coefficients before
differentiating. Put
$$
 a=\mu_T-\mu_L,\qquad
 b=\mu_Ld_L-\mu_Td_T,\qquad
 c=\mu_T/\langle\mu_T\rangle-1,\qquad
 P_{\mu_T}=I-(1+c)\langle\,\cdot\,\rangle .
 \tag{E.7}
$$
Start from the exact interface and long DN identities
$$
 \mathcal E_B=P_{\mu_T}
 \{-M_{\mu_T/\mu_L-1}\mathcal N_{B,Z}P_\perp
                     +M_{\mu_T(d_L-d_T)}\partial_\theta\},
$$
$$
 \mathcal N_{B,Z}
    =\mu_L\mathsf C_L-\mu_LT_{Z,f}P_\perp
                                  +\mu_Ld_L\partial_\theta .
$$
The terms containing the same long drift combine exactly:
$$
 -(\mu_T-\mu_L)d_L+\mu_T(d_L-d_T)
                         =\mu_Ld_L-\mu_Td_T .
$$
Consequently the whole operator is
$$
 \boxed{\quad
 \mathcal E_B=P_{\mu_T}
 \{-M_a\mathsf C_L+M_aT_{Z,f}P_\perp
                                      +M_b\partial_\theta\}.
 \quad}                                                  \tag{E.8}
$$
The C_L term already annihilates constants, so an extra P_perp
there is immaterial. The T term retains its entire mean-slope row.
Equation (E.8) is a signed coefficient identity, not subtraction of
two numerical upper bounds.

The same finite parameter disk used in J.24 gives for each of a,b,c
the complete coefficient bound
$$
 \|\partial_\theta^r a\|_{A_0},\
 \|\partial_\theta^r b\|_{A_0},\
 \|\partial_\theta^r c\|_{A_0}
                   <r!512^r\,2^{24}A_*,\qquad r\le8192 .
 \tag{E.9}
$$
For a and b this follows from J.11, J.24 and the original N.19 bounds and the
actual common mu_0; their subtractions preserve the radial zero.
For c the same true mean denominator and its convergent reciprocal
series are used. Thus no second highest-order coefficient estimate
needs to be multiplied into the first.

The projection's commutators have the exact rank-one form
$$
 \operatorname{ad}_{\partial_\theta}^{\,r}P_{\mu_T}
   =-|\partial_\theta^r c\rangle\langle1|,
                  \qquad r\ge1 .                         \tag{E.10}
$$
The mean functional is bounded by one on H^{-1/2}, and the output
has H^{-1/2} norm at most its A_0 norm. Hence this rank-one factor
needs r derivatives, not r+1. The undifferentiated projection has
norm below 3 by J.22. It still preserves the exact total flux
condition.

The worst term in (E.8) is therefore the projection, one actual
coefficient multiplier and T. Its total differentiated order is
at most q+5: four lag derivatives, one multiplier derivative and
no extra derivative for the rank-one output. Apply (E.5)--(E.6).
All terms with two small coefficient factors are no larger than
the stated single A_* budget, since $A_*<1$. This proves (E.3)
with the same $2^{131072}$ constant.

## 4. Energy, source and scope are unchanged

The uncommuted actual form is still the short connector form plus
the genuine long DN form minus E_B, with every original affine
source and both mean rows kept. Its relative bound is exactly
J.28, $\eta_C+2^{150}A_*$, in the common pulled reference energy.
The real scalar-height/density pairing and its genuine adjoint
remain those of D and J. The estimates above give the additional
finite angular commutators for its complete resolvent identity.

The input curvature means, the ordinary/weak charges, the mean
height span with its actual aw(L) factor, and all independent
metric/nu columns are not changed by this extension. Homogeneous
zero total flux is never used to erase an affine flux source.

This note extends only the proved outer commutator window. Any
larger whole-tail inverse must still pay its actual finite angular
coefficient budget, both 4/3 strong windows, its root and strict
propagation, the unchanged all-layer weights and its final source
readout. Those obligations cannot be inferred from (E.1)--(E.3)
alone. Likewise a higher finite inverse is not yet a complete
nonlinear smoothing construction or the final closed exact family.
