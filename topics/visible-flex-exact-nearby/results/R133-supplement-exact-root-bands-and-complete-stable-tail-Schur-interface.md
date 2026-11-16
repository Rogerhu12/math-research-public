# R133 supplement RBT: exact root bands and the complete stable-tail Schur interface

2026-11-16, tail_connector.

**Exact root-frequency identities and a conditional stable-tail criterion; no numerical evaluation.** On the original root circle, the complete genuine height correction has bandwidth at most384 and the complete bounded root remainder has bandwidth at most576. The root inverse J is not assigned a finite bandwidth. For an original input cutoff above576, the primitive before that inverse has the improved exact gap 4(Jt−576). The remaining original labels97 through Jt−1 form an actual finite Schur problem; they do not disappear.

The original cutoff97 criterion and its new scalar consumer remain unchanged. No tail cutoff, finite inverse, incoming inverse or nonlinear state is certified by this supplement.

## RBT1. Same reference, original circle and exact support

Use the original real repaired family, fixed intrinsic eta0 and analytic root piece of [RD](R133-supplement-exact-leading-root-derivative-and-complete-stable-trace-gate.md), with the original terminal-Ai normalization and both physical input signs. The family qualification is the same real absolute delta at most ten to the minus eight. All coefficient bounds used together below must cover that same root and family.

The exact finite support comes from the explicit centre and response definitions, as recorded in [RH.1–3](R133-supplement-exact-selected-residual-frequency-bands-and-complete-known-high-forcing.md):
$$
 Q_\delta=Q_0+\delta Z,\qquad
 \deg_\phi Q_0\le32,\qquad \deg_\phi Z\le96,
 \qquad \deg_\phi Q_\delta\le96.
 \tag{RBT.1}
$$
The true radial reference is a degree-zero term. The exact repairs add only vectors in the same finite angular slots. On the original analytic root piece, every ordinary radial derivative needed here has the same angular support bound96.

RH's numerical residual bounds have their original smaller delta domain. Only its exact finite-dimensional definitions and support identities are used in RBT.1. An exact finite Fourier expansion remains finite for every coefficient value; no RH numerical bound is extended to a larger delta domain.

Use the normalized original moving circle, whose physical frequencies are4j:
$$
 e_j=e^{4ij\phi},\qquad
 \Pi f=\langle f\rangle,\qquad P=1-\Pi,\qquad
 I=\partial_\phi^{-1}P,\qquad
 P_H=1_{\{|j|\ge97\}}.
 \tag{RBT.2}
$$
The root is normalized by X(r*,phi)=phi. No true-angle or selected common-input composition is inserted into these support statements. Those later compositions can destroy Fourier support.

A radial scalar and an angular mean have degree zero. Angular differentiation, ordinary radial differentiation on the same piece, P and I do not enlarge angular support. Multiplication adds degrees. Thus support identities do not require a norm estimate or a new enclosure.

The actual root scalar coefficients satisfy
$$
 D=\partial_r-d\partial_\phi,\quad p=d_\phi,\quad
 d=-\beta I(u^2+Kv^2),\quad
 \ell=-2\beta uv,\quad b_{\rm op}=\beta(1-u^2).
 \tag{RBT.3}
$$
Here K, beta and eta, and their ordinary derivatives, are radial. In particular d and each needed ordinary radial derivative of d have degree at most192. D itself is not an angular-degree-preserving derivative.

