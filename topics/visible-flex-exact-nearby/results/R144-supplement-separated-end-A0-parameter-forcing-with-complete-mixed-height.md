# R144 GA: separated-end A0 parameter forcing with the complete mixed height

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all 16 new exact rational and integer comparisons pass.**
For the actual S/T family at one fixed physical nonmean coordinate \(w\),
\[
 \|D_\gamma{\cal F}_\gamma(w)[\eta]\|_{Z_{1794}^{[3]}}
   <2^{-48000000}r_\gamma^{-1}\|\eta\|_{A^0}.
\]
The complete high-source window is \(20\le s\le2898\), with one high
background \(W_{s+1}\), where \(W_j=\|w\|_{E_j^+}\). The derivative is
jointly continuous in operator norm \(A^0\to Z_s^{[3]}\) when gamma
varies in \(A^0\) within its original value domain and \(w\) varies in
the common \(E_{2960}^+\) graph. The proof keeps the full mixed
far-height dependence, the actual seed parameter, its radial first
compensation, the infinite first-principal response, all original
source units, and the complete ordinary holonomy-mean source.

The independent reference-height integral is retained separately. It
is not included in a source bound which vanishes at zero nonmean state.

## Completed inputs and the distinction from a small-value argument

The inputs are:

- [GF: complete actual parameter forcing](R144-supplement-complete-parameter-forcing-for-the-selected-exact-tail-family.md), including GF.4, GF.15--GF.29 and its original complete source budgets;
- [T: the actual selected family](R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md), especially T.C.1--T.C.14 and section 5;
- [S: the exact far graph and complete graph Nash construction](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md), especially S.3--S.16;
- [M: the complete two-input zero-width cap](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md), especially M.3--M.7;
- [RG: the rough-inner-input seed and genuine separated-end module](R119-supplement-rough-inner-curvature-data-and-true-smoothed-B-seed.md), especially RG.17--RG.22 and RG.30;
- [the actual nonlinear long screening module](R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md);
- [L: the real low-norm principal value construction](R119-supplement-low-norm-principal-Gamma-map-and-tame-high-conjugacy.md), especially L.9--L.17;
- [E: the complete reference graph and exact residual](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md);
- [G: the full first-principal physical metric source](R119-supplement-low-direction-first-Gamma-projected-metric-source-and-linear-Schur.md);
- [Qmet: the complete ordinary source and reference-height lift](R119-supplement-exact-nonlinear-ordinary-sources-and-Gamma-reference-height-lifts.md).

The new estimate is not obtained by differentiating a small real value
bound. We first differentiate the actual finite-long contraction with
respect to its cap-end input. Then a qualified Banach Cauchy estimate
for the actual cap map supplies the gamma direction. The complete
mixed height kernel is recovered by auxiliary analytic probes of the
far input only; the actual unknown inputs need no spatial strip.

## 1. Domain and the permitted analytic probes

Keep GF.1 and its real-even physical nonmean \(4\mathbb Z\) domain:
\[
 r_\gamma=10^{-9},\quad
 \|\gamma/r_\gamma\|_{A^0}\le1/128,\quad
 \|\gamma/r_\gamma\|_{H^{8193}}\le2^{1048576}.
\]
Use the same common physical reference, the same fixed linear boundary
space, and the same small background condition
\[
 W_{1856}\le2^{-49000000},\qquad
 \epsilon=\epsilon_L=e^{-7L/4}<2^{-57000000}.
\]
For the endpoint calculation put
\[
 G=\gamma/r_\gamma,\qquad
 U=|D_\theta|^2f/r_B,\qquad e=\eta/r_\gamma,\qquad
 r_B=2^{-60},\quad r_f=10^{-8},\quad f=F_Bw .
\]
These are actual normalized inputs. The physical endpoint height is
still scaled by the original \(s_B\); no curvature input is renamed as
a height.

