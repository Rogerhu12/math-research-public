# R46 supplement: all 215 strict cells in scaled norms, with the diagonal budget separated

This note consumes the completed actual strict certificate, without recomputing
any geometry or native cell. It uses the same fixed-type object, the entire
parameter interval

\[
p_5=-7789843107295549/4611686018427387904,
\qquad |p-p_5|\le 10^{-9},
\]

and the same physical interval

\[
[-r_c,r_c],\qquad r_c=268136140016943/1125899906842624.
\]

The nonconstant root-cut connector has exactly this object, parameter box and
physical cut. Its input identity is checked, but none of its different graph
coefficients replaces a coefficient of this strict operator.

For every stated scale, the conclusion is the full actual decomposition

\[
\mathcal C_I=\mathcal W_0+R_2,
\qquad R_2:E_{s,N}\longrightarrow E_{s+2,N},\quad |s|\le8,       \tag{N.1}
\]

with the original four actual WKB branches, the original physical momentum,
the complete mean and ordinary source. In particular, at \(N=2^{20}\),

\[
\boxed{\|R_2:E_{s,N}\to E_{s+2,N}\|<1.745571\,10^{241}.}       \tag{N.2}
\]

This finite bound is substantially smaller than the unscaled complete bound,
but its remaining size has an explicit cause. The saved energy comparison
still contains a tenth-derivative diagonal exponential exceeding
\(4.73228\,10^{195}\). This is a property of that comparison argument,
**not a lower bound on the true PDE evolution**. Changing the norm scale
does not change this diagonal. The report distinguishes it from every
off-diagonal derivative commutator and from the frame/source fees. Neither
(N.2) nor the table below is advertised as a completed effective high
inverse or feedback cutoff.

## 1. Exact norms, physical Fourier lattice and source

Write \(x=4\theta\), so \(x\) has period \(2\pi\). For \(N\ge1\), set

\[
\|u\|_{H_N^s}^2
 =\sum_{n\in\mathbb Z}(1+n^2/N^2)^s|\widehat u(n)|^2,
\qquad
\mathcal P_{s,N}=H_N^{s+1/2}\oplus H_N^{s-1/2},
\quad E_{s,N}=(H_N^s)^2.                                    \tag{N.3}
\]

Thus the physical derivative scale is \(4N\). These norms contain every
Fourier mode; there is no projection at \(N\). The true momentum is still
\(p=au_r+bu_\theta\), and the normal-frame multiplier remains

\[
\Lambda_n=\max(1,4|n|).
\]

In particular its mean value is one. No physical operator is rescaled or
replaced. The complete ordinary source norm in this note is

\[
L^1\bigl(dr;H_N^{s-1/2}\bigr)
\]

of the same scalar right hand side of \(Pu=f\). This statement does not
relabel a divergence load as an ordinary source, or identify a tilted graph
Bochner norm with this physical radial norm.

The complete multiplier, composition and strong estimates below hold on
\([-10.5,10.5]\) where needed; the amplitude map and its inverse are recorded
on \([-10,10]\), and (N.1) on \([-8,8]\). Negative levels follow the exact
flux adjoint, with the same physical momentum. Intermediate real levels use
Hilbert interpolation.

## 2. Reusing the full positive comparison matrix

Let \(A=PB\) be the stored complete \(11\)-by-\(11\) nonnegative lower
triangular matrix of the preceding strict-operator supplement. It already
contains both reflected radial halves, in the correct order, and bounds
every subinterval in either direction. There are 215 closed positive cells;
their adjacent exact rational endpoints and the final endpoint are checked
again by this consumer. No leaf norm equivalence is inserted into the
product.

For derivative order \(j\), scale the energy variable by \((4N)^{-j}\).
The exact complete comparison is consequently

\[
A_N=D_NAD_N^{-1},\qquad
D_N=\operatorname{diag}_{0\le j\le10}(4N)^{-j},
\quad (A_N)_{j\ell}=(4N)^{-(j-\ell)}A_{j\ell}.               \tag{N.4}
\]

