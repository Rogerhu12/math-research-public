# R147 WRC: complete reference-world height and its original negative receiver

2026-11-27, visible-exact-astra-fb31ed6-20261127 / positive_inverse.

**Proved:** the original fixed reference anchors at $b=9/50$ give a
complete physical mean-height parameter column from one additional RHI
contraction, with the full physical-angle term paid. Its correction
from the original weak root/strict PDE sources has the explicit bound

$$
 \boxed{\quad
 |\mathcal L_{\rm ref}(h)|
 <94000(D_*+J_-)+6650F_-+3000F_{\rm st}+8850J_{\rm st}.
 \quad}                                                     \tag{WRC.1}
$$

The units and true interfaces are the original ones of PRN/RRM. No
angular $L^2$ residual or strong trace is inferred from those weak
sources. The actual independent $Q_b,F_b,Y_b,K_b$ ports remain separate.
This result does not declare an unknown actual exterior anchor equal
to the original reference anchor.

## WRC1. Exactly which world is fixed

Retain all conventions and identities of
[WMR](R147-supplement-original-world-anchor-and-physical-mean-height-reduction.md).
In particular the old absolute frame has determinant $-1$, the relative
$A$ is in $SO(3)$ and the fixed world height is the original
$H_*=4347844570122155/4503599627370496$.

Let $\mathsf Q_b^{\rm raw},F_b^{\rm raw}$ be the old reference-model
values at $b$, in that same world. On $[0,b]$ use the original selected
physical state $Q_{\delta_*}$ and its metric $\nu_{\delta_*}$.
The selected short reference model is

$$
 \mathsf Q_{\rm ref}(r)=\mathsf Q_b^{\rm raw}A_\delta(r),
 \qquad F_{\rm ref}(r)=F_b^{\rm raw}
                         +\mathsf Q_b^{\rm raw}x_\delta(r).
                                                               \tag{WRC.2}
$$

This is a precisely defined model with fixed original anchors at $b$.
It does not silently supply the anchor obtained by integrating the
selected state through the remaining interval $[b,25/8]$. Such an
anchor difference belongs to the independent ports below.

Write $q_b=e_z^T\mathsf Q_b^{\rm raw}$,
$q_0=q_bA_\delta(0)$ and $f_0=e_z^TF_{\rm ref}(0)$.
The complete old waist alignment from
[G.4](R133-supplement-complete-141-block-continuous-model-geometry.md)
is

$$
 e_Q=0.000108594777739,\qquad e_F=0.000232681812735.
                                                               \tag{WRC.3}
$$

The canonical old waist has constant vertical frame row $e_1^T$
and exactly zero vertical position. Its full canonical curve is
not reset to a point.

For the same selected short state, retain the actual bounds
$\epsilon=2\,10^{-9}$, $d=10^{-10}$ from WMR2. Define the positive
already-paid comparison budgets

$$
 \begin{aligned}
 B_M&=15.736315\epsilon+0.304809d=3.15031109\,10^{-8},\\
 B_F&=30.196406\epsilon+0.105999d=6.04034119\,10^{-8}.
 \end{aligned}                                               \tag{WRC.4}
$$

Here $B_M$ bounds the integral of the complete connection difference.
$B_F$ bounds the complete short position change and, separately, the
integral of the direct velocity difference: the direct-velocity
integral is one nonnegative component of the full C.17 majorant.
No component is obtained by subtracting two upper bounds.

By the original orthogonal comparisons
[C.16--18](R133-supplement-complete-C0-state-and-nu-geometry-response.md),
restricted to the short interval,

$$
 \|q_0-e_1^T\|_\infty<\kappa_Q:=0.000108627,\qquad
          \|f_0\|_\infty<\kappa_F:=0.000232743.            \tag{WRC.5}
$$

The second estimate is $e_F+B_F$; it includes the same old fixed
world translation. It is a bound on a genuine complete scalar
height function, not on saved grid samples alone.

## WRC2. Whole first angular derivatives from paid second derivatives

The original exact-waist alignment
[A.8](R133-supplement-exact-waist-grid-and-complete-canonical-alignment.md)
gives, on the whole true angle circle,

$$
 \|Q_{\rm raw,\phi\phi}(0)\|_{\rm op}<4.646383,\qquad
             |F_{\rm raw,\phi\phi}(0)|<5.970523.           \tag{WRC.6}
$$

Both results already include the complete residual, true source mean,
all 7722 old boxes and all 6143 original value interfaces. They are
not rerun here.

