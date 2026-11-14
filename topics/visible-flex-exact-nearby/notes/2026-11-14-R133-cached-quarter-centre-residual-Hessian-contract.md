# R133: cached quarter-cell centre residuals for the complete known-trial Hessian

2026-11-14, tail_connector.

**Proved consumption contract.** This is a new use of already computed fixed-$\eta_0$ scalar jets. It does not change the continuous centre, the original finite trial $T$, the direction $w_0$, the physical angle, any of the four physical Green gains, or the unknown-operator Hessian contraction. Its purpose is to tighten the coefficients multiplying the same known trial $Tw_0$.

## 1. Exact inputs and coverage

Keep the 1,341 original local Hessian intervals and the previously completed physical Legendre/module norms of $Tw_0$ on those intervals. The new complete quarter continuation has 7,908 quarter domains: 7,844 new domains and 64 reused domains from the original successful pilot. The new domains retain the actual target midpoint jets and whole-interval third-derivative enclosures at affine parameter offset zero. These are inputs to the original moving-residual algebra, not permission to rerun a target.

For each original Hessian interval $I_i$, form a complete finite cover by intersections with the saved quarter domains. An enclosure valid on an entire quarter is also valid on its intersection; no new target evaluation is needed. Record every true rational intersection endpoint and its original jet/domain identity.

When any necessary cached midpoint or whole-third input is absent, use the original proved bound for that **entire** local Hessian row. In particular the 64 reused quarter rows are not asserted to contain fields that their producer did not save. No missing domain is silently interpolated and no successful original quarter is recomputed.

The raw moving candidate, continuous-repair definition, physical normalization, intrinsic target and fixed $\eta_0$ must have the same exact identities as the original cap source. The original whole-parameter bounds may still be used as conservative bounds at that fixed parameter.

## 2. Two different residual norms

For each component $U,V$, on a covered subinterval $I_{i,s}$ the original directed Fourier/radial algebra gives a finite polynomial plus complete error:
$$
 R^{\rm raw}(r,\phi)=
 \sum_{|k|\le96}\sum_\ell c_{s,k,\ell}x_s(r)^\ell e^{4ik\phi}
                      +E_s^{\rm fun}(r,\phi),\qquad |x_s|\le1 .
 \tag{C.1}
$$
Use the actual complex Fourier convention, or the original equivalent paired sine/cosine convention with the same weights. The even mean has one coefficient and is retained. Set
$$
 f_{s,k}=\sum_\ell |c_{s,k,\ell}|,\qquad
 \|E_s^{\rm fun}\|_{\text{joint }A^0(I_{i,s})}\le E_s .
 \tag{C.2}
$$
The complete remainder still has moving Fourier support $|k|\le96$. This is a property of the known centre residual, not a cutoff for an unknown input or the physical composed output.

The original Banach residual construction pays a joint coefficient error before taking a radial supremum. Consequently valid pointwise whole-cell bounds are
$$
 P_0^{\rm raw}=
   \max_s\left(\sum_k f_{s,k}+E_s\right),\qquad
 P_1^{\rm raw}=
   \max_s\left(\sum_k(1+4|k|)f_{s,k}+385E_s\right).
 \tag{C.3}
$$
They control $\sup_{r\in I_i}\|R^{\rm raw}(r)\|_{A^0,A^1}$.

For the coefficientwise radial-supremum norm needed by a divergence module, use instead
$$
 J_0^{\rm raw}=\sum_k\max_s f_{s,k}+\sum_sE_s,\qquad
 J_1^{\rm raw}=\sum_k(1+4|k|)\max_s f_{s,k}
                                      +385\sum_sE_s .
 \tag{C.4}
$$
For every $k$, the finite polynomial coefficient has supremum at most $\max_s f_{s,k}$. The error inequality follows from
$\sum_k\max_s e_{s,k}\le\sum_s\sum_k e_{s,k}$.
This proves (C.4) without charging the number of subcells to every finite coefficient. Only the unknown error sum is charged per piece. Repeated use of a quarter enclosure on genuine intersections remains safe.

The two pairs (C.3),(C.4) have different uses; the pointwise maximum is not substituted for the joint norm. An independently valid original bound may be compared by taking the smaller scalar upper bound in the same norm and for the same mathematical residual.

## 3. Physical normalization and the repair

Let
$$
 \alpha=6890507429876859/9007199254740992.
$$
Let $F_0,F_1$ be the already paid **physical-normalized** pointwise bounds for the residual change from the raw centre to the exact continuous repair. On every row define
$$
 r_0=\alpha P_0^{\rm raw}+F_0,\qquad
 r_1=\alpha P_1^{\rm raw}+F_1,
$$
$$
 \mathcal J_0=\alpha J_0^{\rm raw}+193F_0,\qquad
 \mathcal J_1=\alpha J_1^{\rm raw}+193F_1 .
 \tag{C.5}
