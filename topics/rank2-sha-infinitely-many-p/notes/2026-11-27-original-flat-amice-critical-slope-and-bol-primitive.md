# Actual flat Amice moments, the critical slope, and the Bol primitive

Date: 2026-11-27. Session: Astra-rank2-Sha-0b097461-20261127.

This note proves a critical-value and critical-slope formula, an exact
connection primitive formula, and a finite reader with a uniform tail,
all on one actual bounded $Q=q_{\rm dR}^{1/p^b}$ source. It does not
identify $Q$-rotations with CM isogenies. At the bad inert point the
source remains $g_1^*F$. No usual-depletion cross is reinstated.

## 1. The same bounded source and its full measure

Let $p\ge5$. After the specified $\theta$ evaluation of the actual
coefficients at the geometric point, write
$$
 A(Q)=\sum_{r\ge0}a_r(Q-1)^r,\qquad
 \inf_r v_p(a_r)=m_A>-\infty .
 \tag{1}
$$
All original periods, finite Schwartz factors and rigidifications
remain in $A$, including its constant coefficient.

The bounded measure $\mu_A$ on $\mathbf Z_p$ is determined by
$$
 \int\binom xr\,d\mu_A=a_r.
 \tag{2}
$$
Indeed, for a continuous Mahler expansion $f=\sum f_r\binom xr$,
$f_r\to0$, define its integral by $\sum f_ra_r$. Its norm is at most
$p^{-m_A}$. Thus $A(Q)=\int Q^x\,d\mu_A$ on $|Q-1|<1$.

The actual flat operator is the complete character projector
$$
 A^\flat(Q)=A(Q)-\frac1p\sum_{a=0}^{p-1}A(\zeta_p^aQ)
           =\int_{\mathbf Z_p^\times}Q^x\,d\mu_A(x).
 \tag{3}
$$
There is no loss of measure norm in the displayed $1/p$.

For $j=(\epsilon,j_p)\in\mathbf Z/(p-1)\times\mathbf Z_p$, set
$$
 \mu_j=\int_{\mathbf Z_p^\times}
       \omega(x)^\epsilon\langle x\rangle^{j_p}\,d\mu_A(x).
 \tag{4}
$$
The Teichmuller and $p$-adic coordinates are distinct. On each fixed
component (4) is analytic, and its derivative inserts
$\log\langle x\rangle$.

Retain the actual Maass coefficient and its original sign:
$$
 C=-\frac{p^b\theta(y_{\rm dR})(y)}{\widehat z(y)},\qquad
 v_p(C)>-\frac1{p-1}.
 \tag{5}
$$
Kriz's weight-three formula on this same bounded source is
$$
 {\cal M}_A(j)=\sum_{i\ge0}c_i(j_p)C^i\mu_{j-i},\qquad
 c_i(X)=\binom{X+2}{i}\binom Xi\,i!.
 \tag{6}
$$
Here $j-i$ shifts both coordinates in (4). For nonnegative integer $j$
the sum is the original finite Maass formula. The input is
arXiv1805.03605 (194)--(213), or AMS212 (6.51)--(6.58) and
(6.64)--(6.65), with the actual bounded-source hypotheses.

## 2. The uniform derivative tail and the whole critical slope

For $i\ge1$ put $\ell_i=\lfloor\log_p i\rfloor$.
Vandermonde and
$\binom th/t=\binom{t-1}{h-1}/h$ imply, for $x,t\in\mathbf Z_p$,
$$
 v_p\left(\frac{\binom{x+t}{i}-\binom xi}{t}\right)
 \ge-\ell_i\quad(t\ne0).
