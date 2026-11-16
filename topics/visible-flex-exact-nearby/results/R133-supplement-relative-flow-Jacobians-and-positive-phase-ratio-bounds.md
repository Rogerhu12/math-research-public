# R133 supplement: relative flow Jacobians and positive phase-ratio bounds

2026-11-16. New exact identities and a first complete scalar-consumer contract.

This note improves the angular *relative* comparison without changing any characteristic, phase, trial, or physical row. Its first step divides the exact differentiated flow equation by the actual positive Jacobian. The linear growth term then cancels before absolute values are taken. This is a different proof from dividing two independently saved upper bounds.

The completed WBF computation, run 43870348355/1, is an immutable input. All 83 of its targets remain saved and are not evaluated again. The new consumer declared below has 56 new scalar targets in four complete graphs. It requires no numerical exponential, logarithm, square root, fractional power, flow integration, or quadrature. No numerical improvement is claimed before those new targets are evaluated.

## 1. The same real flows and the complete first comparison budget

Use the selected real member and original intrinsic parameter of WBF, WDG and WGS. The strict interval and its actual cut are
$$
 I_{\mathrm s}=[0,c],\qquad
 c=\frac{76285779072683}{320000000000000}.
 \tag{WJR.1}
$$
Nothing in this note enlarges that interval to the root germ, a complex strip, or a parameter family.

The three relevant real characteristic velocities are the two original phase velocities and the drift velocity. In the forward radial convention used for the cut representation, they are
$$
 v_\sigma(s,\phi)=-d(s,\phi)-\sigma\eta(s)q(s),
 \quad \sigma\in\{-1,1\},
 \qquad v_0(s,\phi)=-d(s,\phi).
 \tag{WJR.2}
$$
The theorem also applies to their reversed orientations on every shorter interval. Reversal changes the signed velocity, not the absolute derivative comparison below. The radial term in (2) has no angular derivative.

Let $\chi(s,\phi)$ denote any one of these same directed flows, initialized by the identity at the chosen initial endpoint. The fixed periodic angular coordinate has period $\pi/2$. Its lift is increasing; its zeroth lift value is neither assumed periodic nor assigned a finite Fourier norm.

The complete reference drift has label bandwidth 192 and physical bandwidth
$$
 B=768.
$$
The sharp Bernstein theorem in WBF supplies, for $1\le k\le15$,
$$
 \|\partial_\phi^k v(s,\cdot)\|_\infty
       \le B^{k-1}D(s),\qquad D(s)\ge0.
 \tag{WJR.3}
$$
The already saved first flow record $F_*$ has the stronger, original WX positive-algorithm qualification
$$
 \exp\!\left(\int_{\text{any admitted directed shorter interval}}D(s)\,ds\right)
       \le F_*,
 \qquad F_*\ge1.
 \tag{WJR.4}
$$
It is not merely an arbitrary upper bound for a derivative norm. The two orientations, both original phase flows, and the drift are all covered by the same complete comparison proof. No new comparison for an unrelated flow is inferred.

All formulas are ordinary angular derivatives. The piecewise radial construction and its true interfaces remain intact. The differential identities can be integrated on each original piece and concatenated using the actual continuous flow; no radial derivative of a background coefficient is needed here.

## 2. Divide the exact high-derivative equation by the actual Jacobian

For the chosen flow, put
$$
 J=\partial_\phi\chi>0,\qquad
 Y_j=\frac{\partial_\phi^j\chi}{J}\quad(j\ge1),\qquad Y_1=1.
 \tag{WJR.5}
$$
The genuine Jacobian satisfies
$$
 \partial_sJ=v_\phi(s,\chi)J.
 \tag{WJR.6}
$$
Write $\mathcal B_{j,k}$ for the ordinary partial Bell polynomial. Differentiating the actual flow and then differentiating the quotient in (5) gives, for $j\ge2$,
$$
 \partial_sY_j
 =\sum_{k=2}^{j}
    \partial_\phi^k v(s,\chi)\,
    J^{k-1}\,
    \mathcal B_{j,k}(1,Y_2,\ldots,Y_{j-k+1}).
 \tag{WJR.7}
$$
The $k=1$ term cancels exactly against the derivative of the denominator. The equality precedes every norm estimate. It uses $J>0$, not a stored lower bound for $J$.