This is a diagonal conjugation of the already completed product, not a new
estimate of each factor. All lower-derivative couplings remain present.
The positive energy weights become

\[
h_{-,N}=\inf_I\min\{\lambda,(4N)^2\gamma,\alpha\},\qquad
h_{+,N}=\sup_I\max\{\lambda,(4N)^2\gamma,\alpha\},             \tag{N.5}
\]

where \(\lambda=-K_0\), \(\alpha=1/a\), \(\gamma=\mu^2/a\).
Their complete native lower bounds are strictly positive. With
\(W_k=\operatorname{diag}_{0\le j\le k}\sqrt{\binom kj}\), put

\[
E_{k+1/2,N}=
\sqrt{h_{+,N}/h_{-,N}}
\left\|W_k(A_N)_{\le k}W_k^{-1}\right\|_2,
\qquad E_N=\max_{0\le k\le10}E_{k+1/2,N}.                   \tag{N.6}
\]

The identity
\(\sum_{j=0}^k\binom kjN^{-2j}\|\partial_x^ju\|_2^2
=\|u\|_{H_N^k}^2\) proves the scaled energy comparison. Just one global
endpoint equivalence appears in (N.6). The complete source-to-physical-state
gain is at most \(E_N\), by Duhamel. Reflection, flux duality and
interpolation are the same actual ones already proved for the original
strict certificate.

### The invariant diagonal of this comparison

For each cell and each radial direction, the already certified diagonal is

\[
c_{jj}=\max(0,g/2+j\chi),
\]

where \(g\) is the zeroth energy rate and \(\chi\) the first characteristic
derivative rate. Lower triangular multiplication preserves the product of
these diagonal entries. The new report separately sums their complete
integrals and records

\[
\begin{split}
I_0&<79.478945657,\qquad I_\chi<37.107955541,\\
e^{I_0}&<3.290543\,10^{34},\qquad
e^{\sum L\max(0,g/2+10\chi)}<4.732284\,10^{195}.             \tag{N.7}
\end{split}
\]

In these stored comparison data the tenth logarithm agrees with
\(I_0+10I_\chi\), up to the stated directed arithmetic. Formula (N.4)
leaves every diagonal entry unchanged. The report saves the full matrix,
its diagonal part and its strictly lower part, and independently computes
their weighted norms on every half-integer level. The latter two are
diagnostics of this fixed upper-bound argument, not a decomposition of the
actual PDE propagator.

This distinction matters: the norm of this positive comparison matrix is
at least its largest diagonal entry, while the actual propagator need not
have any such lower bound. An improvement that uses exact characteristic
Jacobians must prove a different propagation estimate with all branch
couplings and sources. It cannot be obtained by lowering a diagonal entry
of (N.4) on the grounds that a true ray map is milder.

## 3. Complete scaled multiplication and composition

All analytic field bounds and every actual ray bound are reused with their
original whole-parameter scope. The complete field strip in the normalized
angle is \(X_f=4/640=1/160\). The actual all-time relative-flow strip is

\[
X=2.7952875\,10^{-5},\qquad
|H'|,|(H^{-1})'|\le C_J<36.730914,                           \tag{N.8}
\]

and both real derivatives are at least \(C_J^{-1}\). These are the same
550-segment true R106 flow bounds consumed in the preceding strict theorem,
not a rotational flow or the separate nonlinear Codazzi branch.

For a field bounded by \(M\) on a full strip of width \(a\), use the exact
scaled Leibniz comparison

\[
T_{j\ell}=\binom j\ell (j-\ell)!M/(Na)^{j-\ell},
\quad 0\le\ell\le j\le\lceil |s|\rceil.                   \tag{N.9}
\]

Its weighted principal operator norms bound multiplication in all required
integer norms. Real duality pays negative orders, and interpolation pays
the fractional orders. Denote the resulting maximum by
\(M_{s,N}(M,a)\). Its zeroth coefficient is \(M\); no unnecessary inverse
strip width is charged at derivative order zero.

For composition use the complete Bell polynomials of the actual map, with

