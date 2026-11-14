# R705 — Actual higher Abel blocks and a uniform order bound

## 1. Statement, with the original markings and two coordinates distinguished

Let $p\ge41$ be prime with $p\equiv5\pmod6$.  Keep the specified
$\theta=\theta_{-1}$, the actual $c_1$ tame vector, the Cartan average,
and the absolute Hodge normalization of R575/R588/R592.  Put

$$
q=p^2,\quad e=q-1,\quad
E_0:y^2=x^3-1,\quad dz_{\rm ell}=dx/(2y),\quad D=d/dz_{\rm ell},
$$
$$
C_0=72\beta/\alpha,\quad \alpha^3=4,\quad\beta^2=3,\quad
B=(-1)^{(p-1)/2-(p-2)/3}\binom{(p-1)/2}{(p-2)/3},
\quad c=(3/p)\alpha^2/2.
\tag{705.1}
$$

The elliptic coordinate $z_{\rm ell}$ in the finite kernels is not the
flat modular deformation coordinate $z_{\rm f}$ of R592.  Their exact
comparison is through the actual toric norm and flat jets $M_m$ of
R588, not an identification of the two coordinates.

For $2\le k\le p$, $k\equiv2\pmod3$, write

$$
\mathfrak r_k=[z_{\rm ell}^{(p-1)k}]R_-,\qquad
R_-=\frac{x^2(x^6+34x^3-8)}{x^9-228x^6+48x^3-64}.
\tag{705.2}
$$

Thus R605's old $r_2,r_3$ are respectively $\mathfrak r_p$ and
$\mathfrak r_{p-3}$; $\mathfrak r_2$ below has a different index.

For every $m$ with $2\le m\le p-3$ and $m\equiv2\pmod3$, the
original $c_1$ flat Hodge jet satisfies

$$
\boxed{
v_p(M_m)\ge1-m,\qquad
(p^{m-1}M_m)^2\equiv
\frac{864\zeta^2}{\alpha^2}(m-2)!(m+1)!B^{2m+1}
\mathfrak r_{p+2-m}\mathfrak r_{p-m-1}\pmod p.
}
\tag{705.3}
$$

Every scalar preceding the two coefficients is a unit.  In particular

$$
v_p(M_m)=1-m
\quad\Longleftrightarrow\quad
C_{p+2-m}C_{p-m-1}\not\equiv0\pmod p,
\tag{705.4}
$$

using the full six-torsion Cartier comparison of R683.  A zero residue
only gives the safe improvement $v_p(M_m)\ge3/2-m$.

At the actual endpoint $m=p-3$, the two fixed weights are $5$ and $2$.
Their exact values $C_5=9/2$ and $C_2=-1/2$ give

$$
\boxed{(p^{p-4}M_{p-3})^2\equiv
-\frac{\zeta^2\alpha^2}{12B^8}\pmod p,\qquad
v_p(M_{p-3})=4-p.}
\tag{705.5}
$$

Consequently, if $d$ is the common first nonzero order of the original
Abel formal logarithm in $s=a-1$ as in R682, then

$$
\boxed{1\le d\le(p-2)/3.}
\tag{705.6}
$$

This bounds the order; it does not identify the first nonzero index,
prove $d=1$, or bound the valuation of the first nonzero height jet.
Section 8 gives the additional precise prefix valuations on the actual
scaled coordinate $w=s/\lambda^3$.

## 2. The actual norm identity at every permitted higher jet

For the same actual $\chi_6$ and six-torsion labels, define

$$
H^-(P,v)=\sum_Q\chi_6(Q)^{-1}\Theta_Q(P,v),\qquad
H_r(P)=[u^rv^r]H^-(P+u,v).
\tag{705.7}
$$

The completed Kronecker function and all periods are those of R588 and
R658.  In particular the full inverse-sigma factor is retained at large
$r$.  Define the original finite sums

$$
S_m=-\sum_b\theta(b)H_m(P_b),\qquad
S_{m+1}=-\sum_b\theta(b)^{-1}H_{m+1}(P_b).
\tag{705.8}
$$

