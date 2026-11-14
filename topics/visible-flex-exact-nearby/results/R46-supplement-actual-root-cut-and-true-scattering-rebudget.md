# R46 supplement: smaller actual root/cut and full scattering errors

**Status: proved.** This is the same complete original operator at the
R101 parameter $p_\infty$, with the same R43 first phase, the same physical
cut and the same whole real parameter box for every local estimate.
It improves actual Cauchy and strong-error constants, rather than only
the norm of a model. It does not invert the final finite head or transfer
the result to a changed deep-tail profile.

Put $N=2^{20}$, $J_N(n)=(1+n^2/N^2)^{1/2}$ and
$E_N^s=(H_N^s)^2$. All frequencies, including zero, occur in these
spaces. Write $[R]_+=\|R:E_N^0\to E_N^{4/3}\|$ and
$[R]_- =\|R:E_N^{-4/3}\to E_N^0\|$. The actual complete scattering
operator $\mathscr S$ and its unchanged amplitude-antidiagonal word
$\mathscr S_0$ satisfy

$$
 [\mathscr S-\mathscr S_0]_\pm
 <4.089838668\,10^{102}.                                  \tag{J.1}
$$

The previous bound was $2.983109\,10^{130}$. The new complete
root-to-physical-cut map $K$ satisfies, uniformly for $|s|\le2$,

$$
 \|K\|_{E_N^s\to E_N^s}<1.442974092\,10^{20},\qquad
 \|K^{-1}\|_{E_N^s\to E_N^s}<1.606282238\,10^{21}.          \tag{J.2}
$$

Its complete model error in either stated strong window is
$<1.197826763\,10^{27}$. The actual ordinary source maps, two mean
rows, independent regular ports and all intermediate head crossings
are retained below.

## 1. Exact inputs and the scope of replacement

The following proved inputs are used with their original identities:

- [the full root and its original strong phase](R43-supplement-full-root-Airy-operator-and-scaled-strong-remainder.md),
  in particular (A.13), (A.19)–(A.22) and (A.27)–(A.35);
- [the actual physical graph](R43-supplement-actual-physical-graph-strong-connector.md),
  especially its exact maps (P.26), (P.28), (P.31) and source (P.33);
- [the paired common-characteristic potential](R43-supplement-correlated-root-potential-and-common-characteristics.md)
  and [the sharp complete shifted-Airy change](R43-supplement-sharp-complete-shifted-Airy-frame-change.md);
- [the complete Bessel trace-coordinate estimates](R46-supplement-Bessel-trace-density-coordinates-and-complete-mean.md),
  using its proved v2 report and the original $\Lambda_n=\max(1,|n|)$;
- [the exact strong scattering word](R46-supplement-actual-strong-scattering-and-return-operator-word.md),
  including both opposite windows, the two finite mean corrections and
  the onto anti-$J$ identities;
- [the same full model word and Bessel budget](R46-supplement-complete-return-Bessel-rebudget-and-explicit-cutoff.md)
  and the original complete near-endpoint and stronger-source estimates.

Only upper bounds for identical maps are replaced. In particular the
strict-region Cauchy energy, strict source solver and strict strong
remainder are unchanged. The exact physical cut is

$$
 r_c=268136140016943/1125899906842624.
$$

The original affine center, direction, full real parameter interval,
source hashes and norm scale are compared by the consumer. Root and
strict metadata use different layouts; their common geometric origin,
direction, exact center and exact interval are separately compared.
The first phases are those of the original operator, and no scalar
average substitutes for a nonconstant phase.

## 2. The full root, in the original two-row frame

Let $L=1/4000$, $\sigma=1/40000$, $a=q_-\sigma$ and $v=5050$.
The new proved potential bounds are

$$
 V_*<22575.09344518,\quad W_*:=\sup|V-v|<27625.09344518,
 \quad V_{\xi,*}<2.257509344519\,10^9.                    \tag{J.3}
$$

