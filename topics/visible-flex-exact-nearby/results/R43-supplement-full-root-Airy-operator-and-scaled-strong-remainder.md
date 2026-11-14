# R43 supplement: both Airy rows and the full strong root remainder

This note completes the actual old operator on the whole constant-canonical
interval \(0\le\xi\le L=1/4000\). The preceding complete seven-field
calculation supplies the true potential on this entire collar. The present
consumer pays the higher Sobolev commutators, both Cauchy rows, the full
ordinary canonical source, the exact change back to the original R39
frame, and the original R43 first phase with a complete \(4/3\)-order
remainder.

Every frequency, including the mean, remains in the evolution. The scaled
norms used below do not truncate the equation or discard paths through the
finite head. The actual physical cut is a nonconstant graph strictly below
\(L\); its strong trace connector is a separate remaining interface.

For example, at the norm scale \(N=65536\), uniformly in the whole actual
parameter interval,

\[
 \|C_0(\xi,\eta)\|_{E_N^s\to E_N^s}<2.830691\,10^{11},
 \qquad |s|\le10,\quad \xi,\eta\in[0,L],                    \tag{A.1}
\]

\[
 C_0(L,0)=I+B_{\rm original}+R,\qquad
 \|R:E_N^s\to E_N^{s+4/3}\|<9.595498\,10^{24},
 \qquad |s|\le8.                                          \tag{A.2}
\]

Here \(C_0\) is in the original, unshifted R39 Airy frame. No different
phase or mean replaces \(B_{\rm original}\). The ordinary canonical source
map from \(L^1_\xi H_N^{s-1/3}\) to \(E_N^s\) has norm
\(<2.676923\,10^8\). These are explicit finite bounds, not a small-feedback
or final-cutoff claim.

## 1. The complete actual input and the norm scale

The input is the corrected complete canonical-domain report

    notes/2026-11-13-negative-root-full-canonical-domain.json
    SHA256 e511da0be8da1f489769ed65a948438b6aab6bd059b442b7195a303ec4b42d8e

It proves

\[
 |V|\le M_V<752813.541687
\]

on

\[
 \operatorname{dist}(\xi,[0,L])\le10^{-5},\qquad
 |\Im\phi|\le\sigma=1/40000.
\]

The bound

\[
 |V_\xi|\le M_{\xi}<7.528135416868\,10^{10}                 \tag{A.3}
\]

is used only for real \(\xi\in[0,L]\), still on the full complex
angle strip. No radial derivative bound at the halo boundary is assumed.
The actual canonical quarter-circle frequency satisfies

\[
 38.883851605869<q<38.883851623093.
\]

Put \(x=q\phi\), so \(x\) has period \(2\pi\), and define, for every
integer \(N\ge1\),

\[
 \|u\|_{H_N^s}^2=\sum_{n\in\mathbb Z}
       (1+n^2/N^2)^s|u_n|^2,\qquad E_N^s=(H_N^s)^2.        \tag{A.4}
\]

This is a norm on the entire Fourier sequence. In particular it retains
all \( |n|<N\), every mean/nonmean coupling, and every crossing through
that head.

Use the exact radial reference \(v=5050\), and set \(W=V-v\). The
complete residual bound is

\[
 |W|\le M_W=M_V+5050<757863.541687.
\]

With \(a=q_-\sigma\), Cauchy gives the complete physical-to-normalized
angle conversion

\[
 D_0=M_W,\qquad
 D_j=\frac{j!M_V}{a^j}\quad(1\le j\le11).                 \tag{A.5}
\]

Thus \(\|\partial_x^jW\|_\infty\le D_j\) for every real radial
point. The same list also bounds \(V\), since \(D_0\ge M_V\) and
the positive-order derivatives agree. This observation is used when
returning to the original R43 amplitude system.

## 2. A complete triangular height resolvent

Let \(G_v(t,s)\) be the exact Fourier-diagonal initial-value Green
operator of

