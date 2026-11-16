# R855 — A unit in an original primitive higher Abel block for every sufficiently large allowed prime

Date: 2026-11-16. Session: serre-public-astra-20261115 / sigma_uniform.

**Status: proved.** For every prime $p>104190883$ with $p\equiv2,5\pmod9$, one of two explicitly specified original primitive embeddings has a higher flat jet $M_{m,h}$ satisfying $v_p(M_{m,h})=-m$. The three unit factors occur at the same actual pair $(m,h)$. The order $m$ grows with $p$; this does not assert the fixed $m=2$ criterion, a unit first height coefficient, or completion of Serre uniformity.

## 1. Original objects and statement

Retain the positive cubic quotient, original $c_1$ marking, actual Cartan average, split vector, and absolute Hodge normalization of R575/R588/R592. The notation $M_{m,h}$ has exactly the meaning of R727: it is the flat jet for the coefficient embedding
$$
\theta_h=\theta_{-1}^{\,h},\qquad
\theta_h(y)=[y]^{-h(p-1)}.
\tag{855.1}
$$
The elliptic coordinate in the finite kernels is separately
$$
E_0:y^2=x^3-1,\qquad dz_{\rm ell}=\frac{dx}{2y},\qquad
D=\frac d{dz_{\rm ell}}.
$$
It is not the flat modular deformation coordinate $z_{\rm f}$ in $M_{m,h}$.

Write
$$
n=p+1=6M,\qquad
e=\begin{cases}1,&p\equiv2\pmod9,\\2,&p\equiv5\pmod9,\end{cases}
\qquad k_p=2(3-e)M.
\tag{855.2}
$$
For each $a\in\{0,2\}$, set
$$
\ell_a=6a+5,\qquad m_a=eM-3a-3,
$$
$$
h_a=\begin{cases}
(6-e)M-3a-3,&eM\text{ even},\\
eM+3a+2,&eM\text{ odd}.
\end{cases}
\tag{855.3}
$$
The second case necessarily has $e=1$ and $M$ odd. All these indices are integers in the actual permitted ranges, and
$$
m_a\equiv2\pmod3,\qquad
7\le h_a\le p-4,\qquad h_a\equiv1\pmod6,
\qquad (h_a,p+1)=1.
\tag{855.4}
$$
The theorem is
$$
\boxed{\text{For at least one }a\in\{0,2\},\quad
v_p(M_{m_a,h_a})=-m_a.}
\tag{855.5}
$$
Here and below $v_p(p)=1$. The threshold is a deliberately coarse sufficient bound from three fixed rational Legendre obstructions; no finite prime computation is involved.

More precisely, both candidates have
$$
C_{h_a-m_a},\ C_{p-h_a-m_a}\in\mathbf Z_p^\times,
\tag{855.6}
$$
and at least one of their original finite norms $N_{h_a}$ is a unit. For that same candidate the complete finite Fourier sums and exact original toric norm prove (855.5).

## 2. A general higher-block identity with its full tail

We first prove the needed extension of R705 and R727. Suppose
$$
2\le m\le p-3,\qquad m\equiv2\pmod3,
\qquad h\equiv1\pmod6,\qquad (h,p+1)=1,
$$
$$
k_1=h-m\ge2,\qquad k_2=p-h-m\ge2.
\tag{855.7}
$$
In particular $7\le h\le p-4$, and $k_1,k_2\le p$, with both indices congruent to $2$ modulo $3$.

Use the original constants and rational function
$$
C_0=72\beta/\alpha,\quad \alpha^3=4,\quad\beta^2=3,
\quad C_0^2=15552/\alpha^2,
$$
$$
B=(-1)^{(p-1)/2-(p-2)/3}
\binom{(p-1)/2}{(p-2)/3}\in\mathbf F_p^\times,
$$
$$
R_-=\frac{x^2(x^6+34x^3-8)}{x^9-228x^6+48x^3-64},
\qquad
\mathfrak r_k=[z_{\rm ell}^{(p-1)k}]R_-\pmod p.
\tag{855.8}
$$
For a positive integer $k$, write $(k)_r=k(k+1)\cdots(k+r-1)$. We claim the integral square identity
$$
\boxed{
(p^mM_{m,h})^2\equiv
-\frac{864\zeta^2}{\alpha^2}\,
N_hB^{2m+1}(k_1)_m(k_2)_{m+1}
\mathfrak r_{k_1}\mathfrak r_{k_2}\pmod p.
}
\tag{855.9}
$$
All displayed factors outside $N_h$ and the two $\mathfrak r$'s are units. Formula (855.9) includes growing $m$, the full inverse-sigma contribution, and all Fourier blocks.