The first two hold on the full fixed canonical product domain.
The derivative bound holds on the **real radial segment** $[0,L]$
with the stated complex angular strip. This is precisely the domain
needed for the full first-Dyson estimate; no derivative bound is
claimed at the outer boundary of the radial complex halo.

Use the exact shifted-Airy reference at every nonzero mode and the
exact cosine/sine mean pair. The Wronskian is $-2ic^2/\pi$ also at
zero, as in (A.17). The new complete Fourier-diagonal change from
this reference to the original R39 frame, in both directions, is

$$
 C_{\rm ch}<4.203925520505.                               \tag{J.4}
$$

Thus no reference change modifies the actual PDE or its first phase.

Here only $|s|\le2$ is needed. Pay the whole integer height hierarchy
through order three. Put

$$
 d_0=W_*,\qquad d_j=j!V_*a^{-j}\quad(1\le j\le3),
 \qquad \eta=L^2/2.
$$

For $0\le\ell\le j\le3$ set

$$
 T_{j\ell}=\binom j\ell N^{-(j-\ell)}d_{j-\ell},\qquad
 A=(I-\eta T)^{-1}.                                     \tag{J.5}
$$

This is a finite lower-triangular inverse with positive diagonal
$1-\eta d_0>0$; it is a majorant for the **entire** Fourier multiplier
and height Volterra operator, not a Fourier truncation. With
$W_k=\operatorname{diag}_{0\le j\le k}\sqrt{\binom kj}$ define

$$
 M_k=\|W_kT^{[k]}W_k^{-1}\|_2,\qquad
 H_k=\sqrt{k+1}\|W_kA^{[k]}W_k^{-1}\|_2.                  \tag{J.6}
$$

The factor $\sqrt{k+1}$ pays conversion between separate derivative
time norms and the full time-dependent Sobolev norm. The backward
adjoint has the same payment. Consequently duality and interpolation
give full positive and negative real orders through three. With
$M=\max_{k\le3}M_k$ and $H=\max_{k\le3}H_k$, the exact height
identity and original reference constants $C_D,C_G,\Gamma$ give

$$
 C_v=1+\Gamma LMH\sqrt2C_D,\qquad
 S_v=\Gamma(1+LMHC_G),
$$
$$
 C_r=C_{\rm ch}^2C_v<76896.424579,\qquad
 S_r=C_{\rm ch}S_v<19117.696720.                         \tag{J.7}
$$

The first constant bounds homogeneous evolution and inverse for
every subinterval of $[0,L]$. The second bounds the full ordinary
canonical source
$L^1(d\xi;H_N^{s-1/3})\to E_N^s$ for $|s|\le2$.
The two shifted derivative indices are within the paid order-three
window. Both momentum rows, both mean charges, and all angular
couplings occur in the exact amplitude identity.

For the strong error retain the original R43 phase $B$, with
$D^{-1/2}$ zero on the mean only in that specified first-phase term.
The true mean remains in $C_r-I-B$. For $s=0,-4/3$ put

$$
 p_s=\lceil|s+4/3|\rceil\in\{2,0\},
 \quad
 \mathcal L_s=\sum_{l\in\mathbb Z}
       (1+|l|/N)^{p_s}\langle l\rangle^{4/3}e^{-a|l|}.
$$

The full first-Dyson remainder is at most
$2C_q(V_*+V_{\xi,*})\mathcal L_s$. Its entrywise proof includes
zero input, zero output and opposite cones. The consumer computes
complete geometric/Stirling moments for orders $p_s$ and $p_s+2$,
then uses Hölder with exponents three and $3/2$; there is no cutoff
or omitted analytic tail in this sum.

Set $B_1=100\pi\max_{k\le2}M_k$. The two one-gain kernels in the
ordered second-Dyson identity need the multiplication orders
$s+1/2$ and $s+3/2$, whose absolute values are at most $3/2$ in
both cases. The rightmost full evolution is used only at its input
order. The complete remaining Dyson series therefore costs
$2C_rLB_1^2$. This proves

