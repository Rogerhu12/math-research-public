# R133 CG: the existing actual cap lies in the final moving C0 ball

2026-11-28, visible-exact-astra-b0d5a16-20261128 / cap_world.

**Proved.** Every admitted real reflected M cap, including the actual
selected SCAP cap, satisfies on the complete interval
$[9/10,25/8]$ and the full original moving circle

$$
 \boxed{\quad
 \|u_*-u_{\rm raw}\|_\infty+
 \|v_*-v_{\rm raw}\|_\infty
                   <0.000099309<10^{-4}.\quad}          \tag{CG.1}
$$

All angular frequencies and the actual even mean are included.
The cap's part of the final geometry state-comparison requirement is
therefore automatic once its original inputs are admitted. The
unknown core must still enter that input domain, match this same
cap and meet its own state bound. No such core existence or input
admissibility is inferred here.

The proof consumes only complete saved bounds and the original
fixed-point equations. It does not run the cap iteration again or
impose an angular cutoff on its solution.

## 1. Same already constructed solution and a sharper radius

Use the original repaired centre
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`,
the fixed original $\eta_0$, and the full two-input cap
[M](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md).
The real reflection class has $B$ odd, $C$ even, and even nonmean
inputs $\gamma,f_B$ with

$$
 \|\gamma\|_{A^0}<10^{-9},\qquad
 \|f_B\|_{\dot A^2}<2^{-60}.                            \tag{CG.2}
$$

Whenever finite regularity is needed to realize the cap geometry,
retain M's original finite-regularity domain, in particular the
one used by SCAP. The value estimate itself uses only the original
complete zero-width norm.

Write the actual physical curvature as
$W_*=(B_*,C_*)=\widehat W+x$, $x=(b,c)$, and put

$$
 t=\|x\|_{X_0},\qquad
 \rho=3\,10^{-6},\qquad 0\le t\le\rho.                 \tag{CG.3}
$$

This is the already solved M fixed point, with the original
independent endpoint restriction on $c_{\ne0}(R)$. Its original
complete source decomposition is in
[E.15, E.19--22](R133-supplement-weighted-Q-endpoint-invariance-and-small-analytic-cap-ball.md)
and
[F.4--7](R133-supplement-actual-zero-width-full-periodic-cap-Phi-and-finite-Sobolev-tame.md).
More explicitly:

- the complete known ordinary, inner and outer source norm is
  less than $3.23\,10^{-7}$;
- the same complete linear $Q$ plus true nonlinear outer
  difference is at most $0.879\|x\|$, on the original endpoint
  invariant set;
- the exact Gauss remainder has norm at most $13\|x\|^2$ and
  its full unclosed reference Green gain is below 16, giving
  $208\|x\|^2$;
- the added complete $B$-mean right lift is below $2^{-80}$.

The two curvature means and the complete changing exterior
response remain in those estimates. In particular the linear
outer bound uses the actual endpoint of this same $x$, whose
norm is bounded by $t$. It is not replaced by an unrelated
reference exterior. These facts give, for the actual fixed point,

$$
 t<3.23\,10^{-7}+0.879t+208t^2+2^{-80}.                \tag{CG.4}
$$

This is the original estimate before inserting the prescribed
radius for $\|x\|$. Since $t^2\le\rho t$, it follows that

$$
 t<\frac{3.23\,10^{-7}+2^{-80}}{1-0.879-208\rho}
   =\frac{3.23\,10^{-7}+2^{-80}}{0.120376}
   <2.684\,10^{-6}=:t_*.                              \tag{CG.5}
$$

No new existence argument or new self-map claim is used: (CG.5)
is an a priori consequence for the original unique solution.
Its outer input domain, uniqueness, height span and both mean
equations are unchanged. The harmless $B$-mean allowance has
been retained even in the reflection class where that mean is
zero by parity.

## 2. Mean-separated real inverse-angle comparison

All norms below use the complete signed set $4\mathbb Z$.
Let

$$
 \widehat m=1/\langle\widehat C\rangle_\theta,
 \quad m_*=1/\langle C_*\rangle_\theta,
 \quad\mu=\langle c\rangle_\theta,
 \quad\widehat j=\widehat m\widehat C.                \tag{CG.6}
$$

The known M centre has the complete joint bound
$\|\widehat j\|_{\mathscr A_0}<2$. Its constant Fourier
coefficient is exactly 1 at every radius. Therefore, in the
same joint norm,

$$
             \|\widehat j-1\|_{\mathscr A_0}<1.        \tag{CG.7}
$$

This is removal of an exactly known coefficient of the same
Wiener sum. It is not subtraction of unrelated norm upper
bounds.

The two physical-to-moving angle lifts have the exact
changing-mean difference from RB.11,

$$
 \Phi_*-\widehat\Phi
       =m_*I_\theta(c-\widehat m\mu\widehat C)
       =m_*I_\theta(P_{\ne0}c-\mu(\widehat j-1)).       \tag{CG.8}
$$

The complete mean is precisely the second term of this
identity. With $t_c=\|c\|_{\mathscr A_0}$, (CG.7) gives

$$
 \|P_{\ne0}c-\mu(\widehat j-1)\|_{\mathscr A_0}
 \le\|P_{\ne0}c\|_{\mathscr A_0}
                   +\|\mu\|_\infty=t_c.              \tag{CG.9}
$$

The equality on the right is exactly the zero-mode/nonzero-mode
decomposition of this complete joint Wiener norm. Multiplication
by a radial scalar respects this estimate.

The actual mean satisfies $|m_*|<7$ by M and RB.9. The
zero-mean primitive has norm $1/4$ on the full $4\mathbb Z$
Wiener space. The known inverse angle has derivative below
$33/32$, by RB.7 at $\delta=0$. Consequently the actual real
inverse lifts satisfy

$$
 \|\Theta_*-\widehat\Theta\|_\infty
 \le\frac{33}{32}\|\Phi_*-\widehat\Phi\|_\infty
 <\frac{231}{128}t_c<2t_c.                            \tag{CG.10}
$$

Reflection fixes the same phase in both lifts. No unknown
complex-angle evaluation or same-order composition-operator
estimate is needed.

## 3. Only the known physical readout is differentiated

Write

$$
 F_0(\theta)=(\widehat B/\widehat C,1/\widehat C)
             =\widehat U(\widehat\Phi(\theta)).         \tag{CG.11}
$$

The complete repaired table in
[C.4--8](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md)
and RB.4--7 give

$$
 |\widehat m|<6,\quad
 \|\widehat u_\phi\|_\infty<1/12,\quad
 \|[(\widehat v-\widehat m)/\widehat m]_\phi\|_\infty<1/16,
 \quad\widehat\Phi_\theta<32/31.                      \tag{CG.12}
$$

Since $\widehat m$ depends only on radius, the two global
moving derivative suprema sum to less than
$1/12+6/16=11/24$. The chain rule, applied only to this
known reference, gives

$$
 \|(F_{0,1})_\theta\|_\infty+
 \|(F_{0,2})_\theta\|_\infty
             <\frac{32}{31}\frac{11}{24}
              =\frac{44}{93}<\frac12.                \tag{CG.13}
$$

This is a bound on the sum of two global suprema. It is
therefore valid for comparing both components of $F_0$ at
the two variable angle maps without an additional norm
equivalence factor.

At the same physical angle the actual reciprocal differences
are exactly

$$
 \frac{B_*}{C_*}-\frac{\widehat B}{\widehat C}
  =\frac{\widehat v(b-\widehat u c)}{1+\widehat v c},
 \qquad
 \frac1{C_*}-\frac1{\widehat C}
  =-\frac{\widehat v^{\,2}c}{1+\widehat v c}.           \tag{CG.14}
$$

The already paid reference bounds are
$|\widehat v|<5.953141388<5.954=:V$ and
$|\widehat u|<1/50=:U$. On the original radius $\rho$,
the denominator is bounded away from zero by $1-V\rho$.
Two new rational comparisons give

$$
 \frac{V}{1-V\rho}<6,\qquad
 \frac{V(U+V)}{1-V\rho}<36.                           \tag{CG.15}
$$

Thus, with $t_b=\|b\|_{\mathscr A_0}$,

$$
 \|F_*-F_0\|_{C^0,\mathrm{pair}}
       <6t_b+36t_c.                                  \tag{CG.16}
$$

These are bounds for complete functions, including their means;
no finite physical Fourier support is assigned to the cap.

## 4. Full moving comparison and the original raw candidate

The same exact nonlinear decomposition used in CW.9 is

$$
 U_*-\widehat U=(F_*-F_0)\circ\Theta_*
                     +F_0\circ\Theta_*-F_0\circ\widehat\Theta.
                                                               \tag{CG.17}
$$

For the first term real composition preserves suprema. For
the second term use only (CG.10) and (CG.13). Hence

$$
 \|u_*-\widehat u\|_\infty+
 \|v_*-\widehat v\|_\infty
 <6t_b+36t_c+\tfrac12(2t_c)
 \le37(t_b+t_c)=37t.                                 \tag{CG.18}
$$

The complete centre repair has pair $A_{1/32}$ norm less than
$4.832\,10^{-18}<5\,10^{-18}$. From (CG.5) and (CG.18),

$$
 \|u_*-u_{\rm raw}\|_\infty+
 \|v_*-v_{\rm raw}\|_\infty
 <37(2.684\,10^{-6})+5\,10^{-18}
 <9.9309\,10^{-5}<10^{-4}.                             \tag{CG.19}
$$

This proves (CG.1). The physical-to-moving conversion, the
changing true mean, every high mode and the nonzero repair
have all been paid.

## 5. Exact consequence for the final geometry entry

The cap's intrinsic $\nu$ bump is zero, and all its remaining
intrinsic data are the same original data. Accordingly every
admitted cap above satisfies the cap part of G.16 in
[the finite-Sobolev final geometry entry](R133-supplement-exact-finite-Sobolev-exterior-and-final-geometry-entry.md).

More precisely, suppose a genuine core on $[0,9/10]$ has the
original fixed $\eta_0$, has $|\nu-\nu_0|\le10^{-5}$ and
the required complete componentwise state error at most
$10^{-4}$, and supplies admissible M/selected-tail inputs.
If its full physical $B,C$ values, means and normalized angle
match this actual cap, the joined complete core-plus-cap state
automatically has the G.16 $C^0$ bound on $[0,25/8]$.
There is no additional cap state-enclosure hypothesis to pay.

The original input admissibility (including the genuine
physical inner curvature norm), complete matching, true core
inverse, zero nonlinear residual and final waist/closed-family
conditions are still required. This corollary does not turn a
selected finite trial or an unmatched passive core into that
genuine core.

The [companion rational reader](../scripts/fourfold_codazzi_actual_cap_geometry_ball_saved_bounds.py)
contains seven new exact comparisons, all evaluated once and
all passed. No old iteration, Green integral, coefficient
producer, WMR target or geometry calculation was repeated.
