# R149 RRM: relative frame and position means in the original negative source windows

2026-11-27, visible-exact-astra-fb31ed6-20261127 / positive_inverse.

**Proved.** The complete relative moving-mean rows can receive the
original TC negative residual units directly. On the original selected
background, let $h$ be the full fixed-metric Jacobi response. Let
$\mathcal U(h)$ and $\mathcal Y(h)$ be the three-component moving means
of its short relative axial-frame and position variations. Then

$$
\begin{aligned}
 |\mathcal U(h)|&\le9300(D_*+J_-)+658F_-+294F_{\rm st}+871J_{\rm st},\\
 |\mathcal Y(h)|&\le17200(D_*+J_-)+1217F_-+545F_{\rm st}+1617J_{\rm st}.
                                                        \tag{RRM.1}
\end{aligned}
$$

The first root/source component keeps its original $H^{-2/3}$ unit;
the second keeps $H^{-1}$. Both strict components keep $H^{-1}$.
Ordinary source norms use $L^2(dr)$, and impulses have no radial-length
factor. All Fourier modes and both moving means are retained.

These are relative functional receivers, not whole world-height values.
The original $Q_b,F_b$, rigid ports and physical-coordinate term remain
independent. In particular the result removes the need for a new
ordinary angular $L^2$ residual solely to correct these relative
mean rows. It does not declare the unfinished TC residuals complete.

## RRM1. Same state, exact cut and all source units

Use the original selected $Q_{\delta_*}$, fixed $\eta_0$ and
$|\delta_*|<10^{-10}$. Put

$$
 b=9/50,\qquad r_c=2333968743003/10^{13},\qquad R=1/200,
$$

with the true root interval and its actual left/right states exactly
as [PRN.2--3](R149-supplement-complete-phase-receiver-in-original-negative-source-windows.md).
In particular $0<r_*-r_c\le R$ and $b<r_c$.
For the full physical moving pair define

$$
\begin{aligned}
 D_*&=\|h(r_*)\|_{H^{-2/3}\oplus H^{-1}},\\
 F_-&=\|f\|_{L^2([r_c,r_*];H^{-2/3}\oplus H^{-1})},&
 J_-&=\sum_{r_j\in[r_c,r_*)}\|j_j\|_{H^{-2/3}\oplus H^{-1}},\\
 F_{\rm st}&=\|f\|_{L^2([0,r_c];H^{-1}\oplus H^{-1})},&
 J_{\rm st}&=\sum_{r_j\in(0,r_c)}\|j_j\|_{H^{-1}\oplus H^{-1}}.
                                                        \tag{RRM.2}
\end{aligned}
$$

A cut impulse is assigned to the root side once, so the strict leg
starts at the actual $h(r_c-)$. A true root-state correction is an
independent input even when a finite trial has exact identity
transmissions. The source on $[b,r_c]$ is not discarded just because
the relative functional itself integrates only over $[0,b]$.

Use normalized angular measure and actual frequencies $4j$.
Here $H^{-1}$ is the Bessel norm with weight $(1+16j^2)^{-1/2}$.
The relative variation is the fixed-metric part of RH.7--9. For
the true parameter column versus its trial, both have the same
$\kappa=1$, so their difference has $\kappa=0$ at the same background.
The signed parameter column still includes all its direct metric terms.

## RRM2. Complete base and angular bounds

The original [SP actual bounds](R133-supplement-actual-complete-primitive-and-mean-strict-propagation-to-the-waist.md),
[SJA](R133-supplement-actual-complete-strict-radial-first-symbol-defect.md)
and [RH.2--13](R147-supplement-relative-height-carriers-and-short-full-frequency-errors.md)
give, on the entire short interval, the following genuine suprema:

$$
\begin{gathered}
 |m|\ge M=16/15,\quad |\beta|\le B=211/1000,\quad
 1<\gamma\le G=28/25,\quad |K|\le K_*=21/20,\\
 q=\sqrt{-K},\quad q_0=2669/5000<q<q_*=103/100,\quad
 a\le a_*=9/8,\\
 \sqrt{u^2+q^2v^2}\le R_0=239/125,\qquad
 \sqrt{u_\phi^2+q^2v_\phi^2}\le L_0=463/125 .
                                                        \tag{RRM.3}
