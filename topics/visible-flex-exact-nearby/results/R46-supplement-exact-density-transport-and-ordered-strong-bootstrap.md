# R46 supplement: exact density transports and the ordered lower-order bootstrap

This note replaces the large high-order diagonal comparison in the completed
strict operator by its actual characteristic flows. It uses exactly the same
old fixed-type operator, whole parameter interval \(p_5\pm10^{-9}\), true
physical cut \(r_c=268136140016943/1125899906842624\), physical momentum and
ordinary source. No field from the separate nonlinear Codazzi branch is
substituted.

At the common norm scale \(N=2^{20}\), the new complete bounds are

\[
\boxed{\begin{split}
\|\mathcal C_I:\mathcal P_{s,N}\to\mathcal P_{s,N}\|
   &<1.249362\,10^{167},&& |s|\le10.5,\\
\|R_2:E_{s,N}\to E_{s+2,N}\|
   &<5.517606\,10^{204},&& |s|\le8.
\end{split}}                                                 \tag{D.1}
\]

The Cauchy bound also holds for the inverse and every subinterval. The full
ordinary physical source-to-amplitude gain is below
\(1.807228\,10^{171}\). These are still large comparison constants. The
substantive change is that the exponential containing ten times the integral
of the characteristic derivative is no longer used at high orders. Only the
original zeroth-order energy exponential is retained; the higher estimates
use exact true density transport and a finite, chronologically ordered
one-angular-order recursion.

Every Fourier mode, both mean variables, all ordinary sources and all paths
through the head remain present. The full R46 model, its real nonconstant
phase, its physical normal frame and its four amplitude/frequency branches
are unchanged. No final returned inverse or effective feedback cutoff is
claimed by (D.1).

## 1. An exact density formulation of the physical equation

Use the preceding strict theorem's actual coefficients and definitions:

\[
Pu=\operatorname{div}(A\nabla u)+du=f,\quad
A=\begin{pmatrix}a&b\\b&c\end{pmatrix},\quad
p=au_r+bu_\theta,
\]

\[
\mu=\sqrt{b^2-ac},\quad m=\mu^{-1/2},\quad
v=b/a,\quad\nu=\mu/a,\quad L=\log\mu,
\quad T=(aL_r+bL_\theta)/2,
\quad\mathcal F=P(m)/m.
\]

Put

\[
w=\sqrt\mu\,u,\qquad
\zeta=\frac{p+Tu}{\sqrt\mu},\qquad
z=w_\theta,\qquad
\kappa=\mathcal F/\mu.                                      \tag{D.2}
\]

Direct differentiation, with the full zero-order coefficient included, gives

\[
P(mw)=\sqrt\mu\,[\operatorname{div}(A\mu^{-1}\nabla w)
                                +\kappa w].                 \tag{D.3}
\]

Indeed, the first-order coefficient in \(P(mw)/m\) is
\(\operatorname{div}A-A\nabla L\), which is
\(\mu\operatorname{div}(A/\mu)\). The potential is exactly
\(\mathcal F\), not a principal approximation. Also

\[
p+Tu=m(aw_r+bw_\theta),\qquad
\zeta=\nu^{-1}(w_r+vw_\theta).
\]

The two exact first-order equations are therefore

\[
\begin{split}
w_r&=\nu\zeta-vz,\\
z_r&=\partial_\theta(\nu\zeta-vz),\\
\zeta_r&=\partial_\theta(\nu z-v\zeta)-\kappa w+mf.
\end{split}                                                  \tag{D.4}
\]

For \(\sigma=\pm1\), define

\[
y_\sigma=(z+\sigma\zeta)/2.
\]

Then (D.4) is the exact pair of density transports

\[
\boxed{
(y_\sigma)_r+\partial_\theta[(v-\sigma\nu)y_\sigma]
       =-\frac\sigma2\kappa w+\frac\sigma2mf.}               \tag{D.5}
\]

The two velocities are precisely the actual characteristic velocities used
in the complete R106 flow certificate and in R46. All remaining cross-branch
coupling in (D.5) goes through \(w\), which costs one fewer angular derivative
than \(z=y_++y_-\). The source coefficient is exactly \(m/2\) on each
signed row; this normalization is used in the numerical consumer.