### 2.1. Exact norm at the same embedding and weight

Use R705's original complete kernels
$$
H^-(P,v)=\sum_Q\chi_6(Q)^{-1}\Theta_Q(P,v),\qquad
H_r(P)=[u^rv^r]H^-(P+u,v),
$$
$$
S_{m,h}=-\sum_b\theta_h(b)H_m(P_b),\qquad
S_{m+1,h}=-\sum_b\theta_h(b)^{-1}H_{m+1}(P_b).
\tag{855.10}
$$
The exact identity is
$$
M_{m,h}\overline{M_{m,h}}
=\frac{[m!(m+1)!]^2N_h}{18(p+1)^2}
S_{m,h}S_{m+1,h},\qquad
\overline{M_{m,h}}=-\zeta M_{m,h}.
\tag{855.11}
$$
This combines the actual permitted-weight extension in R705 §2 with the actual coefficient-embedding argument in R727 §2. Here is why both extensions apply together. The two Hecke characters are
$$
a^{2m+1}\chi_6(a)\theta_h(a)^{-1},\qquad
a^{2m+3}\chi_6(a)\theta_h(a).
$$
Since $h\equiv1\pmod6$, the values of $\theta_h$ on $\zeta$ and $\sqrt{-3}$ are the original ones. The unit condition remains $\zeta^{2m+2}=1$. Raising $m$ by three changes no finite unit character or tame projection. The local factors at $2$ and $3$ are therefore still $2/3$ and $1/(3\sqrt3)$, respectively; the ramified odd-valuation coset at $3$ remains outside the support. The primitive local factor at $p$ is exactly $N_h/(p+1)^2$, as in R727, without replacing $N_h$ by $-1$. The archimedean factor and the flat-coordinate cancellation are the general-$m$ formulas already retained in R705 §2. They give the two factorials in (855.11).

The same finite reflection interchanges $\theta_h$ and its inverse and sends the original tame vector to $-\zeta$ times itself. The raising operator commutes with that reflection, and the relevant power $(2\pi i/\Omega)^{2m+2}$ is real. Thus the second equality in (855.11) is the same algebraic conjugation identity. It makes no assertion that complex conjugation fixes a selected $p$-adic place. Consequently
$$
M_{m,h}^2=-\zeta^2M_{m,h}\overline{M_{m,h}}.
\tag{855.12}
$$

### 2.2. Integral rational coefficients and the uniform budget

Let $Y$ be the original integral CM parameter, $q=p^2$, $\varepsilon=q-1$, and $\varpi=Y(P_1)$. R589/R595/R705 give
$$
v_p(\varpi)=1/\varepsilon,\qquad
\varpi^\varepsilon/p\equiv1\pmod p,
$$
$$
\rho=\omega/dY=1+\sum_{j\ge1}a_jY^{j\varepsilon},
\quad a_j\in\mathcal O,\quad v_p(a_1)\ge1,
\quad Y=z_{\rm ell}+O(z_{\rm ell}^{q}).
\tag{855.13}
$$
The completed primitive $E$ satisfies $DE=-x$. In $H_r$, its powers have degree at most $r$, their rational coefficients are integral for $r\le p-2$, and
$$
[E^r]H_r=\frac{C_0D^rR_-}{(r!)^2}.
\tag{855.14}
$$
These are R705 (705.11)--(705.13), including every inverse-sigma term. Their pole budgets and the original primitive coefficient estimate give, for all $t\ge0$,
$$
v_p([Y^t]H_r)\ge
-r-\left\lfloor\frac{t+2r-2}{5p^2}\right\rfloor,
\qquad 1\le r\le p-2.
\tag{855.15}
$$
This is precisely R705 (705.16). In particular it is uniform when $r$ grows with $p$; no fixed-order denominator estimate is substituted for it.

