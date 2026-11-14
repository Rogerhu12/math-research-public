# Same actual inner finite low projection at additional width 3/5: input, complete source and 53-window derivative

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Scope and original object

This is a finite-input and source theorem, not a new infinite-dimensional fixed-point theorem. It concerns the same original background, the same P1 parameter domain `R156_actual_full_cut_posterior`, and the same full inner solution already constructed at the translated width 2/5. In particular, the fixed low field below is

\[
 L_F=\Pi_{2\le |m|\le92}F
     = C_S+\Lambda+\Pi_{2\le |m|\le92}e.
\]

The auxiliary nonlinear field $C_S$ is not renamed as $L_F$. The complete low correction in the actual saved field is included. Neither $L_F$ nor the inner auxiliary field is identified with the different outer low field $C_L$.

The original P1 domain, all 46 normalized coordinate caps, the original envelope $V'=257V_s/256$, and every original radial cell 12 through 224 remain unchanged. The new low Fourier weights are $\tau_n+3/5$; the known full field has weights $\tau_n+2/5$. Only finite Fourier polynomials are reweighted. The unknown modes at and above 94 have not been reweighted, and no new nonlow solution is claimed here.

## 1. Finite input and fixed actual far parameter

The pinned full-field packet is the successful fine53 posterior with SHA `3053e9cba77da784dfe3760451530c15a53d0366abda9b082276ec9e749ab9a5`. It is tied to the successful full-width 641 certificate `ade2693eeb64007fdde072a855b7e65c3f125ba294793eb7e78975bd9ccc79c0` and the modal packet `c23f7f76037247d877a62833f00eb9a96798d4720b8188c5243bc8f128a3c773`. All primary, source and actual owned-resource identities are checked by the producer.

For each cell and physical mode $m=2,4,\ldots,92$, let $c_m$ be the saved pair cap for $C_S+\Lambda$, and $e_m$ the saved complete low correction pair cap. The new pair cap is

\[
 \ell_m^+=\exp(m/5)(c_m+e_m).
\]

The caps are rigorous outward dyadics, including the exponential. If individual caps $a_m$ share the mass constraint $\sum_m a_m\le A$, the support function used for a positive weight $w$ is the exact greedy maximum of $\sum w_ma_m$ subject to those constraints. Thus the complete new common low mass is bounded independently by each of: the sum of new pair caps; the two old common masses consumed separately with their respective pair caps; and the combined old common mass with combined pair caps. Their minimum is still an upper bound for the same field. Radial suprema precede each Fourier sum throughout.

The actual finite 46-mode far parameter is obtained from the already successful shifted 641 field. Its width rises from $38+2/5$ to $38+3/5$ with the conservative finite factor $\exp(92/5)$. The saved result is below one quarter of the new evaluation radius $2^{-2142}$, which is inside the original R43 full graph domain. This is a bound on the actual finite input parameter only. The unknown nonlinear far graph output is not reweighted. Evaluation and lower-width identification of a newly constructed complete graph must still be paid in the conditional nonlow proof.

All 213 rows have

\[
 a_n\|L_F\|_{\tau_n+3/5}<1/128,
 \qquad a_n=\sup_{I_n}V'/w.
\]

The largest saved physical low cap is about $3.6567912\times10^{-17}$, attained at cell 12. Large dimensionless caps in deeper cells do not replace this physical test.

Actual input run: owned exit 0, 45.189 seconds, 57,260 KiB, 654 gates. Primary SHA `ff1df29ff5f24ffd6ed13dbc80c9f4a96d0e3084bacf03ebce41343d2d0ac811`.

## 2. Complete nonlinear source of this actual low field

The source producer evaluates the original full mean-root and inverse majorant, with all 46 physical modes retained. For signed Fourier coefficients write the strong pair caps as halves at both signs, set

\[
 W_m=A_m/(1+|m|),\qquad D_m=|m|W_m,
\]

