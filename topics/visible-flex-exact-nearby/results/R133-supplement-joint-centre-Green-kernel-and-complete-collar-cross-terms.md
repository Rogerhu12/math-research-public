# R133 supplement: the joint centre Green kernel and all collar cross terms

2026-11-16. Proof by newton_source; no numerical evaluation.

**Proved here:** an exact common-factor formula for the complete W2C signed-centre operator, cancellation of the two body-cutoff derivative paths, and an explicit local-plus-integral recipe that retains every collar cross term. No bound or successful finite comparison is assigned. The completed WPS60 and WVC56 calculations remain immutable.

## 1. Fixed realization and scope

Use the actual positive interval, ordinary radial measure, normalized real Fourier coordinates, 193-dimensional low fibre, 97 root-complement coordinates, 96 prescribed root-even coordinates, and the original outer chart with its $H^{-5/6}$ weights. The actual four blocks, radial projections, physical mean, two right-hand sides, seven primal/dual ports, affine jumps, external-function inputs, $\Theta$, $\nu$ and cokernel are unchanged.

The first candidate below fixes the completed WVC low reference $D_f$ and its complete body-to-output receiver $G_f$. It does not substitute the WCTR low reference. In the notation of W2C, put

$$
 L_c=\partial_r-A_c,\quad B_c=B_{HL,c}S^{-1},\quad
 C_c=G_f B_{LH,c},\quad M_c=(A_{L,c}-D_f)S^{-1}.
 \tag{JK.1}
$$

Here $A_c$ is the full repaired-centre high block with its actual principal coefficient. It is an operator replacement in a trial decomposition, not a different physical background solution. The full actual degree96 difference is still paid in W2C.26. The collar centre and its full differences require the genuine original collar inputs identified in W2C9; the old WVC zero packet does not supply them.

Let $\Pi_0$ be the finite high band $97\le |j|\le160$ in the original real parity realization. The original reference inverse $G=G_{0,160}$ is extended by zero outside that band. Its differential operator is $L_0=\partial_r-D$. On its actual homogeneous reference domain,

$$
 L_0G=\Pi_0,\qquad GL_0v=v\quad(v\text{ in that domain and band}).
 \tag{JK.2}
$$

The principal coefficient $D$ can be defined on the finite larger intermediate bands by its same modal formula; only its restriction in (2) is used for inversion. Write $E=A_c-D$. All occurrences of $GEG$ retain the actual intervening band projections. No claim is made that $A_c$ preserves $\Pi_0$.

The original scalar cutoff $\chi$ is zero on the collar and near both physical endpoints, and has the admitted matching values at the original identity-transmission seams. Multiplication by $\chi^2$ preserves the reference domain. This fact, not an identification of the reference root condition with the actual high root chart, is the domain input below.

## 2. The complete common-factor identity

Use the exact W2C collar primitive

$$
 (Jf)(r)=\int_a^{\min(r,c)}f(s)\,ds,
 \qquad \partial_rJ=P_c.
 \tag{JK.3}
$$

Its constant continuation beyond $c$ is part of this definition. Let $X=M_\chi$, let $\psi$ be the full W2C cubic collar cutoff, and define

$$
 P_0=XGX,\quad U=M_\psi(J+JA_cJ),\quad
 V=(-J^*+J^*A_cJ^*)M_\psi.
 \tag{JK.4}
$$

Every adjoint is taken in the original radial/angular distribution pairing; the actual Bessel/Riesz maps are inserted when norms are formed. In particular,

$$
 (J^*f)(s)=\mathbf1_{[a,c]}(s)\int_s^R f(r)\,dr .
 \tag{JK.5}
$$

The upper limit in (5) is $R$, not $c$. Dropping the continuation would delete the transition and body-to-collar terms.

Set $P=P_0+U$ and $Q^*=P_0+V$. The W2C trials are exactly

$$
 \widehat V=PB_c,\qquad \widehat W=Q C_c^*,\qquad
 R_c=L_cPB_c-B_c .
 \tag{JK.6}
$$

Consequently their complete signed centre is

$$
 \boxed{\mathcal H_c
 =G_f\{M_c+B_{LH,c}F B_c\},\qquad
 F=P+Q^*-Q^*L_cP.}
 \tag{JK.7}
$$

Indeed $\widehat W^*=C_cQ^*$, so the second and third terms of W2C.25 are $C_cPB_c-C_cQ^*(L_cP-I)B_c$. This proves (7) in the original order. The complete $G_f$, with every body, root-complement, physical-mean and weighted outer row, now occurs only once. This factorization does not permit taking separate positive norms of its summands and then claiming their signed cancellation.

The exact expansion of (7) is

$$
 F=F_{bb}+U+V-P_0L_cU-VL_cP_0-VL_cU,
 \quad F_{bb}=2P_0-P_0L_cP_0 .
 \tag{JK.8}
$$

There are five collar terms after $F_{bb}$. In particular, $-VL_cU$ is a full primal/dual collar interaction, not an optional higher-order remainder.

## 3. Exact body-cutoff cancellation

For a scalar domain-preserving multiplier $s$, the original reference Green identity gives

