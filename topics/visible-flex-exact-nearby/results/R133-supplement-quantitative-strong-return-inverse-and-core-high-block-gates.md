# R133 supplement: a quantitative strong-return inverse and the exact gates to the core high block

2026-11-15.

This note proves an inverse criterion for the complete strong return, its correct derivative loss, a finite-border elimination formula, and a source-to-two-output criterion that can be used with the finite193 Green result. It also identifies the exact parameter and projection conditions needed for that use. No new scientific numerical evaluation is performed, and no complete core high inverse is claimed.

The main inputs are [the actual selected-family first phase, B.8--B.13](R133-supplement-selected-family-root-finite-part-and-actual-first-phase.md), [the true root branches, P.20--P.26](R133-supplement-actual-moving-root-parametrix-and-scalar-finite-part.md), [the directed return word, W.8--W.9](R133-supplement-directed-return-word-and-root-first-coefficient-contract.md), [the full phase counterterm P.14--P.16](R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md), and [the complete low/high Schur criterion S](R133-supplement-true-Poisson-Grams-actual-cap-transfer-and-complete-low-high-Schur.md).

## 1. The same-object condition precedes every norm estimate

The arithmetic certificate applies to the selected explicit family
Q_delta=Q0+delta Z, nu_delta=nu0+delta, at its selected delta_star and prescribed quadratic target rho15. It identifies the true first scalar coefficient beta_star and proves
$$
 |D_{j,\zeta}|^{-1}<512|j|\le128\Lambda_j,\qquad
 D_{j,\zeta}=
 \exp\{i(2\pi j\rho_{15}+\beta_\star/j)\}-\zeta,\qquad
 \Lambda_j=\sqrt{1+16j^2},
 \tag{H.1}
$$
for every |j|\ge97, both signs and every fourth root zeta. The primitive is the original angular derivative inverse, with frequency 4j.

The current finite193 directional matrices instead bind the fixed physical eta0, original nu, and repaired M32 delta0. A bound on an enclosure parameter does not change that mathematical identity. In particular the inherited process field whole_original_parameter_half_width=1/1000000000 is not a proof that this finite BVP inverse covers that parameter interval. The same-F producer and its complete-range successor explicitly retain the fixed delta0 identity.

To combine H.1 with a finite inverse, one must either transfer the complete finite operator, its right rows and every source to the selected object, or prove the requisite return arithmetic and strong remainder at the finite operator's actual object. A small change in the principal angle cannot be justified uniformly by multiplying that change by an unbounded Fourier label.

The true nonlinear background is another identity. The explicit approximate selected family and its first-symbol certificate are not automatically the unknown exact solution or its true nu response.

## 2. A right preconditioner for the complete strong remainder

Work in the actual phase coordinates in which H.1 holds. Let P_J project onto |j|\ge J, J\ge97, retaining the required signed sectors. Suppose the complete remainder has the genuine bound
$$
 R:H^{s-4/3}\longrightarrow H^s,\qquad \|R\|\le C_s.
 \tag{H.2}
$$
Every nonmean normalizer, incoming inverse, original physical seam, finite-rank term and true positive connector contribution must already be in this R or in the finite border below. The original theorem currently proves the strong class at s=0; H.2 at a different s requires its own complete estimate.

On this same tail, H.1 gives
$$
 \|D^{-1}\|_{H^s\to H^{s-1}}\le128,\qquad
 \|D^{-1}\|_{H^s\to H^{s-4/3}}
       \le128\Lambda_J^{-1/3}.
 \tag{H.3}
$$
Consequently
$$
 \chi_J=128C_s\Lambda_J^{-1/3}<1
 \tag{H.4}
$$
is a sufficient inverse gate. The factorization and inverse have the exact order
$$
 D+P_JRP_J=(I+P_JRP_JD^{-1})D,
$$
$$
 (D+P_JRP_J)^{-1}
   =D^{-1}(I+P_JRP_JD^{-1})^{-1}.
 \tag{H.5}
$$
Thus
$$
 \|(D+P_JRP_J)^{-1}\|_{H^s\to H^{s-1}}
       \le\frac{128}{1-\chi_J}=:K_s .
 \tag{H.6}
$$
The placement of D^{-1} is essential. The proof uses the strong input window in H.2, not an assumed same-order norm for the divisor inverse.

The natural domain is
$$
 X_D^s=\{u\in P_JH^{s-1}:Du\in P_JH^s\},
 \qquad \|u\|_{X_D^s}=\|Du\|_{H^s}.
 \tag{H.7}
$$
It is a Banach space by H.3. Also X_D^s embeds into H^{s-4/3}, so R is defined there. Equations H.5--H.6 prove bijectivity from X_D^s to P_JH^s. They do not say that D maps all of H^{s-1} boundedly into H^s.

