# R133 supplement: complete strong comparison with the P.22-anchored free trial

2026-11-15, visible-exact / phase_inverse.

**Proved operator identity with completed numerical inputs.**
The successful genuine positive correction PC and the successful strict continuation ST can now be composed without introducing another uncomputed negative residual or a cut jump. The required choice is to extend both comparison trials homogeneously below the actual P.22 cut. This note proves that choice is legitimate for the already completed PC source estimate and identifies the exact resulting strong error.

The new conclusion is a particular complete comparison map
$$
 E_{\rm AW}:H^{-4/3}_{|j|\ge97}
      \longrightarrow L^2_{\rm old\ primitive\ density}\oplus\mathbb C^2,
 \qquad
 \|E_{\rm AW}\|\le C_{\rm PC}+C_{{\rm ST},4}.
 \tag{AW.1}
$$
Both constants on the right are already completed bounds. Their sum here is an exact symbolic combination of those two accepted upper endpoints; no additional rounded scalar, old integration, reference column or numerical propagation is evaluated.

The reference is the original free P.8 first-transport trial, evaluated at the actual P.22 circle and then continued by the full selected homogeneous physical equation to the waist. The difference in (AW.1) is against the genuine selected positive high Poisson columns of PC, with their actual nonzero stable root trace. The positive finite-head equations, all independent mean ports and the finite matching problem remain explicit. This is not yet a numerical first-symbol error for the anchored free trial or a complete incoming inverse.

## 1. Same object, input reference and output density

Use the same real family
$$
 Q_\delta=Q_0+\delta Z_{\rm can},\qquad
 |\delta|\le10^{-8},\qquad \eta_{\rm intrinsic}=\eta_0 ,
 \tag{AW.2}
$$
as PC, IN, RR and ST. The centre and canonical direction definition hashes are respectively
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47` and
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`.
The common physical root piece is 2549. On that piece the compact metric perturbation is zero, so the original root and the common intrinsic coefficients agree throughout this real family. The state, its true mean and its transport coefficients still depend on $\delta$.

The exact strict cut is
$$
 r_c=\frac{76285779072683}{320000000000000},\qquad
 r_*\in
 \left[\frac{1191984371497}{5000000000000},
       \frac{2383968743003}{10000000000000}\right].
 \tag{AW.3}
$$
This is the cut of RR, TN, TC and ST, not the old SP endpoint and not radius $1/200$. The successful IN/RR domain gates place this cut in the same genuine and free products. The successful PC signed-disk domain contains the whole portion between this cut and the root, as well as its separately paid positive transition.

Let
$$
 {\cal X}^s_{97}
 =\left\{(a_j)_{|j|\ge97}:
      \sum_{|j|\ge97}\Lambda_j^{2s}|a_j|^2<\infty\right\},
 \qquad \Lambda_j=\sqrt{1+16j^2}.
 \tag{AW.4}
$$
The initial identities are on its finite Fourier sums, with $n=4|j|$ and both signs $\epsilon=\operatorname{sgn}j$.

There are two different pairs of labels. The genuine radial reference matrix has a terminal-Ai column and a growing reference column. The negative oscillatory decomposition of either reference column has two wave branches. Define the norm-one reference injection
$$
 \iota_{\rm dec}:{\cal X}^s_{97}\longrightarrow
     {\cal X}^s_{97}\otimes\mathbb C^2,\qquad
 \iota_{\rm dec}a=(a,0),
 \tag{AW.5}
$$
in the original input-reference order of IN.2. This selects exactly the normalized terminal-Ai column used by PC. It retains both physical signs and both oscillatory wave branches. It does not project the output onto one wave and does not remove the nonzero $\beta_n$ or the other entries of the input-diagonal comparison matrix.

For a complete physical state $h(r)$, set
$$
 {\mathfrak D}_r h
   =\left(Iw(r),\Pi w(r)\right),\qquad
 w=n_gT(q)h,\quad n_g=\frac{a_{\rm phys}^2}{m^2},\quad
 q=\sqrt{-K},\quad I=\partial_\phi^{-1}(1-\Pi).
 \tag{AW.6}
$$
At a strict circle this is the same primitive-plus-mean density map as ST.3--ST.4 and RR. Both mean coordinates are included. Its target is
$$
 {\cal Y}_r=L^2_{\phi,0}(\mathbb C^2)\oplus\mathbb C^2 .