To check the powers in (7), every monomial of $\mathcal B_{j,k}$ has $k$ flow-derivative factors. Substituting $\partial_\phi^m\chi=JY_m$ therefore produces $J^k$, followed by the single denominator $J$. The right side only involves $Y_2,\ldots,Y_{j-1}$; it is triangular. At the initial endpoint, $Y_j=0$ for $j\ge2$.

Let
$$
 A(s)=\int_{\text{initial endpoint}}^{s}D(\tau)\,d\tau,\qquad
 F(s)=e^{A(s)}.
 \tag{WJR.8}
$$
The directed parameter increases from the chosen initial endpoint, so $A\ge0$, and the ordinary first variation gives $J(s,\phi)\le F(s)$. By (3) and (7), absolute values of the $Y_j$ are bounded inductively by the solution of the positive triangular comparison with $J$ replaced by $F$ and $|\partial_\phi^k v|$ replaced by $B^{k-1}D$.

This argument does not estimate an unknown ratio by a quotient of two upper bounds. In particular, neither the old WBF value of $F_{j+1}$ nor the original strict phase lower is divided into a putative Jacobian ratio.

## 3. An explicit positive polynomial for every relative Jacobian derivative

The finite comparison can be solved at the level of formal derivatives. Use the same formal majorant as WBF,
$$
 \partial_A W=\frac{e^{BW}-1}{B},\qquad W(0,h)=h.
 \tag{WJR.9}
$$
Its first derivative at $h=0$ is $W_1=F$. If $W_j=\partial_h^jW(A,0)$ and $Z_j=W_j/F$, then differentiating $Z_j$ cancels the linear $W_j$ term. The resulting triangular equations are precisely the positive comparison for (7), with $Z_1=1$. Thus
$$
 |Y_j|\le Z_j.
 \tag{WJR.10}
$$

For completeness, the formal solution and its finite derivatives are
$$
 W(A,h)
 =h-\frac1B\log\!\left(1-(F-1)(e^{Bh}-1)\right),
$$
$$
 W_j=B^{j-1}\sum_{k=1}^{j}(k-1)!\,S(j,k)(F-1)^k,\qquad j\ge2,
 \tag{WJR.11}
$$
where $S(j,k)$ denotes a Stirling number of the second kind. These are proof identities; the numerical consumer does not evaluate either transcendental function.

The Stirling recurrence gives the exact polynomial factorization
$$
 \sum_{k=1}^{b+1}(k-1)!S(b+1,k)t^k
   =(1+t)\sum_{k=1}^{b}k!S(b,k)t^k.
 \tag{WJR.12}
$$
Indeed, the coefficient of $t^k$ on the right is
$k!S(b,k)+(k-1)!S(b,k-1)=(k-1)!S(b+1,k)$.
Consequently the factor $F=1+t$ is removed algebraically in the comparison, without any numerical reciprocal.

Set
$$
 t_*=\operatorname{upper}(F_*)-1\ge0,\qquad
 {\cal J}_0=1,\qquad
 {\cal J}_b=B^b\sum_{k=1}^{b}k!S(b,k)t_*^k
 \quad(1\le b\le14).
 \tag{WJR.13}
$$
Then every admitted directed shorter flow satisfies the complete ordinary bounds
$$
 \boxed{\quad
 \frac{|\partial_\phi^bJ|}{J}
 =\frac{|\partial_\phi^{b+1}\chi|}{\partial_\phi\chi}
 \le{\cal J}_b,\qquad 1\le b\le14 .
 \quad}
 \tag{WJR.14}
$$
All coefficients in (13) are nonnegative integers. The parameter $t_*$ is the known positive comparison-budget parameter from (4); its construction is not subtraction of an operator upper to claim an unknown operator difference.

The case $F_*=1$ is included: $t_*=0$, so all ${\cal J}_b$, $b\ge1$, vanish. No division by $t_*$, $F_*-1$, or a relative derivative is present.

The already completed WBF ordinary flow records
$$
 f_j\ge\|\partial_\phi^j\chi\|_\infty,\qquad 1\le j\le14,
 \tag{WJR.15}
$$
remain independent read-only inputs for compositions. Their original orders 2 through 14 are not produced again. The new records in (13) certify a different quantity, namely the relative derivative of the actual Jacobian.

## 4. Relative phase derivatives using the true cut lower

