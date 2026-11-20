# R1002 — The actual ten-step theta companion and four free CM jets

Date: 2026-11-21 (Asia/Taipei). Author: serre-public-astra-20261120-de0a3e3b / legendre_shift.

**Status: proved local source comparison and complete finite-jet boundary.** This consumes the exact inverse-character companion from R964 and the actual Katz transport from R826. At the original CM point, its ten-step equation determines one coefficient in a five-dimensional invariant jet space. Its homogeneous kernel has four explicit independent jets. Consequently this local equation does not force the original end column's marked value to be a unit. This is not a counterexample involving the actual global CM form: the four parameters describe local solutions of the specified equation, not arbitrary choices available for that fixed global form.

No mathematical execution, coefficient window or new prime calculation is used. The primitive/Legendre mask is unchanged. In particular the new statement does not undo R996/R999's global cusp nonvanishing results.

## 1. The full CM form and its different quotient weight

Retain

$$
p=6N+5\ge41,\qquad p\bmod9\in\{2,5\},\qquad
k=p-9=6(N-1)+2.
\tag{1002.1}
$$

Let $W_k$ be precisely R954's conductor-$(2s)$ odd CM form, with its original positive embedding and finite character. Define its actual full-level quotient

$$
f=\frac{W_{p-9}}{\eta^4}\in M_{p-11},\qquad
m=N-1,\qquad p-11=6m.
\tag{1002.2}
$$

The full theta input has weight $k=p-9$; the quotient has weight $p-11$. They must not be interchanged in the Katz operator below. Both are the integral objects already constructed in R954/R959.

Write $X=E_4$, $Y=E_6$, and use the actual graded Serre derivation

$$
D=-\frac{Y}{3}\partial_X-\frac{X^2}{2}\partial_Y.
\tag{1002.3}
$$

It preserves $\Delta=(X^3-Y^2)/1728$. On the original tame cover, $\eta^4$ has its already fixed phase and satisfies $(\eta^4)^6=\Delta$. Since $6$ is a unit and $\eta^4$ is nonzero near the CM point, this gives $D\eta^4=0$. Equivalently its Serre derivative is zero before choosing the fixed-discriminant frame.

Let $A=E_{p-1}$ be the original Hasse invariant and put

$$
B=DA=\frac{E_{p+1}}{12}.
\tag{1002.4}
$$

These are identities after reduction, as in R992. For a weight-$j$ input, the actual Katz operator with respect to $q=Q^6$ is transported by

$$
\mathcal T_j=A D+jB.
\tag{1002.5}
$$

This is R826(826.20)–(826.21), with $B=DA$, in the present fixed-discriminant frame. Its original width-six version is $\Theta_Q=6\mathcal T_j$. An application changes the full modular weight from $j$ to $j+p+1$.

R964(964.15)–(964.16), applied to $k=p-9$, gives the complete source identity

$$
\Theta_Q^{10}W_{p-9}=A^{11}H_{12}^{\rm inv},
\qquad H_{12}^{\rm inv}=\eta^4XY.
\tag{1002.6}
$$

The last identity follows from the exact weight-ten full-level quotient in R964, with cusp constant one. It is not a new companion computation.

The successive input weights are $k+j(p+1)$ for $0\le j\le9$. Modulo $p$ they are $-9+j$. Because $D\eta^4=0$, cancellation of the same nonzero $\eta^4$ in (1002.6) therefore gives

$$
\boxed{
\mathcal Lf:=\mathcal T_0\mathcal T_{-1}\cdots
\mathcal T_{-9}f
=6^{-10}A^{11}XY.
}
\tag{1002.7}
$$

Composition is from right to left. Thus $\mathcal T_{-9}$ acts first. The factor $6^{-10}$ and the full input weight $p-9$ are retained; the first operator is not $\mathcal T_{-11}$.

## 2. The original CM local coordinate and the finite primitive

Keep the original $E^-$ frame

$$
P:\quad X=0,\quad Y=Y_0=-864.
\tag{1002.8}
$$

The formulas below also work with any specified unit $Y_0$, but no change to this original frame is needed. On the fixed-discriminant branch through $P$,

$$
Y(X)^2=X^3+Y_0^2,\qquad
Y(X)=Y_0\left(1+\frac{X^3}{Y_0^2}\right)^{1/2},
\qquad DX=-Y(X)/3.
\tag{1002.9}
$$

