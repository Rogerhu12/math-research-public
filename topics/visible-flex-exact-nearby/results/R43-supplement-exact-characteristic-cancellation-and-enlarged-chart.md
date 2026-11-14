# R43 supplement: exact characteristic cancellation and a larger actual negative chart

The full negative-side characteristic chart admits a useful cancellation that
is absent from the previous independent bounds on its two labels. This note
proves that cancellation, evaluates its actual coefficient on a complete
complex bidisk, and constructs a larger holomorphic inverse. It then consumes
the already certified full root Fourier traces, including their correlated
errors, to pay a longer local R43 collar.

The family and each parameter's moving root are unchanged:

\[
p_5=-7789843107295549/4611686018427387904,
\qquad |p-p_5|\le 10^{-9},\qquad \rho=t(p)-r.
\]

The new complete potential disk is

\[
 |\xi|\le \frac1{120000},\qquad
 |\Im\phi|\le s_V,
 \quad s_V>1.05015426167699\,10^{-5},
 \qquad |V|<1.450905012\,10^{10}.                         \tag{C.1}
\]

This disk is in the exact negative characteristic coordinates. On its much
shorter subcollar \(0\le\xi\le 2^{-129}\), the complete R43 operator satisfies

\[
 \boxed{\|C(\delta,0)-I-B:E_s\longrightarrow E_{s+4/3}\|
       <4.319813\,10^{41},\quad |s|\le8.}                  \tag{C.2}
\]

The intermediate layers through \(|s|\le10\), both amplitudes, all Fourier
cones and the mean are retained. The full local homogeneous forward and inverse
bounds are below \(e^{1/10}\); the canonical ordinary-source gain is below
\(20.961937\). These are local operator bounds. Physical frame/source gluing,
the strict interval, positive Ai/contact and the complete returned inverse
remain separate obligations.

## 1. A common scalar equation for the two actual characteristic densities

Use the seven-field notation of R106. In particular,

\[
 U_0=\frac{a_0}{2\sqrt Q},\qquad k=k_{\rm star}=\frac1{2U_0},
 \qquad q=-b_0/a_0.
\]

For \(\rho=s^2\), let

\[
 D_\sigma=\partial_s+(2s q-2\sigma s^2k)\partial_\theta,
 \qquad D_\sigma T_\sigma=0,
 \qquad T_\sigma(0,\theta)=Y_0(\theta),\quad \sigma=\pm1.
                                                               \tag{C.3}
\]

