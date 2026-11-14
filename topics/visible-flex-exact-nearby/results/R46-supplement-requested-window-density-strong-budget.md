# R46 supplement: requested Sobolev windows for the complete actual density budget

This theorem consumes the already completed 215-cell strict certificate and
the complete same-label real Jacobian certificate. It proves the same actual
four-branch decomposition, with the same original phase and momentum,

\[
\mathcal C_I=\mathcal W_0+R_2,\qquad
R_2:E_{s,N}\longrightarrow E_{s+2,N}.                         \tag{W.1}
\]

The constants are now evaluated at the window actually required by (W.1).
In particular, at \(N=2^{20}\),

\[
\begin{array}{c|c}
\text{window}&\text{complete bound for }R_2\\ \hline
s=0&3.776923\,10^{80}\\
|s|\le4/3&1.715736\,10^{93}\\
|s|\le2&1.199049\,10^{101}\\
|s|\le8&3.069056\,10^{191}.
\end{array}                                                  \tag{W.2}
\]

Every number is an outward rounded upper bound for a complete operator.
No frequency is removed at \(N\), and no native geometry or ray cell is
recomputed. These are finite strong bounds; the returned \(R_*\), regular
port elimination, finite Schur complement and effective feedback cutoff
are not conclusions of this note.

## 1. Fixed object, exact norms and physical source

The actual object is
type_fixed_step02_d5_exact_affine_step5_object.json, SHA256
91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848.
The entire affine parameter interval is

\[
p_5=-7789843107295549/4611686018427387904,\qquad
|p-p_5|\le10^{-9}.
\]

The exact physical interval is \([-r_c,r_c]\), where

\[
r_c=268136140016943/1125899906842624.
\]

The consumer rechecks all 215 positive-half closed cells, their continuous
cover, the exact physical endpoint, the source hashes, all listed input
and dependency hashes, and equality of the actual identity carried by the
strict, field, density and real-ray reports. The reflected half is the one
already proved in the complete strict certificate. None of the separate
nonlinear Codazzi branch's coefficients is substituted here.

Use \(x=4\theta\) with period \(2\pi\), and define

\[
J_N=(1-\partial_x^2/N^2)^{1/2},\qquad
\|u\|_{H_N^s}=\|J_N^su\|_2,
\]
\[
E_{s,N}=(H_N^s)^2,\qquad
\mathcal P_{s,N}=H_N^{s+1/2}\oplus H_N^{s-1/2}.              \tag{W.3}
\]

The physical momentum is \(p=au_r+bu_\theta\). The normal-frame multiplier
is still \(\Lambda_n=\max(1,4|n|)\), including its exact mean value one.
The physical derivative scale is \(4N\). Increasing \(N\) changes a norm,
not the equation or the set of retained modes.

For \(Pu=f\), the ordinary source used throughout this theorem is the
same scalar \(f\), in

\[
L^1(dr;H_N^{s-1/2}).                                        \tag{W.4}
\]

No divergence load, tilted-graph Bochner norm or canonical root source
is silently identified with (W.4). Both state rows, both means, and the
same physical Green pairing are retained.

The complete inputs are the following four reports and their theorems:

- 2026-11-13-R46-complete-actual-strict-operator.json,
  with R46-supplement-complete-actual-strict-operator.md;
- 2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz;
- 2026-11-13-R46-complete-density-transport-bootstrap.json,
  with R46-supplement-exact-density-transport-and-ordered-strong-bootstrap.md;
- 2026-11-13-R106-complete-relative-real-Jacobian.json.gz,
  with R106-supplement-complete-same-label-real-relative-Jacobian.md.

The complete multiplier and WKB bookkeeping below are the ones proved in
R46-supplement-215-cell-scaled-strong-operator-and-diagonal-budget.md.
This note changes their bounds only where the following argument supplies
the narrower window or the separate real Jacobian.

## 2. The physical Cauchy window is \(S+2\)

The density theorem gives complete physical Cauchy bounds \(E_{h,N}\)
at every positive half-integer

\[
h=\tfrac12,\tfrac32,\ldots,\tfrac{21}2.
\]

Each applies to every subinterval, in both directions, and to both
physical state rows. Its proof starts with the full zeroth-order energy,
uses the exact density equations