M.3 constructs the complete cap map on the complex product
\(\|\gamma\|_{A^0}<r_\gamma\),
\(\|f\|_{\dot A^2_0}<r_B\), and M.7 bounds its actual right-end output
by \(r_f\) in \(\dot A^2_0\).
For a Taylor coefficient calculation only, allow the far datum \(f\)
to lie in \(\dot A^2_\sigma\), with the same bound \(r_B\), for
\(0\le\sigma\le1\). At the cap end keep width zero.

On the long segment use
\[
             \sigma(t)=\sigma(1-t/L),\qquad
             \alpha=\sigma/L<1/32.                            \tag{GA.1}
\]
The inequality follows from the already proved \(L>23000000\).
These are exactly the variable-width domains in RG.17--RG.20.
The proof of that module depends on \(\alpha\) only through its displayed
upper bound, so the same complete finite Green estimate \(<320\),
two-end lift bound 16, and nonlinear derivative bound \(5/8\) apply
for every \(\sigma\) in (GA.1).

All right-end data, including the unknown gamma and the actual output
of the cap map, remain zero-width. The auxiliary strip is used to test
Taylor coefficients in the far-height slots. It is not assumed for
the physical \(f\) at which the final estimate will be applied.

## 2. Differentiate the actual long module first

Fix both actual boundary values in their stated domains and vary only
the cap-end datum \(g\), with the left datum \(f\) held fixed.
Differentiating the original two-end fixed-point equation gives
\[
 \|\dot h\|_{{\cal Y}_{\sigma,7/4}}
 \le16\|\dot g\|_{\dot A^2_0}
                  +\frac58\|\dot h\|_{{\cal Y}_{\sigma,7/4}},
 \qquad
 \|\dot h\|_{{\cal Y}_{\sigma,7/4}}
                  \le\frac{128}{3}\|\dot g\|_{\dot A^2_0}.
                                                                    \tag{GA.2}
\]
Here the distinguished direction carries the additional radial
difference weight \(e^{(7/4)(L-t)}\); the entire nonlinear background
is not assumed to carry that weight. All complete cap--long reflections
are part of the differentiated contraction.

The original mean small-root equation gives, for this same variation,
\[
 \|\dot\kappa\|_{C^0_{7/4}}\le\frac1{24}\|\dot g\|_{\dot A^2_0}.
\]
At the left endpoint the height variation is zero. Reading its true
nonmean slope and its mean gives
\[
 \|D_g{\cal K}(f,g)[\dot g]\|_{\dot A^1_\sigma\oplus\mathbb C}
 \le\left(\frac{128}{3}+\frac1{24}\right)
                   \epsilon\|\dot g\|_{\dot A^2_0}
 <44\epsilon\|\dot g\|_{\dot A^2_0}.                            \tag{GA.3}
\]
The norm in this formula includes the scalar mean. It is not a projection
of the full output before differentiation.

For \(\|G\|_{A^0}\le1/128\), a complex gamma direction circle of
normalized radius \(1/2\) lies inside M.3 for every allowed \(f\).
The actual holomorphic cap map and its uniform \(r_f\) bound therefore
give
\[
 \|D_G\Phi_{r_\gamma G}(f)[e]\|_{\dot A^2_0}
                      \le2r_f\|e\|_{A^0}.
\]
Define the complete endpoint operator
\[
 {\cal A}_G(U)[e]=
 D_G\left\{{\cal K}\left(r_B|D_\theta|^{-2}U,
       \Phi_{r_\gamma G}(r_B|D_\theta|^{-2}U)\right)\right\}[e].
                                                                    \tag{GA.4}
\]
Its nonmean part is exactly \(D_\gamma q_\gamma(f)[\eta]\).
The pure long self term and the fixed \(\mathsf C_Lf\) have zero gamma
derivative. By (GA.3),
\[
 \|{\cal A}_G(U)[e]\|_{\dot A^1_\sigma\oplus\mathbb C}
       \le88r_f\epsilon\|e\|_{A^0}
       <2^8\epsilon\|e\|_{A^0},
 \qquad \|U\|_{A^0_\sigma}<1.                                 \tag{GA.5}
\]
This is a genuine derivative bound on a qualified full product domain.