\end{gathered}
$$

Consequently use $U=R_0$, $V=18/5$, $U_1=L_0$ and $V_1=11/2$
as bounds for $|u|,|v|,|u_\phi|,|v_\phi|$.
For the last bound, the complete original angular Wiener bound is
$5.437241$, with the $1.970\,10^{-17}$ continuous-repair fee and
the full selected $83\,10^{-10}$ direction fee; see
[D.4--6](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md)
and PRN4. Their sum is below $11/2$. It is not a sampled derivative.

The already paid full $L^2$ operators for state variation satisfy

$$
 \|L_mh\|_2\le(5/2)\|h\|_2,\qquad
 \|L_ch\|_2\le(5/2)\|h\|_2,\qquad |c|\le C_0=19/5,
                                                        \tag{RRM.4}
$$

where $L_mh=\operatorname{ax}(D_Q\mathsf M[h])$ and
$L_ch=D_Qc[h]$. They include the full moving mean
$\mu=\Pi h_2$. They do not require reflected input $h$.

## RRM3. Full angular commutators of the state operators

All scalar metric coefficients and $m=\Pi v$ are radial. Set

$$
\begin{gathered}
 D=(2/5)BR_0^2,\quad D_1=2BR_0^2,\quad
 C_d=Bq_*R_0/2,\quad C_{d1}=Bq_*L_0/2,\\
 J_0=V/M,\quad J_1=V_1/M,\quad C_J=V/M^2.
                                                        \tag{RRM.5}
\end{gathered}
$$

The exact $d=-\beta I(u^2+Kv^2)$ satisfies $|d|\le D$ and
$|d_\phi|\le D_1$. The factor two in $D_1$ retains the removed
quadratic mean. Since $I$ and $\Pi$ commute with $\partial_\phi$,
the coefficient commutator is obtained by differentiating all angular
coefficients in the original operator. In particular

$$
\begin{aligned}
 D_dh&=-2\beta I(uh_1+Kvh_2),\\
 [\partial_\phi,D_d]h&=-2\beta I(u_\phi h_1+Kv_\phi h_2),\\
 D_Jh&=(h_2-J\mu)/m,\qquad
 [\partial_\phi,D_J]h=-v_\phi\mu/m^2.
                                                        \tag{RRM.6}
\end{aligned}
$$

Their norms are bounded respectively by $C_d,C_{d1},C_J,V_1/M^2$.
The exact complete rank-one norm $C_J$ is RH.10; the mean is not
deleted before differentiating.

Using every term of RH.9 at $\kappa=0$, the commutator for
$\dot\tau$ has norm at most

$$
 T^\#=J_1C_d+J_0C_{d1}+D_1C_J+DV_1/M^2<9.             \tag{RRM.7}
$$

For the three connection entries set

$$
\begin{aligned}
 P^\#&=BT^\#,\\
 T_f^\#&=a_*(C_{d1}/M+D_1/M^2),\\
 K_f^\#&=a_*\{(U_1C_d+UC_{d1})/M+D_1/M
                         +(D_1U+DU_1)/M^2\}.
                                                        \tag{RRM.8}
\end{aligned}
$$

The last summand in $K_f^\#$ pays the full moving-mean coefficient
$-du\mu/m^2$, including both its angular product terms.
The new rational combinations give

