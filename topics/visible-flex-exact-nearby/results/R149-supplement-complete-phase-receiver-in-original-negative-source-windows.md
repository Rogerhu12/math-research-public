# R149 PRN: complete phase reception in the original negative source windows

2026-11-27, visible-exact-astra-fb31ed6-20261127 / positive_inverse.

**Proved.** For the original selected member, the full principal-phase
functional receives the TC negative sources in their actual
$H^{-1}\oplus H^{-1}$ and $H^{-2/3}\oplus H^{-1}$ units.
It does not require an ordinary angular $L^2$ source certificate.
The explicit complete bound is

$$
 |L_\Omega h|
 \le2600(D_*+J_-)+184F_-+69F_{\rm st}+245J_{\rm st}.
 \tag{PRN.1}
$$

Every term is defined below. In particular the genuine root error $D_*$,
the two independent means and every prescribed state jump remain.
The full TC negative residuals have not been declared complete, and
(PRN.1) does not assert that a true PDE column or the final Schur inverse
has already been obtained.

## PRN1. One background, true root, sources and independent ports

Fix the original implicit selected pair
$(Q_{\delta_*},\nu_{\delta_*})$ and fixed $\eta_0$ of
[PH](R147-supplement-exact-nonlocal-phase-and-height-parameter-ports.md),
[NP](R147-supplement-independent-strict-nu-particular-and-signed-waist-column.md)
and [TC](R149-supplement-true-root-continuous-PDE-trials-and-complete-residuals.md).
The true conjugacy $H$, including its original phase convention, is the
same actual selected conjugacy. No compact mean-exact centre or new
metric is substituted.

The complete existing Cauchy and SP estimates cover the larger real
family $|\delta|\le10^{-8}$; only their restriction to this selected
member is used. Put

$$
 r_c=\frac{2333968743003}{10^{13}},\qquad R=\frac1{200},\qquad
 r_*\in\left[\frac{1191984371497}{5000000000000},
                 \frac{2383968743003}{10^{13}}\right].
 \tag{PRN.2}
$$

Thus $0<r_*-r_c\le R$. The root is not replaced by a proposal dyadic.
Physical angular frequencies are $4j$ and circle measure is normalized.
All pair norms are Euclidean. Write $\Lambda_j=(1+16j^2)^{1/2}$,
$I=\partial_\phi^{-1}(1-\Pi)$ and $q=\sqrt{-K}$.

Let $h$ solve the full original moving Jacobi equation with ordinary
forcing $f$, prescribed true root state and genuine affine state jumps.
Define exactly

$$
\begin{aligned}
D_*&=\|(h_1(r_*),h_2(r_*))\|_{H^{-2/3}\oplus H^{-1}},\\
F_-&=\|f\|_{L^2([r_c,r_*];H^{-2/3}\oplus H^{-1})},\\
F_{\rm st}&=\|f\|_{L^2([0,r_c];H^{-1}\oplus H^{-1})},\\
J_-&=\sum_{r_a\in[r_c,r_*)}
                 \|j_a\|_{H^{-2/3}\oplus H^{-1}},\\
J_{\rm st}&=\sum_{r_a\in(0,r_c)}
                 \|j_a\|_{H^{-1}\oplus H^{-1}}.
\end{aligned}
 \tag{PRN.3}
$$

A jump at the cut is assigned to $J_-$ once, so that propagation
into the strict interval starts at the actual left state $h(r_c-)$.
The root state is a separate input and contains both means. No radial
length factor is placed in either impulse sum.

For a continuous TC trial corrected by a true solution, the original
state jumps are exactly zero by TC6, but its genuine root correction
is not thereby zero. The positive Green/root matching step must supply
$D_*$ in the stated two-row norm.

## PRN2. The complete phase row already has the needed angular derivative

Use the exact two-leg formula D.6--D.8 in
[the complete distributed phase source](R133-supplement-phase-Schur-complete-distributed-adjoint-source.md).
For the current fixed metric its state functional is

