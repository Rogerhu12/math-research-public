# R968 — The full-level mixed CM jet and its exact critical factor

Date: 2026-11-20. Session: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: proved full-level modular source, heat identities and exact critical factor criterion.** This continues the single-source identity of
R966. It constructs an actual full-level modular-form polynomial whose marked
value is the original completely filtered antidiagonal, with all scalar
factors. The new full-level space has weight $p-5$ and dimension
$\lfloor N/2\rfloor+1$. No spanning, nonvanishing, or trace/mark comparison is
assumed. No mathematical computation is executed.

## 1. The global mixed Gaussian and the exact modular weight

Use the complete source $\mathcal J_o(z,w;\tau)$ of R966(966.1), with the
same positive $s=i\sqrt3$ and finite character $\epsilon_{2s}$. The exact
theta transformations, retaining both variables, give
$$
\mathcal J_o(z,w;\tau+1)=\rho\mathcal J_o(z,w;\tau),
$$
$$
\mathcal J_o(z/\tau,w/\tau;-1/\tau)
=-\tau\exp(12\pi i zw/\tau)\mathcal J_o(z,w;\tau).
\tag{968.1}
$$
For the second formula the total quadratic exponent is
$3(z+w)^2+s^2(z-w)^2=12zw$. All four terms have the same factor, as in
R959. In particular the original minus sign of the odd term is retained.

Introduce algebraic Taylor variables $x=2\pi iz$, $y=2\pi iw$, and put
$$
\boxed{
\mathscr J(x,y;\tau)
=\frac{e^{-E_2(\tau)xy/2}}{6\eta(\tau)^4}
 \mathcal J_o(x/(2\pi i),y/(2\pi i);\tau).
}
\tag{968.2}
$$
The nonhomogeneous term in
$E_2(-1/\tau)=\tau^2E_2(\tau)+6\tau/(\pi i)$ cancels the Gaussian in
(968.1). Division by $\eta^4$ cancels the $T$ multiplier and changes the
$S$ factor from $-\tau$ to $\tau^{-1}$. Thus
$$
\mathscr J(x/(c\tau+d),y/(c\tau+d);g\tau)
=(c\tau+d)^{-1}\mathscr J(x,y;\tau)
\quad(g\in\mathrm{SL}_2(\mathbf Z)).
\tag{968.3}
$$
Consequently
$$
T_{a,b}(\tau):=[x^a y^b]\mathscr J(x,y;\tau)
\in M_{a+b-1}(\mathrm{SL}_2(\mathbf Z),\mathbf Q).
\tag{968.4}
$$
For negative weights this means zero. Holomorphicity at the cusp follows
directly from the complete ideal sum: all nonzero norms are $1\pmod6$,
the smallest norm is one, and $\eta^4=Q(1+O(Q^6))$. The finite Taylor
coefficients have rational Fourier coefficients. Indeed the unit orbits
vanish unless $a-b=1\pmod6$, and otherwise their factor six cancels the
one in (968.2); conjugate ideals give conjugate algebraic integers. Multiplying
by the integral inverse of $\eta^4/Q$ proves the stated rationality.

## 2. The complete heat recursion on these coefficients

Before the Gaussian change, the norm exponent in the lattice sum gives
$\Theta_Q\mathcal J_o=\partial_x\partial_y\mathcal J_o$ in the algebraic
variables. Also $\Theta_Q\eta^4=E_2\eta^4$ and
$\Theta_Q E_2=(E_2^2-E_4)/2$. Applying these identities to (968.2), with
no restriction of either variable, gives
$$
\boxed{
\left(\Theta_Q-\frac{E_2}{2}
 (x\partial_x+y\partial_y-1)\right)\mathscr J
=\partial_x\partial_y\mathscr J+\frac{E_4}{4}xy\mathscr J.
}
\tag{968.5}
$$
If $D_k=\Theta_\tau-kE_2/12$ is the usual Serre derivative, its coefficient
form is
$$
\boxed{
6D_{a+b-1}T_{a,b}
=(a+1)(b+1)T_{a+1,b+1}+\frac{E_4}{4}T_{a-1,b-1},
}
\tag{968.6}
$$
where negative subscripts are zero. This recursion keeps the same CM
difference $a-b$. It is not a pointwise identification of a high derivative
with a low modular value.

## 3. A homogeneous meromorphic derivative and its finite coefficients

Let $\Lambda_\tau=\mathbf Z+\tau\mathbf Z$ and use the canonical
zero-parameter Weierstrass zeta function. Define
$$
Z_{\rm alg}(y;\tau)
=\frac1{2\pi i}\zeta_{\Lambda_\tau}(y/(2\pi i))
=\frac1y+\sum_{n\ge2}\beta_n(\tau)y^{2n-1},
$$
$$
\beta_n(\tau)=\frac{B_{2n}E_{2n}(\tau)}{(2n)!},
\qquad \nabla_y^{\rm alg}=\partial_y-6Z_{\rm alg}(y;\tau).
\tag{968.7}
$$
The expansion follows from
$G_{2n}/(2\pi i)^{2n}=-B_{2n}E_{2n}/(2n)!$. In particular there is no
linear $y$ term in (968.7); introducing one would change the original sigma
normalization.

