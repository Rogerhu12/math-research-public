# R730 — A fixed-depth original Abel isometry from the norm over all embeddings

Date: 2026-11-14. **Status: proved.** For every sufficiently large
prime $p\equiv2,5\pmod9$, at least one actual primitive coefficient
embedding of the original positive CM quotient has a normalized
Abel increment that is an isometry on the fixed closed disc
$v_p(a-1)\ge9$. Neither $C_p$ nor an individually prescribed
$M_{2,h}$ is assumed to be a unit.

The embedding may depend on $p$. The argument proves its existence
inside the original primitive factor, not inside an auxiliary twist.
It improves R729's depth proportional to the coefficient-field degree.
It still does not cover the entire original depth-four candidate disc
and does not assert a canonical-height equation.

## 1. The precise statements

Fix the original curve, tame marking, finite torus, and positive
quotient of R575/R588. Put

$$
n=p+1,\qquad F_0=\mathbb Q(\zeta_n)^+,\qquad
g_0=[F_0:\mathbb Q]=\varphi(n)/2,
$$
$$
\mathcal H^*=\{h\bmod n:(h,n)=1,\ h\equiv1\pmod3\}.
\tag{730.1}
$$

Since $6\mid n$, every member is odd, hence is $1\bmod6$.
Let $M_{m,h}$ be the actual flat jets of that coefficient embedding.
Use $s=a-1$ for the same original rational coarse parameter.
The complete scalar increment is

$$
\mathcal I_h(s)=
 \sum_{j\ge1}\frac{M_{3j-1,h}}{(3j)!}
                 z_{\rm f}(s)^{3j},
\qquad
z_{\rm f}(s)^3=\frac38s+O(s^2).
\tag{730.2}
$$

The true quotient component is $J_h(s)=c_h\mathcal I_h(s)$, where
the fixed original Kodaira–Spencer comparison $c_h$ is nonzero.
No assertion about $v_p(c_h)$ is made.

**Theorem 730.1.** Suppose $p\ge41$, $p\equiv2,5\pmod9$, and the
original $M_{2,1}$ is nonzero. Then every $M_{2,h}$ is nonzero and

$$
\boxed{
\min_{h\in\mathcal H^*}2v_p(M_{2,h})
 <5+\frac{125\log2}{\log p}.
}
\tag{730.3}
$$

Each $2v_p(M_{2,h})$ is an integer. Consequently, if also
$p\ge2^{125}$, there exists an actual primitive $h$ with

$$
\boxed{v_p(M_{2,h})\le5/2.}
\tag{730.4}
$$

This conclusion uses no equality between the actual Hecke field
and $F_0$. If that field were smaller, the norm over $F_0$ would
merely repeat actual components.

**Theorem 730.2.** For any actual primitive $h$ with
$M_{2,h}\ne0$ and $v_p(M_{2,h})\le5/2$, one has

$$
\boxed{
\frac{16\,\mathcal I_h(p^9u)}{p^9M_{2,h}}
 =u+pH_h(u),\qquad
 H_h\in u^2\mathbb Z_p\langle u\rangle.
}
\tag{730.5}
$$

This is an automorphism of the closed unit disc, with inverse in
$\mathbb Z_p\langle u\rangle$, and an exact isometry. In particular

$$
v_p\bigl(\mathcal I_h(s_1)-\mathcal I_h(s_2)\bigr)
 =v_p(M_{2,h})+v_p(s_1-s_2)
\tag{730.6}
$$

for $s_1,s_2\in p^9\mathcal O$ over every complete valued extension.
The original scalar increment has only its simple central zero there.
The same difference valuation for $J_h$ adds $v_p(c_h)$.

R729 makes the nonvanishing premise of Theorem 730.1 unconditional
for every sufficiently large allowed $p$. Thus these two theorems
give a fixed depth nine for all such primes. In particular the whole
original Abel vector cannot return to its central value in that disc,
because its selected actual component cannot do so.

## 2. A square-root bound for both original central values

Use the complete original AFE of R717, without a conductor or
period change:

