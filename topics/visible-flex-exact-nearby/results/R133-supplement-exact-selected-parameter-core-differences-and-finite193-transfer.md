# R133 supplement: exact selected-parameter core differences and the finite193 transfer criterion

2026-11-15, visible-exact-astra-0df9.

**Proved analytic identities and a quantitative conditional transfer theorem.**
This note puts the old finite193 core inverse and the selected phase
parameter in the same physical moving variables. It proves explicit
ordinary-source and boundary perturbation budgets, including the true
mean and the intrinsic parameter column. The final finite feedback
inequalities must still be verified with actual Green and Poisson
gains. An inherited metadata parameter width is not such a verification.

## 1. The actual family and the unchanged intrinsic choices

Use the exactly continuous centre $Q_0$ with definition
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47,
and the exactly continuous physical response $Z$ with definition
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
The core interval is $[0,L]$, where $L=9/10$. The family is
$$
 Q_\delta=Q_0+\delta Z,\qquad \nu_\delta=\nu_0+\delta,\qquad
 |\delta|\le d:=10^{-10},\qquad \eta=\eta_0.
 \tag{D.1}
$$
The [actual selected-family theorem](R133-supplement-selected-family-root-finite-part-and-actual-first-phase.md)
puts its selected $\delta_*$ strictly inside (D.1).
The moving Fourier degrees are $32$ for $Q_0$ and $96$ for $Z$.
The true scalar reference in $v_0$ is included in its mean.