\[
 y_n''+(q^2n^2t+v)y_n=0.
\]

The preceding potential note proves, for every mode including zero,

\[
 |G_v(t,s;n)|\le |t-s|.                                  \tag{A.6}
\]

The estimate holds in both time directions by antisymmetry. It follows
from the nonincreasing Sonin energy for
\(Q(t)=v+q^2n^2t>0\), not from a finite-frequency sample.
Write \(\eta=L^2/2\). The complete scalar Volterra diagonal is

\[
 q_0=\eta D_0<.023683235678<1/40.                         \tag{A.7}
\]

For \(0\le j,\ell\le11\), define the nonnegative lower-triangular
matrix

\[
 T_{j\ell}=
 \begin{cases}
 \binom j\ell D_{j-\ell}N^{-(j-\ell)},&\ell\le j,\\
 0,&\ell>j .
 \end{cases}                                             \tag{A.8}
\]

For integer \(k\), let
\(W_k=\operatorname{diag}_{0\le j\le k}\sqrt{\binom kj}\).
The exact binomial identity is

\[
 \|u\|_{H_N^k}^2
  =\sum_{j=0}^k\binom kj N^{-2j}\|\partial_x^ju\|_2^2.
                                                               \tag{A.9}
\]

Leibniz and (A.5) therefore give the pointwise multiplier bound

\[
 M_k=\|W_kT^{[k]}W_k^{-1}\|_2                            \tag{A.10}
\]

for either \(W\) or \(V\). The executable uses the lesser of the
complete Schur row/column bound and the Frobenius bound, with directed
upper endpoints.

For the true mild equation

\[
 u=h-\int G_v(t,s)W(s)u(s)\,ds,                           \tag{A.11}
\]

let \(e_j=N^{-j}\|\partial_x^ju\|_{L^\infty_tL^2_x}\).
The complete derivative inequalities give

\[
 e\le h_{\rm der}+\eta Te.
\]

Only the diagonal of this triangular comparison needs to be small.
The exact nonnegative inverse \(R_T=(I-\eta T)^{-1}\) is obtained
recursively as

\[
 (R_T)_{j\ell}=
 \frac{\delta_{j\ell}+
       \eta\sum_{b=\ell}^{j-1}T_{jb}(R_T)_{b\ell}}
      {1-\eta D_0}.                                      \tag{A.12}
\]

The higher derivatives occur in finitely many triangular products;
they are not put in a repeated high-order Gronwall exponential.

To pass between the vector of separate derivative time norms and the
ordinary Bochner norm, include the explicit factor \(\sqrt{k+1}\).
Thus a complete height-resolvent bound is

\[
 R_k=\sqrt{k+1}\,
       \|W_kR_T^{[k]}W_k^{-1}\|_2.                        \tag{A.13}
\]

For \(L^\infty_t H_N^k\), the output norm is at most the weighted
vector norm, while the input derivative vector is at most
\(\sqrt{k+1}\) times its ordinary Bochner norm. This pays the
otherwise invalid interchange of a time supremum and a sum of squares.

For negative orders, take the time-space adjoint of (A.11). Its Volterra
kernel is backward and multiplication by the same real \(W(s)\) is
outside the Green integral. The bound (A.6) has column integral at most
\(\eta\), so the identical matrix \(T\) controls
\(N^{-j}\|\partial_x^ju\|_{L^1_tL^2_x}\). In this case

\[
 \|u\|_{L^1H_N^k}
 \le\sqrt{k+1}\,\|(\sqrt{\binom kj}e_j)_{j=0}^k\|_2,
\]

whereas the corresponding input vector norm is no larger than
\(\|h\|_{L^1H_N^k}\). The same factor in (A.13) suffices.
Duality yields the claimed \(L^\infty H_N^{-k}\) resolvent.
Multiplier bounds at negative orders follow from the ordinary
self-adjoint multiplier duality.