The R588 calculation extends to all $m\ge2$, $m\equiv2\pmod3$, with
the same finite vector and measures:

$$
M_m\overline{M_m}
=\frac{[m!(m+1)!]^2N_\theta}{18(p+1)^2}S_mS_{m+1},
\qquad \overline{M_m}=-\zeta M_m,\qquad N_\theta\equiv-1\pmod p.
\tag{705.9}
$$

Here are the checks needed for this extension, rather than an assumption
that the statement formerly printed only for $m=2$ already includes it.
The Hecke factors are exactly

$$
\xi_{2m+1}((a))=a^{2m+1}\chi_6(a)\theta(a)^{-1},\qquad
\xi_{2m+3}((a))=a^{2m+3}\chi_6(a)\theta(a).
\tag{705.10}
$$

On $\zeta$ both unit conditions reduce to $\zeta^{2m+2}=1$, and on
$-1$ they hold because $\chi_6(-1)=-1$.  Thus increasing $m$ by three
changes neither finite conductor nor the finite unit characters that
select the actual local vectors.  This does not assert that the full
unramified parts of the changing Hecke characters are fixed.
The factors at $2,3,p$ in R588 §§5--6 remain respectively
$2/3$, $1/(3\sqrt3)$, and $N_\theta/(p+1)^2$; the correct $C_3$
projection at $3$ is unchanged because the raised weight changes by six.
The value on a ramified uniformizer at $3$ may change, but its entire
odd-valuation coset has zero matrix coefficient by the support argument
of R588 §5.4.  At $2,p$ the unramified torus modulo the rational center
is represented by units.  At the other finite places the spherical
factor cancels the local $L$ factor for the new character, as in R588.
Hsieh's Proposition 3.3 has, for every $m\ge0$, the archimedean factor
$8m!(m+1)!/(4\pi)^{2m+3}$ at weight two.  Proposition 2.1 is the
characteristic-zero Waldspurger identity; no ordinary-prime interpolation
is used.  The CRT grouping and the exact flat-coordinate calculation in
R588 (588R.14)--(588R.34) are formulas with this general $m$, so their
factorial and period cancellations give the first identity in (705.9).

Finally the same transported reflection sends the tame vector to
$-\zeta$ times itself.  The Maass operator commutes with the Fourier
conjugation used there, and $(2\pi i/\Omega)^{2m+2}$ is real for every
$m$.  Hence R588 §8 gives the displayed conjugation identity for every
allowed $m$, not an assertion about conjugation fixing a $p$-adic place.

Primary source rechecked: M.-L. Hsieh, *Special values of anticyclotomic
Rankin--Selberg L-functions*, Propositions 2.1 and 3.3,
https://www.math.ntu.edu.tw/~mlhsieh/research/VBDP.pdf.

## 3. Full kernels, their integral rational coefficients, and pole budgets

Let $E=\zeta_\Lambda$ be the original completed formal primitive and set

$$
L_j^-(P)=[v^j]e^{-E(P)v}H^-(P,v),\qquad
\mathcal U_r=\frac1{r!}\sum_{a=0}^{r}\frac{E^a}{a!}L_{r-a}^-.
\tag{705.11}
$$

Then

$$
H_r=D^r\mathcal U_r,\qquad L_0^-=C_0R_-,\qquad
[E^r]\mathcal U_r=\frac{C_0R_-}{(r!)^2},\qquad
[E^r]H_r=\frac{C_0D^rR_-}{(r!)^2}.
\tag{705.12}
$$

These formulas include every inverse-sigma block; for $r\ge5$ it would
be incorrect to use only the uncorrected numerator Bell polynomial.

For $0\le j\le p-2$, the functions $L_j^-$ have integral rational
Laurent expansions in the actual integral CM parameter $Y$.  The proof
is R658 §2 with $\chi$ replaced by $\chi^{-1}$: all factorials have
index at most $j+1\le p-1$, and every required inverse-sigma coefficient
is integral in that range.  The prime-to-$p$ torsion points remain
distinct from $O$.  No endpoint $p!$ division occurs anywhere in this
argument, including $r=m+1=p-2$.

