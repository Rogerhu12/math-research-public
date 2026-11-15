# Complete divided forcing and ordered derivatives after the exact Airy root-value subtraction

**Status: proved analytic consumer contract; the new scalar budgets have not yet been run.**
This note supplements the [exact root-value subtraction](R133-supplement-exact-root-value-subtraction-and-real-radial-first-Airy-amplitude-bounds.md), the [ordered exterior equations](R133-supplement-ordered-old-radial-transport-and-strict-exterior-first-correction-derivatives.md), and the [actual complete old-radial Taylor coefficients](R133-supplement-actual-complete-old-radial-first-Airy-Taylor-bounds.md). It concerns the same repaired explicit family at the fixed original $\eta_0$, with real $|\delta|\le10^{-8}$. In particular no numerical bound below is a full negative-boundary inverse or a solution of the nonlinear problem.

## S.1. Reuse the complete original root coefficients

Let $f_b(\rho,\phi)$ be the normalized forcing of B.3, written in the old coordinates, and let
$$
 f_b(\rho,\phi)=\sum_{j\ge0}\rho^j f_{b,j}(\phi).
\tag{S.1}
$$
The original natural stages named `normalized-forcing-degree-000` through `normalized-forcing-degree-006` contain the complete finite Laurent coefficients of $f_{b,j}$ and $f_{a,j}$ for $0\le j\le6$. Their Fourier multiplier is $4j$, and their stored means are retained. These stages were computed for the complete complex parameter square, so they also enclose the real parameter interval used here. The consumer must verify every original stage receipt against the original complete native and original process; it may not rebuild the old stages or use a fit in their place.

The exact root function is
$$
 b_*(X)=f_{b,0}(X).
\tag{S.2}
$$
Its complete Fourier coefficient array permits new weighted norm evaluations at any specified angular width. It also permits a separate bound for its zeroth Fourier coefficient and its complete nonconstant part. The operation removing that one coefficient is used only to estimate derivatives and products more accurately. It does not remove the independent even-mean equation, change the trial, or set the root mean to zero.

## S.2. A complete inner forcing tail from the existing auxiliary product

Choose $r_c>h_c>0$ and angular widths $\sigma_c<\Sigma_c$ inside the already certified auxiliary old product. Here $h_c$ includes the entire true-root interval width. Suppose the complete normalized forcings satisfy
$$
 |f_a|,|f_b|\le M_a,M_b
 \quad (|\rho|\le r_c,\ |\operatorname{Im}\phi|\le\Sigma_c).
\tag{S.3}
$$
These bounds can be obtained without re-evaluating a target. The saved whole-product leading bounds give $G^{-1}$, the lower bound for $|x^2+Ty^2|$, and upper bounds for $a_0,b_0,T$. Since
$$
 M_0^{-1}
 =\frac1{G^2(x^2+Ty^2)^2}
  \begin{pmatrix}a_0&-Tb_0\\-b_0&a_0\end{pmatrix},
\tag{S.4}
$$
multiplication of the corresponding entry bounds by the saved complete pair $(F_b,F_a)$ bounds $(f_b,f_a)$. The original direct forcing bounds hold on the entire saved old product before restriction to its canonical rectangle. A consumer must check that precise original width and radius, rather than silently transferring a canonical amplitude bound to a larger old product.

Put $z=h_c/r_c<1$. The tail after degree six obeys
$$
 |R_f|\le M_f\frac{z^7}{1-z},\qquad
 |\partial_\rho R_f|
 \le\frac{M_f}{r_c}
 \left(\frac{7z^6}{1-z}+\frac{z^7}{(1-z)^2}\right).
\tag{S.5}
$$
For $q$ angular derivatives, multiply the complete tail bound on $\Sigma_c$ by $q!/(\Sigma_c-\sigma_c)^q$. The saved finite Laurent coefficients are differentiated with their actual multipliers and summed on $\sigma_c$. This gives a complete inner bound for $f_a,f_b,f_{b,\rho},f_{b,\phi}$ and any explicitly paid angular derivative. It is a new scalar consumption of the existing finite coefficients and whole-product certificate, with zero old FFT, target, or finite-stage recomputation.

