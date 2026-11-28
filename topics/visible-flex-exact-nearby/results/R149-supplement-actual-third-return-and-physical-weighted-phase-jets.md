# R149 ASQ7. The actual third return derivative and two physical phase-inverse jets

**Proved on the complete two-leg domain of RPT.** The physical
coefficient $B$ in ASQ6 contains the derivative of the return in the
actual NP metric direction. Twice differentiating that coefficient
requires a third return variation. This result proves the required
trilinear estimate on the original radial $L^2$ directions and closes
the composition, denominator and moving-data chain rules. We use the
constants, directions $N_s$ and backgrounds $B_s$ of
[RPT.1–4,25–33](R144-supplement-all-angular-principal-return-tame-derivatives.md).
Only the strong backgrounds belong to the nonlinear value domain.

## A third actual coefficient and transport derivative

Write $I=\partial_\phi^{-1}P_{\ne0}$ and $c=\gamma\sqrt{-K}$ as in
[RP.5,13–17](R144-supplement-full-off-constraint-principal-return-Hessian.md).
For mixed derivatives in three independent affine physical directions
$i=1,2,3$ put $x_i=(h_i,k_i)$ and $k_A=\prod_{i\in A}k_i$.
For $D=\{1,2,3\}$ the third field derivative on a leg before its
chronological sign is exactly
$$
 \sum_{A\subset D} k_A
 \big[\beta K^{(|A|)} I\,\partial_{D\setminus A}(v^2)
       -\sigma c^{(|A|)}\partial_{D\setminus A}\langle v\rangle\big] .
 \tag{ASQ7.1}
$$
The superscripts are intrinsic parameter derivatives. In the two
derivatives after them only $v$ varies affinely by $h_{i,2}$.
In particular the state--state entry of $v^2$ is $2h_{i,2}h_{j,2}$.
The other quadratic drift $\beta I(u^2)$ has zero third variation.
In the speed the genuine state mean and its first variations remain.

