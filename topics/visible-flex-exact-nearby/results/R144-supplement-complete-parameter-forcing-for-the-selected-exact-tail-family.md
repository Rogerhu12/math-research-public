# R144 GF: complete parameter forcing for the actual selected exact-tail family

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all 23 new exact exponent comparisons pass.** At one fixed physical
nonmean height coordinate, the actual S/T family has a complete parameter
derivative in the ordinary source space, including all three broken radial
source derivatives. The true nonlinear far graph, the seed's second design
parameter, its radial first compensation, and the first-principal feedback
are all differentiated. The resulting low-source bound is
\[
 \|D_\gamma{\cal F}_\gamma(w)[\eta]\|_{Z_{1794}^{[3]}}
 <2^{-44000000}r_\gamma^{-1}\|\eta\|_{H^{1795}}.
\]
The value parameter remains in T's actual \(H^{8193}\) domain. The statement
does not assume differentiability of the selected nonlinear solution.

This text is the recovery of the completed GF proof after the local
execution environment became unavailable. The mathematical statements,
constants, ranges, and the already completed 23 integer comparisons are
unchanged; the companion reader is the original saved text.

## Sources and conventions

The completed inputs are:

- [S: the actual far graph and complete graph Nash construction](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md), especially S.3--S.16 and S.25--S.27;
- [T: the actual continuous exact-tail family](R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md), whose equations C.1--C.14 are denoted T.C.1--T.C.14 below;
- [E: the fixed reference graph and exact residual](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md), especially E.2--E.4 and E.18--E.26;
- [M: the complete two-input zero-width cap](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md);
- [O: the actual two-input cap--long forms and source units](R133-supplement-actual-two-input-cap-long-tame-forms-and-physical-Poisson.md);
- [L: the low-norm principal value map](R119-supplement-low-norm-principal-Gamma-map-and-tame-high-conjugacy.md), especially L.9--L.20;
- [P: the true first-principal counterterm](R119-supplement-finite-Sobolev-principal-KAM-and-true-first-metric-counterterm.md);
- [G: projected metric sources and the full first-parameter Schur](R119-supplement-low-direction-first-Gamma-projected-metric-source-and-linear-Schur.md);
- [Mhol: the full finite-Sobolev holonomy and height chart](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md);
- [Qmet: exact ordinary sources and reference-height lifts](R119-supplement-exact-nonlinear-ordinary-sources-and-Gamma-reference-height-lifts.md);
- [Gseed: the actual five-jet positive collar](R119-supplement-new-94-B-collar-lift-and-actual-graph-seed.md);
- [A: the complete reference-graph approximate inverse](R119-supplement-reference-graph-approximate-right-inverse-and-exact-port-defects.md).

All angular frequencies belong to the original signed set \(4\mathbb Z\).
Ordinary Fourier mean, holonomy mean, the independent flux charge, and the
rigid height constant are distinct. All graph and source norms below are
the actual ordinary norms with their original layer, finite-connector,
source, and trace weights. A common reference identifies physical
functions; it does not replace any actual metric or PDE coefficient.

## 1. Three parameter objects and the fixed physical coordinate

Keep the real parameter domain
\[
 {\cal D}_\gamma=
 \left\{\gamma\in H^{8193}_{\ne0,\mathrm{ev}}:
 \|\gamma/r_\gamma\|_{A^0}\le1/128,\quad
 \|\gamma/r_\gamma\|_{H^{8193}}\le2^{1048576}\right\},
 \qquad r_\gamma=10^{-9}.                                      \tag{GF.1}
\]
There are three different objects:
\[
 \begin{split}
 q_\gamma(f)&=P_\perp{\cal K}(f,\Phi_\gamma(f))+\mathsf C_Lf,\\
 \mathfrak q(\gamma)&=\Gamma_2^*(a_{94}(\gamma))-\bar\Gamma_2,\\
 q_{\rm ph}&=w_{\rm metric}^{\,2}.
 \end{split}                                                   \tag{GF.2}
\]
The first is the true nonlinear far slope correction. The second is the
actual second design parameter selected by the original 94-step seed.
The third is the physical radial metric scalar. None is substituted for
another.