For a twice differentiable periodic Banach-valued function with
$\|f\|_\infty\le e$ and $\|f''\|_\infty\le M$, central differences give

$$
 \|f'\|_\infty\le e/t+Mt/2
 \quad(t>0),\qquad
                  \|f'\|_\infty\le\sqrt{2eM}.             \tag{WRC.7}
$$

The argument is the integral Taylor remainder on the two sides of
a point, followed by $t=\sqrt{2e/M}$. It applies directly to the
Euclidean row/vector norm. The vertical world projections are
fourfold periodic even though the full horizontal world frame is
equivariant under a quarter-turn.

Apply (WRC.7) to $e_z^TQ_{\rm raw}(0)-e_1^T$ and
$e_z^TF_{\rm raw}(0)$. The complete original bounds yield

$$
 \left|\partial_\phi(e_z^TQ_{\rm raw}(0))\right|<0.03177,
 \qquad
 \left|\partial_\phi(e_z^TF_{\rm raw}(0))\right|<0.05272.
                                                               \tag{WRC.8}
$$

The selected and raw connection matrices and velocity vectors have
angular degree at most288. Their only inverses are radial scalar
means and metric functions. Thus Banach-valued Bernstein gives
a factor $4\cdot288=1152$ for their angular differences. This is
a bound on the known background coefficients, not a Fourier
cutoff on an unknown correction.

The already paid RRM short bounds are

$$
 |M_\phi|_{\rm op}<12,\quad |c|<C_0=19/5,\quad
 |c_\phi|<C_1=25/2,\quad b=9/50.
                                                               \tag{WRC.9}
$$

Every real subinterval propagator has angular derivative at most
$12b$. Differentiating the Duhamel integral, including both
propagator factors, gives the safe complete bounds

$$
\begin{aligned}
 \|\Delta A\|_\infty&\le B_M,\\
 \|\Delta A_\phi\|_\infty&\le(1152+24b)B_M,\\
 \left\|\partial_\phi(A_{\rm raw}^TA_\delta)\right\|_\infty
                         &\le(1152+36b)B_M,\\
 \|\Delta x_\phi\|_\infty
 &\le(1152+24b)B_M C_0b+B_M C_1b+(1152+12b)B_F,\\
 |\partial_\phi\Delta f_0|
 &\le\|\Delta x_\phi\|_\infty+(0.03177+12b)B_F .
\end{aligned}                                                \tag{WRC.10}
$$

For the relative-position line expand
$\Delta(Ac)=\Delta A\,c_{\rm raw}+A_\delta\Delta c$
and differentiate every factor. The $\Delta c$ integral uses
the genuine nonnegative component bound in WRC1.
The final line retains the actual angular outer-frame term:
$\Delta f_0=q_b\Delta x(0)$, so
$\partial_\phi\Delta f_0=q_b\Delta x_\phi+q_{b,\phi}\Delta x$.
Here the raw identity $q_b=(e_z^TQ_{\rm raw}(0))A_{\rm raw}(0)^T$
gives $|q_{b,\phi}|<0.03177+12b$ independently of the selected
bound being proved. The extra contribution is less than
$1.324\,10^{-7}$ and is explicitly included in the new exact
comparison for (WRC.11). The piecewise
radial coefficient joins cause no lost angular or endpoint term:
the passive propagators and positions themselves are continuous,
and each integral includes every original piece.

Since $q_0=(e_z^TQ_{\rm raw}(0))A_{\rm raw}(0)^TA_\delta(0)$,
real orthogonality and (WRC.8--10) give

$$
 \boxed{\quad |q_{0,\phi}|<0.03181,\qquad
                         |f_{0,\phi}|<0.05282.\quad}      \tag{WRC.11}
$$

In particular

$$
 |q_{b,\phi}| \le |q_{0,\phi}|+|A_{\delta,\phi}(0)|
                           <2.19181.                     \tag{WRC.12}
$$

These are actual complete derivative bounds for the specified reference
world. A mere $C^0$ anchor error would not justify its action on a
weak $H^{-1}$ correction; (WRC.11) supplies the missing regularity.

## WRC3. The complete reference parameter column

Let $h=v_\nu$ be the true strict parameter particular and use
$(h,\kappa)=(v_\nu,1)$ in RHI. As in WMR, put
$J=v/m$, $g=h_2/m-v\Pi h_2/m^2$ and $y=y_\nu(0)$.
Holding the independent reference $b$-anchor ports fixed, the
complete physical mean-height derivative is exactly

