# R605 — The actual middle CM block is one characteristic-p coefficient

## 1. Statement and exact scope

Let $p\ge41$ be prime, $p\equiv5\pmod6$, and put $q=p^2$ and $e=q-1$.
We retain the actual $c_1$ character $\chi_6$, the averaged Cartan vector,
and all period and factorial conventions of R595 and the restored R588.
In particular, on

$$
E_0:y^2=x^3-1,\qquad \omega=\frac{dx}{2y},\qquad D=\frac d{dz},
$$

write

$$
\begin{aligned}
\Delta&=x^9-228x^6+48x^3-64,\\
R&=R_-=\frac{x^2(x^6+34x^3-8)}{\Delta},\\
B&=(-1)^{(p-1)/2-(p-2)/3}
       \binom{(p-1)/2}{(p-2)/3}\in\mathbf F_p^\times,\\
C_0&=72\sqrt3/\alpha,\qquad \alpha^3=4.
\end{aligned}
\tag{605.1}
$$

The specified $p$-adic embedding makes $\alpha\bmod p$ the unique cube root
of $4$ in $\mathbf F_p$. This is R595's $R_-$, which begins in degree two;
it is not R589's degree-four $c_0$ kernel $R_0$.

For the actual integral $\mu_e$-equivariant CM coordinate $Y$, define

$$
K_1=\frac p{C_0}[Y^{q+p-2}]H_2(Y)\pmod p,
\qquad
r_2=[z^{q-p}]R,\qquad
r_3=[z^{(p-1)(p-3)}]R\pmod p.
\tag{605.2}
$$

All three expressions are integral in their stated sense. We prove

$$
\boxed{K_1=-\frac{B^2}{4}\,r_2\pmod p.}
\tag{605.3}
$$

Together with the already proved $K_0=K_2=0$ in R601, this gives the
following exact version of the actual $c_1$ first-term criterion:

$$
\boxed{
\begin{aligned}
p^2S_2S_3&\equiv648B^5\alpha^{-2}r_2r_3\pmod p,\\
(pM_2)^2&\equiv5184\zeta^2B^5\alpha^{-2}r_2r_3\pmod p,\\
v_p(M_2)=-1&\quad\Longleftrightarrow\quad r_2r_3\ne0\pmod p.
\end{aligned}}
\tag{605.4}
$$

This removes the modulus-$p^2$ middle-block calculation and its delicate
subtraction from the residue computation. It does not prove $r_2r_3\ne0$
for every prime. In particular, it does not identify different tame points,
establish a global zero image, or replace an actual quadratic height by a
primitive CM coefficient.

## 2. An exact total second derivative of the complete kernel

Define two explicit rational functions

$$
W=\frac{yx^4(x^3+8)}{\Delta},\qquad
V=\frac{635x^6-136x^3+176}{12\Delta}.
\tag{605.5}
$$

In the differential ring with

$$
DE=-x,\qquad Dx=2y,\qquad Dy=3x^2,
\tag{605.6}
$$

the **complete** actual R595 kernel satisfies

$$
\boxed{\frac{H_2}{C_0}=D^2\mathcal U,\qquad
\mathcal U=\frac{E^2R}{4}+\frac{EW}{2}+V.}
\tag{605.7}
$$

Here $E$ is the same completed-zeta variable used in the actual translated
Kronecker sum. Its values at $p$-torsion and its formal primitive are
identified by the division-polynomial constant-term argument in R589;
it is not replaced by an independently selected primitive.

The identity (605.7) is over $\mathbf Q$, before reduction or coefficient
truncation. It can also be anticipated from the exact defining formula
$T_2=D^2S_3/12$, with $S_3=E^3-3Ex-y$, but the rational functions in (605.5)
have been determined and checked for the full actual tame sum.

For a directly reproducible verification, put

$$
N=x^2(x^6+34x^3-8),\quad P=x^4(x^3+8),\quad
L=635x^6-136x^3+176.
$$

For $f=N/\Delta$ one has

$$
D^2f=4(x^3-1)f''+6x^2f'.
\tag{605.8}
$$

The $E^2$, $Ey$, and constant coefficients of the right side of (605.7)
are compared to the full saved polynomials $A_2$, $A_1$, and $A_0$ in
R595(595.8)–(595.9), respectively. Clearing $12\Delta^3$ gives three
integer polynomial identities. The accompanying standard-library checker
performs these complete cross multiplications; all three remainders are
zero. It uses the recovered R595 JSON with SHA256
`63ddd30a930111684ec8595b8bb0f2d0bcb0b147543d0270b8d5f96972eb2501`.