| Primary read for this proof | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| RH, exact finite definitions | 54773aa52c48a3344f59c98f773da3850b205169 | 13244 | b3bfaf73dda241de03e52e052164b33313166de94b5387304aba771b9ec3a1f2 |
| RD, complete stable root products | 24b3523585bdfe9f1d96b57e3ca2e4f0727fd2d4 | 17725 | 34eec24f901205c6e8002aa767484fed4832f590fbbfbb89b3a9f2ece218b81f |
| RDA, complete first a derivative | 5a7b91eea967053bb1e68e0cc60a41fd5183cd69 | 11486 | 8d2570c7b28304001c785e7b7a6d4261cf127909dd59d594262fd22d42caa205 |
| RBG, genuine b values and ordered RD substitution | 6fcf438b00220d8823f86dd619aaf32659b597c8 | 22284 | 157795fdc7fc415156229f5c0b9674b18f92cce1e8cef8ce8df65a271775f268 |
| SE, natural stable windows and Fredholm scope | eb7b1bb1ea1fdf713fcf172428f68ed20afafdb2 | 20047 | 2220174707046248cbdf9f9f8c47bc13bc233b0ab65f5ed598ddcbf964e93ad4 |

The two independent physical mean coordinates are separate from Pi. Their matching equations are not projected away by RBT.2.

## RBT2. Complete coefficient-degree table

Use all symbols and exact formulas of RBG.6–26, with the correlated products formed before taking any modulus. The scalar radial quantities bart, bars, L, barA, barC, Vm and Vrad(0) have degree zero.

| Complete actual coefficient | Degree upper bound | Exact reason |
|---|---:|---|
| u, v and each ordinary radial derivative used | 96 | RBT.1 |
| d, p, ell and their actual ordinary radial or angular derivatives; the root value bop | 192 | quadratic state products in their full neighborhood definitions; I and derivatives preserve support |
| Dp | 384 | p_r−d p_phi |
| D²p | 576 | p_rr−2d p_rphi+d²p_phiphi−(d_r−dp)p_phi |
| t, delta-t, q1, A0 and a*=A0−bop | 192 | RBG.7–8,12–15 |
| x2, s, delta-s and q2 | 384 | RBG.7–8, including p² and d p_phi |
| x3 | 576 | partial-phi of d x2+d_r p+d_rr/2 |
| Sigma2 and delta-R2 | 384 | complete quadratic differences |
| Sigma3, Sigma-ts, delta-R3,0 and delta-t4 | 576 | RBG.9–11, including q2 p and q1 x2 |
| delta-L3, Delta-Lambda3 and delta3 | 576 | full variable-D terms in RBG.12 |
| delta1 | 192 | 21p/10 |
| delta2, Delta-C and C0 | 384 | complete second logarithmic difference and Bell product |
| Delta-C3 | 576 | RBG.14: barC delta1, barA(delta1²+delta2), delta1³, delta1 delta2 and delta3 |
| Z_D | 192 | 2 beta k1 P(v²) |
| Z_DD | 384 | full P(2v v_r)−2d v v_phi in RBG.18 |
| W_AC | 384 | ell²−4 beta eta v u_phi |
| Delta-V at the root | 384 | RBG.19, including Dp and Z_D |
| Delta-V_D at the root | 576 | RBG.20, including p Dp, D²p and the full −k1 W_AC |
| Delta-R at the root and E0 | 384 | RBG.23–24 |
| Delta-R_D at the root, E1 and E1−bop E0 | 576 | RBG.23,26,38; p C0 and A0 Delta-V retain their full products |
| R from RDA.16 | 384 | D(ell/eta) and (ell/eta)p, with eta radial |

For example, the apparently largest new fold terms are
$$
 \deg(d\,s_\phi)\le576,\qquad
 \deg(q_2p)\le576,\qquad
 \deg(q_1x_2)\le576,\qquad
 \deg(d^2p_{\phi\phi})\le576.
 \tag{RBT.4}
$$
The fourth common radial fold coefficient, eta third derivative and Mrr cancel in RBG before these counts. Their cancellation is not used to erase any remaining genuine frequency term.

The complete first a derivative is
$$
 Da_{1,\epsilon}=-i\epsilon{\cal R},\qquad
 {\cal R}=\frac65d_{\phi\phi}
       +\frac12D(\ell/\eta)-\frac12(\ell/\eta)p .
 \tag{RBT.5}
