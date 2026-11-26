# R149 supplement SDI: actual small density inverse constants and full Theta errors

2026-11-27, `visible-exact-astra-fb31ed6-20261127`.

**Proved from the four complete actual IL balls.** For the same true
selected map and the same sign compression as DC/DB, the complete
distributional inverse now satisfies

\[
 \|C^{-1}\|_{H^{-1}_0\to H^{-1}_0}<5/3,
 \qquad \|C^{-1}\|_{H^{-4/3}_0\to H^{-4/3}_0}<5/2.       \tag{SDI.1}
\]

Both are inhomogeneous Bessel norms. The full one-loss Theta error is
bounded in (SDI.9) below. These are consequences of the already completed
IL calculation and the proved DB inverse theorem. No IL target, flow,
KAM conjugacy, Fourier row or old norm is recomputed here.

## 1. The exact actual inputs and a valid first-derivative lower bound

Use [the complete actual IL result](R149-supplement-actual-original-inverse-density-lift.md),
run45896427415/1, with its original manifest
`eca231e77b0248c5585c751c157f82fc6d86985bb4fd24722bc51c9029b71a1d`.
Its whole actual SHA256 is
`9427186020322b43d99d49fc239c2150949f3155cafc66217ac01469bea88b5e`;
the whole execution SHA256 is
`8abee7df4e00e4296b6147929e10c729f852a011ea4e5e7c50a0f87874dbd499`.
All four target balls, including their full radii, give the strict
rational upper bounds

\[
 E_p<2.211\,10^{-7},\quad P_1<1.024974,\quad
 P_2<0.132457,\quad P_3<0.813049.                         \tag{SDI.2}
\]

The maps are precisely $p=H\circ X_-^{-1}$ and
$\widehat p=K_{48}\circ A_-$, on the complete error strip
$\sigma=1/256$, with the physical period $\pi/2$ and frequency $4n$.
The implicit selected parameter is unchanged. In particular it has not
been replaced by zero or by a numerical midpoint.

For clarity, the following subtraction uses an exact algebraic
decomposition, not subtraction of an upper bound for an unknown norm.
In [IL.4--5](R149-supplement-complete-inverse-density-lift-derivative-bounds.md),
the complete finite derivative sums satisfy

\[
 A_-'=1+a,\quad |a|\le A_1-1,\qquad
 K_{48}'=1+k,\quad |k|\le K_1-1,
 \qquad P_1\ge K_1A_1.
\]

The finite lift $A_-$ is real on the real axis. Thus

\[
 |\widehat p'-1|
 =|(1+k\circ A_-)(1+a)-1|\le K_1A_1-1\le P_1-1.
                                                               \tag{SDI.3}
\]

The constants1 are the actual degree-one derivatives and both full
Fourier sums are retained. No unknown mean or sign block is removed.
Cauchy's formula for the whole analytic difference $p-\widehat p$ gives
$\|(p-\widehat p)^{(r)}\|_\infty\le r!E_p\sigma^{-r}$.
Using smaller disks and taking their limit handles an open strip. Hence
the exact rational comparisons in (SDI.2--3) prove

