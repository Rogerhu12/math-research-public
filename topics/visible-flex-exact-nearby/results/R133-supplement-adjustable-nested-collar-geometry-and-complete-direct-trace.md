# R133 supplement: adjustable nested-collar geometry with complete direct angular trace rows

2026-11-15, visible-exact / root.

**Proved conditional statement.** The fixed inner half-width in NC is a choice, not a hypothesis forced by the equation. This note uses the same completed LC and NC/BD coefficients on the same outer collar, permits a smaller final half-width, and retains both complete five-column inequalities at one common geometry. It does not assign any unknown low, shell or body norm.

The original proofs are [LC](R133-supplement-saved-positive-collar-component-bounds-and-high-frequency-coercivity.md), [NC](R133-supplement-nested-collar-localization-and-direct-projected-first-angular-trace.md), and [BD](R133-supplement-complete-degree32-splitting-of-the-differentiated-collar-equation.md). The first successful fixed-geometry calculation is [actual NC/BD](R133-supplement-actual-nested-collar-localization-and-direct-first-angular-trace.md), public run 43733916510/1. Its 16 structural and 12 separate first-angular gates are already complete and must not be rerun.

## 1. Same state, outer window and complete inputs

Keep exactly the repaired selected reference, canonical full direction and fixed intrinsic parameter of LC, with
$$
 I_0=[17/20,19/20],\qquad c=9/10,\qquad L=1/20,\qquad
 |\delta|\le10^{-10}.
 \tag{NG.1}
$$
Let the same real continuous two-sided $H^1$ state $Q$ satisfy the declared equation and the chosen complete outer-collar hypothesis
$$
 \|Q-Q_\delta\|_{C^0(I_0\times\mathbb T)}\le\rho .
 \tag{NG.2}
$$
All six original LC radii are admissible hypotheses. Changing the cutoffs does not prove (NG.2), extend its interval, join two independently chosen states, or supply an interface match.

Set $z=P(Q-Q_\delta)$ with the original diagonal $P$, and take $J=96$ or $288$, $n=4(J+1)$. Retain
$$
 \begin{aligned}
 z_H&=H_Jz,&z_L&=\Pi_{\le J}z,&
 z_S&=(\Pi_{\le J}-\Pi_{\le J-64})z,\\
 F_0&=\|H_JF\|_{L^2(I_0\times\mathbb T)},&
 F_1&=\|H_JF_\phi\|_{L^2(I_0\times\mathbb T)},\\
 Z_L&=\|z_L\|_{L^2(I_0\times\mathbb T)},&
 Z_S&=\|z_S\|_{L^2(I_0\times\mathbb T)},&
 B_0&=\|z_H\|_{L^2(I_0\times\mathbb T)} .
 \end{aligned}
 \tag{NG.3}
$$
Both independent means belong to $z_L$. Every integral uses the true radial measure $dr$ and the original normalized moving circle. The angular frequencies are the physical $4j$.

Read the already proved full zero-order constants $b_p,C_S,C_L$ from LC, and set
$$
 k=\frac{b_p}{n},\qquad E=F_0+C_SZ_S+C_LZ_L .
 \tag{NG.4}
$$
The full first-angular gate $t_1<1$, its $b_{p,1},b_{r,1}$ and the complete trace factor
$$
 \mathcal T_J=p_c\sqrt{1+n^{-2}}
                 \sqrt{\frac{b_{p,1}b_{r,1}}{n}}
 \tag{NG.5}
$$
are those of NC. In the already completed scalar result the valid global LC upper bound for $p_c$ has been used and paid once. These coefficients are bounds on the entire outer window; they remain valid on every smaller interval below. No new energy or angular absorption gate is inferred from a change of width.

## 2. Arbitrary positive inner half-width

Choose $0<a<L$ and an integer $N\ge1$, and define
$$
 h=\frac{L-a}{N},\qquad
 I_i=[c-(L-ih),c+(L-ih)],\quad i=0,\ldots,N .
 \tag{NG.6}
