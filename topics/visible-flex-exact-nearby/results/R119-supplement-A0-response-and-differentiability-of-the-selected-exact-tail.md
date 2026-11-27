# R119 SDIF: A0 response and differentiability of the actual selected exact tail

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved.** The original deterministic S/T selection is Lipschitz in
the $A^0$ parameter distance at the low graph order. It has a genuine
linear parameter derivative, constructed from complete solution
differences without assuming a rough-source inverse. On the strict
$H^{8193}$ interior it is a continuously Frechet differentiable map
into every integer graph order through1164. Its derivative has the
displayed $A^0$ bound.

There is also a precise statement on the closed original domain:
the same linear response exists at its boundary, is continuous in
the operator topology $H^{8193}\to E_s^+$, and gives the relative
first-order expansion along all admitted $A^0$-small increments.
No value construction on an open $A^0$ ball is asserted. Continuity
of the response in the stronger operator topology
$A^0\to E_s^+$ is not inferred.

All parameters here belong to the original real-even physical
nonmean space on $4\mathbb Z$. The true seed-selected second
parameter and the entire first-principal response are part of
the derivative. This is not the final fixed-metric flex parameter.

## 1. The actual domain, equations and completed inputs

Use
[S](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md),
[T](R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md),
[SREG](R119-supplement-higher-regularity-of-selected-tail-and-local-uniqueness.md),
[SLIP](R119-supplement-quantitative-dependence-of-the-selected-exact-tail.md),
and
[GA](R144-supplement-separated-end-A0-parameter-forcing-with-complete-mixed-height.md).
The domain remains exactly
$$
 {\cal D}=\{\gamma\in H^{8193}_{\perp,\mathrm{ev}}:
       \|\gamma/r_\gamma\|_{A^0}\le1/128,\quad
       \|\gamma/r_\gamma\|_{H^{8193}}\le R\},\qquad
 R=2^{1048576},\quad r_\gamma=10^{-9}.                    \tag{SD.1}
$$
Its strict interior is taken in the real $H^{8193}$ subspace.
For a direction or difference set
$$
 |\eta|_X=\|\eta/r_\gamma\|_{A^0},\qquad
 |\eta|_Y=\|\eta/r_\gamma\|_{H^{8193}}.                    \tag{SD.2}
$$
The scaling is kept in every operator estimate.

Write $w_\gamma=w_\infty(\gamma)$ for the same selected nonmean
height in T.C14's common physical reference. The actual equation is
$$
 {\cal F}_\gamma(w_\gamma)=0,\qquad B_0w_\gamma=0,\qquad
 u_\gamma={\cal U}_\gamma w_\gamma,\qquad
 \mathfrak q(\gamma)=\Gamma_2^*(a_{94}(\gamma))-\bar\Gamma_2.
                                                               \tag{SD.3}
$$
The compact design bumps change neither $B_0$ nor the B scale.
All common/actual graph comparisons cost less than2.
The source $Z_j^{[3]}$ keeps its ordinary units, three broken
radial derivatives and original seams.

Put
$$
 A=2^{16777216},\qquad B=2^{71303172},\qquad
 K=2^{25165824},\qquad r=2^{-49000000}.                   \tag{SD.4}
$$
At each exact selected background SREG gives the actual-reference
a priori estimates
$$
 \|h\|_{20}\le A|P_\gamma h|_{1794},
 \quad h\in E_{1856,0}^+,\qquad
 P_\gamma=D_w{\cal F}_\gamma(w_\gamma),                  \tag{SD.5}
$$
and
$$
 \|h\|_s\le A|P_\gamma h|_{s+1734}
                    +B|P_\gamma h|_{1794},
 \quad h\in E_{2960,0}^+,\quad64\le s\le1164.             \tag{SD.6}
$$
These estimates apply to arbitrary size linear directions in the
stated spaces. Only their background is required small.
No onto assertion is substituted for (SD.5)--(SD.6).

GA supplies the actual operator
$$
 Q_{\gamma,w}=D_\gamma{\cal F}_\gamma(w):
                     X\longrightarrow Z_j^{[3]}.
$$
For all selected heights, including a height selected at a different
parameter, its complete bounds are
$$
 \|Q_{\gamma,w}\eta\|_{Z_j^{[3]}}
       \le2^{-48000000}|\eta|_X,\qquad20\le j\le2898.
                                                               \tag{SD.7}
