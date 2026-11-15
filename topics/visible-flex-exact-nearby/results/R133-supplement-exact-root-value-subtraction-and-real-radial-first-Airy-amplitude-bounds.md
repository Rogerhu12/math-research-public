# Exact root-value subtraction and real-radial bounds for the first Airy correction

**Status: proved analytic identities and a conditional complete scalar-majorant contract.**
The bounds below concern the same root-normalized first correction, the same repaired explicit family, and the same fixed original $\eta_0$ as the [ordered old-radial transport](R133-supplement-ordered-old-radial-transport-and-strict-exterior-first-correction-derivatives.md). They do not introduce a different trial or reset an amplitude at an artificial cut. Current numerical use is restricted to the real parameter disk $|\delta|\le 10^{-8}$ covered by the complete piecewise certificates. This note does not assert that the new quantitative path and source bounds have already been evaluated.

The purpose is to remove the exact root value of the normalized second amplitude before estimating the exterior equations. A nonzero root value is an actual part of the correction; estimating its two cancelling appearances separately creates an unnecessary $1/|\rho|$ term. All nonzero Fourier modes, the root mean, physical seams, and old-circle source terms remain present.

## B.1. Exact normalization and the two principal quadratic forms

Use
$$
 \rho=r_*-r,\quad D=\partial_r-d\partial_\phi
       =-\partial_\rho-d\partial_\phi,\quad
 x=X_\phi,\quad y=T_\phi,\quad
 Q=aA^{-1/3},\quad T=-\rho A^{2/3}.
\tag{B.1}
$$
Here $a=a(\rho,\delta)$ is a radial scalar. The exact fold relations are
$$
 DT=Qx,\qquad DX=-QTy,\qquad \eta^2K=Q^2T.
$$
The leading reconstruction matrix is
$$
 M_0=
 \begin{pmatrix}a_0&Tb_0\\b_0&a_0\end{pmatrix},\quad
 a_0=G(x^2-Ty^2),\quad b_0=-2i\epsilon Gxy,
 \qquad \epsilon\in\{1,-1\}.
$$
Its determinant is $G^2(x^2+Ty^2)^2$. In particular the principal scalar coefficient is
$$
 \mu=Q^2(x^2+Ty^2),
\tag{B.2}
$$
whereas $a_0$ uses $x^2-Ty^2$. These two expressions are not interchanged.

Write
$$
 w_1=M_0Z,\qquad Z=\binom{\mathcal A}{\mathcal B},\qquad
 \binom{f_b}{f_a}=M_0^{-1}\binom{F_b}{F_a}.
$$
The canonical equations and the actual root normalization are
$$
 2\mathcal A_T-2i\epsilon T\mathcal B_X=f_a,\qquad
 2T\mathcal B_T+\mathcal B-2i\epsilon T\mathcal A_X=f_b,
\tag{B.3}
$$
$$
 \mathcal A(0,X)=0,\qquad
 \mathcal B(0,X)=f_b(0,X).
$$
These are the equations of the accepted correction, including its full mean. The forcing order in the vector $(f_a,f_b)$ is the reverse of the order $(F_b,F_a)$.

## B.2. Subtract the exact root value before taking norms

Define the exact function, for the same parameter value throughout,
$$
 b_*(X)=f_b(0,X),\qquad
 \mathcal B=\widetilde{\mathcal B}+b_*(X).
$$
Then
$$
 g_a=f_a+2i\epsilon T\,b_*'(X),\qquad
 g_b=f_b-b_*(X)
\tag{B.4}
$$
give
$$
 2\mathcal A_T-2i\epsilon T\widetilde{\mathcal B}_X=g_a,\qquad
 2T\widetilde{\mathcal B}_T+\widetilde{\mathcal B}
       -2i\epsilon T\mathcal A_X=g_b.
\tag{B.5}
$$
Both subtracted amplitudes vanish at the root. In the original analytic root piece, $g_b(0,X)=0$, so $g_b/T$ has a removable singularity. On the other original pieces this quotient is simply evaluated at nonzero $T$; no continuation through a physical seam is assumed.

