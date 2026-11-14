# R712 — The actual second digit of $M_2$ and a two-block reduction

Date: 2026-11-14. **Status: proved and independently reviewed. The actual invariant at 137147 has not been evaluated.**

## 1. Scope and the precise new invariant

Keep the original $c_1$ point, the character $\theta=\theta_{-1}$, the
six-torsion character, and the complete R588/R595/R705 normalization.
Let $p\ge41$, $p\equiv5\pmod6$, $q=p^2$, $e=q-1$, and $N=q-p$.
The elliptic flat coordinate in this note is $z=z_{\rm ell}$, not the
modular deformation coordinate $z_{\rm f}$.  Put

$$
E_0:y^2=x^3-1,\quad dz=dx/(2y),\quad D=d/dz,
\quad C_0=72\beta/\alpha,\quad\alpha^3=4,\quad\beta^2=3,
$$
$$
R=\frac{x^2(x^6+34x^3-8)}{\Delta},\quad
W=\frac{yx^4(x^3+8)}{\Delta},\quad
V=\frac{635x^6-136x^3+176}{12\Delta},
\quad\Delta=x^9-228x^6+48x^3-64.
\tag{712.1}
$$

The constant $B$ and the fixed coefficients $C_k,\mathfrak r_k$ are
exactly R683/R705's.  We concentrate on the exceptional configuration

$$
C_p\not\equiv0\pmod p,\qquad C_{p-3}\equiv0\pmod p.
\tag{712.2}
$$

The certified prime $137147$ satisfies (712.2).  R711 gives
$v_p(M_2)\ge0$ in this configuration, but does not say that $M_2$ is a
unit.  This note identifies a complete second-digit invariant for that
remaining question, retaining every Fourier block to the required
precision.

There is a strict integral CM coordinate $Y$ with

$$
[p](Y)=pY-Y^q.
\tag{712.3}
$$

For this coordinate set

$$
d=q-p+3,\qquad t=2q-4p+2,
$$
$$
F_0=p^3[z^d]\left(\frac{E^3R}{36}
                         +\frac{E^2W}{12}+\frac{EV}{3}\right)
\pmod {p^3},\qquad
R_2=[Y^t]R\pmod p.
\tag{712.4}
$$

Here $E$ is the original odd completed-zeta primitive of R589,
including its actual values at $p$-torsion.  The first expression in
(712.4) is integral, and under (712.2) its class is divisible by $p^2$.
Thus the following class is unambiguously defined:

$$
\boxed{\quad
\mathscr D_p=6\frac{F_0}{p^2}+\frac{B^3}{18}R_2\pmod p.
\quad}
\tag{712.5}
$$

The resulting actual norm congruence is

$$
\boxed{
M_2^2\equiv
-\frac{31104\zeta^2}{\alpha^2}B^2\mathfrak r_p\,
\mathscr D_p\pmod p.
}
\tag{712.6}
$$

All factors preceding $\mathscr D_p$ are units under (712.2).  Hence

$$
v_p(M_2)=0\quad\Longleftrightarrow\quad
\mathscr D_p\ne0\pmod p.
\tag{712.7}
$$

If $\mathscr D_p=0$, R711 gives $v_p(M_2)\ge1$.  No evaluation of
$\mathscr D_{137147}$ is asserted here.  In particular, lifting only
$C_{p-3}$ or its square root does not evaluate (712.5).

## 2. The strict Lubin–Tate coordinate on the original curve

Let $K=\mathbf Q_{p^2}$, containing the original $\mu_6$ and all
$\mu_{p+1}$ character values.  The chosen $\alpha$ belongs to
$\mathbf Z_p$, and $\beta$ belongs to the integers of $K$.  Start with
any integral odd parameter $u$ of $E_0$ having $du(O)=dz(O)$, for
example the chosen formal square root $u=x^{-1/2}$.

The exact reduced endomorphism of $E_0/\mathbf F_p$ is
$[-p]=\operatorname{Frob}_{p^2}$.  This follows from its supersingular
Frobenius polynomial $T^2+p$: $p\equiv2\pmod3$ gives trace zero on
$y^2=x^3-1$, and the equality is an equality of endomorphisms, not just
an equality on points.  Consequently