Let $\Phi_\sigma$ be the same two genuine lifted phases. Along their original directed characteristics,
$$
 \Phi_\sigma(r,\phi)
   =\Phi_\sigma(c,\chi^\sigma_{r,c}(\phi)).
 \tag{WJR.16}
$$
Define the positive derivatives
$$
 p_\sigma=\partial_\phi\Phi_\sigma>0,\qquad
 g_\sigma(\phi)=\partial_\phi\Phi_\sigma(c,\phi)>0.
$$
The chain rule gives the exact product
$$
 p_\sigma(r,\phi)
   =g_\sigma(\chi^\sigma_{r,c}(\phi))J^\sigma_{r,c}(\phi).
 \tag{WJR.17}
$$

Use the genuine cut lower and complete original cut derivatives,
$$
 m_c\le g_\sigma(\phi),\quad m_c>0,\qquad
 C_j\ge\|\partial_\phi^j\Phi_\sigma(c,\cdot)\|_\infty
 \quad(2\le j\le15),
 \tag{WJR.18}
$$
uniformly for both signs. Here $m_c$ is the original WGS record cut_phase_lower. It is not the smaller global strict phase lower and is not a complex-strip nonvanishing claim. The $C_j$ are the complete original cut records already copied into WBF.

For each $1\le\ell\le14$, introduce the finite working expression
$$
 {\cal G}_0=1,\qquad
 {\cal G}_\ell
   =\sum_{k=1}^{\ell}\frac{C_{k+1}}{m_c}
           \mathcal B_{\ell,k}(f_1,\ldots,f_{\ell-k+1}).
 \tag{WJR.19}
$$
By the ordinary chain rule, ${\cal G}_\ell$ bounds the $\ell$-th derivative of
$g_\sigma\circ\chi^\sigma$, divided by its own positive value. The zeroth ratio is exactly 1; no $C_1/m_c$ loss is introduced.

Leibniz applied to (17), after division by the same positive product, yields the common complete targets
$$
 {\cal P}_0=1,\qquad
 {\cal P}_b
   =\sum_{\ell=0}^{b}\binom b\ell
                 {\cal G}_\ell{\cal J}_{b-\ell},
 \quad 1\le b\le14,
 \tag{WJR.20}
$$
and hence
$$
 \boxed{\quad
      |\partial_\phi^bp_\sigma|\le{\cal P}_bp_\sigma,
      \qquad \sigma=\pm1,\quad1\le b\le14 .
 \quad}
 \tag{WJR.21}
$$
The Bell polynomials in (19) use the already saved absolute flow bounds (15). The factors ${\cal J}_{b-\ell}$ use the newly saved relative-Jacobian records (13). Each successor reads the printed saved record of its predecessor. No first-order flow or phase target is recalculated.

The shared real phase average is
$$
 x=X_\phi=\frac{p_++p_-}{2}>0.
$$
Taking the sum of the two inequalities (21) gives
$$
 \boxed{\quad |\partial_\phi^b x|\le{\cal P}_b x .\quad}
 \tag{WJR.22}
$$
There is no additional factor 2 and no division by the global strict lower of $p_\sigma$. The single record ${\cal P}_b$ certifies both positive phase derivatives and their positive average. It is not a newly asserted upper for their absolute values.

Different branch-specific complete bounds could instead be combined by their whole maximum. The declared first consumer uses one common already qualified cut/flow envelope, so (20) is already common to both branches.

## 5. Insert the new common ratio into the positive drift representation

Write $\omega=(\Phi_--\Phi_+)/2>0$, and let
$\chi^0_{r,s}$ be the original drift flow with velocity $-d$. The exact WDG identity is
$$
 \omega(r,\phi)
 =\omega(c,\chi^0_{r,c}(\phi))
       +\int_r^c \eta(s)q(s)
                   x(s,\chi^0_{r,s}(\phi))\,ds.
 \tag{WJR.23}
$$
Every summand is positive on the same strict real interval. The initial cut term is retained in full.

Let ${\cal K}_b$, $1\le b\le14$, be the already completed WBF bounds for the relative derivative of the complete cut contribution. Their exact input paths are stated below. In particular the first ${\cal K}_1$ is the original immutable copied record; it is not multiplied again to recreate the same target.