$$
The angular variable in this definition is the original moving angle. No phase-circle pullback or new primitive is implicit.

## 2. Exact full-state Cauchy continuation below the cut

Write the original physical linearized equation as
$$
 {\cal L}h=\partial_r h-{\cal A}(r)h .
 \tag{AW.7}
$$
The operator ${\cal A}$ is the complete moving operator, including drift, local reaction, angular primitive and the full mean-rank terms. Let ${\cal E}(r,c)$ denote its homogeneous physical Cauchy evolution on the negative strict interval, with both state components, all Fourier coordinates, both means and all original one-sided coefficient seams.

This is a prescribed-data evolution. It is not a two-ended boundary inverse. On the compact strict interval $[0,r_c]$, the exact primitive--mean equations of SP have real characteristic speeds, bounded complete coefficients, bounded primitive/rank terms and the positive endpoint denominators verified by the successful strict certificates. They give the unique full-state evolution: construct it on smooth data by angular regularization, use the complete energy estimate, and pass to the primitive-density completion. The two mean equations are part of the system and the zero mean of the primitive component is preserved by its exact equation.

The completed ST result states, on this same completion,
$$
 {\cal U}_{0c}:={\mathfrak D}_0{\cal E}(0,r_c)
                            {\mathfrak D}_{r_c}^{-1},
 \qquad
 \|{\cal U}_{0c}\|_{{\cal Y}_{r_c}\to{\cal Y}_0}
       \le G_{c\to0}.
 \tag{AW.8}
$$
Its saved complete upper ball is
`[36.73318013558955353160134784914924794029878928743332 +/- 4.18e-51]`.
For a zero-mean primitive pair $u$ and a constant pair $z$, the exact inverse coordinate is
$$
 {\mathfrak D}_r^{-1}(u,z)
   =T(q)^{-1}n_g^{-1}(\partial_\phi u+z).
 \tag{AW.8a}
$$
It has the raw $H^{-1}$ state as its target; this formula restores both means and does not invert a discarded finite block.

The opposite radial factors and the complete two means are already included in this value. The displayed inverse density map is the exact coordinate identification in the definition of ${\cal U}_{0c}$, not a second numerical factor to be inserted.

If the strict coefficients are only given piecewise, ${\cal E}$ uses the original matching rule at each seam. A homogeneous continuation carries no extra raw state jump at those seams. Independent prescribed jumps are separate affine inputs and remain separate below.

## 3. The P.22-anchored genuine trial has no new jump source

Let ${\sf H}^V a$ be the complete genuine curvature trial of PC.4--PC.7 for the input (AW.5):
$$
 h_{2,n}=(1-\Pi)n^{7/6}{\cal U}_n
                  (w_0+n^{-1}w_1^V),\qquad
 h_{1,n}=J(D_0-B_{\rm op})h_{2,n}.
 \tag{AW.9}
$$
It uses the normalized terminal-Ai solution with its actual root shear, the original signed amplitude, exact old angular inverse, and the same true mean residual. Multiplication by the positive cutoff is applied to both physical rows, exactly as in PC.8--PC.9.

Define a new extension only on the negative side:
$$
 {\sf H}^{V,c}a(r)=
 \begin{cases}
 {\cal E}(r,r_c)\,{\sf H}^Va(r_c),&0\le r\le r_c,\\
 {\sf H}^Va(r),&r_c\le r\le r_* .
 \end{cases}
 \tag{AW.10}
$$
The positive-side trial and its cutoff are not changed. Both physical rows agree at $r_c$.

For a piecewise state with a jump at a fixed cut, the distributional radial derivative adds the jump times $\delta_{r_c}$. The angular, local, primitive and mean-rank terms in ${\cal A}$ do not add such a radial atom. Since the jump in (AW.10) is zero, the exact distributional residual on the negative side is
$$
 {\cal L}{\sf H}^{V,c}a
       ={\bf1}_{[r_c,r_*]}\,{\cal L}{\sf H}^Va .
 \tag{AW.11}
$$
Endpoint values of the characteristic function are immaterial for the ordinary source. This identity is in the complete physical two-row system. Reconstructing the first row again from a cut-off scalar second row would be a different trial and would not prove (AW.11).