For a concrete sufficient target at J=97, a complete C_0\le1/32 would give
$$
 \chi_{97}<\frac47,\qquad K_0<299.
 \tag{H.8}
$$
This uses \Lambda_97^{1/3}>7. H.8 is a proposed complete-operator gate, not a claim about any currently computed volume source bound.

Alternatively any verified C_s admits H.4 after a sufficiently large finite J; for example \Lambda_J>(256C_s)^3 gives chi_J<1/2. Every newly exposed frequency below J remains in the finite problem. It is not covered merely because a smaller finite193 block was previously certified.

## 3. Higher regularity after a low-window inverse

There is a useful distinction between a low-window smallness gate and high regularity. Suppose the same tail already has the inverse H.6 at s=0 with constant K_0. Suppose R has complete bounds H^{t-4/3} to H^t throughout the finite window 0\le t\le s, where s\ge1/3. Then its low solution for f in H^s bootstraps to H^{s-1}: the equation Du=f-Ru gains one third of an angular derivative at each use of the strong remainder, until that window is reached.

One explicit final estimate does not need a second smallness assertion for C_s. Choose a spectral scale M\ge1 so that
$$
                    128C_s M^{-1/3}\le\frac12.
 \tag{H.9}
$$
Split u into \Lambda\le M and \Lambda>M. Then
$$
 \|u\|_{H^{s-4/3}}
 \le M^{-1/3}\|u\|_{H^{s-1}}
       +M^{s-1/3}\|u\|_{H^{-1}}.
 \tag{H.10}
$$
Applying H.1 and the complete H.2, and using the established low inverse, gives
$$
 \|u\|_{H^{s-1}}
 \le256\|f\|_{H^s}
       +256C_sM^{s-1/3}K_0\|f\|_{L^2}.
 \tag{H.11}
$$
For rigor the preceding finite sequence of strong-window bootstraps supplies the regularity before H.10 is applied; equivalently use finite spectral truncations with their full commutator equations and pass through the same bounds. One does not commute R through a spectral cutoff for free.

This is a tame consequence once the low inverse and the required higher strong norms exist. It does not supply those higher norms from a single L2 column estimate. The current root strong-class statement by itself therefore does not yet give H.11.

## 4. Phase Fourier tails and physical Fourier tails are different subspaces

The finite193 calculation uses the original moving Fourier projection P_96. H.1 and H.4 use Fourier projection after the true phase conjugacy and nonmean normalizers. These projections generally do not commute with those coordinate maps.

There are two valid ways to connect them. One can construct the return directly for the physical high/high problem and include every projection defect in its return and finite ports. Alternatively transform the full problem, retain the physical constraints P_96 h=0 and the independent low-equation residual multipliers, and eliminate the phase tail only after writing those finite rows.

The latter formulation has the exact abstract form
$$
 F x+C y=f_F,\qquad Bx+(D+R)y=f_H,
 \tag{H.12}
$$
where x comprises the entire retained finite border, y is the phase tail, and every mean is an explicit finite coordinate or row. The matrices in H.12 also retain any additional frequencies exposed by J>97. The constraint rows distinguish a physical high inverse from the unrestricted full equation.

Let G_J=(D+R)^{-1} be the actual inverse H.5. The finite Schur matrix and solution are
$$
 S_F=F-CG_JB,\qquad
 x=S_F^{-1}(f_F-CG_Jf_H),\qquad
 y=G_J(f_H-Bx).
 \tag{H.13}
$$
A complete physical high inverse requires invertibility of this S_F in addition to H.4. If a known finite inverse is used to validate S_F, the exact coordinate identifications and all row/source conversions must first be given. The old finite193 inverse cannot be substituted for S_F solely because the same original labels occur in both descriptions.

A valid posterior finite test is available: if F_ref is a proven invertible matrix in these exact finite coordinates and
$$
 \|F_{\rm ref}^{-1}(S_F-F_{\rm ref})\|<1,
 \tag{H.14}
$$
then S_F is invertible by Neumann. All complete covariance information available from the actual Green computation may be used to bound this product. An unrelated Euclidean norm or a sampled nominal matrix is not F_ref^{-1}.

## 5. A direct formula for the body and cut response matrix

Let Y_B be the ordinary pair L2 body space on [0,9/10], and let Y_C be the ordinary pair L2 trace at 9/10. Neither output substitutes for the other.

For a complete load species d_k, suppose the exact construction of H.12 and reconstruction gives
$$
 f_F=E_{F,k}d_k,\qquad f_H=E_{H,k}d_k,\qquad
 h|_Y=P_{Y,k}d_k+L_{Y,F}x+L_{Y,H}y .
 \tag{H.15}
