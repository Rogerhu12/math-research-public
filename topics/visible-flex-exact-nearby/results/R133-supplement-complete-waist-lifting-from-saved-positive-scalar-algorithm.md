# R133 supplement: complete waist lifting from the saved positive scalar algorithm

2026-11-15. This proves a new small scalar readout of the completed selected-parameter calculation. It supplies the missing coefficient of the original 96-row left source in the same complete finite193 inverse used by SR. No original row enclosure, parameter difference, scalar integral, Green operator or Poisson product is recomputed.

The new numerical values below still require their own public Actions consumer. The proof does not supply a high-frequency inverse, an actual nonlinear solution, or the physical curvature entry conditions.

## WL1. Fixed object and immutable inputs

Use the same continuous selected family
$$
Q_\delta=\bar Q+\delta Z,\qquad \nu_\delta=\nu_0+\delta,
\qquad |\delta|\le d_0=\frac1{10^{10}},
\qquad I=[0,L],\quad L=\frac9{10},
\tag{WL.1}
$$
with the original fixed intrinsic parameter $\eta_0$, continuous centre definition
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
and response definition
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
The complete moving even mean and physical angular frequencies $4j$ remain.

The completed D scalar execution is
[run 43713242980/1](../notes/selected_parameter_core_scalar_fees_ci/run-43713242980-1/execution.json),
blob **ce7af74c8b2f8cf7715775f352d2c26afb03413a**, 40,659 bytes, SHA256
**6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071**.
Its unique scientific child succeeded with all 12 gates passed. It verified all 40 original parts and all 7,721 rows on $[0,25/8]$. The whole-core window in (WL.1) contains 6,376 original closed rows and 6,377 exact scalar restrictions, with both compact-support seams retained.

The exact producer is
[scripts/fourfold_codazzi_selected_parameter_core_scalar_fees.py](../scripts/fourfold_codazzi_selected_parameter_core_scalar_fees.py),
blob **704b1e1d4aa74e97c866c725a2524c1b8624039e**, 25,571 bytes, SHA256
**827fcb237a79b48c095872b61c370ff2ceafc143a8dc6a1774021188ff3ea320**.
The corresponding manifest has SHA256
14271d7d61c70996092f105768ca29cc0dd355665be0becea4386441b38c907f.
Its exact positive formulas, rather than only an abstract operator norm, are used below.

The four already certified global state bounds are
$$
\|\bar Q\|_{A^0,\mathrm{pair}}\le7,\quad
\|\bar Q_\phi\|_{A^0,\mathrm{pair}}\le6,\quad
\|Z\|_{A^0,\mathrm{pair}}\le19,\quad
\|Z_\phi\|_{A^0,\mathrm{pair}}\le83 .
\tag{WL.2}
$$
They include the actual continuous repairs. They are exactly the four chosen constants of the successful D receipt. In particular one may use
$$
\varepsilon=19d_0>0,\quad \varepsilon_1=83d_0,\qquad
M=7+\varepsilon,\quad M_\phi=6+\varepsilon_1
\tag{WL.3}
$$
as complete bounds on $|Q_\delta|$ and $|\partial_\phi Q_\delta|$ throughout $I$. These are known-centre bounds, not bounds on an unknown perturbation.

## WL2. Recover two coefficient products from the original nonnegative algorithm

On each original restricted closed row, the D producer uses
$$
b\ge|\beta|,\qquad
G_+\ge |G_\delta|,\qquad
K_+\ge\max(1,|K_\delta|)
\tag{WL.4}
$$
on the whole family (WL.1). The same $\beta$ is unchanged in the original compact metric variation. The saved original formulas use the fixed positive quantities
$E_0=E_m=\varepsilon$ and $Q_0=7$.

Define
$$
U_0=14\varepsilon+\varepsilon^2>0 .
\tag{WL.5}
$$
In the producer's function **selected_parameter_fees**, the complete positive budget **change** is the upper endpoint of $K_+U_0$. The produced scalar **M0** contains the nonnegative term $3b\,\mathrm{change}$, and the produced scalar **M1** contains the nonnegative term $G_+K_+\varepsilon$. Every other term in both sums is nonnegative. All outward upper-endpoint operations preserve these inequalities. Thus, on every complete row,
$$
M_0^{\mathrm D}\ge3bK_+U_0,\qquad
M_1^{\mathrm D}\ge G_+K_+\varepsilon .
\tag{WL.6}
$$