$$
The bound follows from the one-high GA.14 before its simplification;
the common $E_{2960}^+$ selected bound is
$2^{-49999998}$, so every $W_{j+1}$ in this window is below1.
GA.16 proves joint continuity of this operator in
${\cal L}(X,Z_j^{[3]})$ for gamma in its relative $A^0$ topology
and $w$ in the common $E_{2960}^+$ topology.

The independent reference-height integral, rigid height constant,
and prescribed flux ports are not members of the vanishing
ordinary-source estimate (SD.7). Their full formulas remain those
of GF.24 and the original reconstruction.

## 2. A global A0 comparison on the original domain

For $\gamma,\gamma+\delta\in{\cal D}$ put
$$
 h=w_{\gamma+\delta}-w_\gamma,\qquad d=|\delta|_X.
$$
The complete mismatch of SLIP.4, now estimated by GA.17, satisfies
$$
 D_j\le2^{-48000000}d,\qquad20\le j\le2898.                \tag{SD.8}
$$
Use SLIP.9--SLIP.10, whose full quadratic absorption and source
units have already been proved. Paying the single output reference
factor2 gives
$$
 \boxed{\ \|h\|_{E_{20,c}^+}\le L_0d,\qquad
                      L_0=2^{-31222782}.\ }             \tag{SD.9}
$$
For every integer $64\le s\le1164$ it also gives
$$
 \|h\|_{E_{s,c}^+}
 \le\{2^{-31222783}+2^{23303174}\}d
 \le L_1d,\qquad L_1=2^{23303175}.                       \tag{SD.10}
$$
This retains the entire low-source term in the high inverse.
The high coefficient is not described as a contraction.

The physical nonmean chart and its true gamma variation give, by
the same exact decomposition as SLIP.14,
$$
 \boxed{\ \|u_{\gamma+\delta}-u_\gamma\|_{E_{20,c}^+}
                      \le2^{-31222778}d.\ }             \tag{SD.11}
$$
Indeed its fixed-gamma difference costs at most $8L_0d$ in the
common norm. GA.10, $W_{21}<1$ and one spare reference factor
bound the other term by $2^{-56868926}d$. The sum is below
the displayed coefficient. No affine endpoint term is discarded.

The same original normalized B-height satisfies
$F_B{\cal U}_\gamma w=F_Bw$, and the graph really includes
$2^{440}\|F_Bw\|_{H^{23}}$. Therefore
$$
 \boxed{\ \|f_B(\gamma+\delta)-f_B(\gamma)\|_{H^{23}}
                       \le2^{-31223222}d.\ }            \tag{SD.12}
$$
This is an actual transfer estimate for the existing interface
output. It does not identify the curvature input gamma with that
normalized height or construct a core self-map.

## 3. The stronger continuity needed in the parameter forcing

A low Lipschitz bound alone would not justify substituting a
selected solution in the high source operator. The following
uniform stronger bound supplies the missing argument.

At order3121, SREG.6 and its common-reference seed estimate give
$$
 \begin{split}
 \|w_\gamma\|_{E_{3121,c}^+}
 &\le2^{-49999999}
       +2^{184549391-1500000}\\
 &<2^{183049392}.
 \end{split}                                             \tag{SD.13}
$$
This is a uniform finite bound on the actual limit. It is not
an $E_{8192}$ claim. Hence any selected difference has norm
below $M=2^{183049393}$ at order3121.

The complete graph interpolation, with its genuine added trace
and weighted radial supremum, gives
$$
 \boxed{\ 
 \|w_{\gamma+\delta}-w_\gamma\|_{E_{j,c}^+}
 \le (L_0d)^{(3121-j)/3101}
          M^{(j-20)/3101},\qquad20\le j<3121 .
 \ }                                                     \tag{SD.14}
$$
In particular the selected map is continuous in the relative
$A^0$ topology into $E_{2960,c}^+$, with positive exponent
$161/3101$. The source remainder at order2898 has positive
exponent $223/3101$. Continuity at order3121 in the $A^0$
topology is not claimed.

For the uniform argument below, the domain $\mathcal D$ is compact in X.
To prove this directly, the $H^{8193}$ bound gives a uniformly
vanishing $A^0$ Fourier tail by Cauchy--Schwarz; each finite
coefficient set is bounded. An $A^0$ limit remains in the
$H^{8193}$ ball by the weak Hilbert lower bound on its norm,
and preserves the real-even, nonmean and $A^0$ constraints.
Thus the set is closed and totally bounded in $A^0$.