For the fixed physical nonmean coordinate \(w\in E_{s,0}^+\), put
\[
 f=F_Bw,\qquad
 u={\cal U}_\gamma(w)=w+{\cal L}_\partial q_\gamma(f),\qquad
 F_B{\cal L}_\partial=0,\qquad B_0w=0.                           \tag{GF.3}
\]
The lift is supported in Gseed/S's positive B collar, outside every
negative input interval, root germ, and first- and second-parameter bump.
The full principal fixed-point construction therefore satisfies
\[
 {\cal G}_1({\cal U}_\gamma w,\mathfrak q)
       ={\cal G}_1(w,\mathfrak q)                               \tag{GF.4}
\]
for every admitted \(\mathfrak q\). This is equality of the whole candidate
fixed-point map before selection: both ordered characteristic legs,
counterterms, and metric arguments are identical on their entire input
domains. It is stronger than equality of a boundary value.

Use T.C.10--T.C.14 to identify all reference graphs with
\(\mathfrak q=0\). Define
\[
 W_s=\|w\|_{E_s^+},\qquad
 \mathfrak d_j=r_\gamma^{-1}\|\eta\|_{H^j},\qquad
 \epsilon=\epsilon_L=e^{-7L/4}<2^{-57000000}.                    \tag{GF.5}
\]
Assume
\[
 W_{1856}\le2^{-49000000},\qquad 20\le s\le2898.                 \tag{GF.6}
\]
Higher \(W_s\) are only required to be finite when they occur. The
additional term \(2^{440}\|F_Bw\|_{H^{s+3}}\) belongs to the definition of
\(E_s^+\); it is not obtained from an arbitrary raw radial trace.

## 2. The actual endpoint-graph derivative

At fixed \(f\), the full derivative of the first line of (GF.2) is
\[
 D_\gamma q_\gamma(f)[\eta]
  =P_\perp D_g{\cal K}(f,\Phi_\gamma(f))
                        D_\gamma\Phi_\gamma(f)[\eta].          \tag{GF.7}
\]
The pure \(f\) part \({\cal K}(f,0)+\mathsf C_Lf\) has zero gamma
derivative. Every remaining complete mixed term retains the separated-end
factor \(\epsilon\). This includes the terms with high \(f\), all signed
frequencies, the complete mean output before projection, and the
cap--long reflections.

Use the actual mixed Taylor kernels from M/O and the complete moment
summation S.14. Differentiating a gamma slot adds one Taylor degree factor;
this is within the four additional degree factors already allowed in
S.14. For \(r\le2899\), the same one-high summation gives
\[
 \begin{split}
 \|D_\gamma q_\gamma(f)[\eta]\|_{H^{r+1}}
 \le {}&2^{120}C_r^\partial\epsilon
 \left\{\mathfrak d_r+
 \left(1+\|\gamma/r_\gamma\|_{H^r}
                 +\|f\|_{H^{r+2}}\right)\mathfrak d_1\right\},\\
 C_r^\partial={}&2^{512(r+32)+262144}.
 \end{split}                                                   \tag{GF.8}
\]
The factor \(2^{120}=r_B^{-2}\) restores the original physical height
normalization. There is no deletion of a pure gamma term by assigning it
a nonexistent factor of \(f\).

Set
\[
 v_\eta={\cal L}_\partial D_\gamma q_\gamma(f)[\eta].
                                                                    \tag{GF.9}
\]
S.12 costs \(2^{2048}\), and \(r=s+1\) uses exactly the real added trace
\(f\in H^{s+3}\). T.C.14 gives the common-reference comparison. The value
bound in (GF.1), all finite factors, and the full mean recovery can be
collected as
\[
 \|v_\eta\|_{E_s^+}
 \le K_\partial\epsilon
       \{\mathfrak d_{s+1}+(1+W_s)\mathfrak d_1\},
 \qquad K_\partial=2^{6291456}.                                \tag{GF.10}
\]
For example the maximum endpoint exponent is bounded by
\(512(2899+32)+262144+1048577+120+8192+32<6291456\).
No derivative of the nonlinear selected solution was used.

S.16 in the same physical coordinates also gives
\[
 \|u\|_{E_s^+}\le4(W_s+K_\partial\epsilon),\qquad
 \|u\|_{E_{1856}^+}<2^{-48000000}.                              \tag{GF.11}
\]
The low four-state quantity used below can be taken to be the maximum of
the actual and common-reference low states. It is at most
\(2\|u\|_{E_{20}^+}<2^{-48000000}\), with the harmless finite comparison
absorbed by the strict margin in (GF.11). It is not asserted to equal the
common-reference graph norm.