$$
 \boxed{\quad
   \mathcal L_{\rm ref,\nu}
       =\Pi Jq_b y+\Pi g f_0
       =\Pi Jq_0A^Ty+\Pi g f_0 .
 \quad}                                                     \tag{WRC.13}
$$

The second term is the whole physical-coordinate variation.
It is small because the original reference waist is close to
the same actual canonical plane, not because the term was deleted
or a per-angle gauge was chosen.

Use the unchanged WMR interpolants and define the one new complete
Fourier contraction

$$
 T^a=\Pi e_1^T\widehat A^T(J_0\widehat y),\qquad
          C_2\ge\|J_0\widehat y\|_2.                      \tag{WRC.14}
$$

Its angular degree is at most2080, so the same8192-point directed
quadrature already covers every product exactly. Retain all whole
WMR inputs $E_A,E_Y,E_J,E_G,Y_2,G_2$, and put

$$
\begin{aligned}
 E_W&=(27/8)E_Y+E_JY_2,\\
 U_W&=C_2+E_W,\qquad
 E_T=E_W+E_AC_2,\qquad G_*=G_2+E_G.
\end{aligned}                                                \tag{WRC.15}
$$

Then the complete fixed-reference physical mean-height column lies in

$$
 \boxed{\quad
 T^a+[-1,1]\{E_T+\kappa_Q U_W+\kappa_FG_*\}.
 \quad}                                                     \tag{WRC.16}
$$

This retains the true full PDE response and the two actual means.
It does not use the weak-source receiver of the next section to
invent any missing strong norm: $E_Y$ and $G_*$ come from the
genuine completed RHI and ASB strong inputs already specified
by WMR.

A first WMR execution can save this as a fourth new target while
retaining its original three targets. The original carrier restoration
and8192-point grids are shared. No old target, long geometry ODE,
norm or phase pairing is repeated. A real RHI completion is still
required before an entry is generated or run.

For an actual base anchor let
$B_Q=\|\mathsf Q_b-\mathsf Q_b^{\rm raw}\|_\infty$ and
$B_P=\|F_b-F_b^{\rm raw}\|_\infty$. Its full mean-height value
differs from (WRC.13), before its independent varying ports, by at most

$$
 B_Q\{U_W+(C_0b)G_*\}+B_PG_* .                            \tag{WRC.17}
$$

The remaining varying port is exactly

$$
            \Pi J e_z^T(Y_b+K_b\mathsf Q_bx).              \tag{WRC.18}
$$

These are genuine independent actual inputs. A fixed vertical
translation drops from the $gF_b$ term because $\Pi g=0$;
an independently varying vertical translation remains in $Y_b$.

## WRC4. Weighted relative-position row in the original weak spaces

For a state correction $h$ at the same background, $\kappa=0$.
Define $y_h$ by the complete linearized relative ODE with zero
variation of its independent $b$-anchor. Its weighted position
test in (WRC.13) is

$$
              w(\phi)=J(0,\phi)q_b(\phi)^T.
$$

By the complete bounds of RRM2 and (WRC.12),

$$
 |w|\le W_0=27/8,\qquad
 |w_\phi|\le {11/2\over16/15}+{27\over8}(2.19181)
                                  <W_1=12.554.           \tag{WRC.19}
$$

RRM's exact Fubini formula for $y_h(0)$ has source loads

$$
 q(r)=A(r)^T(X(r)\times w),\qquad z(r)=-A(r)^Tw,\qquad
                   X(r)=\int_0^r A(s)c(s)\,ds .
                                                               \tag{WRC.20}
$$

The two full adjoints are $L_m^*q+L_c^*z$, with the original
mean/primitive terms retained. For a constant unit test, RRM
already bounds their joint $H^1$ norm by26. When the test depends
on angle, differentiating $w$ adds at most

$$
       {5\over2}(C_0r+1)|w_\phi|
       \le{5\over2}(C_0b+1)W_1 .
$$

This uses the genuine full $L^2$ norms of $L_m,L_c$, including
their mean ranks. It does not commute an angular weight through
the nonlocal primitive. The coefficient commutators from RRM
remain in the first term. Therefore the entire dual load satisfies

$$
 \|L_m^*q+L_c^*z\|_{H^1}
   \le26W_0+{5\over2}(C_0b+1)W_1
          =140.60234<141.                                \tag{WRC.21}
$$

Consequently
$|\Pi Jq_b y_h(0)|\le141\int_0^b\|h(r)\|_{H^{-1}\oplus H^{-1}}dr$.
All Fourier modes and both means remain in this duality.