The square root is the branch with value $Y_0$, so it has no new sign freedom. Its needed denominators are units for $p\ge41$.

The Hasse invariant has a simple zero at the fine CM point, and has weight $p-1\equiv4\pmod6$. Consequently

$$
A(X)=a_1X\bigl(1+O(X^3)\bigr),\qquad
a_1\ne0,\qquad
b_0=B(P)=a_1d_0,\qquad d_0=DX(P)=-Y_0/3.
\tag{1002.10}
$$

Here $a_1,b_0,d_0$ are units. The expansions of $A/X$, $Y$, and $f$ on this branch are series in $X^3$. This is the actual order-three stabilizer character, not a supplementary vanishing assumption.

Put

$$
\partial=A^2D,\qquad \gamma=a_1^2d_0=a_1b_0.
\tag{1002.11}
$$

Its inverse differential has the shape

$$
\frac{dX}{A(X)^2DX}
=\gamma^{-1}X^{-2}
\left(1+\sum_{j\ge1}c_jX^{3j}\right)dX.
\tag{1002.12}
$$

We only integrate its terms through exponent $10$. Define the finite Laurent polynomial

$$
u(X)=\gamma^{-1}\left\{
-X^{-1}+\sum_{j=1}^{4}\frac{c_j}{3j-1}X^{3j-1}
\right\}.
\tag{1002.13}
$$

The four positive denominators are $2,5,8,11$, so all are units. Its constant is fixed to be zero. By construction,

$$
u=-\gamma^{-1}X^{-1}+O(X^2),\qquad
\partial u=1+O(X^{15}).
\tag{1002.14}
$$

This is a finite primitive, not an assertion that (1002.12) has a full characteristic-$p$ formal primitive. The first exponent at which the displayed term pattern permits a denominator divisible by $p$ is

$$
3j-1=p,\qquad j=(p+1)/3;
$$

it corresponds to the differential term $X^{p-1}dX$. Its coefficient need not vanish. This possible obstruction lies beyond the terms used in (1002.13).

## 3. Exact conjugation of the ten operators

For every integer $j$, in the local function field one has the operator identity

$$
\mathcal T_j=A^{-j-1}\partial A^j.
\tag{1002.15}
$$

Indeed the right side applied to $v$ is
$A^{1-j}D(A^jv)=A Dv+j(DA)v$. Multiplication by $A^j$ occurs before differentiation. Adjacent conjugating powers cancel, so induction gives

$$
\mathcal T_{j+n-1}\cdots\mathcal T_j
=A^{-j-n}\partial^n A^j.
\tag{1002.16}
$$

For $j=-9,n=10$ this is

$$
\boxed{\mathcal L=A^{-1}\partial^{10}A^{-9}.}
\tag{1002.17}
$$

In particular (1002.7) is equivalent, in the local function field, to

$$
\partial^{10}(A^{-9}f)=6^{-10}A^{12}XY.
\tag{1002.18}
$$

No inverse of $p$ or of an unproved marked value has occurred.

## 4. The complete five-dimensional invariant jet calculation

Work only modulo $X^{13}$, and let

$$
J=\operatorname{span}_k\{1,X^3,X^6,X^9,X^{12}\}
\subset k[[X]]/(X^{13}).
\tag{1002.19}
$$

All coefficients of $\mathcal T_j$ respect the $X^3$ character and the operator does not decrease order at $X=0$. Thus $\mathcal L$ induces an endomorphism of this jet space, and the discarded terms of an actual invariant series, beginning at $X^{15}$, cannot affect it.

For $e\in\{0,3,6,9\}$ define the invariant jets

$$
v_e=[A^9u^e]_{\bmod X^{13}}.
\tag{1002.20}
$$

Their respective orders are $9-e$, with leading coefficients

$$
a_1^9(-\gamma^{-1})^e\ne0.
\tag{1002.21}
$$

They are therefore four independent vectors in $J$. They are all killed by $\mathcal L$ modulo $X^{13}$. To check the finite error explicitly, an application of $\partial$ raises Laurent order by at least one. If $e>0$, the discrepancy between differentiating $u^e$ using $\partial u=1$ and using (1002.14) has order at least $16-e$ after its first occurrence. After a total of ten derivatives, every resulting error has order at least $25-e\ge16$. The ordinary tenth derivative of the polynomial $u^e$ is zero for $e\le9$. Multiplication by $A^{-1}$ in (1002.17) still leaves order at least $15$. For $e=0$, the derivative is exactly zero. This proves