Lattice scaling gives the homogeneous transformation
$$
Z_{\rm alg}(y/(c\tau+d);g\tau)
=(c\tau+d)Z_{\rm alg}(y;\tau).
$$
Hence $\nabla_y^{\rm alg}$ raises the weight of the complete generating
function by one. The projection $\Pi_4^x$ of R966 commutes with the
modular transformation. Therefore the actual coefficients
$$
\boxed{
Z_{a,b}(\tau):=[x^a y^b]
 \Pi_4^x(\nabla_y^{\rm alg})^2\mathscr J(x,y;\tau)
\in M_{a+b+1}(\mathrm{SL}_2(\mathbf Z),\mathbf Q)
\quad(a\equiv4\pmod6)
}
\tag{968.8}
$$
are holomorphic modular forms. The generating expression may have a
Laurent pole in $y$, but every fixed coefficient is a finite combination
of holomorphic forms. It has no cusp pole.

For use without any implicit analytic operator, expansion of
$\partial_y^2-12Z_{\rm alg}\partial_y+36Z_{\rm alg}^2-6Z_{\rm alg}'$
gives the exact finite formula
$$
\begin{aligned}
Z_{a,b}={}&(b-4)(b-5)T_{a,b+2}\\
&+\sum_{\substack{n\ge2\\2n\le b+2}}
 6(2n+9-2b)\beta_n T_{a,b-2n+2}\\
&+36\sum_{\substack{n,m\ge2\\2(n+m)\le b+2}}
 \beta_n\beta_m T_{a,b-2(n+m)+2}.
\end{aligned}
\tag{968.9}
$$
The first coefficient comes from
$(b+2)(b+1)-12(b+2)+42=(b-4)(b-5)$. Thus even the order-two poles in
the intermediate operator have been accounted for explicitly.

## 4. First-p integrality and the exact original marked value

Let $p=6N+5\ge41$, $\ell=N-1$, $i+j=\ell$, and put
$$
a=6i+4,\qquad b=6j+1,\qquad a+b=p-6.
$$
Then (968.8) has weight $p-5=6N$, strictly below $p-1$.
All Taylor indices of $\mathscr J$ needed in (968.9) have total degree
at most $a+b+2=p-4<p$. Their factorials and the Gaussian factorials
are therefore units at $p$. Also
$$
2n\le b+2\le p-8<p-1.
$$
The weighted Eisenstein form $B_{2n}E_{2n}$ has $p$-integral Fourier
coefficients in this range: its constant term is $B_{2n}$, which is
$p$-integral by von Staudt--Clausen, and its nonconstant coefficients are
$-4n\sigma_{2n-1}$. This argument does not assume that the separately
normalized $E_{2n}$ is $p$-integral when $p$ divides a Bernoulli numerator.
The factorial denominator in (968.7) is also a unit. Thus
$$
Z_{6i+4,6j+1}\in M_{p-5}(\mathrm{SL}_2(\mathbf Z),\mathbf Z_{(p)}).
\tag{968.10}
$$

To retain the period factor without inversion, write
$c=\Omega/(2\pi i)$. At the actual mark R966 gives exactly
$$
\mathscr J(x,y;\rho)=c^{-1}\mathscr K_0(cx,cy),\qquad
\nabla_y^{\rm alg}=c\nabla_v
\quad(v=cy).
$$
Therefore
$$
\Pi_4^x(\nabla_y^{\rm alg})^2\mathscr J(x,y;\rho)
=-72c F_0(cx)G_0(cy).
\tag{968.11}
$$
Taking the $(a,b)$ coefficient gives $-72c^{a+b+1}f_i g_j$.
Here $a+b+1=p-5=6N$, and the original R949 scale is
$c^6/E_6(\rho)=-1/864$. Consequently
$$
\boxed{
\left[\frac{Z_{6i+4,6j+1}}{E_6^N}\right]_{\rm mark}
=-72(-864)^{-N} f_i g_j.
}
\tag{968.12}
$$
The exponent is negative. The displayed intermediate power
$c^{a+b+1}$ fixes it uniquely. Since both sides are algebraic and
$p$-integral in the proved range, the comparison reduces modulo $p$
with a unit scalar.

## 5. The same filtered target in a smaller full-level space

Keep the exact weights
$$
w_i=\mathbf1_{(6i+7,p+1)=1}P_{6i+6}(1/s)
$$
from R966(966.17), and form the actual modular polynomial
$$
\mathscr Z_p(C;\tau)
=\sum_{i=0}^{N-1}w_i Z_{6i+4,6(N-1-i)+1}(\tau)C^{6i+4}.
\tag{968.13}
$$
Both original filters are included. This is a polynomial in $C$ with
coefficients in $M_{6N}(\mathrm{SL}_2(\mathbf Z),\mathbf F_p)$.
Its marked specialization is exactly
$$
\boxed{
\left[\frac{\mathscr Z_p(C;\tau)}{E_6^N}\right]_{\rm mark}
=-72(-864)^{-N}\mathcal U_p(C).
}
\tag{968.14}
$$