$$
 [C_r-I-B]_s\le
 2C_q(V_*+V_{\xi,*})\mathcal L_s+2C_rLB_1^2,             \tag{J.8}
$$

where $[\cdot]_s$ denotes gain $4/3$ from order $s$.
Numerically the forward and opposite constants are respectively
$<7.326330236\,10^{19}$ and $<7.292894690\,10^{19}$.
Their common higher-Dyson term is $<2.902478494\,10^{15}$.
All head paths in the full evolution have been kept.

## 3. The exact physical angle is a full Bessel coordinate operator

The original physical graph theorem gives exactly

$$
 \mathscr G_H=\mathcal H
       \operatorname{diag}(Q_H,Q_H^{-*})\mathcal H,
 \qquad
 \mathcal H=2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
                                                               \tag{J.9}
$$

The constant matrix $\mathcal H$ is unitary on every $E_N^s$.
The full v2 Bessel estimate pays $Q_H$, its inverse and both
adjoints, including their distinct mean row and mean input.
Consequently

$$
 G_0:=\max(\|\mathscr G_H\|_0,\|\mathscr G_H^{-1}\|_0)
 <2.055540711874,
$$
$$
 G_2:=\sup_{|s|\le2}
 \max(\|\mathscr G_H\|_s,\|\mathscr G_H^{-1}\|_s)
 <19.515367759370.                                      \tag{J.10}
$$

This replaces the old bound on an **actual** factor of $K$.
It does not treat a compression of $Q_H$ as unitary. The old strong
error $R_G=\mathscr G_H-\operatorname{diag}(Q_H,Q_H)$ is kept
unchanged, so every mean and cross-cone term in that difference is
still paid.

The graph and strict models have the exact same phases as before.
The proved Bessel bounds and same-order phase multiplier bounds
give the following bounds for these unchanged models:

| Model | Base bound | Uniform bound for $|s|\le2$ |
|---|---:|---:|
| $\mathcal W_g$ | $106.927004656$ | $148.524615531$ |
| $\mathcal W_{\rm st}$ | $2513478.242914$ | $567555402.861$ |

For example $W_{g,2}=\max(1,Q_{g,2}(1+h_g))$. The mean is the
separate identity block, and the nonzero branch/cone compressions
are orthogonal. The strict physical frequency $4|n|$ and the
original Airy phase factors are unchanged. The actual graph
propagation $C_g<2.376751992\,10^{10}$, its ordinary source map
and its complete $R_g$ are deliberately reused as proved.

## 4. Actual root/cut maps, both source norms and the finite mean fee

In the notation of (P.31),

$$
 K=D_4\mathscr G_H\mathcal C_gJ_b\Phi\mathcal C_r,
 \quad
 M_{\rm old}=D_4\operatorname{diag}(Q_H,Q_H)\mathcal W_gJ_b
                    \Phi_{\rm app}(I+B).                 \tag{J.11}
$$

The exact mean of $D_4$ is $(5,-3;-3,5)/2$, with eigenvalues one
and four; its nonzero part is $2I$. Thus $\|D_4\|\le4$ and
$\|D_4^{-1}\|\le1$. The original full Airy transition $\Phi$
and its inverse are retained, including the entire finite Airy
head and their exact mean matrices.

For $j=0,2$ write $G_j$ for (J.10). Direct composition gives

$$
 K_j=4G_jC_g\Phi_*C_r,\qquad
 K_j^-=C_r\Phi_*^-C_gG_j.                                \tag{J.12}
$$

At the base these are $<1.519875017\,10^{19}$ and
$<1.691886402\,10^{20}$; at window two they give (J.2).
Reverse evolution uses the inverses of the actual onto factors,
not an inverse of the model.

The exact four-term telescope in (P.32) now gives