Only the left slope and its mean have the screening factor in (GA.3).
The independent long mean-height span in M.7/RG.30 is not assigned the
same factor. The metric reference-height term is retained separately
as in GF.24.

## 3. The complete mixed frequency kernel

For fixed \(G\), expand the holomorphic operator in the far input:
\[
 {\cal A}_G(U)=\sum_{d\ge0}{\cal A}_{d,G}(U,\ldots,U).
\]
The symmetric multilinear coefficients include their Taylor factorials.
Cauchy on the unit \(U\)-ball and the polarization factor
\(d^d/d!\le e^d<4^d\) give their operator norm at most
\(4^d M\), where \(M=2^8\epsilon\).

Use normalized cosine modes in the complex-even space, retaining both
signed Fourier coefficients of every cosine. No extension of the
seed's even parameter theorem to an unproved odd space is needed.
For an output frequency \(m\in4\mathbb Z\), write
\(a_m=\max(1,|m|)\); the zero mode is the mean output.
Absorb \(a_m\) into the scalar kernel coefficient
\(K_{d,G}(m;n_1,\ldots,n_d)[e]\).
The zero-width and width-one versions of (GA.5), on the same normalized
input modes, give
\[
 \begin{split}
 \sum_m|K_{d,G}(m;\mathbf n)[e]|
              &\le M4^d\|e\|_{A^0},\\
 \sum_m e^{\,|m|-\sum_{\ell=1}^d|n_\ell|}
             |K_{d,G}(m;\mathbf n)[e]|
              &\le M4^d\|e\|_{A^0}.
 \end{split}                                                   \tag{GA.6}
\]
These are coefficients of the same zero-width map. Finite Fourier
probes with sufficiently small amplitudes belong to both domains, so
uniqueness of the actual cap and long solutions identifies the Taylor
coefficients. The use of different auxiliary norms does not construct
different maps.

Combining the two inequalities yields
\[
 \sum_m
 e^{\,\left(|m|-\sum_\ell|n_\ell|\right)_+}
 |K_{d,G}(m;\mathbf n)[e]|
                  \le2M4^d\|e\|_{A^0}.                       \tag{GA.7}
\]
The gamma direction has no frequency moment on the right. Output
frequencies can be paid either by the actual far-height input
frequencies or by the positive excess in (GA.7).

This assertion is uniform for one arbitrary complete direction \(e\).
It is not the unsupported claim that the sum over output frequencies
of separate operator norms is bounded. The proof first tests one \(e\),
takes the complete output sum, and only then uses the uniform bound
\(\|e\|_{A^0}\). The subsequent convolution estimate retains that order.

Likewise, no complex angular translation of a fixed rough gamma is
used. The output width follows from the actual separated-end long
module with an analytic far probe and a zero-width cap-end datum.

## 4. Sum every mixed degree with one high far-height factor

For the actual zero-width input set
\[
 b_n=\sum_{k\ne0}|k|^n|U_k|,\qquad b_0\le1/16,\qquad n=s+1.
\]
The mean output is retained even though the input has no zero mode.
For one kernel tuple put
\[
 B=\sum_{\ell=1}^d|n_\ell|,\qquad \lambda=(|m|-B)_+ .
\]
Then
\[
 \begin{split}
 (1+|m|)^n
 &\le3^{n-1}\{1+B^n+\lambda^n\},\\
 B^n&\le d^{\,n-1}\sum_{\ell=1}^d|n_\ell|^n,\qquad
 \lambda^ne^{-\lambda}\le n!.
 \end{split}
\]
The last inequality follows directly from the exponential series.
The terms \(d=0\) and \(m=0\) are covered by the constant and excess
terms; neither is omitted.