$$
f_E(u):=[-p](u)=-pu+\cdots,\qquad f_E(u)\equiv u^q\pmod p.
\tag{712.8}
$$

The formal $\mathcal O_K$ action is the continuous extension of the
original CM action.  Thus this is a Lubin–Tate formal module for
$\pi=-p$.  The strict isomorphism to the Lubin–Tate module with
$f_*(Y)=-pY+Y^q$ is integral.  For completeness, its coefficientwise
construction is particularly transparent here.  If $h(u)=u+\cdots$
has been constructed through degree $n-1$, the degree $n$ equation in
$h\circ f_E=f_*\circ h$ has coefficient $(-p)^n-(-p)$ on the one new
unknown.  Its valuation is one.  Modulo $p$ the obstruction vanishes:
over the residue field $\mathbf F_q$, $h(u^q)=h(u)^q$.  Division by
that coefficient therefore gives an integral new coefficient.  This
proves existence and uniqueness at every degree.  The usual uniqueness
argument, applied to two-variable formal group laws, proves that $h$ is
a group isomorphism.  Applying the same argument to endomorphisms
shows that it intertwines the CM action.

For $\xi\in\mu_e$, multiplication $Y\mapsto\xi Y$ commutes with
$f_*$ and has derivative $\xi$.  Hence the transported $[\xi]$ is
literally this multiplication.  The original character labels are
preserved, and (712.3) follows by negating $f_*$.  Every nonzero
$p$-torsion coordinate $\varpi$ now satisfies

$$
\varpi^e=p
\tag{712.9}
$$

exactly.  There is no new ramified field in the coordinate itself, nor
an assumed equality between an arbitrary earlier coordinate and this
one.  The finite sums $S_2,S_3$ and their norm are unchanged.
Both the old parameter and $Y$ are strict integral parameters with the
same exact $\mu_e$ action, so their change has the form
$Y=T(1+c_1T^e+c_2T^{2e}+\cdots)$ with integral $c_i$.  At the original
torsion point the coordinate ratio is therefore $1+O(p)$.  In
particular the R605 leading residue of $S_2/T^{p-1}$ transfers to
$S_2/\varpi^{p-1}$ without a normalization factor modulo $p$.

As a primary reference for this precise polynomial model in the
supersingular CM case, Bannai–Kobayashi, *Integral structures on
$p$-adic Fourier theory*, §5, use
$[\pi](T)=\pi T+T^{p^2}$ and the isomorphism of the elliptic formal
group with it.  The coefficient argument above supplies the strict
normalization used here.
https://www.numdam.org/article/AIF_2016__66_2_521_0.pdf

## 3. The logarithm and its full relevant precision

Write the logarithm of (712.3) as

$$
\ell(Y)=Y+\ell_1Y^q+\ell_2Y^{2q-1}+\cdots.
$$

Its support is $1\pmod e$ by the exact $\mu_e$ action.  Comparing
coefficients in $\ell(pY-Y^q)=p\ell(Y)$ gives

$$
\ell_1=-\frac1{p(1-p^e)},\qquad
\ell_2=-\frac{\ell_1q p^{q-1}}{p-p^{2q-1}},\qquad
v_p(\ell_2)=q-1.
\tag{712.10}
$$

In particular $z=\ell(Y)$ agrees with $Y$ in every degree below $q$.
For $\rho=dz/dY$, in the entire range of degrees through $2e$,

$$
\rho=1-pY^e\pmod {p^4}.
\tag{712.11}
$$

Indeed the error of the first displayed coefficient has valuation
$q$, and the coefficient of $Y^{2e}$ has valuation $q-1$.  These are
much larger than four.  Terms of degree $3e$ or higher cannot affect
the three Fourier coefficients below, even after three derivatives.
This is why the polynomial model can be used at this precision; the
complete logarithm is not replaced by its first two terms everywhere.

## 4. The full antiderivative of the actual third kernel

Use R705's rational connection coefficients

$$
L_j=[v^j]e^{-E(P)v}H^-(P,v).
$$

They include the full inverse-sigma factor in the original completed
Kronecker function.  R605's exact full second-kernel identity, with the
constant determined from the actual tame sum, gives