$$
 R_K=4\{G_2R_g\Phi_*C_r+G_2W_{g,2}R_\Phi C_r
       +R_GW_{g,2}\Phi_{{\rm app},*}C_r
       +G_2W_{g,2}\Phi_{{\rm app},*}R_r\}
 <1.197826763\,10^{27}.                                 \tag{J.13}
$$

The first three errors gain two derivatives and embed to $4/3$.
The other outside factors have input/output indices between
$-4/3$ and $4/3$, hence the new window-two estimates suffice.
For the opposite window use the same ordered product with its
declared negative-order bounds; all mean components remain.

For the source formula (P.33), the two full output gains are

$$
 S_{r,j}=4G_jC_g\Phi_*S_r,\qquad S_{g,j}=4G_jS_g.          \tag{J.14}
$$

Their base values are $<3.778655482\,10^{18}$ and
$<4.506676898\,10^8$; their window-two values are
$<3.587467324\,10^{19}$ and $<4.278653131\,10^9$.
The former input is the canonical scalar in
$L^1(d\xi;H_N^{s-1/3})$. The latter is the exact tilted density
$f_t=(L-\chi)f_c/q$ in $L^1(dt;H_N^{s-1/2})$.
Both use the **same permitted extension** of the physical source
on the overlapping collar. A tilted radial/angle map does not
identify either norm with an arbitrary untransformed Bochner norm.
The original Piola, height and mean-source conventions still apply.

For the exactly amplitude-antidiagonal model $M$ in (F.10), set

$$
 M_j=2G_jW_{g,j}\Phi_{{\rm app},*}(1+B_*),
 \qquad B_*<9.179738.
$$

Then $M_0<1518293.689$ and $M_2<20022462.055$.
The two original mean corrections are paid again, explicitly:

$$
 [K-M]_\pm\le R'_K:=R_K+M_2+4\Phi_{{\rm app},*}.         \tag{J.15}
$$

The first correction is the mean-output factor $D_4-2I$;
the second replaces $\Phi_{{\rm app},0}$ by its specified
diagonal mean phase. The root phase annihilates mean input,
$\mathcal W_g\Pi_0=\Pi_0$ and $Q_He_0=e_0$, so the second
correction is genuinely finite rank. Neither change is made to
the actual PDE. The added fee is $<20023817.531$, and the mean
input/output and all mean-to-high-to-mean paths of $K$ remain.

## 5. The true strong scattering error

Keep the original conformal flux factor $\kappa$ and its exact
identity $K^{-1}=-\kappa^{-1}JK^*J$. The opposite root is
$K_L=J_bK$. The two complete transfer words are

$$
 \mathscr T=-\kappa^{-1}JK^*J\mathcal C_{\rm st}K_L,
 \qquad
 \mathscr M_T=-\kappa^{-1}JM^*J\mathcal W_{\rm st}M_L.
                                                               \tag{J.16}
$$

The unchanged strict constants are

$$
 C_{{\rm st},0}<6.329523754\,10^{50},\quad
 R_{{\rm st},+}<4.235039380\,10^{73},\quad
 R_{{\rm st},-}<2.121724480\,10^{63},\quad
 \kappa^{-1}<11.131746905882.
$$

One telescope, with the adjoint used in the opposite window as
in (F.14), yields

