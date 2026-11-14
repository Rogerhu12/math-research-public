# Frozen q096: rational bounds for the intended analytic neck

## Actual execution and scope

The reconstructed r2 checker has executed in a V8 isolate: **all 33 exact rational guards passed**. It made no local Node, physical evaluator, ODE, Jacobian, or BVP calls. Its source was read back before execution; only the Node shebang was removed. A preceding attempt rejected the unstripped shebang before executing any mathematical code. This is a new recomputation after environment loss, not a reproduction of the lost old source bytes.

For the **intended exact analytic** neck and tagged terminal bridge of the accepted q096 profile, the guards establish

\[
 3/25<a(s)<9/5,\qquad |a_s(s)|<499/500,\qquad |a_{ss}(s)|\le15/2.
\]

Every nonconstant phase segment has length greater than \(27/10000\); their total length is less than \(4\). In normalized segment coordinate \(u\), the phase is piecewise polynomial of degree at most four and satisfies

\[
 |\phi|<8/5,\quad |\phi_u|<4,\quad |\phi_{uu}|<65,\quad |\phi_{uuu}|<3300.
\]

These are not yet bounds on the implemented NumPy Gauss primitive and its floating evaluation, a stored surface PPoly, or reach. They supply explicit domain and quadrature constants for the separate Gauss64 and mean-homotopy interfaces. They do not replace or delay the same-g M28 refinement.

## Exact inputs and bridge tagging

The complete frozen profile and cut, and six source/port SHA256 values read in the frozen runtime, are retained in the result. Each input float is converted to its exact IEEE-754 rational value. In particular \(V=.31980000000000003\), \(v_p=.8634500737670308\), \(v_d=.98\), \(v_\ell=.985\), \(K=7.5\), \(K_s=6.7475\), and \(K_{\rm sync}=2\).

The port's old default bridge curvature is \(8\). The actual root loader calls neck.tagged_port(port,cfg), which replaces it by the frozen profile's \(K=7.5\). This proof uses the tagged value. The brake uses the constant frozen cut data \(w=.08000000000000027\) and \(w'=-1.866666666666673\), not an uncontrolled interior derivative.

Rational alternating series bound \(\pi\) through Machin's identity. Its branch is checked: \(0<4\arctan(1/5)-\arctan(1/239)<1<\pi/2\), with the last inequality following from \(\arctan1=\int_0^1(1+x^2)^{-1}dx>1/2\). Exact tangent \(1\) then selects \(\pi/4\). Sine and cosine comparisons use Taylor polynomials with rigorous remainders. All pass/fail decisions are rational integer comparisons; decimal displays are truncations for reading.

## Hermite, boost, and descending connector

The initial length \(S\) solves \(k_0S^2+6VS=12\delta\). The guards give \(0.8<S<0.9\). The Bernstein coefficients of the speed derivative are \([k_0,3V/S-k_0,0]\), nonnegative and below \(1\). Thus radius increases from \(1\) to \(1+\delta\).

The boost endpoint angles lie between \(0.32\) and \(1.05\). With \(\epsilon=.08\),

\[
 K_B<0.73/[L_B(1-\epsilon)]<7.5.
\]

The first descending turn has length \(L_1<\pi/[K_s(1-\epsilon)]\). Radius changes by at most arclength, giving an upper radius below \(1.8\) and a lower radius above \(0.12\). The exact guard \(36(1-v_\ell^2)\ge1\) bounds the derivative of arcsine by \(6\), so the sync length is at most \(6(v_\ell-v_d)/[K_{\rm sync}(1-\epsilon)]\). The lower endpoint budget exceeds \(R\) plus this length by more than \(0.2896\). The descending coast therefore has positive length.

## Symmetric loop turns

The flat turn satisfies \(\phi(1-u)=-\phi(u)\) on a symmetric loop turn, so its **ideal** net radial integral is exactly zero. The maximum inward radial loss occurs in the first half and is at most half the arclength. Therefore

\[
 a_{\min}\ge R-\frac{\pi}{2K(1-\epsilon)}>0.12234>0.12.
\]

The other turn is based at \(1.1R\); its upper radius bound is below \(1.8\). Both coasts have positive lengths. The exact ideal cancellation does not by itself certify cancellation of the floating primitive or its accumulated endpoints.

## Terminal bridge and brake

Set

\[
 \phi_t=-\pi/2+\arctan w,\qquad
 \phi_{\rm peak}=-\pi/2+(1-f)\arctan w,\qquad
 \eta_0=(1-f)\frac{w}{1+w^2}.
\]

Because \(\arctan w\ge w/(1+w^2)\), the rigorous cosine estimate gives

\[
 |\sin\phi_{\rm peak}|\le\cos\eta_0
 <0.9974419531365584<0.998.
\]

The bridge is faster than the loop: the value \(0.985\) is not a global speed bound.

The brake length is

\[
 L_{\rm brake}=\frac{2f\arctan(w)(1+w^2)^{3/2}}{-w'}.
\]

Its upper bound uses \(2fw(1+w^2)^2/(-w')\); its lower bound uses \(2fw/[(1+w^2)(-w')]\). Its angular derivative is at most \(-w'/(1+w^2)^{3/2}<-w'<7.5\). The preceding turn has length below \(0.18/[K(1-\epsilon)]\). The remaining coast radius budget exceeds \(0.01523\). All bridge velocities are negative, hence its radius stays between its endpoints and is greater than the cut radius.

## Phase derivative and length constants

For every flat turn,

\[
 |\phi_u|\le\frac{\pi}{1-\epsilon},\qquad
 |\phi_{uu}|\le\frac{3\pi}{2\epsilon(1-\epsilon)},\qquad
 |\phi_{uuu}|\le\frac{6\pi}{\epsilon^2(1-\epsilon)}.
\]

The last two upper bounds are approximately \(64.0271\) and \(3201.352\). The boost is another turn; the quadratic brake satisfies the same looser bounds. The smallest coarse segment lower bound is

\[
 L_{\rm sync}\ge\frac{v_\ell-v_d}{K_{\rm sync}(1-\epsilon)}>0.0027.
\]

All other segment lower bounds and the summed upper bound are checked in the JSON, so the inverse-length factor in the Gauss derivative estimate is explicitly bounded.

## Remaining exact-realization obligations

The provider computes radius by a floating Gauss64 primitive while returning analytic sine/cosine formulas as the next two entries. They cannot be identified as exact first and second derivatives without paying the primitive and floating errors. The missing interfaces are:

1. Actual NumPy nodes and weights versus the exact Gauss64 root and weight boxes.
2. Actual binary segment parameters, trigonometric evaluation, endpoint accumulation, and seams.
3. A declared exact analytic profile with continuous seam jets, or a quantified repair, and its relation to the implemented profile.
4. Whole-domain positive \(a,P,W,D\) boxes for the nonmean field and complete mean homotopy.
5. Actual surface curvature and global reach.

No accepted q096 data or physical metric was modified.
