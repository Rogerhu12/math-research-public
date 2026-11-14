# R721 — Conditional deep-disc isometries for the original Abel primitive

Status: proved under the explicitly stated arithmetic hypotheses.  The
statement is uniform in $p$; it does not assert those hypotheses for every
prime.  In particular, the proof below does not supply the actual $M_2$ value
at $p=137147$ and does not identify any Abel function with a height.

Fix $p\ge41$, $p\equiv5\pmod6$, the actual positive cubic quotient of R575,
the original $\theta=\theta_{-1}$, the full tame marking, and the selected
p-adic embedding used in R705, R710, and R711.

## 1. Statement with the original parameters and constants

Write $s=a-1$ and retain the complete actual Abel primitive

$$
\mathcal I(z_{\rm f})
 =\sum_{j\ge1}\frac{M_{3j-1}}{(3j)!}z_{\rm f}^{3j}.
$$

This is the original flat parameter, not the elliptic-curve formal
coordinate used in the Cartier calculations.  Put

$$
V=z_{\rm f}^3/p^3,\qquad
P_p(V)=p^{-2}\mathcal I(z_{\rm f})
       =\sum_{j\ge1}b_jV^j,\qquad
b_j=\frac{p^{3j-2}M_{3j-1}}{(3j)!}.
\tag{721.1}
$$

Let $j_*=(p-2)/3$ and retain the actual endpoint unit

$$
b_* = b_{j_*}
     =\frac{p^{p-4}M_{p-3}}{(p-2)!}\ne0.
\tag{721.2}
$$

Assume that the original fixed-CM coefficient $C_p$ is a $p$-adic unit and
that the actual full $M_2$, including every original Fourier block, satisfies

$$
v_p(M_2)=0.
\tag{721.3}
$$

Then the original scalar Abel primitive has no noncentral zero in

$$
v_p(a-1)>7/2.
\tag{721.4}
$$

More precisely, if $s$ is nonzero in this range, $t=v_p(s)-3$, then

$$
\boxed{\quad
v_p(\mathcal I(s))=v_p(s),\qquad
v_p\left(\frac{\mathcal I(s)}{M_2s/16}-1\right)
 \ge\min\{t,\,2t-1\}>0 .
\quad}
\tag{721.5}
$$

Here and below the notation $\mathcal I(s)$ means the same original primitive
composed with the complete flat/coarse change, not a new normalization.

There is also a precise integral analytic statement:

$$
\boxed{\quad
G(u):=\frac{\mathcal I(p^4u)}{p^4b_*}
 =\frac{M_2}{16b_*}u+pH(u),\qquad
H\in u^2\mathbf Z_p\langle u\rangle .
\quad}
\tag{721.6}
$$

The displayed linear coefficient is in $\mathbf Z_p^\times$.  Consequently $G$ is
an analytic automorphism of the closed unit disc, with inverse in
$\mathbf Z_p\langle T\rangle$, and for any two points of that disc over a complete extension,

$$
v_p(G(u_1)-G(u_2))=v_p(u_1-u_2).
\tag{721.7}
$$

In particular,

$$
v_p\bigl(\mathcal I(s_1)-\mathcal I(s_2)\bigr)
=v_p(s_1-s_2)\qquad(s_1,s_2\in p^4\mathcal O).
\tag{721.8}
$$

The actual quotient Abel component remains

$$
J_\sigma(s)=c_\sigma\mathcal I(s),
\tag{721.9}
$$

with exactly the single original nonzero Kodaira-Spencer constant
from R711.  Thus its difference valuation is (721.8) plus $v_p(c_\sigma)$;
this proof does not call that constant a unit.

## 2. The adjacent original coefficient forces the quadratic divisibility

R683/R705 give the exact original lowest-valuation criterion

$$
v_p(M_2)=-1
\quad\Longleftrightarrow\quad
C_p C_{p-3}\not\equiv0\pmod p.
\tag{721.10}
$$

Under (721.3), the left side is false.  Since $C_p$ is a unit,
$C_{p-3}\equiv0\pmod p$.  The next original flat jet $M_5$ has the fixed-CM
pair $(C_{p-3},C_{p-6})$, by R705.  Its leading square is therefore zero.

