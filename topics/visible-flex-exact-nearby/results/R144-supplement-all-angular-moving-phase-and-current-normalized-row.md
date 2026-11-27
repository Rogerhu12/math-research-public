# R144 PCT: full moving-phase tame map and current normalized linear row

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved.** This supplies every integer angular order of the actual raw
phase map, its first derivative and full Hessian, and of the first
background derivative of PD's current left-normalized linear row.
The full constant phase, the true parameter, both characteristic legs
and every original state mean remain. All constants below are explicit
functions of one declared low gauge budget and the completed RPT
constants. Every unknown higher background norm occurs only once.

The nonlinear residual is still $E=P\circ g-g\circ R_\star$.
There is no replacement of E by E/J. In particular the complete
$E'a$ term, the derivative of the current denominator and the
variation of the actual direction $g'a$ are all present.

## PCT1. Actual domain and one independent low gauge budget

Keep precisely [RPT.1--4](R144-supplement-all-angular-principal-return-tame-derivatives.md),
including its full-tail compact background, true root, all original
joins and the actual parameter interval. Its norms and constants are

$$
 B_s=1+\sup_r\|Q(r)\|_{A^s,\oplus_1},\qquad
 N_s(h,\kappa)=\|h\|_{L^2_r(H^s\oplus_1H^s)}+100|\kappa|,
 \qquad B_3<S=2^{25}.                                   \tag{PCT.1}
$$

The original normalized circle has period $\pi/2$ and frequencies
$4\mathbb Z$. Let $R_\star(x)=x+\Omega_\star$ be exactly PD.1.
Write $g=\operatorname{Id}+u$ for its original degree-one lift and require

$$
 \tfrac12\le g'\le2,\qquad
 G_s=1+\|u\|_{A^s},\qquad G_2\le L,\qquad L\ge2.           \tag{PCT.2}
$$

The full constant Fourier coefficient of u is included. L is a fixed
declared domain parameter, not a high norm hidden in a constant.
For example $G_2\le1+4\|u\|_{H^3}$ follows directly from
$(1+|k|)^2\le2(1+k^2)$ and the complete $A^0\le2H^1$
embedding. Thus an actual uniform H3 budget suffices.

The C1 neighbourhood in
[CP](R147-supplement-uniform-positive-phase-pivot-near-the-mean-exact-centre.md)
does not by itself supply L. A consumer must retain an actual L in
its domain. Neither bounded C1 distance nor a finite reference
truncation bounds the H3 norm of an arbitrary unknown tail.

For additive input directions $x=(a,\xi)$, where $a=(h,\kappa)$,
put
$$
 X_s(x)=N_s(a)+\|\xi\|_{H^s},\qquad
 Z_n=B_{n+2}+G_{n+1}.                                    \tag{PCT.3}
$$
In particular $Z_0,Z_1<S+L$. The higher Zn are not bounded by L or S.
The displayed estimates use directions with four additional angular
derivatives. This is a sufficient common norm convention, not a sharp
loss assertion and not a bounded same-order inverse.

All statements are first for smooth real admitted backgrounds.
Section PCT8 describes their extension and exact remainders. No
regular PDE, phase equation or mean equation is assumed solved.

## PCT2. An explicit real composition estimate

For an arbitrary periodic f and every integer $n\ge0$, define
$$
 c_n=2^{n+4}(n+1)!\,L^{n+1}.
$$
Then
$$
 \|f\circ g\|_{H^n}
 \le c_n\{\|f\|_{H^n}
               +G_{\max(n,1)}\|f\|_{H^1}\}.            \tag{PCT.4}
$$

Here composition is the actual real-circle composition. No complex
strip, analytic unknown or coefficientwise composition is used.

For n=0, change variables using $g'\ge1/2$ to obtain
$\|f\circ g\|_2\le\sqrt2\|f\|_2$. For n=1, differentiate once
and use $g'\le2$. These are both smaller than (PCT.4).

For n at least2, the complete Faà di Bruno formula consists of
$$
 (f^{(k)}\circ g)\prod_{i=1}^k g^{(m_i)},\qquad
 m_i\ge1,\quad \sum_i m_i=n,\quad 1\le k\le n,             \tag{PCT.5}