$$
\begin{gathered}
W_\pm=a_\pm^2,
\quad A=I(W_+-W_-),\quad M=\Pi(W_++W_-),\\
L_\Omega h=\int_0^{r_*}\langle\ell_1h_1+\ell_2h_2\rangle\,dr,\\
\ell_1=-2\beta uA,\qquad
\ell_2=-2\beta KvA-\gamma qM.
\end{gathered}
 \tag{PRN.4}
$$

This is the original phase row; there is no change to the other output
rows or their normalizers. Its full mean term is explicit. For a
reflected input, (PRN.4) is exactly PH.7 and P96.3, with the two
reflected legs adding. The bound below also applies without imposing
reflection on the state or forcing.

The complete PH.16--17 partial-leg bound gives

$$
       \|a_+\|_\infty,\ \|a_-\|_\infty< a_*:=11/10.
 \tag{PRN.5}
$$

As explained in P96.4, these bounds use the original complete R31
partial-source budgets and true selected $H$ bound. They hold across
the full169 cover and at its root limit, not just the short strict
parameter support. In particular

$$
 \|A\|_2\le\tfrac12a_*^2,\qquad
 \|A\|_{H^1}\le2C_Ia_*^2,\qquad |M|\le2a_*^2,
 \quad C_I=\frac{\sqrt{17}}4<1.031 .
 \tag{PRN.6}
$$

Indeed $\|I\|_{L^2\to L^2}=1/4$ and
$\|I\|_{L^2\to H^1}=C_I$ on the complete fourfold circle.
Only the primitive's own zero mode is removed. The estimate needs
$a_\pm\in L^\infty$; it needs no new derivative of $a_\pm$ and no
angular truncation of the transported weights.

For a vector-valued multiplier $v$, the product rule and Minkowski give

$$
 \|vA\|_{H^1}\le
       \|v\|_\infty\|A\|_{H^1}
        +\|v_\phi\|_\infty\|A\|_2.
 \tag{PRN.7}
$$

This holds for the Euclidean pair directly. It does not introduce a
hidden component-sum conversion.

## PRN3. Pay the phase row in SP's actual primitive and mean energy

The exact energy in SP.15 is

$$
\mathcal E_q(h)^2=
 \|Ih_1\|_2^2+q^2\|Ih_2\|_2^2
       +|\Pi h_1|^2+q^2|\Pi h_2|^2.
 \tag{PRN.8}
$$

For each fixed strict point, integration by parts gives

$$
 \langle\ell,h\rangle
 =-\langle\partial_\phi\ell,Ih\rangle+Pi\ell\cdot\Pi h.
 \tag{PRN.9}
$$

Since $q$ is radial, the corresponding dual norm is at most
$\|(\ell_1,\ell_2/q)\|_{H^1}$. The exact ordered row is

$$
 (\ell_1,\ell_2/q)
       =-2\beta(u,-qv)A-(0,\gamma M).
 \tag{PRN.10}
$$

There is no singular $q^{-1}$ cost. The second mean contributes the
full term $\gamma M$. The first mean is also kept in (PRN.9), even
if a particular reflected column happens to have a zero first mean.

On the entire strict interval, the completed
[SP execution](R133-supplement-actual-complete-primitive-and-mean-strict-propagation-to-the-waist.md)
gives the genuine whole bounds

$$
 \sup\sqrt{u^2+q^2v^2}<1.912,
 \quad\sup\sqrt{u_\phi^2+q^2v_\phi^2}<3.704.
 \tag{PRN.11}
$$

The full intrinsic bounds used in
[RH.2](R147-supplement-relative-height-carriers-and-short-full-frequency-errors.md),
from the larger original
[SJA interval](R133-supplement-actual-complete-strict-radial-first-symbol-defect.md),
give $|\beta|<.211$ and $\gamma<1.12$ here.
All bounds concern the same selected family, with both one-sided
values at every original seam. From (PRN.6)--(PRN.11),