\[
\partial_ry_\sigma+
\partial_\theta[(v-\sigma\nu)y_\sigma]
 =-\frac{\sigma\kappa}{2}w+\frac{\sigma m}{2}f,
\]

and preserves every chronological integration factor in the triangular
lower-order bootstrap. In particular, we do not reinsert the final
supremum into each time integral.

The exact Green-flux adjoint gives the same bound at \(-h\).
The pairing exchanges the two rows of \(\mathcal P_{h,N}\), so its dual
state is exactly \(\mathcal P_{-h,N}\); there is no additional scale or
mean normalization in this step.

For \(T\ge0\), define \(\mathfrak E_N(T)\) as follows. If \(T\le1/2\),
use \(E_{1/2,N}\) by interpolation between the two flux-dual endpoints.
If \(T\) lies between consecutive positive half-integers \(h_0<h_1\),
put

\[
E_{T,N}\le
E_{h_0,N}^{\,1-t}E_{h_1,N}^{\,t},\qquad
t=(T-h_0)/(h_1-h_0).                                      \tag{W.5}
\]

Take the maximum of this endpoint bound and all positive half-integer
bounds at or below \(T\). This is a uniform bound on
\([-T,T]\), not just on its endpoints. The saved report records the
exact rational interpolation weights.

To prove (W.1) for every \(|s|\le S\), the physical Cauchy correction
is needed at \(s+2\), hence within

\[
|s+2|\le T:=S+2.                                          \tag{W.6}
\]

The separate frame multipliers need absolute order \(T+1/2\), but that
does not change the Cauchy index in (W.6). Using the largest available
Cauchy bound at \(21/2\) for this entire task was valid and unnecessary.
For example, at \(N=2^{20}\),

\[
\mathfrak E_N(2)
 \le\sqrt{E_{3/2,N}E_{5/2,N}}
 <1.712467\,10^{57},                                      \tag{W.7}
\]

whereas the old uniform \(21/2\) bound exceeded \(10^{167}\).
This is a change in what is requested from the proved hierarchy, not a
change of the PDE or a discarded high-order remainder.

For (W.4), Duhamel and the all-subinterval bound give the same
\(\mathfrak E_N(T)\) from the ordinary source into the physical state,
at each permitted state index. The mean source uses this same argument.

## 3. Complete composition with distinct real and complex permissions

Write \(H\) for any actual relative characteristic map required by the
strict theorem, or its inverse. The same-label real-ray result gives

\[
C_r<14.983653,\qquad
C_r^{-1}\le H'(x)\le C_r\quad(x\in\mathbb R).               \tag{W.8}
\]

The previous complete complex certificate remains

\[
|H'(z)|\le C_c<36.730914,\qquad
|\Im z|\le X,\qquad X=2.7952875\,10^{-5}.                   \tag{W.9}
\]

Both maps have their separately paid complex domains. Formula (W.8)
does not authorize replacing \(C_c\) by \(C_r\) in a complex Cauchy
estimate. Accordingly use the real derivative majorants

\[
H_1=C_r,\qquad
H_j=(j-1)!\,C_c/(X/2)^{j-1}\quad(j\ge2).                  \tag{W.10}
\]

The deliberately smaller Cauchy radius \(X/2\) is valid at every real
point. Let \(B_{j\ell}\) be the complete nonnegative Bell recursion

\[
B_{00}=1,\qquad
B_{j\ell}=\sum_{b=1}^{j-\ell+1}
 {j-1\choose b-1}H_bB_{j-b,\ell-1}.
\]

All undefined entries are zero. In the scaled derivative vector, the
composition matrix is

\[
A_{j\ell}=B_{j\ell}N^{-(j-\ell)}.                          \tag{W.11}
\]

For integer \(k\), put \(W_k=\operatorname{diag}_{0\le j\le k}
\sqrt{\binom kj}\). The identity

\[
\|u\|_{H_N^k}^2
 =\sum_{j=0}^k\binom kjN^{-2j}\|\partial_x^ju\|_2^2
\]

and the real change of variables give

\[
\|u\circ H\|_{H_N^k}
 \le\sqrt{C_r}\,
 \|W_kA_{\le k}W_k^{-1}\|\,\|u\|_{H_N^k}.                 \tag{W.12}
\]

Thus only the real Jacobian and the leading repeated first derivative
use \(C_r\). The lower Bell entries preserve every higher complex
derivative cost.