The auxiliary analytic object is identified with the physical family only in the original root piece. Its use in S.5 is restricted to the physical inner interval contained in that piece. No physical seam is crossed by this Taylor argument.

## S.3. Nested path widths and the real negative side

Use four explicitly checked widths
$$
 \sigma_{\rm value}<\Sigma_{\rm ray}
 <\Sigma_{\rm quotient}<\Sigma_{\rm root}<\Sigma_c.
\tag{S.6}
$$
The complete external $f_a,f_b,f_{a,\rho},f_{b,\rho}$ bounds are already saved on their actual strip $1/32$. The new consumer must keep $\Sigma_{\rm root}<1/32$. Angular Cauchy losses are always taken from that saved width or from an explicitly wider certified domain.

For a real negative-side radius $\rho>0$ and real allowed $\delta$, $t_\rho=i\sqrt{\rho}$ makes the extra ray velocity $\sigma i\epsilon a t_\rho$ real. The coefficients $d$ and $a$ are real on the real circle. On a strip with $|d_\phi|\le D_1$,
$$
 |\operatorname{Im}d(s,z)|
 \le D_1|\operatorname{Im}z|.
$$
Consequently a terminal-value ray starting in width $\sigma_{\rm value}$ remains in width
$$
 \sigma_{\rm value}e^{D_1R}.
\tag{S.7}
$$
A strict comparison with $\Sigma_{\rm ray}$ proves containment. This improvement applies only on the real parameter interval and the negative side. On the positive side the consumer retains the complete optical displacement of B.11, unless another full path theorem is separately supplied.

The fixed-$X$ lift used to estimate $g_b$ is checked independently. B.14 must place a lift starting at width $\Sigma_{\rm quotient}$ inside $\Sigma_{\rm root}$. The complete root inner forcing bounds of S.5 are evaluated on the latter width. Finally, the actual composition $b_*(X)$ is bounded on a width containing $X$ of each required path. Since $X$ is real on the real circle and $|X_\phi|\le E$, the sufficient composition gate is $E\Sigma_{\rm quotient}<\Sigma_{\rm root}$. The consumer may also evaluate the finite root polynomial on a larger explicitly declared width.

A failed new path gate is recorded as such. It neither invalidates the original completed bound nor authorizes use of the new formula outside its domain. Any fallback must retain the original complete bound with an explicit label.

## S.4. Cumulative divided forcing on the actual common grid

For each side, traverse the original exterior cells from the inner boundary outward. Let $L_i$ be a genuine lower bound for $|\rho|$ on a cell and let $H_i$ bound
$$
 |f_{b,\rho}|+
 \left|d-\frac{QTy}{x}\right||f_{b,\phi}|
\tag{S.8}
$$
on the full fixed-$X$ lift domain. Start with the complete inner contribution $h_cH_{\rm inner}$. Add $\Delta r_i H_i$ for each traversed cell and add every actual forcing jump that has been crossed. The jump bound is the complete B.17 bound using the original pair $( [F_b],[F_a])$, not a jump inferred from a fitted scalar approximation.

If $C_i$ is the resulting nonnegative cumulative bound through the outer edge of cell $i$, then throughout that cell
$$
 |L_b|=\left|\frac{g_b}{T}\right|
 \le\frac{C_i}{L_i A_-^{2/3}}.
\tag{S.9}
$$
Including a boundary jump before it is needed only enlarges this bound; omitting or double-claiming cancellation of a jump is forbidden. The consumer records the exact cell identities, root-distance intervals, and the indices of all included seams. No new physical subdivision or artificial boundary condition is introduced.

Take the maximum of these bounds over the already traversed cells and the inner interval. This supplies a valid full-path value bound for B.22--B.23. A Cauchy loss from $\Sigma_{\rm quotient}$ to $\Sigma_{\rm ray}$ bounds $(L_b)_\phi$. This construction uses actual cell lengths and positive lower distances; it does not replace a root interval by its midpoint.

## S.5. Evaluate the entire normalized forcing action before differentiating