The full original norm bound in R705 first gives $v_p(M_5)\ge-7/2$.
The common rational Abel line and the nonzero endpoint in R711 make
every actual jet valuation an integer, so

$$
v_p(M_5)\ge-3.
\tag{721.11}
$$

No value, unit status, or nonvanishing of $C_{p-6}$ is required.
The role of the $C_p$ assumption is precisely to force the shared
$C_{p-3}$ factor in this adjacent pair.

Divide the complete function by the same endpoint $b_*$ and write

$$
\widetilde P_p=P_p/b_*=\sum_{j\ge1}a_jV^j.
$$

R710 proves full-tail integrality and convergence, including every
$j$ whose factorial contains $p$; R711 gives the rational coefficient
line.  Therefore

$$
\widetilde P_p\in\mathbf Z_p\langle V\rangle.
\tag{721.12}
$$

In particular this is an assertion about all $j$, not just the finite
Cartier prefix.  The first two coefficients are exactly

$$
\boxed{\quad
a_1=\frac{pM_2}{6b_*},\qquad
a_2=\frac{p^4M_5}{720b_*}.
\quad}
\tag{721.13}
$$

Since $p\ge41$, both $6$ and $720$ are units.  Equations (721.3) and
(721.11) consequently give

$$
v_p(a_1)=1,\qquad v_p(a_2)\ge1,\qquad
v_p(a_j)\ge0\quad(j\ge3).
\tag{721.14}
$$

The coefficients tend to zero p-adically, by the entire Hodge/flat
bound of R710.  No coefficient beyond the finite prefix has been
silently discarded.

## 3. Strict dominance in the full infinite sum

Let $V\ne0$ have valuation $t>1/2$.  The linear term has valuation
$1+t$.  Every other term has strictly greater valuation:

$$
v_p(a_2V^2)\ge1+2t>1+t,\qquad
v_p(a_jV^j)\ge jt\ge3t>1+t\quad(j\ge3).
$$

The entire tail converges, and the difference from the linear term
has relative valuation at least $\min\{t,2t-1\}$.  Thus

$$
v_p(\widetilde P_p(V))=1+t,\qquad
v_p\left(\frac{\widetilde P_p(V)}{a_1V}-1\right)
\ge\min(t,2t-1).
\tag{721.15}
$$

This is a strict full-tail estimate.  It does not require the
remaining first nonzero residue coefficient to be the cubic term,
nor any bound on how long the later zero-Cartier string can be.

## 4. The complete coarse change preserves the estimate

R711 proves that the entire original change is rational and that

$$
V=\Psi(v)=\frac{\Xi(p^3v)}{p^3},\qquad
v=s/p^3,\qquad
\Psi(v)=\frac38v+\sum_{n\ge2}\psi_nv^n,
$$
$$
\Psi\in\mathbf Z_p\langle v\rangle,\qquad
\psi_n\in p\mathbf Z_p,\qquad
v_p(\psi_n)\longrightarrow\infty.
\tag{721.16}
$$

This uses the full scaled integral change in R710; the assertion
does not follow merely by retaining its linear term.

For $v_p(v)=t\ge0$, one has $v_p(\Psi(v))=t$.  For $t>0$,

$$
v_p\left(\frac{\Psi(v)}{(3/8)v}-1\right)\ge1+t.
\tag{721.17}
$$

Multiply (721.15) by this exact change.  Since
$p^2b_*a_1V=p^3M_2V/6=M_2z_{\rm f}^3/6$, its original $s$-linear
term is exactly $M_2s/16$.  Equation (721.17) has strictly larger
error valuation than the bound needed in (721.15).  This proves
(721.5), including every higher change-of-parameter term.

The center is a simple characteristic-zero zero because its
derivative is $M_2/16\ne0$.  Every $\mathbf Q_p$ point with $v_p(s)>3$ has integral
valuation $v_p(s)\ge4$, so it lies in the region (721.4).

## 5. Closed-disc automorphism and exact isometry

Set

$$
R(u)=\Psi(pu)/p
 =\frac38u+\sum_{n\ge2}p^{n-1}\psi_nu^n.
$$

It belongs to $\mathbf Z_p\langle u\rangle$, has no constant term, and its nonlinear
coefficients are divisible by $p^2$.  Substituting into (721.12) gives