The bivariate function $H^-$ is regular at $(0,0)$, since the $v^{-1}$
term cancels.  Under $\epsilon\in\mu_6$ it transforms as
$H^-(\epsilon z,\epsilon v)=\epsilon^2H^-(z,v)$: the character on
$\epsilon Q$ contributes $\epsilon^{-3}$ and the theta function
contributes $\epsilon^{-1}$.  Its total degree is therefore at least
two.  It follows that

$$
\operatorname{ord}_O L_j^-\ge2-j.
\tag{705.13}
$$

Consequently the coefficient of $E^a$ in $\mathcal U_r$ has order at
least $a+2-r$, and that in $H_r$ has order at least $a+2-2r$.
Differentiation preserves integrality of those rational coefficients;
$DE=-x$ has pole order two.  This proves these order bounds by induction
through all $r$ differentiations.

Use the actual R595 primitive expansion

$$
E(Y)=Y^{-1}+\sum_{k\ge1,\ k\equiv5\ (6)}e_kY^k,
\qquad v_p(e_k)\ge-v_p(k).
\tag{705.14}
$$

For such a positive index $k$,

$$
v_p(k)\le1+\frac{k+1}{5p^2}.
\tag{705.15}
$$

Indeed the assertion is immediate for valuations zero or one.  If the
valuation is two, $p^2\equiv1\pmod6$ forces $k\ge5p^2$.  If it is
$a\ge3$, use $k\ge p^a$ and $p^{a-2}\ge5(a-1)$ for $p\ge41$.

In a term of $E^a$ times one of the rational coefficients of $H_r$,
replacing a polar factor $Y^{-1}$ by a positive primitive term of
degree $k$ costs $k+1$ degrees.  At coefficient index $n$ the total
available budget is at most $n+2r-2$.  There are at most $r$ factors.
Summing (705.15) therefore proves the complete bound

$$
\boxed{v_p([Y^n]H_r)\ge
-r-\left\lfloor\frac{n+2r-2}{5p^2}\right\rfloor
\quad(n\ge0,\ 1\le r\le p-2).}
\tag{705.16}
$$

For $\mathcal U_r$, the same argument has budget $n+r-2$ instead.
These bounds control the entire infinite tails.  In particular they
do not charge a second $p$ to all primitive factors as soon as a single
large index is possible.

## 4. The first Fourier sum: complete block analysis

Let $\varpi=Y(P)$ for the chosen nonzero $p$-torsion point.  R595 gives

$$
v_p(\varpi)=1/e,\quad \varpi^e/p\equiv1\pmod p,
\quad\rho=\omega/dY=1+a_1Y^e+a_2Y^{2e}+\cdots,
\quad v_p(a_1)\ge1,\quad a_j\in\mathcal O.
\tag{705.17}
$$

The complete character sum selects $n_j=p-1+je$, so
$S_m=-e\sum_{j\ge0}[Y^{n_j}]H_m\,\varpi^{n_j}$.
For now suppose $m\ge5$.  We prove

$$
\boxed{\frac{p^{m-2}S_m}{\varpi^{p-1}}
\equiv
eC_0\frac{(m-2)!(-B)^m}{(m!)^2}
\mathfrak r_{p+2-m}\pmod p.}
\tag{705.18}
$$

### Block $j=0$

The needed coefficient of $\mathcal U_m$ has index $p+m-1$.  Its
primitive budget is $p+2m-3\le3p-9<3(p+1)$, so at most two primitive
factors can have a $p$-denominator.  No such index can have two
$p$-denominators.  Thus its valuation is at least $-2$.
The derivation $D^m$ agrees with $\partial_Y^m$ at this index because
the first correction has degree shift $e$.  The ordinary derivative
factor is $p(p+1)\cdots(p+m-1)$ and has valuation one.  Hence
$v_p([Y^{p-1}]H_m)\ge-1$.  After multiplication by $p^{m-2}$ this
block vanishes modulo $p$.

### Block $j=1$

Write $n_1=e+p-1=q+p-2$.  The coefficient of
$\partial_Y^m\mathcal U_m$ is