$$
L(\xi_{2r+1,h},r+1)
 =2\sum_{(\mathfrak a,6p)=1}
       \frac{\xi_{2r+1,h}(\mathfrak a)}
            {N\mathfrak a^{r+1}}
        K_r(cN\mathfrak a/p),
\quad r=2,3,\qquad
c=\frac{\pi}{3\sqrt3},
$$
$$
K_r(x)=e^{-x}\sum_{j=0}^r x^j/j!.
\tag{730.7}
$$

Choose the unique primary generator of each ideal. Its contribution
in absolute value is $K_r(c|a|^2/p)/|a|$.
For a direct lattice bound, distinct Eisenstein integers have distance
at least one. The disjoint discs of radius $1/2$ around the lattice
points of absolute value at most $T$ lie inside the disc of radius
$T+1/2$. Consequently their number is at most

$$
4(T+1/2)^2\le9T^2\qquad(T\ge1).
\tag{730.8}
$$

This also bounds the subset of ideal generators. Nonzero lattice
points have absolute value at least one.

Set $d=c/(2p)$ and $f(T)=e^{-dT^2}/T$. Partial summation, with
the counting function zero for $0\le T<1$, gives

$$
\begin{aligned}
\sum_{a\in\mathcal O_K\setminus\{0\}}
       \frac{e^{-d|a|^2}}{|a|}
&\le 9\int_1^\infty (1+2dT^2)e^{-dT^2}\,dT\\
&\le 9\sqrt{\pi/d}
 =9\sqrt{6\sqrt3}\sqrt p
 <36\sqrt p.
\end{aligned}
\tag{730.9}
$$

All lattice points, including every infinite tail, occur in this
bound. It does not replace an ideal count by a claim that there are
only finitely many relevant shells.

The elementary inequality used in R729 is

$$
K_r(x)\le(2^{r+1}-1)e^{-x/2}.
$$

Equations (730.7)–(730.9) therefore imply, at every primitive embedding,

$$
\boxed{
 |L(\xi_{5,h},3)|<504\sqrt p<2^9\sqrt p,\qquad
 |L(\xi_{7,h},4)|<1080\sqrt p<2^{11}\sqrt p.
}
\tag{730.10}
$$

The absolute values are intentional: this proof needs no theorem
asserting a sign for the individual central values.

Keep the original quantity

$$
\mathcal P=\frac{S_2(\theta)S_3(\theta^{-1})}{C_0^2}\in F_0,
\qquad C_0=72\sqrt3/\sqrt[3]4.
$$

R717's exact periods give all its conjugates:

$$
\sigma_h(\mathcal P)=
 \frac{\alpha^2p^2}{144\Omega^2\mathcal A^5}
 L(\xi_{5,h},3)L(\xi_{7,h},4),
\quad
\alpha=\sqrt[3]4,\quad
\mathcal A=\frac{\sqrt3\Omega^2}{2\pi}.
\tag{730.11}
$$

R729 proves directly that
$\alpha^2/(144\Omega^2\mathcal A^5)<2^{16}$:
one uses $\Omega>2/\sqrt7$, $\mathcal A>1/14$, and $\alpha^2<3$.
Hence

$$
\boxed{|\sigma_h(\mathcal P)|<2^{36}p^3.}
\tag{730.12}
$$

This improves only an upper bound; no complex approximation or
new numerical computation is involved.

## 3. The original finite toric norm is totally positive and integral

Let $V_h$ be the actual finite cuspidal representation in R727,
with original split vector $e_0$, original torus $\mathsf T_\zeta$,
and Hermitian form

$$
G(e_r,e_s)=p\delta_{rs}-1.
$$

The Borel representation on functions modulo constants is irreducible.
The $G$-invariant positive Hermitian form of the finite representation
is therefore a positive scalar times the displayed form; its
normalization at $e_0$ fixes that scalar. This holds for every complex
primitive embedding. The actual averaging operator

$$
A_h=\frac1{p+1}\operatorname{Tr}_{\mathsf T_\zeta},
\qquad u_h=A_he_0
$$

is a $G$-orthogonal projection. The unchanged original norm is

$$
N_h=G(e_0,\operatorname{Tr}_{\mathsf T_\zeta}e_0)
    =(p+1)G(u_h,u_h).
\tag{730.13}
$$