The full-level basis
$$
E_6^{N-2r}\Delta^r,\qquad 0\le r\le\lfloor N/2\rfloor,
$$
has respective leading $q^r$ coefficients one. Thus it is an integral
basis in the characteristic under consideration, and
$$
\frac{\mathscr Z_p(C;\tau)}{E_6^N}
=\mathscr Q_p(C,U),\qquad
U=\frac\Delta{E_6^2},\qquad
\mathscr Q_p\in\mathbf F_p[C,U],\quad
\deg_U\mathscr Q_p\le\lfloor N/2\rfloor.
\tag{968.15}
$$
At the original mark $U_0=-1/1728$, and
$1+1728U=E_4^3/E_6^2$. Hence
$$
\boxed{
\mathcal U_p=0
\ \Longleftrightarrow\
(1+1728U)\mid\mathscr Q_p(C,U)
\ \Longleftrightarrow\
E_4^3\mid\mathscr Z_p(C;\tau)
\text{ coefficientwise.}
}
\tag{968.16}
$$
This is the same actual same-label three-factor failure as R959 and
R966, now in the full-level space of dimension $\lfloor N/2\rfloor+1$.
It does not identify the full-level polynomial with R959's graph-level
polynomial away from the mark; their exact marked comparison is (968.14)
together with R966(966.18).

## 6. Boundaries of the possible next step

The $N$ displayed coefficient forms lie in a space of dimension about
$N/2$. This does not prove that they span it, that any selected subset
spans it, or that their common factor at $E_4=0$ is absent. The original
primitive and Legendre filters may remove many directions, and must be
kept in any proposed spanning or nonvanishing argument.

The weights allow multiplication of an unfiltered coefficient by the
original $v=V_4^\dagger$ to land in the weight of
$F=V_{p-1}^\dagger$. This does not prove a source inclusion: in R959's
coordinate $X$, $F/v=E_6^NP_N(X)$ can have an odd part in $X$, whereas
the present full-level forms depend on $U=-X^2/3$. Nor does a linear
relation of global modular forms turn the complete supersingular trace
into their value at the marked CM point.

A genuine linear functional from the complete filtered coefficient
space to the unchanged full trace $S$, or to the actual weak Frobenius
unit of R961, would be stronger than the single central implication
excluded by R945. Such a functional has not been constructed here.

This note uses R954/R959's exact theta transformations, R966's complete
single CM source, R949's unchanged period scale, and the standard
Weierstrass Laurent expansion explicitly normalized in (968.7). All
claims above are paper identities. No finite evaluation or uniform
nonvanishing has been substituted for (968.16).


## Sources and exact dependencies

- [R966](R966-single-conductor-two-s-CM-kernel-and-original-critical-jet.md): the complete two-variable conductor-$(2s)$ source, its precise CM rank-two identity, the original derivative operator and both filters.
- [R954](R954-original-odd-sigma-and-conductor-two-s-CM-evaluations.md) and [R959](R959-exact-coarse-CM-factor-criterion-for-the-original-antidiagonal.md): the original finite character, theta conventions, full S and T multipliers and integral triangular bases. The two-variable Gaussian is kept explicitly in (968.1).
- [R949](R949-original-all-weight-sigma-CM-marked-identity.md): the unchanged positive period and the exact scale $c^6/E_6=-1/864$.
- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md) and [R702](R702-first-pole-block-and-uniform-shifted-units.md): original zero-parameter sigma sections and the distinction between the integral first-$p$ range and later pole blocks. The source integrality needed here is also proved directly in §4.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md): original labels, primitive mask and Legendre value. Their exact shifted implementation and the original marked-polynomial comparison are retained from R966.
- [R945](R945-original-central-sigma-zeros-and-same-label-alternatives.md) and [R961](R961-actual-weak-Frobenius-unit-and-Cartier-cokernel-top.md): the separate boundaries on a proposed full-trace or weak-Frobenius-unit comparison, as stated in §6. No such comparison is used as an input.
- Fernando Rodriguez Villegas, *On the Taylor coefficients of theta functions of CM elliptic curves*, [author paper](https://frvillegas.github.io/pdf/frv-cm-theta.pdf), §2.2: canonical Weierstrass sigma/zeta scaling and the normalized lattice Eisenstein conventions. The particular Laurent coefficient formula (968.7) is displayed and used explicitly above. The ordinary-reduction interpolation results of that paper are not used at the present inert primes.

The exact modular source and factor criterion have been proved. Generation of the full space, absence of the displayed common factor, and a functional giving the original complete trace or weak Frobenius unit remain unproved.