$$
(n_1+m)_{\underline m}[Y^{n_1+m}]\mathcal U_m,
\qquad
\frac{(n_1+m)_{\underline m}}p\equiv-(m-2)!\pmod p.
\tag{705.19}
$$

The unique $p$-divisible factor is $q+p=p(p+1)$.  To check the actual
coordinate, expanding $D^m=(\rho^{-1}\partial_Y)^m$ shows that a
correction of total degree shift $\ell e$ uses a coefficient of
$\mathcal U_m$ at index $n_1+m-\ell e$.  Only $\ell=1$ can occur,
and its coefficient is divisible by $p$.  Its remaining index is
$p+m-1$, whose valuation is at least $-2$ as above.  Thus this whole
correction disappears after multiplication by $p^{m-1}$.

The maximum positive primitive index in the remaining coefficient is
at most $q+p+2m-4<2q$.  The original R595/R605 Cartier identity
$pE\equiv-BY^p$ is valid throughout this range; there is no index
with a $p^2$ denominator.  More explicitly, $dE=-x\omega$ and
$\mathcal C(x\omega)=B\omega$ identify the coefficient at index
$\ell p-1$ of $x\rho$ modulo $p$ with $B$ times the $p$th power
of the coefficient at index $\ell-1$ of $\rho$.  In the present
range $\ell<2p$, whereas $\rho=1+\sum a_jY^{je}$ has no positive
index below $e=p^2-1$.  Thus among indices divisible by $p$ below
$2q$, only the primitive coefficient at $Y^p$ survives after
multiplication by $p$; its value is $-B$.  A primitive index with
two $p$ factors is at least $5q$ by its congruence $5\pmod6$.
This proves the stated truncated Cartier identity at the exact
precision used here.  By (705.12), only the highest $E^m$ term
survives after multiplying $\mathcal U_m$ by $p^m$.  Therefore

$$
\frac{p^{m-1}}{C_0}[Y^{n_1}]H_m
\equiv-\frac{(m-2)!(-B)^m}{(m!)^2}
[Y^{(p-1)(p+2-m)}]R_-.
\tag{705.20}
$$

This last index is less than $q$, so R595's $Y=z_{\rm ell}+O(z_{\rm ell}^q)$
comparison identifies it with $\mathfrak r_{p+2-m}$.

### Block $j=2$

For $n_2=2e+p-1$, the uncorrected ordinary derivative again contributes
one factor $p$, now from $2q+p$, since $m\ge3$.  Every primitive index
in $\mathcal U_m$ is below $3q<5q$, so its coefficient has valuation
at least $-m$.  The correction with degree shift $e$ has an additional
$p$ from $a_1$.  The correction with shift $2e$ has integral coefficient
and uses the low coefficient of valuation at least $-2$.
Thus every contribution has valuation at least $1-m$.  After its
torsion factor $\varpi^{2e}$ and the scaling $p^{m-2}$, this block
has positive valuation.

### All blocks $j\ge3$

Since $n_j+2m-2<(j+1)q$, (705.16) gives
$v_p([Y^{n_j}]H_m)\ge-m-\lfloor j/5\rfloor$.
The valuation of the scaled block is at least

$$
j-2-\lfloor j/5\rfloor\ge1\qquad(j\ge3),
\tag{705.21}
$$

and tends to infinity.  This proves the full tail assertion.  Combining
the sole surviving block (705.20) with $\varpi^e/p\equiv1$ proves
(705.18), including its sign.  For $m=2$, (705.18) is exactly the
already proved R601/R605 identity, whose two exceptional blocks were
handled there; no new claim about those blocks is needed.

## 5. The second Fourier sum and its complete tail