$$
 (P^\#)^2+(T_f^\#)^2+(K_f^\#)^2<64,\qquad
 a_*T^\#<10.
$$

Thus, on the complete real $L^2$ spaces,

$$
 \|[\partial_\phi,L_m]\|<8,\qquad
 \|[\partial_\phi,L_c]\|<10.                           \tag{RRM.9}
$$

Integration by parts yields
$[\partial_\phi,L^*]=[\partial_\phi,L]^*$.
Consequently, for every full three-vector row $z$,

$$
\begin{aligned}
 \|L_m^*z\|_{H^1}&\le(5/2)\|z\|_{H^1}+8\|z\|_2,\\
 \|L_c^*z\|_{H^1}&\le(5/2)\|z\|_{H^1}+10\|z\|_2.
                                                        \tag{RRM.10}
\end{aligned}
$$

This follows by Minkowski applied to the zeroth and first derivative
components. It keeps the commutators with every mean coefficient.

## RRM4. Actual relative angular frame derivative

The actual connection derivative is bounded directly, not by applying
an $L^2$ operator norm pointwise. Set

$$
 T_1=D_1J_0+DJ_1+GU_1,\quad
 P_1=BT_1,\quad T_{f1}=a_*D_1/M,\quad
 K_{f1}=a_*\{GK_*V_1+(D_1U+DU_1)/M\}.
$$

The same new rational comparisons give

$$
 P_1^2+T_{f1}^2+K_{f1}^2<144,\qquad a_*T_1<25/2.
$$

Therefore the true real connection and velocity satisfy

$$
 \|\mathsf M_\phi\|_{op}<12,\qquad |c_\phi|<25/2.
                                                        \tag{RRM.11}
$$

The relative $A_r=A\mathsf M$, $A(b)=I$, is orthogonal.
Differentiate this actual equation and use its real orthogonal
propagators. This proves the complete pointwise bound

$$
                  \|A_\phi(r)\|_{op}\le12(b-r).         \tag{RRM.12}
$$

No bound on $Q_b'$ is used here; $A$ is relative, and the true
world anchor remains a separate function.

## RRM5. Exact adjoint rows and their full H1 norms

For the fixed-metric state response define

$$
 u_h(0)=-\int_0^b A(r)L_mh(r)\,dr .
$$

For every constant real unit vector $w$, its full scalar row is
$L_m^*z$ with $z=-A^Tw$. Equations (RRM.10),(RRM.12) give

$$
 \|L_m^*z\|_{H^1}
 \le(5/2)\sqrt{1+144(b-r)^2}+8<14.                    \tag{RRM.13}
$$

This is the complete row, including its angular mean.

For position, change the order of the two genuine radial integrals.
With $X(r)=\int_0^r A(s)c(s)\,ds$, the exact identity is

$$
 y_h(0)=\int_0^b\{(A L_mh)\times X-A L_ch\}\,dr .
                                                        \tag{RRM.14}
$$

Its $w$-row is $L_m^*z_m+L_c^*z_c$, where

$$
             z_m=A^T(X\times w),\qquad z_c=-A^Tw .
$$

Both signs and the original world-coordinate order are fixed by
(RRM.14). From (RRM.11--12),

$$
\begin{aligned}
 |X(r)|&\le C_0r,\\
 |X_\phi(r)|&\le12C_0(br-r^2/2)+(25/2)r,\\
 |z_m'|&\le r(B_0-B_1r),\qquad
 B_0=24C_0b+25/2,\quad B_1=18C_0 .
                                                        \tag{RRM.15}
\end{aligned}
$$

Put $g=103/100$ and $s=16/25$. Direct positive rational comparisons
prove, for $0\le r\le b$,

$$
\begin{aligned}
 \|z_m\|_{H^1}&\le g\,r(B_0-B_1r),&
 \|z_m\|_2&\le C_0r,\\
 \|z_c\|_{H^1}&\le1+12s(b-r),&
 \|z_c\|_2&=1 .
                                                        \tag{RRM.16}
\end{aligned}
$$

For the first inequality it suffices that
$C_0^2<(g^2-1)(B_0-B_1b)^2$.
For the third use convexity of $\sqrt{1+t^2}$ and its chord on
$[0,12b]$, with $\sqrt{1+(12b)^2}<1+12sb$.

Substitution into (RRM.10) gives a concave quadratic upper bound

$$
 P(r)=(25/2)+30sb+
       \{(5/2)gB_0+8C_0-30s\}r-(5/2)gB_1r^2 .
$$

Its derivative is positive throughout $[0,b]$, and its exact endpoint
value is $P(b)=25.667954<26$. Thus the complete position row satisfies

$$
              \|L_m^*z_m+L_c^*z_c\|_{H^1}<26.         \tag{RRM.17}
$$

Taking the supremum over all unit $w$ gives the Euclidean norms of
the three-component mean outputs, with no extra $\sqrt3$.
For smooth $h$, duality proves

$$
 |\mathcal U(h)|\le14\int_0^b\|h(r)\|_{H^{-1}\oplus H^{-1}}dr,\qquad
 |\mathcal Y(h)|\le26\int_0^b\|h(r)\|_{H^{-1}\oplus H^{-1}}dr .
                                                        \tag{RRM.18}
$$

These exact full rows extend by density to the rough source spaces.
There is no assertion of a pointwise frame solution for arbitrary
distributional input, and no unproved angular regularity upgrade.

## RRM6. Full primitive-and-mean propagation from the true root

Use the original SP energy

$$
 \mathcal E_q(h)^2=\|Ih_1\|_2^2+q^2\|Ih_2\|_2^2
                         +|\Pi h_1|^2+q^2|\Pi h_2|^2.
$$

The exact Bessel weights give

$$
 \|h\|_{H^{-1}\oplus H^{-1}}
 \le\|(Ih,\Pi h)\|\le q_0^{-1}\mathcal E_q(h).          \tag{RRM.19}
$$

The first inequality preserves the zero-frequency weight one; the
second uses $q>q_0$ only on the strict interval.

The completed original root and SP conclusions, with their complete
source-insertion qualifiers, give

$$
 N_I=11.272695,\quad U_-=173.872,\quad J=1.060693 .
$$

Their provenance and original whole run numbers are
[PRN.14--18](R149-supplement-complete-phase-receiver-in-original-negative-source-windows.md):
root run43621934843/1 and SP run43731464771/1. These are the original
selected constants, not the later compact-centre transfer.
At the true cut,

$$
 \mathcal E_{q(r_c)}(h(r_c-))
 \le N_I\{D_*+J_-+\sqrt R\,F_-\}.                    \tag{RRM.20}
$$

The complete $(I,\Pi)$ operator, not just the primitive, is paid by
the original product $C_I C_{-1}=N_I$; PRN4 proves the exact mean
qualification. For every $r\in[0,b]$ the complete reverse SP bound gives

$$
 \mathcal E_q(h(r))\le U_-\left[
 N_I\{D_*+J_-+\sqrt R F_-\}
 +J\int_r^{r_c}\|f(s)\|_{H^{-1}\oplus H^{-1}}ds
 +J\sum_{r_j\ge r}\|j_j\|_{H^{-1}\oplus H^{-1}}\right].
                                                        \tag{RRM.21}
$$

This retains all intervening original seams, both means and every
shorter ordered propagation. No endpoint trace is taken from an
ordinary radial $L^2$ estimate.

## RRM7. The short functional still receives the entire strict interval

Changing order over the exact rectangle/triangle gives

$$
 \int_0^b\int_r^{r_c}\|f(s)\|\,ds\,dr
   =\int_0^{r_c}\min(b,s)\|f(s)\|\,ds
   \le b\sqrt{r_c-2b/3}\,F_{\rm st}.                 \tag{RRM.22}
$$

Each strict impulse is multiplied by $\min(b,r_j)\le b$, retaining
its source status; no square-root radial factor is assigned to it.
For either row bound $C=14$ or $26$, (RRM.18--22) give

$$
 {CU_-\over q_0}\left[
 bN_I(D_*+J_-+\sqrt R F_-)
 +Jb\sqrt{r_c-2b/3}\,F_{\rm st}+JbJ_{\rm st}\right].
                                                        \tag{RRM.23}
$$

The [new exact rational consumer](../scripts/fourfold_codazzi_relative_mean_negative_receiver_saved_bounds.py)
checks the squared positive source
comparisons and the linear root/impulse comparisons. They yield
(RRM.1). All 18 new rational combinations were evaluated once from
these already completed constants; no old scientific target or
carrier was re-evaluated.

For a completed TC column, insert its actual complete negative source
bounds and independent true root correction into (RRM.1). Until those
whole bounds exist, the true column remains conditional. The relative
candidate row and this receiver do not prove the finite inverse or a
phase/height Schur. Actual world height still uses the full
$Q_b(\phi),F_b(\phi)$, its independent terminal variations and the
unchanged $C_\theta$ row; a moving mean does not replace any of them.