$$
Hence the actual two-sign operator is multiplication by R followed by the original signed input isometry, times minus i. Its bandwidth is at most384 and its L2 norm is at most the complete supremum of R. Combining the two signs does not introduce an extra factor two.

The rational-frequency quantities Delta0(j^-2), Delta1(j^-2), A_n, D_n and V_n(0) are scalars attached to the original input label. They are complete diagonal operators, including all denominators, nonzero Airy shear and finite-frequency corrections. They do not enlarge bandwidth. No potential diagonal is changed into an angular multiplier and no unproved negative-window bound is inferred from this support fact.

## RBT3. Complete genuine root operators and their bands

For an operator on original inputs with absolute label at least97, say it has bandwidth B if
$$
 \langle e_j,Ae_k\rangle=0
       \quad\hbox{whenever } |j-k|>B,\quad |k|\ge97 .
 \tag{RBT.6}
$$
This describes the actual high-input matrix. It does not define the missing physical low-input columns by zero.

RBG.36 and38 give
$$
 {\mathsf B}^{V}
   =M_{{\cal E}_0}P_H+D_{\Delta_0}P_H,
$$
$$
 {\cal H}
   =M_{{\cal E}_1-b_{\rm op}{\cal E}_0}P_H
        +M_{a_*}D_{\Delta_0}P_H+\frac13D_{\Delta_1}P_H .
 \tag{RBT.7}
$$
Consequently BV has bandwidth384 and H has bandwidth576. All input diagonals stay to the right of their actual multipliers.

With the original positive input frequency N e_k=4|k|e_k, the exact complete products are
$$
 E_2=P{\mathsf B}^{V}D_DN^{-4/3},
$$
$$
 \begin{split}
 R_0={}&PM_{a_*}D_A+P{\mathsf A}_rD_AN^{-1}
       +P{\cal H}D_DN^{-4/3}\\
 &-\lambda P{\mathsf B}^{V}D_VD_AN^{-2}
       +PM_{b_{\rm op}}\Pi{\mathsf B}^{V}D_DN^{-4/3}.
 \end{split}
 \tag{RBT.8}
$$
These are RBG.39 and the full RD.17–19. In particular the genuine correction is not added again after BV and H.

| Exact R0 summand in its original order | Bandwidth |
|---|---:|
| P M_a* D_A | 192 |
| P A_r D_A N^-1 | 384 |
| P H D_D N^-4/3 | 576 |
| minus lambda P BV D_V D_A N^-2 | 384 |
| P M_bop Pi BV D_D N^-4/3 | 576 |

For the last row, Pi BV has input support at absolute labels at most384: the multiplier E0 has degree384, and the nonzero-input diagonal D_Delta0 cannot reach the zero output. The output of P M_bop has absolute label at most192. Therefore this whole rank term has input support at most384, output support at most192, and difference bandwidth at most576. It has not been omitted from the full operator.

It follows that
$$
 \boxed{\operatorname{bw}(E_2)\le384,\qquad
                   \operatorname{bw}(R_0)\le576.}
 \tag{RBT.9}
$$
The complete root inverse
$$
 {\mathscr J}=(\eta_*\partial_\phi+L)^{-1}
 \tag{RBT.10}
$$
is the original RD operator. No finite bandwidth is asserted for this inverse, for its products with L, for the complete stable trace, or for any radial propagation.

## RBT4. Exact primitive gap for a new original-root tail

Let Jt be an integer strictly larger than576, and set
$$
 P_t=1_{\{|j|\ge J_t\}},\qquad
 Q_t=P_H-P_t,\qquad N_t=4J_t .
 \tag{RBT.11}
$$
The original head Q_t contains every original label from97 through Jt−1 with both signs, subject only to the original reflection convention. It is not the old Q97, not the moving normalizer cutoff and not a final principal-angle cutoff.

Every output of R0 P_t has absolute label at least Jt−576. If a complete same-domain bound is supplied,
$$
                  \|R_0P_t\|_{L^2_H\to L^2}\le r_t,