$$
The derivative has the same bound. Hence
$v_p(c_i(x))\ge v_p(i!)$ and
$v_p(c_i'(x))\ge v_p(i!)-\ell_i$, also for the corresponding difference
quotient. Since $\log\langle x\rangle\in p\mathbf Z_p$ on the units,
the derivative of the $i$th summand of (6), and its difference quotient,
have valuation at least
$$
 m_A+v_p(i!)+i\,v_p(C)-\ell_i .
 \tag{7}
$$
This tends to infinity: one may use
$v_p(i!)\ge i/(p-1)-1-\ell_i$ and (5).
Thus the derivative tails are uniform, and differentiating (6) is
justified. This does not infer differentiability merely from a
continuous interpolation theorem.

At $j=(-2,-2)$ one has
$$
 c_0(-2)=1,\quad c_i(-2)=0,\quad
 c_i'(-2)=-(i+1)(i-1)!\quad(i\ge1).
 \tag{8}
$$
For the last equality use
$\left.\frac d{dX}\binom{X+2}{i}\right|_{-2}=(-1)^{i-1}/i$
and $\binom{-2}{i}=(-1)^i(i+1)$.
Therefore
$$
 \boxed{{\cal M}_A(-2)=\int_{\mathbf Z_p^\times}x^{-2}\,d\mu_A(x),}
 \tag{9}
$$
$$
 \boxed{
 {\cal M}_A'(-2)=
 \int_{\mathbf Z_p^\times}x^{-2}\log\langle x\rangle\,d\mu_A(x)
 -\sum_{i\ge1}(i+1)(i-1)!C^i
           \int_{\mathbf Z_p^\times}x^{-2-i}\,d\mu_A(x).}
 \tag{10}
$$
No mass or lower convolution is deleted.

Equivalently, let
$$
 {\cal E}(T)=\sum_{n\ge0}n!T^n,\qquad
 {\cal H}(T)=(1+T){\cal E}(T)-1
           =\sum_{i\ge1}(i+1)(i-1)!T^i .
$$
Their radius is $p^{1/(p-1)}$, and (5) gives
$$
 {\cal M}_A'(-2)=
 \int_{\mathbf Z_p^\times}x^{-2}
  \bigl(\log\langle x\rangle-{\cal H}(C/x)\bigr)\,d\mu_A(x).
 \tag{11}
$$
This kernel comes from the actual $c_i$, not a new Gamma normalization.

For $j(u)=(p^2-1)u-2$, the $u$ derivative is $(p^2-1)$ times
(10). A full toric sum
$\sum_\alpha w_\alpha(u){\cal M}_{A_\alpha}(j(u))$ also has the term
$\sum_\alpha w_\alpha'(0)\int x^{-2}d\mu_{A_\alpha}$.
Finite characters, periods and outer weights must therefore remain.

At the actual bad inert normalization $b=2$, use precisely the
CM basis of AMS212 Proposition 7.7 (printed pp. 203--205).
That proposition gives $|\widehat z|=1$ and permits the specified basis
with $|y_{\rm dR}|=|\theta(y_{\rm dR})|=|2|^{-1}$.
Its proof uses (4.17) and the CM-conjugate values
$z_{\rm dR}=2/(1+\sqrt{-d})$ and
$\widehat z=2/(1-\sqrt{-d})$, giving
$y_{\rm dR}=(1+\sqrt{-d})/(2\sqrt{-d})$.
For odd inert $p$ this is a unit, and so $v_p(C)=2$.
The correction sum in (10) is then in
$p^{m_A+2}{\cal O}_{\mathbf C_p}$. This refers to that actual basis
and to the source norm $m_A$; the nonintegral valuation of
$\Omega_p$ in Proposition 7.7 (7.8) has not been set to zero.
For an arbitrary basis only the displayed hypothesis (5) is used.

## 3. An analytic double primitive of this same source

On $|Q-1|<1$ define
$$
 {\cal B}_A(Q)=\int_{\mathbf Z_p}
    \frac{Q^x-1-x\log Q}{x^2}\,d\mu_A(x),
 \tag{12}
$$
with value $(\log Q)^2/2$ at $x=0$.
For a closed disk $|Q-1|\le r<1$, choose $a$ large enough that
$Q^{p^a}$ and $x\log Q$ lie in the exponential disk when
$x\in p^a\mathbf Z_p$. On that part the kernel is the uniformly
convergent series
$\sum_{n\ge2}x^{n-2}(\log Q)^n/n!$.
On its complement $x^{-2}$ is bounded and the binomial expansion of
$Q^x$ converges uniformly. This proves uniform regularity at $x=0$
and analyticity on each such closed disk.

For $D_Q=Q\,d/dQ$,
$$
 D_Q^2{\cal B}_A=A,\qquad
 {\cal B}_A(1)=D_Q{\cal B}_A(1)=0.
 \tag{13}
$$
Flat commutes with $D_Q$ and kills both $1$ and $\log Q$.
The complete root average of (12) consequently gives
$$
 {\cal B}_A^\flat(Q)=
 \int_{\mathbf Z_p^\times}x^{-2}Q^x\,d\mu_A(x),\qquad
 D_Q^2{\cal B}_A^\flat=A^\flat .
 \tag{14}
$$
In particular
$$
 {\cal M}_A(-2)=
 {\cal B}_A(1)-\frac1p\sum_{a=0}^{p-1}{\cal B}_A(\zeta_p^a).
 \tag{15}
$$
At $\zeta_p^a$ the kernel vanishes on $p\mathbf Z_p$ and is
$(\zeta_p^{ax}-1)/x^2$ on the units, checking the sign.
Any two analytic double primitives differ by $a+b\log Q$, so (15)
is independent of both integration constants. These are evaluations
of the same $Q$-expansion, not asserted CM isogeny evaluations.

## 4. The actual Bol and Hodge-valued primitive

Put $t=\log Q$, $z=z_0+p^bt$. In the horizontal de Rham frame use
$$
 \omega_{\rm can}=-z e_1+e_2,\qquad
 \langle e_1,e_2\rangle=-1,\qquad
 {\rm KS}(\omega_{\rm can}^{\otimes2})=-dz .
 \tag{16}
$$
These are arXiv1805.03605 (96)--(97) and (114)--(115), with its Tate
pairing normalization. External source multipliers stay in $A$.

The variable scaled connection is
$C(t)=C(0)/(1+C(0)t)$, so $D_QC=-C^2$. Hence
$$
 (D_Q+C)(D_Q-C)=D_Q^2 .
 \tag{17}
$$
This is precisely the weight-minus-one to weight-three Bol identity.
The variable connection has not been replaced by a constant.

Given $D_Q^2B=A$, set
$$
 {\cal G}_B=-p^b(D_QB)\omega_{\rm can}-p^{2b}B e_1 .
 \tag{18}
$$
Since $D_Q\omega_{\rm can}=-p^be_1$, direct calculation gives
$$
 \nabla{\cal G}_B=-A\omega_{\rm can}\,dz,\qquad
 \langle{\cal G}_B,\omega_{\rm can}\rangle=p^{2b}B .
 \tag{19}
$$
The first right side is the KS image of
$A\omega_{\rm can}^{\otimes3}$ under (16).

Let $\mathcal G$ be an actual Coleman primitive of this same source
and take its complete formal $Q$-expansion in (16). Its difference
from (18) is a horizontal constant vector. Formula (12) thus provides
an analytic continuation of that formal expansion to $|Q-1|<1$.
This uses the connection equation and the bounded source, not an
ordinary-to-supersingular rigidity argument.
Flat kills that horizontal constant; also
$\omega_{\rm can}(\zeta_p^aQ)=\omega_{\rm can}(Q)$. We obtain
$$
 \boxed{
 {\cal M}_A(-2)=p^{-2b}
 \left\langle
  {\cal G}(1)-\frac1p\sum_{a=0}^{p-1}{\cal G}(\zeta_p^a),
  \omega_{\rm can}(1)
 \right\rangle .}
 \tag{20}
$$
This is a source-level connection identity. The finite trace remains
the actual analytic $Q$-trace.

The bad-point transport has a necessary determinant cost.
For $g_1=\operatorname{diag}(p,1)$,
$g_1^*\omega_{\rm can}=\omega_{\rm can}$ and
$g_1^*dz=p^{-1}dz$. If $\mathcal G_{\rm good}$ is a primitive of
the good source $F$, the primitive of the bad coefficient source
$A=g_1^*F$, with its standard KS identification, is
$$
 {\cal G}_A=p\,g_1^*{\cal G}_{\rm good}.
 \tag{21}
$$
The actual degree-$p$ pullback also multiplies the Poincare pairing
by $p$. Thus the bad $b=2$ factor in (20) is
$p^{-4}\cdot p\cdot p=p^{-2}$ times the good pairing, exactly the
good $b=1$ factor. Both factors are required. This agrees with the
proved equality of the good $(p\theta_3)^j$ reader and the bad
$(p^2\theta_3)^j$ reader on $g_1^*F$, not on a substituted $F$.

## 5. Full unflat Maass data return to the Amice coefficients

Let $m_r=\int_{\mathbf Z_p}x^r\,d\mu_A$ be the unflat moments and
$R_n=\sum_{i=0}^n c_i(n)C^i m_{n-i}$ the unflat Maass values of this
same source at the point. As formal power series,
$$
 \sum_{n\ge0}R_n\frac{Z^n}{n!}
  =(1-CZ)^{-3}A\left(\exp\frac{Z}{1-CZ}\right),
 \tag{22}
$$
$$
 m_n=\sum_{i=0}^n c_i(n)(-C)^iR_{n-i}.
 \tag{23}
$$
For (22), put $n=m+i$ and sum
$\sum_i\binom{m+i+2}{i}(CZ)^i=(1-CZ)^{-m-3}$.
Its inverse substitution $Z=T/(1+CT)$ proves (23).

For signed Stirling numbers of the first kind $s(r,m)$, the actual
ordinary coefficient is
$$
 a_r=\frac1{r!}\sum_{m=0}^r s(r,m)
          \sum_{i=0}^m c_i(m)(-C)^iR_{m-i}.
 \tag{24}
$$
Every lower term is retained. These are finite coefficient identities.
They do not preserve a common numerical input precision for free.
Keeping the actual $C$ exact, if the supplied $R_l$ has error of valuation
at least $L_l$, the error in (24) satisfies
$
 v_p(\delta a_r)\ge
 \min_{\substack{0\le i\le m\le r\\s(r,m)c_i(m)\ne0}}
 \{L_{m-i}+v_p(s(r,m)c_i(m)C^i)\}-v_p(r!).
 \tag{24a}
$
The usual convention omits zero summands, including $C^i=0$.
A convenient sufficient uniform loss through $N$ is
$
 \Delta_N=\max_{0\le r\le N}
 \left\{v_p(r!)+
  \max_{\substack{0\le i\le m\le r\\c_i(m)C^i\ne0}}
       [-v_p(c_i(m)C^i)]\right\}.
 \tag{24b}
$
The $i=0$ term makes the inner maximum nonnegative.
Thus input precision $L+\Delta_N$ gives all $a_r$, $r\le N$, to
precision $L$. When $v_p(C)\ge0$, in particular in the stated bad
$b=2$ basis, all $c_i(m)C^i$ are integral and
$\Delta_N=v_p(N!)$. The complete finite sums can sometimes improve
this sufficient bound, but no such improvement is assumed.

At a root of unity one evaluates the actual bounded $Q-1$ series (1);
one must not substitute $\log\zeta_p=0$ into the formal exponential
expression before paying its analytic domain.

## 6. A finite critical reader and its full tail

Let $f_s(x)={\bf1}_{\mathbf Z_p^\times}(x)x^{-s}$ with $f_s(0)=0$.
Its $s=2$ Mahler coefficients are the rational $p$-integers
$$
 \lambda_{r,p}=
 \sum_{\substack{0\le j\le r\\p\nmid j}}
       (-1)^{r-j}\binom rj\,j^{-2}.
 \tag{25}
$$
The same actual critical value is
$$
 {\cal M}_A(-2)=\sum_{r\ge0}\lambda_{r,p}a_r .
 \tag{26}
$$

Write $b_{s,r}$ for the Mahler coefficients of $f_s$.
For $r>0$ the full roots-of-unity expression for $f_0$ gives
$v_p(b_{0,r})\ge r/(p-1)-1$.
The identity $xf_{s+1}=f_s$ gives
$b_{s,r}=r(b_{s+1,r}+b_{s+1,r-1})$ for $r\ge1$.
The coefficients tend to zero by continuity, so solving from the tail
gives
$$
 b_{s+1,r}=(-1)^{r+1}
            \sum_{h>r}(-1)^h b_{s,h}/h .
 \tag{27}
$$
These sums converge by the preceding bound and induction.
For $r\ge2p$, the functions
$x/(p-1)-a\log_p x$, $a=1,2$, are increasing in the required range.
Two applications of (27) prove
$$
 v_p(\lambda_{r,p})\ge
 \frac{r+2}{p-1}-1-2\log_p(r+2).
 \tag{28}
$$
Consequently, for $N\ge2p$, the entire remainder of (26) after $r=N$
has valuation at least
$$
 m_A+\frac{N+3}{p-1}-1-2\log_p(N+3).
 \tag{29}
$$
A complete coefficient prefix $a_0,\ldots,a_N$ known modulo
$p^{m_A+H}$, with the bound (29) at least $m_A+H$, therefore determines
(26) to that precision. If this prefix is obtained instead from the
same complete $R_0,\ldots,R_N$, sufficient input precision is
$p^{m_A+H+\Delta_N}$ by (24a)--(24b); all $\lambda_{r,p}$ are integral.
In the stated integral-$C$ case this additional cost is $v_p(N!)$.
There are no new independently adjustable moments or zero rows.
The prefix length is of order $p(H+\log_p(H+1)+1)$; the separate
input-precision cost has not been absorbed into that length.

## 7. The exact remaining source comparison

Equations (9)--(11), (15), (20)--(21), and (24)--(29) are paid for
every actual bounded source under the displayed hypotheses.
For the original bad inert point they concern $g_1^*F$. They may be
summed with all original Schwartz, Artin and corestriction coefficients,
including their actual weight derivatives.

What remains is to return the full analytic $Q$-trace in (20), or the
full source coefficients in (24), to the original canonical Newton
reader or the specified proper finite-polynomial graph pairing.
A source degree, a single L-factor, or a usual-depletion formula
does not perform that return. This note gives no new canonical zero
and asserts no infinite-prime nonvanishing.

### Exact dependencies

- D. J. Kriz, arXiv1805.03605 (2018), (96)--(97), (114)--(115),
  (194)--(213): https://arxiv.org/pdf/1805.03605 .
- D. J. Kriz, *Supersingular p-adic L-functions, Maass-Shimura
  Operators and Waldspurger Formulas*, AMS212 (2021), (6.51)--(6.58),
  (6.64)--(6.65). Only the actual source and coefficient formulas
  are used, not the disputed usual-depletion cross.
- [Actual bad-point source and p-square boundary](2026-11-27-original-bad-cm-b2-source-and-p-square-boundary.md).
- [The earlier continuity audit](2026-11-27-original-psi4-common-factor-digit-and-continuity-audit.md);
  its scope restrictions remain in force.

No mathematical program or new numerical computation was run.