\[
|H^{(j)}|\le (j-1)!C_J/(X/2)^{j-1}.
\]

Each Bell entry \(B_{j\ell}\) is multiplied by \(N^{-(j-\ell)}\).
The real change of variables contributes \(\sqrt{C_J}\). The negative
norms are obtained from the exact adjoint, including the genuine inverse
Jacobian multiplier. Call the resulting uniform bound through absolute
order 11 \(N_{c,N}\). The report saves both positive and negative integer
tables and the full scaled Bell matrix. Its finite matrices are proof
comparisons for complete infinite Fourier operators.

The complete Fourier moment used for ordering is

\[
Z_{p,k}(N,a)=\sum_{\ell\in\mathbb Z}
 (1+|\ell|/N)^p|\ell|^k e^{-a|\ell|}.                       \tag{N.10}
\]

It is evaluated by expanding the finite integer power and using the exact
positive Stirling/geometric power-tail formula. There is no omitted
Fourier tail. Formula (N.10) is also the explicit cutoff-dependent Peetre
weight: high derivatives carry \(N^{-k}\), and large Fourier lags retain
their full weights. No path through the low frequencies is deleted.

## 4. Two independent complete cross-cone bounds

The old complete 24-fold integration-by-parts constants are still valid in
the normalized angle and are retained in the new report. If \(B_{24}\)
is the appropriate starting-amplitude constant, the scaled Schur sums use

\[
\sum_{h\ge1}(1+h/N)^P h^{-D}
\le\sum_{j=0}^P\binom PjN^{-j}
       \left(1+\frac1{D-j-1}\right),\quad D>P+1.             \tag{N.11}
\]

The alternative gained-derivative splitting uses a known same-order bound
plus \(N^{-g}\) times the complete differentiated bound. The two cases are
\((P,g)=(9,2)\) for the unit amplitude and \((10,1)\) for the phase.
All nonzero input modes and bad-sign or zero outputs are included.

A much better independent bound follows from the actual analytic maps.
On \(|\Im x|\le X/2\), Cauchy gives \(|H''|\le2C_J/X\). Starting with
the real lower bound in (N.8), vertical integration therefore gives

\[
\Re H'(z)\ge c=\frac1{2C_J},\qquad
|\Im z|\le a_c=\frac{X}{4C_J^2}.                            \tag{N.12}
\]

This holds for each actual relative map and its actual inverse. The
completed directed values are \(a_c>5.1796813\,10^{-9}\) and
\(c>0.013612512\). If \(j\) and \(k\) have opposite signs, or \(k=0\)
with nonzero \(j\), shift the contour by \(\operatorname{sgn}(j)a_c/2\).
Since the maps are real on the real circle,

\[
\left|\widehat{A e^{ijH}}(k)\right|
 \le M e^{-d(|j|+|k|)},\qquad d=ca_c/2.                    \tag{N.13}
\]

The complete phase modulus is the original
\(H_*<2078931.088\), on the full relative-flow strip; it can be used as
\(M\) in (N.13). The unit amplitude uses \(M=1\).

For input absolute order at most \(r\) and output order at most 10.5,
a safe full Hilbert-Schmidt bound is

\[
M\{Z_{22,0}(N,2d)Z_{2r,0}(N,2d)\}^{1/2}.                  \tag{N.14}
\]

For a gain of \(g=1\) or 2, a second bound is the complete same-order
composition norm plus

\[
N^{-g}M\{Z_{2r,2g}(N,2d)Z_{2r,0}(N,2d)\}^{1/2}.           \tag{N.15}
\]

Indeed \(J_N\le I+|D_x|/N\) and \(J_N^2=I+|D_x|^2/N^2\),
where \(J_N=(1-D_x^2/N^2)^{1/2}\). The complete same-order part
retains the whole head and all zero outputs. The consumer takes the
minimum of the two independently proved contour bounds and the two
independently proved 24-fold bounds. Mean input is paid separately by the
full true Cauchy evolution below; no nonzero-input contour argument is
applied to it.

## 5. Exact frame, source, phase and strong remainder