Read, without recomputing, the complete saved fields
$$
\mathfrak M_0=
 \mathrm{upper}(\texttt{complete_scalar_fee_conclusions.whole_core.maxima.M0}),
\quad
\mathfrak M_1=
 \mathrm{upper}(\texttt{complete_scalar_fee_conclusions.whole_core.maxima.M1}).
\tag{WL.7}
$$
The precise field path is under **actual_scientific_receipt**. The original accumulator takes the maximum of the complete positive row budgets over every one of the true core restrictions. Its exact cover and positive algorithm identities are part of the required input gates.

The two new scalar quantities
$$
B_*=\frac{\mathfrak M_0}{3U_0},\qquad
G_*=\frac{\mathfrak M_1}{\varepsilon}
\tag{WL.8}
$$
therefore satisfy, uniformly on $I$ and (WL.1),
$$
|\beta|\max(1,|K_\delta|)\le B_*,
\qquad |G_\delta|\max(1,|K_\delta|)\le G_* .
\tag{WL.9}
$$
Indeed use the same $b,G_+,K_+$ in (WL.4)--(WL.6), then the complete global maxima. No division by a sampled state or by a vanishing parameter is used: $d_0$ is the fixed positive radius of the already completed computation, even when the current member has $\delta=0$.

This argument uses the explicit nonnegative producer terms and their original complete global maxima. It would not follow from an arbitrary upper bound on the norm of $\mathcal A_\delta-\mathcal A_0$. No cancellation of interval bounds, lower bound on an operator norm, or inferred reverse norm inequality occurs.

## WL3. A complete finite-frequency coefficient and its real radial cost

Use [NF.22--23](R133-supplement-divergence-nonlinear-core-source-and-complete-finite193-receivers.md), retaining its original independent mean terms and normalized-circle Euclidean pair norm. Since $K_+\ge1$, both $b$ and $bK_+$ are bounded by $B_*$, while $G_+K_+$ is bounded by $G_*$. Therefore the new constant
$$
\begin{split}
a_*={}&384\left\{\frac{\pi}{8}B_*M^2+G_*M\right\}\\
&+B_*\left(1+3M^2+\frac12MM_\phi\right)+G_*M_\phi
\end{split}
\tag{WL.10}
$$
bounds the whole coefficient $a_{96}(r)$ of NF.22 at every $r\in I$.
The factor 384 is the largest physical angular frequency in the actual 96-mode block. There is no additional fold, amplitude or normalized-circle factor. Mixed curvature signs are allowed by $\max(1,|K_\delta|)$.

Let $U=(I_{96},0)$ denote the original orthonormal waist rows and set
$$
\psi(r)=1-r/L,\qquad W_{b_0}(r)=\psi(r)U^tb_0,\qquad
\mathcal D_\delta=\partial_r-\Pi_{96}\mathcal A_\delta\Pi_{96}.
\tag{WL.11}
$$
The projection contains the complete even mean. The injection $U^t$ itself puts the prescribed data in the odd block only. The true angular projection is orthogonal, so its norm is one.

Because $\|U^tb_0\|_2=\|b_0\|$,
$$
\|\mathcal D_\delta W_{b_0}\|_{L^2(I;L^2_\phi)}
 \le \ell_*\|b_0\|,
\qquad
\ell_* = L^{-1/2}+a_*\sqrt{L/3}.
\tag{WL.12}
$$
Here $\int_0^L|\psi'|^2\,dr=1/L$ and
$\int_0^L\psi^2\,dr=L/3$ are exact. The two terms are combined by the triangle inequality in the complete ordinary-source norm. No old row integral or Green product is evaluated again.

## WL4. The same CPA case gives the uniform fifth column

Let $g_B,g_N,g_C$ be the three actual ordinary-source gains of one complete successful CPA case in
[the actual weighted-cap inverse](R133-supplement-actual-weighted-cap-inner-difference-and-finite193-inverse.md).
Use either its full physical $\gamma$ ball of radius $10^{-9}$ or its tail ball of radius $10^{-9}/128$, preserving that case's own $\kappa$, both positive diagonal gates, positive determinant and all remaining domain qualifications.