$$
\mathcal Lv_e=0\quad\text{in }J.
\tag{1002.22}
$$

For an invariant monomial whose initial order is $\nu$, the leading indicial coefficient of $\mathcal L$ is

$$
b_0^{10}\prod_{j=0}^{9}(\nu-9+j).
\tag{1002.23}
$$

In particular

$$
\mathcal L(X^{12})
=b_0^{10}\frac{12!}{2}X^{12}\pmod {X^{13}}.
\tag{1002.24}
$$

It is nonzero, since $p\ge41$. The four independent vectors in (1002.22), together with (1002.24), show that $\mathcal L$ has rank exactly one on $J$, with image $kX^{12}$ and kernel exactly their span. This proves the full finite-jet statement, rather than only listing the roots of an indicial polynomial.

The right side of (1002.7) is

$$
6^{-10}a_1^{11}Y_0 X^{12}\pmod {X^{13}}.
$$

Its coefficient is a unit. A particular solution is $c_*X^{12}$, where

$$
\boxed{
c_*=\frac{2a_1^{11}Y_0}{6^{10}12!b_0^{10}}
=\frac{a_1}{2^9 12!Y_0^9}\ne0.
}
\tag{1002.25}
$$

The second equality uses $b_0=a_1(-Y_0/3)$ and keeps the width-six factor in (1002.7). Therefore the necessary and sufficient condition for an invariant jet to satisfy the actual equation modulo $X^{13}$ is

$$
\boxed{
f\equiv c_*X^{12}
 +\lambda_0v_0+\lambda_3v_3
 +\lambda_6v_6+\lambda_9v_9
\pmod {X^{13}},
\qquad \lambda_e\in k.
}
\tag{1002.26}
$$

The possible initial orders permitted by this exact local equation are precisely

$$
\boxed{0,3,6,9,12.}
\tag{1002.27}
$$

Each occurs for a solution jet in (1002.26). In particular the actual global $f$ cannot have order greater than twelve, but this local equation alone does not exclude any of the five displayed orders. Its actual global parameters remain fixed by the CM theta source, by its Fourier normalization and by global holomorphicity.

The separate global weight bound is still retained: since $f=Y^mR(X^3/Y^2)$ with $\deg R\le\lfloor m/2\rfloor$, its actual order also satisfies $\nu\le3\lfloor m/2\rfloor$. Thus a formal solution jet of a displayed order larger than this bound is not being claimed to come from an element of the actual global weight space.

## 5. The unchanged end column and its two free low jets

For clarity, here is the exact original source comparison needed to interpret the end-column functional. Put $T_{a,b}=[u^av^b]\mathscr J$ as in R968. For an integer weight $k\equiv2\pmod6$, let $f_k=W_k/\eta^4$, and define

$$
P_b=(k+b-1)!\,b!\,T_{k+b-1,b}.
\tag{1002.28}
$$

The complete lattice source gives $P_0=f_k$. Applying the already proved R968 heat equation, including its $Xuv/4$ term, gives

$$
P_1=6Df_k,\qquad
P_{b+1}=6DP_b-\frac{b(k+b-1)}4XP_{b-1}.
\tag{1002.29}
$$

Using $DX=-Y/3$ before specializing, its third step is exactly

$$
P_3=216D^3f_k-\frac32(3k+2)X Df_k+\frac{kY}{2}f_k.
\tag{1002.30}
$$

For $k=p-9$, the corresponding indices are $k+2=p-7$ and $b=3$. R996's complete end-column identity is $Z_{p-7,1}=12T_{p-7,3}$; hence its actual reduction is

$$
\boxed{
(p-7)!Z_{p-7,1}
=432D^3f+75X Df-9Yf.
}
\tag{1002.31}
$$

All factorials used in (1002.28)–(1002.31) are below $p$. This is an exact comparison of the original column, not a replacement by a single Gaussian summand or by a different theta family.

Write the actual full-level polynomial as