The full normal frame, including its real conormal shear, is unchanged:

\[
\mathscr F(z_+,z_-)=2^{-1/2}
\binom{m\Lambda^{-1/2}(z_++z_-)}
{-Tm\Lambda^{-1/2}(z_++z_-)
       +i\sqrt\mu\Lambda^{1/2}(z_+-z_-)}.                   \tag{N.16}
\]

For \(J_N\) in (N.15), the exact physical multiplier bounds

\[
\|\Lambda^{1/2}J_N^{-1/2}\|\le\sqrt{4N},\qquad
\|J_N^{1/2}\Lambda^{-1/2}\|\le2^{1/4}
\]

include the mean. Thus, if \(M_m,M_\mu,M_T\) denote (N.9)'s complete
multiplier bounds for \(m,\sqrt\mu,T\), sufficient frame constants are

\[
\begin{split}
u_N&=2^{1/4}M_m,\\
F_N&=[u_N^2+(M_Tu_N+\sqrt{4N}M_\mu)^2]^{1/2},\\
I_N&=[4NM_\mu^2+\sqrt2M_m^2(1+M_T^2)]^{1/2}.               \tag{N.17}
\end{split}
\]

The exact phase \(h_\sigma\), initial momentum defect and canceled ordinary
residual \(P(mh_\sigma)\) are the same ones in the preceding theorem.
Their complete both-half residual integral is already

\[
P_*<1.136648\,10^{13};
\]

it is not multiplied by two again. At the true endpoint the scalar initial
defect is \(m\mathcal F a/(2\mu)\), and the remaining momentum field is
\(C_J\mathcal F a/(2\mu^2)\). Write their complete moduli as \(D_*\)
and \(L_*\). Define

\[
\begin{split}
d_N&=2^{3/4}M_{19/2,N}(D_*,X_f),\\
q_N&=4\,2^{1/4}N_{c,N}M_{19/2,N}(P_*,X),\\
a_N&=I_NE_N(d_N+q_N+F_N)+1,\\
\ell_N&=2M_{19/2,N}(L_*,X)N_{c,N},\\
Q_N&=2^{1/4}\sqrt{4N}\,N_{c,N},\\
K_N&=8H_*Z_{10,1}(N,X).                                    \tag{N.18}
\end{split}
\]

The factor four in \(q_N\) retains all amplitude/frequency branches. The
\(F_N\) term and final one in \(a_N\) retain the complete mean input
columns and all of their outputs. The physical lag is \(4\ell\), which
explains the factor eight in \(K_N\); the physical \(\Lambda\) was not
silently replaced by the normalized \(|n|\).

Let \(X_{1,N},X_{h,N}\) be the complete cross bounds in section 4 and put

\[
X_N=\sqrt{4N}\,[2^{1/4}X_{1,N}+2^{3/4}X_{h,N}].
\]

The complete R46 estimate is then

\[
\boxed{
R_{2,N}=a_N+4[2X_N+\ell_N+Q_NK_N].}                         \tag{N.19}
\]

The actual amplitude propagator and its inverse have bound
\(C_N=I_NE_NF_N\). The complete ordinary physical source-to-amplitude
gain is \(S_N=I_NE_N\). A sufficient complete model bound is
\(\max\{1,Q_N[1+M_{11,N}(H_*,X)]\}\). Formula (N.19) uses no
finite set of WKB columns as a substitute for a full operator theorem.

## 6. Completed values and the size of the remaining diagonal

The consumer ran at 320-bit directed precision in 1.89 seconds. The table
rounds every upper bound outwards. The diagonal and strictly lower columns
below include the same final global energy equivalence as the complete
energy column.