By (SD.14) its image
$\mathcal W=\{w_\gamma:\gamma\in{\cal D}\}$ is compact in
the common $E_{2960}^+$ graph. GA.16 on the compact set
$\mathcal D\times\mathcal W$ is therefore uniformly continuous
as an operator into every source order used below.
All pairs in this product remain in GA's true low domain:
the change from common to any admitted actual reference
still places the height strictly inside the radius r.

## 4. An actual first-order equation with a uniform small remainder

At fixed base gamma set
$$
 P_\gamma=D_w{\cal F}_\gamma(w_\gamma),\qquad
 Q_\gamma=D_\gamma{\cal F}_\gamma(w_\gamma).
$$
For an admitted difference $\delta$, Taylor's exact identity
and the exact selected equations give
$$
       P_\gamma h+Q_\gamma\delta
                            ={\cal E}_\gamma(\delta).    \tag{SD.15}
$$
Here the height remainder is the complete S.27 term.
In the actual reference, (SD.9) and its factor2 imply
$$
 \begin{split}
 {|\mathcal R_\gamma(h)|_j\over d}
 \le K\{&
  2L_0\|h\|_j\\
 &+4(1+\|w_\gamma\|_j)L_0^2d\}\longrightarrow0
 \quad(20\le j\le2898).
 \end{split}                                             \tag{SD.16}
$$
The convergence is uniform in the base point by (SD.14)
and the already uniform selected low bounds.
The affine and nonradial linear parts cancel only in this
fixed-gamma height remainder; they stay in the parameter term.

The other remainder is the actual integral
$$
 \int_0^1
 \{D_\gamma{\cal F}_{\gamma+t\delta}(w_{\gamma+\delta})
                   -D_\gamma{\cal F}_\gamma(w_\gamma)\}
                           [\delta]\,dt .               \tag{SD.17}
$$
GA's complete parameter derivative is used at every point.
The whole segment belongs to ${\cal D}$.
The compact uniform operator continuity just proved and
(SD.14) show that (SD.17), divided by d, tends to zero
uniformly in every $Z_j^{[3]}$ with $j\le2898$.

Consequently there are nondecreasing functions $\omega_j$,
tending to zero at zero, such that
$$
 |{\cal E}_\gamma(\delta)|_j
                  \le d\,\omega_j(d),\qquad20\le j\le2898,
                                                               \tag{SD.18}
$$
uniformly for $\gamma,\gamma+\delta\in{\cal D}$.
This proves a genuine first-order remainder. It does not
assume the selected map differentiable, nor infer a second
derivative of the first-principal value map.

## 5. Inward solution differences construct the derivative, including at the boundary

The domain is a closed intersection of two norm balls.
Ordinary two-sided difference quotients need not be admitted
at its boundary. Use actual inward differences instead.

For $|\eta|_Y\le1$ and $0<t<1/512$ put
$$
 \gamma_t^0=(1-256t)\gamma,\qquad
 \gamma_t^1=(1-256t)\gamma+t\eta,\qquad
 v_t(\gamma;\eta)
     ={w_{\gamma_t^1}-w_{\gamma_t^0}\over t}.             \tag{SD.19}
$$
Both parameters belong to the original domain. In the
normalized low norm,
$$
 |\gamma_t^1|_X
 \le(1-256t)/128+t=1/128-t,
$$
and in the high norm
$$
 |\gamma_t^1|_Y\le(1-256t)R+t\le R,
$$
because $256R>1$. The other parameter is an admitted radial
contraction. The two increments from gamma have X norms
at most $3t$ and $2t$, respectively.

Apply (SD.15) separately to these two increments at the
same actual background $w_\gamma$, then subtract:
$$
 P_\gamma v_t(\gamma;\eta)
        =-Q_\gamma\eta+e_t(\gamma;\eta),\qquad
 |e_t|_j\le5\omega_j(3t).                                \tag{SD.20}
$$
All comparisons use the one fixed linear $B_0=0$ space.
The full holonomy reconstructions in $P_\gamma$ are those
of SREG; no ordinary mean difference is dropped.