$$
with total nonnegative coefficient at most n!. One elementary proof
of the count identifies each set partition with the permutation
whose cycles are its blocks written in increasing order. This is an
injection into the n! permutations and counts the usual Bell
coefficients of (PCT.5).

Set $M=\|g'\|_{A^0}$, so $1\le M\le L$. Log-convexity of
the complete weighted Fourier sum gives
$$
 \|g^{(m)}\|_\infty
 \le \|g'\|_{A^{m-1}}
 \le M^{1-(m-1)/(n-1)}
           \|g'\|_{A^{n-1}}^{(m-1)/(n-1)}.
$$
The product of these factors has high exponent $(n-k)/(n-1)$.
Sobolev interpolation of f between orders1 and n has the
complementary exponent $(k-1)/(n-1)$. Hölder followed by the
weighted arithmetic-geometric mean inequality therefore bounds
each whole term by
$$
 \sqrt2\,L^n\{
       \|f\|_{H^n}+\|g'\|_{A^{n-1}}\|f\|_{H^1}\}
 \le\sqrt2\,L^n\{\|f\|_{H^n}+G_n\|f\|_{H^1}\}.            \tag{PCT.6}
$$

Since $\|g'\|_{A^{n-1}}\le G_n$, this proves the safe complete
composition estimate
$$
 \boxed{\quad
 \|f\circ g\|_{H^n}
 \le c_n\{\|f\|_{H^n}
               +G_{\max(n,1)}\|f\|_{H^1}\}.
 \quad}                                                  \tag{PCT.7}
$$
The index includes the derivative belonging to g itself; it is
not reduced by treating g' as an independent derivative-free input.
At n=0 and n=1 the displayed G1 is harmless and bounded by L.
The high index used below is at most $G_{n+1}$, exactly as in
(PCT.3).
The Bessel norm conversion costs at most $2^{n/2}$ times
the largest derivative norm from0 to n. The factor
$2^{n+4}(n+1)!$ pays that cost, the factor $\sqrt2$, and all
partitions. The proof treats all signed frequencies and the mean.

## PCT3. Complete reciprocal and product estimates

Put $j=g'\circ R_\star$. For $r=1,2$, define
$$
 d_n=2^{4(n+3)}((n+3)!)^2L^{n+3}.
$$
The actual real reciprocal satisfies
$$
                  \|j^{-r}\|_{H^n}\le d_nG_{n+1}.        \tag{PCT.8}
$$
At order0 this follows from $j^{-r}\le4$. At positive order,
the complete reciprocal chain rule has terms
$$
 (-1)^k(r)_k j^{-r-k}
              \prod_{i=1}^k j^{(m_i)},\qquad \sum_i m_i=n.
$$
Here $(r)_k\le(k+1)!$. Interpolating each derivative of j
between its A0 and An norms gives a product bounded by
$L^{k-1}G_{n+1}$. The coefficients with ordered blocks obey
$$
 \sum_{k=1}^n k!B_{n,k}(1,\ldots,1)
       \le n!\,2^{n-1}.
$$
Indeed order each block internally and concatenate the ordered
blocks; a permutation and k-1 cuts specify a larger collection
than all such ordered partitions. Thus the extra factor k+1 is
at most n+1. With $j^{-r-k}\le2^{n+2}$ and the full Bessel
conversion, the stated dn dominates every derivative, including
the lower ones. No inverse denominator uses a high Gs.

We will also use the complete Fourier product bound for
$1\le q\le5$:
$$
 \left\|\prod_{i=1}^q f_i\right\|_{H^n}
 \le q^{n+1}2^{q-1}
       \sum_{i=1}^q\|f_i\|_{H^n}
                         \prod_{\ell\ne i}\|f_\ell\|_{H^1}.
                                                               \tag{PCT.9}
$$
It follows from $\langle\sum k_i\rangle\le\sum\langle k_i\rangle$,
the complete convolution Young inequality and $A^0\le2H^1$.
This holds also for n=0 by the larger stated factor.
Every term has exactly one high factor. Multiplying separate
high bounds for all factors is unnecessary and is not done.

## PCT4. Finite explicit constants and elementary map packets

Use the rational constants Rn, An and Hn defined in RPT.11,
RPT.22 and RPT.25. Set
$$
 \begin{split}
 M_n&=1+\max_{0\le j\le n+3}\{R_j,A_j,H_j\},\\
 T_n&=2^{8(n+8)}((n+8)!)^2
        (1+L)^{2n+16}(1+S)(1+M_n),\\
 C_n&=T_n^{32}.
 \end{split}                                                \tag{PCT.10}
$$

These are finite explicit real constants for any fixed L; if L is
rational they are rational. A requested finite angular order uses
only finitely many completed RPT recurrences. No unknown Bs or Gs
above the stated fixed low budgets enters these definitions.

For reference the complete packets used in the formulas below are
$$
 \begin{array}{c|c}
 \hbox{packet}&\hbox{high expression before its fixed coefficient}\\ \hline
 (P-\operatorname{Id})\circ g & Z_n\\
 P'\circ g,\quad P''\circ g,\quad j^{-1},j^{-2},g'&Z_n\\
 DP[a]\circ g & N_n(a)+Z_nN_4(a)\\
 (DP[a])'\circ g & N_{n+1}(a)+Z_nN_4(a)\\
 D^2P[a,b]\circ g&
 N_{n+3}(a)N_4(b)+N_4(a)N_{n+3}(b)
                         +Z_nN_4(a)N_4(b).
 \end{array}                                                \tag{PCT.11}
$$
Each entry is an Hn bound with coefficient at most $T_n^3$.
Its H1 bound uses the corresponding low direction norms, a fixed
coefficient at most $T_n^3$, and no unknown high background.

To check this without hiding a composition hypothesis, substitute
RPT.32--33 into (PCT.7). The low H1 data for the last three
packets are bounded respectively by
$$
 A_1(1+S)N_1(a),\qquad
 A_2(1+S)N_2(a),\qquad
 H_1(S+2)N_4(a)N_4(b).                                  \tag{PCT.12}
$$
The low H1 data for P' and P'' are at most $R_2S$ and $R_3S$.
Their high orders are respectively $B_{n+1}$ and $B_{n+2}$.
This is why the background budget in Zn is $B_{n+2}$.
Composition adds at most $G_{\max(n,1)}$, already paid by
$G_{n+1}$. Equations (PCT.8) and $g'\in A^n$ give the other
background packets. At low H1 all of them use only $B_3<S$
and $G_2\le L$. There is no appeal to $B_4<S$.

The coefficient allowance $T_n^3$ dominates cn, c1, dn, d1,
the factors S+2 and L, the listed RPT constants, and their
at-most-three products in these substitutions. The product
coefficient for five factors in (PCT.9) is also smaller than Tn.
Consequently a sum of at most eight products of at most five
such packets has coefficient below $T_n^{17}<C_n$:
five packets cost $T_n^{15}$, the Fourier product costs Tn,
and their complete sum costs at most another Tn.
This is the explicit coefficient ledger used below.

The low estimates in (PCT.12) are assigned before multiplying.
Thus a high background from one packet is always multiplied
by low bounds for all the others. No product $B_sG_t$ of two
unknown high norms is introduced.

## PCT5. Raw phase map, first derivative and full Hessian

The actual map and its derivatives are exactly
$$
 \begin{split}
 E&=P\circ g-g\circ R_\star,\\
 DE[x]&=DP[a]\circ g+(P'\circ g)\xi-\xi\circ R_\star,\\
 D^2E[x,y]&=D^2P[a,b]\circ g
      +(DP[a])'\circ g\,\eta+(DP[b])'\circ g\,\xi\\
 &\hspace{36mm}+(P''\circ g)\xi\eta ,
 \end{split}                                                \tag{PCT.13}
$$
where $y=(b,\eta)$. The second line is the full derivative at
fixed exact target rotation. The last line is precisely RP.27.

For every integer $n\ge0$ the complete bounds are
$$
 \|E\|_{H^n}\le C_n Z_n,                                  \tag{PCT.14}
$$
$$
 \|DE[x]\|_{H^n}
       \le C_n\{X_{n+4}(x)+Z_nX_4(x)\},                   \tag{PCT.15}
$$
$$
 \boxed{\begin{split}
 \|D^2E[x,y]\|_{H^n}\le C_n\{&
     X_{n+4}(x)X_4(y)+X_4(x)X_{n+4}(y)\\
     &+Z_nX_4(x)X_4(y)\}.
 \end{split}}                                             \tag{PCT.16}
$$

For the value estimate write
$E=(P-\operatorname{Id})\circ g+u-u\circ R_\star-\Omega_\star$.
The full constant is retained; $0<\Omega_\star<2$ and $Z_n\ge2$
pay it. For the derivatives apply (PCT.9) to the literal four
terms in (PCT.13), with packets (PCT.11).
The high direction orders needed are at most n+3 in the
return Hessian and n+1 in the mixed terms. The common n+4
buffer also pays their low H1 versions. All constants fit
the explicit ledger of PCT4.

Nothing in this derivation projects away the phase average.
The only projections inside P are its original primitive's
intermediate zero-mode removal, already accounted for in RPT.
The state mean, the parameter's true direct term and the
constant gauge direction are genuine inputs to (PCT.13).

RP's sharper low-norm Hessian and its 400 quadratic remainder
remain valid and should be used when they suffice.
The large Cn are a full higher-order estimate, not a revision
of those sharper completed inequalities.

## PCT6. Actual current left-normalized linear row

For a fixed abstract direction $v=(a,\alpha)$ define the
operator family
$$
 \mathscr L_{Q,\nu,g}v
       =j^{-1}DE(Q,\nu,g)[a,g'\alpha].                    \tag{PCT.17}
$$
Set $Y_s(v)=N_s(a)+\|\alpha\|_{H^s}$.
This is exactly the current PD row, in its declared input
coordinate. The exact identity is
$$
 \mathscr L v
 =\frac{DP[a]\circ g}{j}
       +\alpha-\alpha\circ R_\star+\frac{E'}j\alpha .
                                                               \tag{PCT.18}
$$
It uses $P'(g)g'=j+E'$ and retains the entire residual term.

At a current background direction $x=(b,\xi)$, with the
abstract a and alpha fixed, write $U_a=DP[a]\circ g$ and
$V=P'\circ g$. Direct differentiation gives all seven terms
$$
 \begin{split}
 D\mathscr L[x]v={}&
  j^{-1}(D^2P[b,a]\circ g)
 +j^{-1}((DP[a])'\circ g)\xi
 -j^{-2}(\xi'\circ R_\star)U_a\\
 &+j^{-1}((DP[b])'\circ g)g'\alpha\\
 &+j^{-1}(P''\circ g)\xi g'\alpha
 +j^{-1}V\xi'\alpha
 -j^{-2}(\xi'\circ R_\star)Vg'\alpha .
 \end{split}                                                \tag{PCT.19}
$$

The sixth term is the variation of the actual direction $g'\alpha$.
The third and seventh terms are the variation of the denominator.
They are not zero at a solved phase. As a coordinate-free check,
the same expression is
$$
 D\mathscr L[x]v
 =-\frac{\xi'\circ R_\star}{j^2}DE[a,g'\alpha]
   +\frac1j\{D^2E[x,(a,g'\alpha)]+DE[0,\xi'\alpha]\}.
                                                               \tag{PCT.20}
$$
This identity also explains why differentiating an allegedly
fixed $g'\alpha$ would give the wrong operator-family derivative.

The direct seven-term formula and PCT4 prove
$$
 \|\mathscr L v\|_{H^n}
       \le C_n\{Y_{n+4}(v)+Z_nY_4(v)\},                   \tag{PCT.21}
$$
$$
 \boxed{\begin{split}
 \|D\mathscr L[x]v\|_{H^n}\le C_n\{&
 X_{n+4}(x)Y_4(v)+X_4(x)Y_{n+4}(v)\\
 &+Z_nX_4(x)Y_4(v)\}.
 \end{split}}                                             \tag{PCT.22}
$$

In (PCT.19) there are seven complete products and at most five
factors per product. The only additional direction derivative
is $\xi'$, whose high Hn norm costs H(n+1) and low H1 norm
costs H2. These are paid by (PCT.22). In particular one need
not insert the weakened four-derivative estimate (PCT.16)
into the coordinate-dependent vector $g'\alpha$ and create
an artificial high g derivative. The literal formula (PCT.19)
has background order exactly Zn.

This proves one background derivative of the whole operator
family, at every angular order. It does not assert its second
background derivative without a third derivative of P.
It is the first and full second derivative of the nonlinear E
that have been proved in PCT5.

## PCT7. Same-state scalar and divisor consumer

Taking the complete normalized mean in (PCT.17) has norm one
on H0. Therefore (PCT.21)--22 also pay the full mean functional
and its first background derivative. Applied to CP's fixed
particular candidate, these are tame bounds for that same
candidate's scalar S, with its genuine direction and all regular
response defects still present.

The positive lower $1/60<S<3/50$ belongs only to the additional
explicit CP neighbourhood. To combine it with this result take
the intersection of the two actual domains, including (PCT.2).
It does not make the candidate a full regular inverse or set
its regular residual to zero.

The exact divisor solve and residual fee are still PD.14--18:
$$
 \|\alpha\|_{H^s}\le17\|w\|_{H^{s+1}},\qquad
 \|E'\alpha\|_{H^s}\le17C_s^{\rm PD}
 \{\|E\|_{H^{s+1}}\|w\|_{H^2}
       +\|E\|_{H^2}\|w\|_{H^{s+1}}\},\quad s\ge1.
                                                               \tag{PCT.23}
$$
These are cited completed bounds, not recalculated targets.
No average of $E'\alpha$ is set to zero. Current division
by j is only a left multiplication of the linear equation;
it never authorizes a same-order inverse for the principal
small divisor or a replacement of the nonlinear residual.

The physical chart residual also remains the full RP.28 secant
$$
 \Theta_0(g\circ R_\star+E)-\Theta_0(g\circ R_\star).
                                                               \tag{PCT.24}
$$
This note proves the declared moving-angle residual. A consumer
differentiating (PCT.24) must include the independent waist-chart
variations and its entire secant. Replacing it by one endpoint
derivative is not part of this proof.

## PCT8. Remainders, real density and scope

For an additive increment z and an admitted real line segment,
let $Z_n^*$ be the whole segment supremum; use one L valid
on that whole segment. The exact integral remainder yields
$$
 \|E(q+z)-E(q)-DE(q)z\|_{H^n}
 \le C_n\{X_{n+4}(z)X_4(z)
                         +Z_n^*X_4(z)^2\}.               \tag{PCT.25}
$$
The direction norms do not depend on the current background.
Likewise integrating (PCT.16) gives the complete derivative
difference estimate, and integrating (PCT.22) gives
$$
 \|(\mathscr L_{q+z}-\mathscr L_q)v\|_{H^n}
 \le C_n\{X_{n+4}(z)Y_4(v)+X_4(z)Y_{n+4}(v)
                      +Z_n^*X_4(z)Y_4(v)\}.             \tag{PCT.26}
$$

For real density, approximate u by positive periodic convolution,
retaining its constant mode. Its derivative remains between
1/2 and2 and its A2 norm does not grow. Approximate the
full-tail state exactly as in RPT, preserving the finite
compact centre, the original means and all radial interfaces.
The real composition, reciprocal and variational formulas
converge in the displayed Sobolev norms. The bounds extend
the derivatives to their stated direction spaces. This does
not define the original nonlinear flow on an unrestricted
rough radial L2 ball; the admitted strong background domain
is retained throughout.

Thus the full moving-phase D2 tame interface and the actual
current left-row C1 interface have explicit same-object
bounds. A complete regular finite/high inverse, its true
parameter response, physical means, all matching and cap
graphs, the physical chart secant, a summable iteration and
the final fixed-metric geometric family remain separate
obligations. The final topic criterion is not claimed here.

The companion calculation contains only new rational coefficient
comparisons for this proof. It restores no old carrier, phase
integral, norm target, finite residual or scientific workflow.