| \(N\) | Full \(E_N\) | Diagonal comparison only | Strictly lower comparison only | Full \(R_{2,N}\) |
|---:|---:|---:|---:|---:|
| 1 | \(2.602675\,10^{245}\) | \(3.552142\,10^{197}\) | \(2.602675\,10^{245}\) | \(1.890384\,10^{495}\) |
| 4096 | \(9.324502\,10^{212}\) | \(1.454958\,10^{201}\) | \(9.324502\,10^{212}\) | \(1.741010\,10^{288}\) |
| 16384 | \(1.187290\,10^{208}\) | \(5.819829\,10^{201}\) | \(1.187290\,10^{208}\) | \(3.445837\,10^{267}\) |
| 65536 | \(3.744850\,10^{204}\) | \(2.327932\,10^{202}\) | \(3.744778\,10^{204}\) | \(1.021469\,10^{251}\) |
| 1048576 | \(3.952528\,10^{203}\) | \(3.724691\,10^{203}\) | \(1.322556\,10^{203}\) | \(1.745571\,10^{241}\) |

For \(N=2^{20}\), the individual positive half-integer Cauchy bounds are:

| Level | Complete Cauchy bound |
|---:|---:|
| \(1/2\) | \(2.589924\,10^{42}\) |
| \(3/2\) | \(3.381892\,10^{58}\) |
| \(5/2\) | \(4.418229\,10^{74}\) |
| \(7/2\) | \(5.776716\,10^{90}\) |
| \(9/2\) | \(7.561116\,10^{106}\) |
| \(11/2\) | \(9.910355\,10^{122}\) |
| \(13/2\) | \(1.301116\,10^{139}\) |
| \(15/2\) | \(1.711547\,10^{155}\) |
| \(17/2\) | \(2.256462\,10^{171}\) |
| \(19/2\) | \(2.982303\,10^{187}\) |
| \(21/2\) | \(3.952528\,10^{203}\) |

At that same scale, the full actual amplitude bound is below
\(9.687675\,10^{211}\), the full model bound below
\(2.920301\,10^{29}\), and the complete ordinary physical-source gain
below \(5.717415\,10^{207}\). The contour cross term is below
\(6.033116\,10^{126}\), while the source/mean correction \(a_N\) is
below \(1.745571\,10^{241}\). Thus the improved contour estimate removes
the old 24-fold-IBP dominance at this scale. The remaining dominant term
uses the actual Cauchy comparison, its large diagonal, and the complete
ordinary residual; it is not an omitted Fourier tail.

The graph and root consumers use precisely these normalized norms at the
same scales. This permits honest norm-compatible composition, but does
not establish a small full return. Improving (N.7) requires the true
characteristic or normal-form propagation, with the current coefficients,
parameter box, complete branch coupling, frame and physical source paid.

## 7. Reproduction, identity and exact scope

The frozen consumer is
`scripts/fourfold_strict_scaled_complete_R46_budget.py`, and its final
report is
`notes/2026-11-13-R46-215-cell-scaled-strong-operator.json`.
Run from the topic directory with a new output path:

~~~bash
python3 scripts/fourfold_strict_scaled_complete_R46_budget.py \
  --scales 1 4096 16384 65536 1048576 \
  --out notes/R46-215-cell-scaled-strong-operator-reproduced.json
~~~

The consumer verifies the complete strict report and its source/dependencies,
the complete 215-cell native report and its source/dependencies, the actual
object hash and parameter identity, and the physical graph's exact endpoint
and family. The native report SHA256 is

    8a97d6780955b94f3f96ab7cd8c8d4e518f291cd04e0903505c03e2abe176788

and the original full strict consumer SHA256 is

    770fbb61134db79eb3ecb48710b5d65f72e1ff79b2eb3fc1015609a5da040b42

The scaled final report SHA256 is

    5f30d6f64a3a1b398dc3e9be7b17e0ea9e5f8117ef97ea50654cc2980e87dc02

The report contains the whole scaled matrix for every scale, every
half-integer bound, diagonal/off-diagonal diagnostics, full negative
composition bounds, both independent cross estimates, every frame/source
fee and all exact input hashes. No large raw native cache is newly saved.

The result is a complete strong theorem for this same strict interval.
Positive Ai/contact matching, the full returned nonmean phase, the complete
returned \(R_*\), finite head Schur inversion and the final quantitative
feedback cutoff remain separate obligations. Norm scaling never licenses
dropping those obligations or a low-frequency crossing.