The exact subtraction uses the actual $b_*$, not the midpoint of an interval enclosure. Complete stored Fourier enclosures may bound this same function and all its derivatives. The [actual finite Taylor computation](R133-supplement-actual-complete-old-radial-first-Airy-Taylor-bounds.md) already contains the natural normalized-forcing degree-zero stage from which $b_*$ can be consumed. Re-evaluating the old target or that finite stage is unnecessary.

The same-parameter branch identity has $b_{*,-}=b_{*,+}$ and $\mathcal A_-=-\mathcal A_+$, $\mathcal B_-=\mathcal B_+$ under the original conventions. It is algebraic and does not conjugate a complex parameter.

## B.3. Cancellation in the original radial equations

Let $Z_*=(0,b_*(X))^t$. In the notation of E.9,
$$
 Z_\rho=CZ_\phi+MZ-Nf,\qquad f=(f_a,f_b)^t,
$$
$$
 C=-dI-i\epsilon Q\begin{pmatrix}0&T\\1&0\end{pmatrix},
$$
$$
 M=\frac Q2\begin{pmatrix}0&-i\epsilon y\\0&x/T\end{pmatrix},
 \qquad
 N=\frac Q2\begin{pmatrix}x&-i\epsilon y\\-i\epsilon y&x/T\end{pmatrix}.