This check also detects the transcription in the recovered display
R595(595.10): for $V_N=N'\Delta-N\Delta'$, the last term is
$6x^2V_N\Delta$, not $6x^2V_N\Delta'$. The explicit recovery erratum records
the old and corrected expressions and distinguishes the lost old checker
from the intact rational-kernel constructor. None of the saved kernel
coefficients changes.

## 3. The integral CM coordinate and the only derivative correction

The coordinate constructed in R595 has

$$
Y=z+v_qz^q+O(z^{2q-1}),\qquad v_p(v_q)\ge-1.
\tag{605.9}
$$

Consequently

$$
\rho(Y):=\frac{\omega}{dY}
=1+aY^e+O(Y^{2e}),\qquad a=-qv_q,\qquad v_p(a)\ge1.
\tag{605.10}
$$

The subsequent coefficients of $\rho$ are integral because $Y$ is an
integral parameter of the actual smooth formal elliptic curve.
The parameter is not assumed to be a flat integral coordinate in all
degrees. In particular, the possible valuation $-1$ of $v_q$ is retained.

At the origin, the actual functions in (605.7) satisfy

$$
R=Y^2+O(Y^8),\quad W=-Y+O(Y^7),\quad V\in Y^6\mathcal O[[Y]],
\quad E=Y^{-1}+\sum_{k\equiv5\ (6)}e_kY^k.
\tag{605.11}
$$

Thus $\mathcal U$ is a regular formal series, with constant $-1/4$.
R589's exact completed-zeta and Cartier argument gives
$v_p(e_k)\ge-v_p(k)$. Through degree $p+1$, at most one of the two $E$
factors can contribute a nonintegral positive term: its first such degree
is $p$, and two such degrees would exceed the coefficient under discussion.
It follows that

$$
v_p\bigl([Y^{p+1}]\mathcal U\bigr)\ge-1.
\tag{605.12}
$$

Put $n=q+p-2=e+p-1$ and $u_j=[Y^j]\mathcal U$. Since
$D=\rho^{-1}\partial_Y$, direct differentiation gives