$$
L_0=C_0R,\qquad L_1=C_0W,\qquad
L_2=C_0(2V+17/36).
\tag{712.12}
$$

The corresponding exact third antiderivative is

$$
\mathcal U_3=\frac1{3!}\sum_{a=0}^3\frac{E^a}{a!}L_{3-a},
\qquad H_3=D^3\mathcal U_3,
$$
$$
\frac{\mathcal U_3}{C_0}
=\frac{E^3R}{36}+\frac{E^2W}{12}+\frac{EV}{3}
 +\frac{17E}{216}+\frac{L_3}{6C_0}.
\tag{712.13}
$$

The constant $17/36$ must not be lost by integrating the R605 identity.
Here is an exact check with all eighteen labels.  For $r^3=4$ and the
representatives with $\delta=1,j=0$, write

$$
x_Q=r^2+r+2,\quad y_Q=\beta(-r^2-2r-3),\quad
e_Q=\beta(r^2+2r+2)/6,\quad\chi_6(Q)^{-1}=r/\alpha.
$$

Negation and the simultaneous threefold rotation supply a factor six.
The ordinary numerator Bell coefficient is
$(e_Q^3-3e_Qx_Q-2y_Q)/6$, so direct reduction modulo $r^3-4$ gives

$$
\frac{[v^2]H^-(0,v)}{C_0}
=\frac1{72}\operatorname{Tr}_{\mathbf Q[r]/\mathbf Q}
\left[r(3e^3-3ex-2y_0)\right]=-\frac1{36},
$$

where $e=(r^2+2r+2)/6$ and $y_0=-r^2-2r-3$.
The $zv$ coefficient of $H^-/C_0$ is zero by the same trace (equivalently
by $L_1=C_0W$ and $W=-z+\cdots$).  Since $E=z^{-1}+\cdots$ and
$H_0/C_0=z^2+\cdots$, the constant of $L_2/C_0$ is
$-1/36+1/2=17/36$.  R605 fixes the rest: the difference of two rational
second antiderivatives is constant; the possible $E$ coefficient is
constant and odd and hence zero.  This proves (712.12) with its exact
constant, rather than setting that integration constant to zero.

All rational connection coefficients here are $p$-integral in $Y$.
The inverse-sigma expansion has its first positive correction in degree
six; no such correction is missing in degrees at most three.  The
last term of (712.13) is nevertheless retained until its integrality
has been used below.  The regularity of the complete Kronecker sum at
$(P,v)=(O,0)$ makes $\mathcal U_3$ regular at $O$, though individual
terms of (712.13) can have poles.

For $j=0,1,2$ put

$$
n_j=N+je,\quad r_j=n_j+3,\quad
u_j=[Y^{r_j}]\mathcal U_3/C_0,\quad F_j=p^3u_j.
\tag{712.14}
$$

All $F_j$ are integral.  To see this without an unproved coefficient
estimate, use the original primitive bound
$v_p(e_k)\ge-v_p(k)$ and $k\equiv5\pmod6$.  A positive primitive
index divisible by $p^2$ is at least $5q$.  At these three coefficient
indices the entire primitive degree budget is below $3q$, and at most
three primitive factors occur.  Hence the coefficient loses at most
three powers of $p$.

Since $r_0=q-p+3<q$, $u_0$ is exactly the flat $z$ coefficient of the
complete regular expression (712.13).  The $L_3$ term has an integral
flat coefficient in this degree: its pole has order at most one and
the first coordinate correction has degree $q$, so a possible correction
only starts in degree $q-2>r_0$.  The primitive coefficient $[z^{r_0}]E$
is also integral, because $r_0\equiv3\pmod p$ and the same coordinate
cutoff applies.  Thus both the $L_3$ term and the exact extra $17E/216$
term contribute zero to $F_0\pmod{p^3}$.
This proves exactly (712.4); discarding $L_3$ before this check would
not have been justified.

Finally, Cartier for the original primitive gives
$pE\equiv-BY^p$ throughout the relevant positive degree range below
$5q$.  In $F_1$ only the highest $E^3$ term survives modulo $p$.
Therefore