On the original support $C=[1/20,9/50]$, $c^2$ is affine in the
metric parameter, so $c'''=3(c')^3/c^2$, and RP gives
$|c'''|<12(47)^3<2^{21}$. Also
$|\beta K'''|<12$ by
[TH.12–14](R144-supplement-complete-low-norm-tame-Hessian-and-mean-preserving-smoothing.md).
Off $C$ all intrinsic derivatives vanish before any root division.
Since (ASQ7.1) contains at least one such derivative in every
nonzero summand, it produces no extra root source or jump.

Let $A_D(n)$ denote a majorant for $\int\|\partial_DW\|_{H^n}dt$
with RPT's reversed chronological $W$. For one and two labels take
the respective right sides of RPT.18. For three take
$$
 A_D(n)=2^{n+40}\left[
   (1+B_{\max(n,1)})\prod_i N_1(x_i)
   +\sum_i N_{\max(n,1)}(x_i)\prod_{j\ne i}N_1(x_j)\right].
 \tag{ASQ7.2}
$$
Here is a direct ledger. In a $v^2$ term place the high angular
derivative on either of its two factors by RPT.19. Background low
factors cost at most $10$, low direction Wiener factors at most
$2N_1$ after the radial norm. The primitive costs at most one.
There are at most eight subsets, a multiplicity at most two from
$v^2$, and at most two product terms per subset. With two radial
direction factors use Cauchy--Schwarz on the original radius and
pay the folding factor two. With one factor use $2\sqrt{r_*}<1$,
and with none use $2r_*<1$. Each metric scalar is at most $N_1$
in its original units. For the speed there are at most four nonzero
terms, and the state mean costs its full $L^2$ norm. Thus even
$2^n\cdot 2^{21}\cdot 8\cdot2\cdot2\cdot 2\cdot 10^2\cdot 2^2$
fits $2^{n+40}$. No product of three arbitrary radial $L^2$ functions
ever enters the source.

Write $p$ for the full transported label, $z_A=\partial_A p$ for
nonempty $A$, and $z_\varnothing=p$. Differentiating the original
transport gives, with the same zero initial data for nonempty $D$,
$$
 (\partial_t+W\partial_\phi)z_D
      =-\sum_{\varnothing\ne A\subset D}W_A\partial_\phi z_{D\setminus A}.
 \tag{ASQ7.3}
$$
This keeps all three mixed two--one and all three one--two contributions.
There is no derivative of the radial endpoint because the actual metric
control fixes $r_*$. Intermediate flow times are included.

Here are explicit constants. Use $V_\varnothing(j)=R_{j+1}B_{j+1}$
to bound $p_\phi$ in $H^j$. For $1\le |A|\le2$, let $V_A(j)$
be the corresponding right side of RPT.27 or RPT.31 at order $j+1$.
It bounds $\partial_\phi z_A$ in $H^j$ uniformly in time.
For integer $n\ge1$ define
$$
 S_D(n)=C_n\sum_{\varnothing\ne A\subset D}
    [A_A(n)V_{D\setminus A}(1)+A_A(1)V_{D\setminus A}(n)],
 \qquad M_D(n)=K_n[S_D(n)+B_n S_D(1)] .
 \tag{ASQ7.4}
$$
Here $C_n=(9/8)2^{n-1}$. PD.17 and RPT.12 prove
$\sup_t\|z_D\|_{H^n}\le M_D(n)$. For $n=1$ the enlarged
formula also follows from RPT's direct $H^1$ bound. It covers $n=0$
by monotonicity. This is a finite positive rational recurrence in
the stated data.

For clarity the apparent two-high factors in this recurrence have a
one-high bound with no new low background gate. Let $L_n$ be (ASQ7.4)
evaluated at $B_j=2^{25}$ and every $N_j(x_i)=1$, including
(ASQ7.2) and the cited RPT formulas. For $n\ge1$,
$$
 \|D^3P[x_1,x_2,x_3]\|_{H^n}
 \le L_n\left[
 (1+B_{n+3})\prod_i N_5(x_i)
 +\sum_i N_{n+5}(x_i)\prod_{j\ne i}N_5(x_j)\right].
 \tag{ASQ7.5}
$$
To check this reduction, count in each monomial of (ASQ7.4) the sum
of $(j-3)_+$ over its background factors $B_j$ and of $(j-5)_+$
over its direction factors $N_j$. Its total is at most $n$.
Indeed $|A|=3$ has $p_\phi$ of orders at most $B_{n+1}$ or $B_2$;
$|A|=2$ has $V_1(1)$ using at most $B_3,N_2$, or
$V_1(n)$ using $B_{n+2},N_{n+1}$. For $|A|=1$ the low
$V_2(1)$ uses $B_4,N_5$, so the costly product adds just one to
$(n-3)_+$ or $(n-5)_+$. Its high $V_2(n)$ uses
$B_{n+3},N_{n+4}$ and the multiplying $A_1(1)$ is low.
Finally the cost of $S_D(1)$ is at most one, also in $B_n S_D(1)$.
Each monomial is linear in the norm profile for each of the three
directions. Zero directions give zero. Otherwise interpolate
$B_j$ between $B_3,B_{n+3}$ and each $N_j$ between
$N_5,N_{n+5}$ by log convexity. The high ratios occur with total
power at most one, so weighted AM--GM is bounded by one plus their
sum. Use $B_3\le2^{25}$ in the low factors and $B_3\ge1$ in the
high ratio. This proves (ASQ7.5), with all constants outside the high
norms. The variation is obtained on smooth directions by the real
chronological transport and its three variational equations; the
same integral and multilinear bound extends it by angular density.
For differentiation of the value map use strong backgrounds along
the full admissible segment, as for RPT.34.

## Composition at the true lift

All remaining estimates can use the following elementary composition
bound on the original fourfold circle. Suppose $g'>c>0$ and put
$G=\max(1,(9/8)\|g'\|_{H^1})$. For $n\ge1$ write
$$
 U_n(f,g)=c^{-1/2}2^{n/2}\operatorname{Bell}(n)G^n
     [\|f\|_{H^n}+(1+\|g'\|_{H^n})\|f\|_{H^1}].
 \tag{ASQ7.6}
$$
Then $\|f\circ g\|_{H^n}\le U_n(f,g)$ for periodic $f$.
The normalized order-zero estimate is $c^{-1/2}\|f\|_2$.
For each derivative of order $1\le r\le n$, the partition formula
contains at most $\operatorname{Bell}(n)$ terms counted with
multiplicity. A partition into $k$ blocks of sizes $j_i$ gives
$(f^{(k)}\circ g)\prod (g')^{(j_i-1)}$. The first factor costs
$c^{-1/2}\|f\|_{H^k}$ in $L^2$, and the others cost
$(9/8)\|g'\|_{H^{j_i}}$ in $L^\infty$. Interpolate between 1 and
$n$ separately for $f$ and $g'$. The sum of high exponents is
$[(k-1)+\sum(j_i-1)]/(n-1)=(r-1)/(n-1)\le1$. The resulting
low constants are bounded by $G^n$: indeed $\|g'\|_{H^1}\ge1$
for a degree-one lift. Weighted AM--GM gives (ASQ7.6), and the
integer Bessel square is the binomial sum of squared derivative
norms with sum of coefficients $2^n$. For $n=1$ use the ordinary
chain rule with $\|g'\|_\infty\le G$ directly. The constant
displacement of $g$ is included through the actual composition.

For ratios at positive real $J$ one can use an explicit reciprocal
bound in the same norms. If $J\ge c>0$, $n\ge1$, put
$G_J=\max(1,(9/8)\|J\|_{H^1})$, $a_J=\max(1,c^{-1})$. Then
$$
 \|1/J\|_{H^n}\le
 2^{n/2}\operatorname{Bell}(n)n!\,a_J^{n+1}
 G_J^n[1+(9/8)\|J\|_{H^{n+1}}].                     \tag{ASQ7.7}
$$
Indeed $|(1/t)^{(k)}|\le k!a_J^{k+1}$ on $t\ge c$; each
$J^{(j)}$ costs $(9/8)\|J\|_{H^{j+1}}$ in sup norm.
Interpolate the latter between orders $1,n+1$: total high power
$r/n\le1$. This proves the claimed bound, including order zero.
The same proof for $\log m$ uses $(k-1)!\max(1,\inf(m)^{-1})^k$
for $k\ge1$, plus its actual real zero-derivative sup bound
$\max(|\log\inf m|,|\log\sup m|)$. In ASQ6 the low $H^2$
logarithm gate is still checked on the whole residual.

## The actual physical mixed jet

For any state-dependent periodic function $A$, write its *physical*
jets before composition as $A_i,A_{ij}$ and denote spatial
derivatives by primes. The complete mixed jet of $A\circ g$ is
$$
 A_{ij}\circ g+(A_i'\circ g)g_j+(A_j'\circ g)g_i
 +(A''\circ g)g_i g_j+(A'\circ g)g_{ij}.                 \tag{ASQ7.8}
$$
The first jet is $A_i\circ g+(A'\circ g)g_i$.
For the numerator of $m$, take $A=P'$, and then multiply by $g'$,
including $g'_i,g'_j,g'_{ij}$ in its ordinary product rule.
Here $A_i=(DP[x_i])'$, and
$A_{ij}=(D^2P[x_i,x_j]+DP[x_{ij}])'$. The constant part of $P'$
comes from the degree-one term. For either $N_B$ or the return term
in $N_F$ of [ASQ6.8](R149-supplement-off-conjugacy-full-weighted-phase-and-physical-recovery.md),
take $A=DP[Z]$, with $Z=(h^a,1)$ or $Z=(z,0)$ respectively. Then
$$
 \begin{aligned}
 A_i={}&D^2P[x_i,Z]+DP[Z_i],\\
 A_{ij}={}&D^3P[x_i,x_j,Z]+D^2P[x_{ij},Z]
        +D^2P[x_i,Z_j]+D^2P[x_j,Z_i]+DP[Z_{ij}].
 \end{aligned}                                           \tag{ASQ7.9}
$$
Here $x_{ij}$ includes the actual second coordinate variation. The
fixed trial itself has $Z_i=0$ in fixed raw coordinates; passive
lifts are differentiated when they vary. For $N_F$ the full
$b_i,b_{ij}$ and independent external sources enter with their raw
signs. Use ASQ6.8 to divide, charging $J_i,J_{ij}$; use ASQ6.6–7
for the inverse and $\delta g=g'a$ with its product derivatives
for physical recovery. For the phase residual itself, (ASQ7.8) with
$A=P-\mathrm{Id}$ plus $g-g\circ R$ gives the complete RP.27
and its moving-coordinate corrections. In an affine chart its
quadratic integral is at most half the supremum of ASQ7.8 with
$i=j$, by Taylor. This uses actual both-leg $D^2P$ at every point
of the segment.

These formulas give explicit physical norm bounds: for every atomic
$P-\mathrm{Id},DP,D^2P,D^3P$ use RPT.32, RPT.33, ASQ7.5; a spatial
prime raises the index by one. Use (ASQ7.6) for each composed atom,
(ASQ7.7) for every reciprocal, PD.17 for each product, and the sum
for each plus or minus. The formulas form a finite recurrence for
any requested integer output order. For example the most demanding
atom of $A_{ij}$ for $A=DP[Z]$ in $H^r$ requires the true
$N_{r+5}$ of these three directions and $B_{r+3}$; the $A''$ atom
requires $N_{r+2},B_{r+3}$. The coefficient inverse differentiations
then take the progressively shifted orders in ASQ6.6–7. All costs
are one-high products over the displayed low windows, which may
contain genuine higher *low* norms of the lift, external input or
directions. The tiny CP.13 value ball does not bound arbitrary
such high norms. RP.29 remains the sharper actual low Hessian.

Changing to a physical waist-angle lift uses the entire RP.28
secant. A state-dependent output normalizer retains its $D^2O\,r$
and both $DO\,Dr$ terms, and a varying regular solution contributes
the $Z_i,Z_{ij}$ in (ASQ7.9). The estimate closes the two physical
jets of the phase inverse on their specified strong data. It does
not give second derivatives of an unknown full regular inverse or
bound unrelated cap or holonomy residuals.