This change of dependent variables leaves the radial coordinate fixed.
There is no differentiation in a mixed radial/angular coordinate. In
particular, it does not demand nonexistent tenth radial derivatives across
the scalar spline knots. The original \(C^2\), piecewise higher radial
regularity is sufficient for (D.3)–(D.5), including their weak joining.
The prior theorem already supplies existence at every required angular
Sobolev level, so the estimates below are not a circular existence argument.

## 2. Complete means and the exact scaled antiderivative

All angular \(L^2\) norms use normalized circle measure. Put \(x=4\theta\),
and keep the norm convention

\[
\|u\|_{H_N^s}^2=\sum_{n\in\mathbb Z}(1+n^2/N^2)^s
                                      |\widehat u(n)|^2,
\quad\mathcal P_{s,N}=H_N^{s+1/2}\oplus H_N^{s-1/2}.          \tag{D.6}
\]

The derivative in (D.2) is the physical \(\partial_\theta\), whose
multiplier is \(4in\). Hence

\[
c_N=\frac{\sqrt{1+N^{-2}}}{4},\qquad
\|w\|_{H_N^{k+1}}
 \le |\langle w\rangle|+\sqrt2c_N
             \|(y_+,y_-)\|_{(H_N^k)^2}.                     \tag{D.7}
\]

This follows from the exact maximum of
\(\sqrt{1+n^2/N^2}/(4|n|)\) over nonzero integers and the triangle
inequality for \(y_++y_-\). It is not applied to the zero mode.

The constraint \(\langle y_++y_-\rangle=0\) follows from \(z=w_\theta\)
and is preserved by (D.5), since the two source rows cancel on summation.
The other density mean, \(\langle\zeta\rangle\), is present in the full
two-component norm. The height mean satisfies

\[
\frac{d}{dr}\langle w\rangle
 =\langle\nu(y_+-y_-)-v(y_++y_-)\rangle.                    \tag{D.8}
\]

It is bounded in section 4 using the original full physical energy; it is
never set to zero or reconstructed by an inverse angular derivative.

## 3. The actual density propagator and separate real/complex bounds

Let \(S_{r,t}\) be the actual relative characteristic label between any
two radial times. The homogeneous solution of one row of (D.5) is

\[
\mathscr D_{r,t}g=(S_{r,t})_\theta\,g\circ S_{r,t}.           \tag{D.9}
\]

The new complete R106 same-label certificate gives

\[
C_R<14.983652402,\qquad C_R^{-1}\le S_\theta\le C_R
\quad\hbox{on the real circle}.                             \tag{D.10}
\]

The old complete complex bound is still

\[
|S'|\le C_C<36.730914,\qquad
|\Im x|\le X=2.7952875\,10^{-5}.                            \tag{D.11}
\]

Both maps and inverses, both branches, all relative times and the entire
parameter interval are covered. The equality between the current operator
and those flow inputs is verified in the consumer, including its exact
physical cut. No R101 final-angle derivative is used for an intermediate
map.

For the normalized degree-one lift of \(S\), use

\[
J_1=C_R,\qquad
J_j=(j-1)!C_C/(X/2)^{j-1},\quad j\ge2.                      \tag{D.12}
\]

