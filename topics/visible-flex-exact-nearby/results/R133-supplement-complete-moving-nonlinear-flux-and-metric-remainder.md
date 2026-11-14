# R133 supplement: complete nonlinear moving flux, true mean, and joint metric remainder

2026-11-14, visible-exact / root. **Proved, with 32 actually executed exact
rational and complete Laurent gates.** The identities below hold for the
whole moving equation, including the primitive and its genuine mean.
They apply to infinite Fourier directions; a finite Laurent field is used
only for an independent exact algebra check.

On the actual current root germ, a full angular analytic ball of radius
\(1/100\) has explicit nonlinear remainder and derivative bounds
\(51000\rho^2\) and \(102000\rho\), respectively, with the stated loss from
strip \(1/1024\) to \(1/2048\). This is not a same-space contraction:
a whole inverse compatible with the source and strip losses remains
necessary. All geometric and global BVP obligations remain.

The current centre is
\[
 \mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}.
\]
The source uses only published complete input bounds, not reconstructed
binary arrays. The true \(\nu\) bump is zero on this root germ; the joint
parameter identities below also cover its actual interior support.

## 1. The exact conservative equation and its full mean

Put \(Q=(u,v)^t\), \(m=\langle v\rangle\), and
\[
 S_K(Q)=u^2+Kv^2,\qquad
 B_K(Q,h)=uh_1+Kvh_2,\qquad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.
\]
Here \(I=\partial_\phi^{-1}P_{\ne0}\) is the full mean-zero fourfold
primitive and \(d=-\beta I S_K(Q)\). The complete nonlinear right side is
\[
 F(Q)=dQ_\phi+\gamma mJQ_\phi
       +\beta\operatorname{diag}(-1,1)Q-\beta S_K(Q)Q.
 \tag{N.1}
\]
All intrinsic coefficients are radial. Since
\(d_\phi=-\beta(S_K(Q)-\langle S_K(Q)\rangle)\), exactly
\[
 \boxed{F(Q)=\partial_\phi\mathcal F(Q)
       +\beta\operatorname{diag}(-1,1)Q
       -\beta\langle S_K(Q)\rangle Q,\quad
 \mathcal F(Q)=-\beta I S_K(Q)\,Q+\gamma mJQ.}
 \tag{N.2}
\]
The nonmean local reaction has canceled against the derivative of the
primitive. Its mean has not canceled. In particular the true mean is
\[
 \langle F_2(Q)\rangle
   =\beta m(1-\langle S_K(Q)\rangle).
 \tag{N.3}
\]
In the actual reflection class \(u\) is odd, \(v\) is even, and the first
mean vanishes. The second mean generally does not.

These identities require no equation for the radial derivative of the
centre. They therefore hold on both sides of every actual saved PPoly
interface and at an approximate centre with nonzero PDE residual.

## 2. The exact complete quadratic and cubic remainder

Let \(h=(h_1,h_2)\), \(z=\langle h_2\rangle\), \(S_h=S_K(h)\) and
\(B=B_K(Q,h)\). Taylor expansion of the actual polynomial equation gives
\[
 F(Q+h)-F(Q)-D_QF(Q)h=\partial_\phi\mathcal A(Q,h)+\mathcal B(Q,h),
 \tag{N.4}
\]
where
\[
 \boxed{\mathcal A=
 -\beta\{I S_h\,Q+2I B\,h+I S_h\,h\}
                      +\gamma zJh,}
 \tag{N.5}
\]
\[
 \boxed{\mathcal B=
 -\beta\{\langle S_h\rangle Q+
                  2\langle B\rangle h+\langle S_h\rangle h\}.}
 \tag{N.6}
\]
The first two primitive terms and \(\gamma zJh\) are quadratic in \(h\);
the remaining primitive term is cubic. The same quadratic/cubic
separation is exact in (N.6). There are no fourth or higher state terms.

For example, before putting the derivatives in conservative form the
complete remainder is
\[
 -\beta\{ I S_h Q_\phi+2I B h_\phi+I S_h h_\phi
                         +S_hQ+2Bh+S_hh\}
                  +\gamma zJh_\phi .
\]
Using \((If)_\phi=f-\langle f\rangle\) gives (N.4)–(N.6), with every
mean term displayed. In particular
\[
 \langle R_2\rangle=
 -\beta\{\langle S_h\rangle m+
                  2\langle B\rangle z+\langle S_h\rangle z\}.
 \tag{N.7}
\]
This is generally nonzero, even with all actual reflection symmetries.

Differentiating (N.5)–(N.6) in a complete direction \(k\) gives the
exact Jacobian difference
\((D_QF(Q+h)-D_QF(Q))k\). Both mean-rank terms occur in its flux:
\(\gamma\{\langle k_2\rangle Jh+\langle h_2\rangle Jk\}\).
The source checks this full identity against the direct differentiated
equation, including nonzero even means in both directions.