The root normalization is exact: \(k(0,\theta)Y_0'(\theta)=1\).
Differentiate (C.3) with respect to \(\theta\), multiply by \(k\), and put
\(F_\sigma=kT_{\sigma,\theta}\). The terms containing
\(\sigma k_\theta\) cancel:

\[
 \boxed{D_\sigma F_\sigma=2s\mathcal C F_\sigma,
 \quad F_\sigma(0)=1,\quad
 \mathcal C=\frac{k_\rho+qk_\theta}{k}-q_\theta
 =-\frac{U_{0,\rho}+qU_{0,\theta}}{U_0}-q_\theta.}           \tag{C.4}
\]

No average over \(\theta\), replacement by the radial model, or finite Fourier
projection occurs in this identity. It holds for each member of the actual
parameter interval.

The new producer
`fourfold_negative_characteristic_cancellation.py` consumes the complete
parameter-transferred degree-80, Fourier-degree-650 seven-field certificate.
It evaluates all 81 radial rows and all 1301 angular coefficients by a directed
two-dimensional Fourier transform, using 128 radial phase cells and 2048
closed angular cells. These dimensions exceed the corresponding exact
polynomial degrees, so the finite evaluation has no uncharged alias.

For a differentiated term \(z_{nk}\), the finite closed-cell motion is bounded
by

\[
 |z_{nk}|\left((n-a)\pi/128+|k|\pi/2048\right),
\]

where \(a\) is its radial derivative order. The coefficient used to form
\(z_{nk}\) already includes the exact radial and physical-angle derivative
factors. The complete field errors are added before division. The derivative
errors are paid by Cauchy on the larger certified bidisk
\(R_0=7/25000,S_0=1/400\):

\[
 \epsilon_{U_\rho}=\epsilon_U/(R_0-R),\qquad
 \epsilon_{U_\theta}=\epsilon_U/(S_0-S),\qquad
 \epsilon_{q_\theta}=\epsilon_q/(S_0-S).
\]

The calculation proves, on the whole bidisk

\[
 R=13/50000=.00026,\qquad S=1/500=.002,
\]

\[
 \begin{split}
 |\mathcal C|&<101.014848318=:M_C,\\
 |q|&<.822753758=:M_q,\\
 |k|&<21.691157230=:M_k,\\
 \Re U_0&>.0263038151084.
 \end{split}                                                  \tag{C.5}
\]

The quotients are evaluated only after the last positivity inequality is
checked. Schwarz reflection supplies the lower angular boundary. Successive
maximum principles, first for the real part of \(U_0\) and then for each
holomorphic quotient, give the entire complex bidisk. Thus (C.5) is not a
boundary-node or truncated-field assertion.

The complete transferred field certificate also supplies

\[
 |1/k|=2|U_0|<.359384659911=:M_{1/k}.                         \tag{C.6}
\]

Its domain contains the bidisk above. The actual root inverse-angle certificate
supplies

\[
 \Re Y_0'>m=.056008227289439767\ldots
 \quad\text{on }|\Im\theta|\le1/256.                         \tag{C.7}
\]

All scientific inputs, whole parameter intervals and object identities are
checked by the consumers.

## 2. Complete control of the deflated difference

Take \(S_1=3/2000=.0015\). A signed characteristic followed backwards from
\((s,\theta)\) moves the physical angle by at most
\(M_q|\rho|+(2/3)M_k|\rho|^{3/2}\). In the argument below it is also evaluated
along a common characteristic of
\(D_0=\partial_s+2sq\partial_\theta\). The total nested movement is at most

\[
 2M_qR+\tfrac23M_kR^{3/2}
 <.000488456916862 <S-S_1.                                   \tag{C.8}
\]

The remaining strict margin is greater than
\(1.1543083138\,10^{-5}\). Analytic ODE continuation therefore constructs all
these paths, in both directions, inside the complete coefficient domain.
Integrating (C.4) along the complex straight radial path gives

\[
 |F_\sigma-1|\le e^{M_C|\rho|}-1,
 \qquad |F_\sigma|\le e^{M_C|\rho|}.                         \tag{C.9}
\]

Let \(W=T_+-T_-\), \(\phi=(T_++T_-)/2\). The exact equations imply

\[
 D_0W=2s^2(F_++F_-),\qquad
 D_0\phi=s^2(F_+-F_-).                                     \tag{C.10}
\]

The symmetry \(T_+(-s)=T_-(s)\) makes

\[
 \Delta=\frac{3W}{4s^3},\qquad \xi=\rho\Delta^{2/3}
\]

holomorphic in \(\rho\) at zero, with \(\Delta(0)=1\). Integrating the first
identity in (C.10) along the common characteristic and using (C.9) gives

\[
 |\Delta(\rho,\theta)-1|\le e^{M_C|\rho|}-1.
                                                               \tag{C.11}
\]

In particular, on the complete \((R,S_1)\) domain,

\[
 e_R:=e^{M_CR}-1<.026611795105<1/4.                           \tag{C.12}
\]

The branch \(\log\Delta\) is therefore globally fixed by its root value.
For real variables the two exponentials in (C.4) are positive, so this is the
actual positive branch of the negative-side characteristic chart.

The second identity in (C.10), with
\(\phi_\theta=(F_++F_-)/(2k)\), also gives the useful exact derivative

\[
 \boxed{\phi_\rho=-q\frac{F_++F_-}{2k}
                 +\frac{\sqrt\rho}{2}(F_+-F_-).}            \tag{C.13}
\]

The apparent square root in the second term is removable by the same branch
symmetry. Retaining (C.13) avoids a small radial Cauchy denominator in the
inverse-map estimate.

## 3. The enlarged holomorphic inverse

Set

\[
 r_0=1/60000,\qquad b_0=mS_1/4
 >2.10030852335399\,10^{-5},\qquad y=Y_0(\theta).
\]

The positive-real-derivative argument of the earlier negative chart proves
that the root inverse is holomorphic on the full strip
\(|\Im y|\le4b_0\), with image in \(|\Im\theta|\le S_1\).
Write

\[
 (\xi,\phi)=(\rho+E_\xi,\ y+E_\phi).
\]

On \(|\rho|\le2r_0\), put \(e_2=e^{2M_Cr_0}-1\). Equation (C.13) yields

\[
 M_\phi=M_qM_{1/k}e^{2M_Cr_0}
           +\sqrt{2r_0}\,e_2<.296701850047,
 \qquad |E_\phi|\le2r_0M_\phi.                              \tag{C.14}
\]

Since \(\Delta-1\) vanishes at zero and is bounded by \(e_R\) on its whole
outer disk, its complete Taylor series gives

\[
 |\Delta_\rho|\le
 D_\Delta:=\frac{e_R/R}{(1-2r_0/R)^2}<134.670416404.           \tag{C.15}
\]

Define

\[
 d_2=\frac{2e_2}{3(1-e_2)^{1/3}},\qquad
 a_2=\frac{2}{3(1-e_2)^{1/3}}.
\]

Then \(|E_\xi|\le2r_0d_2\). On the smaller angular strip
\(|\Im y|\le2b_0\), use the complete \(4b_0\) strip for the angular Cauchy
estimates. In the weighted maximum norm
\(\max(|d\rho|/r_0,|dy|/b_0)\), the two derivative row sums are bounded by

\[
 \begin{split}
 \kappa_\xi&\le2d_2+2r_0a_2D_\Delta<.007498231343,\\
 \kappa_\phi&\le 2r_0M_\phi/b_0<.470886136883.
 \end{split}                                                  \tag{C.16}
\]

For example, the angular derivative fee in the second line is
\((2r_0M_\phi)/(2b_0)\), and its radial derivative is the exact bound
\(M_\phi\); the two scaled fees are equal. The first line similarly combines
the exact radial derivative of \(\rho(\Delta^{2/3}-1)\) and the angular
Cauchy estimate of its complete modulus. No mixed derivative is omitted.

Both rows are below \(1/2\), while

\[
 |E_\xi|<7.503639\,10^{-8}<r_0,\qquad
 |E_\phi|<9.890062\,10^{-6}<b_0.
\]

For every target \(|\xi|\le r_0,|\Im\phi|\le b_0\), the map
\((\rho,y)\mapsto(\xi,\phi)-E(\rho,y)\) preserves and contracts the closed
polydisk of radii \(r_0,b_0\) about that target. The entire search domain lies
in \(|\rho|\le2r_0,|\Im y|\le2b_0\). Uniform analytic iteration provides
the inverse; uniqueness gives the correct periodic lift. Its real branch is
the actual negative-side chart, with the root fixed exactly.

## 4. Full potential, root traces and the complete R43 consumer

The actual grounded density \(\mathcal U=\alpha\beta_1\) and the determinant
law for a two-dimensional divergence density give

\[
 L=\log\alpha_c=\tfrac12\log\mathcal U-\tfrac13\log\Delta,
 \qquad
 V=-\tfrac12L_{\xi\xi}-\tfrac14L_\xi^2
      +\xi\bigl(\tfrac12L_{\phi\phi}+\tfrac14L_\phi^2\bigr).
                                                               \tag{C.17}
\]

The native complete logarithm certificate is on a larger physical bidisk and
has \(|\log\mathcal U|<1.665294042\). Thus on the inverse target domain,

\[
 |L|\le M_L=\tfrac12M_{\log\mathcal U}
                     -\tfrac13\log(1-e_2)<.833773200164.
\]

Cauchy on the half-radius, half-width domain gives the complete bound

\[
 M_V=M_L(4+M_L)
       \left(r_0^{-2}+\frac{r_0/2}{b_0^2}\right)
 <14509050116,
\]

which proves (C.1). It includes every radial coefficient, not just the root
jets. For the smaller \(\delta=2^{-129}\) collar, set
\(z=\delta/(r_0/2)\). The complete radial errors are

\[
 \epsilon_0=M_Vz^2/(1-z),\qquad
 \epsilon_1=\frac{M_V}{r_0/2}\frac{z(2-z)}{(1-z)^2}.          \tag{C.18}
\]

The full root traces \(V(0)=v_0\) and \(V_\xi(0)=v_1\) are consumed from
R99/R98's actual canonical Fourier certificates. The finite reference is used
only with its entire correlated projected \(L^2\) error and complete analytic
infinite complement. Specifically, the same exact consumer as the preceding
root-Fourier supplement uses

\[
 \sum_n\langle n\rangle^p|v_{i,n}|
 \le \sum_{|n|\le N}\langle n\rangle^p|c_{i,n}|
 +E_i\left(\sum_{|n|\le N}\langle n\rangle^{2p}\right)^{1/2}
 +2M_i\sum_{n>N}\langle n\rangle^p e^{-4u_*n}.               \tag{C.19}
\]

The current whole-parameter errors are \(E_0<1.872673\,10^{-5}\) and
\(E_1<.012340301\). All reference coefficients are exact stored dyadics.
The remaining errors (C.18) are bounded on the full collar before taking their
Fourier sum, with the actual quarter-period decay
\(e^{-q_c s_V|n|}\). The actual frequency interval is

\[
 38.883851605869<q_c<38.883851623093.
\]

The exponents \(31/3,19/2,32/3\) respectively pay R43's intermediate
\(K^{(0)}\), one-gain \(B^{(1)}\), and \(\mathcal W\). The directed
complete values are

| Quantity | Bound |
|---|---:|
| \(K^{(0)}\) | \(<2.698780820\,10^{37}\) |
| \(\delta K^{(0)}\) | \(<.039655020091<1/10\) |
| \(B^{(1)}\) | \(<1.333705746\,10^{34}\) |
| \(\mathcal W\) | \(<4.535355440\,10^{38}\) |
| \(C_q\) | \(<476.237534756\) |

The complete R43 expression
\(2C_q\mathcal W+2e^{1/10}\delta(B^{(1)})^2\) proves (C.2).
The canonical ordinary-source gain retains R39's factor
\(5\sqrt2\pi/c_A\), including both amplitude rows and the mean.
No physical source norm is identified with this canonical one without its
separate Jacobian, density and frame calculation.

## 5. Executed artifacts and scope

The three new executable producers/consumers and their saved reports are:

| Source | Complete report | SHA256 of report |
|---|---|---|
| `scripts/fourfold_negative_characteristic_cancellation.py` | `notes/2026-11-13-negative-characteristic-cancellation-bidisk.json` | `9d356257b5a4fe220121e4335f8182b872932ff3eb13403111d8fd7a30b9a44d` |
| `scripts/fourfold_negative_canonical_cancellation_chart.py` | `notes/2026-11-13-negative-canonical-cancellation-chart.json` | `71f1f5277ea9764eef3cce264c320ef33ab23278bead7b5c2e53fd599dd61cb0` |
| `scripts/fourfold_negative_collar_cancellation_R43.py` | `notes/2026-11-13-negative-cancellation-R43-window8.json` | `9cbed50e5b5d40c68050a4aff822f94c9bc4ed4fbd00bf149321704dec9ba175` |

From the topic directory, using fresh report paths when rerunning:

~~~bash
python3 scripts/fourfold_negative_characteristic_cancellation.py \
  --out notes/2026-11-13-negative-characteristic-cancellation-bidisk.json
python3 scripts/fourfold_negative_canonical_cancellation_chart.py \
  --out notes/2026-11-13-negative-canonical-cancellation-chart.json
python3 scripts/fourfold_negative_collar_cancellation_R43.py \
  --collar-dyadic-power 129 \
  --out notes/2026-11-13-negative-cancellation-R43-window8.json
~~~

The first calculation took about 43.03 seconds. The two following directed
consumers check the full inputs and all domain/contraction/shortness gates.
No new large intermediate coefficient or node data are needed.

The exact cancellation and enlarged chart reduce the previous radial Cauchy
loss and extend the paid local R43 collar. They do not identify the full
returned \(b-\beta\), bound the complete returned \(R_*\), close the actual
positive Ai/contact and source/frame network, or verify the final finite
Schur block. The strong constant in (C.2) is still large. It is not presented
as a practical final cutoff or as the README completion theorem.
