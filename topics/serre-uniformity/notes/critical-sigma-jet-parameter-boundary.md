# A parameter boundary for the critical sigma jet

Date: 2026-11-14. Status: proved boundary of a proposed argument. This is
**not a counterexample to the original $C_p$**, and it makes no claim
about the value at the actual completed CM constant.

## 1. The data that stay fixed and the datum that is varied

Let $p\ge41$ be prime with $p\equiv5\pmod6$, and work over
$k=\overline{\mathbf F}_p$. Retain the original
$E_0:y^2=x^3-1$, $\omega=dx/(2y)$, the real cyclic six-isogeny of R697,
and its reduction

$$
\pi:E_0\longrightarrow E',\qquad
E':Y^2=X^3+aX+c_0,\qquad \pi^*(dX/(2Y))=\omega,
$$
$$
a=-180\alpha^2-240\alpha-375,\qquad
c_0=-2100\alpha^2-3360\alpha-5566,\qquad \alpha^3=4.
\tag{B.1}
$$

Use the same nonzero two-torsion point $Q_+$ of R697,

$$
X(Q_+)=5+2\alpha^2+2\beta(\alpha^2+2\alpha+3),\qquad
Y(Q_+)=0,\qquad\beta^2=3.
\tag{B.2}
$$

The curve and this point are fixed throughout. The actual completed
weight-two constant is

$$
s=2\alpha^2+4\alpha+5.
\tag{B.3}
$$

Only for the boundary argument, replace $s$ by an independent parameter
$c$. In the polynomial differential algebra
$k[c,X,Y,e]/(Y^2-X^3-aX-c_0)$ use

$$
Dc=0,\qquad DX=2Y,\qquad DY=3X^2+a,\qquad De=-X-c.
\tag{B.4}
$$

Define ordinary Bell polynomials, without divided factorials, by

$$
S_0=1,\qquad S_{m+1}=DS_m+eS_m,
$$
$$
F_m(c)=S_m(X(Q_+),0,0;c)\in k[c].
\tag{B.5}
$$

At $c=s$, these are exactly the even-branch ordinary derivatives
$f_m^+$ in R697. At other $c$, the Gaussian factor has changed. Such
values are not the arithmetic roots $A_k$ of the original problem.

## 2. The common nonzero Cartier constant

Put $p=6N+5$ and use the unchanged original constant

$$
B=(-1)^{N+1}\binom{3N+2}{2N+1}\in\mathbf F_p^\times.
\tag{B.6}
$$

R574 proves on $E_0$

$$
D^p=0,\qquad D^{p-1}x=-B.
\tag{B.7}
$$

All factors in the displayed binomial coefficient are units modulo
$p$. In particular, the sign and nonzero value in (B.7) are fixed,
rather than inferred from an unspecified Hasse scalar.

The normalized six-isogeny has the exact addition formula

$$
\pi^*X(P)=x(P)+
 \sum_{0\ne T\in\ker\pi}\bigl(x(P+T)-x(T)\bigr).
\tag{B.8}
$$

The invariant derivative commutes with translation, and the five
$x(T)$ terms are constants. Applying $D^{p-1}$ gives

$$
\pi^*(D^{p-1}X)=-6B.
$$

Pullback on function fields is injective, so

$$
-D^{p-1}X=\beta_p:=6B\in k^\times.
\tag{B.9}
$$