$$
The two identities
$$
 MZ_*=N\binom{0}{b_*},\qquad
 CZ_{*,\phi}-Z_{*,\rho}=-N\binom{2i\epsilon T b_*'}{0}
\tag{B.6}
$$
show that $\widetilde Z=(\mathcal A,\widetilde{\mathcal B})^t$ satisfies the identical ordered equation with $f$ replaced by $(g_a,g_b)^t$. Thus the exact root value contributes no term of the form $b_*/T$ to this equation. The remaining first- and second-radial derivative formulas are still the full ordered E.10--E.12 formulas; no matrix is commuted past another.

## B.4. The physical radial paths keep the original seams

On either real half-axis choose $t_\rho$ with $t_\rho^2=-\rho$, consistently on that half-axis, and put
$$
 \tau=t_\rho A^{1/3},\qquad \tau^2=T,\qquad Q\tau=a\,t_\rho.
$$
The last identity is decisive: its right side is radial and has no angular derivative. Define
$$
 D_\sigma=\partial_r-(d+\sigma i\epsilon a t_\rho)\partial_\phi,
 \qquad C_\sigma=Q(x-\sigma i\epsilon\tau y),\qquad \sigma=\pm1.
$$
Direct substitution gives
$$
 D_\sigma=C_\sigma(\partial_T-\sigma i\epsilon\tau\partial_X).
\tag{B.7}
$$
For
$$
 V_\sigma=\mathcal A+\sigma\tau\widetilde{\mathcal B},
$$
equation B.5 yields
$$
 D_\sigma V_\sigma
   =C_\sigma\left(\frac{g_a}{2}+
                      \frac{\sigma g_b}{2\tau}\right).
\tag{B.8}
$$
The terms $\sigma\widetilde{\mathcal B}/(2\tau)$ cancel exactly. If
$$
 L_b=g_b/T,
$$
the last right side is $C_\sigma(g_a+\sigma\tau L_b)/2$ and is integrable at the root.

For a fixed real endpoint $\rho$, use the original coordinate $s$ as the path parameter and solve
$$
 \frac{d}{ds}H_\sigma(s;\rho,\phi)
    =d(s,H_\sigma)+\sigma i\epsilon a(s)t_s,\qquad
 H_\sigma(\rho;\rho,\phi)=\phi.
\tag{B.9}
$$
All scalar coefficients here are written as functions of $\rho$ rather than $r$. The radius $s$ is real throughout. Therefore a path crosses a physical seam at its actual real radius. It never uses a complex radial extension of one cubic as a replacement for a different physical piece.

The corresponding integral is
$$
 V_\sigma(\rho,\phi)
   =-\frac12\int_0^\rho
       C_\sigma(s,H_\sigma)
          \bigl(g_a(s,H_\sigma)+\sigma\tau(s,H_\sigma)L_b(s,H_\sigma)\bigr)\,ds.
\tag{B.10}
$$
The sign follows from $D_\sigma=-(\partial_\rho+
(d+\sigma i\epsilon at_\rho)\partial_\phi)$. It is immaterial only after this exact formula has been established.

## B.5. Explicit sufficient angular-domain gates

Fix $0<R$ and two angular widths $0<\sigma<\Sigma$. Suppose the original coefficients and the functions evaluated in B.10 are holomorphic on $|\operatorname{Im}\phi|<\Sigma$, for every real original radius with $|\rho|\le R$, and that the closed-strip bounds
$$
 |a|\le a_{\max},\qquad |d|\le D_0,\qquad |d_\phi|\le D_1
$$
hold there. A sufficient path-containment gate is
$$
 D_0R+\frac23a_{\max}R^{3/2}<\Sigma-\sigma.
\tag{B.11}
$$
Indeed this bounds the absolute displacement of either terminal-value path in B.9, on either side of the root. Existence and uniqueness follow piecewise and then across the finitely many original seams, using the angular Lipschitz bound. A consumer may use a sharper already proved path-domain estimate, but must identify its exact widths.

For the two paths with the same endpoint, Gronwall gives, with $\ell=|\rho|$ and $0\le u\le\ell$,
$$
 |H_+(u)-H_-(u)|
 \le\frac43a_{\max}e^{D_1\ell}
                 \bigl(\ell^{3/2}-u^{3/2}\bigr).
\tag{B.12}
$$
Here $u$ denotes absolute radial distance on the chosen half-axis. The estimate uses that the difference of the two added ray velocities is radial. No angular derivative of $a t_\rho$ is charged or omitted.

The strip is convex. Consequently the same width contains the straight angular segment between the two paths, which justifies the angular mean-value estimate used below. This is a segment in the angle at a fixed real radius, not a segment in complex radius.

## B.6. A complete divided-forcing bound with the actual seam jumps

A fixed-$X$ lift in the original radius satisfies
$$
 \frac{d\chi}{d\rho}
   =-\frac{X_\rho}{x}
   =d-\frac{QTy}{x}.
\tag{B.13}
$$
Assume $|x|\ge x_->0$ on its complete angular domain and pay its path-containment gate. One simple sufficient gate is
$$
 R\left(D_0+
 \frac{a_{\max}A_+^{1/3}Y_2R^3}{x_-}\right)<\Sigma-\sigma,
\tag{B.14}
$$
when $|A|\le A_+$ and $|y|\le Y_2|\rho|^2$. This displayed gate is intentionally a whole-interval supremum; direct integration can reduce it.

At the root $X(0,\chi)=\chi$. Thus the root value reached by this lift is exactly the same $b_*(X)$ that occurs in B.4. On the open physical pieces,
$$
 \frac{d}{d\rho}f_b(\rho,\chi(\rho))
  =f_{b,\rho}+
       \left(d-\frac{QTy}{x}\right)f_{b,\phi}.
\tag{B.15}
$$
Integrating and adding every physical forcing jump gives the valid bound
$$
 |g_b(\rho,\phi)|
 \le \int_{\text{root to }\rho}
       \left(|f_{b,\rho}|+
        \left|d-\frac{QTy}{x}\right||f_{b,\phi}|\right)|ds|
       +\sum_{r_i\ {\rm crossed}}\|[f_b]_{r_i}\|_{\Sigma}.
\tag{B.16}
$$
Therefore division by the genuine lower bound
$$
 |T|\ge|\rho|A_-^{2/3}
$$
produces a complete bound for $L_b$. A public consumer must include the root interval width in every distance, use the accepted inner Taylor data for its near-root start, and then integrate only the previously unconsumed scalar majorants on the actual old common grid.

The original $M_0$ is continuous at each physical seam, so
$$
 [f_b]
   =(M_0^{-1})_{11}[F_b]+(M_0^{-1})_{12}[F_a].
\tag{B.17}
$$
The original complete seam native retains both normalized degree-zero forcing jumps. Its nonzero values must be paid in B.16. They are not inferred from the jump of a finite fit and are not set to zero by the root subtraction. A Cauchy loss in angle, from a separately paid wider strip, may bound $(L_b)_\phi$. It requires no new radial derivative or false analytic continuation through a seam.

## B.7. Separate the even and odd two-ray integrands

Define, at one and the same physical point,
$$
 \mathcal E=Qx\,g_a-i\epsilon QTy\,L_b,\qquad
 \mathcal O=a t_\rho(xL_b-i\epsilon y g_a).
\tag{B.18}
$$
The integrand in B.10 is exactly $\mathcal E+\sigma\mathcal O$. Hence
$$
 \mathcal A=-\frac14\int_0^\rho
  \{\mathcal E(H_+)+\mathcal E(H_-)
              +\mathcal O(H_+)-\mathcal O(H_-)\}\,ds,
$$
$$
 \widetilde{\mathcal B}
  =-\frac{1}{4\tau(\rho,\phi)}\int_0^\rho
  \{\mathcal E(H_+)-\mathcal E(H_-)
              +\mathcal O(H_+)+\mathcal O(H_-)\}\,ds.
\tag{B.19}
$$
The two-ray cancellation is performed before estimating either amplitude. In particular the large root constant is absent from both integrands.

## B.8. Complete uniform coefficients for the explicit amplitude bounds

On the paid path strip, suppose
$$
 A_-\le|A|\le A_+,\quad |x|\le X_0,\quad
 |x_\phi|\le C_2|\rho|,\quad
 |A_\phi|\le c_1|\rho|,
$$
$$
 |y|\le Y_2|\rho|^2,\qquad
 |y_\phi|\le Y_{\phi,2}|\rho|^2.
$$
These bounds are supplied by the original fold and angular variational estimates. For example, if $|A_{\phi\phi}|\le c_2|\rho|$, one may take
$$
 Y_2=\frac23A_-^{-1/3}c_1,\qquad
 Y_{\phi,2}=\frac23A_-^{-1/3}c_2+
                      \frac29R A_-^{-4/3}c_1^2.
\tag{B.20}
$$
Set
$$
 U_0=a_{\max}A_-^{-1/3}X_0,\qquad
 U_1=a_{\max}A_-^{-1/3}
                  \left(C_2+\frac{X_0c_1}{3A_-}\right),
$$
$$
 J_3=a_{\max}A_+^{1/3}Y_2,\quad
 J_{\phi,3}=a_{\max}A_+^{1/3}Y_{\phi,2},\quad
 J_{\phi,4}=\frac{a_{\max}}3A_-^{-2/3}c_1Y_2.
\tag{B.21}
$$
Then
$$
 |Qx|\le U_0,\quad |(Qx)_\phi|\le U_1|\rho|,
$$
$$
 |QTy|\le J_3|\rho|^3,\quad
 |(QTy)_\phi|\le J_{\phi,3}|\rho|^3+
                             J_{\phi,4}|\rho|^4.
$$
The identities $a_\phi=0$ and $QTy=-a\rho A^{1/3}y$ justify these formulas. All powers used in denominators need genuine positive lower bounds, with outward interval rounding.

Let
$$
 |g_a|\le G_a,\quad |g_{a,\phi}|\le G_{a,1},\qquad
 |L_b|\le L_b^0,\quad |L_{b,\phi}|\le L_b^1.
$$
These four constants must hold on the entire paths in B.10. Bounds only on the endpoint strip are insufficient.

## B.9. Explicit real-radial two-ray amplitude inequalities

For $0<\ell=|\rho|\le R$, equations B.12 and B.19 imply
$$
\begin{aligned}
 |\mathcal A|\le{}&
 \frac{U_0G_a}{2}\ell+\frac{J_3L_b^0}{8}\ell^4\\
 &+a_{\max}^2e^{D_1\ell}
 \left(
  \frac{C_2L_b^0}{20}\ell^4+
  \frac{X_0L_b^1}{9}\ell^3+
  \frac{Y_{\phi,2}G_a+Y_2G_{a,1}}{35}\ell^5
 \right).
\end{aligned}
\tag{B.22}
$$
Similarly,
$$
\begin{aligned}
 |\widetilde{\mathcal B}|\le{}&
 \frac{a_{\max}}{A_-^{1/3}}
   \left(\frac{X_0L_b^0}{3}\ell+
                   \frac{Y_2G_a}{7}\ell^3\right)\\
 &+\frac{a_{\max}e^{D_1\ell}}{A_-^{1/3}}
 \left(
   \frac{U_0G_{a,1}}5\ell^2+
   \frac{U_1G_a}{14}\ell^3+
   \frac{J_{\phi,3}L_b^0+J_3L_b^1}{44}\ell^5+
   \frac{J_{\phi,4}L_b^0}{65}\ell^6
 \right).
\end{aligned}
\tag{B.23}
$$
To verify every coefficient, use
$$
 \int_0^\ell u^p(\ell^{3/2}-u^{3/2})\,du
 =\frac{3\ell^{p+5/2}}{2(p+1)(p+5/2)}.
\tag{B.24}
$$
In B.22 the three difference integrals have $p=3/2,1/2,5/2$; in B.23 they have $p=0,1,3,4$, followed by division by $|\tau(\rho,\phi)|\ge\ell^{1/2}A_-^{1/3}$. The direct odd integrals have $p=1/2,5/2$. This proves the factors $1/9$ and $1/5$ on actual real-radial paths, together with the additional nonradial terms required by the physical chart.

No straight complex radial path or unsupported canonical rectangle is used in B.22--B.23.

## B.10. Recover the same original correction and its derivatives

The actual amplitude remains
$$
 w_1=M_0\left\{\binom{\mathcal A}{\widetilde{\mathcal B}}
                    +\binom{0}{b_*(X)}\right\}.
\tag{B.25}
$$
For example,
$$
 \partial_\rho b_*(X)=b_*'(X)X_\rho,\qquad
 \partial_\rho^2 b_*(X)
   =b_*''(X)X_\rho^2+b_*'(X)X_{\rho\rho}.
$$
Thus the large angular mean of $b_*$ does not appear when differentiating the composition itself. It still multiplies the true derivatives of $M_0$ in B.25, as required. Those actual contributions cannot be discarded.

Use B.6 and the full ordered exterior derivative identities to differentiate the subtracted amplitude, then use B.25 with all product terms. At an original physical seam, $M_0$, $M_{0,\rho}$, $X$, and $X_\rho$ retain their original common traces. The subtracted term is therefore $C^1$ there. The true first-correction jumps, and consequently the actual reconstructed state jumps, are unchanged. There is no new interface source at the inner/exterior integral split.

These common traces are supplied by M.4--M.7 and M.12 of the [original piecewise real-root transport](R133-supplement-piecewise-real-root-fold-and-closed-forced-Airy-transport.md). The repaired background and all its angular derivatives have common values at each original seam; this does not assert continuity of its radial derivatives. The continuous characteristic velocities give common traces for the true flows and their first radial derivatives. At a strict seam, the fold formulas therefore give common traces for $X,T$ and their first radial derivatives. M.12 gives the same statement for $G,a_0,b_0$, hence for $M_0$ and $M_{0,\rho}$. The original nonzero background radial jumps and the forcing jumps in M.16--M.17 remain exactly present.

## B.11. What a further consumer must establish

A correct numerical use must separately verify:

1. The exact same root, repaired background, direction, fixed $\eta_0$, parameter set, forcing order and branch identities.
2. The actual widths and the real-radial path gates, including the fixed-$X$ lift used for $L_b$.
3. The exact complete root Fourier coefficient stage for $b_*$ and the necessary composition strip.
4. The complete inner contribution, every original open-piece derivative bound, and all physical forcing jumps in B.16.
5. The four full-path constants in B.22--B.23, followed by complete ordered derivative reconstruction.
6. The old-circle $I/J$ words, independent even mean, true unnormalized local numerator $\mu L_0w_1$, complete Fourier outputs, and actual radial source integrals.

Only the first five items are the amplitude contract proved here. The last item uses the already stated full-source interfaces and still requires its actual scalar consumer. These identities alone do not provide a full negative-boundary inverse, the low/high Schur closure, a numerical strong-return cutoff at $97$, or a genuine solution of the original nonlinear equations.