## 3. Explicit analytic estimates, with the derivative loss retained

On the actual fourfold circle use
\[
 \|f\|_{A_\sigma}=\sum_{k\in4\mathbb Z}e^{\sigma|k|}|\widehat f_k|,
 \qquad
 \|Q\|_{A_\sigma}=\|u\|_{A_\sigma}+\|v\|_{A_\sigma}.
\]
This is a complete Banach algebra; the vector convention is stated to
avoid an unpaid vector-product constant. For \(0<\varepsilon<\sigma\),
\[
 \|I f\|_{A_\sigma}\le\tfrac14\|f\|_{A_\sigma},\qquad
 \|\partial_\phi f\|_{A_{\sigma-\varepsilon}}
                 \le\varepsilon^{-1}\|f\|_{A_\sigma}.
 \tag{N.8}
\]
The second inequality follows from \(x e^{-x}\le1\); the zero mode
causes no exception. Means have norm at most one.

Set
\[
 b=|\beta|,\quad g=|\gamma|,\quad
 k_0=\max(1,|K|),\quad B_0=\|Q\|_{A_\sigma},\quad
 \rho=\|h\|_{A_\sigma}.
\]
Equations (N.5)–(N.6) give
\[
 \|\mathcal A\|_{A_\sigma}
 \le k_0\{b(3B_0\rho^2/4+\rho^3/4)+g\rho^2\},
\]
\[
 \|\mathcal B\|_{A_\sigma}
 \le bk_0(3B_0\rho^2+\rho^3).
\]
Consequently the full nonlinear state remainder obeys
\[
 \boxed{\|R_Q(h)\|_{A_{\sigma-\varepsilon}}
 \le k_0\left[
 b\left\{\left(\frac{3}{4\varepsilon}+3\right)B_0+
                \left(\frac1{4\varepsilon}+1\right)\rho\right\}
           +\frac g\varepsilon\right]\rho^2.}
 \tag{N.9}
\]
The derivative of the complete remainder satisfies
\[
 \boxed{\|(D_QF(Q+h)-D_QF(Q))k\|_{A_{\sigma-\varepsilon}}
 \le k_0\left[
 b\left\{\left(\frac3{2\varepsilon}+6\right)B_0+
                \left(\frac3{4\varepsilon}+3\right)\rho\right\}
           +\frac{2g}\varepsilon\right]\rho\|k\|_{A_\sigma}.}
 \tag{N.10}
\]
These estimates retain all unknown high frequencies. They do not use the
centre's exact finite band to truncate a nonlinear direction.

The same formulas supply an ordinary source \(\partial_\phi\mathcal A+
\mathcal B\), or separate angular-divergence and ordinary source columns,
according to the actual inverse's paid source space. Calling the former
a weak source does not by itself grant a better inverse estimate.
A bounded operator on a fixed Sobolev space cannot be inserted into
(N.9) while silently removing its one angular derivative or strip loss.

## 4. The actual current root-germ numerical instance

The [current complete complex germ](R133-supplement-current-moving-body-physical-complex-germ.md),
the [positive root proof](R133-supplement-current-moving-positive-root-Riccati-and-full-head.md),
and the [negative forward proof](R133-supplement-current-moving-negative-root-forward-and-mean.md)
give, on the entire real part of the genuine joint root rectangle and
the whole original \(|\eta|\le10^{-9}\),
\[
 \|u\|_{A^0}<13,\qquad\|v\|_{A^0}<9/5,\qquad
 |\beta|,\gamma<9/5,\qquad |K|<61/100000 .
\]
The exact centre has degree 32, so its largest physical frequency is 128.
For \(\sigma=1/1024\), the positive geometric series bound
\(e^{1/8}<8/7\) gives
\[
 \|Q\|_{A_\sigma}
 <(13+9/5)(8/7)=592/35<17.
 \tag{N.11}
\]
This is only a bound for the centre. The allowed correction remains
an arbitrary full \(A_\sigma\) element.

Take \(\varepsilon=1/2048\) and \(0\le\rho\le1/100\).
The exact rational source computes the two outward constants
\[
 C_R=\frac{25394517}{500}<51000,\qquad
 C_D=\frac{50793651}{500}<102000 .
 \tag{N.12}
\]
Thus (N.9)–(N.10) give the numerical conclusion stated at the start.
The centre's complete complex angular gap is
\(-\operatorname{Re}v>.4488872879\) and
\(-\operatorname{Re}m>1.1197077044\). The same full correction ball gives
\[
 -\operatorname{Re}(v+h_2)>.4388,\qquad
 -\operatorname{Re}(m+\langle h_2\rangle)>1.1097 .
 \tag{N.13}
\]
The chart survives the ball; this is independent of whether the
correction has a finite Fourier expansion.

