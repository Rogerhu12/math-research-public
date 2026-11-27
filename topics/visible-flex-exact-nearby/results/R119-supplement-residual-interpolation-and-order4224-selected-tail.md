# R119 SRH: residual interpolation and the same selected tail through order4224

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved.** The original S/T selected tail has stronger regularity:
the same sequence converges in every integer complete graph order
through4224. Its actual and common-reference order4000 norm is
below $2^{-49999998}$. The exact selected background therefore
supports the original linearized a priori estimate at every
output order $64\le s\le2204$, for directions in $E_{4000,0}^+$,
with the unchanged two constants.

The new input is the already proved high residual bound in S.37.
Interpolating the complete residual before applying the inverse
is sharper than paying the full smoothing loss from its low norm.
No iteration, seed, inverse, source or previous comparison is
recomputed. The selector, physical parameter domain, step sizes
and all actual means and boundaries are unchanged.

## 1. Same original iterates and complete quantities

Use [S](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md),
[T](R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md),
[SREG](R119-supplement-higher-regularity-of-selected-tail-and-local-uniqueness.md)
and [SHL](R119-supplement-L2-response-of-the-actual-selected-tail-and-physical-readouts.md).

The value domain is still exactly
$$
 \mathcal D=\left\{\gamma\in H^{8193}_{\perp,\mathrm{ev}}:
   \|\gamma/r_\gamma\|_{A^0}\le1/128,\quad
   \|\gamma/r_\gamma\|_{H^{8193}}\le2^{1048576}\right\},
                 \qquad r_\gamma=10^{-9}.                \tag{SRH.1}
$$
For each gamma keep its same actual94 seed, selected second
parameter, fixed profiles, stop, shallow piece, far chart and
one height gauge. Its first principal parameter is the same
actual value map. Work first in the actual reference for this
fixed gamma.

The exact original S.34 construction is
$$
 \begin{aligned}
 a&=1856,\qquad b=6396,\qquad
 T_n=2^{1500000(5/4)^n},\\
 F_n&=\mathcal F_\gamma(w_n),\qquad v_n=S_{T_n}w_n,\\
 h_n&=-\widehat{\mathcal R}_{v_n}(S_{T_n}F_n),\qquad
                           w_{n+1}=w_n+h_n .
 \end{aligned}                                           \tag{SRH.2}
$$
There is no additional smoothing outside this inverse.
All iterates and directions have the same fixed $B_0=0$
condition. The actual nonlinear far graph is satisfied by
$\mathcal U_\gamma(w_n)$ at each step.

S.37 already gives, for every $n\ge1$,
$$
 \begin{aligned}
 |F_n|_a&\le T_n^{-3000},&
 |F_n|_b&\le T_{n-1}^{400}=T_n^{320},\\
 \|w_n\|_{E_a^+}&\le\rho_+/4<1,&
 \|w_n\|_{E_b^+}&\le T_{n-1}^{3500}=T_n^{2800}.
 \end{aligned}                                           \tag{SRH.3}
$$
At $n=0$ the same inequalities follow directly from the
already completed full seed bounds S.31. In particular
the high residual is not an unknown new input. The
ordinary source norm $|\cdot|_s=Z_s^{[3]}$ keeps all
three broken radial derivatives, true seams, physical
units and complete mean reconstruction.

For each compatible graph/source Hilbert scale the
original angular smoothing has norm at most1 at the
same order. Constant-one interpolation holds for its
complete angular components; Hölder retains the state,
trace and weighted radial supremum or source sums.
No Fourier support assumption about an actual solution
is used.

## 2. Interpolate the entire residual before applying the inverse

Let $1856\le s\le4600$. Then
$$
 a\le s+1734\le b,\qquad
 a\le s+1796\le b.
$$
Interpolate the first line of (SRH.3) at the actual source
order required by S.24:
$$
 \begin{aligned}
 |S_{T_n}F_n|_{s+1734}
 &\le |F_n|_{s+1734}\\
 &\le |F_n|_a^{1-\theta_s}|F_n|_b^{\theta_s}
 \le T_n^{p(s)},\\
 \theta_s&=\frac{s+1734-1856}{4540}
                         =\frac{s-122}{4540},\\
 p(s)&=-3000+\frac{3320(s-122)}{4540}
                         =\frac{166s-701252}{227}.
 \end{aligned}                                           \tag{SRH.4}
$$
Both bounds in the interpolation are the full source
bounds from the same iterate. This does not infer a
strong source norm from a weaker output or replace the
actual source by its finite part.

For the high background in that same inverse estimate,
(SRH.3) gives
$$
 \|v_n\|_{E_{s+1796}^+}
 \le\|w_n\|_{E_{s+1796}^+}
 \le T_n^{2800(s-60)/4540}.                              \tag{SRH.5}
$$
The low source satisfies
$|S_{T_n}F_n|_{1794}\le|F_n|_a\le T_n^{-3000}$.
Because the exponent in (SRH.5) is nonnegative,
$$
 (1+\|v_n\|_{E_{s+1796}^+})|S_{T_n}F_n|_{1794}
 \le2T_n^{q(s)},\qquad
                 q(s)=\frac{140s-689400}{227}.            \tag{SRH.6}