$$
f=Y^mR(z),\qquad z=X^3/Y^2,\qquad m=N-1\equiv-11/6\pmod p,
$$
$$
R(z)=R_0+R_1z+\cdots.
\tag{1002.32}
$$

On the fixed-discriminant branch, put $f=f_0+f_3X^3+O(X^6)$. Then

$$
f_0=Y_0^mR_0,\qquad
f_3=Y_0^{m-2}\left(R_1+\frac m2R_0\right),\qquad
D^3f(P)=-\frac{2Y_0^3}{9}f_3.
\tag{1002.33}
$$

Substituting in (1002.31) gives the exact marked functional

$$
\boxed{
\frac{(p-7)!}{Y_0^N}Z_{p-7,1}(P)
=79R_0-96R_1.
}
\tag{1002.34}
$$

Equivalently, before division by the specified $Y_0^N$,

$$
(p-7)!Z_{p-7,1}(P)=-9Y_0f_0-96Y_0^3f_3.
\tag{1002.35}
$$

The jets $v_9$ and $v_6$ in (1002.26) have orders zero and three with unit leading coefficients. Thus $(f_0,f_3)$ can be prescribed arbitrarily among these local solution jets, and the remaining parameters and the forced $X^{12}$ term do not change that fact. In particular the local theta equation is compatible with a unit $f_0$ and

$$
f_3=-\frac{3}{32Y_0^2}f_0,
\qquad\text{equivalently}\qquad R_1=\frac{79}{96}R_0,
\tag{1002.36}
$$

which makes (1002.34) zero. It is equally compatible with choices making (1002.34) nonzero. All the displayed denominators are units for $p\ge41$.

If the actual global form has order exactly three at $P$, (1002.35) does give a nonzero end-column mark. Orders six, nine or twelve give a zero end-column mark. Order zero requires the specific comparison (1002.34). The ten-step equation by itself does not select between these cases.

## 6. Exact scope of the boundary

This result proves a local finite-jet statement for the actual ten-step companion equation, with its unchanged phase, full weight, width-six scale, Hasse zero and original end column. It does not claim that every local jet in (1002.26) extends to a global modular form, or that the actual fixed CM form can be changed to a different one. A successful next argument must use a property not supplied by this local equation, such as the original global integral modular lattice, its CM Fourier source, or an additional genuine relation among its marked jets.

R996 already proves the end column globally nonzero from its cusp coefficient, and proves it survives the original filter when $5\nmid p+1$. Those results are fully compatible with (1002.36): a nonzero modular form may have zero value at the CM point. R999's larger nonzero-space family does not remove the same marked-value issue. Neither $\mathcal G$-stability nor the original same-label three-factor nonvanishing has been proved here.

## Sources consumed without redoing their conclusions

- [R826, original companion comparison](R826-original-inert-companion-theta-CM-pairing.md), (826.20)–(826.24): the genuine weight-dependent Katz transport and its normalizations. The present ten-step resonance is a different specified CM family and is analyzed explicitly above.
- [R954](R954-original-odd-sigma-and-conductor-two-s-CM-evaluations.md) and [R959](R959-exact-coarse-CM-factor-criterion-for-the-original-antidiagonal.md): the actual odd family, full-level quotient and integral modular lattice.
- [R964](R964-inverse-conductor-two-s-CM-family-and-original-sigma-heat-channel.md), (964.6), (964.15)–(964.16): the inverse-character companion and the complete ten-step source used in (1002.6).
- [R968](R968-full-level-mixed-CM-jet-and-critical-factor.md): the original two-variable heat equation, canonical-zeta column and actual Taylor factorials.
- [R992](R992-original-full-level-Jacobi-operator-and-filtered-stability-criterion.md): the actual Hasse relations, simple fine CM zero and distinction between global filtered space and marked functional.
- [R996](R996-original-end-column-cusp-unit-and-filtered-space-nonzero.md): the exact end column and its global cusp unit, consumed here without recomputation.

The main Serre-uniformity goal remains open.

## Independent review

The entire proof was independently checked on paper by root, handoff_audit and literature_frontier. The review included the full theta weight versus quotient weight, the width-six factor, the finite primitive and its error, the exact rank and particular-solution coefficient, and the actual end-column factorial and marked functional. The three source comparisons retain the original curve and differential. No mathematical execution was performed.