There is also a direct, limited consumption of the paid positive-root
inverse. The final strip embeds into \(H^{1/3}\) with norm below 10:
\[
 \langle k\rangle^{1/3}e^{-|k|/2048}
 \le 1+(2048/3)^{1/3}<10.
\]
On its actual interval of length \(9\cdot10^{-6}\), the full source
(N.9) therefore has \(L^2_rH^{1/3}_\phi\) norm below \(1530\rho^2\).
With zero port data, the already paid positive-root inverse gives
\[
 \|G_{\rm root}R_Q(h)\|_{L^2_rL^2_\phi}<\rho^2/5,\qquad
 \|\operatorname{Tr}G_{\rm root}R_Q(h)\|<62\rho^2 .
 \tag{N.14}
\]
These are estimates for one application of that complete local inverse.
Its output norm is not \(L^\infty_r A_\sigma\), so (N.14) does not close
a same-norm nonlinear iteration or grant a nonlinear root solution.

No full-body coefficient envelope is inferred from this root instance.
The compact \(\nu\) bump vanishes identically here, so every explicit
parameter term in the next section is exactly zero on this germ.

## 5. The actual joint ν change without finite differences

Keep the true radius and \(\beta=a'/a\) fixed, and let
\(E_\nu=E e^{\nu w}\). At the current \(\nu\) put
\(T=\beta/(2E_\nu)\), \(p=\gamma K\). For a scalar increment \(d\nu\),
the exact target identities are
\[
 K_{\nu+d\nu}=e^{-d\nu w}(K+d\nu\,T w'),\qquad
 \gamma_{\nu+d\nu}=\gamma e^{d\nu w/2},
\]
\[
 p_{\nu+d\nu}=e^{-d\nu w/2}(p+d\nu\,\gamma T w').
 \tag{N.15}
\]
They retain the \(w'\) term and the mixed product \(\gamma K\).
The equation (N.1) is affine in the three coefficient coordinates
\(K,\gamma,p\) when these are treated as independent variables.
This affine reorganization does not replace \(p=\gamma K\).

For actual coefficient differences \(\Delta K,\Delta\gamma,\Delta p\),
the entire right-side difference at fixed \(Q\) is
\[
 \Delta F(Q)=
 \partial_\phi\left\{-\beta\Delta K I(v^2)Q+
                     m(\Delta p\,v,-\Delta\gamma\,u)^t\right\}
               -\beta\Delta K\langle v^2\rangle Q .
 \tag{N.16}
\]
Again the mean is explicit.

Let \(W_0=\|w\|_\infty\), \(W_1=\|w'\|_\infty\) on a true radial cell,
\(\kappa=|K|\), \(\tau=|T|\), \(d=|d\nu|\),
\(E_1=e^{dW_0}\), \(E_{1/2}=e^{dW_0/2}\).
Then
\[
 |\Delta K|\le dE_1(W_0\kappa+W_1\tau),
\]
\[
 |\Delta\gamma|\le dE_{1/2}gW_0/2,\qquad
 |\Delta p|\le dE_{1/2}g(W_0\kappa/2+W_1\tau).
 \tag{N.17}
\]
After subtracting each true first derivative, the coefficient remainders
are bounded respectively by \(d^2 K_2,d^2 G_2,d^2 P_2\), where
\[
 K_2=E_1(W_0^2\kappa/2+W_0W_1\tau),\quad
 G_2=E_{1/2}gW_0^2/8,
\]
\[
 P_2=E_{1/2}g(W_0^2\kappa/8+W_0W_1\tau/2).
 \tag{N.18}
\]
The elementary exponential Taylor remainder proves all three inequalities
for real or complex increments. If \(dW_0<1\), one may replace the two
exponentials by \(1/(1-dW_0)\) and \(1/(1-dW_0/2)\).
No numerical derivative of a nearby branch is used.

For the actual bump
\(w=4096t^6(1-t)^6\), \(t=(r-1/20)/(13/100)\), the global bounds are
\[
 W_0=1,\qquad
 W_1^2=\left(\frac{2400}{13}\right)^2
                      \frac1{11}\left(\frac{10}{11}\right)^{10}
       <35^2 .
 \tag{N.19}
\]
Indeed \(w=(1-x)^6\) with \(x=(1-2t)^2\), and the derivative square
maximizes \(x(1-x)^{10}\) at \(x=1/11\).
Both control endpoints and the exterior have the actual zero extensions.

Write \(a_1=|\Delta K|\), \(d_1=|\Delta p|+|\Delta\gamma|\), and
\(\rho=\|h\|_{A_\sigma}\). The mixed state/parameter fee in the full
joint Taylor remainder is, by (N.16),
\[
 \|\Delta F(Q+h)-\Delta F(Q)\|_{A_{\sigma-\varepsilon}}
 \le b a_1\left(\frac1{4\varepsilon}+1\right)
          (3B_0^2\rho+3B_0\rho^2+\rho^3)
       +\frac{d_1}{\varepsilon}(2B_0\rho+\rho^2).
 \tag{N.20}
\]
The remaining pure parameter Taylor fee at \(Q\) is at most
\[
 d^2\left\{
 b K_2\left(\frac1{4\varepsilon}+1\right)B_0^3+
             \frac{P_2+G_2}{\varepsilon}B_0^2\right\}.
 \tag{N.21}
\]
The sum of (N.9), (N.20), and (N.21) is the complete joint remainder
of the real equation at the true same centre. Actual full-body
\(B_0,b,g,K,T\) envelopes still have to be supplied on their genuine cells.

## 6. Normalized variables and genuine radial interfaces

The actual solver uses \(u=\alpha U\), \(v=s(\nu)+\alpha V\) at fixed
\(\alpha\). A nonlinear increment of normalized variables \(k\) and
parameter \(d\nu\) has the exact physical state increment
\[
 h=\alpha k+(0,s(\nu+d\nu)-s(\nu))^t .
\]
Its linear part is
\(h_{\rm lin}=\alpha k+(0,s_\nu\,d\nu)^t\).
Let \(\mathcal D=\partial_r-D_QF(Q,\nu)\) be the complete true moving
linearization. The normalized residual Taylor remainder is exactly
\[
 \boxed{R_{\rm norm}
 =\alpha^{-1}\{\mathcal D(h-h_{\rm lin})
                         -R_{\rm joint}(h,d\nu)\}.}
 \tag{N.22}
\]
The sign in this formula is for residual \(Q_r-F\).
In particular the second radial jet of the normalized reference
cannot be dropped by applying only (N.9).

On any actual parameter neighborhood where the rotational branch is
separated, set \(\rho_0=a'^2/E_\nu\). Direct differentiation gives
\[
 s_\nu=-\frac{s\,\rho_0}{2(1-\rho_0)}w,\qquad
 s_{\nu\nu}=\frac{s\,\rho_0(\rho_0+2)}
                         {4(1-\rho_0)^2}w^2 .
 \tag{N.23}
\]
The full target jet and the radial derivative of (N.23) are needed to
bound the \(\mathcal D(h-h_{\rm lin})\) term. It is not a free
normalization. This agrees with the separate
[mean reference elimination](R133-supplement-full-scalar-mean-Green-and-residual-sensitive-nu.md)
and [complete ν column](R133-supplement-compact-metric-parameter-source-and-ray-return-twist.md).

The raw moving interface equation is \(Q^+-Q^-=0\), whose state
linearization is exact. Thus its Taylor remainder is zero in this
raw coordinate, while the centre's actual jump remains a nonzero data
row to pay. The true reference \(s(\nu)\) and its parameter derivatives
are continuous at the original intrinsic and control interfaces, so
(N.22) does not create fictitious raw jumps. Transformed mean, physical
angle and Riccati ports still require their separate exact interface
formulas; their nonlinear dependence has not been declared linear.

Nonlinear exterior Robin, mean and far-label rows remain separate
components of the full BVP. This body identity does not replace them.

## 7. Executed material and exact scope

Source:
[scripts/fourfold_codazzi_moving_nonlinear_flux_budget.mjs](../scripts/fourfold_codazzi_moving_nonlinear_flux_budget.mjs).

Report:
[32-gate exact budget](../notes/2026-11-14-R133-moving-nonlinear-flux-rational.json).

The full BigInt core actually executed in V8. It checks the conservative
equation, complete quadratic/cubic remainder, both mean-rank derivative
terms, all coefficient differences, the complete fifth parameter jet,
actual bump bound, and the same-root quantitative constants.
The finite Laurent fixture is explicitly artificial, has nonzero even
means, and includes every product mode. It is not a numerical replay of
the missing candidate. General identities were proved above; the
algebra check provides independent exact consistency.

The actual core and the Node CLI source are saved together. The Node
wrapper itself has not been run while the local executor is unavailable.
The source report contains its SHA256 and the exact input proof blobs.
Reproduction from the topic directory is
\[
 \texttt{node scripts/fourfold_codazzi_moving_nonlinear_flux_budget.mjs
 --out notes/2026-11-14-R133-moving-nonlinear-flux-rational.json}.
\]
Use a new output path if the original report is already present.

The complete nonlinear body formula and one actual root-germ application
are now paid. The full current-centre inverse, whole radial native cover,
compatible analytic/tame iteration, independent exterior equations,
and final closed-family geometry are still required.