With \(x=4b_0\le1/4\), the exact degree sums satisfy
\[
 \sum_{d\ge0}x^d\le4/3,\qquad
 \sum_{d\ge1}4^d d^n b_0^{d-1}
 \le4n!(1-x)^{-n-1}\le2^{n+3}n!.
\]
For example \(d^n\le n!\binom{d+n-1}{n}\) proves the middle bound.
Thus the highest far input is paid once, by \(b_n\); all other far
factors are paid by \(b_0\).

Finally
\(\langle m\rangle^{s+2}/a_m
 \le2^{s+2}(1+|m|)^{s+1}\).
Combining this with (GA.7) and the preceding sums gives
\[
 \|{\cal A}_G(U)[e]\|_{H^{s+2}}
 \le2^{4s+24}(s+1)!\epsilon(1+b_{s+1})\|e\|_{A^0}
 \le2^{65536}\epsilon(1+b_{s+1})\|e\|_{A^0},
 \quad20\le s\le2898 .                                       \tag{GA.8}
\]
This was proved in a stronger weighted absolute Fourier sum before
passing to \(H^{s+2}\). For the last inequality,
\((s+1)!<2^{12(s+1)}\), since \(s+1\le2899<4096\), and
\(16s+36\le46404<65536\).

The Taylor series converges at the actual \(b_0\le1/16\). The absolute
kernel majorant controls the entire sum and hence gives its actual
strong Sobolev output. This is not a finite Taylor truncation. Every
mixed \(f_{\rm high}\) term remains in (GA.8).

In the original physical units,
\[
 \begin{split}
 b_{s+1}
 &=r_B^{-1}\|f\|_{\dot A^{s+3}}
 \le r_B^{-1}\|f\|_{H^{s+4}}
 \le2^{-380}W_{s+1}.
 \end{split}                                                   \tag{GA.9}
\]
The first Sobolev comparison uses
\(\sum_{k\in4\mathbb Z\setminus\{0\}}\langle k\rangle^{-2}<1\).
The last comparison uses exactly the real added trace in \(E_{s+1}^+\),
with its coefficient \(2^{440}\). The condition on \(b_0\) follows
from the same low trace and \(W_{20}\le2^{-49000000}\).

Apply \(P_\perp\) only now and use the actual S.12 lift. Because
\(65536+2048<131072\),
\[
 \boxed{\quad
 \|D_\gamma{\cal U}_\gamma(w)[\eta]\|_{E_s^+}
 \le2^{131072}\epsilon(1+W_{s+1})
                         \|\eta/r_\gamma\|_{A^0},
 \quad20\le s\le2898 .
 \quad}                                                       \tag{GA.10}
\]
The lift retains its real five-jet support and all original radial
source units. The complete mean-root derivative is recovered in the
ordinary residual calculation; it has not been discarded by using
a nonmean coordinate.

## 5. Joint continuity of the full endpoint operator

The preceding estimates also hold uniformly on the slightly larger
normalized gamma ball \(\|G\|_{A^0}\le1/32\). An additional gamma
difference uses a qualified Cauchy derivative in that same complete
product, with a fixed finite factor at most 4 in the kernel estimate.