$$
Thus $I_N=[c-a,c+a]$ and every successive loss of half-width is $h$.

A cutoff that is one on $I_i$, vanishes at the ends of $I_{i-1}$ and has derivative at most $1/h$ gives the same NC zero-order inequality
$$
 B_i:=\|z_H\|_{L^2(I_i\times\mathbb T)}
 \le kE+\frac{k}{h}B_{i-1}.
 \tag{NG.7}
$$
The complete ordinary source, low and shell terms have only been restricted; each is bounded by its original outer-window norm in (NG.3). The commutator with the radial cutoff contributes exactly $(1/h)B_{i-1}$ before multiplication by $k$. All actual drift, mean and rank terms remain those of LC/NC.

Induction yields
$$
 B_N\le\eta_{a,N}B_0+\sigma_{a,N}E,\qquad
 r_{a,N}=\frac{kN}{L-a},\qquad
 \eta_{a,N}=r_{a,N}^{\,N},\qquad
 \sigma_{a,N}=k\sum_{i=0}^{N-1}r_{a,N}^{\,i}.
 \tag{NG.8}
$$
This is a finite positive polynomial identity. It is valid also for $r_{a,N}\ge1$; such a choice may be unhelpful but is not a structural failure. A denominator $1-r_{a,N}$ is neither needed nor permitted as a replacement without its own sign check.

## 3. The two final cutoffs and the whole differentiated equation

On $I_N$, let $\chi_0$ equal one for $|r-c|\le a/2$, decrease linearly to zero at $|r-c|=a$, and vanish outside. Let $\chi_1$ be the triangle supported on $|r-c|\le a/2$, with value one at $c$. Then
$$
 \chi_0=1\ \hbox{on }\operatorname{supp}\chi_1,\qquad
 |\chi_0'|,\ |\chi_1'|\le\kappa_a,\qquad
 \kappa_a=\frac2a .
 \tag{NG.9}
$$
These are bounded Lipschitz cutoffs independent of the unknown state. The weak energy and angular-mollification argument of NC.20--23 applies directly; no unknown $H^2$ hypothesis or uncharged angular commutator is introduced.

Let $B_{10}^{\rm NC}$ denote the complete NC high-output coefficient from its exact differentiated equation, and retain
$$
 \Gamma_L^{\rm NC}
   =B_{10}^{\rm NC}+4JA_1^++(4J)^2d_+ .
 \tag{NG.10}
$$
For the band-refined BD formula retain its already proved complete high, shell and low derivative coefficients $D_H,D_S,D_L$. In particular, $D_L$ retains the full perturbation of the selected reference and the unknown state. The exact base band64 cancellation does not replace the full $A_1^+$ in the first-angular gate.

Use $M\in\{\mathrm{NC},\mathrm{BD}\}$ solely as a formula label, and put
$$
 \begin{aligned}
 B_H^{\rm NC}&=B_{10}^{\rm NC},&
 B_H^{\rm BD}&=D_H,\\
 \Gamma_H^M(a)&=B_H^M+\kappa_a^2b_p,&
 \Theta^M(a,N)&=\kappa_ab_p+\Gamma_H^M(a)\sigma_{a,N}.
 \end{aligned}
 \tag{NG.11}
$$
The factor $\kappa_a^2b_p$ is the product of the two actual cutoff derivative costs. To see it explicitly, first apply the zero-order angular estimate on $\chi_0z_H$:
$$
 \|H_Jz_\phi\|_{L^2(\operatorname{supp}\chi_1)}
 \le b_p\bigl(E+\kappa_a B_N\bigr).
 \tag{NG.12}
$$
The derivative of $\chi_1$ then contributes at most
$\kappa_ab_pE+\kappa_a^2b_pB_N$ in the differentiated source.

