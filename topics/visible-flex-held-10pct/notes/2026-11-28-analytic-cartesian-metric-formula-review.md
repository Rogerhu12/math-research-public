# Independent formula review of the new common-Cartesian metric verifier

## Scope and outcome

This is a read-only review of the sources bound in the adjacent JSON. It did not rerun the angular oracle, continuous metric scan, original BVP, or an old bridge certificate. No source belonging to the active verifier was edited. The reviewed algebra and enclosure argument match the same new Cartesian map: its final shared radial defining jets, full true-core lift, actual center two-jet correction, and shared phase chart. I found no algebraic error in the examined formulas. A numerical certificate still requires the actual complete run and its coverage record.

## Complete angular derivatives

Write \(e_0=E_0\), \(e_2=E_{ss}(0)\),

\[
\theta_0(\psi)=\psi-e_0\sin(3\psi)/3,\quad
\rho=1-e_0\cos(3\psi),\quad
\rho'=3e_0\sin(3\psi),\quad
\rho''=9e_0\cos(3\psi).
\]

For the true material curve \(\Gamma\), the first three derivatives of its composition are

\[
\rho\Gamma',\qquad
\rho^2\Gamma''+\rho'\Gamma',\qquad
\rho^3\Gamma'''+3\rho\rho'\Gamma''+\rho''\Gamma'.
\]

The circle has third derivative \((\rho''-\rho^3)e_\theta-3\rho\rho'e_r\). These are precisely the table formulas. The center target has radial second jet \(b\Gamma'\), where \(b=-e_2\sin(3\psi)/3\). Its third angular derivative is

\[
b'''\Gamma'+(3b''\rho+3b'\rho'+b\rho'')\Gamma''
 +(3b'\rho^2+3b\rho\rho')\Gamma'''+b\rho^3\Gamma''''.
\]

The coefficients and signs in the third angular center derivative agree. The full fourth material derivative comes from the original true-integral core oracle, including curvature derivatives; it is not estimated by finite differences.

The planar projection reexpression follows the exact identity

\[
e^{i\psi}\{R\cos(m\psi)+iT\sin(m\psi)\}
 =\tfrac12(R+T)e^{i(1+m)\psi}
  +\tfrac12(R-T)e^{i(1-m)\psi}.
\]

The literal original projection coefficients and the physical factor \(q\) are retained. Negative planar frequencies receive their signed cubic power. The complete angular lift subtracts both the circle and this original projection from \(\Gamma\circ\theta_0\). The center differences subtract the final Cartesian radial jets and the full radial lift, so they refer to the actual map rather than the intermediate source mean.

## Map identity and periodic endpoints

ActualR53CartesianPrefix sets the full radial lift on the final Cartesian knot vector; PhaseAngleChart uses that identical knot vector. Consequently the field, lift and chart in HermiteIntervals use the same original defining knots. They are not reconstructed on an unrelated grid. The center width is added separately to the interval partition.

The finite planar frequencies equal \(1\pmod 3\), the height frequencies equal \(0\pmod3\), and the true R53 curve is normalized to exact covariance under \(2\pi/3\) rotation. The original oracle constructs its origin from its full-sector primitive by solving \((R_{2\pi/3}-I)\Gamma(0)=J\). Circle, projection, radial lift and all three center target jets preserve that covariance. The normalized Gram matrix therefore has exact period \(2\pi/3\). This justifies using the first angular node as the right endpoint of the final sector cell; it does not assume numerical endpoint equality.

## Radial and angular error bounds

Let \(X\) be the final Cartesian map and let the shared phase chart be \(\theta=\psi-e(s)\sin(3\psi)/3\). The vectors used by the code are

\[
U=X_s-\frac{\theta_s}{\rho}X_\psi,\qquad
V=\frac{X_\psi}{a\rho},\qquad
E=\begin{pmatrix}U\cdot U-1&U\cdot V\\U\cdot V&V\cdot V-1\end{pmatrix}.
\]

These are the material-coordinate orthonormal components for the fixed target \(ds^2+a(s)^2d\theta^2\). Differentiating this complete expression with D2 retains all core, lift, center and chart terms. Radial differentiation requires \(X_{sss}\) and \(e'''\), which are enclosed on each shared polynomial piece. It requires only \(a,a',a''\), despite the target provider also returning a fourth slot.

For a symmetric two-by-two matrix with entries \((A,B,C)\),

\[
\|E\|_{\rm op}=\frac{|A+C|}{2}+\sqrt{\frac{(A-C)^2}{4}+B^2}.
\]

The implementation bounds this expression outward from the three interval components. If \(p,d,d_2\) bound the matrix value, first radial derivative and second radial derivative at the prescribed angular nodes, the uniform endpoint bound on a radial halfwidth \(h\) is \(p+hd+h^2d_2/2\). The radial first derivative is bounded at the center and the second derivative on the whole radial piece.

For an angular cell of width \(w\), Banach-valued linear interpolation has error at most \(w^2\sup\|E_{\psi\psi}\|_{\rm op}/8\). Convexity of the norm bounds its endpoint interpolant by the uniform nodal radial bound. Thus the implemented sum

\[
p+hd+\tfrac12h^2d_2+\tfrac18w^2d_{\psi\psi}
\]

has the stated meaning. The angular second derivative is computed over the whole angular box and whole radial piece, not sampled at the angular endpoints. The true-\(\pi\) cell widths and angular endpoint uncertainty are enclosed before this argument.

The angular tightening of the small lift/center values uses the left-node Taylor formula with a full-box second derivative. Its first derivative is bounded by the corresponding first-order formula, while the full-box second and third derivatives remain unchanged. This is compatible with the later D2 computation.

## Fixed target and one-sided derivatives

The target adapter retains the exact multistage profile and the true primitive of the frozen bridge phase, including its analytic endpoint extension. The last \(1/1000\) correction has coefficients equal to the unique true-tail two-jet minus the unique true-bridge endpoint two-jet. Interval enclosures of those fixed coefficients do not choose a new metric. The factor \((-L)^j(-1/L)^k\) in its \(k\)th derivative has the correct orientation. The partition includes the prefix subpieces, both bridge phase joins, and the target correction join.

The globally shared objects are \(C^2\) and piecewise \(C^3\); one-sided third derivatives suffice for the piecewise Taylor argument. In particular the point call FrozenTarget.jets(entry,entry) returns zero in its unused third-derivative slot although the true bridge can have a different right third derivative there. This does not affect the present evaluator, which reads only the first three radius slots. A future caller requiring that fourth slot at the join must request a side or enclose both one-sided values. No claim of global \(C^3\) regularity follows from this review.
