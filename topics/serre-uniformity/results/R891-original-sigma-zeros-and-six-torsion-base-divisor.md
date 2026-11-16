# R891 — Original sigma coefficient zeros and the full six-torsion base divisor

Date: 2026-11-16. Status: proved geometric interpretation and base-divisor bound. This does not prove that the original primitive/Legendre-visible pair has a nonzero coefficient.

## 1. Actual weight spaces and their local frame

Use exactly R889's original curve, differential, CM parameter, theta section, and distribution:
$$
E_0:y^2=x^3-1,\quad \omega=dx/(2y),\quad
p=6N+5\ge41,\quad k=\mathbf F_{p^2},
$$
$$
L_m=O(mO),\quad
\mathcal H=H^0(E_0,L_{6p}),\quad
Q=q-\frac{d_p}{6B},\quad
\mathcal H_0=\{f^p s_{6p}:f\in H^0(E_0,L_6)\}.
\tag{891.1}
$$
For $0\le r<p$ set
$$
V_r=Q^r\mathcal H_0.
\tag{891.2}
$$
This is the actual six-dimensional theta weight space of character $t^{-r}$. Its construction uses the actual $p$th theta distribution, including the noncommuting term in R889 (889.18a).

At $O$ use the actual local frame $\epsilon_{6p}=s_{6p}/Y^{6p}$. Put
$$
c_n(f)=[z^n](f\sigma^6).
$$
R889 (889.35) gives
$$
[Y^k]\bigl(Y^{6p}Q^r(f^p)\bigr)
=\frac{r!}{k!}(-6B)^{k-r}c_{r-k}(f)^p
\quad(0\le k\le r<p),
\tag{891.3}
$$
and all coefficients with $r<k<p$ are zero. All outside factors in (891.3) are units.

Thus $O$ is a base point of the entire space $V_r$ if and only if the linear functional
$$
c_r:H^0(E_0,L_6)\longrightarrow k
\tag{891.4}
$$
is zero. Here the coefficients of $c_r$ are reduced modulo $p$; the Frobenius in (891.3) is retained. This is a statement about the common vanishing of all six sections, not just one chosen section.

## 2. Why a single original coefficient gives the whole base point

The original rational basis of $H^0(E_0,L_6)$ is
$$
1,\quad x,\quad y,\quad x^2,\quad -xy,\quad x^3.
\tag{891.5}
$$
Under the original order-six automorphism with $z\mapsto\varepsilon z$, its weights are respectively
$$
0,\quad4,\quad3,\quad2,\quad1,\quad0\pmod6.
\tag{891.6}
$$
The factor $\sigma^6$ has weight zero. Therefore $c_r(f)$ can be nonzero only in the summand of (891.5) whose displayed weight is $r\bmod6$.

With exactly R770's coefficients
$$
x\sigma^6=z^4\sum_i f_i z^{6i},\qquad
-xy\sigma^6=z\sum_j g_j z^{6j},
\tag{891.7}
$$
it follows that
$$
\boxed{
f_i=0\ \Longleftrightarrow\
O\text{ is a base point of }V_{6i+4}
\qquad(6i+4<p),
}
$$
$$
\boxed{
g_j=0\ \Longleftrightarrow\
O\text{ is a base point of }V_{6j+1}
\qquad(6j+1<p).
}
\tag{891.8}
$$
There is only one basis vector of weight $4$, and only one of weight $1$. No reflection of the two sigma sequences is used.

## 3. Propagation to all thirty-six marked torsion points

Let $\mathcal G_6$ be the actual six-primary theta group of $L_{6p}$. It commutes with the $p$-primary theta group, hence with $Q$. It also preserves $\mathcal H_0$, by the actual Cartier descent of R878. Consequently every $V_r$ is $\mathcal G_6$-stable.

For any $A\in E_0[6]$, choose a theta lift above translation by $A$. Its action is an isomorphism of the actual line bundle and sends $V_r$ onto itself. In a local trivialization, it transports the germ of a section at $A$ to its germ at $O$ multiplied by an invertible local factor. Thus it preserves common vanishing orders. The choice of theta lift differs only by a nonzero central scalar and has no effect on this assertion.

In particular, if
$$
\nu_r=\min_{v\in V_r,\ v\ne0}\operatorname{ord}_O(v),
\tag{891.9}
$$
then the common vanishing order is $\nu_r$ at every $A\in E_0[6]$. These are the thirty-six actual marked points, all rational over $k$ as in R878; the assertion also holds after extension to $\overline k$.

Let $D_r$ be the full common base divisor of $V_r$. Then
$$
\boxed{
D_r\ \ge\ \nu_r\sum_{A\in E_0[6]}[A].
}
\tag{891.10}
$$
Moreover $D_r$ is invariant under translation by all of $E_0[6]$. Over $\overline k$ this action on the curve is free, so every orbit has thirty-six points, with constant multiplicity in $D_r$. Hence
$$
\deg D_r\equiv0\pmod{36}.
\tag{891.11}
$$
This uses the actual theta lifts and their units in the local frames, not an assumed global action of the norm-one $p$-torus on the curve.

## 4. An exact order formula and its limited degree bound

The functional $c_0$ is nonzero, since $x^3\sigma^6$ has constant one. Define
$$
\mathcal I=\{\,n:0\le n<p,\ c_n\text{ is not the zero functional}\,\}.
$$
Equation (891.3) implies the exact formula
$$
\boxed{
\nu_r=r-\max\{n\le r:n\in\mathcal I\}.
}
\tag{891.12}
$$
Indeed the first nonzero local coefficient among all sections of $V_r$ is the first $k$ for which $c_{r-k}$ is a nonzero functional. Such a $k$ exists with $k\le r$, because $c_0\ne0$. Thus no coefficient beyond the first-$p$ range is needed to compute this common order.

After removal of $D_r$, the six-dimensional space $V_r$ injects into
$H^0(E_0,L_{6p}(-D_r))$. A degree-zero line bundle on an elliptic curve has at most one section, and a positive-degree line bundle has dimension equal to its degree. Therefore
$$
\deg L_{6p}(-D_r)\ge6.
$$
Combining this with (891.10) gives
$$
\boxed{
36\nu_r\le\deg D_r\le6p-6,\qquad
\nu_r\le\left\lfloor\frac{p-1}{6}\right\rfloor=N.
}
\tag{891.13}
$$
In particular the complete six-channel coefficient sequence has no run of more than $N$ zero functionals before degree $p$. This weak bound is stated with its actual size; it is not a fixed-width recurrence.

For the original critical indices $i+j=N-1$, (891.8)--(891.10) identify each failed factor with a genuine full six-torsion base divisor of its own specified weight space. They do not prove that the two such base divisors cannot occur at the complementary indices. Nor do they force the primitive label to be Legendre-visible. The original R770 same-label nonvanishing and the original modular-quotient normal content therefore remain open.

## Sources

- [R889](R889-original-theta-distribution-and-same-label-sigma-jet.md), (889.29)--(889.35): actual weight spaces and the complete first-$p$ jet in the original local frame.
- [R878](R878-original-finite-theta-action-and-section-projections.md), §§1--4: rational six-torsion marking, commuting actual theta groups, and Cartier descent.
- [R770](R770-same-primitive-label-square-and-finite-bilinear-pairing.md), §§1--3: the original two coefficient sequences and complementary same-label indices.

All arguments are algebraic and use the already fixed original marking. No numerical computation or additional prime window is used.