Write $\widetilde Z=(\mathcal A,\widetilde{\mathcal B})^t$ and $L=L_b$. With the matrices $C,M,N$ of B.3, perform the exact cancellation
$$
 V:=N\binom{g_a}{TL}
 =\frac Q2
 \binom{xg_a-i\epsilon yTL}{-i\epsilon yg_a+xL}.
\tag{S.10}
$$
Then
$$
 \widetilde Z_\rho=C\widetilde Z_\phi+M\widetilde Z-V.
\tag{S.11}
$$
In particular the second entry of $V$ contains $xL$, with no division by $T$. Taking a bound for $g_b$ and then multiplying separately by $1/T$ needlessly loses this identity.

The exact first derivatives needed for $V$ include
$$
 (g_a)_\rho=(f_a)_\rho+
 2i\epsilon\{T_\rho b_*'(X)+T b_*''(X)X_\rho\},
$$
$$
 L_\rho=
 \frac{(f_b)_\rho-b_*'(X)X_\rho-T_\rho L}{T}.
\tag{S.12}
$$
These are used only on strict exterior cells. Their denominators are the actual lower bounds for $|T|$ on the cell. The same physical-root function occurs in every term. Angular derivatives of S.10 retain all product terms, including $(TL)_\phi$.

The full ordered derivative equations are
$$
\begin{aligned}
 \widetilde Z_{\rho\phi}={}&
 C_\phi\widetilde Z_\phi+C\widetilde Z_{\phi\phi}
 +M_\phi\widetilde Z+M\widetilde Z_\phi-V_\phi,\\
 \widetilde Z_{\rho\rho}={}&
 C_\rho\widetilde Z_\phi+C\widetilde Z_{\rho\phi}
 +M_\rho\widetilde Z+M\widetilde Z_\rho-V_\rho.
\end{aligned}
\tag{S.13}
$$
These are exact differentiated equations, before any entrywise majorants. No coefficient matrices are commuted. They require only the already saved first forcing derivative, the paid leading derivatives, and the new scalar divided-forcing bounds. They do not require new fourth- or fifth-order target derivatives.

## S.6. Reconstruct every original derivative and retain the root mean

Put $Z_*=(0,b_*(X))^t$. The original correction is
$$
 w_1=M_0\widetilde Z+M_0Z_*.
\tag{S.14}
$$
For example,
$$
 (Z_*)_\rho=\binom{0}{b_*'(X)X_\rho},\qquad
 (Z_*)_{\rho\rho}=\binom{0}{b_*''(X)X_\rho^2+b_*'(X)X_{\rho\rho}}.
$$
The full second derivative therefore is
$$
 (w_1)_{\rho\rho}
 =(M_0)_{\rho\rho}(\widetilde Z+Z_*)
 +2(M_0)_\rho(\widetilde Z_\rho+(Z_*)_\rho)
 +M_0(\widetilde Z_{\rho\rho}+(Z_*)_{\rho\rho}).
\tag{S.15}
$$
The mean of $b_*$ still multiplies the true derivatives of $M_0$ in this formula. It is absent only from derivatives of the composition itself. Keeping the mean and nonconstant root part separate is useful for angular derivatives; it is not a projection of the actual correction.

Where needed, use the fold identities directly:
$$
 T_\rho=-Qx-dy,\qquad X_\rho=QTy-dx.
\tag{S.16}
$$
Their angular and radial derivatives are ordinary product rules. For instance
$$
 X_{\rho\rho}=Q_\rho Ty+QT_\rho y+QTy_\rho-d_\rho x-dx_\rho.
$$
The already paid wider-strip leading bounds may be used in these new products; a closed lower-order coefficient is not recomputed by rerunning its former producer.

All actual physical seams and the complete independent mean retain their earlier contracts. The root subtraction is $C^1$ through the original seams by B.10, so the original nonzero correction-source jumps are unchanged. New amplitude and derivative bounds can subsequently be consumed by the complete local numerator and old-circle source consumers. This note does not itself assign them an uncomputed source norm, a positive affine-port norm, or a numerical strong-return cutoff.