Interpolation fills all real orders in \([-11,11]\). One can verify this
directly on smooth finite-support test data by inserting the Fourier
multiplier \(\langle D/N\rangle^{z}\) and applying the three-lines
inequality to the scalar pairing at each output time. The boundary
estimates are the already established Bochner bounds. Taking the
time supremum and then completing the Fourier sequences gives the
stated bound; the finite-support tests are a density argument, not a
change of the evolved operator.

Consequently set

\[
 M=\max_{0\le k\le11}M_k,\qquad
 R_H=\max_{0\le k\le11}R_k.                               \tag{A.14}
\]

Both are full operator constants. At \(N=65536\),
\(M<835983.969089\) and \(R_H<3.557026626\).

## 3. Both exact shifted-Airy columns, including the mean

Let

\[
 c=\sqrt{\operatorname{Ai}(0)/[-\operatorname{Ai}'(0)]},
 \quad \lambda=q|n|,\quad
 z_n(t)=-\lambda^{2/3}t-v\lambda^{-4/3}.
\]

For \(n\ne0\), choose

\[
 D_\pm^v(t,n)=c\lambda^{-1/3}
       [\operatorname{Bi}(z_n(t))\pm i\operatorname{Ai}(z_n(t))].
                                                               \tag{A.15}
\]

For the mean choose

\[
 D_\pm^v(t,0)=
 c\left[\cos(\sqrt v\,t)
       \pm i\frac{\sin(\sqrt v\,t)}{\pi\sqrt v}\right].
                                                               \tag{A.16}
\]

Their complete Cauchy matrix
\(F_v=(D_+^v,D_-^v;\partial_tD_+^v,\partial_tD_-^v)\)
has the same exact Wronskian

\[
 \det F_v=-2ic^2/\pi                                     \tag{A.17}
\]

at every frequency, including zero. Thus no limiting nonzero-frequency
formula is used at the mean. The true equation still couples this mean
to the other frequencies through \(W\).

The negative-real-axis Airy bounds proved in R39 give

\[
 C_D=10c\max(1,2^{1/6}q_-^{-1/3}),\qquad
 C_G=\max(L,50\pi2^{1/3}q_-^{-2/3}),                      \tag{A.18}
\]

as bounds respectively for
\(D_\pm^v:H_N^s\to H_N^{s+1/3}\) and
\(G_v:H_N^s\to H_N^{s+2/3}\).
They hold for all \(N\ge1\); the reference is Fourier diagonal.
The inverse momentum-source column of (A.17) has bound

\[
 \Gamma=\frac{\pi C_D}{\sqrt2c^2}
 \quad\text{from }H_N^{s-1/3}\text{ to }E_N^s.             \tag{A.19}
\]

For \(|s|\le10\), all height and source orders lie in the paid
\([-11,11]\) window. The mild height solution satisfies

\[
 \sup_t\|u(t)\|_{H_N^{s+1/3}}
 \le R_H\left(\sqrt2C_D\|z_v(\eta)\|_{E_N^s}
                 +C_G\|f\|_{L^1H_N^{s-1/3}}\right).
                                                               \tag{A.20}
\]

Use the exact, complete amplitude identity

\[
 \partial_tz_v=F_v^{-1}(0,f-Wu)^t.                       \tag{A.21}
\]

It retains both momentum rows and every mean/cross-frequency term.
Combining (A.19)–(A.21) gives

\[
 C_v=1+\Gamma LMR_H\sqrt2C_D,\qquad
 S_v=\Gamma(1+LMR_HC_G).                                 \tag{A.22}
\]

These bound the homogeneous propagation and ordinary canonical source
map, respectively. The same argument starts at either endpoint of any
subinterval; (A.6) is symmetric and all reference columns are bounded on
the same whole interval. Hence \(C_v\) also bounds every inverse.

For completeness the executable pays explicit natural two-row endpoint
frames. Set

\[
\begin{split}
 C_{P,0}&=10c\max\left(\pi^{-1},
              (q_+N)^{1/3}+v^{1/4}\right),\\
 C_P&=10c\max\left(vL+\pi^{-1},
              (q_+N)^{1/3}+v^{1/4}
                      +L^{1/4}(q_+N)^{1/2}\right),\\
 C_H&=10c\max(1,2^{1/4}L^{-1/4}q_-^{-1/2}).
\end{split}                                               \tag{A.23}
\]

At the root the target is
\(H_N^{s+1/3}\oplus H_N^{s-1/3}\); at \(L\) it is
\(H_N^{s+1/2}\oplus H_N^{s-1/2}\). Complete frame and inverse
bounds are

\[
\begin{array}{ll}
 B_0=\sqrt{2(C_D^2+C_{P,0}^2)},&
 I_0=\dfrac{\pi}{\sqrt2c^2}\sqrt{C_D^2+C_{P,0}^2},\\[2mm]
 B_L=\sqrt{2(C_H^2+C_P^2)},&
 I_L=\dfrac{\pi}{\sqrt2c^2}\sqrt{C_H^2+C_P^2}.
\end{array}                                               \tag{A.24}
\]

The \(N\)-factors in (A.23) are necessary for the negative-order momentum
slots; they have not been omitted by calling the norms scaled.
These are the entire \((u,u_\xi)\) frames, not height-only estimates.

## 4. Return exactly to the original R39 frame

Let \(F_0\) be the original R39 frame, with its original mean columns.
At every time and frequency,
\(M(t)=F_0(t)^{-1}F_v(t)\) is exact. The products of the full Airy
function and derivative bounds give

\[
 \|M(t)\|,\ \|M(t)^{-1}\|
 \le C_{\rm ch}:=
 \max\left\{
 100\pi\left[1+(1+vq_-^{-4/3})^{1/4}\right],
 2(1+L/\pi)(1+\pi vL/2)
 \right\}<1100.925158.                                   \tag{A.25}
\]

The second expression is the separately calculated mean matrix.
For the first, if \(a=\lambda^{2/3}t\) and
\(b=v\lambda^{-4/3}\), the only derivative-to-height ratio is bounded by
\(((1+a+b)/(1+a))^{1/4}\le(1+vq_-^{-4/3})^{1/4}\);
the reverse ratio is at most one. The two products in each inverse
matrix entry, its exact Wronskian and the two-by-two operator norm
give (A.25). The same computation with the factors exchanged bounds
the inverse. These diagonal Fourier changes have the same norm on
every \(E_N^s\).

It follows that the original amplitudes have

\[
 C_f=C_{\rm ch}^2C_v,\qquad S_f=C_{\rm ch}S_v.             \tag{A.26}
\]

This change is applied at both ends of a homogeneous propagation and
at the output of a source solution. It does not reset the old phase,
alter the actual potential, or discard an initial-frame defect.
Equations (A.22)–(A.26) prove (A.1) and its stated source bound.

## 5. The original first phase and complete strong remainder

The original full R39 amplitude equation is
\(z_0'=\mathcal K_0z_0+\Gamma_0f\). We now estimate its actual Dyson
identity directly. The shifted reference is used only for the complete
propagator constant \(C_f\).

The first R43 matrix \(B_{\rm original}\) is unchanged:

\[
 a_{\sigma\epsilon}(\phi)=\frac1{2q}\int_0^L
 \frac{V(\xi,\phi-\sigma\epsilon\,2\xi^{3/2}/3)}
      {\sqrt\xi}\,d\xi,
\]

\[
 A_\sigma=\sum_{\epsilon=\pm1}
   \Pi_\epsilon D^{-1/2}M_{a_{\sigma\epsilon}}
                          D^{-1/2}\Pi_\epsilon,\qquad
 B_{\rm original}=i\operatorname{diag}(A_+,-A_-).          \tag{A.27}
\]

As in R43, \(D^{-1/2}\) is zero on the mean only in this specified
first-phase expression. The actual mean propagation, the cross-sign
blocks and all remaining mean couplings stay in the full remainder.

The complete entrywise first-Dyson estimate of R43 is

\[
 |(T_1-B_{\rm original})_{\sigma\tau;kj}|
 \le C_q\langle k-j\rangle^{4/3}
              (v_{k-j}+v^{(1)}_{k-j})\langle j\rangle^{-4/3},
                                                               \tag{A.28}
\]

including the cases \(j=0\), \(k=0\) and opposite frequency signs.
Here \(v_l,v_l^{(1)}\) are the true suprema in (A.3), and

\[
 C_q=4(50\pi+5)q_-^{-4/3}+150\pi+3/q_-<476.237535.
\]

The proof of (A.28) only uses \(L\le1\) and the complete potential
and derivative bounds. Its first-Dyson calculation does not require
a small same-order Volterra norm.

For \(l=k-j\), the scaled weights obey

\[
 \frac{\langle k/N\rangle^{s+4/3}}
      {\langle j/N\rangle^{s}}\langle j\rangle^{-4/3}
 \le(1+|l|/N)^{|s+4/3|}.
                                                               \tag{A.29}
\]

The last input factor is at most one because
\(\langle j/N\rangle\le\langle j\rangle\).
For \(|s|\le8\), use exponent \(10\) in (A.29), which is larger
than \(|s+4/3|\). Complete analyticity gives

\[
 v_l+v_l^{(1)}\le(M_V+M_\xi)e^{-a|l|}.                   \tag{A.30}
\]

Define the entire sums

\[
\begin{split}
 A_0(N)&=\sum_{l\in\mathbb Z}(1+|l|/N)^{10}e^{-a|l|},\\
 A_2(N)&=\sum_{l\in\mathbb Z}(1+|l|/N)^{10}
                                      (1+l^2)e^{-a|l|}.
\end{split}
\]

Hölder with this positive measure yields

\[
 \sum_l(1+|l|/N)^{10}\langle l\rangle^{4/3}e^{-a|l|}
 \le A_0(N)^{1/3}A_2(N)^{2/3}=:\mathcal L_N.              \tag{A.31}
\]

The executable evaluates both complete sums through positive
Stirling/geometric formulas, to power twelve. There is no truncated
tail and the \(4/3\) power is not rounded up to two. The two branch
rows and columns in (A.28) then give

\[
 F_N=2C_q(M_V+M_\xi)\mathcal L_N.                         \tag{A.32}
\]

For the second and all higher Dyson terms, the exact R42 integrable
one-gain estimate works in the same scaled spaces:

\[
 \|\mathcal K_0(\xi):E_N^s\to E_N^{s+1}\|
 \le B_N\xi^{-1/2},\qquad
 B_N=100\pi\max_{0\le k\le10}M_k.                        \tag{A.33}
\]

The required multiplication orders \(s+1/2\) and \(s+3/2\) lie in
\([-10,10]\). The same \(T\) already bounds \(V\).
The condition \(q_->4\) pays the harmless frequency factor in R42.

Use the exact twice-iterated Volterra identity

\[
 C_0(L,0)-I-T_1=
 \int_{0<t_1<t_2<L}
       \mathcal K_0(t_2)\mathcal K_0(t_1)C_0(t_1,0)
       \,dt_1dt_2 .
\]

The rightmost full propagator uses \(C_f\) only in its input order.
The other two factors each gain one full derivative. The scalar
ordered integral is \(2L\), exactly as in R42. Consequently

\[
 \|C_0-I-T_1:E_N^s\to E_N^{s+2}\|
       \le2C_fLB_N^2.                                    \tag{A.34}
\]

All intermediate orders are within the declared window.
Embedding the output by \(2/3\) of a derivative now gives the complete
strong constant

\[
 \boxed{R_N=F_N+2C_fLB_N^2.}                              \tag{A.35}
\]

This proves (A.2) on the whole actual collar, without imposing the
previous tiny-\(\delta\) same-order gate. It does not replace
\(I+B_{\rm original}\) by \(e^B\) without paying its second-order
difference.

## 6. Full head preservation and conversion back to ordinary Sobolev norms

At this stage every operator acts on every Fourier mode. Let \(P_{\ge N}\)
be applied only to the final input and output. For \(|n|\ge N\),

\[
 1\le\frac{N\langle n/N\rangle}{\langle n\rangle}\le\sqrt2.
\]

For \(|s|\le8\), this gives

\[
 \|P_{\ge N}R P_{\ge N}:E^s\to E^{s+4/3}\|
       \le16N^{4/3}R_N.                                  \tag{A.36}
\]

The factor \(16\) bounds the remaining powers of the ratio above
through the entire window. The operator between the projections in
(A.36) is the full one: high-to-head-to-high paths remain.
For the full unprojected ordinary Sobolev map a safe uniform conversion is

\[
 \|R:E^s\to E^{s+4/3}\|\le N^{28/3}R_N.                 \tag{A.37}
\]

This also keeps every input or output in the head.

Some directed numerical bounds are:

| Norm scale \(N\) | Height resolvent \(R_H\) | Original amplitude \(C_f\) | Scaled strong \(R_N\) | Ordinary projected strong bound (A.36) |
|---:|---:|---:|---:|---:|
| \(1\) | \(<5.911631\,10^{39}\) | \(<2.308628\,10^{91}\) | \(<1.497404\,10^{178}\) | \(<2.395846\,10^{179}\) |
| \(4096\) | \(<10.381872\) | \(<3.617022\,10^{13}\) | \(<4.748088\,10^{29}\) | \(<4.978731\,10^{35}\) |
| \(16384\) | \(<3.599264\) | \(<4.118180\,10^{11}\) | \(<2.676750\,10^{25}\) | \(<1.782192\,10^{32}\) |
| \(65536\) | \(<3.557027\) | \(<2.830691\,10^{11}\) | \(<9.595498\,10^{24}\) | \(<4.056587\,10^{32}\) |

The norm scale is not a final feedback cutoff. In particular (A.36)
does not certify a finite Schur complement, absorb its remaining
feedback, or replace a true phase by its average.

## 7. Executed consumer, reproduction and remaining interface

The complete new files are

- scripts/fourfold_negative_root_full_Airy_operator.py;
- notes/2026-11-13-negative-root-full-Airy-operator.json;
- this proof.

The report SHA256 is

    4a84d560b61efbd3abc44566fe9ae201a7677682a8de7e1062e2c2fc97a8138d

From the topic directory, using python-flint 0.9.0, reproduce with a
fresh output path:

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python3 scripts/fourfold_negative_root_full_Airy_operator.py \
      --out /tmp/negative-root-full-Airy-operator-recheck.json

The consumer checks the true input producer hash, all input identities
and complete gates, uses 320-bit directed arithmetic, retains both
twelve-by-twelve comparison matrices for each scale, and reports every
integer multiplier/resolvent and every full source/frame constant. The
executed calculation took about .707 seconds. Run time and output path
may change a newly generated report digest; all mathematical constants
are determined by the checked input.

The exact physical cut graph
\(\chi_p(\phi)\in(.000240160024215254,.000248188362538822)\)
lies strictly inside this paid collar. Equations (A.1)–(A.37) establish
the root-to-constant-section operator. They do not yet turn evaluation
on that graph into a bounded strong trace map. The nonconstant graph
requires its actual two-row conormal, angle and height conversions;
the ordinary physical source requires the corresponding density
conversion. The positive Ai/contact network, full returned phase
\(b-\beta\), complete returned \(R_*\), head Schur matrix and the
final effective cutoff remain explicit further obligations.