$$
 R_{T,\pm}=\kappa^{-1}\{
   R'_KC_{{\rm st},0}K_2+M_2R_{{\rm st},\pm}K_2
                     +M_2W_{{\rm st},2}R'_K\}.           \tag{J.17}
$$

The strict actual Cauchy bound is used only at order zero.
The output regularity in the other two terms is supplied by
their stated strong errors. No high Sobolev Cauchy contraction
has been inferred from base unitarity. Directed values are

$$
 R_{T,+}<1.363279556\,10^{102},\qquad
 R_{T,-}<1.217830727\,10^{99}.                            \tag{J.18}
$$

For completeness the exact onto anti-$J$ transfer
$\mathscr T=(A,B;C,D)$ has $\|B^{-1}\|_0,\|C^{-1}\|_0\le1$.
The identities
$B^{-1}A=D^*(C^*)^{-1}$ and
$B^{-1}=B^*-D^*DB^{-1}$, together with their opposite-window
adjoints, put a true scattering contraction on the right of
every error supplying output regularity. The four block errors
are bounded by $R_T,2R_T;2R_T,R_T$, whose Euclidean norm is
$3R_T$. This proves (J.1). This is the same exact onto-unitary
$\mathscr S$ and the same $\mathscr S_0$ as before.

## 6. Full negative ordinary affine source columns

Let $S_{\rm half}$ be the previously proved actual near-end half-core
ordinary source bound, and $S_{{\rm core},1}$ its stronger
$L^1H_N^{1/2}\to E_N^1$ bound. Use the exact radial reflection
and split at the core midpoint as in the original source theorem;
the two radial $L^1$ norms add exactly, without an extra factor two.

The near-endpoint complete raw columns are

$$
 g_0=(K_0^-S_{\rm half},\ K_0^-S_{r,0},\ K_0^-S_{g,0}),
 \qquad
 g_1=(K_2^-S_{{\rm core},1},\ K_2^-S_{r,2},\ K_2^-S_{g,2}).
                                                               \tag{J.19}
$$

The exact affine scattering fold has base norm $\sqrt2$;
it is independent of the chosen particular solution. Hence
$s_0=\sqrt2g_0$ gives:

| Complete original negative source | Base affine output bound |
|---|---:|
| Strict core, $L^1(dr;H_N^{-1/2})$ in $x=4\theta$ | $4.934157762\,10^{49}$ |
| Either canonical root, $L^1(d\xi;H_N^{-1/3})$ | $9.041146255\,10^{38}$ |
| Either tilted graph, $L^1(dt;H_N^{-1/2})$ | $1.078307487\,10^{29}$ |
| Core and the two root/graph pairs, Euclidean direct sum | $4.934157762\,10^{49}$ |

The last bound is exactly
$(s_c^2+2s_r^2+2s_g^2)^{1/2}$. It keeps both physical sides.
For the stronger columns in (J.19) the corresponding source orders
are $1/2,2/3,1/2$; the report stores these separately, without
renaming the base source spaces. Positive ordinary and weak sources
and the two independent regular fluxes are unchanged. Their final
composition with the improved negative map is a subsequent explicit
calculation, not an omitted or zero source here.

## 7. Reproduction and exact remaining obligations

The directed consumer is
`scripts/fourfold_actual_root_cut_strong_rebudget.py` and the completed
report is `notes/2026-11-13-actual-root-cut-true-strong-rebudget.json`.
It uses 384-bit Arb arithmetic and validates all original input,
source and dependency hashes. The six numerical comparisons all
passed; no native geometry was recomputed.

From the topic directory, with python-flint 0.9.0 available:

```sh
python3 scripts/fourfold_actual_root_cut_strong_rebudget.py \
  --out /tmp/actual-root-cut-true-strong-rebudget.json
```

The report records complete multipliers and height resolvents,
both first-Dyson and full root errors, all actual/model connector
constants, the separate finite mean fee, both transfer errors,
the full scattering constant, and base/stronger physical source
columns. Its SHA256 is
`bcf37acb85638acefdc1e6b5df486113ab11e7078305a13039886b3e503a55f0`;
the source SHA256 is
`f014311ca4df2dc31728d7004cb39616b00fc0a4cabc38d19ad616d16842afb1`.

The remaining dominant constants are the actual strict Cauchy and
strict strong-error terms in (J.17), not the physical coordinate
norm. The complete returned $R_*$, high cutoff and all final $H^1$
source columns must be reconsumed using (J.1); this theorem does not
declare them recomputed. The full finite head and its Schur equations
remain genuine obligations. It gives no complete feedback inverse,
no nonlinearly converged closed surface, and no automatic comparison
with the different newer nonlinear body or deep-tail profile.