For the coordinate term use the exact identity
$g_h=\partial_\phi\dot\Theta_h$. Periodicity and (WRC.11) give

$$
 |\Pi g_h f_0|
  =|\Pi\dot\Theta_h f_{0,\phi}|
  \le {5\over4}(0.05282)\|(Ih,\Pi h)(0)\|
  =0.066025\|(Ih,\Pi h)(0)\| .                            \tag{WRC.22}
$$

The $5/4$ factor is the already proved full mean-preserving angle
map of RH6. A constant phase port contributes zero here only
because the physical test is the mean. Nonconstant height tests
retain that separate port.

## WRC5. Complete original root/strict source reception

Use exactly the definitions and interface assignment of
[RRM1](R149-supplement-relative-frame-position-means-in-original-negative-source-windows.md):
$D_*$ is the true-root state norm in $H^{-2/3}\oplus H^{-1}$;
$F_-,J_-$ are the complete root ordinary $L^2(dr)$ source and
unweighted affine-jump sums in those units; $F_{\rm st},J_{\rm st}$
are their complete strict counterparts in $H^{-1}\oplus H^{-1}$.
A cut jump is assigned to the root side exactly once.

Retain the original constants

$$
\begin{gathered}
 r_c={2333968743003\over10^{13}},\quad R=1/200,\quad
 q_0=2669/5000,\quad U=173.872,\\
 N_I=11.272695,\qquad J_{\rm in}=1.060693 .
\end{gathered}
$$

The already completed SP products include every shorter ordered
product and every source insertion. They imply

$$
 \|(Ih,\Pi h)(0)\|
 \le{U\over q_0}\left[
 N_I(D_*+J_-+\sqrt R F_-)
 +J_{\rm in}(\sqrt{r_c}F_{\rm st}+J_{\rm st})\right].
                                                               \tag{WRC.23}
$$

This is a true endpoint propagation bound, not a trace obtained
from an ordinary radial $L^2$ norm.

Let $C=141$ and $c_\theta=0.066025$. The exact same Fubini weights
as RRM, plus the endpoint term (WRC.23), give four positive coefficients

$$
\begin{aligned}
 K_D&={UN_I\over q_0}(Cb+c_\theta),&
 K_-&=K_D\sqrt R,\\
 K_{\rm st}
  &={UJ_{\rm in}\over q_0}
    \{Cb\sqrt{r_c-2b/3}+c_\theta\sqrt{r_c}\},&
 K_J&={UJ_{\rm in}\over q_0}(Cb+c_\theta).
\end{aligned}                                                \tag{WRC.24}
$$

The source on $[b,r_c]$ is included through the original insertion
weights. There is no radial length factor on an affine impulse.
Exact rational upper comparisons, using only
$\sqrt R<0.070711$, $\sqrt{r_c-2b/3}<0.337$ and
$\sqrt{r_c}<0.484$, give

$$
       K_D<94000,\quad K_-<6650,\quad
       K_{\rm st}<3000,\quad K_J<8850.                    \tag{WRC.25}
$$

Combining (WRC.21--25) proves (WRC.1). For original TC96 columns
the corresponding complete actual source records are still needed.
Their completion is not asserted here. Once available, (WRC.1)
corrects each new reference-height trial entry in the original
source units, and an $\ell^2$ combination of those entire errors
corrects the full signed row.

## WRC6. Actual scope and new saved comparisons

Correction to the first publication658c31092cb0995bfc4a52ec3eded7244edf9231:
(WRC.10) now explicitly differentiates the angular fixed reference
anchor. The previous relative-position derivative did not by itself
bound the world-height derivative. The retained additional term is
$q_{b,\phi}\Delta x$. It leaves $|f_{0,\phi}|<0.05282$, all four
receiver constants and the first-execution target formulas unchanged.
No scientific entry had been triggered by the first publication.

The companion
[saved-bound consumer](../scripts/fourfold_codazzi_reference_world_height_saved_bounds.py)
contains the original14 exact rational comparisons and one additional
comparison retaining $q_{b,\phi}\Delta x$, for15 in total. The original14
were not rerun. The additional complete derivative comparison was
evaluated once with exact integer fractions and passed. No source field,
old model norm, old geometry integral, RHI target or TC target
was evaluated.

The new fourth contraction in WRC3 remains a genuinely new
scientific target. Its input must be the real whole RHI result.
The original determinant-$-1$ world, actual $b$-anchor differences,
rigid ports, two means, true-root transmissions and full
high/finite/phase Schur remain explicit. This result does not
claim the topic complete.