By [SR.2--9](R133-supplement-uniform-secant-cap-rows-and-complete-finite193-nonlinear-receivers.md), these gains are uniform for every complete boundary-difference operator $\mathcal K$ in that same case's Hilbert norm ball. No derivative of the actual tail selection is inferred.

The right boundary rows read only the true value at $L$. Thus
$$
UW_{b_0}(0)=b_0,\qquad W_{b_0}(L)=0,\qquad
\mathcal B_\delta^\mathcal K W_{b_0}(L)=0 .
\tag{WL.13}
$$
For the complete ordinary inverse $G_{\delta,\mathcal K}$ the state
$$
\mathcal W_{\delta,\mathcal K}b_0
 =W_{b_0}-G_{\delta,\mathcal K}\mathcal D_\delta W_{b_0}
\tag{WL.14}
$$
satisfies the exact homogeneous finite193 body equation, the left source $b_0$, and the homogeneous complete 97-row right boundary condition. It is continuous. Its internal old frame interfaces and virtual-waist term are already part of the same original inverse.

Write
$$
r_N=\frac{2383968743003}{10^{13}},\qquad
J_N=r_N-\frac{r_N^2}{L}+\frac{r_N^3}{3L^2}
       =\int_0^{r_N}(1-r/L)^2\,dr .
\tag{WL.15}
$$
The three new fifth-column bounds are
$$
w_B=\sqrt{L/3}+g_B\ell_*,
\qquad
w_N=\sqrt{J_N}+g_N\ell_*,
\qquad
w_C=g_C\ell_* .
\tag{WL.16}
$$
Their inputs are the original 96 Euclidean waist rows. Their outputs are, respectively, the full core ordinary $L^2$ pair, the original negative-window ordinary $L^2$ pair, and the genuine cut $L^2$ pair including the even mean. The cutoff and physical units agree with the other four columns of the same CPA case. Old $\kappa=0$ fifth columns are not relabelled as these columns.

If the completed [WA reader](R133-supplement-exact-selected-waist-data-and-original96-rows.md) supplies the uniform original96 bound $b_*^{\mathrm{WA}}$ for precisely $|\delta|\le d_0$, then
$$
\|\mathcal W_{\delta,\mathcal K}b_{0,\delta}\|_Y
 \le w_Y b_*^{\mathrm{WA}},\qquad Y=B,N,C .
\tag{WL.17}
$$
The WA row for a larger radius does not enlarge the present parameter domain. At a fixed selected $\delta$, two actual states satisfying the same waist condition have the same $b_{0,\delta}$; its affine contribution then cancels in their difference. This observation does not give a derivative in $\delta$ or remove the independent high-frequency waist conditions.

## WL5. Required new small execution and scope

A new public scalar consumer must verify the complete D success, its exact source/manifest identities and 12 gates, all four constants (WL.2), the true whole-core cover, the original compact support and the exact positive terms (WL.6). It then reads the two full saved balls in (WL.7), preserving those original strings in its conclusion. It does not import or call the old D producer.

It must separately verify the complete CPA success and select each case as a whole. All three ordinary gains are read from that same case. The new output contains $B_*,G_*,M,M_\phi,a_*,\ell_*,J_N$, all six fifth-column gains, and, if the new WA success is available, all six complete selected-waist contributions. Every square root uses a proved nonnegative exact quantity or an outward upper bound; no nonfinite value is clipped.

The complete small scientific result is atomically saved before rendering and emitted recoverably before Git publication. No old row archive, native array, response shard, QR factor, repair sequence or successful integral is needed by this consumer. Any unsuccessful identity or positivity gate is preserved as an actual failure.

This completes only a coefficient of the five-input finite193 receiver, conditional on the stated successful numerical evaluation. The actual affine right source, nonlinear interior source, high-body and high-cut inputs, physical $\gamma$ entry, whole-core ball, true parameter equation, all remaining means and matching, and the final fixed-metric geometric family remain independent obligations.