\[
 \begin{gathered}
 p'>2-P_1-256E_p>m:=9749/10000,
 \qquad |p'|<1.0251,\\
 |p''|\le P_2+2\,256^2E_p<1/6=:b_2,\\
 |p'''|\le P_3+6\,256^3E_p<24=:b_3.
 \end{gathered}                                               \tag{SDI.4}
\]

These are bounds for the true map, not just its finite trial. Positivity
also follows from the original DC qualification; (SDI.4) is the sharper
qualified value used here.

## 2. The complete inverse bootstrap with actual constants

Apply the proved [DB theorem](R149-supplement-complete-Theta-row-regularity-and-negative-window-density-inverse.md)
with $m<1$, retaining its whole opposite-sign operator, both signs and
the zero-mean spaces. In its notation,

\[
 B_{\rm off}=\frac1{16}\left(\frac{b_3}{m^3}
                 +\frac{3b_2^2}{m^4}\right)<5/3,
 \quad L_0<10/9,\quad L_{1/3}<15/4.                         \tag{SDI.5}
\]

For $S=U_p^{-1}$ its two needed bounds are

\[
 S_0=m^{-1/2}<51/50,
 \quad S_{1/3}=\big[m^{-7/2}(m+b_2/4)\big]^{1/3}<21/20.
                                                               \tag{SDI.6}
\]

All comparisons are rational: for the second it suffices to verify
$(m+b_2/4)^2/m^7<(21/20)^6$. Also
$4^{-5/6}<1/3$, $(17/16)^{2/3}<21/20$, and
$\sqrt{17}/4<21/20$. These inequalities can be proved by raising
positive numbers to integer powers.

DB's inverse exists first on the entire
$\mathscr H=\dot H^{-1/2}_0$ by the exact two Krein identities; its
regularity bootstrap is not a Galerkin inverse or a smallness assumption.
Writing $T=(C^\dagger)^{-1}$, DB.17 now gives

\[
 \max\{\|T\|_{L^2_0\to L^2_0},
 \|C^{-1}\|_{\dot H^{-1}_0\to\dot H^{-1}_0}\}
 <\frac{51}{50}\left(1+\frac59\right)
 =\frac{119}{75}<\frac85.                                  \tag{SDI.7}
\]

For the inhomogeneous $H^{-1}$ norm, the one required comparison costs
$\sqrt{17}/4<21/20$, since the least nonzero physical frequency is4.
Thus its bound is less than
$(21/20)(119/75)=833/500<5/3$. For the original $H^{-4/3}$ window,
the one-factor comparison of DB.18 gives

\[
 \begin{aligned}
 K_{C,-4/3}
 &<(21/20)^2\left(1+\frac13\frac{15}4\right)\\
 &=\frac{3969}{1600}<\frac52.
 \end{aligned}                                               \tag{SDI.8}
\]

This proves (SDI.1) in the original Bessel spaces. It does not assert
that $C^{-1}$ has the same bound on $L^2$; the $L^2$ statement in
(SDI.7) concerns the specified energy-adjoint inverse $T$.

## 3. Actual full one-loss error for the original Theta rows

Keep the complete joint residual of the same96 trial columns,
$R=C^\dagger\widehat Z-B$, and let $\epsilon_H,\epsilon_0$ be
its whole $\ell^2_{96}\to\mathscr H$ and
$\ell^2_{96}\to L^2$ bounds. They must include both signs, all aliases,
tails and true-map errors, as in
[IR](R149-supplement-complete-inverse-density-row-residuals.md).
DB.24, with the unchanged $A=Id-\mathcal T_\alpha I$,
$K_A=1+\|\alpha\|_\infty/4$ and a completely qualified
$K_G=\|\overline G:Y_a^0\to H^{-1}\|$, yields

\[
 \boxed{\quad
 \|\Theta-\widehat\Theta\|
 <\frac{1071}{1000}K_GK_A
          (\epsilon_0+\tfrac{10}{9}\epsilon_H).
 \quad}                                                       \tag{SDI.9}
\]

Here $1071/1000=(21/20)(51/50)$. This is a joint96 bound; no
additional $\sqrt{96}$ is required. If the actual multiplication
coefficient $\alpha$ is replaced by a trial, the separate full DB.25
term remains and is at most $(21/20)K_G e_\alpha Z_G$ in its original
units. Neither a missing signed $\alpha$ carrier nor a partial IR
prefix supplies that term. A complete norm, when needed, is

\[
 \|\Theta\|
 <\frac{1071}{1000}K_GK_A
       (384+\tfrac{10}{9}\sqrt{384}).                         \tag{SDI.10}
\]

This is a sufficient whole norm, not a claim that the bound has been
used to pass a finite physical matrix gate.

## 4. The unchanged whole graph and retained finite equations

Substitute (SDI.8), conservatively $K_{C,-4/3}<4$, into the **general**
ordered bounds DG.14 and DG.18 of
[DG](R149-supplement-complete-graph-remainder-through-same-sign-density-compression.md).
Every old graph term and its physical qualification remains. At the
same $J=2^{4608}$ this gives

\[
 \begin{aligned}
 \|P_JK_0P_J\|&<2^{-449},\\
 \|P_JK_+P_J\|&\le2^{-1474}C_{\rm add},\\
 \|P_JU_{\rm phys}\Theta P_J\|
       &\le2^{-1491}D_{96}+2^{-1482}.                         \tag{SDI.11}
 \end{aligned}
\]

Consequently $C_{\rm add}\le2^{1471}$ and $D_{96}\le2^{1488}$
are sufficient for the full physical96-augmented high deviation to be
less than1/2. These two inputs still require the actual whole common6
and PN56 certificates. Their absence is not converted to a successful
gate. The unchanged ordinary finite complement has dimension $J-1$;
all low/cross equations, original source/target normalizers, two physical
means, height, true parameter and phase border remain. The actual
physical signed square and nonlinear closed-family construction are
not concluded here.

The accompanying [exact saved-ball checker](../scripts/fourfold_codazzi_small_density_inverse_saved_bounds.py)
checks only the full fixed IL files and rational implications above.
It calls no scientific producer and creates no replacement actual
records. The original four successful targets remain the sole IL data.