$$
F_1\equiv-\frac{B^3}{36}[Y^{2q-4p+2}]R
=-\frac{B^3}{36}R_2\pmod p.
\tag{712.15}
$$

## 5. Three Fourier blocks suffice, and the third actually vanishes

Define the unramified scalar

$$
\mathcal G_3=\frac{p^3S_3}{C_0\varpi^N}.
\tag{712.16}
$$

Exact character orthogonality and (712.9) give

$$
\mathcal G_3=-e\sum_{j\ge0}p^{3+j}
[Y^{n_j}]H_3/C_0.
\tag{712.17}
$$

The complete R705 tail estimate is

$$
v_p([Y^n]H_3)\ge
-3-\left\lfloor\frac{n+4}{5q}\right\rfloor.
$$

Because $n_j+4<(j+1)q$, a term of (712.17) with $j\ge3$ has valuation
at least

$$
j-\left\lfloor\frac{j+1}{5}\right\rfloor\ge3.
\tag{712.18}
$$

This proves that the entire infinite tail, not just a chosen sample,
vanishes modulo $p^3$.

We now keep the full differentiation in the remaining three blocks.
For $g=\rho^{-1}$,

$$
D^3=g^3\partial_Y^3+3g^2g'\partial_Y^2
       +g((g')^2+gg'')\partial_Y.
\tag{712.19}
$$

Using (712.11), the coefficient of the shift by $e$ is $pQ_1(r)$,
and that of the shift by $2e$ is $p^2Q_2(r)$, where

$$
Q_1(r)=3r(r-1)(r-2)+3er(r-1)+e(e-1)r,
$$
$$
Q_2(r)=6r(r-1)(r-2)+12er(r-1)+(7e^2-4e)r.
\tag{712.20}
$$

Put $A_j=(n_j+1)(n_j+2)(n_j+3)$.  Then $A_0$ is a unit, while
$v_p(A_1)=v_p(A_2)=1$.  Substitution in (712.17) yields

$$
\boxed{
\mathcal G_3\equiv-e\left\{
A_0F_0+p^2\left(\frac{A_1}{p}F_1+Q_1(r_0)F_0\right)
\right\}\pmod {p^3}.
}
\tag{712.21}
$$

Here are the precise discarded valuations.  The direct $j=2$ term is
$p^2A_2F_2$, divisible by $p^3$.  Its one-shift correction is
$p^3Q_1(r_1)F_1$, and its two-shift correction is
$p^4Q_2(r_0)F_0$.  Both vanish.  Thus no coefficient of $\mathcal U_3$
at the third large index is needed at all.  The errors in (712.11)
have at least four additional powers of $p$ before the allowed
three-power primitive loss and therefore also vanish after the
scaling in (712.17).

Formula (712.21) is a two-block formula with all derivative corrections
accounted for.  It is not obtained by treating $Y$ as a globally flat
coordinate.

## 6. The square and the exceptional second digit

Under (712.2), R605 and R683 give

$$
A:=\frac{S_2}{\varpi^{p-1}}\in\mathcal O_K^\times,
\qquad A\equiv-\frac{C_0B^2\mathfrak r_p}{4}\pmod p.
\tag{712.22}
$$

The exact product, using $N+(p-1)=e$ and (712.9), is

$$
S_2S_3=C_0 A\frac{\mathcal G_3}{p^2}.
\tag{712.23}
$$

The actual norm and reflection are the unchanged R588 identities

$$
M_2\overline{M_2}=
\frac{8N_\theta}{(p+1)^2}S_2S_3,
\qquad\overline{M_2}=-\zeta M_2,
\quad N_\theta\equiv-1\pmod p.
\tag{712.24}
$$

Consequently

$$
v_p(M_2^2)=v_p(\mathcal G_3)-2.
\tag{712.25}
$$

R711 and (712.2) show $v_p(M_2)\ge0$, so
$\mathcal G_3\in p^2\mathcal O_K$.  Equation (712.21), with its unit
$A_0$, now proves

$$
F_0\in p^2\mathcal O_K\pmod {p^3}.
\tag{712.26}
$$

The last correction $p^2Q_1(r_0)F_0$ in (712.21) therefore vanishes.
Finally

$$
-e\equiv1,\qquad A_0\equiv6,\qquad A_1/p\equiv-2\pmod p,
$$

so (712.15) gives

$$
\frac{\mathcal G_3}{p^2}
\equiv6F_0/p^2-2F_1
=6F_0/p^2+\frac{B^3}{18}R_2
=\mathscr D_p\pmod p.
\tag{712.27}
$$

Combining (712.22)--(712.24), using $C_0^2=15552/\alpha^2$, proves
(712.6).  This proof fixes its sign and its complete scalar; it does
not replace the norm by a claim that complex conjugation fixes the
chosen $p$-adic embedding.

## 7. Exact finite certificate and the remaining computational problem

A certificate for an evaluation of (712.5) must contain:

1. The original prime, $B$, the chosen cube-root embedding, and the
   certified nonzero $C_p$ and zero $C_{p-3}$ residues.
2. The coefficient $F_0\pmod {p^3}$ of the complete polynomial in
   $E,R,W,V$ in (712.4), with the tested divisibility by $p^2$.
3. The coefficient $R_2\pmod p$ in the strict coordinate (712.3), or a
   proved coordinate comparison that computes exactly this coefficient.
4. The residue $\mathscr D_p$ and the scalar in (712.6).

Only the first block needs three-digit precision.  The second block
needs one digit, and all other blocks have already been removed by
proof.  The last connection term $L_3$ and all the discarded tails
have exact reasons to disappear; they are not neglected numerically.

This is a finite coefficient specification, but a direct expansion to
$q-p+3$ or $2q-4p+2$ still has quadratic length in $p$.  It is not an
appropriate implementation at $p=137147$.  The present note does not
submit such an expansion to a runner.

The highest primitive terms in the two blocks have fixed-family weight
indices $p-3$ and $2p-2$, respectively, since

$$
n_j+3-3p=(p-1)\bigl(p-3+j(p+1)\bigr).
\tag{712.28}
$$

This explains a possible route to a computation of length proportional
to $p$, but (712.28) is an index identity only.  R683 proves its
Cartier comparison modulo $p$ in the range $k\le p$; it supplies
neither a three-digit comparison in the first block nor the divided
factorial comparison at $k=2p-2$.  Those missing comparisons must be
proved before using the small-degree sigma recurrence to evaluate
$\mathscr D_p$.

In particular, $A_{p-3}\equiv0\pmod p$ and the rational square
formula for $C_{p-3}$ do not prove $v_p(M_2)=0$.  Even a nonzero
$A_{p-3}/p\pmod p$ would not by itself evaluate the second term in
(712.5) or all the first-block corrections.

For $137147$, if a valid computation eventually gives
$\mathscr D_p\ne0$, R711's exact Weierstrass quadratic is Eisenstein:
its two possible nonzero scalar Abel zeros have $v_p(a-1)=7/2$ and
cannot be rational $p$-adic candidates, which satisfy
$v_p(a-1)\ge4$.  Until that evaluation or another argument is supplied,
this remains conditional.  It is also a scalar Abel statement, not a
replacement for the actual quadratic-height jet.

## Public exact-algebra record

The small finite trace and total-derivation identities in this proof were
verified by this public repository's own
[Actions run 43594244072](https://github.com/Rogerhu12/math-research-public/actions/runs/43594244072),
from source commit `6ab42353295419f5f3f2028c388d3cd745df4f86`.
The full [input, output, source snapshots and manifest](../computations/R712-exact-small-algebra/43594244072-1/)
retain twelve hashed files. The exact arithmetic source SHA256 is
`f9b9c1e401831e025122757ac3ebd4317362bcf462745f273e4bbaba377bc70b`;
the certificate SHA256 is
`2832fa12ba8a8252749bc12db958c1468a857d830041da011fc7405ebcdf6ce5`.
The certificate checks the complete eighteen-label constant $17/36$,
the three total-derivative shifts, and their displayed residue factors.
It does not evaluate $F_0$, $R_2$, $M_2$, or $\mathscr D_{137147}$,
and does not replace the infinite-tail proof above by a finite test.