Using (22) and the same already saved all-shorter drift bounds $f_j$, define the new complete bulk-composition targets
$$
 {\cal B}_b
 =\sum_{k=1}^{b}{\cal P}_k\,
                \mathcal B_{b,k}(f_1,\ldots,f_{b-k+1}),
 \quad 1\le b\le14.
 \tag{WJR.24}
$$
They bound the relative derivative of each $x(s,\chi^0_{r,s}(\phi))$, uniformly in the full ordinary radial integral. The radial weight $\eta(s)q(s)$ has no angular derivative.

Differentiate the exact sum (23) before using its positive weights. Dividing the resulting inequality by the same actual $\omega(r,\phi)$ gives
$$
 \boxed{\quad
 {\cal R}_b=\max({\cal K}_b,{\cal B}_b),\qquad
 \frac{|\partial_\phi^b\omega|}{\omega}\le{\cal R}_b,
 \quad1\le b\le14 .
 \quad}
 \tag{WJR.25}
$$
The point-dependent positive probability weights are used only after the derivative identity. They are not differentiated as an artificial representation. Both complete contributions are retained before the maximum, and there is no subtraction of old phase uppers.

The new ${\cal R}_b$ are a complete alternative 14-record packet for the same $\omega$. The earlier WDG and WBF packets remain immutable complete results. This proof neither assumes nor announces that the new packet is numerically smaller.

## 6. First exact read-only input closure

Only the following two complete actual files are required for the new arithmetic.

| Role | Complete actual file | Git blob | Bytes | SHA-256 |
|---|---|---|---:|---|
| WBF actual | notes/sharp_Bernstein_finite_flow_ci/run-43870348355-1/actual-scientific-conclusion.json | df5ea6fff610d70ad98fbebc9dd004d24388ce86 | 59417 | 87621adee76080dbbc14abdd7f8e5dce5d3e2742ba299fc941d13ff40f4410c0 |
| WGS main | notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json | 32ff92c516fcc5c43f3619930d4845d294289270 | 72251 | 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e |

All paths in this table are relative to topics/visible-flex-exact-nearby. The WBF actual binds that very WGS main and its original companion. The new reader must verify the complete bytes, field sets, original gates and status, source/manifest/runtime identity, retained scope, all 83 saved WBF slots, and the existing original-input chain. It must not fetch or execute an old producer.

The 43 consumed record objects are copied verbatim:

1. Fourteen absolute flow records $f_1,\ldots,f_{14}$. The first is WBF copied_original_scalar_records.flow_1. For $j=2,\ldots,14$, use complete_new_graphs.complete_new_sharp_flow_conclusion.new_records.ordinary_flow_orders_2_through_15 at index $j-2$. The already saved order-15 record remains in the complete source; it is not a new target here.

2. Fourteen cut records $C_2,\ldots,C_{15}$, from WBF copied_original_scalar_records.cut_phase_2 through cut_phase_15. Their complete original fields and both-sign qualification remain unchanged.

3. One genuine cut lower $m_c$, from WGS complete_higher_flow_and_cut_conclusion.cut_phase_lower. This is the only lower-endpoint scalar in the new arithmetic. Every norm record uses its saved upper endpoint.

4. Fourteen complete cut-composition records ${\cal K}_1,\ldots,{\cal K}_{14}$. The first is WBF copied_original_scalar_records.cut_composition_1. For $b=2,\ldots,14$, use complete_new_graphs.complete_new_sharp_transport_relative_conclusion.new_records.ordinary_cut_contribution_orders_2_through_14 at index $b-2$.

The new reader also preserves the full original mathematical qualifications and their array positions. The WBF copied scope archive includes the earlier WGS/WDG qualifications and the original scientific-success versus formatter-failure distinction. A later success is not used to rewrite any earlier operational status.

No new actual first-flow budget, cut derivative, absolute phase bound, cut-composition bound, square root, exponential, or old whole error is evaluated. The finite expressions ${\cal G}_\ell$ in (19) are working subexpressions of the new complete phase-ratio targets, not old scientific targets being rerun.

## 7. The 56 new targets and complete failure protocol

The first consumer is fixed to the following four complete graphs.

| Ordered graph | Newly saved target | Orders | New records |
|---|---|---|---:|
| relative Jacobian | ${\cal J}_b$, formula (13) | $b=1,\ldots,14$ | 14 |
| common positive phase and average | ${\cal P}_b$, formula (20), qualifying both $p_\sigma$ and $x$ | $b=1,\ldots,14$ | 14 |
| complete transported bulk ratio | ${\cal B}_b$, formula (24) | $b=1,\ldots,14$ | 14 |
| complete relative gap | ${\cal R}_b$, formula (25) | $b=1,\ldots,14$ | 14 |

