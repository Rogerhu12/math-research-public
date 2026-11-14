# R692 — The actual cubic ray character and an exact three-point theta formula

## Statement and scope

This result gives a weight-one modular-form expression for the *actual*
fixed-conductor central values occurring in R615/R683.  All three cubic
weights are retained.  It is a starting point for a theta factorization,
not an assertion that the remaining characteristic-$p$ coefficients are
units.

Put

$$
\zeta=\frac{-1+\sqrt{-3}}2,\qquad y=\Im\zeta=\frac{\sqrt3}2,
\qquad \epsilon(n)=\left(\frac n3\right),
\qquad m=k-1,
\tag{692.1}
$$

where $k\ge2$ and $k\equiv2\pmod3$.  Let

$$
\Theta(t)=\sum_{a,b\in\mathbf Z}
   e^{2\pi i(a^2-ab+b^2)t}
 =1+6\sum_{n\ge1}\left(\sum_{d\mid n}\epsilon(d)\right)e^{2\pi int}.
\tag{692.2}
$$

For a function of modular weight $w$ write

$$
\delta_w=\frac1{2\pi i}\frac\partial{\partial t}
           -\frac{w}{4\pi\Im t},
\qquad
\delta_1^{(m)}=\delta_{2m-1}\circ\cdots\circ\delta_3\circ\delta_1,
\tag{692.3}
$$

and use the identity operator when $m=0$.  Define

$$
\begin{aligned}
\mathcal V_m={}&2^m\overline{\delta_1^{(m)}\Theta(2\zeta)}\\
&-2^{-m-1}\left(
\zeta^{-1}\overline{\delta_1^{(m)}\Theta(\zeta/2)}
+\zeta^{-2}\overline{\delta_1^{(m)}\Theta((1+\zeta)/2)}
\right).
\end{aligned}
\tag{692.4}
$$

Then the actual Hecke character of R615/R683 satisfies

$$
\boxed{
L(\xi_k,k)=\frac{\pi}{3\sqrt3}\,
               \frac{(-4\pi y)^m}{m!}\,\mathcal V_m.
}
\tag{692.5}
$$

Thus, retaining the *same* $\Omega,\mathcal A,\alpha,\beta$ as R615,

$$
\boxed{
C_k=\frac{(-3)^m}{\alpha\beta\Omega\mathcal A^m}
       \frac{\pi}{3\sqrt3}
       \frac{(-4\pi y)^m}{m!}\,\mathcal V_m.
}
\tag{692.6}
$$

The formula applies to both $k=p$ and $k=p-3$ of the actual Cartier
criterion.  It does not replace a complex nonzero value by a residue-field
unit, and it does not assert a square factorization of $\mathcal V_m$.

## 1. The fixed cubic character belongs to the conductor-six ring-class group

For a generator $\nu$ prime to $6$ write

$$
\nu\bmod3=\delta\zeta^i,\qquad
\nu\bmod2=\zeta^j,
\qquad \delta\in\{\pm1\},\quad i,j\in\mathbf Z/3\mathbf Z.
\tag{692.7}
$$

The actual character is
$\chi_6(\nu)=\delta\zeta^{j-i}$.  Since $2k-1\equiv3\pmod6$,
the canonical Hecke character $\psi$, defined by selecting the generator
congruent to $1$ modulo $3$, obeys

$$
\psi^{2k-1}((\nu))=\delta\nu^{2k-1}.
\tag{692.8}
$$

Indeed multiplication by $\delta\zeta^{-i}$ selects that generator, and
$(\delta\zeta^{-i})^{2k-1}=\delta$.  Hence

$$
\boxed{
\xi_k=\psi^{2k-1}\tau,\qquad
\tau((\nu))=\zeta^{i-j}.
}
\tag{692.9}
$$

The expression for $\tau$ is unchanged by multiplication of $\nu$ by
any unit: multiplication by $\zeta$ increases both $i$ and $j$ by one,
while multiplication by $-1$ only changes $\delta$.  It is nontrivial.
The units of $\mathcal O_K/3$ have order six and those of
$\mathcal O_K/2\cong\mathbf F_4$ have order three.  Since
$\mathcal O_K$ has class number one, the finite ray-class sequence gives

$$
\operatorname{Cl}_K(6)
 \cong(\mathcal O_K/6)^\times/\mathcal O_K^\times,
\qquad \#\operatorname{Cl}_K(6)=18/6=3.
\tag{692.10}
$$

The rational units modulo six are $\{\pm1\}$, already contained in
$\mathcal O_K^\times$.  The usual description of proper ideal classes
of $\mathcal O_6=\mathbf Z+6\mathcal O_K$ therefore gives the same
quotient.  Consequently $\tau$ is a nontrivial character of the
order-three ring-class group of discriminant $-108$.