$$
 [L_0,M_s]=M_{s'},\qquad
 GM_{s'}G=M_sG-GM_s .
 \tag{JK.9}
$$

To verify the second identity, apply the first to $Gf$, use both identities in (2), and keep the intervening finite-band projection. Scalar multiplication commutes with that projection. The raw reference solutions and $sGf$ have the same homogeneous endpoint qualification, so there is no omitted endpoint term. Across a raw identity seam, $s$ and the solution have matching values; there is no impulse contribution. If a future realization has a different transmission, this proof must include its full boundary form instead.

For $s=\chi^2$, expansion before any absolute value yields

$$
 L_cP_0=\chi^2\Pi_0+(\chi'I-\chi E)G\chi,
 \tag{JK.10}
$$

and therefore

$$
 \boxed{F_{bb}
 =2XGX-\tfrac12X^3GX-\tfrac12XGX^3
             +XG\,M_{\chi^2}E\,GX.}
 \tag{JK.11}
$$

For example the term with $\chi\chi'$ is

$$
 XG\,M_{\chi\chi'}GX
       =\tfrac12X^3GX-\tfrac12XGX^3.
 \tag{JK.12}
$$

Thus the exact kernel of the first three terms of (11) is

$$
 \chi(r)\chi(s)
 \left[2-\frac{\chi(r)^2+\chi(s)^2}{2}\right]G(r,s),
 \tag{JK.13}
$$

and the remaining term is

$$
 \chi(r)\int_a^R G(r,t)\chi(t)^2E(t)G(t,s)\,dt\,\chi(s).
 \tag{JK.14}
$$

Both Green triangles, all modal contractions and the exact signed $E$ belong to (14). In a region where both outer cutoff values and the internal multiplier are one, the displayed expression has the familiar $G+GEG$ form. This is only an algebraic explanation, not a bound or a claim that the cutoff can be removed globally.

**The cancellation in (11) is restricted to the joint signed-centre map.** The separate primal and dual residuals in W2C.12--21 still contain their complete cutoff and transition terms. No source receiver, dual receiver or seven-port fee may omit a $\chi'$ or $\psi'$ term on the strength of (11).

## 4. Derivative-free representation of all collar cross terms

Put $m(r)=\min(r,c)$ and define the ordered coefficient primitive

$$
 A[s,t]=\int_s^t A_c(u)\,du\qquad(s\le t\le c).
 \tag{JK.15}
$$

This is an integral of the actual centre operator coefficients, not a derivative or a commuting-matrix approximation. The kernels of $U$ and $V$ are

$$
 u(r,s)=\psi(r)\mathbf1_{a\le s\le m(r)}[I+A[s,m(r)]],
 \tag{JK.16}
$$

$$
 v(r,s)=\psi(s)\mathbf1_{a\le r\le m(s)}[-I+A[r,m(s)]].
 \tag{JK.17}
$$

In (17) the rightmost cutoff in (4) becomes $\psi(s)$. Interchanging it with $J^*$ would be a different operator.

Let $S_U=L_cU$. It has the exact local-plus-integral representation

$$
 S_U=P_c+\mathcal S,
 \tag{JK.18}
$$

where the kernel of $\mathcal S$ is

$$
 s_U(r,s)=
 \begin{cases}
 -\mathbf1_{a\le s\le r}A_c(r)A[s,r],&a\le r\le c,\\
 \mathbf1_{a\le s\le c}[\psi'(r)I-\psi(r)A_c(r)]
                         [I+A[s,c]],&r>c.
 \end{cases}
 \tag{JK.19}
$$

This follows from $\partial_r(J+JA_cJ)=P_c(I+A_cJ)$; on the collar the two first-order $A_cJ$ terms cancel exactly. No derivative of $A_c$, $B_c$, or an arbitrary head input is used.

Similarly let $T_0=L_cP_0$. Its local part is $\chi^2\Pi_0$ and its integral kernel is

$$
 k_0(r,s)=[\chi'(r)I-\chi(r)E(r)]G(r,s)\chi(s).
 \tag{JK.20}
$$

With $p_0(r,s)=\chi(r)G(r,s)\chi(s)$, all five collar terms in (8) have the following one-integral kernel on the external source band:

$$
 \begin{split}
 f_{\rm cross}(r,s)={}&u(r,s)
  +v(r,s)P_b(s)[I-\chi(s)^2\Pi_0]\\
 &-\int_a^R p_0(r,t)s_U(t,s)\,dt\\
 &-\int_a^R v(r,t)[k_0(t,s)+s_U(t,s)]\,dt .
 \end{split}
 \tag{JK.21}
$$

To check (21), use $P_0P_c=0$ because $\chi=0$ on the collar, expand $S_U=P_c+\mathcal S$ and $T_0=\chi^2\Pi_0+\mathcal K_0$ in (8), and combine the direct $V-VP_c$ terms. Since $B_c(s)$ has source support $\Pi_0$, the rightmost bracket may become $1-\chi(s)^2$ **only after multiplication by that actual $B_c(s)$**. Before that restriction, the projection in (21) stays explicit.

Equations (13),(14),(21), followed by the complete exterior factors in (7), are one exact signed kernel recipe. They contain no differentiated input, no unsupplied radial coefficient derivative and no independently subtracted upper bound.

## 5. Domains, finite supports and endpoint observations

The collar corrections satisfy the W2C compact-core argument: finite angular support, ordinary radial $H^1$, zero raw values at both physical endpoints, and continuity at each actual identity-transmission seam. Consequently they belong to the original homogeneous and dual graph closures. This does not identify the reference high-even root condition with the actual root chart.

Angular source and observation factors begin in $97\ldots160$. A centre multiplication or ordered primitive can expand support by64. The collar trials reach224, centre residuals reach288, and their complete full-degree96 differences reach416. The intermediate angular sums in (14),(19),(21) must retain these true supports; a $\Pi_0$ at an external $B_c$ or $B_{LH,c}$ does not justify projecting an intermediate $A_c$ action prematurely. The unknown actual $G_H\mathcal R$ remains an infinite high state.

Every $G_f$ endpoint atom is applied to the final joint body source in (7). It is not discarded by the compact support of the high test function. Likewise any independent actual high endpoint, affine or impulse observation outside $C_c=G_fB_{LH,c}$ retains its separate original row. Physical mean components remain in $A_{L,c}$ and in the complete $G_f$ receiver. The genuine identity $\Pi_{\phi,2}B_{LH,c}=0$ can only eliminate the corresponding returned mean output; it does not remove mean input columns from a general cross block.

All matrices and adjoints in a numerical realization must use the original normalized real sine/cosine basis, mean basis1, nonzero-mode $\sqrt2$, cell factors, $S$, and outer Riesz factors. They are not inferred from a complex signed kernel without the actual isometries.

## 6. Implementable joint-kernel interface

An implementation may provide the following exact objects before any positive majorant:

1. The original complete modal two-triangle $G(r,s)$ with both endpoint qualifications, and the full low receiver $G_f$, including every endpoint atom.
2. Signed $M_c(r)$, $B_c(r)$, $B_{LH,c}(r)$ and $E(r)$ on admitted full continuous panels, including the genuine collar.
3. The signed primitives $A[s,t]$, both cutoffs and their derivatives, with exact ordered composition and the correct half-triangle supports.
4. The kernels (13),(14),(21), combined as one $F$ and then as the single whole map (7).
5. A true forward row and transposed column enclosure for that same complete signed map, with local multiplication and atomic observations present.

The two Green triangles are semiseparable in each declared mode. The single intermediate integrals in (14),(21) can therefore be split at $a,c,c+w,r,s$ and the original coefficient joins, and represented by prefix/suffix coefficient integrals or a finite state-space cascade. This avoids treating the displayed formula as a mandatory dense $155^2\times193^2$ array. Any such representation must prove equality to the entire signed kernel, retain both orientations, and never divide by a possibly zero discrete transfer factor. This note does not assign a runtime or a rank to an unconstructed compressed representation.

Most importantly, the complete signed $G_fM_c$ and feedback term in (7) must be combined before the final pointwise absolute-value comparison. Replacing (7) by the saved old centre bound171 plus nonnegative correction fees is a valid triangle inequality but cannot deliver a comparison below1. Equation (11) gives a different exact kernel to evaluate; it does not subtract any number from that old bound.

The full actual-family remainder remains precisely W2C.26--29. Every new norm must be saved as a complete new whole target, with its actual input/output windows, while old complete targets remain literal copies. No new numerical target, bound, finite inverse or physical column is reported here.

## 7. Primary identities

All repository paths are relative to `topics/visible-flex-exact-nearby/`.

| Role | Path or exact object | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| Full two-sided identity and complete centre decomposition | `results/R133-supplement-two-sided-high-feedback-and-complete-centre-correctors.md` | `7e1c46ddc9c1a771a06c6bb4bf87c8676fd8c898` | 24119 | `72bef388c4bf801bfe746f0b645d1439d1a066ae3d6b7d68ab75b374b2908d6b` |
| Fixed two-term collar candidate | `results/R133-supplement-complete-collar-Volterra-dual-feedback-candidate.md` | `41e309e49a41984fb624afbca21684f7e91c7c79` | 25536 | `09ada380c17b64f26d0f88f49734d52361b794ce10b6617b16d58f6de053ae01` |
| Original complete Green kernel and paired source realization | `results/R133-supplement-paired-source-circuits-and-complete-finite-residual-candidate.md` | `e830f7df4643fe77b941478dbde06ebf9378ebef` | 43851 | `ffd000ff15f705ffaaf3c33dddcd0c09c997c0c92d5110bab5be5ea9c114fa72` |
| Completed original WVC calculation, including false finite gate | `notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json` | `746ec1e16befe8914c64521ad087c1f1dd23ab73` | 78627 | `85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88` |

The complete pure proof has been read by root, and the joint identities (8)--(21), domains and kernel ordering have also passed the designated peer check. The primary pathnames were matched to their exact existing Git blobs and SHA256 values by read-only metadata checks. No scientific function was executed.