The original root-piece amplitudes and coefficients are smooth through this cut. Across other old seams, (AW.10) uses ${\cal E}$ with the exact original physical matching. Thus no new affine impulse is created. The complete ordinary even mean of the genuine residual is restricted together with the rest of the residual; it is not deleted.

Multiplication by ${\bf1}_{[r_c,r_*]}$ and zero extension outside that set are contractions in each of the original true-$dr$ volume source norms. This remains true uniformly for the whole exact root bracket. The successful RJ/PC negative estimate already covers the larger original support, including the uncertain-root band, full first source and independent mean source. Consequently its completed bound $C_-$ remains valid for (AW.11), with no new radial integral and no transfer from a negative profile to a positive one.

This is exactly the restriction/zero-extension option stated in PC Section 9. It changes the comparison trial below the chosen cut. It does not change the selected positive column or its complete negative Cauchy continuation.

## 4. The actual PC correction is unchanged, including its finite root input

For finite input sums, let $\Psi a$ be PC's corrected positive high column:
$$
 \Psi_+a=P_H\chi{\sf H}^Va+e_+(a).
 \tag{AW.12}
$$
The correction $e_+$ is supplied by the already completed full-real-$\delta$ positive seven-port graph with stable correction input zero, ordinary source equal to the negative of PC's complete projected high residual, supplied finite head zero, and all independent exterior and affine inputs zero.

The actual stable trace of $P_H{\sf H}^Va$ is retained:
$$
 S_{\rm tr}^Ya=
   Y_{\rm stable}(P_H{\sf H}^Va)(r_*).
 \tag{AW.13}
$$
It is the same before and after correction. It has not been set to zero or replaced by a bounded arbitrary $L^2$ input for $a\in{\cal X}^{-4/3}_{97}$. The positive high equation and its exterior condition are satisfied by (AW.12). Its finite equations and mean equations remain independent rows.

Continue the complete corrected root state to the negative side by the original physical Cauchy equation. The difference from the trial at the root contains
$$
 e_+(r_*)-P_F{\sf H}^V(r_*),
 \tag{AW.14}
$$
with the original mixed-root conversion. The second term is the complete finite root vector, including its means. Zero supplied positive head in (AW.12) is not permission to remove (AW.14).

The anchored extension (AW.10) has the identical root value and the identical positive side. Its negative residual is merely the contraction (AW.11). Therefore the original complete three-term PC estimate gives
$$
 {\cal E}_{{\rm PC},c}
      :={\mathfrak D}_0(\Psi-{\sf H}^{V,c}),
 \qquad
 \|{\cal E}_{{\rm PC},c}\|_{{\cal X}^{-4/3}_{97}\to{\cal Y}_0}
 \le
 9C_R\omega_1C_++C_RC_F+C_OC_-
 =:C_{\rm PC}^{\rm alg}.
 \tag{AW.15}
$$
The actual saved complete bound $C_{\rm PC}$ dominates that positive algorithm. Its accepted ball is
`[1018227964328341484881354948482360.900886437770295542 +/- 1.43e-19]`.

The root factor $9$, all mixed-root factors, the ordinary collar port, the finite head, the complete negative source, both means and the true radial measure are already included in this bound. The actual negative-one graph reflection is used; it is not replaced by $1/2$ or by the smaller reflection of a different Sobolev window.

In particular (AW.15) pays the PC correction for this precise anchored trial. It does not subtract one unknown operator from another using their upper bounds. No estimate for the full individual trial in ${\cal Y}_0$ is required.

## 5. The same anchor converts the completed Darboux comparison into the ST contribution

Let ${\sf H}^0$ be the original free P.8 first-transport trial, with the same real fold, the same $w_0,w_1$, both curvature rows and the same old projection/inverse convention. Its input reference matrix is the free two-column Airy matrix of IN.2.

IN.8 and IN.13 give the exact same-cut difference between the genuine and free trials. The full root input multiplier, including nonzero $\beta_n$, is retained. The two inhomogeneous reconstruction terms and the free $R_2,R_3$ products are retained. The original old-mean projections are in the order fixed by the [final DR contract](R133-supplement-complete-strict-physical-Darboux-receiver.md); the two physical output means remain independent.

Write its complete signed map as
$$
 \Delta_c={\mathfrak D}_{r_c}
            \bigl({\sf H}^{V}_{\rm two\,ref}
                        -{\sf H}^{0}\bigr)(r_c).
 \tag{AW.16}