Each $v_t$ belongs to $E_{2960,0}^+$. It may have a large
higher norm when t is small, which is harmless: (SD.5)--(SD.6)
are a priori estimates on arbitrary linear directions.
For two positive parameters t and u their forcing terms in
(SD.20) cancel. Hence, in the common reference,
$$
 \|v_t-v_u\|_{20,c}
 \le2A\{5\omega_{1794}(3t)+5\omega_{1794}(3u)\},           \tag{SD.21}
$$
and, for $64\le s\le1164$, the analogous bound is the sum
of $2A$ times the source-order $s+1734$ remainder and
$2B$ times the source-order1794 remainder.
It tends to zero uniformly in gamma and in $|\eta|_Y\le1$.

Graph completeness constructs a common limit
$$
 V_\gamma[\eta]=\lim_{t\downarrow0}v_t(\gamma;\eta)
                         \quad\hbox{in }E_{1164,c}^+ .   \tag{SD.22}
$$
Its limits at all lower orders agree.
This is an existence proof for this specific parameter
response from actual solution differences. It assumes no
onto inverse on an arbitrary rough source.

To see linearity, first allow any finite set of directions and
choose a larger inward coefficient in place of256 so that
all their actual parameter pairs are admitted. Formula
(SD.20) is unchanged except for a fixed finite remainder factor.
Comparing two choices of inward coefficient by
(SD.5)--(SD.6) shows that the limit is independent of that choice.
For $\eta_1,\eta_2,\eta_1+\eta_2$, apply the same a priori
estimates to the corresponding linear combination of the
three finite differences. Its limiting source is zero
because $Q_\gamma$ is linear. The limit is therefore zero.
Scalar homogeneity follows in exactly the same manner,
including negative real scalars. Thus $V_\gamma$ is linear.

Taking (SD.5)--(SD.6) on $v_t$ before passing to its limit
also proves bounds depending on the X norm of the
direction, not on the inward coefficient or its high norm.
A convenient common bound is
$$
 \boxed{\begin{split}
 \|V_\gamma[\eta]\|_{E_{20,c}^+}
       &\le L_0|\eta|_X,\\
 \|V_\gamma[\eta]\|_{E_{s,c}^+}
       &\le L_1|\eta|_X,\qquad64\le s\le1164 .
 \end{split}}                                             \tag{SD.23}
$$
For example the direct low coefficient before this widening
is $2^{16777217-48000000}=2^{-31222783}$.
The full high coefficient is
$2^{-31222783}+2^{23303173}<L_1$.
No large low-source term was removed.

Finite even Fourier polynomials are dense in $A^0_{\perp,\mathrm{ev}}$.
The bounds (SD.23) therefore extend this linear operator
uniquely and boundedly to the full X direction space.
This extends a linear response, not the nonlinear value domain.

## 6. The relative Frechet expansion and the genuine C1 topology

Let $\gamma,\gamma+\delta\in{\cal D}$ and $d=|\delta|_X>0$.
The direction $\eta=\delta/d$ belongs to the original high
space, although its high norm need not be uniformly bounded.
Its response is already defined by linearity and the
independent inward construction.

Compare $h/d$ with an inward difference approximating
$V_\gamma[\eta]$. Both finite directions belong to
$E_{2960,0}^+$. Equations (SD.15),(SD.20) and the same
a priori estimates apply. Send the inward step to zero.
Using (SD.18) gives
$$
 \boxed{\ 
 \|w_{\gamma+\delta}-w_\gamma-V_\gamma[\delta]\|_{E_{s,c}^+}
                           =o(|\delta|_X),
 \quad s=20,\ 64,\ldots,1164 .
 \ }                                                     \tag{SD.24}
$$
The remainder is uniform on the closed original domain.
The statement includes its boundary, along admitted increments.
At no step was the unknown difference quotient assumed to
have a bounded $E_{1856}$ or $E_{2960}$ norm.