Its conductor is exactly $(6)$: the $j$ factor is nontrivial on
$(\mathcal O_K/2)^\times$, and the $i$ factor is nontrivial on the
order-three quotient $(1+\pi\mathcal O_K)/(1+\pi^2\mathcal O_K)$,
where $\pi=1-\zeta$.  Thus its exponents at $2$ and $\pi$ are one and
two.  Multiplication by the quadratic finite character in (692.8)
does not cancel the order-three character at $\pi$.  This also recovers
the exact conductor $(6)$, hence CM modular level $3N(6)=108$, for
$\xi_k$ in the weight classes under consideration.

The three reduced primitive positive binary forms of discriminant
$-108$ are

$$
[1,0,27],\quad[4,2,7],\quad[4,-2,7].
\tag{692.11}
$$

For completeness, the reduced-form bound $a\le\sqrt{108/3}=6$, together
with $b^2-4ac=-108$, $|b|\le a\le c$ and primitivity, leaves exactly
these three forms.  The principal form is $[1,0,27]$, and the other two
are inverse nontrivial classes.  This identifies the three-class
structure; it does not select an unproved theta square root.

## 2. Three explicit lattices preserve the actual cubic weights

Each ideal prime to $3$ has a unique generator congruent to $1$ modulo
$3$: the six units map bijectively onto $(\mathcal O_K/3)^\times$.
Write such a generator as $a+3b\zeta$, with $a\equiv1\pmod3$.
Adjoining its negative gives the symmetric sign $\epsilon(a)$.

Consider the three lattices

$$
\begin{aligned}
\Lambda_0&=\mathbf Z+6\mathbf Z\zeta,\\
\Lambda_1&=2\mathbf Z+3\mathbf Z\zeta,\\
\Lambda_2&=2\mathbf Z+3\mathbf Z(1+\zeta).
\end{aligned}
\tag{692.12}
$$

Inside $\mathcal O_3=\mathbf Z+3\mathcal O_K$, their reductions modulo
$2$ are the three $\mathbf F_2$ lines
$\{0,1\}$, $\{0,\zeta\}$ and $\{0,\zeta^2\}$, respectively.
Their pairwise intersection is $2\mathcal O_3$.
Thus an element prime to $2$ belongs to exactly one lattice, and its
cubic factor in (692.9), after taking the primary generator, is
$\zeta^{-j}$ on $\Lambda_j$.

In an absolute-convergence half-plane, put $n=2k-1$ and define

$$
Z_j(s)=\frac12\sum_{0\ne\nu\in\Lambda_j}
 \epsilon(a(\nu))\frac{\nu^n}{|\nu|^{2s}},
\qquad \nu=a(\nu)+3b(\nu)\zeta.
\tag{692.13}
$$

The terms divisible by $3$ vanish because $\epsilon(a)=0$.
Terms in $2\mathcal O_3$ occur in all three sums with the same sign,
and cancel because $1+\zeta^{-1}+\zeta^{-2}=0$.  All remaining terms
are precisely the generators prime to $6$, with their actual character.
Therefore

$$
\boxed{L(\xi_k,s)=Z_0(s)+\zeta^{-1}Z_1(s)+\zeta^{-2}Z_2(s).}
\tag{692.14}
$$

This proves explicitly that no Euler factor at $2$ has been dropped:
the nonunit part cancels in the actual nontrivial cubic component.
The equality continues meromorphically from the absolute-convergence
half-plane.

The norm forms of these lattices are equivalent to (692.11).
For example $\Lambda_1$ gives $4a^2-6ab+9b^2$, which changes to
$4a^2+2ab+7b^2$ under $a\mapsto a+b$; $\Lambda_2$ gives the inverse
class.  The principal lattice gives $a^2-6ab+36b^2$, equivalent to
$a^2+27b^2$.

## 3. The weight-one Eisenstein series and its exact theta normalization

Let

$$
G(t)=\frac12\sum_{(u,v)\in\mathbf Z^2\setminus\{(0,0)\}}
       \frac{\epsilon(v)}{3ut+v},
\tag{692.15}
$$

using Hecke's continuation for the weight-one sum.  Direct Fourier
summation gives

$$
G(t)=L(1,\epsilon)
    +\frac{2\pi}{\sqrt3}\sum_{u,r\ge1}\epsilon(r)e^{2\pi iurt}
    =\frac{\pi}{3\sqrt3}\Theta(t).
\tag{692.16}
$$

Here is a normalization check rather than an appeal to an unspecified
theta convention.  For $u>0$,

$$
\sum_v\frac{\epsilon(v)}{3ut+v}
=\frac\pi3\bigl(\cot\pi(ut+1/3)-\cot\pi(ut+2/3)\bigr)
=\frac{2\pi}{\sqrt3}\sum_{r\ge1}\epsilon(r)e^{2\pi iurt}.
\tag{692.17}
$$

The terms $u$ and $-u$ agree.  The $u=0$ term, including the factor
$1/2$, is $L(1,\epsilon)=\pi/(3\sqrt3)$.  Finally the number of
elements of norm $N>0$ in the Eisenstein integers is
$6\sum_{d\mid N}\epsilon(d)$: factor ideals into split, inert and
ramified primes and use that every ideal is principal with six
generators.  This proves the second equality in (692.2) and all constants
in (692.16).