There are 56 new records and no original record evaluated as a new target. The 43 original records are separately copied with their full object shape and exact source paths.

The source computes the Stirling and Bell coefficients as exact finite integers. Each complete new scalar is saved as a 75-digit directed record before it is read by a successor. The phase graph reads all 14 saved relative-Jacobian records; the transported bulk reads all 14 saved phase/average ratios; the final graph takes the maximum of the complete saved old cut candidate and the complete saved new bulk candidate.

The public execution is a single new scientific child with the same five scalar CLI arguments and unchanged frozen worker. Complete original records and qualifications are saved before importing the numerical library. Every record updates an atomic full prefix and the complete stdout before a size gate. A failure preserves all already computed targets and prohibits automatic rerunning of the same scientific attempt. Diagnostic limits do not truncate mathematical records.

A complete static output model, source pin, input manifest, field list, gate list, graph shapes, and actual progress counters must be frozen before the new Actions run. This proof does not replace that byte model with a promise about output size.

## 8. Downstream scope and limits

The packet in (25) consists of ordinary real angular ratios only. When WSJ forms a normalized frozen angular coefficient, it divides its saved upper by the exact $b!$ once. This note does not provide relative order15.

The new ${\cal P}_b$ have a separate explicit meaning: they bound the derivative of a positive $p_\sigma$ or $x$, divided by that same function. They may be used in a later complete finite mixed-jet construction only through a proved identity that preserves this normalization. They are not absolute phase derivatives and must not replace WBF's $P_2,\ldots,P_{15}$ by a mere relabeling.

All radial identities, frozen-$t_0$ conventions, full $H^{-1}$ and $\mu^{-1}$ matrices, geometry versus Wiener norms, $G$, genuine and free amplitudes, full potential extension, all retained powers, and all terminal terms remain under their original complete contracts. No radial derivative is gained by the cancellation in (7).

The actual angular $J$ inverse and $J_r$, two physical means, full scalar-mean equation and initial condition at the true root, all 3070 interfaces, ordinary radial lengths, jumps, the original PW cut, positive/root response, and all four waist endpoints remain unchanged. This note does not subtract anything from a saved received or whole-error upper.

The actual 96 physical columns and their still uncomputed signed normalization, $\nu$, $\Theta$, radial head, independent function-valued inputs, actual finite compatibility and Schur inverse, and nonlinear obligations remain separate. Neither a small angular bound nor completion of all 56 numerical targets proves any of those gates.

## 9. Primary proof identities

| Primary object | Complete identity |
|---|---|
| WBF sharp Bernstein and positive integrated flow theorem | [R133-supplement-sharp-Bernstein-and-integrated-finite-flow-jets.md](R133-supplement-sharp-Bernstein-and-integrated-finite-flow-jets.md); blob 0c1a3593617a4134ea875697a268b7b6eea3bb3b; 16027 bytes; SHA-256 2dd1cdc598fde3ca47ca1cf0d787fdc60b9ced5601654865cfc3736cdba6c323; published 8365203025845ba6ea9acb1896a50c07e151283b |
| WDG true drift positive-sum theorem | [R133-supplement-positive-drift-and-complete-relative-angular-fold-bounds.md](R133-supplement-positive-drift-and-complete-relative-angular-fold-bounds.md); blob 0e4bf6ce75e0450a3aab4a1fc2365ffdcacb9512; 27168 bytes; SHA-256 212385b518812e52cb934ef381e0664b34e155d8967ac5572a7830514a8a5ebb |
| WSJ normalized frozen mixed-jet interface | [R133-supplement-scaled-strict-mixed-jets-and-exact-fold-inverses.md](R133-supplement-scaled-strict-mixed-jets-and-exact-fold-inverses.md); blob 10c6e4220377b772692095347f096e5d897afc5e; 31568 bytes; SHA-256 217cdff81516dd827122987ba6abe9a2cdacb6597d01fe9b4ee58a47faa8960d |

The two actual input identities are stated in section 6. Their complete original mathematical successes and failures remain as recorded. This note performs zero new scientific evaluations.