There is a precise operator continuity statement as well.
For fixed t, (SD.19) is continuous in its base gamma,
uniformly for $|\eta|_Y\le1$. Indeed (SD.9)--(SD.10) give
$$
 \sup_{|\eta|_Y\le1}
 \|v_t(\gamma;\eta)-v_t(\gamma';\eta)\|_{E_{s,c}^+}
 \le {2L_s(1-256t)\over t}\,|\gamma-\gamma'|_X,            \tag{SD.25}
$$
where $L_{20}=L_0$ and $L_s=L_1$ for $64\le s\le1164$.
The uniform convergence in (SD.21)--(SD.22) makes
$V_\gamma$ a continuous map
$$
 {\cal D}\ \longrightarrow\
 {\cal L}(H^{8193}_{\perp,\mathrm{ev}},E_{s,c}^+)          \tag{SD.26}
$$
even when the base set is given its relative $A^0$ topology.
Normalization by the fixed $r_\gamma$ does not change this
operator topology.

On the strict $H^{8193}$ interior, (SD.24) implies the usual
Frechet remainder in the $H^{8193}$ norm, and (SD.26)
proves continuity of that derivative. Thus the selected map
is genuinely C1 there. All intermediate graph orders
between20 and1164 follow by continuous inclusion.

Although each $V_\gamma$ has the bounded X extension (SD.23),
(SD.26) is not stated in ${\cal L}(X,E_s^+)$.
A fixed inward step in (SD.19) is uniformly admitted for the
high unit ball, not for every rough $A^0$ unit direction.
The original value family has not been enlarged to an
open $A^0$ ball.

## 7. The actual linearized equation and far readout

For the specific limits above the ordinary linearized
formula passes continuously from $v_t$ in the lower graph.
The reference source is a component of that graph; the
fixed low rational coefficients, three radial source jets,
holonomy mean derivative, L.15 first-principal derivative
and the actual nilpotent endpoint chart are bounded on
the lower direction norms in S.26a and A.18.

Consequently (SD.20) gives the genuine identity
$$
       P_\gamma V_\gamma[\eta]+Q_\gamma\eta=0,
                         \qquad B_0V_\gamma[\eta]=0 .    \tag{SD.27}
$$
It holds at least as a strong ordinary $Z_{20}^{[3]}$
identity, and in every lower source order paid by the
constructed direction. Its right side is the full actual
parameter forcing. This argument uses convergence of
these particular complete graph directions; it makes no
unproved top-order density assertion.

The changing seed parameter, the radial first compensation,
the complete first-principal feedback, original mean
projection and reference source are included in $Q_\gamma$.
The equation is not the fixed-metric Poisson column renamed.

For the actual nonmean height the exact chain rule is
$$
 D_\gamma u_\gamma[\eta]
   =D_w{\cal U}_\gamma(w_\gamma)V_\gamma[\eta]
                         +D_\gamma{\cal U}_\gamma(w_\gamma)[\eta].
                                                               \tag{SD.28}
$$
The chart's genuine first differences and remainders are
S.14--S.16; GA proves the complete parameter term.
They justify the relative first-order expansion and the
usual interior C1 statement in the common $E_{20}^+$ graph.
The same low coefficient as (SD.11) is valid:
$$
             \|D_\gamma u_\gamma[\eta]\|_{E_{20,c}^+}
                         \le2^{-31222778}|\eta|_X.        \tag{SD.29}
$$
The independent reconstructed scalar height, metric
reference integral, rigid height constant and world
frame ports must still be read through their genuine
operators; (SD.29) concerns the physical nonmean height.

Finally the B-height is a fixed continuous linear readout:
$$
 \boxed{\ 
 D_\gamma f_B[\eta]=F_BV_\gamma[\eta],\qquad
 \|D_\gamma f_B[\eta]\|_{H^{23}}
                         \le2^{-31223222}|\eta|_X .
 \ }                                                     \tag{SD.30}
$$
All exact mean/root constraints and the true normalized
physical scale of this readout remain unchanged.
There is no free radial trace and no phase normalization.

## 8. Scope and new arithmetic

This completes actual selected-tail parameter differentiability
in the stated finite window, with a true $A^0$ operator cost,
a uniform relative expansion on its closed value domain,
and the explicitly stated high-direction C1 operator topology.
The proof uses the complete forced equation and difference
quotients of already constructed solutions. It does not
invoke an equal-order implicit-function theorem.

No general rough-source onto result, selected $E_{1856}$
derivative, $E_{8192}$ limit, second selected derivative,
core inverse, full nu/phase Schur or final closed embedded
fixed-metric family is asserted. Independent physical
means, height/rigid ports, all B/C/Cmean matching and
the final geometry obligations remain.

The companion reader records only the new integer
combinations of the completed SREG, GA and SLIP constants.
The first evaluation uses exact safe integer arithmetic
after the local execution environment became unavailable.
No old seed, norm, carrier, PDE or scientific target is run.