For a far-height difference, telescope each full \(d\)-linear term by
replacing one far input at a time. The extra degree factor is paid by
the same sum with moment order \(n+1\). All remaining low factors are
still bounded by a number strictly below the convergence radius.
The highest difference may occur either in the distinguished slot or
in one unchanged background slot, giving
\[
 \begin{split}
 &\|{\cal A}_G(U)-{\cal A}_{G'}(U'):
                       A^0\longrightarrow H^{s+2}\|\\
 &\quad\le2^{131072}\epsilon
 \big\{\|U-U'\|_{\dot A^{s+1}}
  +(1+b_{s+1}+b'_{s+1})
       [\|U-U'\|_{A^0}+\|G-G'\|_{A^0}]\big\},
 \quad20\le s\le2898 .                                       \tag{GA.11}
 \end{split}
\]
For \(s+2\le2900\), the added factorial factor costs at most another
12 bits per extra moment, and the finite polarization/difference
factors fit a further 64 bits:
\(16\cdot2898+36+12+64<65536\).
The displayed \(2^{131072}\) leaves ample room for these complete
difference sums.

In particular, the actual operator
\(D_\gamma{\cal U}_\gamma(w):A^0\to E_s^+\) is jointly continuous
for gamma in \(A^0\) and \(w\) in \(E_{s+1}^+\).
The term involving a high far-height background in (GA.11) is
essential. Omitting it would not prove the joint operator statement
needed at the selected limit.

## 6. The actual metric and infinite principal feedback are continuous too

T.C.3--T.C.9 give holomorphy of the actual seed on its auxiliary gamma
ball and the genuine continuous operator
\[
 D_\gamma\mathfrak q(\gamma):
              A^0\longrightarrow{\cal P}_2,\qquad
 \|D_\gamma\mathfrak q(\gamma)\|
                    <2^{-110000000}/r_\gamma .
\]
Its range is the actual layer-weighted second parameter. Its radial
first compensation and its full principal feedback are GF.14--GF.19,
not a fixed-metric proxy column.

Here is the needed continuity of that feedback, including its infinite
part. For a fixed finite collection of original components, the
coefficients of the real ordered characteristic ODE, the holonomy
small root, the original scalar metric curves, and the L.9 counterterm
are continuously differentiable in their actual low norms. GF's
uniform real-flow remainder permits a second-parameter direction in
\({\cal P}_2\). The low \(E_{20}\) background controls the required
18 angular derivatives, and \(E_{2960}^+\) supplies much more than
this on the present domain.

Keep the full inverse
\[
 R=(I-D_pT)^{-1},\qquad \|R\|<2.
\]
Its Neumann expansion is used only to justify continuity, not to
delete any coupling. Every actual row depends on the finite original
support-neighborhood of metric bumps. After finitely many insertions
the set of components affecting a fixed finite output remains finite.
The remainder after \(N\) insertions is uniformly bounded by
\(2^{1-N}\). The finite pieces are continuous operator-valued
expressions by the preceding real ODE and counterterm argument.
Taking the finite-piece limit proves continuity of the needed
finite-output operators with the full principal inverse retained.
Equivalently, wherever the full operator difference is taken, its
resolvent identity is
\(R-R'=R(D_pT-D_pT')R'\).
This argument is on the original support graph and uses its original
row norm; it adds no new finite truncation to the theorem.

One must still form the physical source before taking the infinite
layer supremum. GF.19 gives the actual scalar and broken jet profile,
and GF.22 gives the strongest new narrow-source factor. In the deep
range it is
\[
 J_j^3h_j^{-10}\frac{\zeta_j}{\mu_j}\delta_j^{-57/2}
 =2^{-30}J_j^3\delta_{4096}^{-3/2}
          \delta_{8192}^{-485/4}\delta_j^{98-10/256}
       \longrightarrow0 .                                   \tag{GA.12}
\]
All six-neighbor collections, both profile junctions, and the shallow
\(o\) term are exactly the ones already paid in GF/T; the displayed
tail is used only after that finite prefix.

The coefficient of \(\dot\psi{\cal L}_0w\) tends to zero even faster,
by its original \(J^3\delta^{-5}C^\#\) profile. The other nonlinear
and holonomy-mean terms have the same source profile or an additional
small state factor. The three original scaled radial source
derivatives use the same four broken bump derivatives. Their
one-sided jumps and original root germs remain unchanged.

On a convergent \(E_{2960}^+\) sequence all the \(W_j\), \(j\le2898\),
are uniformly bounded. Formula (GA.12) therefore makes the physical
operator tail \({\cal P}_2\to Z_j^{[3]}\) tend to zero uniformly on
that sequence. Finite-prefix operator continuity followed by this
uniform tail bound proves the desired continuity of the entire
metric source, including the infinite principal response.
A bare parameter supremum without its physical source weights
would not suffice for this step.

The off-shell mean contribution \((D\Pi_A)\mathfrak f\) in GF.25
obeys the same complete local product estimates. It is retained.
The separate reference-height integral remains GF.24, including its
reference 1 and its independent integration constant. No vanishing
ordinary-source bound is applied to that independent height port.

## 7. Exact separation of the two ordinary-source contributions

There is a useful exact identity, beyond an estimate. Set
\[
 v_\gamma={\cal L}_\partial q_\gamma(F_Bw),\qquad
 u=w+v_\gamma .
\]
The whole support of \(v_\gamma\) is the fixed positive B collar.
Every actual design bump and every negative principal input is
outside it. GF.4 holds at every candidate first parameter, for every
admitted second parameter. On the collar all the metrics in question
and their ordinary source units agree; outside it, \(u=w\) together
with the required jets. Consequently
\[
 \boxed{\quad
 {\cal F}_\gamma(w)
   =\mathfrak f_{\mathfrak q(\gamma)}(w)
      +\{\mathfrak f_0(w+v_\gamma)-\mathfrak f_0(w)\}.
 \quad}                                                       \tag{GA.13}
\]
The first term uses the full actual first-principal map on \(w\).
The brace is supported in the same positive collar and vanishes
outside it. This identity holds for the complete ordinary residual
before dropping its holonomy mean, since the same local mean small
root is used at every radius.

Formula (GA.13) is an identity of ordinary sources. It does not say
that a propagated PDE solution is compactly supported, or that an
integrated height, coordinate phase, frame, or spatial position is
zero outside the collar. In particular it does not change the
independent reference-height formula GF.24.

This identity allows the metric column to be evaluated on \(w\)
itself. The endpoint affine lift does not need to be charged a
second time in that separate metric contribution.

## 8. Complete A0 forcing and joint source-operator continuity

Differentiate (GA.13) at fixed physical \(w\). The endpoint part is
the actual ordinary \(D_u\mathfrak f_0(w+v_\gamma)\) applied to
\(D_\gamma v_\gamma\); all dependence of \(v_\gamma\) on the complete
mixed \(f\) is already in (GA.10). The metric part is the full
GF.21 column at \(w\), applied to the true seed derivative in T.C.9.

GF's complete ordinary source estimate is
\[
 \|D_u\mathfrak F(u)[v]\|_{Z_s^{[3]},{\rm full}}
 \le2^{4194304}
   \{\|v\|_{E_s^+}+(1+\|u\|_{E_s^+})\|v\|_{E_{20}^+}\}.
\]
Use (GA.10), the actual low bound \(W_{21}\le2^{-49000000}\),
and GF.11 before multiplying high factors. The single highest
background is \(W_{s+1}\), and
\[
                  4194304+131072+16<8388608 .
\]
The complete metric source uses GF.26 at \(w\) and T.C.9. Widening
only fixed factors, the resulting bound is
\[
 \boxed{\begin{split}
 \|D_\gamma{\cal F}_\gamma(w)[\eta]\|_{Z_s^{[3]}}
 \le\{&
 2^{8388608}\epsilon(1+W_{s+1})\\
 &+2^{6291456-110000000}W_s\}
                         \|\eta/r_\gamma\|_{A^0},
 \qquad20\le s\le2898 .
 \end{split}}                                                 \tag{GA.14}
\]
The same statement keeps the complete ordinary holonomy-mean source
and its off-shell charge identity. Independent reference-height,
rigid height, and prescribed flux ports are retained separately
in their original units.

All three scaled radial source derivatives in (GA.14) are the
original ones. Internal sources still use
\(\zeta_j\delta_j^{16}\); the finite connector retains its true
ordinary unit and \(2^{440}\) weight. No internal density factor is
inserted in the finite source, and no raw trace is substituted for
the added physical height trace.

If \(W_{s+1}\le1\), then
\[
 \|D_\gamma{\cal F}_\gamma(w)[\eta]\|_{Z_s^{[3]}}
       <2^{-48000000}r_\gamma^{-1}\|\eta\|_{A^0}.               \tag{GA.15}
\]
Indeed the endpoint exponent is at most \(-48611391\), the metric
exponent at most \(-103708544\), and a two-term sum is bounded by
\(2^{-48611390}<2^{-48000000}\).
At \(s=1794\) the hypothesis follows from the original
\(W_{1856}\) condition. At the actual selected limit the already
paid \(E_{2960}^+\) bound supplies it simultaneously for every
\(s\le2898\).

For continuity, (GA.11) treats the complete endpoint derivative.
On its fixed finite collar, the original ordinary rational
coefficients, local mean small root, and three source jets depend
continuously on the graph background; (GA.13) ensures there is
no unaccounted principal variation in this term. Section 6 treats
the complete physical metric column and the seed derivative.
Thus
\[
 \boxed{\quad
 (\gamma,w)\longmapsto D_\gamma{\cal F}_\gamma(w)
 \ \hbox{is continuous in }\
 {\cal L}(A^0_{\ne0,\mathrm{ev}},Z_s^{[3]}),
 \quad20\le s\le2898,
 \quad}                                                       \tag{GA.16}
\]
for gamma in the relative \(A^0\) topology of T.C.1 and \(w\) in
the common \(E_{2960}^+\) topology. In particular this gives the
\(H^{8193}\)-direction operator continuity needed for actual selected
difference quotients. The stronger \(A^0\) direction estimate did
not assume a spatial strip for the unknown gamma or far height.

The value family is still the actual S/T construction on T.C.1.
No assertion of high regularity at an arbitrary rough cap endpoint
is made by (GA.16).

## 9. Actual finite differences and the selected-limit interface

For \(\gamma,\gamma'\) in the convex original domain, keep one
physical \(w\) and use its actual family along
\(\gamma_t=\gamma'+t(\gamma-\gamma')\).
All endpoint maps, seed parameters, radial compensations, and first
principal values in this integral are the true ones. The fundamental
theorem of calculus and (GA.14) give the complete high-source
difference bound with the same coefficients. In particular
\[
 \boxed{\quad
 \|{\cal F}_\gamma(w)-{\cal F}_{\gamma'}(w)\|_{Z_{1794}^{[3]}}
   <2^{-48000000}r_\gamma^{-1}
                          \|\gamma-\gamma'\|_{A^0}.
 \quad}                                                       \tag{GA.17}
\]
For \(64\le s\le1164\), the required source index
\(s+1734\le2898\) and the one high background index
\(s+1735\le2899<2960\) are in the proved windows.

This supplies both the true parameter mismatch and its joint operator
continuity for the separate selected-limit argument. The present
proof does not assume that selected solutions are differentiable,
does not assume onto solvability of a rough-source inverse, and does
not use a fixed-metric response column as the whole parameter
derivative.

## 10. New saved-bound combinations

The companion
[fourfold_codazzi_separated_gamma_forcing_saved_bounds.py](../scripts/fourfold_codazzi_separated_gamma_forcing_saved_bounds.py)
records the 16 new rational/integer combinations. Their first
execution after local environment loss used exact integer exponent
arithmetic and BigInt cross multiplication for the rational
comparisons; all 16 passed. The displayed Python reader records
the same arithmetic in standard Fraction form. No assertion is
made that Python ran in the unavailable local environment.

These checks only combine already completed long-module, cap, graph,
profile, and GF bounds. They do not rerun GF's 23 comparisons, any
native array, long solution, kernel target, or scientific integration.