$$
The four complete RR components of this map are exactly the objects labeled `error_density_0`, `error_density_1`, `free_R2` and `free_R3`. Their signed expression is the one in IN.8 and IN.13. The successful bounds include their already assigned powers of $n$, primitive readouts, $J/L/B$ actions, radial factors, full source reconstruction and means. No new power of $n$, $\eta^{-1}$, $\sqrt{17}/4$ or root-coordinate factor is attached here.

Define the anchored free state by
$$
 {\sf H}^{0,c}a(r)
    ={\cal E}(r,r_c)\,
         {\sf H}^{0}(r_c)\iota_{\rm dec}a,\qquad 0\le r\le r_c .
 \tag{AW.17}
$$
Linearity of the same homogeneous physical evolution yields
$$
 {\mathfrak D}_0({\sf H}^{V,c}-{\sf H}^{0,c})
       ={\cal U}_{0c}\,\Delta_c\,\iota_{\rm dec}.
 \tag{AW.18}
$$
The four completed ST columns are precisely the estimates for the right side before restriction by the norm-one map $\iota_{\rm dec}$. ST multiplies each complete RR case by the single $G_{c\to0}$, forms the complete case sum, and only then takes the case maximum.

Thus the actual saved complete same-case bound gives
$$
 \|{\mathfrak D}_0({\sf H}^{V,c}-{\sf H}^{0,c})\|
_{{\cal X}^{-4/3}_{97}\to{\cal Y}_0}
 \le C_{{\rm ST},4},
 \tag{AW.19}
$$
whose original outward ball is
`[285704814464526022070.2591010762034890706384188211054 +/- 2.24e-33]`.

The use of the terminal-Ai input in (AW.18) does not discard the growing component generated by the full root comparison matrix acting on that input. It also does not discard either negative wave branch. Both are already inside $\Delta_c$ and its accepted complete estimate.

## 6. Exact telescoping and completed strong comparison

For every finite input sum, add the two actual differences:
$$
 \begin{split}
 {\mathfrak D}_0\Psi
     -{\mathfrak D}_0{\sf H}^{0,c}
 ={}&{\mathfrak D}_0(\Psi-{\sf H}^{V,c})
       +{\mathfrak D}_0({\sf H}^{V,c}-{\sf H}^{0,c})\\
 ={}&{\cal E}_{{\rm PC},c}
       +{\cal U}_{0c}\Delta_c\iota_{\rm dec}.
 \end{split}\tag{AW.20}
$$
This proves (AW.1). Both terms already have the required strong input and output spaces. Their sum extends uniquely from finite sums to ${\cal X}^{-4/3}_{97}$ with values in ${\cal Y}_0$. The argument extends the **difference**; it does not infer that each order-zero trial or the nonzero stable trace separately maps ${\cal X}^{-4/3}_{97}$ into $L^2$.

No new mathematical consumer is needed for the operator identity. A later numerical ledger may add the two stored upper endpoints once using directed arithmetic if it needs a single decimal ball. Until then the exact expression $C_{\rm PC}+C_{{\rm ST},4}$ is the bound.

The selected high columns are unchanged by the choice of negative comparison extension. In particular the complete stable factor is still the one in IN.28:
$$
                         \Psi_H={\cal P}_+S_{\rm tr}^Y .
 \tag{AW.21}
$$
The nonzero stable factor can be canceled in an incoming/outgoing ratio only in the complete natural-domain identity of IN.29, with all finite cross maps retained. Equation (AW.20) does not commute that factor through a Fourier projection and does not prove its inverse at cutoff 97.

## 7. Independent ports and the remaining free first-symbol work

The zero values in the construction of $e_+$ specify this one correction problem. For additional genuine positive source, exterior, head, root, seam or strict-source data, retain the complete original PW port operator. By linearity the comparison becomes
$$
 {\mathfrak D}_0\Psi[a,p]
   ={\mathfrak D}_0{\sf H}^{0,c}a
       +E_{\rm AW}a+{\cal G}_{\rm PW}p,
 \tag{AW.22}
$$
whenever $p$ lies in the exact source and trace spaces of those original ports. The full three independent mean rows, finite root/head maps and physical affine jumps have not been absorbed into $E_{\rm AW}$. No new fee or source window for $p$ is asserted here.