$$
Thus the full high-background/low-source term is retained.

Apply S.24 to the actual direction in (SRH.2), including
its true added B trace. Its two coefficients remain
$2^{16777216}$ and
$2^{67108864}(1+\overline B_\gamma)^2$.
The already established SREG.4 budget
$$
                            C_*=2^{184549390}
$$
pays those same two summands, their fixed factors and the
single common-reference conversion. Therefore
$$
 \|h_n\|_{E_{s,c}^+}
       \le C_*\max(T_n^{p(s)},T_n^{q(s)}),
                       \qquad1856\le s\le4600.            \tag{SRH.7}
$$
The same bound covers the actual-reference norm.
No new choice of the inverse or its arbitrary high
background is made.

For this whole window,
$$
 p(s)-q(s)=\frac{26s-11852}{227}>0 .
$$
Consequently the sharper useful increment estimate is
$$
 \boxed{\ 
 \|h_n\|_{E_{s,c}^+}\le C_*T_n^{(166s-701252)/227},
                         \qquad1856\le s\le4600 .
 \ }                                                     \tag{SRH.8}
$$
Orders above the sign change of the exponent need not
converge. This formula alone is not an unlimited
regularity statement.

## 3. Actual convergence through4224 and the small order4000 norm

For every integer $1856\le s\le4224$, put
$$
                     d_s=\frac{701252-166s}{227}.
$$
The smallest such decay exponent is
$$
                          d_{4224}=\frac{68}{227}>\frac14 .
                                                               \tag{SRH.9}
$$
Since
$$
 \frac{T_{n+1}^{-d_s}}{T_n^{-d_s}}
                  =T_n^{-d_s/4}
                  <2^{-1500000/16}<\frac12 ,
$$
the entire infinite correction series obeys
$$
 \boxed{\ 
 \sum_{n\ge N}\|h_n\|_{E_{s,c}^+}
                \le2C_*T_N^{-d_s},
                     \qquad1856\le s\le4224 .
 \ }                                                     \tag{SRH.10}
$$
Complete graph convergence and its closed linear boundary
condition identify its limit with the original S/T
$w_\gamma$. Every lower-order limit agrees by inclusion.
All four state jets, all three source jets, the weighted
radial supremum and the fixed trace remain in the limit.

At $s=4000$ the two exact numerator values are
$$
       227p(4000)=-37252,\qquad227q(4000)=-129400 .
$$
Both exponents are strictly below $-164$. Hence
$$
 \|w_\gamma-w_0\|_{E_{4000,c}^+}
 \le2C_*T_0^{-164}
                    =2^{-61450609}.                      \tag{SRH.11}
$$
SREG already records the actual initial common-reference
bound $\|w_0\|_{E_{8192,c}^+}<2^{-49999999}$.
Since $61450609>49999999$, it follows that, in both
the actual and declared common reference,
$$
 \boxed{\qquad
                 \|w_\gamma\|_{E_{4000}^+}
                           <2^{-49999998}.
 \qquad}                                                 \tag{SRH.12}
$$
This is uniform on the original domain. It improves the
order at which the same small bound is known; it does
not tighten or rerun the old order2960 computation.