Before substituting (NG.8), the two complete differentiated source bounds are therefore
$$
 \begin{aligned}
 G_1^{\rm NC}
 &\le F_1+\kappa_ab_pE+
      \Gamma_H^{\rm NC}(a)B_N+\Gamma_L^{\rm NC}Z_L,\\
 G_1^{\rm BD}
 &\le F_1+\kappa_ab_pE+
      \Gamma_H^{\rm BD}(a)B_N+D_SZ_S+D_LZ_L .
 \end{aligned}
 \tag{NG.13}
$$
All norms in (NG.13) may be bounded by their outer-window versions. This step never truncates a nonlocal primitive or deletes an input mean. The finite-output mean rank is removed only where the original NC/BD high output projection removes it exactly.

## 4. Both complete five-column trace inequalities

The two-ended fundamental-theorem-of-calculus estimate and high Poincare inequality are unchanged. Using (NG.8) in (NG.13) proves
$$
 \boxed{\begin{aligned}
 \|H_J(Q-Q_\delta)(c)\|_{H^1_\phi}
 \le \mathcal T_J\{&
 F_1+\Theta^{\rm NC}F_0+
       \Theta^{\rm NC}C_SZ_S\\
 &+(\Gamma_L^{\rm NC}+\Theta^{\rm NC}C_L)Z_L+
       \Gamma_H^{\rm NC}\eta_{a,N}B_0\}.
 \end{aligned}}
 \tag{NG.14}
$$
Independently,
$$
 \boxed{\begin{aligned}
 \|H_J(Q-Q_\delta)(c)\|_{H^1_\phi}
 \le \mathcal T_J\{&
 F_1+\Theta^{\rm BD}F_0+
       (D_S+\Theta^{\rm BD}C_S)Z_S\\
 &+(D_L+\Theta^{\rm BD}C_L)Z_L+
       \Gamma_H^{\rm BD}\eta_{a,N}B_0\}.
 \end{aligned}}
 \tag{NG.15}
$$
Every coefficient in these inequalities is nonnegative. The output is the Euclidean pair $H^1$ norm in the same moving circle. A later pair-sum, physical-angle or density conversion remains a separate explicit step.

At $a=1/40$, (NG.6), (NG.9) and (NG.11) give exactly the fixed NC geometry and its two derivative bounds80. This is a symbolic consistency check, not authorization to repeat the successful fixed-geometry scalar calculation.

For a true residual-zero solution, the complete WC source balls and exact degree288 vanishing are unchanged. For an approximate residual, $F_0,F_1$ and its effects on the actual mean/log-speed remain independent obligations. If (NG.2) is separately proved, then
$$
 B_0\le p_+\rho\sqrt{|I_0|}.
 \tag{NG.16}
$$
This is conditional; it does not bound $Z_L$ or $Z_S$ by an already proved small quantity. The right-cap bound alone supplies neither the whole outer collar nor a smaller $\rho$.

## 5. A finite, reproducible choice of whole geometry

The new finite candidate set is
$$
 a\in\{1/100,1/200,1/400,1/1000\},\qquad N=1,\ldots,128 .
 \tag{NG.17}
$$
For each of the six original radii and both high projections, evaluate all four widths and all128 counts. There are6144 new parameter triples $(\rho,J,(a,N))$, with12288 complete formula rows. Full candidate receipts remain temporary; only the selected whole conclusions and exact audit identity are retained.

For each fixed $\rho,J$, include one additional baseline: the exact already published pair of NC/BD rows at $a=1/40$, with its already selected $N=13$ or39. Copy those original rows and their geometry and readouts byte-exact. Do not run the old64 counts again, and do not reconstruct old scalar bounds from rounded displayed numbers.

For a new candidate define its comparison score to be the larger of the two certified high-body coefficient upper endpoints:
$$
 \operatorname{score}(a,N)
  =\max\{(\mathcal T_J\Gamma_H^{\rm NC}(a)\eta_{a,N})^{\rm up},
          (\mathcal T_J\Gamma_H^{\rm BD}(a)\eta_{a,N})^{\rm up}\}.
 \tag{NG.18}