$$
orthogonality and the actual physical multiplier of I give
$$
 \boxed{\|IR_0P_t\|_{L^2_H\to L^2}
              \le \frac{r_t}{4(J_t-576)}.}
 \tag{RBT.12}
$$
This uses the gap before applying J or L. It neither commutes I through R0 nor assumes that J preserves any band.

There is also the exact identity
$$
                    \Pi{\mathsf B}^{V}P_t=0 .
 \tag{RBT.13}
$$
Thus the last term of RBT.8 vanishes on this particular tail input. Its original labels97 through384 still carry the whole mean-rank term. The two independent physical means remain separate equations for every cutoff.

A complete recipe for r_t can use any actually paid same-tail bounds
$$
 \|{\mathsf B}^{V}P_t\|\le B_t,\quad
 \|{\cal H}P_t\|\le H_t^\#,\quad
 \|{\mathsf A}_rP_t\|\le A_r^\#,
 \quad \|a_*\|_\infty\le a^\#,
$$
and complete diagonal suprema A*, D*, V*, with lambda at most lambda+. A whole original-input bound is an admissible tail bound; it is never sharpened merely by renaming it. Then
$$
 \begin{split}
 e_{2,t}&=B_tD_*N_t^{-4/3},\\
 r_t&=a^\# A_*+A_r^\# A_*N_t^{-1}
       +H_t^\#D_*N_t^{-4/3}
       +\lambda_+B_tV_*A_*N_t^{-2}
 \end{split}
 \tag{RBT.14}
$$
are sufficient for E2 P_t and R0 P_t. There is no mean-rank term in this tail recipe precisely because of RBT.13. The unprojected BV bound is still retained; post-projection norms are not substituted for it.

At the original cutoff97, RBT.12 and13 do not apply. The original complete mean-rank fee and the primitive cost r0/4 in RD.26 and RBG.40 remain valid and unchanged.

## RBT5. A complete L2 high stable block

Use RD's exact stable trace on the original high space:
$$
 \widehat S=D_g+E,\qquad
 E=P_HE_2-\eta_*^{-1}P_HN_{\rm out}^{-2/3}R_0
    +P_H{\cal Z}N_{\rm out}^{1/3}
                   {\mathscr J}L\eta_*^{-1}IR,
$$
$$
 R=\lambda_*D_DN_{\rm in}^{2/3}+R_0,\qquad
 {\cal Z}e_j=i\,\operatorname{sgn}(j)e_j .
 \tag{RBT.15}
$$
All occurrences of N on an input or output keep their indicated side. The original J maps even mean-zero sources to odd states; no J Pi is introduced.

Suppose the complete root bounds
$$
 \|\partial_\phi{\mathscr J}\|\le J_1,\qquad
 \|L\|\le L_0,\qquad \eta_*\ge\eta_->0
$$
and the same-domain values in RBT.14 have been established. Then
$$
 \boxed{\displaystyle
 \|P_tEP_t\|_{L^2\to L^2}\le e_t
 :=e_{2,t}+\frac{N_t^{-2/3}}{\eta_-}
 \left[r_t+J_1L_0
   \left(\lambda_+D_*N_t^{-1/3}
                   +\frac{r_t}{4(J_t-576)}\right)\right].}
 \tag{RBT.16}
$$
Indeed the final high-output projection gives
$$
 \|P_t{\cal Z}N_{\rm out}^{1/3}{\mathscr J}\|
                 \le N_t^{-2/3}J_1.
$$
The leading input term has primitive norm at most lambda+ D* N_t^-1/3. Only the R0 input uses RBT.12. Every intermediate frequency inside J and L remains allowed.

Let g- be a genuine common lower bound for the complete diagonal g_n of RD.13; the original rational choice is17/57. If an outward computation proves
$$
                              e_t<g_-,
 \tag{RBT.17}