For the first sum put $r=m$, $b_0=h(p-1)$, $k=k_1$. For the second put $r=m+1$, $b_0=(p+1-h)(p-1)$, $k=k_2$. In either case
$$
0<b_0<\varepsilon,\qquad b_0-pr+r=(p-1)k.
\tag{855.16}
$$
The complete corresponding Fourier sum is
$$
S_{r,h}^{\rm side}
=-\varepsilon\sum_{j\ge0}[Y^{b_0+j\varepsilon}]H_r\,
\varpi^{b_0+j\varepsilon}.
\tag{855.17}
$$
For every $j\ge1$, since $r\le p-2$,
$$
b_0+j\varepsilon+2r-2<(j+2)p^2.
$$
Thus (855.15) bounds the valuation of that block after the scaling $p^r/\varpi^{b_0}$ from below by
$$
j-\left\lfloor\frac{j+1}{5}\right\rfloor\ge1.
\tag{855.18}
$$
It tends to infinity. This controls every discarded block of both sums, including arbitrarily high primitive denominators.

### 2.3. The first block, including derivative factors

For $j=0$ the positive primitive indices required by the budget are below $b_0+2r-2<2p^2$. R589 (589.17) proves, throughout the larger exact range of positive exponents below $5p^2$,
$$
pE\equiv-BY^p\pmod p.
\tag{855.19}
$$
Multiplying $H_r$ by $p^r$ therefore kills all powers $E^a$ with $a<r$, and the first block becomes
$$
\frac{p^r}{C_0}[Y^{b_0}]H_r
\equiv\frac{(-B)^r}{(r!)^2}
[Y^{b_0-pr}]D^rR_-.
\tag{855.20}
$$
There is no hidden $p!$ division: $r\le p-2$.

The first correction from $D=\rho^{-1}\partial_Y$ to $\partial_Y$ has degree shift $\varepsilon$. Since $\operatorname{ord}_O R_-=2$, the correction in $D^rR_-$ starts at degree at least $\varepsilon+2-r$, whereas the required index $b_0-pr$ is smaller. Consequently $D^r$ can be replaced by $\partial_Y^r$ at this particular coefficient. Its source index is $(p-1)k<q$, so (855.13) also identifies the source coefficient with the original $\mathfrak r_k$.

The falling-factorial contribution is
$$
((p-1)k)_{\underline r}\equiv(-1)^r(k)_r\pmod p.
$$
Together with (855.20), this gives the exact positive sign
$$
\frac{p^r}{C_0}[Y^{b_0}]H_r
\equiv\frac{B^r(k)_r}{(r!)^2}\mathfrak r_k\pmod p.
\tag{855.21}
$$
All factors in $(k)_r$ lie strictly between zero and $p$: their largest values are $h-1$ and $p-h$ for the two sides.

Combining (855.17)--(855.21), multiplying the two sides, and using $b_0^{(1)}+b_0^{(2)}=\varepsilon$ and $\varpi^\varepsilon/p\equiv1$, yields
$$
\frac{p^{2m}S_{m,h}S_{m+1,h}}{C_0^2}
\equiv
\frac{B^{2m+1}(k_1)_m(k_2)_{m+1}}
{(m!)^2((m+1)!)^2}
\mathfrak r_{k_1}\mathfrak r_{k_2}\pmod p.
\tag{855.22}
$$
Both normalized individual sums used here are integral, regardless of whether their displayed reductions vanish. Equations (855.11)--(855.12), $\varepsilon^2\equiv1$, $(p+1)^2\equiv1$, and $C_0^2/18=864/\alpha^2$ prove (855.9), including its integrality.

As a sign check within the proved formula, at $m=2$ the product of rising factors is
$$
(h-2)_2(p-h-2)_3\equiv
-(h-2)(h-1)h(h+1)(h+2),
$$
so (855.9) is exactly R727 (727.6).

## 3. The two Cartier factors are actual units