$$
\begin{aligned}
\|\ell\|_{\mathcal E_q^*}
&\le4(.211)(1.1)^2
       \{(1.031)(1.912)+3.704/4\}
          +2(1.12)(1.1)^2\\
&=5.66921005728<5.67.
\end{aligned}
 \tag{PRN.12}
$$

Thus $|L_{\Omega,[0,r_c]}h|\le5.67\int_0^{r_c}\mathcal E_q(h)\,dr$.
The proof extends by density to the full primitive/mean energy space;
it is not an ordinary $L^2$ estimate assigned to a rough state.

## PRN4. Full root-window phase dual and the original two-source Cauchy leg

For the small root window it suffices to use the raw $H^1$ row.
The complete original margins in
[RP.4](R144-supplement-full-off-constraint-principal-return-Hessian.md) and
[D.4--D.6](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md) give
$\|Q_{\delta_*}\|_{A^0}<7$ and
$\|\partial_\phi Q_{\delta_*}\|_{A^0}<6$ on the whole negative interval.
The latter follows from the original $5.437241$ bound, its
$1.970\,10^{-17}$ continuous-repair fee and the complete selected
$83\,10^{-10}$ direction fee. None is a sampled derivative.
The loose full intrinsic bounds $|\beta|<2$, $\gamma<7$, $q<1.03$
also apply on the root window (the metric bump is zero there).

Applying (PRN.6)--(PRN.7) to $(u,Kv)$ gives

$$
\begin{aligned}
\|\ell\|_{H^1\oplus H^1}
&\le 4(2)(1.1)^2
 \{(1.031)(1.03)^2(7)+(1.03)^2(6)/4\}
       +2(7)(1.03)(1.1)^2\\
&=106.967536104<107.
\end{aligned}
 \tag{PRN.13}
$$

The completed original
[large-root run43621934843/1](R133-supplement-actual-full-real-large-root-Cauchy-energies.md)
has, at $R=1/200$,

$$
 C_{-1}<N:=10.936120,\qquad C_I C_{-1}<N_I:=11.272695.
 \tag{PRN.14}
$$

These are the original constants, not the larger compact-centre
transfer. E.6 and the complete source argument explicitly admit the
anisotropic ordinary norm $H^{-2/3}\oplus H^{-1}$ in (PRN.3),
including its independent mean and every affine impulse.
Set

$$
        B=D_*+J_-+\sqrt R\,F_-.
 \tag{PRN.15}
$$

Then $\sup_{[r_c,r_*]}\|h\|_{H^{-1}\oplus H^{-1}}\le NB$.
Consequently

$$
       |L_{\Omega,[r_c,r_*]}h|\le107RN B.
 \tag{PRN.16}
$$

At the cut the original complete SP bound gives $q(r_c)<.723092<1$.
The complete map $h\mapsto(Ih,\Pi h)$ from Bessel $H^{-1}$ has
norm exactly $C_I$, because its zero-frequency ratio is1 and its
largest nonzero ratio is $\sqrt{17}/4$. Therefore

$$
             \mathcal E_{q(r_c)}(h(r_c-))\le N_I B.
 \tag{PRN.17}
$$

The saved scalar $N_I$ was originally displayed for the primitive
readout. Its value is the exact same complete product $C_I C_{-1}$,
so the just-proved complete $(I,\Pi)$ map licenses (PRN.17).
It is not a free assertion that a primitive bound contains a mean,
and no second $C_I$ or $\sqrt2$ is added.

## PRN5. Strict propagation and a triangular source integral

The original SP run43731464771/1 certifies

$$
 U_-<U:=173.872,
 \qquad C_{\rm inj}<J:=1.060693.
 \tag{PRN.18}
$$