$$
G(u)=p^{-2}\widetilde P_p(pR(u))
=\frac{a_1}{p}R(u)+a_2R(u)^2+
 \sum_{j\ge3}p^{j-2}a_jR(u)^j.
\tag{721.18}
$$

All the displayed series converge in the Tate algebra.
The first coefficient $a_1/p$ is the unit $M_2/(6b_*)$; the second term
is divisible by $p$, and every term with $j\ge3$ is divisible by $p$.
The only linear term is therefore $M_2u/(16b_*)$, proving (721.6).

For an integral Tate series $H$, the difference $H(x)-H(y)$ is divisible
by $x-y$ with integral quotient whenever $x$ and $y$ are in the closed
unit disc.  Therefore $\kappa+p(H(x)-H(y))/(x-y)$ is a unit, where
$\kappa=M_2/(16b_*)$.  This proves (721.7).

For any $w$ in that disc, iterate

$$
u_{r+1}=\kappa^{-1}(w-pH(u_r)),\qquad u_0=\kappa^{-1}w.
$$

The iteration contracts by a factor at most $|p|$, so it has one
solution and converges uniformly.  The same iteration in the complete
Tate algebra $\mathbf Z_p\langle w\rangle$ gives an integral restricted inverse series.
Thus the assertion is an analytic automorphism, and not merely a
pointwise zero-count.  Multiplying back by $p^4b_*$ proves (721.8).

## 6. A useful variant if the original $M_2$ has positive valuation

The same proof also records precisely what survives if $C_p$ is a
unit and $M_2\ne0$ has an integer valuation $h\ge0$.  Equation (721.10)
still forces $C_{p-3}$ to vanish, so $a_2$ remains in $p\mathbf Z_p$, while
$v_p(a_1)=h+1$.  Strict linear dominance holds whenever

$$
t>\max\{h,(h+1)/2\}.
\tag{721.19}
$$

In that range the exact original valuation is $v_p(\mathcal I(s))=h+v_p(s)$.
On the integer closed disc $s\in p^{h+4}\mathcal O$ there is the more concrete
automorphism

$$
\frac{\mathcal I(p^{h+4}u)}{p^{2h+4}b_*}
=\frac{p^{-h}M_2}{16b_*}u+pH_h(u),
\qquad H_h\in u^2\mathbf Z_p\langle u\rangle.
\tag{721.20}
$$

To verify all denominators, write $e=h+1$ and $R_e(u)=\Psi(p^eu)/p^e$.
After division by $p^{2h+2}$, the $j=1$ term is
$(a_1/p^{h+1})R_e$.  The $j=2$ term is $a_2R_e^2$, still divisible by $p$.
For every $j\ge3$ its additional $p$ power is

$$
j(h+1)-(2h+2)=(j-2)(h+1)\ge1.
$$

The nonlinear coefficients of $R_e$ are also divisible by $p$.
This proves (721.20) with the same contraction argument.
The zero value $M_2=0$ is not covered by this variant.

## 7. Scope and links to the actual problem

This proof uses the exact original coefficients from
[R705](R705-actual-higher-Abel-blocks-and-uniform-order-bound.md),
the complete scaled tail from
[R710](R710-unramified-squared-jets-and-complete-coarse-Abel-reduction.md),
and the single rational Abel line and full change from
[R711](R711-rational-CM-Abel-line-and-integral-jet-valuations.md).
It makes no assertion that $C_p$ or $M_2$ is a unit for every prime.
Its unit hypothesis concerns the full original $M_2$, rather than
a p-adic lift of the single coefficient $C_{p-3}$.

The statements about the unnormalized original Abel primitive and
the nonzero comparison constant do not require the Mordell-Weil
nonvanishing assumption of R616.  Any use of R682's normalized $t_i$,
its common order, or the actual height exterior product continues
to retain that original L-value hypothesis.

The actual candidate range $v_p(a-1)\ge4$ from R317 lies in (721.4),
under the stated unit assumptions.  This shows that a candidate in
that range cannot make this scalar Abel increment return to its
center value.  The true height contains the original $\Lambda$,
Coleman-Gross constants, and $\ell_h$.  None of those terms has been
identified with this Abel increment or removed.  Hence this result
is not an exclusion of the actual height zero or a completion of
the Serre uniformity problem.