$$
All maps have actual, specified units:
E_H,k maps to H^s, B maps finite x to H^s,
C maps H^{s-1} to the finite equations, and
L_Y,H maps H^{s-1} to the stated physical Y.
Let e_F,k,e_H,k,p_Y,k,l_Y,F,l_Y,H,b,c and sigma_F bound their respective norms and \|S_F^{-1}\|.

Substitution of H.13 proves the quantitative coefficient
$$
 \begin{split}
 b_{Y,k}={}&p_{Y,k}+l_{Y,H}K_s e_{H,k}\\
 &+(l_{Y,F}+l_{Y,H}K_s b)\,
       \sigma_F(e_{F,k}+cK_s e_{H,k}).
 \end{split}
 \tag{H.16}
$$
This is an upper bound for the complete load-to-output operator, including its finite-border response. Terms sharing one source are combined by triangle, not by a false square sum.

Take species k=body for the complete low-to-high body source and k=cut for the complete low-to-high cap column. Then
$$
 \mathcal B=
 \begin{pmatrix}
 b_{Y_B,{\rm body}}&b_{Y_B,{\rm cut}}\\
 b_{Y_C,{\rm body}}&b_{Y_C,{\rm cut}}
 \end{pmatrix}
 \tag{H.17}
$$
is exactly a candidate for matrix B in S.17, provided every hypothesis of H.12--H.16 is verified at the same background. Independent ordinary sources, prescribed jumps, boundary errors, mean, metric and height charges are separate additional species and supply the data vector e. They are not erased by taking the two feedback columns.

After the actual finite low boundary gate S.9 is passed, its matrix A and H.17 may be tested in the full positive two-by-two Schur gate S.18. This is a directly usable sufficient criterion, not an assertion that the entries presently have favorable size.

## 6. What the presently paid source windows do and do not supply

The negative Cauchy theorem at order -1 takes ordinary
L2_r H^{-2/3} in the first row and L2_r H^{-1} in the second row to raw H^{-1} state. In the present source consumers the second row is an independent even constant, so its Sobolev norm is exactly its scalar norm. One original angular primitive then gives an L2 output with the separate factor sqrt(17)/4.

The full-delta negative-one positive graph has corresponding raw H^{-1} output, all seven source/jump ports, and its genuine trace conversions. These facts do not give the raw L2 body or cut outputs required in H.15. Its given complete head is a supplied input, not an already solved low/high feedback.

The [genuine radial source-kernel result K.5--K.20](R133-supplement-genuine-radial-reference-two-source-kernels-and-both-outputs.md) proves an explicit local reference statement: two ordinary L2_r H^t sources give density coefficient in the joint modewise-sup H^{t+1} module, while the negative reference body and a fixed strict negative cut each consume one derivative of that coefficient. This is not yet the complete nonradial source-to-return E_H,k in H.15. The first-order coupling in C.18 remains.

The same reference's root mixed trace has size n^{7/6} times the normalized density coefficient. Therefore, if one uses the already proved positive graph through its unweighted mixed root port, H^{7/6} coefficient control is sufficient at that port. With the one-derivative return loss H.6, a possible sufficient return window is s=13/6. This statement only fixes a potential common window; its complete strong norm and all actual order-zero normalizers and source maps still have to be paid. A smaller window would require a sharper true root-to-output estimate.

For the fixed M32 body, this paragraph concerns the original two-row raw moving operator A_HL used in S, before scalar elimination. Its complete formula is Q.4 of [the negative quadratic-density theorem](R133-supplement-negative-quadratic-density-and-full-frequency-transport.md):
$$
 \mathcal A h=(d\,{\rm Id}+\gamma m J(K))h_\phi+Lh
  -2\beta Q_\phi I(uh_1+Kvh_2)
  +\gamma\langle h_2\rangle J(K)Q_\phi,\qquad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.
 \tag{H.18a}
$$
Here d=-beta I(u^2+Kv^2), L is the full quadratic local matrix, and I has its original zero-mean convention. The repaired M32 field has angular support at most32; d and L have support at most64. For a low input through96, the two-factor primitive term has intermediate support at most128 and final support at most160. The mean-rank term has output at most32. The other derivative terms are angular constant or have the stated bandwidth. Thus the complete raw low-to-high body source is supported in 97<=|j|<=160, with the independent even mean retained in the full operator. This is the same support assertion consumed in [the actual M32 body-cross result, section2](R133-supplement-actual-M32-body-cross-weighted-Green.md).