R683's full six-torsion comparison applies in the complete range used above:
$$
\mathfrak r_k=c(-3B)^{-(k-1)}C_k,
\qquad c=(3/p)\alpha^2/2,
\qquad 2\le k\le p,\quad k\equiv2\pmod3.
\tag{855.23}
$$
Here $B$, $c$, $\alpha$, and $3$ are units. R851 proves the original individual assertion
$$
C_{k_p}\in\mathbf Z_p^\times\qquad(p\ge257).
\tag{855.24}
$$
The other two indices are $5$ and $17$. To display their normalization without an auxiliary calculation, write the original function as
$$
F=x\sigma^6=z_{\rm ell}^{4}\sum_{i\ge0}f_i z_{\rm ell}^{6i}.
$$
The original curve equation and $D^2x=6x^2$ give
$$
x=z_{\rm ell}^{-2}+\frac{z_{\rm ell}^4}{7}
+\frac{z_{\rm ell}^{10}}{637}+O(z_{\rm ell}^{16}).
$$
Integrating $D^2\log\sigma=-x$ in the canonical $c=0$ normalization gives
$$
\log(\sigma/z_{\rm ell})
=-\frac{z_{\rm ell}^6}{210}
-\frac{z_{\rm ell}^{12}}{84084}+O(z_{\rm ell}^{18}).
$$
Therefore
$$
f_0=1,\qquad f_2=
\frac1{637}-\frac1{245}+\frac1{2450}-\frac1{14014}
=-\frac{381}{175175}
=-\frac{3\cdot127}{5^2\cdot7^2\cdot11\cdot13}.
\tag{855.25}
$$
These are paper expansions of the original functions, with no change of Gaussian or period. R697 (697.2)--(697.3), equivalently the odd branch of R770 (770.9), gives
$$
C_{6a+5}=3\,2^{-(6a+4)}(6a+4)!\,f_a^2.
\tag{855.26}
$$
Hence $C_5=9/2$ and $C_{17}$ are units for every $p\ge257$.

For either $a$ in (855.3),
$$
2m_a+k_p+\ell_a=p,
$$
and the two possible orientations are $m_a+\ell_a$ and $m_a+k_p$. They add to $p$, so exactly one is odd. Formula (855.3) chooses precisely that odd one. Consequently
$$
(h_a-m_a,p-h_a-m_a)=
\begin{cases}(k_p,\ell_a),&eM\text{ even},\\
(\ell_a,k_p),&eM\text{ odd}.
\end{cases}
\tag{855.27}
$$
Equations (855.24)--(855.27) prove (855.6). They retain the same $a$, $m_a$, and $h_a$ throughout; no coefficient from one candidate is paired with the finite norm of the other.

## 4. Legal ranges and genuine primitivity

From the allowed residue classes, $eM\equiv2\pmod3$. Thus $m_a\equiv2\pmod3$, and both orientations above are $1$ modulo $3$. Selecting the odd one makes $h_a\equiv1\pmod6$.

For $p\ge257$, $M\ge43$ and
$$
2\le m_a\le2M-3<p-3,
\qquad 7\le h_a\le p-4.
\tag{855.28}
$$
The factorials $m_a!,(m_a+1)!$ and all rising factors in (855.9) are accordingly units. The two Cartier indices in (855.27) are at least two and strictly less than $p$.

If $eM$ is even, any common divisor of
$$
h_a=(6-e)M-3(a+1),\qquad 6M
$$
divides $18(a+1)$. Here $a+1$ is $1$ or $3$, and $h_a$ is coprime to $6$, so that common divisor is one. If $eM$ is odd, then $e=1$, $M$ is odd, and $h_a=M+(3a+2)$. A common divisor with $6M$ divides $6(3a+2)$; for $a=0,2$ the latter additional factors are $2$ and $8$. Again $h_a$ is coprime to $6$, so the common divisor is one. This proves the full primitivity assertion, not merely the congruence $h_a\equiv1\pmod6$.

## 5. At least one of these same two finite norms is a unit

R727 gives, in the fixed original period basis and split vector,
$$
N_h\equiv-P_{h-1}(x)^2\pmod p,
\qquad x=1/\sqrt{-3},\quad x^2=-1/3.
\tag{855.29}
$$
The two labels (855.3) differ by six. Put $d$ equal to the smaller of their two Legendre degrees. The bounds above imply $1\le d$ and $d+6<p$.

R734 (734.7)--(734.11) proves that $P_d(x)$ and $P_{d+6}(x)$ cannot both vanish unless
$$
U_5(d)=\frac{x}{9}(2d+7)
\left(91[d(d+7)]^2+1800d(d+7)+8748\right)=0.
\tag{855.30}
$$
Indeed, if $P_d=0$, then $P_{d-1}\ne0$ by downward Legendre recurrence, and
$$
P_{d+6}=-\frac{dU_5(d)}{(d+1)\cdots(d+6)}P_{d-1}.
$$
Every displayed denominator is a unit in our range.

Since $M\equiv1/6\pmod p$, the three possible substitutions are as follows. In the last column $Q(r)=91r^2+1800r+8748$.