$$
then the actual high block
$$
 {\cal K}_t=P_t\widehat S P_t:\operatorname{ran}P_t
                                \longrightarrow\operatorname{ran}P_t
$$
has the L2 inverse bound
$$
                         \|{\cal K}_t^{-1}\|_{L^2\to L^2}
                                  \le(g_--e_t)^{-1}.
 \tag{RBT.18}
$$
This follows by the Neumann series around the actual positive diagonal Dg restricted to that tail.

The estimates RBT.16–18 are L2 statements. They are not silently reused as norms of the same block in a negative Sobolev window. When the complete root map is proved invertible, SE's fixed-window Fredholm and regularity argument gives its corresponding natural-window inverse, as specified below. Quantitative negative-window bounds remain separate.

## RBT6. The actual finite root Schur equation

Assume RBT.17 has actually been certified. For the original root equation
$$
                         \widehat Sx=f,\qquad x\in\operatorname{ran}P_H,
$$
write x=p+q with p=P_t x and q=Q_t x. The exact high solution is
$$
 p={\cal K}_t^{-1}\{P_t f-P_t\widehat S Q_tq\}.
 \tag{RBT.19}
$$
The remaining finite equation is
$$
 \boxed{\displaystyle
 {\mathfrak S}_tq
 =Q_t f-Q_t\widehat S P_t{\cal K}_t^{-1}P_t f,\qquad
 {\mathfrak S}_t
 =Q_t\widehat S Q_t
  -Q_t\widehat S P_t{\cal K}_t^{-1}
                                P_t\widehat S Q_t .}
 \tag{RBT.20}
$$
All entries are those of the complete original root map. The original physical units, two signs, finite-frequency potential and complete mean-rank term remain in these entries. The outer high/low factors are not interchanged with J, L or the input diagonals.

This is a genuine finite matrix on the actual original labels97 through Jt−1. Its cross terms generally need the full J and the actual high inverse. The band of R0 does not give a band for those cross terms, and does not replace this matrix by its positive leading diagonal.

The standard block elimination proves that, under RBT.17, the whole original high root map is invertible if and only if this actual finite matrix is nonsingular. A high-block pass alone does not prove this. A singularity or failure is not inferred from an upper-bound test that fails.

If both the tail gate and finite matrix have been certified, the root stable kernel vanishes. RD/SE then give the same inverse on each fixed natural stable window, in particular the windows minus seven sixths and minus five halves. This is the same qualitative extension already available from RD; a numerical L2 inverse bound is not asserted to be the negative-window norm.

The physical means, original root labels below97, supplied radial head and every independent regular or exterior port are not part of Q_t. They retain their original rows and domains. Root stable invertibility is not a proof of the full waist incoming inverse or the final bordered matching inverse.

## RBT7. What can be consumed and what remains new

A future scalar consumer may use complete already successful root bounds for eta, lambda, the genuine profile diagonals, BV, H, Ar, a*, J1 and L0 to evaluate RBT.14–17 for a new Jt. Any new coefficient or denominator bound must first be paid on the same domain. It must retain the original97 verdict independently.

RBO's input-frequency refinements, if subsequently proved and evaluated, may supply sharper same-tail B_t and H_t bounds. That would change positive budgets, not the band proof or the ordered complete operators. The current97 consumer need not be changed for this supplement.

The finite matrix in RBT.20 requires the complete actual signed entries and controlled cross terms. It is a new obligation. Existing scalar norms do not supply those entries, and no old Green sweep, root enclosure, ray or successful scalar calculation is requested to be repeated.

For the full incoming and return problem, the established BF/BT and FC requirements still apply: a complete square realization, actual finite columns and dual rows, all independent physical means and functional ports, the complete infinite strong remainder and its actual finite inverse. Neither an original-circle support identity nor a root stable-tail test changes that accounting.

This supplement supplies no numerical tail pass, finite Schur pass, complete incoming inverse, full return, nonlinear background or final surface. It proves an exact option for improving the primitive gap while preserving the finite and infinite obligations.