The matrix J(K) in H.18a is not the old-circle inverse J=(eta partial_phi+L_old)^{-1}. The latter generally has infinite Fourier bandwidth. No support assertion is passed through that inverse or through subsequent phase/physical composition. The full source maps E_H,k must still retain those operations.

For this raw body source only, a legitimately required H^t norm, t>=0, can be paid from its L2 norm by the explicit factor
$$
                    \Lambda_{160}^{\,t}.
 \tag{H.18}
$$
This observation is useful for the body column of H.17. It does not apply to the cap column, whose output has infinitely many physical Fourier modes, or to a changed M96 background without its separate support proof.

The current genuine-trial volume certificates concern their stated root piece and source window. They are not arbitrary ordinary-source-to-wave operators. Their bounds may enter the complete remainder error ledger only after the actual propagation, original seams, incoming inverse and reconstruction are supplied. A large valid upper bound is not a lower bound on the true operator.

## 7. A source defect must be converted to the return in its true norm

Suppose a new trial has full residual map F_err, true one-sided jump maps J_i, finite-head maps H_i and exact right-boundary defect B_err. A complete return error estimate has the form
$$
 R_{\rm err}
 =T_{\rm vol}F_{\rm err}
       +\sum_i T_{{\rm jump},i}J_i
       +\sum_i T_{{\rm head},i}H_i
       +T_{\rm right}B_{\rm err},
 \tag{H.19}
$$
with each T mapping its actual source units into the normal-form return. The order in every product is fixed.

The current volume norm L2_r H^{-2/3} cannot be inserted as C_0 in H.2 without the appropriate complete T_vol. The same holds for a root mixed energy, a raw endpoint L2 trace, or a given-head positive graph. Unknown high input is not restricted by the finite support of a known trial.

If a new genuine reference is used only on the root piece while the older construction is used outside it, the exact seam discrepancy belongs in H.19. A cut inside one unchanged reference has no physical jump; changing reference or trial across that cut can nevertheless produce a genuine coordinate or trial discrepancy that must be retained.

## 8. The phase counterterm uses one scalar parameter and all original regular rows

The full counterterm chooses
$$
                P(Q,\nu)\circ g=g\circ R_{\Omega_\star}.
 \tag{H.20}
$$
Its body operator A_reg retains all original regular rows, including the physical fourth mode and independent mean. For
D h-(partial_nu F)delta_nu=f it uses
h=h_f+q_nu delta_nu and
$$
 S_\Omega=t_\nu+L_\Omega q_\nu,\qquad
 \delta\nu=\frac{g_\Omega-L_\Omega h_f}{S_\Omega}.
 \tag{H.21}
$$
The waist amplitude is an output with a later geometric lower-bound test. This formulation does not add a fixed waist-amplitude equation, remove the fourth Robin row, or require a new independent alpha parameter.

There is an exact distinction between an invariant background and a nearby arbitrary iterate. Keep Omega_star fixed and set
E=P(Q,nu) composed with g minus g composed with R_Omega_star.
For delta g=g' a, differentiation gives
$$
 \frac{\delta E}{g'\circ R_{\Omega_\star}}
 =a-a\circ R_{\Omega_\star}
   +\frac{\delta P\circ g}{g'\circ R_{\Omega_\star}}
   +\frac{E'}{g'\circ R_{\Omega_\star}}a .
 \tag{H.22}
$$
Indeed P'(g)g'=g' composed with R_Omega_star plus E'. If the target Omega is also varied, the additional term is -delta_Omega.

Only at E=0 does H.22 reduce exactly to P.15. Away from that set the last term is a genuine zero-order multiplication operator, including its average. Its small coefficient alone does not give a same-order Neumann estimate after a one-derivative-loss divisor inverse.

Thus a complete nonlinear argument must either keep the true phase constraint in its iterates or prove the required tame approximate-inverse and quadratic-defect estimates for H.22. This note does not supply that iteration. It also does not infer that the true first scalar beta stays in its certified interval solely from the principal phase equation; that coefficient retains its own background comparison.

## 9. Current exact status

The new proved consequences are H.3--H.11, the finite-border algebra H.12--H.16, the directly usable two-output formula H.17, and the off-constraint identity H.22. They are analytic statements with explicit hypotheses.

To turn them into the core high inverse, the remaining actual inputs are the complete strong norm at the same scalar-gap object, the actual incoming and normalizing maps, the full source-to-return maps and both physical output lifts, the physical-versus-phase finite border, and the genuine boundary/mean/jump identities. These are concrete missing operators, not additional equations imposed on the problem.

The current finite193 computation, the selected-family scalar gap, the local genuine volume budgets and the given-head positive graph each retain their already proved scopes. None is relabelled as the missing full high inverse. Successful accepted scientific objects are unchanged and need not be recomputed merely to state this criterion.