For any subsequent complete incoming or outgoing receiver ${\cal R}$ bounded from ${\cal Y}_0$ to its declared $L^2$ coordinate, the immediate consequence is
$$
 \|{\cal R}E_{\rm AW}\|_{{\cal X}^{-4/3}_{97}\to L^2}
      \le\|{\cal R}\|\,(C_{\rm PC}+C_{{\rm ST},4}).
 \tag{AW.23}
$$
Its leading multiplier, true circle map and any finite-rank mean correction must be part of that receiver's actual norm and order. TC's strict-cut coordinate norm cannot be relabeled as a waist coordinate norm. Equation (AW.23) is the typed interface, not an unpaid identification of the receiver.

The remaining free-symbol problem is now concrete: compare
${\mathfrak D}_0{\sf H}^{0,c}$ with the correctly ordered first-symbol incoming/outgoing maps. This includes:

- The first omitted free-Airy term and complete finite angular-inverse reconstruction at $r_c$, in the actual P.24 convention.
- The complete remainder produced by propagating those first-symbol trial amplitudes and branch coordinates from $r_c$ to the waist, with all nonlocal rank, mean and finite terms.
- The leading incoming/outgoing coordinate factors, their two Sobolev windows, actual incoming error and inverse, and the resulting finite complement.
- Every independently supplied port in (AW.22).

The already paid free $R_2,R_3$ terms in (AW.19) are Darboux comparison terms. They are not substitutes for the first omitted free-Airy/first-symbol remainder in this list. Likewise $C_{\rm PC}$ and (AW.1) are base-window $s=0$ strong errors. No all-$s$ family or whole return $R_0$ has been inferred.

## 8. Exact reusable evidence

The following immutable objects determine the result. Only their complete small conclusions and original proof identities are used.

| Object | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| PC analytic contract | `35f3ddaec691c2d7c636ec43da3f52605ed6b329` | 37079 | `5368abae4c66f73800c16d5f2b906ddaa0f1d62d07e9bd9a3ca539061bdf5d68` |
| [PC actual report](R133-supplement-actual-genuine-positive-Airy-cutoff-and-complete-strong-correction.md) | `2dd428006e36c3e7a8651ba3908d932bf58fc0e5` | 34946 | `b2acc64af2f848bb3fa20b6ff2694aa072a3299b5a206145cb9d765c4901d802` |
| [PC execution 43740173506/1](../notes/genuine_positive_Ai_cutoff_strong_correction_ci/run-43740173506-1/execution.json) | `c32b8e3f3aca08d338784504c2cce5054d203bc6` | 46253 | `75f780f60446bd2a47fe286e72ca24fad929e3486c12d9ecbea42f42b9b1a817` |
| [IN exact Darboux contract](R133-supplement-genuine-Darboux-comparison-and-complete-incoming-factorization.md) | `f13509b4d0afc691cfc95d86c0f8e5562f919129` | 33894 | `d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75` |
| [RR execution 43750683671/1](../notes/root_mean_value_saved_product_Darboux_receiver_ci/run-43750683671-1/execution.json) | `ef746ab2c3c0975eafe1fb4354d1a86cc1cc9510` | 51791 | `a75da290077cf0e134834be5e35a0fa7cd55cd79104f5128d87eaee898af162b` |
| [ST analytic contract](R133-supplement-complete-strict-tail-from-true-branch-cut-to-waist.md) | `7fe7d81a6f2e91b69cdd0446efdfacd6ba6b68e7` | 22403 | `b15c1630edba1510dc293dea447d4bfe8144680cf73523c3b3b7a237949d5938` |
| [ST execution 43757644616/1](../notes/strict_tail_true_cut_to_waist_ci/run-43757644616-1/execution.json) | `94eb4c7d643edc33f696d101753e4d23a7936a26` | 47282 | `b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637` |
| [Original root parametrix, P.8 and P.22--P.26](R133-supplement-actual-moving-root-parametrix-and-scalar-finite-part.md) | `11250cbb5f9921fdaa70791b6095c306e16bc5d7` | 35230 | `f8268dc8c299fdb5813034efcd259f27d660faba0b9324cfd3865f878c8fcbe7` |

PC's actual scientific child had 30 passed gates, RR's 28 and ST's 25. They remain frozen successes. This note neither evaluates their source budgets nor restores a profile, amplitude, target, potential, ray, matrix, old native or mean calculation. It closes the comparison (AW.20) by an exact support and continuation argument using their already complete source domains.