$$
D^2\mathcal U
=\mathcal U''-a\bigl(2Y^e\mathcal U''+eY^{e-1}\mathcal U'\bigr)
+\text{terms irrelevant to degree }n.
\tag{605.13}
$$

Indeed every omitted term has an extra factor of degree at least $2e$;
even the two differentiations leave minimum possible degree $2e-2>n$.
Extracting the specified coefficient yields

$$
\begin{aligned}
p[Y^n]D^2\mathcal U
={}&p(n+2)(n+1)u_{n+2}\\
&-pa(p+1)(2p+e)u_{p+1}.
\end{aligned}
\tag{605.14}
$$

The second line has valuation at least $1+1-1=1$, by
(605.10) and (605.12). This proves exactly why the change of derivation
does not affect $K_1\bmod p$. No unit assertion is deleted, and no
nonintegral reparameterization is silently treated as integral.

## 4. Extraction of the sole surviving term

The full coordinate/Cartier argument in R589 gives, in the positive degree
range needed here,

$$
pE\equiv-BY^p\pmod p.
\tag{605.15}
$$

The range reaches $n+2=q+p<5q$. No exponent of $E$ divisible by $p^2$
can occur before $5q$, because its positive exponents are $5\pmod6$.
The pole term $pY^{-1}$ also vanishes modulo $p$. Thus the coefficientwise
reductions used below are integral and justified by the existing complete
primitive argument, not by a pointwise approximate value at torsion.

Since $R,W,V$ are integral Laurent expansions in $Y$ and the product
$\mathcal U$ is regular, (605.7) implies

$$
p^2\mathcal U\equiv\frac{B^2}{4}Y^{2p}R\pmod p
\quad\text{in the required coefficient range}.
\tag{605.16}
$$

The $EW$ term disappears because $pE$ is integral there, and the $V$ term
disappears immediately. On the other hand,

$$
p(n+2)(n+1)=p^2(p+1)(q+p-1),
\qquad(p+1)(q+p-1)\equiv-1\pmod p.
\tag{605.17}
$$

Equations (605.14)–(605.17) prove

$$
K_1=-\frac{B^2}{4}[Y^{q-p}]R\pmod p.
\tag{605.18}
$$

Finally $q-p<q$, and (605.9) makes the $Y$ and flat $z$ expansions of
the integral rational function $R$ identical through this degree.
This proves (605.3). The same argument works for every strict integral
$\mu_e$-equivariant coordinate used by R595.

Substituting (605.3) into R595's two actual norm congruences gives (605.4).
The factors $648$, $5184$, $B$, $\alpha$, and $\zeta$ are units at the
primes in the statement. If $r_2r_3=0$, the squared congruence gives only
the safe bound $v_p(M_2)\ge-1/2$ without an additional value-field theorem.

## 5. A common characteristic-p coefficient algorithm

Set $u=x^{-1/2}$ with $y=-u^{-3}\sqrt{1-u^6}$, $w=u^6$, and

$$
\begin{aligned}
C(w)&=(1-w)^{-1/2},\qquad
Z(w)=\sum_{k\ge0}\frac{\binom{2k}{k}}{4^k(6k+1)}w^k,\\
A(w)&=\frac{1+34w-8w^2}{1-228w+48w^2-64w^3},\qquad
\mathcal T(w)=\frac{Z(w^p)}{Z(w)}.
\end{aligned}
\tag{605.19}
$$

Then $z=uZ(w)$, $dz/du=C(w)$, and $R=u^2A(w)$. Changing variables in a
formal residue gives, in characteristic zero,

$$
[z^{2+6M}]R=[w^M]A(w)C(w)Z(w)^{-(3+6M)}.
\tag{605.20}
$$

This identity has no division by the target exponent. That is essential
for $r_2$, whose target exponent $p(p-1)$ is divisible by $p$.

Every coefficient of $Z$ below $L=(q-1)/6$ is integral. A denominator
$6k+1$ divisible by $p$ has low base-$p$ digit $(5p-1)/6>p/2$; the central
binomial numerator has the cancelling carry. The first uncancelled
denominator is at $k=L$, where $6L+1=q$. This is the exact integrality
argument already used in R595, and all cutoffs below are strictly below $L$.

Reducing (605.20) and applying Frobenius only in this integral truncation
gives

$$
\boxed{
\begin{aligned}
r_2&=[w^{M_2}]AC\,\mathcal T,&
M_2&=\frac{p^2-p-2}{6},\\
r_3&=[w^{M_3}]AC\,\mathcal T^4,&
M_3&=\frac{p^2-4p+1}{6}.
\end{aligned}}
\tag{605.21}
$$

For example, $Z^{-q+p-1}$ becomes $Z^{-1}Z(w^p)$ because the omitted
$Z(w^q)^{-1}$ equals one in the stated degree range. The second line is
the same previously defined actual $r_3$; it is not a newly selected
coefficient or character.

For comparison only, the actual $c_0$ coefficient in R589 has the equally
valid expression

$$
r'_p=[w^{(p^2-2p-3)/6}]
\frac{7+4w+16w^2}{1-228w+48w^2-64w^3}\,C(w)\mathcal T(w)^2.
\tag{605.22}
$$

Thus powers $1,2,4$ of the same formal Frobenius quotient occur. This
algebraic comparison alone makes no claim that the distinct $c_0$ and
$c_1$ points, their global quotients, or their candidate transports agree.

## 6. Actual new arithmetic and reproducibility

The complete identity (605.7) was actually executed first by exact rational
polynomial arithmetic and then by the separate standard-library integer
cross-multiplication checker included with this result. The latter checks
all coefficients, not selected point values.

One new, small coefficient computation was executed at $p=41$ to test
the precise new normalization:

$$
n=1640,\quad M_2=273,\quad r_2=24,\quad B=11,
\quad-\frac{B^2r_2}{4}=12\pmod{41}.
\tag{605.23}
$$

The value $12$ agrees with the independently retained historical $K_1$
from R595. The new computation uses exact integer central binomial
coefficients, solves the direct quotient equation $QZ=AC$, and takes the
seven terms of the final sparse $Z(w^{41})$ convolution. Its certificate
records each summand, all indices at which a denominator is cancelled,
the coefficient-vector hash, and the exact largest accumulated integer
dot product. It does not rerun the old torsion orbit or the old middle
block. No finite prime grid was made.

For a portable replay from the topic directory:

```bash
python scripts/verify_R605_total_second_derivative.py
python scripts/R605_r2_coefficient.py --prime 41 --output /tmp/R605_r2_prime41-recheck.json
```

The former needs only the recovered R595 coefficient JSON; both scripts
use Python's standard library. The symbolic discovery script is retained
as a working artifact, but is not required for these replays.

The genuine remaining arithmetic question is whether, or under which
additional explicit hypotheses, the two actual coefficients in (605.21)
are nonzero in the original remaining classes $p\equiv2,5\pmod9$.
Nothing here calls the unrelated old $p=719$, $k=215$ channel a failure of
this criterion. The already verified $p=269$ minimum belongs to the
broader local theorem and has $269\equiv8\pmod9$.