| Case | Exact lower degree $d$ | $d\bmod p$ | $2d+7\bmod p$ | $r=d(d+7)\bmod p$ | $Q(r)\bmod p$ |
|---|---:|---:|---:|---:|---:|
| $e=2$ | $4M-10$ | $-28/3$ | $-35/3$ | $196/9$ | $7379644/81$ |
| $e=1$, $M$ even | $5M-10$ | $-55/6$ | $-34/3$ | $715/36$ | $104190883/1296$ |
| $e=1$, $M$ odd | $M+1$ | $7/6$ | $28/3$ | $343/36$ | $44269867/1296$ |

For completeness, the three integer numerators are the direct identities
$$
\begin{aligned}
91\cdot196^2+1800\cdot196\cdot9+8748\cdot81
&=3495856+3175200+708588=7379644,\\
91\cdot715^2+1800\cdot715\cdot36+8748\cdot1296
&=46521475+46332000+11337408=104190883,\\
91\cdot343^2+1800\cdot343\cdot36+8748\cdot1296
&=10706059+22226400+11337408=44269867.
\end{aligned}
\tag{855.31}
$$
Thus for $p>104190883$, all factors in (855.30) are units, including $x$, $2d+7$, and $Q(r)$. Both Legendre values cannot vanish. By (855.29), at least one of these exact two primitive labels has $N_{h_a}\in\mathcal O^\times$.

## 6. Conclusion and the remaining original target

Choose the candidate furnished by §5. Both of its Cartier factors are units by §3, and (855.23) transports them to the two original $\mathfrak r$'s. All other factors of (855.9) are units by §4. The integral left side of (855.9) therefore has nonzero reduction. This proves $v_p(M_{m_a,h_a})=-m_a$ and hence (855.5).

In the original scalar Abel primitive, the exact flat coefficient in question is
$$
\mathcal I_h(z_{\rm f})
=\sum_{j\ge1}\frac{M_{3j-1,h}}{(3j)!}z_{\rm f}^{3j},
\qquad j_a=\frac{m_a+1}{3},
$$
$$
v_p\!\left(\frac{M_{m_a,h_a}}{(m_a+1)!}\right)=-m_a.
\tag{855.32}
$$
The factorial here is still a unit. On the actual fine scaled coordinate $z_{\rm f}/\lambda$ of R592, where $v_p(\lambda)=p/(p+1)$, the corresponding coefficient has the exact valuation
$$
v_p\!\left(\frac{\lambda^{m_a+1}M_{m_a,h_a}}{(m_a+1)!}\right)
=1-\frac{m_a+1}{p+1}.
\tag{855.33}
$$
This is a coefficient of the actual original scalar primitive, not of an auxiliary elliptic-coordinate series. Passage to a chosen invariant quotient differential retains the one nonzero comparison scalar $c_h$ of R727 (727.29); its valuation must be added and is not asserted to vanish.

The statement has a varying positive order $m_a$, generally much larger than two. It neither supplies $C_{h-2}C_{p-h-2}$ at that label nor makes the high coefficient the first nonzero coefficient. It also does not show that this coefficient dominates all earlier or later terms on the candidate coarse disc. The original height normalization and its linear term remain separate. Thus the fixed $m=2$ same-label three-unit problem and the actual rational-point/height exclusion remain open.

## References within the original chain

- [R705](R705-actual-higher-Abel-blocks-and-uniform-order-bound.md), §§2--5 and §§7--8: permitted higher weights, complete rational kernels, uniform denominator budget, original flat scale.
- [R727](R727-other-primitive-embeddings-toric-norm-and-original-M2.md), §§1--2, §§7--9: actual primitive embeddings, finite norm, conjugation, and quotient differential comparison.
- [R734](R734-primitive-unit-toric-norm-at-every-prime.md), (734.7)--(734.11): exact six-step Legendre recurrence.
- [R683](R683-even-weight-Cartier-channel-and-actual-r3.md): original full six-torsion Cartier comparison.
- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md), (697.2)--(697.3): original sigma square formulas.
- [R851](R851-original-cubic-central-value-and-third-position-Cartier-unit.md): the specified individual $C_{k_p}$ unit for every allowed $p\ge257$.

No new mathematical computation was executed. The finite integer expansions in (855.25) and (855.31) are displayed paper identities; all infinite tails are controlled by (855.15)--(855.18).