R727 proves $N_h=\sigma_h(N_1)\ne0$ for every primitive $h$.
Projection can only decrease the positive squared length. Thus

$$
\boxed{0<N_h\le(p+1)G(e_0,e_0)=p^2-1.}
\tag{730.14}
$$

The global integrality used below has no unaccounted $p$ denominator.
For the Weyl element, the original formula is

$$
we_r=-\frac1p\sum_{y\in\mathbb F_{p^2}^{\times}}
       \theta_h(y)e_{rN(y)+\operatorname{Tr}(y)}.
$$

Pairing it with $e_s$ multiplies the delta term by $p$; the remaining
term vanishes because $\sum_y\theta_h(y)=0$. Thus

$$
G(e_s,we_r)=
 -\sum_{rN(y)+\operatorname{Tr}(y)=s}
       \overline{\theta_h(y)}
 \in\mathbb Z[\zeta_n].
$$

Borel elements permute the indicator vectors. Bruhat decomposition
then gives the same integrality for $G(e_0,ge_0)$ for every finite
$g$. Summing over the actual torus proves $N_1\in\mathbb Z[\zeta_n]$.
Complex conjugation inverts $\theta$; the bijection $y\mapsto y^p$
preserves each norm/trace fiber, so the scalar is real. Hence

$$
\boxed{N:=N_1\in\mathcal O_{F_0},\qquad \sigma_h(N)=N_h>0.}
\tag{730.15}
$$

This proof uses the original pair $(e_0,\mathsf T_\zeta)$.
A change of torus coordinates without transporting $e_0$ would
not be a permissible replacement.

## 4. The norm average cancels the coefficient-field degree

Assume the specified $M_{2,1}$ is nonzero. Its exact original norm
identity is

$$
M_{2,1}^2=-\frac{8\zeta^2N}{(p+1)^2}C_0^2\mathcal P.
$$

Since $N\ne0$, this implies $\mathcal P\ne0$.
Every conjugate $\sigma_h(\mathcal P)$ is therefore nonzero.
Together with $N_h\ne0$, the actual identity for each embedding gives

$$
M_{2,h}^2
 =-\frac{8\zeta^2N_h}{(p+1)^2}C_0^2\sigma_h(\mathcal P)\ne0.
\tag{730.16}
$$

All scalar factors outside $N_h\sigma_h(\mathcal P)$ are $p$-units.
Both factors lie in the selected copy of $\mathbb Q_p$, because
$p$ splits completely in $F_0$. Consequently

$$
2v_p(M_{2,h})=v_p\bigl(\sigma_h(N\mathcal P)\bigr)\in\mathbb Z.
\tag{730.17}
$$

It is not necessary here to prove that every $M_{2,h}$ itself lies in
$\mathbb Q_p$, or to assert an integer rather than half-integer
valuation for every such jet.

R717 gives the global integral denominator

$$
D=2^{37}3^{26}p^5,\qquad D\mathcal P\in\mathcal O_{F_0}.
$$

By (730.15), $DN\mathcal P$ is a nonzero algebraic integer.
Equations (730.12), (730.14), and $2^{37}3^{26}<2^{89}$ give

$$
|\sigma_h(DN\mathcal P)|<2^{125}p^{10}.
$$

Its field norm is thus a nonzero ordinary integer satisfying

$$
0<\left|N_{F_0/\mathbb Q}(DN\mathcal P)\right|
 <(2^{125}p^{10})^{g_0}.
\tag{730.18}
$$

Because $p\equiv-1\bmod n$, the prime $p$ splits completely in
$F_0$. There are exactly $g_0$ primes above $p$, with residue degree
one, and the embeddings in $\mathcal H^*$ run through them.
Therefore the valuation of this same integer is exactly

$$
v_p\left(N_{F_0/\mathbb Q}(DN\mathcal P)\right)
 =5g_0+2\sum_{h\in\mathcal H^*}v_p(M_{2,h}).
\tag{730.19}
$$

Since the absolute value of a nonzero integer is at least the
corresponding power of $p$, (730.18)–(730.19) imply

$$
\frac1{g_0}\sum_{h\in\mathcal H^*}2v_p(M_{2,h})
 <5+\frac{125\log2}{\log p}.
