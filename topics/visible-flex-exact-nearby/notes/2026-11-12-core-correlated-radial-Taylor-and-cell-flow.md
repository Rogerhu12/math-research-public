# Correlated radial primitives and a true finite core cell transfer

## Scope and exact function

The source modules are
`scripts/fourfold_phase_core_radial_taylor.py` and
`scripts/fourfold_phase_core_cell_flow.py`. They use the same exact affine
symmetric infinite phase graph as the published quarter-cut cap inputs:
\[
 \delta=-7789843107295549/4611686018427387904.
\]
The source enforces a single exact common scalar spline span. On that span,
each scalar profile has its complete degree-at-most-20 polynomial
representation. Its analytic continuation is that polynomial germ; no
continuation across a different real spline span is silently substituted.

The result of the flow runner, if its complete flag is true, is a directed
transfer enclosure on precisely its stated real subinterval and retained
physical angular channels. A domain-only success is not a flow success. No
complete half-core, infinite core DN, or full Schur inverse is asserted.

## 1. Why the primitive is expanded before radial enclosure

Let \(P_Q(r,\theta)\) be the explicitly defined finite Fourier primitive
obtained from the exact phase tangent at the \(Q\) angular nodes. This is a
finite analytic function of \(r\), including the prescribed zero modes and
Nyquist deletion. For a fixed exact center \(c\), its finite Fourier
coefficients have expansions
\[
 \widehat P_{Q,k}(c+z)=\sum_{j\ge0}p_{j,k}z^j.
\]
The native Arb series engine encloses \(p_{j,k}\) before any nonzero radial
box is introduced. Only afterward does directed Horner evaluation enclose
the polynomial \(\sum_{j<P}p_{j,k}z^j\) and its first three radial derivatives.
Thus high angular modes carry their actual small radial Taylor coefficients.
They do not inherit a common wide interval error from independently boxed
values at the original angular sampling nodes.

This is an enclosure of a particular finite analytic primitive. It is not
yet the actual infinite primitive. Two independent remainders are retained.

For a finite-primitive modulus \(M_\ell\) on
\[
 |r-c|\le R_*,\qquad |\operatorname{Im}(4\theta)|\le s,
\]
where \(\ell=0,1,2\) counts physical angular derivatives, its radial Taylor
tail after \(P\) terms, differentiated \(j\le3\) times, is bounded by
\[
 M_\ell R_*^{-j}
 \sum_{n=P}^\infty n(n-1)\cdots(n-j+1)(\rho/R_*)^{n-j}.            \tag{1}
\]
The implemented finite closed form is the \(j\)-th derivative of
\(q^P/(1-q)\), with \(q=\rho/R_*<1\). All coefficients, factors and
derivatives in (1) are retained.

Separately the established exact infinite-primitive Fourier budget supplies
\(e_\ell\) on a radial disk of radius \(d\) around each evaluated radial box.
Cauchy's estimate gives its radial-derivative error \(j!e_\ell/d^j\).
The bulk interface expects a single scalar error in this convention. The
new source therefore returns
\[
 e_\ell^{\rm new}
 =e_\ell+\max_{0\le j\le3}\frac{d^j}{j!}
       \operatorname{Tail}_{P,j}(M_\ell,R_*,\rho).                \tag{2}
\]
Consequently its existing \(j!e_\ell^{\rm new}/d^j\) contract pays both
remainders for every required radial derivative. The maximum in (2) does
not subtract any original primitive error.