## 3. The actual seed's second-parameter column

Retain T.C.5's two-neighbor weights:
\[
 \|\mathfrak a\|_{\mathcal P_2}
   =\sup_i|\mathfrak a_i|/W_i,\qquad
 W_i=J_j^3\delta_j^{-5}C_j^{\rm P}\ (i=(j,k)\ne o),\quad W_o=1.
                                                                    \tag{GF.12}
\]
The six-neighbor \(C_j^\#\) is used only when the actual supports are
collected on a cell. It is not substituted into this definition.

The actual auxiliary gamma ball and the true seed derivative in T.C.9
give
\[
 \|\mathfrak q(\gamma)\|_{\mathcal P_2}<2^{-110000000},\qquad
 \|D_\gamma\mathfrak q(\gamma)[\eta]\|_{\mathcal P_2}
                  \le2^{-110000000}\mathfrak d_1.              \tag{GF.13}
\]
For nonmean \(4\mathbb Z\) functions,
\(\sum_{k\in4\mathbb Z\setminus\{0\}}\langle k\rangle^{-2}<1\);
hence \(\|\eta\|_{A^0}\le\|\eta\|_{H^1}\), with no extra factor required.

The reference associated with each second parameter includes the exact
radial first compensation \(\chi_i(\mathfrak q_i)\), with
\(|\chi_i'|<2\). That compensation is retained in every metric derivative
below. Formula (GF.13) is a genuine derivative of the seed map, not a
derivative inferred from a small value bound.

## 4. The full first-principal response to a second-parameter change

We next pay the part not supplied by differentiating only a radial
reference. In P/L notation, the actual first metric parameter is
\[
 \Gamma_{1,i}(p,\mathfrak q)
 =G_i\!\left((\omega_i-\Omega_i^0+p_i)/4
       -\theta_{2,i}(\bar\Gamma_{2,i}+\mathfrak q_i)
       -\theta_{\Xi,i}\right).                                \tag{GF.14}
\]
Let \(f_i(p,u,\mathfrak q)\) be the complete ordered return minus its
prescribed translation \(x+\omega_i+p_i\), and put
\(T_i(p,u,\mathfrak q)=\tau_i(f_i(p,u,\mathfrak q))\).
The selected principal vector solves \(p=T(p,u,\mathfrak q)\).
Differentiation gives the full infinite-dimensional identity
\[
 D_{\mathfrak q}p[\mathfrak a]
   =(I-D_pT)^{-1}D_{\mathfrak q}T[\mathfrak a],
 \qquad\|(I-D_pT)^{-1}\|_{\mathcal P\to\mathcal P}<2.            \tag{GF.15}
\]
The inverse here is the original full principal fixed-point inverse,
including its off-diagonal responses.

Here are the ordinary real-flow estimates needed to justify (GF.15) in
its actual norm. Write \(\tau=\|\mathfrak a\|_{\mathcal P_2}\) and denote
the low four-state size by \(\varepsilon_u<2^{-48000000}\).

Mhol's original scalar weights are
\(C_j=2^{200}h_j^{-5}\zeta_j/(\mu_j\delta_j^2)\), and their complete
neighbor collection satisfies \(C_j^\#<2^{256}C_j\). Therefore
\[
 W_i\le2^{456}J_j^3h_j^{-5}(\zeta_j/\mu_j)\delta_j^{-7}
 \le2^{456}J_j^3h_j^{-10}(\zeta_j/\mu_j)\delta_j^{-57/2}.
\]
T.C.13 bounds the last profile by \(2^{262144}\). In particular,
\(\sup_iW_i<2^{263000}\), and a \(\mathcal P_2\) ball of radius
\(2^{-524288}\) is inside the original raw second-parameter box
\(2^{-34}\). The actual seeds in (GF.13) lie strictly inside this
auxiliary joint parameter ball.

At fixed \(p\), the original scalar curve bounds
\[
 |\theta_{2,i}'|<4\sqrt{\eta_i/\Delta_i},\qquad
 |G_i'|<512\sqrt{\Delta_i/\eta_i}
\]
give \(|\partial_{\mathfrak q_i}\Gamma_{1,i}|<2^{12}\).
The sharper \(|\chi_i'|<2\) at the radial reference remains valid.
Collecting the actual two bump supports gives the direct coefficient
bound \(g_j\le2^{48}J_j^3\delta_j^{-5}C_j^\#\tau\).

The broken bump derivatives through order four are T.C.12. For partial
radial translations, differentiate the original speed using
\(\int|\delta Q|/(2\sqrt Q)\); the support is inside the already paid
region \(Q\ge\sqrt{12}\Delta/(2\eta)\), and the actual bump variation has
\(\int|\psi_{r,x}|=2\). The root germs do not change. All these scalar
jets and partial translations cost at most \(2^{524288}\tau\), since
\[
 262144+456+48+64+16<524288.
\]

Differentiate the one actual ordered flow in L.10: the plus leg is
forward and the minus leg is reversed. On one fixed physical \(u\), the
nonmean state variations are \(-\dot\psi W\), while the complete mean
variation is given by G.12. The exact radial translation, whose endpoint
is \(\omega_i+p_i\), is subtracted before estimating the nonradial
return. Every remaining differentiated term consequently has a factor
of \(u\) or \(u_\theta\). No such factor is asserted for the separate
radial translation itself.

The real \(H^{16}\) flow calculation uses at most 18 angular derivatives,
which are available from the low \(E_{20}\) norm. One new metric insertion
in the original finite-flow argument costs at most another \(8192+64\)
bits. With the original
\[
 E_i=2^{4096}J_jC_j^{\rm P}\ (i\ne o),\qquad E_o=2^{4096},
\]
this gives
\[
 \|D_{\mathfrak q}f_i[\mathfrak a]\|_{H^{16}}
             \le2^{786432}E_i\varepsilon_u\tau.                 \tag{GF.16}
\]
Indeed \(524288+8192+64<786432\). This is differentiation of the
actual real characteristic ODE and the original L.9 counterterm; it
does not evaluate a rough unknown angle at a complex point.

For completeness, the derivative is a genuine joint Banach derivative.
The two-insertion real-flow remainder has a finite bound
\(2^{2\cdot786432}\) before the row weights. The original
\(E_i/(\gamma_iD_i)^2<2^{4416}\) controls those remainders uniformly
in the actual principal norm. Thus the difference quotient remainder
tends to zero there, and the uniform contraction differentiates the
complete selected fixed point. Coordinatewise differentiation followed
by an unsupported supremum is not used.

The real counterterm derivative satisfies
\(|D\tau_i[v]|\le\|v\|_\infty\). Applying (GF.15), with the original
row refinement of the feedback, gives
\[
 \|D_{\mathfrak q}p[\mathfrak a]\|_{\mathcal P}
      <2^{791000}\varepsilon_u\tau,\qquad
 |D_{\mathfrak q}p_i[\mathfrak a]|
      <2^{786433}E_i\varepsilon_u\tau.                         \tag{GF.17}
\]
The norm exponent is \(786432+4416+1=790849<791000\).
The row estimate follows by substituting the full norm bound back into
the actual row equation; its extra \(E_i\varepsilon_u\) factor absorbs
the row feedback, rather than discarding it.

The metric curves have
\(|\partial_p\Gamma_{1,i}|<2^{-18}\kappa_i^{-1}\).
Internally \(\kappa_i^{-1}<2^{28}J_j\delta_j^{-1}\), and at \(o\)
the actual bound is \(2^{132}\). Hence the first-principal feedback in
the metric coefficients satisfies
\[
 |\dot\Gamma_{1,i}^{\rm fb}|
   <2^{800000}J_j^2\delta_j^{-1}C_j^\#
                   \varepsilon_u\tau\quad(i\ne o),\qquad
 |\dot\Gamma_{1,o}^{\rm fb}|<2^{800000}\varepsilon_u\tau .
                                                                    \tag{GF.18}
\]
The corresponding exponents before widening are 790539 and 790643.
Since \(\varepsilon_u<2^{-48000000}\), these terms fit strictly inside
the direct profile after being retained.

For the total metric derivative
\[
 \dot\psi=\sum_i\psi_{1,i}D_{\mathfrak q}{\cal G}_{1,i}[\mathfrak a]
                     +\sum_i\psi_{2,i}\mathfrak a_i,
\]
the resulting usable bounds are
\[
 \begin{gathered}
 g_j\le2^{64}J_j^3\delta_j^{-5}C_j^\#\tau,\\
 \max_{a\le4}\ell_j^a|\partial_t^a\dot\psi|\le2^{64}g_j,\qquad
 \max_{a\le3}\ell_j^a|\partial_t^{a+1}\dot\psi|
                            \le2^{64}\delta_j^{-3/2}g_j .
 \end{gathered}                                                   \tag{GF.19}
\]
The shallow \(o\) coefficient has its actual bound \(2^{14}\tau\)
and is paid in cell 129. It is not treated as an asymptotic deep cell
or as part of the unchanged finite connector.

## 5. Complete ordinary metric sources in the common physical reference

Use bars for the fixed \(\mathfrak q=0\) reference. Put
\(\Psi=\log(w_{\rm metric}/\bar w)\), so that
\[
 Q=\bar Q-\Psi_t,\qquad q_{\rm ph}=\bar q\,e^{2\Psi},
 \qquad c=\bar c\,e^{2\Psi}.
\]
The four reference states \(p_0,k_0,U_0,V_0\) are E.2--E.4 on
one fixed physical \(u\). Write
\[
 {\cal Q}(W;Q,q_{\rm ph})=F_Q(W)-Q(2K+U)
\]
for the complete quadratically vanishing nonlinearity, including its
holonomy mean. The exact common-reference ordinary residual is
\[
 \mathfrak f_{\mathfrak q}(u)
  =e^\Psi{\cal L}_0u
       +\bar c e^\Psi\Psi_t(k_0+U_0)
       -cP_\perp{\cal Q}(W;Q,q_{\rm ph}).                       \tag{GF.20}
\]
This is the original reference-source identity T.C.11 plus the exact
nonlinear residual. On the added finite connector every metric bump
vanishes; its source is the original ordinary
\(e_0-P_\perp{\cal Q}\). No internal factor \(c\) is inserted into that
finite source unit.

At fixed physical \(u\), the exact metric derivative of (GF.20) is
\[
 \begin{split}
 D_{\mathfrak q}\mathfrak f_{\mathfrak q}(u)[\mathfrak a]
 ={}&e^\Psi\dot\psi\,{\cal L}_0u\\
 &+\bar c e^\Psi(\dot\psi\,\Psi_t+\dot\psi_t)(k_0+U_0)\\
 &-cP_\perp\{2\dot\psi\,{\cal Q}
       +D_W{\cal Q}[\dot W]
       -{\cal Q}_Q\dot\psi_t
       +2q_{\rm ph}\dot\psi\,{\cal Q}_{q_{\rm ph}}\},
 \end{split}                                                   \tag{GF.21}
\]
where
\[
 \dot W=-\dot\psi(P,K_\perp,U,V)+(0,\dot\kappa,0,0),
 \qquad \dot K=-\dot\psi K_\perp+\dot\kappa .
\]
The first line is bounded using the actual graph source
\({\cal L}_0u\), not by treating a second radial derivative as a
free state norm.

The only additional linear narrow-source profile is the same one
already exposed in T.C.13. From G.20 and (GF.19),
\[
 \frac{\bar c C_j^\#|\dot\psi_t|}
             {\zeta_j\delta_j^{16}}
 \le2^{1296}J_j^3h_j^{-10}
                    \frac{\zeta_j}{\mu_j}\delta_j^{-57/2}\tau,
 \qquad1296=1168+64+64.                                       \tag{GF.22}
\]
All three scaled ordinary radial source derivatives obey this same
profile bound: they require at most the four broken bump derivatives
already paid in (GF.19). The original scaled Leibniz rule retains every
one-sided jet and original interface jump.

T.C.13 pays the entire finite prefix, both profile junctions, and the
shallow exception before the deep tail. Its global supremum is
\(2^{262144}\); in the deep range its power is
\(\delta^{98-10/256}\), which tends to zero. There is no use of a deep
asymptotic bound on an unpaid prefix.

Every other term in (GF.21) has two small state factors, a graph factor,
or the exact mean-root variation from G.12. In its original scalar
notation that identity gives
\[
 |\dot\kappa|+|\dot\psi\,\kappa+\dot\kappa|
                    \le2^{16}n_2^2|\dot\psi|.
\]
The one-high rational expansions from E, now with one differentiated
metric insertion, can be collected through order 2898 at cost
\(2^{655360}\): the original \(524288\) bits plus \(131072\) bits
pay the additional insertion and finite sums. No product contains two
highest background norms.

A deliberately loose complete exponent budget is
\[
 655360+524288+262144+131200+1168+128
          =1574288<2097152.
\]
The separate shallow cost \(212992\) is inside the same budget.
Consequently
\[
 \|D_{\mathfrak q}\mathfrak f_{\mathfrak q}(u)[\mathfrak a]\|
                         _{Z_s^{[3]}}
     \le2^{2097152}\tau\|u\|_{E_s},
 \qquad20\le s\le2898.                                       \tag{GF.23}
\]
The actual bump jets of orders 0, 1, and 2 vanish at their support
endpoints. Thus differentiating the parameter introduces no new atoms;
the original broken-source jump convention is unchanged.

### Holonomy mean, reference height, and off-shell charge

The full mean row must be recovered before a nonmean residual is used
as a complete physical source. With G's exact notation, let
\(\ell=\dot\psi\,\kappa+\dot\kappa\). The metric source and the
reference-height derivative have the identities
\[
 \begin{split}
 -\Pi_A\,\delta_{\rm met}N
   &=\Pi_A\{c e_{\psi,{\rm rem}}
          +c(F_K-2Q)\ell-\dot\psi N\},\\
 (H_{\rm met})_t
   &=a_{\rm ph}w_{\rm metric}
                     \{\dot\psi(1+\kappa)+\dot\kappa\}.
 \end{split}                                                   \tag{GF.24}
\]
In particular, the reference \(1\) in the height derivative is retained.
Its original directed integral and endpoint port are not declared
zero merely because the bumps are compactly supported.

For the complete physical residual \(\mathfrak F\), differentiating
the actual holonomy projection gives
\[
 D\mathfrak F=\Pi_A D\mathfrak f+(D\Pi_A)\mathfrak f.             \tag{GF.25}
\]
The scalar mean pairings and their first three radial derivatives use
the original low norm factors. A scalar mean is not assigned a
fictitious high angular derivative. Keeping the complete ordinary
holonomy-mean source and its charge identity gives the version
\[
 \|D_{\mathfrak q}\mathfrak F_{\mathfrak q}(u)[\mathfrak a]\|
                          _{Z_s^{[3]},{\rm full}}
     \le2^{4194304}\tau\|u\|_{E_s}.                            \tag{GF.26}
\]
Here the subscript 'full' means the ordinary PDE source before its
holonomy mean and associated charge identity are dropped. It does not
include the independent reference-height readout in a vanishing-source
estimate. That readout is exactly the directed integral in (GF.24),
including its reference 1, and can be nonzero when u=0. Independent
rigid height and prescribed nonzero flux ports retain their own original
coordinates.

Off shell, the charge identity is
\(\langle A\,D\mathfrak F\rangle
=-\langle DA\,\mathfrak F\rangle\).
Only at an exact solution does the right side vanish. This proof does
not erase it on a nearby non-solution.

## 6. Chain rule for the actual selected family

The family in S/T is
\[
 {\cal F}_\gamma(w)
    =\mathfrak f_{\mathfrak q(\gamma)}({\cal U}_\gamma w).
                                                                    \tag{GF.27}
\]
At fixed physical \(w\), its exact derivative is
\[
 \begin{split}
 D_\gamma{\cal F}_\gamma(w)[\eta]
 ={}&D_u\mathfrak f_{\mathfrak q(\gamma)}(u)[v_\eta]\\
   &+D_{\mathfrak q}\mathfrak f_{\mathfrak q(\gamma)}(u)
                       [D_\gamma\mathfrak q(\gamma)[\eta]] .
 \end{split}                                                   \tag{GF.28}
\]
The first term is the actual boundary-lift source. By (GF.4), its
variation of the first-principal map on the negative cap is exactly
zero. The second term includes the actual second-parameter bumps,
radial first compensation, and the full first-principal response
(GF.15)--(GF.19). These support facts are source identities; they do
not set any propagated response or reference-height constant to zero.

The complete E.25/E.26 calculation can be used in the safe form
\[
 \|D_u\mathfrak F_{\mathfrak q}(u)[v]\|_{Z_s^{[3]},{\rm full}}
 \le2^{4194304}
   \{\|v\|_{E_s^+}+(1+\|u\|_{E_s^+})\|v\|_{E_{20}^+}\}.
\]
Apply (GF.10)--(GF.11) before multiplying high factors. Since
\(K_\partial\epsilon<1\), the endpoint part retains one highest
norm. Its total exponent
\(4194304+6291456+16<12582912\)
pays the ordinary source, complete holonomy-mean, and finite-sum factors.

For the second part, use (GF.13), (GF.23), (GF.26), and (GF.11).
The following single formula covers both the original nonmean
residual and its full-mean interpretation (GF.25):
\[
 \begin{split}
 \|D_\gamma{\cal F}_\gamma(w)[\eta]\|_{Z_s^{[3]}}
 \le{}&
 2^{12582912}\epsilon
       \{\mathfrak d_{s+1}+(1+W_s)\mathfrak d_{21}\}\\
 &+2^{6291456-110000000}
                  (W_s+K_\partial\epsilon)\mathfrak d_1,
 \qquad20\le s\le2898 .
 \end{split}                                                   \tag{GF.29}
\]
All actual common-reference source terms and the three broken radial
derivatives are included. The original independent mean/height ports
remain in their own coordinates.

For \(s=1794\), (GF.6) makes \(W_s<1\), and the direction norms of
orders 1 and 21 are bounded by \(\mathfrak d_{1795}\). Thus
\[
 \|D_\gamma{\cal F}_\gamma(w)[\eta]\|_{Z_{1794}^{[3]}}
  <2^{-44000000}r_\gamma^{-1}\|\eta\|_{H^{1795}}.                \tag{GF.30}
\]
Before the last widening, the exponent from the two nonnegative source
contributions is at most \(-44417085\). This is a bound for the true
complete parameter forcing, including the changes in both design
parameters.

More generally the same bound at source index \(j\le2898\) holds if
\(W_j\le1\), with direction order \(j+1\). At the actual selected limit,
the already paid common \(E_{2960}^+\) bound supplies this hypothesis.
In particular, for \(64\le s\le1164\), source index \(s+1734\) and
direction order \(s+1735\le2899<8193\) lie inside the proved window.

The value family is still constructed on (GF.1). A lower direction
cost in a particular source estimate is not an assertion that the
value construction is defined on an open \(H^{1795}\) ball.

## 7. Genuine finite parameter differences

The domain (GF.1) is convex. At the same fixed physical \(w\), put
\(\gamma_t=\gamma'+t(\gamma-\gamma')\). Each point uses its own actual
seed, true second parameter, radial compensation, endpoint map, and
selected first-principal map. The chain rule above gives
\[
 {\cal F}_\gamma(w)-{\cal F}_{\gamma'}(w)
   =\int_0^1D_\gamma{\cal F}_{\gamma_t}(w)
                            [\gamma-\gamma']\,dt.             \tag{GF.31}
\]
Consequently
\[
 \|{\cal F}_\gamma(w)-{\cal F}_{\gamma'}(w)\|_{Z_{1794}^{[3]}}
 <2^{-44000000}r_\gamma^{-1}
                         \|\gamma-\gamma'\|_{H^{1795}}.       \tag{GF.32}
\]
For the higher source window, integrate (GF.29) with
\(\mathfrak d_j=r_\gamma^{-1}\|\gamma-\gamma'\|_{H^j}\).

This provides the complete actual parameter mismatch needed by the
separate selected-limit a priori argument. It does not infer
differentiability of that limit from surjectivity of a finite-regularity
inverse. It also does not yet assert an \(A^0\)-only high-source
estimate: that requires a separate complete mixed separated-end
argument.

## 8. Saved-bound arithmetic

The companion
[fourfold_codazzi_selected_tail_parameter_forcing_saved_bounds.py](../scripts/fourfold_codazzi_selected_tail_parameter_forcing_saved_bounds.py)
contains the 23 new exact integer comparisons used above. They passed
once on the completed local text before the environment interruption.
They combine already proved exponents only; they do not reevaluate any
native array, characteristic integration, Green function, or prior
scientific target. The reader preserves that original completed result
and has not been rerun during text recovery.
