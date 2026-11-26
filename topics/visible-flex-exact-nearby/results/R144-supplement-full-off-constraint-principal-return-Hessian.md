# R144 RP: the complete off-constraint principal return Hessian

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved on a common real neighbourhood, including the metric direction; all32 new saved-rational comparisons pass.**
The complete principal two-ray return and the unnormalized phase
invariance equation have uniform estimates
\[
 \|D^2P[a,b]\|_2<530N(a)N(b),\qquad
 \|\partial_\phi DP[a]\|_2<150N(a),                         \tag{RP.1}
\]
\[
 \|D^2E[x,y]\|_2\le400\{\mathcal H(x)\mathcal E(y)
                         +\mathcal H(y)\mathcal E(x)\}.    \tag{RP.2}
\]
Here \(N(h,\kappa)=\|h\|_{L^2_rL^2_\phi}+100|\kappa|\);
\(\kappa\) is the actual \(\nu\) direction. The phase-direction
norms are specified below. No exact conjugacy or solved PDE is assumed
at the background. Both rays, the full even mean, true root, direct
metric terms and phase constant remain.

This pays a low-order phase Hessian required by
[PD.25](R133-supplement-complete-phase-row-approximate-inverse-and-quadratic-defect.md).
The existing one-step identities and divisor estimate are reused.
The complete regular inverse, parameter Schur lower and convergence
are not asserted here.

## RP1. The common domain and exact field

Fix \(\eta_0\), the original continuously repaired degree32 state
\(Q_0\), and the true root \(r_*\). The metric control is supported in
\(C=[1/20,9/50]\) and leaves \(r_*\) fixed. Use the convex domain
\[
 |\nu-\nu_0|\le10^{-10},\quad r_*<.239,\quad
 \sup_r\|Q-Q_0\|_{A^0}\le2\,10^{-6},\quad
 \sup_r\|(Q-Q_0)_\phi\|_{A^0}\le3\,10^{-6}.                 \tag{RP.3}
\]
Pair norms are Euclidean, as in TH. Circle measure is normalized on
period \(\pi/2\), with physical frequencies \(4\mathbb Z\).
Both one-sided values at the original interfaces enter the suprema.
Directions are first smooth; the estimates then extend to the
displayed Hilbert modules at these strong backgrounds. An unrestricted
rough Hilbert ball is not a nonlinear value domain.

[SM.25--SM.29](R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md)
and [TH.21](R144-supplement-complete-low-norm-tame-Hessian-and-mean-preserving-smoothing.md)
put every \(\widetilde Q_\delta+e\) with complete component-sum
\(\sup_r\|e\|_{A^3}\le10^{-6}\) in (RP.3): the compact-to-raw
bounds are \(4.739\,10^{-7}\) and \(1.255\,10^{-6}\), and the
continuous repair adds \(3.861\,10^{-18}\) and \(1.970\,10^{-17}\).
The same completed margins give
\[
 \|Q\|_{A^0},\ \|Q_0\|_{A^0},\
                  \|(Q_0)_\phi\|_{A^0}<7 .               \tag{RP.4}
\]
Only \(Q_0\) is assigned finite angular support.

Keep the original complete characteristic fields
\[
 F_\sigma=\beta I(u^2+Kv^2)-\sigma cm,\quad
 m=\langle v\rangle,\quad c=\gamma q,\quad q=\sqrt{-K},
 \quad I=\partial_\phi^{-1}P_{\ne0},\quad \sigma=\pm1 .
                                                               \tag{RP.5}
\]
The selected intrinsic bounds and NR give on the negative interval
\(|\beta|<2,\gamma<7,0\le q<1.03\), and \(q>.5338\) on \(C\).
TH.7 gives the whole-body bound
\(|\beta|\|\operatorname{diag}(1,K)\|<6\).
These are for the same selected metric interval.

## RP2. Both rays are one chronological flow

