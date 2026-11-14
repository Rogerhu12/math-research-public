# R133: residual-derivative split for a fixed complete cap trial

This contract concerns the exact repaired centre and the same complete physical trial $x=T w_0$ already used by public runs 43616252389 and 43618931236. It gives an additional valid Hessian source decomposition. Its numerical size remains to be consumed by the new public worker. The original complete physical cap error and unknown-input error operator remain unchanged.

## H.1. Exact four-source identity

Use the complete physical-angle definitions in the continuous-centre conjugation theorem:
$$
 h=(D\Psi)^{-1}x,\qquad t=PR,\qquad e=I_\theta(CR_2),\qquad
 e_h=I_\theta(Ch_2),\qquad \mu_h=\langle Ch_2\rangle_\theta .
$$
The original identity is
$$
 D^2\Psi[R,h]=-e x_\theta+DP[t]h-t_\theta e_h+
 W_\theta\{(CR_2)e_h+e\mu_h-\langle Ceh_2\rangle_\theta\}.
$$
On each true radial cell, use
$$
 -t_\theta e_h=\partial_\theta(-t e_h)+t(Ch_2-\mu_h).
$$
Thus the complete divergence source is $F_d=-t e_h$ and the complete ordinary source is
$$
 F_o=-e x_\theta+DP[t]h+t(Ch_2-\mu_h)
 +W_\theta\{(CR_2)e_h+e\mu_h-\langle Ceh_2\rangle_\theta\}. \tag{H.1}
$$
All three means in this formula remain. In particular the original even Hessian mean $2z_Rz_h/m^3$ is not set to zero. No radial differentiation of $R$ or of this decomposition occurs.

Write $C_*,B_*,C_1,B_1,U_*,V_*,H_C,H_2$ for the same proved background and inverse-differential bounds. On a cell let $R_U,R_V$ be the original saved complete physical-normalized residual bounds, including their continuous-repair fees. Set
$$
 \begin{aligned}
 T_B&=C_*R_U+B_*C_*R_V,&T_C&=C_*^2R_V,\\
 b_*&=C_*^2R_V/4+2C_*E_\infty,&
 E_\infty&=(\pi/8)C_*R_V .
 \end{aligned}
$$
The mean-zero projection is an $L^2$ contraction, so
$\|Ch_2-\mu_h\|_2\le C_*H_2\|x_C\|_2$. The new complete ordinary zero-order coefficients are therefore
$$
 \begin{aligned}
 \widetilde Z_{BB}&=T_CV_*,\\
 \widetilde Z_{BC}&=T_CH_C+
       (2C_*T_B+B_*T_C+B_1b_*)H_2,\\
 \widetilde Z_{CC}&=(3C_*T_C+C_1b_*)H_2 .
 \end{aligned} \tag{H.2}
$$
The two ordinary source norms on the cell satisfy
$$
 \begin{aligned}
 O_B&\le E_\infty\|x_{B,\theta}\|_{L^2}
          +\widetilde Z_{BB}\|x_B\|_{L^2}
          +\widetilde Z_{BC}\|x_C\|_{L^2},\\
 O_C&\le E_\infty\|x_{C,\theta}\|_{L^2}
          +\widetilde Z_{CC}\|x_C\|_{L^2}.
 \end{aligned} \tag{H.3}
$$
These are the already completed true-radial Legendre norms. They include radial length exactly once. The even mean has zero angular derivative and a retained zero-order contribution.

## H.2. The stored raw residual is a joint coefficient bound

For a radial cell $I$, write
$$
 \|f\|_{\mathscr A_j(I)}
   =\sum_{k\in\mathbb Z}(1+|4k|)^j\sup_{r\in I}|f_k(r)|.
$$
The following property is specific to the original stored producer, rather than an inference from a generic pointwise norm.

The original candidate conversion bounds each exact Fourier coefficient radius before summing. The target Taylor remainder is a radial scalar coefficient. Its absolute bound is also a joint angular norm, since it occupies only the zero angular slot. Addition and the product recurrence
$$
 E_{ab}\le N_aE_b+N_bE_a+E_aE_b
$$
remain valid in the Banach algebra $\mathscr A_0(I)$. The complete primitive acts coefficientwise by $(4ik)^{-1}$ for $k\ne0$, annihilates the mean, and therefore has joint norm at most $1/4$.

Finally, the original complete residual producer sums the Fourier norm of every retained radial power coefficient and adds the propagated remainder. That sum bounds the supremum of each Fourier coefficient before summation. Its saved first-order norm multiplies those coefficients by $1+4|k|$ and charges $385E$ for the remainder of exact support $|k|\le96$. Consequently its raw saved $A^0$ and $A^1$ values are joint bounds of the form above.