\tag{730.20}
$$

At least one summand is no larger than its average. This proves
(730.3). If $p\ge2^{125}$, the right side is at most six, and the
strict inequality remains. The integral numbers in (730.17)
cannot then all be at least six. At least one is at most five,
which is (730.4).

In contrast to a bound at one preassigned place, division by
$g_0$ removes the field degree. The selected $h$ is allowed to vary
with $p$; this is essential for the use below.

## 5. All jets lie on one rational line for the selected embedding

Fix a primitive $h$ furnished by (730.4), and put
$\eta_h=v_p(M_{2,h})\le5/2$.
The actual quotient and the rational CM point are defined over
$\mathbb Q$. Its real Hecke field is contained in $F_0$, so its
$p$-adic eigenline is defined over $\mathbb Q_p$.

The original argument of R711 therefore gives, for this same
embedding,

$$
J_h(s)=c_h\mathcal I_h(s)\in s\mathbb Q_p[[s]].
$$

The entire inverse between $s$ and $z_{\rm f}^3$ belongs to
$\mathbb Q_p[[s]]$. This is the rational Gauss–Manin calculation
of R711, independent of $h$. Comparing every coefficient gives

$$
c_hM_{3j-1,h}\in\mathbb Q_p\quad(j\ge1).
$$

The first jet is nonzero. Division by this one fixed coefficient
therefore proves

$$
\boxed{
M_{3j-1,h}/M_{2,h}\in\mathbb Q_p
\quad\text{for every }j\ge1.
}
\tag{730.21}
$$

No separate rescaling at different derivative orders is allowed or
used. This statement does not require the special $h=1$ nonzero
endpoint of R705.

## 6. The complete one-p Hodge bound at every primitive embedding

For clarity, the general estimate from R727 does not need its
three residue-unit hypotheses. Those hypotheses were used there
to evaluate the first jet and to improve the final depth.

In the finite cuspidal model, every Borel matrix acts integrally
on the indicator lattice, and every element of the other Bruhat cell
uses the Weyl formula with only one denominator $p$. Thus, for
every $g$,

$$
p\,g e_0\ \text{is integral},\qquad
p\,g u_h=\frac1{p+1}\sum_{t\in\mathsf T_\zeta}p\,(gt)e_0
\ \text{is integral}.
$$

This bounds the whole averaged vector at every cusp; it does not
multiply two estimates and create an unnecessary second denominator.
The original normalized theta newform has integral algebraic Fourier
coefficients; the original tame matrices are integral at $p$.
The same all-cusp $q$-expansion principle and original Hodge/flat
comparison as in R592 consequently give, for every $m\ge0$,

$$
v_p(M_{m,h}/m!)\ge-1-m\frac p{p+1}.
\tag{730.22}
$$

The bound applies to the complete original series, including
factorials divisible by $p$.

Put

$$
V=z_{\rm f}^3/p^3,\qquad
E_{j,h}=\frac{p^{3j}M_{3j-1,h}}{(3j)!}.
$$

From $(3j)!=(3j)(3j-1)!$, (730.22) gives exactly

$$
v_p(E_{j,h})\ge
 \frac{3j-1}{p+1}-v_p(3j).
\tag{730.23}
$$

This lower bound is strictly positive for every $j\ge1$.
If $p\nmid3j$, that is immediate. If $a=v_p(3j)\ge1$, then
$p^a\mid j$, since $p\ne3$, and the lower bound is at least

$$
\frac{3p^a-1}{p+1}-a>1.
$$

For $a=1$ this equals $2-4/(p+1)>1$; increasing $a$ increases
the expression. The lower bound in (730.23) also tends to infinity
as $j$ tends to infinity.

Normalize by the same first coefficient

$$
E_{1,h}=p^3M_{2,h}/6,\qquad
G_h(V)=\mathcal I_h(V)/E_{1,h}
      =V+\sum_{j\ge2}b_{j,h}V^j.
$$

Every $b_{j,h}$ belongs to $\mathbb Q_p$ by (730.21). Moreover

$$
v_p(b_{j,h})>-\eta_h-3\ge-11/2.
$$