Write $G=\gamma_{\nu_0}>0$, $K=K_{\nu_0}$, and $\beta=a'/a$.
The original metric definition $E_\nu=E_{\nu_0}\exp((\nu-\nu_0)w)$ gives
$$
 G_\delta=Ge^{\delta w/2},\qquad
 K_\delta=e^{-\delta w}(K+\delta T w'),\qquad
 T=\frac{\beta}{2G^2a^2}.
 \tag{D.2}
$$
Here $T$ is a base radial coefficient, not the canonical fold coordinate.
The functions $a,\beta$ and $\eta_0$ do not change.
The compact weight and its derivative vanish outside $[1/20,9/50]$;
the old exact inequalities $|w|\le1$, $|w'|\le2400/13$ may be used
on its support. No reference-state $\partial_\nu s$ is added to the
physical source.

The original full moving formula is (Q.4) of
[the complete moving operator](R133-supplement-negative-quadratic-density-and-full-frequency-transport.md).
The existing exact implementation is
[scripts/fourfold_codazzi_complete_response_repair_source.py](../scripts/fourfold_codazzi_complete_response_repair_source.py),
functions operator_fee and parameter_fee. Its original 7721 rows are
inputs to a later new consumer; this theorem does not recompute them.

## 2. Full first-order operator and pointwise difference

Let $I=I_\phi=\partial_\phi^{-1}P_{\ne0}$ on the normalized
$4\mathbb Z$ circle, and
$$
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\quad
 S=u^2+Kv^2,\quad m=\langle v\rangle_\phi,\quad d_Q=-\beta I S .
$$
The actual nonlinear field is
$$
 F(Q,\nu)=(d_Q I_2+GmJ(K))Q_\phi+\beta(-u,v)-\beta SQ .
 \tag{D.3}
$$
For $h=(h_1,h_2)$ its complete differential is
$$
 \begin{aligned}
 A(Q,\nu)h={}&(d_QI_2+GmJ(K))h_\phi+L(Q,\nu)h\\
 &-2\beta Q_\phi I(uh_1+Kvh_2)
       +G\langle h_2\rangle_\phi J(K)Q_\phi,\\
 L={}&\begin{pmatrix}
 -\beta(1+3u^2+Kv^2)&-2\beta Kuv\\
 -2\beta uv&\beta(1-u^2-3Kv^2)
 \end{pmatrix}.
 \end{aligned}
 \tag{D.4}
$$
The last rank-one mean term and the mean in the principal coefficient
are both retained.

At a fixed radial point or on a complete real cell put
$$
 b\ge|\beta|,\ g\ge G,\ k\ge|K|,\ t\ge|T|,\quad
 W\ge|w|,\ W_1\ge|w'|.
$$
Let $Q_0^{\#},Q_1^{\#}$ bound the full pair $A^0$ norms of $Q_0$
and $(Q_0)_\phi$, and let
$$
 E_0\ge d\|Z\|_{A^0,\mathrm{pair}},\quad
 E_1\ge d\|Z_\phi\|_{A^0,\mathrm{pair}},\quad
 E_m\ge d|\langle Z_2\rangle_\phi|,\quad m_0^{\#}\ge|m_0|.
$$
One can use the already certified wider full-body bounds
$Q_0^{\#}=7,Q_1^{\#}=6,E_0=19d,E_1=83d,E_m\le E_0$;
the exact original complete cell bounds may be substantially sharper.
For $Q_0^{\#},Q_1^{\#}$ the original full-body raw bounds are
$6.406213,5.437241$, and the complete centre-repair fees are below
$3.861\,10^{-18},1.970\,10^{-17}$, respectively, in the
[actual response-repair summary](../notes/response_repair_source_ci/run-43597921732-1-complete-known-response-centre-repair/evidence/complete-known-response-centre-repair-source-summary.json).
The source of the response bounds and repair fee is given in
[the selected-parameter cap rows](R133-supplement-selected-parameter-cap-row-transfer-with-unknown-high-input.md),
(Cδ.1)--(Cδ.3).

Define
$$
 \begin{aligned}
 G_+&=g e^{dW/2},&
 K_+&=\max\{1,e^{dW}(k+dtW_1)\},\\
 k_\Delta&=(e^{dW}-1)k+d e^{dW}tW_1,\\
 J_\Delta&=g\max\{(e^{dW/2}-1)k+d e^{dW/2}tW_1,\
                                  e^{dW/2}-1\},\\
 \Delta S_Q&=K_+\{2Q_0^{\#}E_0+E_0^2\}.
 \end{aligned}
 \tag{D.5}
$$
Then $k_\Delta$ bounds $|K_\delta-K|$ and $J_\Delta$ bounds the
Euclidean matrix norm of $G_\delta J(K_\delta)-GJ(K)$.
The latter uses the exact product
$G_\delta K_\delta=Ge^{-\delta w/2}(K+\delta Tw')$.
The term $\Delta S_Q$ bounds only the state difference at the new
metric; the intrinsic contribution $k_\Delta(Q_0^{\#})^2$ is separate.

Set
$$
 \begin{aligned}
 M_1={}&b\Delta S_Q/4+G_+K_+E_m
              +bk_\Delta(Q_0^{\#})^2/4+m_0^{\#}J_\Delta,\\
 M_0={}&3b\Delta S_Q
       +\frac{bK_+}{2}\{E_0Q_1^{\#}+(Q_0^{\#}+E_0)E_1\}
       +G_+K_+E_1\\
       &+3bk_\Delta(Q_0^{\#})^2
              +\frac{bk_\Delta}{2}Q_0^{\#}Q_1^{\#}
              +J_\Delta Q_1^{\#}.
 \end{aligned}
 \tag{D.6}
$$
For every angular $H^1$ input, including its genuine even mean,
$$
 \boxed{\quad
 \|(A(Q_\delta,\nu_\delta)-A(Q_0,\nu_0))h\|_2
              \le M_1\|h_\phi\|_2+M_0\|h\|_2 .
 \quad}
 \tag{D.7}
$$

To prove this, first change $Q_0$ to $Q_\delta$ with the new metric
held fixed, then change that metric with $Q_0$ held fixed.
The primitive has the exact $L^2$ norm $1/4$.
The cubic local differential is
$-\beta(SI_2+2Q(u,Kv))$ up to its fixed linear part.
Its state change has norm at most $3b\Delta S_Q$.
The two changed factors in the nonlocal row cost
$bK_+\{E_0Q_1^{\#}+(Q_0^{\#}+E_0)E_1\}/2$.
The principal mean and the rank-one mean respectively give
$G_+K_+E_m$ and $G_+K_+E_1$.
At fixed $Q_0$ the same four estimates give the remaining terms in
(D.6), using $k_\Delta,J_\Delta$.
This proves (D.7) without treating a first-order difference as an
order-zero full-frequency operator.

## 3. Actual finite support and ordinary source units

Let $P=P_{\le96}$ be the original moving Fourier projection,
including the even mean and all 96 odd and 96 nonmean even modes.
Let $H=1-P$. The quadratic coefficients of (D.4) have degree at most
192 on the selected family. The primitive and mean rows do not enlarge
this support. Consequently
$$
 \begin{aligned}
 \|P(A_\delta-A_0)Ph\|_2
       &\le (M_0+384M_1)\|Ph\|_2,\\
 \|P(A_\delta-A_0)Hh\|_2
       &\le (M_0+1152M_1)\|P_{97\le|j|\le288}h\|_2,\\
 \|H(A_\delta-A_0)Ph\|_2
       &\le (M_0+384M_1)\|Ph\|_2 .
 \end{aligned}
 \tag{D.8}
$$
The last output is also supported in $|j|\le288$.
The numbers $384=4\cdot96$ and $1152=4\cdot288$ use the physical
angular frequency. A subsequent $H^s$ output bound must pay its
actual factor $\Lambda_{288}^s$.

The old M32-only shell $97,\ldots,160$ is not used for (D.8).
Nor is the new finite band transferred through a physical-angle
composition, an old-circle inverse, or a phase conjugacy.

For example, if
$$
 e=\operatorname*{ess\,sup}_{0\le r\le L}(M_0+384M_1),\qquad
 e_{LH}=\operatorname*{ess\,sup}_{0\le r\le L}(M_0+1152M_1),
 \tag{D.9}
$$
then these are ordinary $L^2_rL^2_\phi$ source operator fees on the
core $[0,L]$. Original one-sided pieces and compact-weight seams
must all be included in that supremum. A weighted original-source
consumer may use the full cellwise (D.6) instead, keeping its exact
measure and source norm. No new value of (D.9) is asserted here.

## 4. A genuine two-output finite feedback theorem

Let $G_0$ denote the complete old finite193 inverse of
$\partial_r-PA_0P$ with the original 96 waist rows and 97 actual
right rows. Let $R_0$ denote its complete right Poisson column.
Use one common Hilbert normalization for states, ordinary sources
and the orthonormal 97 boundary rows. For output
$Y=B$ (whole core $L^2$), $Y=C$ (actual right state trace), or
$Y=N$ (the required negative interval), assume actual bounds
$$
 \|G_0 f\|_Y\le g_Y\|f\|_{L^2_rL^2_\phi},\qquad
 \|R_0b\|_Y\le p_Y\|b\|_{\mathbb R^{97}} .
 \tag{D.10}
$$
If an old certificate uses a different pair norm, its conversion
must be made explicitly before calling its number $g_Y$.
The $g_Y$ are generic ordinary-source gains; they are not the
already specialized body-cross gains $a_Y$.

Suppose the new right boundary operator is $\mathcal B_0+\Delta\mathcal B$
and
$\|\Delta\mathcal B\,P\|_{L^2_\phi\to\mathbb R^{97}}\le\epsilon_L$.
The preceding cap-row theorem supplies the complete coordinate fee
$<10^{-4}$, with the separate true physical-cap fee (Cδ.27) if needed.
The waist rows have the original unchanged linear form; all affine
waist data remain on the right-hand side.

For new right-hand-side data let $u_0$ be the old inverse applied
to those data, with known output bounds $d_Y$.
The exact finite equation is
$$
 u=u_0+G_0P(A_\delta-A_0)Pu
                    -R_0\Delta{\cal B}\,u(L).
 \tag{D.11}
$$
Work on the product space of the whole-body $L^2$ state and an
independent finite-dimensional cut state. Apply the right side
and its actual cut trace to these two coordinates. Its nonnegative
Lipschitz matrix is
$$
 {\cal M}=
 \begin{pmatrix}
 g_Be&p_B\epsilon_L\\
 g_Ce&p_C\epsilon_L
 \end{pmatrix}.
 \tag{D.12}
$$
If
$$
 {\cal M}_{11}<1,\quad {\cal M}_{22}<1,\quad
 (1-{\cal M}_{11})(1-{\cal M}_{22})
                  -{\cal M}_{12}{\cal M}_{21}>0,
 \tag{D.13}
$$
then $\rho({\cal M})<1$. A positive weighted product norm makes
this map a contraction. Reconstruction by the actual old Green
operator ensures that the fixed cut coordinate equals the trace
of its fixed body solution. There is no use of an unbounded trace
map on arbitrary body $L^2$ functions.

Writing $(x_B,x_C)^t$ for its bounds gives
$$
 \binom{x_B}{x_C}
 \le(I-{\cal M})^{-1}\binom{d_B}{d_C},\qquad
 \|u\|_Y\le d_Y+g_Ye\,x_B+p_Y\epsilon_Lx_C .
 \tag{D.14}
$$
This applies in particular to $Y=N$. It proves uniqueness and
existence of the actual finite BVP if the complete gates (D.13)
are paid. It is not an inverse on the full infinite-frequency
core space.

The already certified old source correlations can be retained.
If $a_Y$ bounds the old complete column $G_0P A_0H$ on a unit
high state in the whole-body $L^2$ norm, the new load is bounded by
$$
 d_Y^{\rm body}=a_Y+g_Ye_{LH}.
 \tag{D.15}
$$
If $c_Y$ is the old signed high-cap column and
$\|\Delta\mathcal B\,H\|\le\epsilon_H$, use
$$
 d_Y^{\rm cap}=c_Y+p_Y\epsilon_H.
 \tag{D.16}
$$
For a new unit independent regular row use $d_Y=p_Y$.
Apply (D.14) separately to these columns. The cap-row theorem
bounds both $\epsilon_L$ and $\epsilon_H$ in their genuine full
input norms. No dimension factor or false entrywise Gram
majorant is needed.

## 5. The true intrinsic parameter source and response defect

At fixed physical moving state $Q$, differentiate (D.3) in $\nu$:
$$
 F_\nu(Q,\nu)=-\beta K_\nu
                  \{I(v^2)Q_\phi+v^2Q\}
                      +mJ_\nu Q_\phi,
 \quad J_\nu=\partial_\nu(GJ(K)).
 \tag{D.17}
$$
On the explicit family the exact radial coefficients are
$$
 \begin{aligned}
 (K_\nu)_\delta&=e^{-\delta w}
                 (Tw'-wK-\delta wTw'),\\
 (J_\nu)_\delta&=
 \begin{pmatrix}
 0&Ge^{-\delta w/2}
       \{Tw'-(w/2)(K+\delta Tw')\}\\
 -(w/2)Ge^{\delta w/2}&0
 \end{pmatrix}.
 \end{aligned}
 \tag{D.18}
$$
In particular this entire ordinary source is exactly zero outside
the compact metric support. Its Fourier degree may reach 288;
the 96-state label of $Z$ does not truncate (D.17).

For an explicit positive fee put
$$
 \begin{aligned}
 K_{\nu,+}&=e^{dW}\{tW_1+Wk+dWtW_1\},\\
 J_{\nu,+}&=g e^{dW/2}
       \max\{tW_1+(W/2)(k+dtW_1),W/2\},\\
 k_{\nu,\Delta}&=(e^{dW}-1)(tW_1+Wk)
                             +d e^{dW}WtW_1,\\
 J_{\nu,\Delta}&=g\max\{
  (e^{dW/2}-1)(tW_1+Wk/2)
                          +(dW/2)e^{dW/2}tW_1,\
  (W/2)(e^{dW/2}-1)\}.
 \end{aligned}
 \tag{D.19}
$$
These bound the two coefficients and their differences from
$\delta=0$. Define
$$
 U=2Q_0^{\#}E_0+E_0^2,\qquad V=(Q_0^{\#}+E_0)^2 .
$$
Changing first the state, then the metric, in (D.17) gives
$$
 \begin{aligned}
 \|F_\nu(Q_\delta,\nu_\delta)-F_\nu(Q_0,\nu_0)\|_2
 \le {\cal N}_\nu:={}&
 bK_{\nu,+}\{UQ_1^{\#}/4+VE_1/4+UQ_0^{\#}+VE_0\}\\
 &+J_{\nu,+}\{E_mQ_1^{\#}+(m_0^{\#}+E_m)E_1\}\\
 &+bk_{\nu,\Delta}\{(Q_0^{\#})^2Q_1^{\#}/4
                                      +(Q_0^{\#})^3\}\\
 &+m_0^{\#}J_{\nu,\Delta}Q_1^{\#}.
 \end{aligned}
 \tag{D.20}
$$
This follows directly from the actual primitive norm, complete
mean and product differences. It is valid on every original
one-sided cell, and is set exactly to zero off the compact support.

Let $\mathcal D_\delta=\partial_r-A(Q_\delta,\nu_\delta)$ and define
the trial response defect with the positive parameter-source convention
by $s_\delta=F_\nu(Q_\delta,\nu_\delta)-\mathcal D_\delta Z$. Then
$$
 s_\delta=s_0+
       \{F_\nu(Q_\delta,\nu_\delta)-F_\nu(Q_0,\nu_0)\}
                         +(A_\delta-A_0)Z .
 \tag{D.21}
$$
The last sign is plus. Thus the additional ordinary source is bounded
pointwise by
$$
 {\cal N}_\nu+M_1\|Z_\phi\|_{A^0,\mathrm{pair}}
                         +M_0\|Z\|_{A^0,\mathrm{pair}} .
 \tag{D.22}
$$
For clarity, $s_\delta$ is the negative of
$\partial_\delta\{(Q_\delta)_r-F(Q_\delta,\nu_\delta)\}$.
These two sign conventions must not be interchanged.

If the actual parameter boundary source is $b_{\nu,\delta}$, the
corresponding trial defect is
$$
 b_{\nu,\delta}-{\cal B}_\delta Z
 =(b_{\nu,0}-{\cal B}_0Z)
       +(b_{\nu,\delta}-b_{\nu,0})-\Delta{\cal B}\,Z(L).
 \tag{D.23}
$$
Its full 97-row norm, independent waist data and any genuine
particular-source traces remain part of the input to (D.11).
A changed prescribed-data column is not silently set to zero.

## 6. Remaining actual gates

The old finite negative-window response error
$.003509417445587$ and the separate whole-core value
$.007490301792401$ are distinct output estimates. Formula (D.14)
can transfer their appropriate negative and cut source columns
only after (D.9)--(D.13), (D.20)--(D.23) and the complete actual
boundary comparison have been evaluated in the same normalization.
Neither number is already a full-frequency $\nu$ response error.

The complete high inverse, its body and actual cut readouts, and
the finite/high Schur gate are still required by
[the quantitative strong-return theorem](R133-supplement-quantitative-strong-return-inverse-and-core-high-block-gates.md).
The physical fourth Robin row and independent mean remain regular
boundary rows. The design parameter $\nu$ solves the true phase
condition; the waist amplitude is an output, not an added fixed
amplitude row.

Finally, (D.1) is still an explicit approximate state family.
The exact full core, the physical inner-data gates and nonlinear
matching must be constructed at the selected final metric.
This theorem makes their same-parameter finite transfer explicit;
it does not replace any of them by a metadata interval.