and keep the original balanced-frame lower bound $B\ge120$. If $C$ is the complete low common cap and $a=\sup V'/w$, then the positive Laurent majorant for the denominator perturbation is

\[
 L=a(W+5D/(4B))+4a^2C^2\delta_0.
\]

The zero mode is retained. The common numerator is formed coefficient by coefficient, before inverse multiplication, as the maximum of the two material numerators

\[
 Q_s^+=\tfrac54D*D,
\]

\[
 Q_\ell^+=(1+1/(4B^2))W*W
       +\tfrac5{2B}D*W+\tfrac5{4B^2}D*D
       +8aC^2(W+5D/(4B))+16a^2C^4\delta_0.
\]

This is the previously proved complete R33/R106 numerator bound, including the full mean root. Its physical source materials are $V'^2/(rw)$ and $|w_r/w|V'^2/w$; the corresponding relative source-x materials are $s(V'/w)^2$ and $|\ell|(V'/w)^2$. No material or output factor is changed.

The finite inverse polynomial retains powers 0 through 6. With $\lambda=\|L\|<1/2$, the full omitted inverse contribution has the strictly positive bound

\[
 \|Q^+\|\lambda^7/(1-\lambda).
\]

The numerator zero mode is multiplied by the complete inverse before projection. The finite nonzero polynomial has support through physical mode 736; this support is not imposed on the infinite inverse tail. The same shared inverse-tail mass is charged once when a total band is consumed. All saved coefficients are explicitly finite and nonnegative. The source common numerator dominates both radial materials pointwise in each Laurent coefficient; it is not inferred by taking the maximum of two unrelated total norms.

All 213 cells completed with owned exit 0, 50.842 seconds and 44,584 KiB. The complete source-summary SHA is `9f9ba881882e14f633a59fbd1111c7fd0ade9657fee36822f14ad8c495052b38`. The 11 compressed full source parts are pinned in that summary and cheaply regenerable from the frozen producer. They remain private under the repository's derived-data rule.

## 3. Actual DQ(LF), exact window support

The output partition consists of all 46 singleton modes 94 through 184 and the seven windows 186..192, 194..256, 258..512, 514..1024, 1026..2048, 2050..4096, and 4098..8190. Input windows consist of the complete low band 2..92, these 53 windows, and the complete infinite input 8192 and above. A separate 53 by 46 low-singleton table is also saved.

Each input window is one shared strong pair mass. No number-of-modes factor is introduced. For a fixed input frequency $n$, the admissible center modes are obtained from exact even-integer sum and difference membership. Difference interactions carry the actual new factor $\exp(-2k\tau_n^{new})$. On each fixed-membership interval the original endpoint-max proof applies to the two positive coefficient functions. The source coefficient carries no output factor $1+m$; that factor belongs to its Green readout.

The same original pairwise formulas are used with the new actual low pair caps. Every coefficient of the s-material majorant dominates the ell-material coefficient under the original $B\ge120$ condition, and this is checked for every actual entry. The infinite input is not truncated: frequencies above the finite output maximum plus 92 have exactly zero DQ contribution by Fourier support, while all other infinite input frequencies are included in the membership partition.

The actual run has 1,262,284 gates, owned exit 0, 89.578 seconds, 49,532 KiB. Certificate SHA `f652efba56708c9b0efe0230a52838abe106967266273a48740c2f09ccbdad18`. Each of the 213 compressed cell chunks is pinned, permitting a consumer to stream the table within 96 MiB. Its numerical values are source bounds only; the complete $Q(Z)$, full $T(L_F+Z)-T(L_F)$, and nonlinear far forcing remain separate obligations.

## 4. What remains

A new conditional map may now fix this actual $L_F$ and the actual finite far parameter and solve only for the complete nonlow field. To claim a new solution it must pay a strict invariant domain, an appropriate distance estimate, all whole-ball physical mean and inverse gates, the complete nonlinear far graph, and an independent lower-width uniqueness comparison with the same already existing field. No such claim is made by this package. No new ODE, radial integral, Green solve or quadrature was run.