Here $U_-$ is the complete reverse primitive/mean propagation norm,
including its original radial $q$ factor. It bounds every ordered
subinterval and every source insertion: each complete nonnegative
comparison factor is entrywise at least the identity, and its
whole product dominates every shorter ordered product. The complete
source injection satisfies
$\sqrt{q}\|(ITf,\Pi Tf)\|\le J\|f\|_{H^{-1}\oplus H^{-1}}$.
Neither number is a waist density normalization.

Thus on $0\le r\le r_c$,

$$
\mathcal E_q(h(r))\le U\left[
 N_I B+J\int_r^{r_c}\|f(t)\|_{H^{-1}\oplus H^{-1}}dt
   +J\sum_{r<r_a<r_c}\|j_a\|_{H^{-1}\oplus H^{-1}}\right].
 \tag{PRN.19}
$$

All unknown frequencies and both means are propagated before
pairing. Fubini and radial Cauchy--Schwarz give the exact length fee

$$
\begin{aligned}
\int_0^{r_c}\int_r^{r_c}\|f(t)\|dt\,dr
 &=\int_0^{r_c}t\|f(t)\|dt
 \le\sqrt{r_c^3/3}\,F_{\rm st},\\
\int_0^{r_c}\sum_{r<r_a<r_c}\|j_a\|dr
 &=\sum_a r_a\|j_a\|\le r_cJ_{\rm st}.
\end{aligned}
 \tag{PRN.20}
$$

Combining (PRN.12), (PRN.16) and (PRN.19)--(PRN.20) yields

$$
\begin{gathered}
|L_\Omega h|\le C_* B+C_fF_{\rm st}+C_jJ_{\rm st},\\
C_*=5.67U r_cN_I+107RN<2600,\\
C_*\sqrt R<184,\qquad
C_f=5.67UJ\sqrt{r_c^3/3}<69,\qquad
C_j=5.67UJr_c<245.
\end{gathered}
 \tag{PRN.21}
$$

All inequalities are strict for the stated positive outward constants;
zero data use their non-strict form. The companion
[exact rational reader](../scripts/fourfold_codazzi_negative_phase_receiver_saved_bounds.py)
makes seven new comparisons, squaring the two positive square-root
inequalities. It evaluates no original scientific target.
Equation (PRN.21) proves (PRN.1).

## PRN6. Apply to TC and P96 without inventing completed residuals

The two complete negative TC norms $F_{-,j}$ and $F_{{\rm st},j}$
in TC.15 are exactly the norms required by (PRN.3). For a continuous
trial $T_j$ and a true full negative column $u_j$ on the same
background, write $e_j=u_j-T_j$. Once its whole root error $D_{*,j}$
and the two whole residual norms are available,

$$
 |L_\Omega u_j-L_\Omega T_j|
 \le2600D_{*,j}+184F_{-,j}+69F_{{\rm st},j}.
 \tag{PRN.22}
$$

The sign of the opposite residual does not change its norm.
Every genuine state jump would be added by (PRN.1); the displayed
TC specialization uses its proved continuous trial definition.

P96's final signed ball encloses the true phase functional of the
fixed candidate $T_j$, including its separate label, background,
arithmetic and root-sliver fees. Formula (PRN.22) can be added to
that entire ball when its inputs are actually complete. No centre
or uninflated trial pairing is substituted for it.

For a joint Euclidean96 input estimate, use the square root of the
sum of the96 squared complete error bounds, or a sharper genuinely
paired matrix bound when supplied. No unobserved direction or mean
is subtracted. The ordinary $L^2$ residual targets that would have
been needed by a direct use of PH.19 are therefore unnecessary for
this specific phase correction: the original TC source units suffice.

The original992/7724 prefix remains incomplete. Its true PDE source
columns, positive correction/root errors, independent physical
height/mean/Robin ports, nonmean phase, finite/high inverse and full
bordered Schur remain separate obligations. This theorem supplies a
complete receiver for those inputs; it does not declare them computed.