Define, for \(0\le t\le2r_*\),
\[
 V(t,\phi)=
 \begin{cases}
 F_+(t,\phi),&t\le r_*,\\
 -F_-(2r_*-t,\phi),&t\ge r_* .
 \end{cases}                                                 \tag{RP.6}
\]
The solution \(X_t=V(t,X), X(0,x)=x\) has the exact terminal map
\[
 X(2r_*,x)=H_-(r_*)^{-1}(H_+(r_*,x))=P(x).                 \tag{RP.7}
\]
The second leg is the full reverse flow with its actual terminal
input. No derivative of an inverse endpoint is omitted.
The possible velocity jump at \(t=r_*\) gives no state impulse.
Original radial coefficient interfaces are concatenated with the
same continuous flow, without differentiating an enclosure in \(r\).

Here \(P\) is the original moving-angle return P.7--P.8.
Its physical counterpart retains the exact waist chart:
\[
                    P_\theta=\Theta_0P\Theta_0^{-1}.       \tag{RP.8}
\]
The two root charts cancel as maps, exactly as P.9 proves; neither
is replaced by the identity. Section RP7 retains the full
off-constraint relation between the phase equations in these charts.

## RP3. Actual uniform angular budgets

The completed same-centre
[P.25](R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md)
gives
\[
 L_0=\int_0^{r_*}\|(F_{\sigma,0})_\phi\|_\infty dr
                                      <.036374621 .        \tag{RP.9}
\]
The scalar speed has no angular derivative, so the two signs use
the same bound. The known differentiated drift has degree at most64,
or physical frequency at most256. The trigonometric Bernstein
inequality gives
\(\int\|(F_{\sigma,0})_{\phi\phi}\|_\infty\le256L_0\).
This support assertion is only for the known \(Q_0\).

Put \(\epsilon_0=2\,10^{-6},\epsilon_1=3\,10^{-6}, B=6,d=10^{-10}\).
TH.11 supplies \(|\beta\partial_\nu K|<4\).
Subtracting the exact quadratic drifts at the same angle gives
the complete one-leg integral increments
\[
 \begin{split}
 \Delta_1&=2B(14\epsilon_0+\epsilon_0^2)(.239)
                                      +2(4)d(49)(.13),\\
 \Delta_2&=2B(7\epsilon_1+7\epsilon_0+\epsilon_0\epsilon_1)(.239)
                                      +2(4)d(49)(.13).
 \end{split}                                                 \tag{RP.10}
\]
The first factor two pays \(P_{\ne0}\) on \(L^\infty\).
For the second angular derivative the constant is gone and
the exact expression is \(2\beta Q^tD_KQ_\phi\).
The metric change is supported only on \(C\).
It follows on the entire folded interval, and every shorter
chronological interval, that
\[
 L:=\int\|V_\phi\|_\infty<.074,\qquad
 L_2:=\int\|V_{\phi\phi}\|_\infty<19.                       \tag{RP.11}
\]
These are new nearby-background combinations of completed integrals,
with only real \(A^1\) control of the unknown.

Set \(J=27/25,C_J=26/25\). The elementary
\(e^x\le(1-x)^{-1}\), for \(0\le x<1\), gives
\[
 e^L<J,\quad J^{-1}<X_x<J,\qquad
              \|f\circ X(t,\cdot)\|_2\le C_J\|f\|_2.       \tag{RP.12}
\]
The composition bound is the exact change-of-variables bound
\(\sqrt J<C_J\). The same bounds hold on each shorter forward
or reverse characteristic. No sampled Jacobian is used.

## RP4. Complete metric derivatives and their support

The saved complete lower in
[SJA2--SJA4](R133-supplement-actual-complete-strict-radial-first-symbol-defect.md)
is
\[
 \gamma>1.037358753383131215741741470992565155029296875>1 .
\]
Its original \(|\nu-\nu_0|\le10^{-8}\) interval and cut beyond
\(9/50\) cover \(C\) here. It is intrinsic and independent of \(Q\).

