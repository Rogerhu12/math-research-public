# Scope correction: exact polynomial interfaces in the relative-centre bound

This note supplements the frozen
`results/R133-supplement-relative-centre-full-derivative-budget.md`
and its complete numerical DQ report. Their stored bytes are preserved.

The saved floating PPoly coefficients are interpreted as exact dyadic
numbers. The polynomials on adjacent radial pieces need not then have
exactly equal values at their common endpoint. It is therefore not
justified to regard the saved centre itself as an element of
\(\ell^1(4\mathbb Z;C(I))\) without paying its interface jumps.

For the **derivative-only** result, use the following ambient Banach
algebra instead. On the finite subdivision containing all candidate
joins, keep two distinct traces at each interior endpoint and put

\[
 \mathcal A_0=\ell^1\!\left(4\mathbb Z;
          \bigoplus_{i=1}^{N}C([r_{i-1},r_i])\right),\qquad
 \|f\|_{\mathcal A_0}=
 \sum_m\max_i\sup_{r\in[r_{i-1},r_i]}|f_{m,i}(r)|.
\]

The direct sum here has its maximum norm, including both endpoint
traces. The exactly stored centre belongs to this algebra. It obeys
the same convolution inequality, radial multiplier bound, and
Neumann inversion estimate as used in that proof. All 994 native
closed boxes already include these endpoint values separately.

Consequently the entire frozen relative-centre computation, including
the infinite-mode derivative columns, absolute correction norm,
\(L<.763578348\), and conditional residual room
\(>.0001182108262\), remains valid in \(\mathcal A_0\). Its earlier
reference to a continuous-centre \(C(I)\) space should be read with
this explicit ambient-space correction. This is still a derivative
bound, with no claim of a completed residual or a solution.

For any subsequent nonzero-centred existence proof, each exact jump
\(j_i=\widehat U(r_i+)-\widehat U(r_i-)\) must also enter the residual.
The complete Green bound for these point sources is

\[
 H_D\sum_i\|(j_{B,i})_{\ne0}\|_{A^0}
 +(H_Dq_++H_C)\sum_i\|(j_{c,i})_{\ne0}\|_{A^0}
 +\sum_i|(j_{B,i})_0|+\sum_i|(j_{c,i})_0|.
\]

The point-source factors have no \(1/|m|\) gain. They retain both
means. The first two constants follow from the same triangular
\(d=b+q_mc\) Green map: a D jump has norm at most one before the
already paid D-to-C factor, and a direct C jump has norm at most one.
The two backward mean flows each have norm at most one. A complete
consumer will compute every jump from the exact dyadic coefficients
and add this fee to the centre's regular residual.

The resulting fixed point, if its full gates pass, satisfies the
original integral equation \(U=Hh+G_QQ(U)\). Each finite-mode Green
integral is continuous across the interfaces. Its complete Fourier
tails are uniformly summable by the established all-mode Green
bound, so the actual solution is radially continuous. This provides
the required passage from the ambient piecewise algebra to the true
continuous solution; it is not assumed of the finite centre.

This note changes no target, input bytes, numerical bound, or Fourier
scope. It prevents a derivative-only calculation, or an uncorrected
piecewise residual, from being presented as a continuous cap
existence theorem.