Similarly, (B.7) and the preserved differential imply $D^p=0$ on
$k(E')$. Neither assertion depends on $c$.

## 3. The shifted jet is a unit for every Gaussian parameter

For any derivation in characteristic $p$, the ordinary Bell identity is

$$
S_p=e^p+D^{p-1}e.
\tag{B.10}
$$

For completeness, write the ordinary derivative of a formal exponential
as the sum over set partitions of $p$ labeled elements, a block of size
$j$ contributing $D^{j-1}e$. Cyclic permutation of the labels preserves
each contribution. Every orbit has size $p$ except the partition into
singletons and the single-block partition: a partition fixed by the
cyclic group gives a block system for its transitive prime-degree
action, so only those two occur. Reducing the partition sum modulo $p$
proves (B.10) coefficientwise over the differential polynomial ring.
This proof involves no division by $p!$.

Since $p-1\ge2$ and $Dc=0$, equations (B.4) and (B.10) give

$$
S_p=e^p-D^{p-2}X=:K,\qquad DK=-D^{p-1}X=\beta_p.
\tag{B.11}
$$

Translation by the two-torsion point $Q_+$ is compatible with negation:
$Q_+-P=-(Q_++P)$. Consequently $X(Q_++P)$ is even in the local
group parameter and every odd invariant derivative of $X$ vanishes
at $Q_+$. Since $p-2$ is odd,

$$
D^{p-2}X(Q_+)=0.
$$

Together with $e(Q_+)=0$, this proves the two identities

$$
\boxed{
F_p(c)=0,\qquad F_{p+1}(c)=\beta_p=6B\ne0
\quad\text{in }k[c].
}
\tag{B.12}
$$

Indeed $S_{p+1}=DS_p+eS_p=\beta_p+eK$. Thus the same model,
point, nonzero Cartier constant, and shifted ordinary jet are
unchanged for every $c$.

## 4. The critical jet is a nonconstant polynomial

For $m<p$, all factorials used in an ordinary Taylor expansion through
degree $m$ are units. We may therefore work in
$k[c][z]/(z^{m+1})$ with the local coordinate satisfying
$D=d/dz$ to the required order. Equivalently, one may first use the
universal characteristic-zero differential polynomials and then
reduce, since no denominator divisible by $p$ is introduced in this
range.

Changing $c=0$ to an arbitrary $c$ changes the logarithmic derivative
by $-cz$. With both functions equal to $1$ at zero, the finite formal
identity is

$$
f_c(z)=\exp(-cz^2/2)f_0(z)\pmod{z^{m+1}}.
$$

In ordinary derivatives this says precisely

$$
F_m(c)=
m!\sum_{j=0}^{\lfloor m/2\rfloor}
 \frac{(-c/2)^j}{j!(m-2j)!}F_{m-2j}(0).
\tag{B.13}
$$

Every denominator is a unit because $m<p$. Now take
$m=p-1$ and $r=(p-1)/2$. The highest term comes only from $j=r$,
where $F_0(0)=1$. Hence

$$
\boxed{
\deg_c F_{p-1}(c)=r,\qquad
[c^r]F_{p-1}(c)=\frac{(p-1)!}{r!}(-1/2)^r\in k^\times.
}
\tag{B.14}
$$

In particular, $F_{p-1}(c)$ has at least one root in $k$ and is not
identically zero. At each such root, the shifted derivative in
(B.12) remains the same unit $6B$.

This does not require a numerical prime example or a finite prime
window.

## 5. Exact scope of the obstruction

The following data, taken alone, do not imply that the critical
ordinary derivative is a unit:

- the fixed supersingular curve $E'$ and the fixed point $Q_+$;
- the nonzero Cartier constant $6B$;
- the identities $F_p=0$ and $F_{p+1}=6B$.

They all persist along the parameter family above, whereas
$F_{p-1}$ vanishes at some parameters. This is an obstruction to
deriving a critical-jet unit from those data alone.

The original problem has additional structure. It fixes the
completed CM constant (B.3), the theta line bundle and its Gaussian,
and the entire tame marking. In that original normalization R697
gives, with $f_4^+$ denoting the characteristic-zero derivative
whose reduction is $F_4(s)$,

$$
A_p=
6\,2^{-(p-5)/2}\frac{F_{p-1}(s)}{F_4(s)},\qquad
N_{\mathbf Q(\alpha,\beta)/\mathbf Q}(f_4^+)=2^{26}3^{10},
$$
$$
C_p\equiv-3A_p^2\pmod p.
\tag{B.15}
$$

Thus the remaining question is still the nonvanishing of
$F_{p-1}(s)$ at this one specified constant. No root from (B.14)
has been identified with $s$, and the proof makes no assertion
about $F_4(c)$ at the other parameters. It is therefore neither an
actual $C_p$ counterexample nor a proof that the original unit
assertion is false.

The same distinction applies to the shifted original units in R702:
their proof is valid, but their existence alone cannot be run
backward across the factorial and pole boundary to determine $A_p$.

## References within the repository

- [R574](../results/R574-completed-zeta-Cartier-input.md), especially
  (574R.3)--(574R.7) and the ordinary Bell identity (574R.17).
- [R697](../results/R697-original-sigma-six-sections-and-integral-square-roots.md),
  the fixed six-isogeny, its Gaussian constant, the actual point,
  and the base-derivative norm.
- [R702](../results/R702-first-pole-block-and-uniform-shifted-units.md),
  including the explicitly positive range of its shifted recurrence.