The target metric coefficient is the true bilinear angular mean
\(E=\langle F_r\cdot F_r\rangle\). The finite part is calculated by the
complete Fourier convolution with the reverse frequency, and the native
bilinear remainder adds all finite/infinite cross terms and error squares.
The same applies to \(E_r\). Then
\[
 K_0=\frac{a'E_r-2a''E}{2aE^2}
\]
uses genuine complex-valued \(E\) when \(r\) is complex. There is no real-axis
projection at a complex radial point.

## 2. Geometry and angular aliases

The primitive gives \(F,F_r,F_{rr}\). The exact phase tangent gives
\(F_\theta=aT\), \(F_{r\theta}\), \(F_{\theta\theta}\), without equating an
unpaid finite-primitive derivative to the exact tangent.

For a finite rotating-frame Fourier coefficient with normalized frequency
\(k\), a closed angular cell of halfwidth \(\pi/L\) and imaginary width \(s\)
has the displacement bound
\[
 |e^{ik\Delta x}-1|
 \le e^{|k|s}|k|\pi/L+e^{|k|s}-1,\qquad x=4\theta.               \tag{3}
\]
For complex \(r\), both real and imaginary parts of the center value remain
complex enclosures in (3). The real-axis shortcut used for real \(r\) is not
applied to a complex center.

The core coefficients are exactly the R37 coefficients, including the
original zero-order term and the complete ground-state correction:
\[
 a=-n\frac{F\cdot F}{S^2},\quad
 b=m\frac{F\cdot F}{S^2},\quad
 c=-\frac{(m^2+K_0G^2)(F\cdot F)}{S^2n},\quad
 \tau=d_0+(c_0-c)\ell^2,\quad \sigma=(c_0-c)\ell.
\]
Here \(S=F\cdot(F_\theta\times F_r)\),
\(G=(F_\theta\times F_r)\cdot(F_\theta\times F_r)\), and \(l,m,n\)
are the corresponding raw second-form contractions. On an ordinary disk
\[
 \ell=F_{\theta,z}/F_z-(F\cdot F_\theta)/(F\cdot F).
\]
The present ordinary-disk implementation rejects a nontrivial disk containing
the waist until the removable \(F_z/r\) quotient is supplied.

For the angular alias bounds, a broad rectangular enclosure of \(n\) need
not separate zero even when \(n\) is nonzero. The exact moving-frame identity
\[
 n=-a_{\rm radius}^2
   \big[(1+\beta_\theta)\cos\gamma\,Q-\gamma_\theta v\big]          \tag{4}
\]
instead gives the sufficient modulus bound
\[
 |n|\ge |a_{\rm radius}|^2
 \big(|1+\beta_\theta|\,|\cos\gamma|\,|Q|
             -|\gamma_\theta|\,|v|\big).                        \tag{5}
\]
All four factors and the remainder in (5) belong to the same true fields.

A useful bound for \(1+\beta_\theta\) evaluates its **radial polynomial
coefficients before radial Horner evaluation**, at each of the two angular
boundaries \(x_j\pm is\). Each real angular cell is closed. Positivity of
\(\operatorname{Re}(1+\beta_\theta)\) on these boundaries extends to the
whole periodic strip by the harmonic minimum principle. This also retains
radial correlation among the different phase harmonics.

If the true coefficient \(g(r,\theta)\) has modulus at most \(M_g\) on this
angular strip, the trapezoidal coefficient of lag \(k\) on \(L\) nodes has
the complete alias bound
\[
 M_g\frac{e^{-(L-|k|)s}+e^{-(L+|k|)s}}{1-e^{-Ls}}.               \tag{6}
\]
Both signs and all translates are included. The generator is built from the
actual retained coefficients with \(k=-N,\ldots,N\), including the mean.

## 3. A radial analytic domain without a wrapping matrix inverse

A true outer Cauchy domain for the **finite projected generator** needs
holomorphy in \(r\), not a nonzero angular complex strip at every outer \(r\).
The complete real angular circle suffices to define and bound each Fourier
coefficient analytically in \(r\). Angular strips for (6) are paid separately
at the time-DFT sample points.

On the entire complex radial box, suppose the closed real angular cover gives
\[
 \operatorname{Re}a(r,\theta)\ge m>0.
\]
For \(A=P_NaP_N\) and any retained complex vector \(v\),
\[
 \operatorname{Re}\langle Av,v\rangle
 =\int\operatorname{Re}a\,|v|^2\ge m\|v\|^2.
\]
Thus every \(A(r)\) is invertible and \(\|A(r)^{-1}\|\le m^{-1}\).
This assertion preserves the Toeplitz origin of \(A\); it does not require
every unrelated matrix in an entrywise wide box to be invertible.

Put \(D=\operatorname{diag}(4ik)\), \(\lambda=\|D\|=4N\), and let
\(B=P_NbP_N\), \(C=P_NcP_N\). The zero-order matrix is
\[
 H=P_N\tau P_N+D(P_N\sigma P_N)-(P_N\sigma P_N)D.
\]
In particular
\[
 \|H\|\le\|\tau\|_\infty+2\lambda\|\sigma\|_\infty.                \tag{7}
\]
No uncomputed full derivative of \(\sigma\) is needed for this finite block.

In the state \((w,p/\kappa)\), \(\kappa>0\) exact, the true generator is
\[
 {\cal F}=
 \begin{pmatrix}
 -A^{-1}BD&\kappa A^{-1}\\
 (DBA^{-1}BD-DCD-H)/\kappa&-DBA^{-1}
 \end{pmatrix}.                                                 \tag{8}
\]
If \(b_*,c_*,t_*,s_*\) bound the four scalar moduli on the complete real
angular circle, the four block norms in (8) are bounded by
\[
 f_{11}=f_{22}=b_*\lambda/m,\quad f_{12}=\kappa/m,\quad
 f_{21}=\frac{\lambda^2b_*^2/m+\lambda^2c_*+t_*+2\lambda s_*}
                 {\kappa}.
\]
The scalar two-by-two Frobenius norm is a valid upper bound \(M\) for
\(\|{\cal F}\|\). This proves a genuine holomorphic finite-generator domain
even if an entrywise interval inversion of the wide Fourier matrix fails.

## 4. Complete time-circle extraction

Let the physical real interval be \([c-h,c+h]\), \(h>0\) exact, and
\(u=(r-c)/h\). Assume the previous section proves
\(\|{\cal F}(u)\|\le M\) on \(|u|\le R\), where \(R>1\).
Choose \(1<\rho<R\) and an even number \(L_t\) of circle nodes.

The sample values are directed enclosures of the **true** generator.
For real \(r\), \(a,c,\tau\) are angularly even and \(b,\sigma\) are odd.
The two factors of \(i\) in the projected formulas make every entry of
\({\cal F}(r)\) real. Thus
\({\cal F}(\bar u)=\overline{{\cal F}(u)}\), which justifies obtaining the
lower time half-circle by conjugation. At the two real circle nodes the
mathematically real entries may be restricted to their real parts.

For \(0\le j<m<L_t\), the normalized circle DFT, divided by \(\rho^j\),
differs from the true radial Taylor matrix coefficient by at most
\[
 M R^{-j}\frac{(\rho/R)^{L_t}}{1-(\rho/R)^{L_t}}.                 \tag{9}
\]
Only the aliases \(j+\ell L_t\), \(\ell\ge1\), occur because the generator
is holomorphic at \(u=0\). The Acb DFT encloses all actual node errors.
After choosing an exact real dyadic coefficient \(F_j\), its complete fee
is the operator/Frobenius norm of the DFT enclosure minus \(F_j\), plus (9).

The complete unretained time tail on \(|u|\le1\) is
\[
 M\frac{R^{-m}}{1-R^{-1}}.                                      \tag{10}
\]
Summing the chosen-coefficient errors and (10) yields
\(\|{\cal F}-F_{\rm poly}\|\le\varepsilon_F\) on the full real interval.
A small finite tail is never substituted for (10).

## 5. Exact rational reference and true local transfer

Define the degree-\(q\) matrix polynomial \(Z\) by
\[
 Z_0=I,\qquad
 Z_{k+1}=\frac{h}{k+1}
   \sum_{j=0}^{\min(k,m-1)}F_jZ_{k-j},\quad 0\le k<q.             \tag{11}
\]
The saved \(F_j\) and \(h\) are exact dyadic numbers. Formula (11) therefore
defines exact rational coefficients. Arb only encloses this exact definition;
it does not select rounded coefficients for \(Z\).

Let \(d_Z=\sum_{k=1}^q\|Z_k\|<1\). On \(|u|\le1\),
\[
 \|Z\|\le1+d_Z,\qquad \|Z^{-1}\|\le(1-d_Z)^{-1}.                 \tag{12}
\]
By the defining recurrence, all coefficients of \(hF_{\rm poly}Z-Z'\)
of degrees \(0,\ldots,q-1\) vanish **algebraically**. The source bounds all
remaining coefficients through degree \(q+m-1\), without deleting any
high term. Write their norm sum as \(e_{\rm poly}\).

For the genuine equation \(W'=h{\cal F}W\), set \(W=ZV\). The complete
reduced perturbation has integral at most
\[
 A_*=\frac{2}{1-d_Z}
       \big(e_{\rm poly}+h\varepsilon_F(1+d_Z)\big).               \tag{13}
\]
The time-ordered integral equation, or Gronwall's inequality, gives
\(\|V(1)-I\|\le e^{A_*}-1\) when \(V(-1)=I\). Hence the actual local
transfer \(T\) satisfies
\[
 \big\|T-Z(1)Z(-1)^{-1}\big\|
 \le\frac{1+d_Z}{1-d_Z}\big(e^{A_*}-1\big).                       \tag{14}
\]
The final selected dyadic transfer center has its separate directed
selection error added to (14). The factor \(Z(-1)^{-1}\) is essential:
the reference is normalized at \(u=0\), not at the left endpoint.

## 6. Outputs and future composition

A completed flow report records the exact common span and actual real
subinterval, exact object and source hashes, all domain bounds, every
time-coefficient fee, (10)--(14), and the selected-array hash.
Its NPZ contains the complete exact dyadic \(F_j\) and local transfer center.

For a later complete chain of local centers \(T_j\) with errors
\(\epsilon_j\), let \(P_j=T_j\cdots T_1\). If every necessary prefix inverse
is verified, an admissible accumulated perturbation is
\[
 \beta_j=\|P_j^{-1}\|\,\epsilon_j\,\|P_{j-1}\|,\qquad
 \|T_{\rm true,full}-P_{\rm last}\|
 \le\|P_{\rm last}\|\big(\exp(\sum_j\beta_j)-1\big).
\]
This avoids replacing the actual moderate transfer by
\(\exp(\int\|{\cal F}\|)\). No missing common span, even a binary-width
near-coincident one, may be skipped. This composition and the subsequent
finite DN conversion require their own complete reports.

The ordinary prototype deliberately rejects a nontrivial waist disk. A future
waist implementation must use the analytic \(F_z/r\) quotient with its own
complete primitive/Taylor remainder. It cannot suppress a division by zero
merely because a floating evaluation is small.

Actual successful and failed remote runs are kept separately under
`notes/core_remote/<run-id>/`. The old rectangle support failure and the
subsequent wide-matrix inversion failure are enclosure failures; neither is
reported as a geometric singularity.


## 7. Removable waist quotient on the first positive common germ

The separate `fourfold_phase_core_waist_taylor.py` adapter supplies the
previously missing waist case. It does not declare the positive spline germ
to be globally even or odd. Instead, explicit reflection and continuity give
the exact identities \(\gamma(0,\theta)=Z(0)=0\). These imply
\[
 F_z(0,\theta)=P_{Q,z}(0,\theta)=0
\]
for every retained affine parameter. The positive single-span analytic
extensions therefore have removable quotients by \(r\), even when their
higher Taylor coefficients do not have a global parity.

The native finite primitive is expanded at the exact center \(r=0\).
Its vertical constant coefficient is set to the known exact zero after
confirming that its directed enclosure contains zero. This is the use of an
analytically proved identity, not a rule that small numbers are zero.

Suppose \(V\) is either the finite vertical primitive or its physical angular
derivative, analytic in \(|r|\le R_*\), with \(V(0)=0\) and \(|V|\le M\).
The maximum principle applied to \(V/r\) gives
\[
 |V(r)/r|\le M/R_*.
\]
If the primitive uses \(P\) radial terms, its quotient retains \(P-1\) terms.
Its full radial remainder at \(|r|\le\rho<R_*\) is at most
\[
 \frac{M}{R_*}\frac{(\rho/R_*)^{P-1}}{1-\rho/R_*}.                \tag{15}
\]
The actual infinite-minus-finite primitive also vanishes at zero. Its complete
Fourier error \(e_\ell\), bounded on the same outer disk, contributes
\(e_\ell/R_*\) to the quotient error. These two errors are added, separately
for \(Q=F_z/r\) and \(Q_\theta\).

The exact ground-state coefficient is then evaluated as
\[
 \ell=Q_\theta/Q-(F\cdot F_\theta)/(F\cdot F),
\]
after a directed nonvanishing bound for \(Q\). No division by a radial interval
containing zero occurs. The fields \(F_\theta\) and the other nonquotient jets
continue to use the exact tangent representation. Formula (15) and the whole
infinite Fourier error ensure that their shared object is the same actual
infinite graph.

## 8. Uniform affine parameter interval

The adapter `fourfold_phase_core_parameter_taylor.py` uses the already frozen
`ParameterGermMixin.direction_scalars` construction. It first forms complete
central and direction scalar polynomials, with exact common-span selection:
\[
 \beta_p=\beta_{\delta_5}+p\,\dot\beta,\quad
 \gamma_p=\gamma_{\delta_5}+p\,\dot\gamma,\quad
 a_p=a_{\delta_5}+p\,\dot a,\quad Z_p=Z_{\delta_5}+p\,\dot Z.
\]
Only afterward is the one real increment \(p\in[-\eta,\eta]\) enclosed.
The central raw coefficients already contain \(\delta_5\); adding the
increment \(p\), rather than \(\delta_5+p\), avoids counting the center twice.

Every native primitive coefficient, analytic majorant, denominator bound,
projected coefficient, circle sample and flow defect encloses this entire
same parameter interval. The Cauchy estimates and time alias formula are
uniform in the real parameter. A single selected dyadic reference polynomial
therefore yields a uniform local transfer error for the whole stated family.

The report names both the central exact object and the complete rational
parameter interval. A center-only result is never relabeled as a family
certificate. The intended initial family pilot uses the explicit half-width
\(\eta=1/1000000000\).

## 9. Executed center check and an explicitly invalidated predecessor

Run `43303783707` produced nonfinite norm fees because the original norm
helper squared Arb absolute-value balls containing zero and then took a
square root of an enclosure with a slightly negative lower endpoint. The
complete flag in that output was incorrect. Its
`notes/core_remote/43303783707/invalidated.json` explicitly removes any
local-transfer claim from that report; it remains as failure evidence.

The norm routine now squares each exact nonnegative absolute **upper bound**
before summing, and the flow runner rejects all nonfinite fee records.
Run `43304523644` genuinely recomputed the center cell 90 and obtained
\[
 \|T_{\rm true}-T_{\rm saved}\|
 <1.844604306\cdot10^{-11}
\]
in the state \((w,p/8)\), with \(d_Z<0.077345854\).
Its complete report SHA256 is
`d42f3523f4e0871b7d6b14413bb917e06e63663b78c0007a2b54a2428cd5d74b`.
The interval is exactly
\([1/8,2296835809958953/18014398509481984]\).
This is one actual center cell, not the complete core or the family pilot.