The valuation of a nonzero rational $p$-adic coefficient is an
integer. Thus

$$
\boxed{
b_{j,h}\in p^{-5}\mathbb Z_p,\qquad
v_p(b_{j,h})\longrightarrow\infty.
}
\tag{730.24}
$$

This integral rounding is applied to the ratios in (730.21), not
to the individual possibly half-integral jets.

## 7. The entire fixed-depth coarse isometry

Equation (730.24) implies

$$
\frac{G_h(p^6u)}{p^6}
 =u+\sum_{j\ge2}p^{6(j-1)}b_{j,h}u^j
 \in u+p\,u^2\mathbb Z_p\langle u\rangle.
\tag{730.25}
$$

The exponent is at least one for every $j\ge2$, and tends to
infinity. Thus no high-degree term omitted from a finite prefix
can affect the assertion.

R710/R711 give the complete original coarse change

$$
V=\Psi(s/p^3),\qquad
\Psi(v)=\frac38v+\sum_{j\ge2}\psi_jv^j,\qquad
\psi_j\in p\mathbb Z_p,\quad
\Psi\in\mathbb Z_p\langle v\rangle.
\tag{730.26}
$$

For $s=p^9u$, the expression $\Psi(p^6u)/p^6$ is
$(3/8)u$ plus a higher series divisible by $p$.
Compose this with (730.25). Since $E_{1,h}=p^3M_{2,h}/6$,
the resulting exact normalization is

$$
\frac{16}{p^9M_{2,h}}\,\mathcal I_h(p^9u)
 =\frac83\,\frac{G_h(\Psi(p^6u))}{p^6}
 =u+pH_h(u),
$$

which proves (730.5) with its factor sixteen.

For completeness, a restricted series $F(u)=u+pH(u)$,
$H\in u^2\mathbb Z_p\langle u\rangle$, has an inverse of the same
integral restricted form. Iterating

$$
u_{k+1}=v-pH(u_k)
$$

is a contraction in the complete Tate algebra; it converges to a
restricted inverse with linear term one. The same contraction
works on the closed unit disc over any complete valued extension.
For any $u_1,u_2$ in that disc, division of
$H(u_1)-H(u_2)$ by $u_1-u_2$ is integral. Consequently

$$
F(u_1)-F(u_2)=(u_1-u_2)(1+pQ),\qquad v_p(Q)\ge0.
$$

The parenthesis is a unit. This proves the exact difference
valuation and the unique-center assertion of Theorem 730.2.

## 8. What this closes and what it leaves

R729 supplies nonvanishing at every sufficiently large allowed
prime. The norm over all actual primitive embeddings now selects
a component with a uniformly bounded first-jet valuation, and the
complete all-order estimates give depth nine uniformly in $p$.
This strengthens the first-order input available for the original
quotient without a conjectural all-prime Cartier-unit statement.

The selected component is a component of the same actual Abel map.
If two points in this disc have the same original Abel value, their
selected component agrees, so (730.6) forces their parameters to
agree. This is a statement about the original local map, not a
claim that every rational point must have the central Abel value.

The original candidate region begins at depth four. The intermediate
depths have not been removed by this theorem. More fundamentally,
the positive-rank rational-point condition is governed by the actual
height functions and their fixed constants; it is not the equation
$\mathcal I_h=0$. R724's actual height input, R728's original
$q/\beta$ comparison, and the common-root certificate remain to
be completed. No Serre-uniformity conclusion is asserted.

## Dependencies

- [R729](R729-uniform-full-Abel-nonvanishing-and-valuation-bound.md):
  unconditional sufficiently-large nonvanishing of the original
  $M_2$, exact original periods, and the elementary period bound.
- [R717](R717-exact-original-CM-norm-from-certified-complex-traces.md):
  full AFE, finite CM sums, field and global integral denominator.
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md):
  original finite cuspidal model, toric norm, full all-cusp
  one-$p$ denominator, and unchanged primitive tame direction.
- [R710](R710-unramified-squared-jets-and-complete-coarse-Abel-reduction.md),
  [R711](R711-rational-CM-Abel-line-and-integral-jet-valuations.md):
  full rational flat/coarse comparison and the fixed actual KS line.