$$
There are 193 signed Fourier slots, including zero, in the known repair residual. Thus the last pair is a safe promotion even if $F_0,F_1$ were proved only pointwise. The factor $\alpha$ is applied exactly once. If an original saved field already contains one repair copy, the equivalent increment is $192F_q$, not another $193F_q$.

All physical means remain. In particular the mean of the full Hessian contains the original $2z_Rz_h/m^3$ term; this is not set to zero by a nonmean projection.

## 4. Composition and the two exact source representations

Use the same proved inverse-angle displacement $\psi$ and background bounds $B,C,B_1,C_1,U,V,H_C,H_2$, with $J_*=\|\phi_\theta\|_\infty$ and $\phi_\theta=mC=1/(1+w)$.

For an ordinary $L^2$ source, real composition preserves the pointwise supremum. The derivative chain rule is exactly
$$
 \partial_\theta(R\circ\phi)
      =(R_\phi\circ\phi)\phi_\theta .
 \tag{C.6}
$$
Thus the original complete coefficients (L.7)--(L.10) of
[R133 local triangular Hessian](../results/R133-supplement-local-triangular-cap-Hessian-and-trial-source.md)
may be recomputed with the new $r_{U,0},r_{V,0},r_{U,1},r_{V,1}$. For example
$$
 \begin{split}
 t_{B,1}={}&C_1r_{U,0}+CJ_*r_{U,1}
       +(B_1C+BC_1)r_{V,0}+BCJ_*r_{V,1},\\
 t_{C,1}={}&2CC_1r_{V,0}+C^2J_*r_{V,1}.
 \end{split}
 \tag{C.7}
$$
No factor 96 from a joint composition estimate is inserted in these ordinary coefficients.

The first valid representation keeps the complete identity
$$
                  D^2\Psi[R,h]=-e\,x_\theta+Zx
 \tag{C.8}
$$
entirely ordinary for the known finite $x=Tw_0$. Its two norms are bounded using the same saved physical $L^2_rL^2_\theta$ norms of $x_B,x_C,\partial_\theta x_B,\partial_\theta x_C$. The mean of $\partial_\theta x_C$ is zero, while the mean in $Zx$ remains.

The second representation uses the previously proved identity
$-t_\theta e_h=-\partial_\theta(t e_h)+t(Ch_2-\langle Ch_2\rangle)$.
It keeps the remaining terms of the original complete second differential. Its ordinary coefficients use (C.3),(C.5); its two divergence coefficients use the joint composition bounds
$$
 R_A\le e^{384\psi}\mathcal J_0,\qquad
 R_A\le(1-c)\mathcal J_0+c\mathcal J_1,\quad
 c\ge(e^{384\psi}-1)/384,\quad0\le c\le1 .
 \tag{C.9}
$$
A directed upper endpoint may be chosen as the exact scalar $c$ because $1+cq$ remains a dominating chord for every $0\le q\le384$. Both coefficients are nonnegative. This does not rely on subtracting two independent norm upper bounds.

The full $e_h$ module bound, the primitive's true mean subtraction, all components of $DP[t]h$, and both remaining mean pairings in the original (C.20) are retained. The known-trial derivative is not replaced by a cutoff for an unknown solution.

## 5. Whole representation selection and the final bridge

On each original local row, each valid representation supplies one complete vector
$$
 (\mathcal O_B,\mathcal O_C,\mathcal D_B,\mathcal D_C).
 \tag{C.10}
$$
Choose the whole old vector, the whole new ordinary vector (with two zero divergence entries), or the whole new split vector. Never select one channel from each decomposition. The original physical Gram weights are unchanged: the even mean has weight one and nonmean sine/cosine slots weight one half.

For every whole selection, sum the squared local ordinary norms and the squared local coefficientwise-supremum divergence modules using their original definitions, then apply all four original physical Green gains. Ordinary norms already contain their actual radial length through the saved Legendre integral; divergence modules receive no extra radial length.

Compare only complete global bounds: all old, all new ordinary, all new split, and the coupled row selection. Each carries its matching four source norms and four fees. Changing the angular-divergence representation between radial rows creates no radial delta source.

Finally use the same original complete Hessian resolvent to obtain the additive known-direction error. The remaining $Z_{\rm even}-w_0$ still pays the old **complete moving error-operator norm**. The physical cap residual, true cut conversion, separate mean output, known high output and boundary errors remain separate original terms.

This contract certifies neither an improved unknown infinite error operator nor the true full cut source, finite193 response, global high/low inverse, parameter Schur complement or nonlinear solution. A public Actions consumer must retain all exact input/domain identities and its real process/native records. It performs no new target evaluation and no recomputation of any old physical residual or trial norm.