Put $r=m+1\le p-2$ and $N_p=p(p-1)$ (this $N_p$ is unrelated to
R698's index).  The character selects $N_p+je$.  We prove

$$
\boxed{\frac{p^{m+1}S_{m+1}}{\varpi^{N_p}}
\equiv-eC_0\frac{(-B)^{m+1}}{(m+1)!}
\mathfrak r_{p-m-1}\pmod p.}
\tag{705.22}
$$

In the first block, all needed positive primitive indices are below
$N_p+2r-2<2q$.  Multiplication by $p^r$ leaves only
$(-B)^rY^{pr}C_0D^rR_-/(r!)^2$.
The required coefficient of $R_-$ has index

$$
n_*=(p-1)(p-r),\qquad
n_*\equiv r\pmod p,\qquad
(n_*)_{\underline r}\equiv r!\pmod p.
\tag{705.23}
$$

It lies below $q$.  The $\rho$ correction cannot enter the required
degree of $D^rR_-$, and the same strict parameter comparison applies.
This proves the displayed leading residue.

For every $j\ge1$, (705.16) and
$N_p+je+2r-2<(j+2)q$ bound the scaled block's valuation below by

$$
j-\lfloor(j+1)/5\rfloor\ge1.
\tag{705.24}
$$

This tends to infinity, proving the entire discarded tail and hence
(705.22).

## 6. Multiplying the actual blocks, and the endpoint constant

Since $(p-1)+N_p=e$, multiplying (705.18) and (705.22), then using
$\varpi^e/p\equiv1$, gives

$$
p^{2m-2}S_mS_{m+1}\equiv
C_0^2\frac{(m-2)!B^{2m+1}}{(m!)^2(m+1)!}
\mathfrak r_{p+2-m}\mathfrak r_{p-m-1}\pmod p.
\tag{705.25}
$$

Here $e^2\equiv1$ and the two signs cancel.  Combining (705.25) with
(705.9), $C_0^2=15552/\alpha^2$, and
$M_m^2=-\zeta^2M_m\overline{M_m}$ proves (705.3).  At $m=2$ it
recovers exactly R605's coefficient $5184\zeta^2B^5\alpha^{-2}$.

Both indices in (705.3) lie in the proved R683 range $2\le k\le p$;
all factorials $m!,(m+1)!$ remain $p$-units even at the endpoint.
R683 gives

$$
\mathfrak r_k=c(-3B)^{-(k-1)}C_k.
\tag{705.26}
$$

At $m=p-3$ this is

$$
\mathfrak r_5=\frac{c}{18B^4},\qquad
\mathfrak r_2=\frac{c}{6B}.
\tag{705.27}
$$

Wilson's theorem gives $(p-5)!=-1/24$ and $(p-2)!=1$ modulo $p$.
In (705.3), $B^{2p-5}=B^{-3}$ and $c^2=\alpha^4/4$.  Substitution
therefore gives

$$
\frac{864\zeta^2}{\alpha^2}\left(-\frac1{24}\right)
B^{-3}\frac{c^2}{108B^5}
=-\frac{\zeta^2\alpha^2}{12B^8},
$$

proving (705.5).  No high-weight value or modulo-$p$ unit conjecture
is used at this endpoint.

## 7. The precise original Abel-map consequence

The actual $c_1$ primitive in R592 is

$$
\mathcal I(z_{\rm f})
=\sum_{j\ge1}\frac{M_{3j-1}}{(3j)!}z_{\rm f}^{3j},\qquad
z_{\rm f}^3=\frac38(a-1)+O((a-1)^2).
\tag{705.28}
$$

The coefficient at $j_*=(p-2)/3$ is nonzero by (705.5).  Therefore
the first nonzero order of this primitive in $z_{\rm f}^3$, and hence
in $a-1$, is at most $j_*$.  A later nonzero coefficient is used only
to bound the first order, not to identify that first coefficient.

To connect this scalar primitive to the actual quotient, R575
(575.13), (575.24)--(575.25) identifies the same projected tame line
with $A_{\theta,1}$, not the opposite cubic family.  If
$\omega_\sigma$ is a corresponding invariant quotient differential,
then the pullback $q_1^*\omega_\sigma$ is a nonzero constant multiple
of the Kodaira--Spencer differential of this Hodge section.  The
constant is retained and is not called a $p$-unit.

The constancy of this comparison along the disc can be checked directly:
R592 gives $\mathcal F_{\rm flat}=u_1^2\mathcal F_t$ and
$dz_{\rm f}=b\,dt/u_1^2$, so
$\mathcal F_{\rm flat}dz_{\rm f}=b\mathcal F_tdt$.
Kodaira--Spencer sends $\omega^{\otimes2}$ to a fixed nonzero
cup-product normalization times $b\,dt$.  Thus no additional varying
factor changes the vanishing order.  Taking a primitive at $c_1$
is the corresponding linear functional of
$\log(q_1[x-c_0])-\log(q_1[c_1-c_0])$.

It follows that the original Abel vector has a nonzero coefficient
of order at most $j_*$.  R682's common-order statement, for this same
quotient and parameter, proves (705.6).  This step needs no rank-one
Mordell--Weil generator to compute the scalar, and it makes no claim
about the quotient's integral cotangent lattice.

The unnormalized scalar Abel order bound itself does not require the
Mordell--Weil rank or the nontorsion of a chosen base-point image.  If it
is inserted into R682's normalized $t_i$, their squared differences, or
the resulting height exterior products, retain that result's R616
hypothesis $L'(g_{-1,+},1)L(g_{-1,-},1)\ne0$.  The present argument
does not remove that hypothesis or supply the height's first jet.

## 8. Concrete prefix valuations on the actual scaled coarse disc

Let $\lambda$ be exactly R592's full-level scale, with
$v_p(\lambda)=\sigma=p/(p+1)$, and put

$$
w=(a-1)/\lambda^3,\qquad
U=z_{\rm f}^3/\lambda^3=\Phi(w),\qquad
\Phi(w)\in w\mathcal O[[w]],\quad \Phi'(0)=3/8.
\tag{705.29}
$$

The integral change follows from R592's integral fine change
$z_{\rm f}/\lambda$ in $t/\lambda$, its $\mu_3$ symmetry, and the
exact algebraic $j$ relation.  Hence its cube descends to an integral
change in $w$, with the displayed unit linear coefficient.

Before this last change the coefficient of $U^j$ in the raw primitive
is $D_j=\lambda^{3j}M_{3j-1}/(3j)!$.  For $1\le j\le j_*$, all
factorials have index $3j\le p-2$, and (705.3)--(705.5) give

$$
v_p(D_j)\ge2-\frac{3j}{p+1},\qquad
v_p(D_{j_*})=\frac{p+4}{p+1}.
\tag{705.30}
$$

Writing $\mathcal I=\sum d_jw^j$, integrality of $\Phi$ implies the
same lower bounds for $d_j$ through $j_*$.  At the endpoint, all
contributions from $D_i$, $i<j_*$, have strictly higher valuation
than $D_{j_*}$, whereas its own contribution is multiplied by
$(3/8)^{j_*}$, a unit.  Thus

$$
\boxed{v_p(d_j)\ge2-\frac{3j}{p+1}\ (j\le j_*),\qquad
v_p(d_{j_*})=\frac{p+4}{p+1}.}
\tag{705.31}
$$

Multiplication by the actual nonzero differential comparison scalar
adds its valuation to every bound in (705.31).  It does not disappear.

These are complete, explicit assertions about the finite prefix.
They do not make $d_{j_*}$ the first nonzero coefficient.  Nor do they
make it dominate every later coefficient: R592 alone gives the full
tail estimate $v_p(D_j)\ge\sigma-v_p(3j)$, which does not imply that
all later terms have larger valuation than (705.30).  In particular
the height function $\mathscr E$ of R699 also contains its actual
height-normalization constants and the linear term $\ell_h$; the
Abel endpoint unit does not remove them or determine its first jet.

## 9. Relation to the original exception and to R702

At $p=137147$, the independently confirmed $C_{p-3}=0\pmod p$
prevents the $m=2$ minimum valuation and also prevents the $m=5$
minimum in (705.4).  It does not make either jet zero in characteristic
zero.  The endpoint (705.5) still holds, so this exception does not
make the Abel germ formally constant.

The weights $p+3,p+6$ of R702 would correspond here to negative $m$;
they are not later Abel terms.  The usable later mapping is the
decreasing pair $p+2-m,p-m-1$ established by the original Fourier
blocks above.  The higher-jet and order-bound theorem therefore does
not depend on an unjustified inverse use of the R702 shift.