Negative orders must also include the exact inverse-Jacobian multiplier:

\[
C_H^*=M_{(H^{-1})'}C_{H^{-1}}.
\]

For this multiplier the scaled Leibniz matrix is

\[
T_{j\ell}=\binom j\ell
\begin{cases}
C_r,&j=\ell,\\
(j-\ell)!\,C_c/(NX/2)^{j-\ell},&j>\ell.
\end{cases}                                               \tag{W.13}
\]

Multiplying (W.12) by
\(\|W_kT_{\le k}W_k^{-1}\|\) therefore pays \(H_N^{-k}\).
The same construction applies to \(H^{-1}\). Interpolation pays real
orders. The comparison norm of each finite nonnegative matrix is
bounded by the better of its full Frobenius and Schur bounds.
These matrices compare complete infinite Fourier operators.

For a requested strong window \(S\), let

\[
d_S=\lceil S+5/2\rceil,\qquad
\mathfrak C_N(S)=
\max_{0\le k\le d_S}
\{\text{positive and negative bounds above}\}.             \tag{W.14}
\]

The complete matrices and all individual integer bounds are saved.
This proves the smaller composition constants used below without any
analytic-width enlargement.

## 4. Requested-order cross-cone estimates, including zero outputs

Two independently complete estimates are available. The old 24-fold
integration-by-parts bound, with its original complex \(C_c\), is reused
unchanged. It has enough differentiability for all stated windows.

There is also a refined contour bound using (W.8) only on the real axis.
Cauchy gives \(|H''|\le2C_c/X\) on the half strip. Therefore

\[
a_c=\frac{X}{4C_rC_c},\qquad c=\frac1{2C_r}
\quad\Longrightarrow\quad
\Re H'(z)\ge c\quad (|\Im z|\le a_c).                      \tag{W.15}
\]

Indeed the vertical loss is at most
\((2C_c/X)a_c=1/(2C_r)\). The smaller strip lies inside the
already proved half strip.

For a complete analytic amplitude \(A\), \(|A|\le M\), the Fourier
matrix of \(A\,C_H\), on nonzero input \(j\) and opposite-sign or zero
output \(k\), obeys

\[
|\widehat{Ae^{ijH}}(k)|
 \le M e^{-d(|j|+|k|)},\qquad d=ca_c/2.                   \tag{W.16}
\]

Shift by \(\operatorname{sgn}(j)a_c/2\); realness of \(H\)
and (W.15) supply the input decay, while the output exponential has
at least this much decay because \(c\le1\).

For nonnegative integers \(p,k\), retain the exact complete moment

\[
Z_{p,k}(N,a)=\sum_{\ell\in\mathbb Z}
 (1+|\ell|/N)^p|\ell|^ke^{-a|\ell|}.                       \tag{W.17}
\]

Its consumer expands the integer power and uses the exact
Stirling/geometric rational-function sum for every power moment.
There is no omitted Fourier complement.

For a requested input order \(|r|\le p\) and smoothing gain
\(g\in\{1,2\}\), the full Hilbert-Schmidt estimate from (W.16) is

\[
M\{Z_{2p,0}(N,2d)Z_{2(p+g),0}(N,2d)\}^{1/2}.             \tag{W.18}
\]

This replaces the old universal output exponent 22 by the actual
requested output exponent \(2(p+g)\).
A second independent bound is

\[
B_{\rm same}
 +N^{-g}M
 \{Z_{2p,0}(N,2d)Z_{2p,2g}(N,2d)\}^{1/2}.                \tag{W.19}
\]

Here \(B_{\rm same}\) is the complete same-order composition/multiplier
bound. For \(g=1\), use \(J_N\le I+|D_x|/N\); for \(g=2\), use
\(J_N^2=I+|D_x|^2/N^2\). The projections have norm one.
The weights in (W.18)–(W.19) also cover negative \(r\).

Use

\[
(p,g,M)=
(\lceil S+1/2\rceil,2,1)
\quad\hbox{or}\quad
(\lceil S+3/2\rceil,1,H_*).                               \tag{W.20}
\]

The complete same-order bounds are respectively
\(\mathfrak C_N(S)\) and
\(M_{p,N}(H_*,X)\mathfrak C_N(S)\).
Take the better of (W.18), (W.19) and the two existing 24-fold bounds.
Call the resulting constants \(X_{1,N,S}\) and \(X_{h,N,S}\).

All bad-sign and zero outputs are present in these sums. Mean input is
handled by the full physical Cauchy correction in section 6, not by
applying a nonzero-input contour argument to it. Paths entering and
leaving any finite head are never projected away.

## 5. Windowed frame, with the original physical momentum

Let \(M_{t,N}(M,a)\) be the complete multiplier bound from the scaled
Leibniz matrix, duality and interpolation in the prior scaled theorem.
The normalized field strip remains \(X_f=4/640=1/160\).
For \(|s|\le T\), take its absolute multiplier order \(T+1/2\)
for \(m=\mu^{-1/2}\), \(\sqrt\mu\), and \(T_{\rm sh}\), the
original real conormal shear. Denote these three bounds by
\(M_m,M_\mu,M_{\rm sh}\).

The exact frame is

\[
\mathscr F(z_+,z_-)=2^{-1/2}
\binom{m\Lambda^{-1/2}(z_++z_-)}
 {-T_{\rm sh}m\Lambda^{-1/2}(z_++z_-)
   +i\sqrt\mu\Lambda^{1/2}(z_+-z_-)}.
\]

With
\(\|\Lambda^{1/2}J_N^{-1/2}\|\le\sqrt{4N}\) and
\(\|J_N^{1/2}\Lambda^{-1/2}\|\le2^{1/4}\), including the
mean, sufficient full frame/inverse constants are

\[
u_N=2^{1/4}M_m,\qquad
F_N(T)=
\{u_N^2+(M_{\rm sh}u_N+\sqrt{4N}M_\mu)^2\}^{1/2},
\]
\[
I_N(T)=
\{4NM_\mu^2+\sqrt2M_m^2(1+M_{\rm sh}^2)\}^{1/2}.            \tag{W.21}
\]

Consequently, the actual amplitude evolution and its inverse on the
whole window \([-T,T]\) have bound

\[
C_N(T)=I_N(T)\mathfrak E_N(T)F_N(T),                       \tag{W.22}
\]

and the unchanged ordinary physical source-to-amplitude bound is

\[
S_N(T)=I_N(T)\mathfrak E_N(T).                             \tag{W.23}
\]

Both statements hold on all subintervals and in both directions. They
are not bounds for a separately normalized root or graph source.

## 6. The same complete phase and the same R46 remainder

The actual full strict phase and the canceled ordinary residual retain
their original bounds:

\[
H_*<2078931.088,\qquad
P_*=\int_{-r_c}^{r_c}\sup|P(mh_\sigma)|\,dr
 <11366470529343.                                         \tag{W.24}
\]

The second number already covers both halves and is not doubled again.
The smaller complete geometric whole-forward phase uses cancellation
with root counterterms; it cannot replace the individual strict
\(H_*\) in (W.24).

At the exact physical endpoint, retain the full scalar bounds

\[
D_*=\sup|m\mathcal F a/(2\mu)|,\qquad
L_*=\sup|C_c\mathcal F a/(2\mu^2)|.                        \tag{W.25}
\]

The latter is still a complex bound with \(C_c\); the real improvement
does not replace this factor. All its constituent fields are taken
from the unchanged last native closed cell.

For \(|s|\le S\), put \(T=S+2\), and define

\[
\begin{split}
d_{N,S}&=2^{3/4}M_{S+3/2,N}(D_*,X_f),\\
q_{N,S}&=4\,2^{1/4}\mathfrak C_N(S)
                    M_{S+3/2,N}(P_*,X),\\
a_{N,S}&=I_N(T)\mathfrak E_N(T)
             [d_{N,S}+q_{N,S}+F_N(T)]+1,\\
\ell_{N,S}&=2M_{S+3/2,N}(L_*,X)\mathfrak C_N(S),\\
Q_{N,S}&=2^{1/4}\sqrt{4N}\,\mathfrak C_N(S),\\
K_{N,S}&=8H_*Z_{\lceil S+2\rceil,1}(N,X),\\
X_{N,S}&=\sqrt{4N}
 [2^{1/4}X_{1,N,S}+2^{3/4}X_{h,N,S}].
\end{split}                                                \tag{W.26}
\]

Every entry is the original complete R46 term, evaluated at its
needed window. The momentum defect and the ordinary residual act at
physical order \(s+3/2\); the state correction is at \(s+2\).
The factor four in \(q_{N,S}\) pays all four branches. The
\(F_N(T)\) and final one in \(a_{N,S}\) keep the complete
\(\mathcal C_I\Pi_0-\Pi_0\), including all outputs of the mean input.
The factor eight in the ordering term retains the physical lag
\(4\ell\).

The same Duhamel, four-branch, cross-cone and ordering proof therefore
gives the complete bound

\[
\boxed{\|R_2:E_{s,N}\to E_{s+2,N}\|
 \le a_{N,S}+4[2X_{N,S}+\ell_{N,S}+Q_{N,S}K_{N,S}]}
\quad (|s|\le S).                                         \tag{W.27}
\]

The unchanged complete model also satisfies

\[
\|\mathcal W_0:E_{s,N}\to E_{s,N}\|
 \le\max\{1,Q_{N,S}[1+M_{d_S,N}(H_*,X)]\}.                \tag{W.28}
\]

No scalar mean phase, finite WKB head, smoothed reference, or new
boundary model enters (W.27).

## 7. Complete directed output and reproduction

The source is scripts/fourfold_strict_windowed_density_R46.py, SHA256
79dc3d8628fa34030d3310abfb73bcbbf928e49b3958c6720abfded8f299b96d.
The complete report is
notes/2026-11-13-R46-windowed-density-strong-budget.json, SHA256
bb8f8b4751f87f8a41ce219a8722fff5976ce233a009c90952682c3f2d24539b.
It ran at 320-bit directed precision in 3.86 seconds and recomputed zero
native cells. Its source and all input/dependency identities are saved.
Safe outward rounded values of (W.27) are:

| \(N\) | \(s=0\) | \(\lvert s\rvert\le4/3\) | \(\lvert s\rvert\le2\) | \(\lvert s\rvert\le8\) |
|---:|---:|---:|---:|---:|
| 4096 | \(4.650592\,10^{89}\) | \(1.004679\,10^{110}\) | \(2.046241\,10^{124}\) | \(8.986983\,10^{278}\) |
| 16384 | \(4.391774\,10^{85}\) | \(1.076346\,10^{103}\) | \(5.660609\,10^{114}\) | \(2.067431\,10^{242}\) |
| 65536 | \(5.469102\,10^{82}\) | \(6.042988\,10^{97}\) | \(2.614035\,10^{107}\) | \(6.785793\,10^{215}\) |
| 1048576 | \(3.776923\,10^{80}\) | \(1.715736\,10^{93}\) | \(1.199049\,10^{101}\) | \(3.069056\,10^{191}\) |

The saved report additionally gives every integer positive/negative
composition row, all inverse-Jacobian rows, both complete cross-cone
alternatives, all full phase/residual/mean terms, the exact interpolated
Cauchy window and the model norm.

At \(N=2^{20}\), the amplitude and source bounds (W.22)–(W.23) are:

| Uniform amplitude window \(\lvert s\rvert\le T\) | Amplitude and inverse | Ordinary physical source |
|---:|---:|---:|
| \(0\) | \(6.329524\,10^{50}\) | \(3.740767\,10^{46}\) |
| \(4/3\) | \(7.798358\,10^{59}\) | \(4.608316\,10^{55}\) |
| \(2\) | \(4.187533\,10^{65}\) | \(2.474150\,10^{61}\) |
| \(10/3\) | \(1.148708\,10^{77}\) | \(6.786132\,10^{72}\) |
| \(4\) | \(4.852161\,10^{83}\) | \(2.866033\,10^{79}\) |
| \(10\) | \(5.837423\,10^{166}\) | \(3.445096\,10^{162}\) |

Reproduce from the topic directory with a new output path:

~~~sh
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python3 scripts/fourfold_strict_windowed_density_R46.py \
  --scales 4096 16384 65536 1048576 \
  --windows 0 4/3 2 8 --bits 320 \
  --out /tmp/R46-windowed-density-independent.json
~~~

The producer refuses to overwrite an existing output. Comparing an
independent run should ignore only the elapsed-time field.

The remaining large constants are explicit upper bounds from the paid
base energy, density bootstrap, frame conversion and full residual.
They do not lower-bound the actual evolution. Neither a larger \(N\)
nor this narrower bookkeeping proves a small high feedback block by
itself. The actual returned operator still requires its complete root,
positive-cap, source and independent regular-port composition.