Let \(B_{j\ell}\) be the complete Bell polynomials bounded with these
\(J_j\). To bound a density transport, take any primitive \(G'=g\)
on the lifted real line. It may have a linear mean part. The exact chain
rule is

\[
\partial_x^j(S'g(S))
 =S'\sum_{\ell=0}^j
       \frac{B_{j+1,\ell+1}(S',\ldots)}{S'}
                         g^{(\ell)}(S).                    \tag{D.13}
\]

Its leading coefficient inside the sum is exactly \((S')^j\). Moreover,

\[
\|S'h\circ S\|_2^2
 =\int S'(S^{-1}\eta)|h(\eta)|^2\,d\eta
 \le C_R\|h\|_2^2.                                        \tag{D.14}
\]

Consequently the complete scaled derivative matrix has entries

\[
D_{j\ell,N}=
\begin{cases}
C_R^j,&j=\ell,\\
C_R B_{j+1,\ell+1}(J_1,J_2,\ldots)N^{-(j-\ell)},&\ell<j.
\end{cases}                                                \tag{D.15}
\]

With the same binomial weight \(W_k\) as before, define

\[
d_{k,N}=\sqrt{C_R}\,
 \|W_k(D_N)_{\le k}W_k^{-1}\|_2.                            \tag{D.16}
\]

This bounds (D.9) on the complete \(H_N^k\). Its zeroth value is
\(\sqrt{C_R}\), and its highest diagonal uses the true real Jacobian
power. Higher derivative entries retain the old complex Cauchy costs.
Both the full matrix and every norm are saved. In particular, no complex
estimate has been reduced merely because a real Jacobian improved.

Equations (D.13)–(D.16) hold for nonzero and zero Fourier inputs alike.
The primitive in their proof is a device for the chain rule, not an
operation that deletes the mean.

## 4. The original base energy pays all mean and starting costs once

Use the unchanged actual constraint energy

\[
e_0^2=\int(\lambda|u|^2+\gamma|u_\theta|^2+\alpha|p|^2),
\quad\lambda=-K_0>0,\quad\alpha=1/a,\quad\gamma=\mu^2/a.
\]

The original 215-cell certificate and exact reflection give, in either
orientation and on every subinterval,

\[
e_0(t)\le E_0\left[e_0(s)+\sqrt{\alpha_+}
                                  \int_s^t\|f(r)\|_2|dr|\right],
\quad
E_0=e^{I_0},\quad I_0<79.478945657.                          \tag{D.17}
\]

Only this zeroth exponent is used. In the scaled state norm,
\(e_0(s)\le\sqrt{h_{+,N}}\|(u,p)(s)\|_{\mathcal P_{1/2,N}}\),
with the same globally paid \(h_{+,N}\) as in the previous scaled consumer.

For each original cell, the full true field moduli and the positive energy
weights give

\[
\begin{split}
|\langle w\rangle|&\le W_0 e_0,\\
\|(y_+,y_-)\|_2&\le Y_0 e_0,                                \tag{D.18}
\end{split}
\]

where one sufficient local choice is

\[
\begin{split}
W_0&\ge\frac{\|\sqrt\mu\|_\infty}{\sqrt{\lambda_-}},\\
Z_0&=\|\sqrt\mu\|_\infty
       \left(\gamma_-^{-1/2}
                    +\frac{\|L_\theta\|_\infty}{2\sqrt{\lambda_-}}\right),\\
P_0&=\|m\|_\infty
       \left(\alpha_-^{-1/2}
                    +\frac{\|T\|_\infty}{\sqrt{\lambda_-}}\right),\\
Y_0&\ge\sqrt{(Z_0^2+P_0^2)/2}.
\end{split}                                                  \tag{D.19}
\]

The consumer computes (D.19) on each actual cell before taking the maximum.
It obtains \(W_0<4.546543\) and \(Y_0<69777.388\). The latter includes
the real conormal shear near the physical cut; it is not suppressed.

For unit initial data, put

\[
M_C=W_0E_0\sqrt{h_{+,N}},\qquad
V_{0,C}=Y_0E_0\sqrt{h_{+,N}}.
\]

For unit total ordinary-source norm with zero initial data, put

\[
M_S=W_0E_0\sqrt{\alpha_+},\qquad
V_{0,S}=Y_0E_0\sqrt{\alpha_+}.                               \tag{D.20}
\]

They bound respectively the full height mean and the base density vector.
Their hypotheses hold at any higher input angular order by the exact
embedding of the scaled norms. They cover arbitrary forced means.

## 5. Ordered lower-order bootstrap, with all chronological factors

Let \(M_{k,N}(M,a)\) denote the complete scaled Leibniz/Cauchy multiplier
bound of the preceding note. The native complex field strip is
\(a_f=1/160\) in \(x\). The full coefficient \(\kappa\) has the genuine
piecewise scalar majorant

\[
q(r)=M_{\mathcal F,i}/\mu_{-,i}
\quad\hbox{on cell }i,
\qquad Q_*:=\int_Iq(r)|dr|<113197.898279.                    \tag{D.21}
\]

The integral already includes the reflected half. Since the multiplier
comparison is homogeneous in its modulus,

\[
\|\kappa(r)g\|_{H_N^k}
 \le K_{k,N}q(r)\|g\|_{H_N^k},\qquad
K_{k,N}=M_{k,N}(1,a_f).                                    \tag{D.22}
\]

For unit initial physical data at level \(k+1/2\), a sufficient complete
initial density bound is

\[
F_{k,N}=\frac1{\sqrt2}\left[
4N M_{k+1,N}(\|\sqrt\mu\|_\infty,a_f)
 +M_{k,N}(\|m\|_\infty,a_f)
       \sqrt{1+M_{k,N}(\|T\|_\infty,a_f)^2}\right].          \tag{D.23}
\]

It follows by differentiating \(w=\sqrt\mu u\) with the actual physical
derivative and keeping \(\zeta=m(p+Tu)\). The factor \(4N\) is necessary;
the physical derivative is not normalized away.

Let \(V_k(t)=\|(y_+,y_-)(t)\|_{(H_N^k)^2}\). Duhamel for the exact
density equations, followed by (D.7), gives for \(k\ge1\)

\[
\begin{split}
V_k(t)\le d_{k,N}V_k(s)
 +d_{k,N}K_{k,N}\int_s^tq(r)
       \left(\frac{|\langle w(r)\rangle|}{\sqrt2}
                         +c_NV_{k-1}(r)\right)|dr|\\
\hspace{25mm}
 +\frac{d_{k,N}}{\sqrt2}M_{k,N}(\|m\|_\infty,a_f)
                                  \int_s^t\|f(r)\|_{H_N^k}|dr|.
\end{split}                                                  \tag{D.24}
\]

This is a strict one-order recursion, not a Gronwall inequality at order
\(k\). The main potential term contains \(w\), whose nonmean part is
recovered from density order \(k-1\); its mean was already paid in (D.20).

The consumer retains the time ordering in (D.24). For either initial-data
or source columns, define nonnegative polynomials \(P_k(Q)\) as follows:

\[
\begin{array}{c|cc}
&\text{initial-data column}&\text{ordinary-source column}\\ \hline
P_0&V_{0,C}&V_{0,S}\\
A_k&d_{k,N}F_{k,N}
 &d_{k,N}M_{k,N}(\|m\|_\infty,a_f)/\sqrt2\\
M&M_C&M_S
\end{array}
\]

and

\[
\boxed{
P_k(Q)=A_k+
  \frac{d_{k,N}K_{k,N}M}{\sqrt2}Q
  +d_{k,N}K_{k,N}c_N\int_0^QP_{k-1}(v)\,dv.}               \tag{D.25}
\]

At each intermediate time use \(Q(t)=\int_s^tq(r)|dr|\). The chain rule
\(dQ=q|dr|\) proves (D.25) directly by induction. Thus
\(V_k(t)\le P_k(Q_*)\). The integration of a monomial retains every
factor \(1/(j+1)\), including the factorial in the longest coupling chain.
Replacing every previous level by its final-time supremum would lose these
factors; the final report does not do so.

All polynomials and all coefficients are recorded. The old complete bound
\(F_{k,N}E_{k+1/2,N}^{\rm old}\) supplies an independent optional upper
bound for \(V_k\). The consumer takes the minimum only after evaluating
the valid complete polynomial. It does not use that minimum as though it
were an unproved intermediate-time polynomial.

## 6. Recovering both physical rows and the unchanged R46 model

From a completed bound for \(V_k\), use the exact identities

\[
u=mw,\qquad p=\sqrt\mu(y_+-y_-)-Tmw.                       \tag{D.26}
\]

Writing \(M_m,M_\mu,M_T\) for the indicated complete scaled multiplier
bounds, the two row estimates are

\[
\begin{split}
\|u\|_{H_N^{k+1}}
 &\le M_{m,k+1}(M+\sqrt2c_NV_k),\\
\|p\|_{H_N^k}
 &\le\sqrt2M_{\sqrt\mu,k}V_k
   +M_{T,k}M_{m,k}(M+\sqrt2c_NV_{k-1}).                     \tag{D.27}
\end{split}
\]

For \(k=0\), use \(V_0\) on the last line and the valid nonmean
\(L^2\) antiderivative constant \(1/4\le c_N\). Take the Euclidean norm
of these two scalar bounds. The complete old physical-state bound remains
an independent alternative, so the better value is retained at each
half-integer. At level \(1/2\), the old direct energy is kept.

All estimates apply in both radial orientations and to every subinterval.
The exact selfadjoint Green-flux pairing gives the negative half-integer
levels with the same physical momentum and scaled dual norms. Hilbert
interpolation then gives the complete window \([-10.5,10.5]\). Let
\(E_N^{\rm new}\) be its largest bound. For ordinary physical sources,
Duhamel gives \(L_r^1H_N^{s-1/2}\to\mathcal P_{s,N}\) with gain
\(E_N^{\rm new}\), including both means. The report additionally keeps
the sharper positive-level source columns from (D.25).

Finally reuse the frozen scaled R46 frame constants \(F_N,I_N\), actual
initial defect \(d_N\), full ordinary residual \(q_N\), cross terms
\(X_N\), remaining momentum \(\ell_N\), composition \(Q_N\), and
ordering \(K_N^{\rm ord}\). Only the actual Cauchy bound changes:

\[
\begin{split}
a_N^{\rm new}&=I_NE_N^{\rm new}(d_N+q_N+F_N)+1,\\
R_{2,N}^{\rm new}&=a_N^{\rm new}
       +4[2X_N+\ell_N+Q_NK_N^{\rm ord}].                   \tag{D.28}
\end{split}
\]

The full amplitude map/inverse bound is \(I_NE_N^{\rm new}F_N\), and the
ordinary physical source-to-amplitude gain is \(I_NE_N^{\rm new}\).
Every other coefficient in (D.28) is the previous complete one. In
particular the actual nonconstant phase, its source residual, its mean
columns and all high/low crossings have not been replaced by a scalar
or by a finite Fourier calculation.

## 7. Actual finite output and reproduction

The source is
`scripts/fourfold_strict_density_transport_bootstrap.py`; its report is
`notes/2026-11-13-R46-complete-density-transport-bootstrap.json`.
The final 320-bit consumer took 2.20 seconds and recomputed zero native
geometry cells. It checked the unchanged full 215-cell certificate,
the complete prior scaled consumer, the new whole-time real Jacobian
certificate, their exact actual family and source identities, and every
listed source dependency and input hash.

Safe outward rounded complete values are:

| \(N\) | Full physical Cauchy bound | Full strict \(E_{s,N}\to E_{s+2,N}\) remainder |
|---:|---:|---:|
| 1 | \(2.602675\,10^{245}\) | \(1.890384\,10^{495}\) |
| 4096 | \(9.324502\,10^{212}\) | \(1.741010\,10^{288}\) |
| 16384 | \(1.473453\,10^{192}\) | \(4.276362\,10^{251}\) |
| 65536 | \(2.300220\,10^{179}\) | \(6.274222\,10^{225}\) |
| 1048576 | \(1.249362\,10^{167}\) | \(5.517606\,10^{204}\) |

At \(N=2^{20}\), the full amplitude/inverse bound is below
\(3.062195\,10^{175}\), and the complete ordinary physical-source gain
below \(1.807228\,10^{171}\). The retained physical half-integer bounds
are:

| Level | Complete bound |
|---:|---:|
| \(1/2\) | \(2.589924\,10^{42}\) |
| \(3/2\) | \(2.098554\,10^{53}\) |
| \(5/2\) | \(1.397411\,10^{61}\) |
| \(7/2\) | \(1.503305\,10^{70}\) |
| \(9/2\) | \(2.616055\,10^{80}\) |
| \(11/2\) | \(7.316356\,10^{91}\) |
| \(13/2\) | \(3.265641\,10^{104}\) |
| \(15/2\) | \(2.312355\,10^{118}\) |
| \(17/2\) | \(2.584364\,10^{133}\) |
| \(19/2\) | \(4.540094\,10^{149}\) |
| \(21/2\) | \(1.249362\,10^{167}\) |

The report SHA256 is

    f86e1cd3e2be7542b4f0e3e5c52b297a77b016b3744df64cbfa04446a559ade7

Run from the topic directory with a fresh output path:

~~~bash
python3 scripts/fourfold_strict_density_transport_bootstrap.py \
  --out notes/R46-complete-density-transport-bootstrap-reproduced.json
~~~

The exact density identities (D.3)–(D.5), including the physical source
coefficient and both signs, were independently hand-checked by the tail
connector task before this consumer was frozen.

The improvement removes the artificial repeated high-order characteristic
exponent of the old comparison. It does not assert that the remaining
positive-majorant constants are close to the true propagation norm. In
particular, the unregularized strict potential integral (D.21), complete
frame changes and phase/source bounds remain substantial. The positive
Ai/contact network, the full returned nonmean phase, the full returned
\(R_*\), the finite Schur block and the final effective cutoff still
require their own quantitative proofs.