Let \(C_\nu=\gamma\left(\begin{smallmatrix}0&K\\-1&0\end{smallmatrix}\right)\),
using TH.6's parameter-labelled matrix.
TH.11 gives \(\|\partial_\nu C_\nu\|<24\), while \(|K|<1.061\).
Exact differentiation therefore gives on \(C\)
\[
 c_\nu=-\frac{\partial_\nu(\gamma K)+K\partial_\nu\gamma}{2q},
 \quad |c_\nu|<47,\quad c>\tfrac12 .                       \tag{RP.13}
\]
In (RP.13)--(RP.17), subscripts on \(c,K\) mean partial derivatives.

There is also an exact cancellation. Since
\(\gamma^2=E_\nu/a^2\) and
\(K_\nu=-wK+\beta w'/(2E_\nu)\),
\[
 \partial_\nu(\gamma^2K)=\frac{\beta w'}{2a^2},\quad
 \partial_\nu^2(\gamma^2K)=0,\quad
 c_{\nu\nu}=-c_\nu^2/c,\quad |c_{\nu\nu}|<4418 .             \tag{RP.14}
\]
The radial \(a,\beta,w\) do not depend on \(\nu\).
Furthermore \(0\le w\le1\) and
\[
 K_{\nu\nu}=-2wK_\nu-w^2K,\qquad
                              |\beta K_{\nu\nu}|<14 .     \tag{RP.15}
\]
All these metric derivatives are exactly zero outside \(C\).
That identity is applied before division by \(q\); there is no
singular metric source at the true root or extra seam impulse.

## RP5. Low Hilbert modules for the actual field

For \(a=(h,\kappa)\), let
\[
 E_h=\|h\|_{L^2([0,r_*];L^2_\phi\oplus_2L^2_\phi)},\qquad
                         N(a)=E_h+100|\kappa| .            \tag{RP.16}
\]
There is no \(\alpha\), waist-density or artificial parameter
normalizer in \(\kappa\). The complete field differentials are
\[
 \begin{split}
 D_QF_\sigma[h]&=2\beta I(Q^tD_Kh)-\sigma c\langle h_2\rangle,\\
 D_Q^2F_\sigma[h,k]&=2\beta I(h^tD_Kk),\\
 \partial_\nu F_\sigma&=\beta K_\nu I(v^2)-\sigma mc_\nu,\\
 D_Q\partial_\nu F_\sigma[h]&=2\beta K_\nu I(vh_2)
                                  -\sigma c_\nu\langle h_2\rangle,\\
 \partial_\nu^2F_\sigma&=\beta K_{\nu\nu}I(v^2)-\sigma mc_{\nu\nu}.
 \end{split}                                                 \tag{RP.17}
\]
All even means remain.

P.20--P.25 give the sharper original value receiver
\[
 a_0=2|\beta|c_I R_0+\gamma_0,\quad
 c_I=\|I:L^2\to L^\infty\|<1/2,\quad
                         \|a_0\|_{L^2_r}<.591950779 .
\]
The complete selected metric-change bound
\(|K-K_0|<1.048\,10^{-7}\) from
[PH.10](R147-supplement-exact-nonlocal-phase-and-height-parameter-ports.md)
is only restricted from its wider parameter interval.
On \(C\),
\[
 |q-q_0|<\frac{1.048\,10^{-7}}{2(.5338)},\qquad
 R_Q-R_0\le1.03\epsilon_0+7|q-q_0|<3\,10^{-6}.
\]
Outside \(C\), the metric change vanishes. Also
\(|\gamma-\gamma_0|<4\,10^{-10}\).
Thus \(a_Q\le a_0+10^{-5}\), and the full negative interval satisfies
\[
 \|a_Q\max(1,q)\|_{L^2_r}
 <1.03(.591950779+.49\,10^{-5})<.610 .                      \tag{RP.18}
\]
This transfers the receiver to all backgrounds (RP.3), including
the true root interval and both state means.

Folding both legs now gives
\[
 A(a):=\int_0^{2r_*}\|D_aV[a]\|_\infty dt\le2N(a).           \tag{RP.19}
\]
The state part costs \(2(.610)E_h\).
The complete metric field has norm below430 by (RP.13)--(RP.17),
so its folded support costs \(.26(430)|\kappa|<200|\kappa|\).

For the angular derivative, use the complete \(L^2\) contraction
of the nonmean projection:
\[
 \|(D_QF_\sigma[h])_\phi\|_2\le84\|h\|_2,\qquad
             \|(\partial_\nu F_\sigma)_\phi\|_2<200 .
\]
Since \(2\sqrt{r_*}<1\), these give
\[
 A_1(a):=\int_0^{2r_*}\|\partial_\phi D_aV[a]\|_2dt
                                                     \le84N(a). \tag{RP.20}
\]

The normalized periodic primitive has convolution kernel bounded
by \(\pi/4<1\), so \(\|I:L^1_{\rm normalized}\to L^\infty\|<1\).
The state--state term in (RP.17), after both legs and radial
Cauchy--Schwarz, therefore costs at most \(24E_hE_k\).
The mixed field costs less than \(76\|h\|_2\) on \(C\), giving
less than \(55(E_h|\lambda|+E_k|\kappa|)\).
The pure metric field is below32000 and costs less than
\(8320|\kappa\lambda|\). All three fit into
\[
 A_2(a,b):=\int_0^{2r_*}\|D_a^2V[a,b]\|_\infty dt
                                                 \le24N(a)N(b). \tag{RP.21}
\]
No angular derivative of an unknown direction appears in these
bounds. The actual primitive keeps its order and removes only
its own intermediate constant mode.

## RP6. The full variational equations

Write \(Y_a=D_aX[a]\), \(Z_{ab}=D_a^2X[a,b]\), \(J_X=X_x\).
With exact zero initial values,
\[
 \begin{split}
 (Y_a)_t&=V_\phi(X)Y_a+D_aV[a](X),\\
 (Z_{ab})_t&=V_\phi(X)Z_{ab}+V_{\phi\phi}(X)Y_aY_b\\
 &\quad+(\partial_\phi D_aV[a])(X)Y_b
       +(\partial_\phi D_aV[b])(X)Y_a+D_a^2V[a,b](X),\\
 (\partial_xY_a)_t&=V_\phi(X)\partial_xY_a+
       V_{\phi\phi}(X)J_XY_a+(\partial_\phi D_aV[a])(X)J_X .
 \end{split}                                                 \tag{RP.22}
\]
They are equations on the original initial circle and include
the full reverse leg.

Variation of constants and the actual composition/Jacobian bounds give
\[
 \|Y_a\|_\infty\le JA(a)\le2.16N(a),
\]
\[
 \begin{split}
 \|Z_{ab}\|_2
 &\le J\{19(J\,2)^2+2C_J(J\,2)(84)+24\}N(a)N(b)
                                      <530N(a)N(b),\\
 \|\partial_xY_a\|_2
 &\le J^2\{19(J\,2)+C_J(84)\}N(a)<150N(a).
 \end{split}                                                 \tag{RP.23}
\]
The exact rational coefficients are 529.244928 and149.765760.
A differentiated direction is in \(L^2\); the other variation
is in \(L^\infty\). It is not an unbounded derivative treated
as an ordinary \(L^2\) source.
The spatial variational equation also gives
\[
                              \|P''\|_\infty\le J^3(19)<24 .
                                                               \tag{RP.24}
\]
This proves (RP.1), and \(\|DP[a]\|_\infty\le2.16N(a)\).

Piecewise radial approximation and angular density identify the
extensions with these same actual flows. The estimates preserve the
original interfaces and require no PDE or conjugacy residual to vanish.

## RP7. The full unnormalized phase equation and its chart

Use the original exact target \(\Omega_\star\) of PD.1.
In the original moving angle choose the degree-one lift \(g\) and set
\[
 E(Q,\nu,g)=P(Q,\nu)\circ g-g\circ R_\star,\quad
 R_\star(x)=x+\Omega_\star,\quad \tfrac12\le g'\le2 .
                                                               \tag{RP.25}
\]
The phase constant is not projected out. No fitted rotation
or current normalization \(E/(g'\circ R_\star)\) replaces this map.
In particular the off-constraint defect \(E'a\) in PD.9 remains.

For \(x=(h,\kappa,\xi)\), with periodic lift variation \(\xi\), define
\[
 \mathcal E(x)=N(h,\kappa)+\|\xi\|_2,\qquad
 \mathcal H(x)=N(h,\kappa)+\|\xi\|_{H^1}.                    \tag{RP.26}
\]
TH.5 already gives the fourfold embedding constant \(11/10\).
The exact second differential, for \(a=(h,\kappa)\),
\(b=(k,\lambda)\), is
\[
 \begin{split}
 D^2E[x,y]={}&D^2P[a,b]\circ g
   +(\partial_\phi DP[a])\circ g\,\eta\\
 &+(\partial_\phi DP[b])\circ g\,\xi+(P''\circ g)\xi\eta .
 \end{split}                                                 \tag{RP.27}
\]
Composition on \(L^2\) costs less than \(3/2\), since \(g'\ge1/2\).
The complete bound is therefore
\[
 \begin{split}
 795N(a)N(b)&+247.5\{N(a)\|\eta\|_{H^1}+N(b)\|\xi\|_{H^1}\}\\
 &+13.2\{\|\xi\|_{H^1}\|\eta\|_2+\|\eta\|_{H^1}\|\xi\|_2\}.
 \end{split}
\]
The last line is the average of the two whole product estimates.
As \(795<800\), this proves (RP.2).

The physical lift is exactly \(g_\theta=\Theta_0\circ g\).
Its entire nonlinear residual satisfies
\[
 \begin{split}
 P_\theta\circ g_\theta-g_\theta\circ R_\star
 &=\Theta_0(g\circ R_\star+E)-\Theta_0(g\circ R_\star)\\
 &=E\int_0^1\Theta_0'(g\circ R_\star+tE)\,dt . 
 \end{split}                                                 \tag{RP.28}
\]
Thus the zero equations in the two declared charts are equivalent.
A nonzero residual is not replaced by one endpoint derivative.
A consumer using a fixed physical angle must retain all chart
derivatives and residual terms of (RP.28), as P.11 and PH.23--24
require. No independent waist or root origin is reset.
The present quantitative Hessian is for the declared moving-angle
phase row (RP.25).

## RP8. Quadratic remainder and actual scope

On every real segment staying in (RP.3),(RP.25),
\[
 \|E(z+x)-E(z)-DE(z)x\|_2
                             \le400\mathcal H(x)\mathcal E(x). \tag{RP.29}
\]
For two admissible increments of \(\mathcal H\)-norm at most \(\rho\),
whose connecting segments stay admitted, the remainder difference
is at most \(800\rho\mathcal H(x-y)\).

With \(\nu,g\) fixed and \(\sup_r\|h(r)\|_{A^0}\le\rho\),
\(E_h^2\le.239\rho^2\). The sharper state term in (RP.27) gives
\[
 \|E(Q+h,\nu,g)-E(Q,\nu,g)-D_QE[h]\|_2<96\rho^2 .           \tag{RP.30}
\]
At \(\rho=10^{-6}\) the bound is \(9.6\,10^{-11}\).
The nonzero linear and constant residuals still have to be solved.

The companion reader only makes new rational combinations of
completed conclusions and these formulas. It calls no old flow,
coefficient or phase-target producer. The true regular parameter
response, homogeneous boundary compensation, phase Schur lower,
high-order tame estimates, world-height closure and a summable
augmented iteration remain separate obligations. The metric
parameter is chosen once for the final construction; the domain
(RP.3) is not a flex family with varying intrinsic metric.
