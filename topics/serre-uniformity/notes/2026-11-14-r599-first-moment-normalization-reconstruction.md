# Reconstructing the marked q-principalization first moment

Date: 2026-11-14. **Status: normalization reconstructed and proved;
the principalization and its numerical moment remain unevaluated.**

The public checkpoint refers to an unfinished R599, but does not preserve
its complete first-moment formula. This note therefore defines an explicit
quantity $J_\ell$ from the preserved original principalization conditions.
It does not claim byte-for-byte recovery of a lost R599, and does not
supply an unproved coefficient relating an older symbol $J$ to $b$.

## 1. The same field, prime, norm, and character projector

Keep the original $p=43$, the original 776-bit $q$, the original
$K=\mathbf Q(i)$ and degree-$44$ field $F$, and R591's actual
anti-scalar degree-$43$ field $F_t/F$. The generator is the same
positive $t=1+21pi$ at the first layer. Write
$T=\langle t\rangle$, and keep the original $\tau$-fixed prime
$P_0$ of $F_t$ above the marked prime $\mathfrak q_0$ of $F$.
All $43$ primes above $\mathfrak q_0$ split completely in $F_t/F$.

Put

$$
\alpha_F=1+89460y_F,\qquad
A_\alpha=P_+[\alpha_F],\qquad
P_+=\sum_{j=0}^{43}\widehat\omega^j\sigma^j.
$$

There is no division by $44$. The coefficient of
$\mathfrak q_0$ in $\operatorname{div}(A_\alpha)$
and of $P_0$ in $P_+P_0$ is one.

All multiplicative expressions below are written additively
in the completed $\mathcal O=\mathbf Z_{43}[i]$ character
module. The intended principalization is

$$
\operatorname{div}_{F_t}(X)=P_+P_0,\qquad
N_TX=A_\alpha.
\tag{J.1}
$$

These are full ordinary divisor equalities. In particular
there are no unrecorded auxiliary prime divisors.

Existence in the completed q-unit lattice follows from the
proved pure-$p$ ordinary results. The character class group
of $F_t$ is zero, so a principalization of $P_+P_0$ exists.
Its norm differs from $A_\alpha$ by an ordinary base unit.
The entire unit lattice is
$E_{F_t}=\mathcal O[T]u_t$, with $N_Tu_t=u$ and
$E_F=\mathcal O u$, so this difference can be removed
by an ordinary unit without changing the divisor.

## 2. A definition that includes the q-unit part at the pole

At the fixed completion $(F_t)_{P_0}=K_q$, define

$$
L_j=\ell\bigl(t^jX-\mathbf 1_{j=0}A_\alpha\bigr)
\in k=\mathbf F_{43^2},\qquad 0\le j\le42,
\tag{J.2}
$$

where $\ell$ is exactly the original Weil-normalized
power-residue logarithm. The expression in parentheses
has local valuation zero: only $X$ itself has valuation
one at $P_0$, and all other $t^jX$ have valuation zero
there. Thus (J.2) always evaluates a local unit. It is
also a well-defined homomorphism on the completed local
unit group, so no individual p-adic coefficient is treated
as a literal exponent of a complex algebraic number.

The norm condition gives

$$
\sum_{j=0}^{42}L_j
=\ell(N_TX-A_\alpha)=0.
\tag{J.3}
$$

Define the marked first moment by

$$
\boxed{J_\ell=\sum_{j=0}^{42}jL_j
       =\sum_{j=1}^{42}j\,\ell(t^jX).}
\tag{J.4}
$$

The first expression records the normalized local-unit
vector; the second is equivalent because the missing
pole term has coefficient zero. A future calculation
must retain the original positive $t$ and R591 prime
label when evaluating this sum.

## 3. Independence of the ordinary principalization choice

Suppose $X'$ satisfies the same two conditions (J.1).
Then $e=X'-X$ is an ordinary unit of $F_t$ with norm zero.
Freeness of the complete ordinary lattice
$\mathcal O[T]u_t$ gives

$$
e=(t-1)h\qquad(h\in E_{F_t}).
$$

With $D_T=\sum_{j=0}^{42}jt^j$, the change in (J.4) is

$$
\ell(D_T(t-1)h)=\ell((p-N_T)h)
=-\ell(N_Th).
$$

The norm belongs to $E_F=\mathcal O u$. The original
$\ell(u)=0$ follows also from $u=N_\Gamma y$:
the q extension is totally ramified of degree $p$,
and its residue norm is the pth power. Hence

$$
\boxed{J_\ell(X')=J_\ell(X).}
\tag{J.5}
$$

This argument uses the entire ordinary unit lattice.
It does not permit replacement of $X$ by a local norm
preimage or a field element with additional prime support.

## 4. Reality and the exact conversion of residue conventions

Use the semilinear involution on the chosen character
component, namely complex conjugation together with
conjugation of $\mathcal O$ coefficients. As in R708,
$A_\alpha$ is fixed; the marked $P_0$ is fixed and
$t$ is sent to $t^{-1}$. Averaging any solution of
(J.1) with its conjugate, with coefficient $1/2$,
preserves both exact conditions. By (J.5) it preserves
the moment. We may therefore compute the moment on
an involution-fixed solution.

At the inert q completion, conjugation acts on the
residue field as the qth power, and $q\equiv-1\bmod p$.
For the fixed original Weil root this gives

$$
L_{-j}=-\overline{L_j}.
$$

Reindexing the sum in (J.4) modulo $p$ now gives

$$
\boxed{J_\ell=\overline{J_\ell}\in\mathbf F_{43}.}
\tag{J.6}
$$

If $r_\mu$ denotes the direct exponent in the original
$\mu_{43}$ Weil root, the original relation is
$r_\mu=-2\ell$, not $r_\mu=\ell$. Thus the corresponding
direct-exponent moment is exactly

$$
\boxed{J_r=-2J_\ell.}
\tag{J.7}
$$

Changing the positive generator to $t^a$ would multiply
the first moment by $a^{-1}$; no such change is made.

## 5. What is still required

The quantity (J.4) is fixed by the actual field,
ordinary divisor, norm, prime label, and residue
convention. Its value has not been computed. The
principalization existence proof does not supply
its coordinates or its q residues.

R720 proves the original ordinary bridge
$C=9ib$ and
$\Omega_2=\varepsilon(22+17b)$; hence this last
obstruction vanishes exactly at $b=24$.
That critical value is not the numerical value of
the actual $b$, and is not identified with R204's
separate primal reference value $24$.

A further exact comparison is required before
assigning a coefficient connecting this explicit
$J_\ell$ to $b$ or to a lost, incompletely normalized
R599 symbol. No such coefficient is asserted here.

Dependencies: the actual marked field and prime of
[R591](../results/R591-explicit-marked-anti-p-field-and-relative-maximal-order.md);
the pure-$p$ ordinary lattices and class vanishing in
[R619](../results/R619-ordinary-anti-p-class-group-and-actual-artin-nine.md),
[R657](../results/R657-full-ordinary-class-module-and-exact-scalar-norm-criterion.md),
and
[R686](../results/R686-all-p-power-layers-and-exact-ordinary-class-growth-law.md);
the fixed semilinear marking in
[R708](../results/R708-exact-isogeny-compression-and-the-43-valued-local-norm-fiber.md);
and the actual chain bridge in
[R720](../results/R720-original-C-and-b-by-the-complete-Robert-chain-comparison.md).