The exact source bodies establishing these facts are the unchanged
`fourfold_codazzi_reciprocal_continuous_residual_v3.py`,
`fourfold_codazzi_moving_continuous_residual.py`, and
`fourfold_codazzi_moving_residual_checkpointed.py`.
The complete merged raw residual is bound by SHA256
`6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1`
inside the exact local native. No original target, residual polynomial, primitive, or interface is recomputed.

For additional robustness, treat the repair difference fee $F_j$ merely as a pointwise-in-$r$ full $A^j$ bound. It has support in all 193 complex slots $|k|\le96$, so $193F_j$ is a safe joint bound. The local stored residual already includes one $F_j$. Hence use
$$
 J_j=R_j+192F_j,\qquad j=0,1 . \tag{H.4}
$$
This does not assume the repair is zero or silently promote a general pointwise norm to a joint norm.

## H.3. Actual physical-angle composition

Let $\psi_*$ be the complete joint inverse-angle displacement bound. For each frequency, composition costs at most $e^{4|k|\psi_*}$. Thus
$$
 \|\bar R\circ\phi\|_{\mathscr A_0(I)}
 \le e^{384\psi_*}J_0 . \tag{H.5}
$$
A further independent bound follows from the convex chord on $[0,384]$. For a chosen exact nonnegative scalar $c$ satisfying
$$
 c\ge\frac{e^{384\psi_*}-1}{384},\qquad c\le1,
$$
one has $e^{q\psi_*}\le1+cq=(1-c)+c(1+q)$ for every $0\le q\le384$. Therefore
$$
 \|\bar R\circ\phi\|_{\mathscr A_0(I)}
       \le(1-c)J_0+cJ_1 . \tag{H.6}
$$
The implementation chooses an outward upper endpoint for the exponential and then for this single chord slope. Increasing this slope preserves the pointwise chord inequality because $q\ge0$; both coefficients in (H.6) are nonnegative. All arithmetic in the complete expression remains directed. It does not independently choose inconsistent endpoints in a signed expression.

The old individually bounded frequency sum remains an independent option. Taking the smaller of (H.5), (H.6), and that old complete bound is legitimate. The zero mode has weight exactly one; no extra negative-frequency multiplicity is missing.

## H.4. Complete divergence modules

The exact inverse-angle differential gives
$$
 p_c=I_\theta(c-mC\langle c\rangle_\theta),\qquad
 e_h=-P_0(vp_c),
$$
where $P_0$ removes only the scalar Fourier mean. Consequently, in the complete coefficientwise radial module,
$$
 \|e_h\|_{\mathfrak M(I)}
 \le E_h\|x_C\|_{\mathfrak M(I)},\qquad
 E_h=\frac{V_A(1+|m|_{\max}C_A)}4 . \tag{H.7}
$$
Let $R_{U,A},R_{V,A}$ be the bounds from H.3, and put
$$
 T_{B,A}=C_AR_{U,A}+B_AC_AR_{V,A},\qquad
 T_{C,A}=C_A^2R_{V,A}.
$$
Then the two complete divergence source modules on the cell are bounded by
$$
 D_B=T_{B,A}E_h\|x_C\|_{\mathfrak M(I)},\qquad
 D_C=T_{C,A}E_h\|x_C\|_{\mathfrak M(I)}. \tag{H.8}
$$
The input modules are the previously completed 257-slot physical modules, with independent even mean Gram weight one and nonmean weight one half. They are not replaced by a local $L^2$ supremum. There is no radial-length factor in (H.8).

## H.5. Full cap consumption and scope

For each original one of the 1,341 radial cells, the consumer may choose either the original two-ordinary-source representation or the complete four-source representation (H.1). Selection is made for all four channels together. The choice depends only on $r$; the differentiated source is an angular divergence, so no new radial interface delta is introduced. The original trial and its actual radial derivative do not change.

For each channel, square and sum its cell norms and then take the square root. This exactly combines ordinary $L^2_rL^2$ sources. For divergence sources, the cell square sum is a safe upper bound for the full coefficientwise radial supremum. Apply all four already closed physical Green gains and the one original Hessian resolvent. The consumer also evaluates the all-original and all-new representations and selects only a complete valid additive.

The complete native records the old ordinary terms separately, the new terms, every joint-norm/chord fee, every chosen decomposition, and all 1,341 original row identities. It preserves every mean and all 1,977 original trial intersections. The six physical boundary errors and eight physical residual terms remain part of the independent original physical-cap error; none is altered by this consumer.

This gives only an optional smaller additive for the same known $w_0$. The remainder $Z_{\rm even}-w_0$ continues to use the original complete moving error operator. The unknown-input Hessian feedback, full low/high Schur complement, true response error and nonlinear existence are not concluded here.