For a linear form $\ell=3ut+v$, induction gives

$$
\delta_1^{(m)}\ell^{-1}
=m!\left(-\frac1{4\pi\Im t}\right)^m
       \frac{\overline\ell^{\,m}}{\ell^{m+1}}.
\tag{692.18}
$$

The same identity holds for the continued sum (692.15).  One may first
insert $|\ell|^{-2s}$ in the defining sum, differentiate where this is
absolutely convergent, and continue to $s=0$.  This is the standard
Hecke-trick differentiation identity: the derivative identity with the
auxiliary parameter has factors polynomial in $s$, and its specialization
at zero is (692.18).  The relevant Eisenstein family is regular there.
Equivalently it is the weight-one case of the directly proved equation
(16) and Proposition in section 3 of Rodriguez--Villegas--Zagier's
*Square roots of central values of Hecke L-series*.  Their subsequent
square-root theorem is not used.  In particular no assumption $d>3$ or
quadraticity of our *cubic* $\tau$ is imported from that theorem: only
the analytic identity for the displayed $G$ is required.

It follows that

$$
\frac12\sum'\epsilon(v)
 \frac{(3ut+v)^m}{(3u\overline t+v)^{m+1}}
=\frac{(-4\pi\Im t)^m}{m!}\,
      \overline{\delta_1^{(m)}G(t)},
\tag{692.19}
$$

with exactly the same continuation as (692.13).

## 4. Evaluating the three lattices

For $\Lambda_0$ use $\nu=6u\zeta+v=3u(2\zeta)+v$.
For $\Lambda_1$ use
$\nu=3u\zeta+2v=2(3u(\zeta/2)+v)$.
For $\Lambda_2$ use
$\nu=3u(1+\zeta)+2v=2(3u((1+\zeta)/2)+v)$.

In the last two cases the sign character is
$\epsilon(2v)=-\epsilon(v)$.  The central scaling is
$2^{2k-1-2k}=1/2$; it is independent of $k$.  Since the three imaginary
parts are $2y,y/2,y/2$, respectively, (692.19) yields

$$
\begin{aligned}
Z_0(k)&=\frac{(-4\pi y)^m}{m!}\,2^m
       \overline{\delta_1^{(m)}G(2\zeta)},\\
Z_1(k)&=-\frac{(-4\pi y)^m}{m!}\,2^{-m-1}
       \overline{\delta_1^{(m)}G(\zeta/2)},\\
Z_2(k)&=-\frac{(-4\pi y)^m}{m!}\,2^{-m-1}
       \overline{\delta_1^{(m)}G((1+\zeta)/2)}.
\end{aligned}
\tag{692.20}
$$

Substitution into (692.14), followed by (692.16), proves (692.5).
The exact R615/R683 period identity then proves (692.6).

## 5. A convergent Laguerre form and the limits of the reduction

Write $\Theta(t)=\sum_{N\ge0}a_Ne^{2\pi iNt}$, $a_0=1$.
For $Y=\Im t$, equation (692.3) also gives the absolutely convergent
expression

$$
\frac{(-4\pi Y)^m}{m!}\,
\overline{\delta_1^{(m)}\Theta(t)}
=\sum_{N\ge0}a_N L_m(4\pi NY)e^{-2\pi iN\overline t},
\tag{692.21}
$$

where $L_m$ is the ordinary Laguerre polynomial.  Therefore (692.5)
may alternatively be written with three rapidly convergent theta
series, with coefficients $1,-\zeta^{-1}/2,-\zeta^{-2}/2$ and their
respective imaginary parts.  This provides a useful analytic expression
without discarding the fixed cubic character.

As a normalization diagnostic only, the first 180 terms of (692.21),
evaluated at 60 decimal digits, reproduce $C_2=-1/2$, $C_5=9/2$ and
$C_8=-81/70$ from the exact Kronecker recurrence.  The calculation is
not the proof and is not an interval-certified nonvanishing theorem.

The general theta factorization formula, equation (23) of the cited
Rodriguez--Villegas--Zagier paper, allows rational characteristics and
is a legitimate possible next tool for (692.21).  Its later
Hecke-character square-root theorem has more restrictive hypotheses
and is not applied here.  A square factorization with correct signs,
periods, and the three cubic weights still has to be derived.  Even
such a factorization would not, by itself, prove that its square root
is a $p$-adic unit.

## References and dependencies

- R615 and R683: actual $\xi_k$, full six-torsion trace, and exact
  $C_k$ period normalization.
- F. Rodriguez Villegas and D. Zagier, *Square roots of central values
  of Hecke L-series*, sections 2--4, equations (16), (23), and the
  section 3 proposition.  Primary preprint:
  <https://people.mpim-bonn.mpg.de/zagier/files/mpim/92-68/fulltext.pdf>.
  The analytic differentiation identity and the general factorization
  formula are distinguished from that paper's more restrictive final
  Hecke square-root theorem.