$$
The baseline score is read from its two saved complete rows. Select the smallest certified score among these complete choices. An exact tie prefers the saved baseline, then the width order in (NG.17), then increasing $N$. Both complete five-column rows, all three conditional readouts and the selected geometry must use that one choice.

An implementation must compare the actual outward bounds it retains, including any final bounded-length formatting. It may not claim an improvement of the published high coefficient from a comparison that is lost after output widening. Reusing the original baseline is always a valid option. This rule bounds the retained high-body score by the saved baseline score; it does not claim that each separate formula's high coefficient improves, and it does not claim that any other column or the full unknown error is optimized.

No entrywise minimum between widths, layer counts or formulas is used. Once all five actual nonnegative inputs are supplied, the two complete right sides may be compared as whole bounds. Unknown source/low/shell input sizes cannot be guessed to optimize an asserted actual trace.

## 6. Exact reuse and the next public consumer

Read only complete current small UTF8 inputs with exact sizes and SHA256 values. The essential immutable scientific objects are:

| Input | Bytes | SHA256 |
|---|---:|---|
| Complete LC compact science |55770|44b4da07b50dcca9be7671b8cb59b227999e76871237c25a1bc0aec4bc02492c|
| Original LC process |15189|a15e9b16d6867d0f69a85d9549ad66953f70b444e7d9462ec45281aadf84cb58|
| LC lossless recovery record |7905|22d627a37aeb0b5a519df4d82aa4de111f82caca15127e2081010e94c3820a41|
| Complete fixed-geometry NC/BD science |35707|83e06a289105254022cba13ae23ff102ce384c1ae9e2ade468e5cdc979654df6|
| Fixed-geometry NC/BD process |15995|3157ed355d059c032662f130b40f5952f564c7337a7ef986e8429ae019bc4057|

Read $b_p,C_S,C_L$ directly from the corresponding original LC case. The NC small result does not independently store $C_S,C_L$; dividing two rounded upper coefficients is not a valid way to recover them. Read $k,\mathcal T_J,B_{10}^{\rm NC},\Gamma_L^{\rm NC},D_H,D_S,D_L$ and the full angular gate from the corresponding completed NC/BD case. All original case labels, six radii, both means and the full selected parameter radius must agree.

The public consumer performs only the new finite formulas (NG.6)--(NG.18). It must not recalculate original targets, Fourier products, intrinsic jets, repair, ordinary-source integrals, LC coefficients, the fixed-geometry768 scalar triples, Green propagation or the independent MA high-domain result. The earlier LC output-format failure and its exact recovery remain part of the provenance.

Use the public repository's own Actions and320-bit Arb. Freeze source, exact parameters, analytic contracts and input hashes; verify the full immutable Python AST closure before the unique mathematical child. Retain every new trial in a temporary complete audit, with exact byte count and SHA256. Emit the entire small selected conclusion and report before terminal publication. Respect the current root README, real checked pulls, successful-result reuse, publication-size gates and actual topic-capacity limit.

No value of the new selected widths, layer counts or constants is asserted until that new public run completes. A failed sufficient choice is not a singularity or obstruction claim. The mathematical theorem remains conditional on the same complete state and domain.

## 7. Remaining actual interfaces

The direct trace proof avoids interpolating the narrow $H^{8193}$ estimate for this particular $H^1$ output. It neither proves nor extends that independent high regularity domain. Low and shell norms, the whole-collar $C^0$ hypothesis, left/right state matching, the physical inner-curvature readout, actual core existence, the true parameter and phase rows, and the final fixed-metric family remain separate tasks.

The next use is to pay the high-body part more efficiently while preserving the exact same low/shell receiver problem. A small high-body column alone never supplies an actual trace or the README's completion criterion.