For a convenient uniform high bound, use $d_{4224}>1/4$
in (SRH.10). Together with the seed bound this gives
$$
 \|w_\gamma\|_{E_{4224,c}^+}<2^{184174392},\qquad
 \|w_{\gamma'}-w_\gamma\|_{E_{4224,c}^+}
                                      <2^{184174393}.     \tag{SRH.13}
$$
The large number is finite and is not called a small
high norm. The exponent preceding the final widening
is $184549391-1500000/4=184174391$.

For every fixed finite iterate, T's original continuity
in $E_{1856}^+$ and locally uniform $E_{6396}^+$ bounds
give continuity at every order strictly below6396.
The uniform tail (SRH.10) therefore proves that the
same selected map is continuous through integer
order4224 for the original $H^{8193}$ parameter topology.
The actual chart $\mathcal U_\gamma$ retains the
corresponding strong-topology finite-order continuity;
the highest angular input needed here is4225, below
the original8193 window.

## 4. Relative L2 background continuity below the new top order

SHL.8 already proves the actual low estimate
$$
 \|w_{\gamma'}-w_\gamma\|_{E_{20,c}^+}
 \le L_0d,\qquad
 L_0=2^{-31222782},\quad
 d=\|(\gamma'-\gamma)/r_\gamma\|_2 .
$$
Combining it with (SRH.13) by the same complete graph
interpolation gives a new higher background modulus:
$$
 \boxed{\ 
 \|w_{\gamma'}-w_\gamma\|_{E_{j,c}^+}
 \le (L_0d)^{(4224-j)/4204}
          \big(2^{184174393}\big)^{(j-20)/4204},
                  \qquad20\le j<4224 .
 \ }                                                     \tag{SRH.14}
$$
Thus the selected graph is continuous in relative $L^2$
into every integer order through4223, in particular
into $E_{4000,c}^+$. The original parameter set is compact
in relative $L^2$ by SHL.12 and its high Fourier bound;
the corresponding $E_{4000,c}^+$ image is compact.

This conclusion uses the existing SHL low response
and the new actual high value bound. It does not yet
extend SHL's high-direction derivative window, and it
does not claim relative $L^2$ continuity at order4224.
No nonlinear value map on an open rough ball is created.

## 5. Exact-limit a priori estimates through output2204

At each exact selected background put
$$
                    P_\gamma=D_w\mathcal F_\gamma(w_\gamma).
$$
The original low a priori estimate remains unchanged.
The new high statement is
$$
 \boxed{\begin{aligned}
 \|h\|_{E_s^+}\le{}&
    2^{16777216}|P_\gamma h|_{s+1734}\\
 &+2^{71303172}|P_\gamma h|_{1794},
 \qquad h\in E_{4000,0}^+,\quad64\le s\le2204 .
 \end{aligned}}                                         \tag{SRH.15}
$$
This is in the actual reference; the same fixed
common-reference comparison is available when needed.
It applies to arbitrary-size linear directions.
Only the background is constrained by (SRH.12).

Here is the passage to the exact background, with every
needed order recorded. Let $\bar w_T=S_Tw_\gamma$.
The original finite-smooth proxy is defined at
$\mathcal U_\gamma(\bar w_T)$, which has the exact
nonlinear far graph and all its true holonomy and
first-principal components. By the same complete
weak/strong uniqueness used in SREG.11, the inverse
estimate S.24 gives its lower estimate on a smooth
direction. Strong lower-order cutoffs then give it
for all $h\in E_{4000,0}^+$.

The literal identity is still SREG.12:
$$
 \mathscr P_T h
  =D\mathcal F_\gamma(\bar w_T)[h]
            +P_\perp\mathcal E_{\mathcal U_\gamma(\bar w_T)}
                                                   [H_T(h)] .
                                                               \tag{SRH.16}
$$
It includes the full residual-sensitive holonomy error.
There is no deletion of that error at a finite
approximant and no second charge for a parameter lift.

For output $s\le2204$ the order ledger is:

| Actual input or comparison | Highest required order |
|---|---:|
| inverse high background $s+1796$ | 4000 |
| ordinary source $s+1734$ | 3938 |
| residual-sensitive source $s+1735$ | 3939 |
| internal coefficient $s+1742$ | 3946 |
| actual outer state $s+1780$ | 3984 |
| actual outer physical height $s+1782$ | 3986 |

The added B trace in $E_{4000}^+$ is its original
$2^{440}H^{4003}$ trace. All orders in this table fit
the same original network and cap windows; no
overall8193 network inverse is inferred.

Order4001 convergence from (SRH.10) supplies strong
cutoff convergence at4000, without asserting Fourier
density in the highest weighted radial norm. The
complete derivative-difference estimate from A.18
after S's exact chart therefore makes the first term
in (SRH.16) converge in the required operator/source
norms. The exact residual is zero, and the complete
nonlinear map is continuous to the source orders in
the table. The full approximating residual and its
mean lift consequently tend to zero there. Literal
A.17, with the uniformly bounded lower holonomy lift,
makes the second term in (SRH.16) tend to zero too.

The high inverse coefficient is the same one already
bounded in SREG.14: the new maximum background order
is still bounded by the same small numerical value,
now by (SRH.12). Thus $2^{71303172}$ remains valid.
Taking the actual proxy limit proves (SRH.15).

This argument never needs a bounded $E_{8192}$ norm
for the limiting background or its smoothing family.
All higher smoothing norms are finite at each fixed
cutoff, while the limit is taken only in the displayed
lower norms. It also does not assume an onto inverse
for arbitrary rough sources.

## 6. Fixed data, new use and limits

The statement concerns the exact same selector and
intrinsic data at each fixed gamma. The original
first-principal feedback, second seed parameter,
ordinary/holonomy means, actual B row, independent
charges and height constant remain distinct.
The old local uniqueness result remains valid and
was not re-proved or numerically repeated here.

The useful new inputs are:

- actual convergence and strong-topology continuity through4224;
- the uniformly small complete order4000 value bound;
- relative $L^2$ background continuity through4223;
- the exact-limit a priori output window through2204.

A subsequent high parameter-response proof must
still supply the full parameter forcing through3938
and its operator continuity in the larger background
window. This note does not promote an earlier
lower-order forcing theorem merely by changing an
index. The actual physical cap/core admissibility,
full finite/high/mean/parameter inverse, all world
and waist matching and the final closed fixed-metric
family remain independent obligations.

The companion
[fourfold_codazzi_selected_tail_residual_interpolation_saved_bounds.py](../scripts/fourfold_codazzi_selected_tail_residual_interpolation_saved_bounds.py)
records only17 new integer/rational comparisons for
the new exponents, whole summable tails and actual
order ledger. Their first exact evaluation passed in
the connected integer runtime. The preserved Python
reader was not run in the unavailable local executor.
There were zero new Nash steps and zero old scientific
targets or saved comparisons repeated.
