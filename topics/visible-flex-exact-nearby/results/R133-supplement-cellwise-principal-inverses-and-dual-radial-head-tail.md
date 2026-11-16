# R133 supplement: cellwise principal inverses and the dual radial tail of the complete positive head

The failed sufficient WHV mesh test admits a different complete operator certificate. A frozen symmetric angular principal matrix can be inverted exactly on each radial mean-zero complement, without an exponential or a small h times principal-norm condition. The complete high feedback has an input-tail estimate obtained from its actual adjoint source equation. Combining these facts gives a second mesh factor for the feedback.

This is an analytic certificate and a new-target contract. None of its new coefficient contractions or strict comparisons has been evaluated. It does not declare the positive head inverse, prescribed physical 96 columns, or any finite determinant to exist.

## WPT1. Actual outcome and unchanged spaces

The complete WHV science of run 43838214094/1 passed fourteen admission/completeness gates and retained its strict comparison as false. Its saved epsilon is

[35.5162849016096175926993926870198490179833360745262969087788838134567295951 +/- 4.46e-74].

The original required-N diagnostic is 145475, above the declared cap 4096. The actual counters are three saved-row maxima, eighteen new scalar records, one strict comparison, zero old targets recomputed and zero matrix allocations. No resolvent was admitted. These facts are read from the complete outcome, without evaluating the balls again. Failure of this sufficient upper-bound test is not evidence of a singular operator.

Keep the selected-member positive interval, the original reflected raw coordinates and ordinary radial measure:
$$
 I_+=[r_*,25/8],\qquad
 E_L=Q_{\{|j|\le96\}}\{h_1\ {\rm odd},h_2\ {\rm even}\},
 \quad\dim_{\mathbb R}E_L=193,\qquad
 \mathscr H=L^2(I_+;E_L).
 \tag{WPT.1}
$$
The angular measure is normalized, and physical angular frequencies are 4j. Use the complete WHR.4 operator:
$$
 A=A_L,\quad B_{LH}=Q_L\mathcal A P_H,\quad
 B_{HL}=P_H\mathcal A Q_L,\quad A_{HH}=P_H\mathcal A P_H,\quad
 K=B_{LH}G_HB_{HL}.
 \tag{WPT.2}
$$
Here G_H is the old high given-head inverse on its ordinary source column, with all stable root, independent head, outer, mean and jump ports zero:
$$
 G_H:L^2_rH^{-2/3}_{\phi,H}\longrightarrow L^2_rH^{-1}_{\phi,H}.
 \tag{WPT.3}
$$
It is not the coupled physical inverse. Every other original input is retained separately. The raw operator includes drift, both local reactions, the ordered two-multiplier primitive, and its complete physical mean rank.

Writing V_0f(r)=\int_{r_*}^rf(t)\,dt, the unchanged self-block is
$$
                     F_0=Id-V_0(A+K).
 \tag{WPT.4}
$$
The original root initial coordinate, actual impulses and all other sources appear on its right. The endpoint is WHV's bounded complete integral row; it is not evaluation on an arbitrary L2 head.

## WPT2. The cell primitive is skew adjoint

Partition I_+ into cells I_i of positive lengths h_i. Let Pi_i be ordinary cell averaging and Q_i=Id-Pi_i; Pi and Q denote their direct sums. A cell can contain old coefficient subdivision points only when the coefficients used below are continuous there with the stated piecewise weak derivative. Otherwise every actual nonzero value/transmission jump must be a cell endpoint.

For q in Q_iL2 define
$$
 (\mathcal B_iq)(r)=\int_{\inf I_i}^rq(t)\,dt
 -\frac1{h_i}\int_{I_i}\int_{\inf I_i}^xq(t)\,dt\,dx .
 \tag{WPT.5}
$$
Thus B_i=Q_iV_{0,i}Q_i, its derivative is q, and its mean is zero. Because q has integral zero, its primitive's endpoint values are equal. Integration by parts and density give
$$
 \mathcal B_i^*=-\mathcal B_i,\qquad
                   \|\mathcal B_i\|=\frac{h_i}{2\pi}.
 \tag{WPT.6}
$$
Equivalently, its multiplier on nonzero radial Fourier frequencies omega_{ik}=2 pi k/h_i is 1/(i omega_{ik}). The complete periodic Fourier basis is a basis of cell L2; this does not impose a new periodic boundary condition on the physical head.

The map without an input Q_i has the distinct bound
$$
                  \|Q_iV_{0,i}\|_{L^2\to L^2}\le h_i/\pi.
 \tag{WPT.7}
$$
Apply the mean-zero Poincare inequality to its output and use (Q_iV_{0,i}f)'=f. The input projection in (WPT.6) cannot be silently inserted in (WPT.7); in particular, a constant input gives a nonzero centered ramp.

## WPT3. Exact principal inverse without h||D|| smallness

Choose fixed invertible real S_i and fixed D_i on each cell with
$$
          \widetilde D_i=S_iD_iS_i^{-1}
                         =\widetilde D_i^* .
 \tag{WPT.8}
$$
The adjoint is in the inherited fixed Euclidean fiber. Pay S_i and S_i^{-1} whenever a conclusion is converted to the original head norm. Let S be their piecewise constant multiplication and use tildes for S-conjugated head operators.

B_i commutes with the fixed angular matrix Dtilde_i. Their product is bounded and skew adjoint. Therefore
$$
 R_i=Id-\mathcal B_i\widetilde D_i,\qquad
 R_i^{-1}\ {\rm exists},\qquad \|R_i^{-1}\|\le1.
 \tag{WPT.9}
$$
Indeed Re<R_i x,x>=||x||^2 gives a closed range and injectivity; the same estimate for the adjoint gives dense range, hence onto. The exact multiplier is
$$
 \widehat{R_i^{-1}f}(k)=
 i\omega_{ik}(i\omega_{ik}Id-\widetilde D_i)^{-1}\widehat f(k),
 \qquad k\ne0.
 \tag{WPT.10}
$$
On an angular eigenvalue lambda its modulus is |omega|/sqrt(omega^2+lambda^2)<=1. This uses no fundamental matrix, IVP exponential, or bound h_i||D_i||<1.

A concrete body-cell choice freezes exact real reference numbers eta_i and q_i>0:
$$
 D_i=\eta_i
 \begin{pmatrix}0&-q_i^2\partial_\phi\\\partial_\phi&0\end{pmatrix},
 \qquad S_i(h_1,h_2)=(h_1,q_i h_2).
 \tag{WPT.11}
$$
The q_i factor applies to the entire even component, including its physical mean. On each reflected angular pair j=1,...,96, Dtilde_i is the real symmetric block
$$
             4j\eta_iq_i\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$
It is zero on the even angular mean. That mean's radial mean-zero complement still has R_i=Id; its complete scalar mean equation remains in the remainder.

At the true root K(r_*)=0. There is no global positive curvature lower bound here. A safe first-cell choice is D_0=0,S_0=Id. Alternatively a positive q_i is only a chosen reference, and all differences between the actual coefficients and that reference must be paid, even if actual curvature vanishes in the cell.

## WPT4. The complete principal difference

For a body cell using (WPT.11), a sufficient e_i>=||S_i(A-D_i)S_i^{-1}|| is the complete recipe
$$
\begin{split}
 \mathcal E_i={}&384\|d\|_\infty+
 384\max\left\{\frac{\|\eta K-\eta_iq_i^2\|_\infty}{q_i},
                         q_i\|\eta-\eta_i\|_\infty\right\}\\
 &+\|L_{11}\|_\infty+\|L_{22}\|_\infty
                    +(\|K\|_\infty/q_i+q_i)\|\ell\|_\infty\\
 &+\frac{|\beta|_*}{2}(U_1+q_iV_1)
                              (U_0+\|K\|_\infty V_0/q_i)\\
 &+|\gamma|_*(\|K\|_\infty V_1/q_i+U_1),\qquad e_i\ge\mathcal E_i.
\end{split}
 \tag{WPT.12}
$$
U_t,V_t bound actual multiplier moduli, for example by complete accepted Fourier A0 bounds. The primitive's factor 1/2 is 2 times the true L2 norm 1/4 of I. It is not an L-infinity primitive estimate.

The principal difference requires actual enclosures of eta K-eta_iq_i^2 and eta-eta_i. Subtracting unrelated positive upper bounds is invalid. Every drift, local reaction, ordered primitive and physical mean rank in WHR.4 has been included. A sharper signed finite-matrix recipe can replace (WPT.12) only for the same whole cell operator.

For D_0=0,S_0=Id, the old complete collar generator record 62286/125 can be read directly on a cell inside its original collar. It is not extended into the body. A large reference q_i or its poor conditioning is not free: all S conversions and complete differences remain.

## WPT5. Dual regularity of the actual high feedback

The adjoint below is first the formal dual in the original angular L2 distribution pairing. From (WPT.3),
$$
 G_H^*:L^2_rH^1_{\phi,H}\longrightarrow L^2_rH^{2/3}_{\phi,H}.
 \tag{WPT.13}
$$
It is not a same-Hilbert-space adjoint with Riesz weights omitted.

The old collar and body source columns C_c,C_b both bound the complete whole-positive raw output. Thus
$$
                         C_G=(C_c^2+C_b^2)^{1/2}
 \tag{WPT.14}
$$
is a valid joint bound for G_H and its dual. Split an ordinary source over the disjoint collar/body intervals, use the two original full columns and apply Cauchy--Schwarz on the input norms. Reading only the old body slot is insufficient. This combination is a new scalar target if evaluated; C_c and C_b themselves remain original records.

For psi in the transformed head space set w=G_H^*B_LH^*S^*psi. Its true dual boundary and transmission conditions are those of G_H. Testing against compactly supported smooth high states gives
$$
 -w'=A_{HH}^*w+B_{LH}^*S^*\psi,\qquad
                    \widetilde K^*\psi=S^{-*}B_{HL}^*w.
 \tag{WPT.15}
$$
For such a high test state v, G_H(v'-A_HH v)=v: every original endpoint and impulse port is zero. This proves the weak interior identity without assuming a coupled head inverse.

Inside a cell S_i is constant, so exactly
$$
 (\widetilde K^*\psi)'=
 S_i^{-*}\{(B_{HL}^*)'-B_{HL}^*A_{HH}^*\}w
            -S_i^{-*}B_{HL}^*B_{LH}^*S_i^*\psi .
 \tag{WPT.16}
$$
No derivative of psi or of a saved scalar upper bound occurs. Define complete operator bounds
$$
\begin{split}
 C_{LH,1}&\ge\|B_{LH}^*S^*\|_{\mathscr H\to L^2_rH^1_{\phi,H}},\\
 C_1&\ge\mathop{\rm ess\,sup}_{r\in I_i,\ i}
  \|S_i^{-*}\{(B_{HL}^*)'-B_{HL}^*A_{HH}^*\}
                                      \|_{H^{2/3}_{\phi,H}\to E_L},\\
 C_2&\ge\mathop{\rm ess\,sup}_{r\in I_i,\ i}
  \|S_i^{-*}B_{HL}^*B_{LH}^*S_i^*\|_{E_L\to E_L}.
\end{split}
 \tag{WPT.17}
$$
The complete broken derivative satisfies
$$
 \|(\widetilde K^*\psi)'\|_{L^2_rE_L}
 \le C_{K^*,1}\|\psi\|,\qquad C_{K^*,1}=C_1C_GC_{LH,1}+C_2.
 \tag{WPT.18}
$$
The true dual boundary conditions remain inside G_H^*. Replacing them by a convenient artificial condition would change the operator.

All three coefficients in (WPT.17) are finite angular contractions. The original shift bound 192 gives
$$
 B_{HL}=P_{\{97\le|j|\le288\}}B_{HL},\qquad
 A_{HH}B_{HL}=P_{\{97\le|j|\le480\}}A_{HH}B_{HL}.
 \tag{WPT.19}
$$
With Lambda_j=(1+16j^2)^(1/2), C_1 is obtained from the full matrix
S_i^{-*}[(B_HL')^*-(A_HH B_HL)^*] Lambda_{97:480}^{-2/3}.
C_LH,1 uses Lambda_{97:288} B_LH^*S_i^*, and C_2 uses the indicated complete product. These are support identities for coefficient composites, not a band assigned to the unknown high solution.

The primitive retains both ordered convolutions and the annihilation of its intermediate zero mode. The radial derivative comes from actual coefficient derivatives on every original piece. WHV's saved scalar maxima contain no radial derivative certificate and cannot be differentiated.

If coefficients and their angular derivatives are continuous at an old seam and the homogeneous raw high state has zero jump, the finite projections in (WPT.15)--(WPT.16) match there. They are H1 across the seam even if derivatives jump. Otherwise that seam is a projection endpoint, or its full jump must be a separate factor. Changes of S are always projection endpoints. This distinguishes true discontinuities from subdivisions made only to estimate a continuous coefficient.

Cell Poincare and duality now give the full-input estimate
$$
 \|\widetilde KQ\|=\|Q\widetilde K^*\|
                      \le h_{\max}C_{K^*,1}/\pi .
 \tag{WPT.20}
$$
No radial derivative of an ordinary source is required.

## WPT6. A new complete tail gate

Put R_D=direct_sum R_i on QH. Every past-cell Volterra integral is constant on the receiving cell, and the final Q_i annihilates it. With all finite Pi rows still retained, the exact tail block is
$$
 R_Q:=Q\widetilde F_0Q
   =R_D-QSV_0(A-D)S^{-1}Q-QSV_0KS^{-1}Q .
 \tag{WPT.21}
$$
The first difference is bounded by max_i h_i e_i/pi using (WPT.7). After removing the past-cell constant, the second is Q_iV0,i applied to (Ktilde Q a)|I_i. Thus (WPT.7) and (WPT.20) imply
$$
 \|R_D-R_Q\|\le
 \delta_{\rm cell}:=\max_i\frac{h_i e_i}{\pi}
                     +\frac{h_{\max}^2}{\pi^2}C_{K^*,1}.
 \tag{WPT.22}
$$
If a saved outward comparison proves
$$
                         \delta_{\rm cell}<1,
 \tag{WPT.23}
$$
there is a true two-sided inverse
$$
                   \|R_Q^{-1}\|\le(1-\delta_{\rm cell})^{-1}.
 \tag{WPT.24}
$$
Factor R_Q=R_D[Id-R_D^{-1}(R_D-R_Q)] and use ||R_D^{-1}||<=1. A false comparison is a complete result, not authorization for an unannounced larger mesh.

This test removes the large frozen angular principal norm from the first mesh term. It retains the complete high feedback through its true dual derivative and two mesh factors. Neither step proves the new bound is small; rough C_1 or badly conditioned S can still make it unusable.

## WPT7. Exact refinements before bounding

The complete moving mean equation N.7 gives the identity
$$
                              \Pi_2B_{LH}=0.
 \tag{WPT.25}
$$
For a pure high state, its mean and its pairings with degree96 u and v vanish. Applying the full N.7 row proves (WPT.25). This is an exact cancellation, not subtraction from a positive norm estimate. The independent physical mean, its coupling to other low modes, its endpoint and its affine sources remain in A and the full physical system.

In the already qualified decomposition into a large degree32 background and a small degree96 difference, the large background's total shift is at most 64. Its high-to-low block can reach only low frequencies 33 through 96. Frequencies 1 through 32 receive the complete small difference, which must still be paid. This refinement may be used in the actual finite contractions, retaining that original decomposition; it does not declare the whole background to have degree32.

One optional further refinement has an exact finite cost. Let E_N be the normalized cell-constant isometry and introduce
$$
                         \zeta=E_N^*\widetilde K\widetilde a .
 \tag{WPT.26}
$$
This is a full L2 dual row. Splitting the receiving-cell input gives
$$
 QSV_0KS^{-1}\widetilde a
 =\mathcal BQ\widetilde K\widetilde a+J_{\rm ramp}\zeta .
 \tag{WPT.27}
$$
B is direct_sum B_i. J_ramp is the exact centered integral of a normalized cell constant, with norm h_i/sqrt(12) on cell i. No ramp or source is discarded. For the choice (WPT.11), or another S preserving the physical mean, (WPT.25) makes zeta's angular mean component zero. A general S does not justify this deletion. The actual head means in E_N^*atilde remain.

For the radial mean-zero part alone there is the stronger spectral bound
$$
 \|R_i^{-1}\mathcal B_i f\|
 \le\|\rho_i(\widetilde D_i)f\|,\qquad
 \rho_i(\lambda)=\big[(2\pi/h_i)^2+\lambda^2\big]^{-1/2}.
 \tag{WPT.28}
$$
It follows mode by mode from (WPT.10). A weighted complete candidate can use (WPT.28) after adding the full equation (WPT.26), its ramp columns and all cross terms. Applying it directly to an unprojected radial input is invalid. The optional candidate is selected only as a whole; entries from different candidates are never mixed.

## WPT8. Complete signed finite reduction

Retain the original equations in trace-safe form
$$
       F_0a=\mathscr B y+f,\qquad
       \mathscr C a+\mathscr D y=g.
 \tag{WPT.29}
$$
The unknown y keeps its actual product space. An independent external function in y is still infinite-dimensional. Put Ftilde=S F0 S^-1, Btilde=S B, ftilde=S f and Ctilde=C S^-1. Write atilde=E_Nu+z, z in QH.

Under (WPT.23), the exact tail is
$$
 z=R_Q^{-1}(Q\widetilde{\mathscr B}y+Q\widetilde f
                                -Q\widetilde F_0E_Nu).
 \tag{WPT.30}
$$
The remaining complete equations are
$$
 \begin{pmatrix}
 E_N^*\widetilde F_0E_N-E_N^*\widetilde F_0Q R_Q^{-1}Q\widetilde F_0E_N&
 E_N^*\widetilde F_0Q R_Q^{-1}Q\widetilde{\mathscr B}
                                      -E_N^*\widetilde{\mathscr B}\\
 \widetilde{\mathscr C}E_N-
             \widetilde{\mathscr C}Q R_Q^{-1}Q\widetilde F_0E_N&
 \mathscr D+\widetilde{\mathscr C}Q R_Q^{-1}Q\widetilde{\mathscr B}
 \end{pmatrix}
 \binom u y
 =
 \binom{E_N^*\widetilde f-E_N^*\widetilde F_0Q R_Q^{-1}Q\widetilde f}
       {g-\widetilde{\mathscr C}Q R_Q^{-1}Q\widetilde f}.
 \tag{WPT.31}
$$
Every sign follows from (WPT.30); conversely these equations reconstruct (WPT.29). Initial and jump particular solutions stay in the same f and B. No naked physical trace acts on an arbitrary L2 intermediate.

For the prescribed-root-even positive problem, after its genuine boundary chart is used, the remaining finite unknowns are the original 97 root-complement and 96 low outer-chart coordinates. The core then has dimension 193N+193. This count proves neither invertibility nor affordability. Adding (WPT.26), WFR/WCF or other genuine finite coordinates adds all their equations and cross terms. High graph Theta constraints, the metric direction, both stored density means and the true independent physical even-mean equation remain.

A subsequent exact rational or dyadic approximate inverse must be checked against the whole signed core, including errors in applications of R_Q^-1 and its actual boundary/mean rows. A strict complete residual below one proves that finite inverse. An isolated principal-block bound does not. If y still contains an unknown function, (WPT.31) remains an operator system.

The purpose is a separately capped small radial space, not allocation of the old required-N diagnostic. No finite allocation or feasible inverse is asserted by this proof.

## WPT9. Minimal input closure and executable target

A future child has the following complete sequence.

1. Read the complete WHV science, the old negative-one summary/process and their immutable source/proof identities. Preserve the false old mesh gate, all three completed maxima and nine original literals. Do not repeat the old positive graph, Green, Riccati or row maxima.
2. Pin an exact finite mesh, all exact eta_i,q_i or D_i=0 choices, and S_i. Declare a cell cap and signed-matrix memory cap before any new target. Actual nonzero coefficient/transmission jumps must be projection endpoints. Old integration subdivisions need not become unknowns when full continuity is actually qualified.
3. Read the same repaired centre, full direction and intrinsic coefficients through their existing exact definitions and saved enclosures. Match the genuine root, selected delta, physical parameter, angle and ordinary dr. Any canonical restoration is temporary inside own Actions; no binary is consumed in chat.
4. Admit values and first ordinary-r derivatives on every original positive piece. Read completed derivatives verbatim where available. Do not differentiate an old upper bound or request a derivative of an arbitrary ordinary source. True one-sided fields and actual continuity are separate admission facts.
5. Compute only the new composites e_i, C_LH,1, C_1 and C_2, retaining every piece and the complete angular bands in (WPT.19). Form signed composites before the final bound, or use a proved complete positive recipe. Keep all primitive and mean terms.
6. Form the new joint C_G, C_K*,1 and delta_cell. Save every complete directed record before the next target, then compare the finally saved endpoints. Root-cell and S-conversion qualifications remain explicit.
7. If the gate is false, save it and stop without a resolvent or finite matrix. If true, save the new tail inverse bound and the complete factorization (WPT.30)--(WPT.31). Finite pairings remain a subsequent signed target with their own declared resource bound.
8. That later target must enclose all actually missing entries/applications and the full signed approximate-inverse residual. All ordinary sources, true jumps, chart ports, metric, mean, WFR/WCF and Theta columns carry their original units. A failure is retained normally.

The old small norm summaries do not determine signed coefficient matrices or their radial derivatives. They freeze prior qualifications and coarse bounds; they do not supply nonexistent entries. Exact canonical restoration tuples and already-computed derivative scopes must be closed before the new coefficient stage. This proof does not claim that stage has run.

The complete negative-waist error does not enter this positive self-block gate. The full physical square still retains its negative radial head, independent external functions, affine data, all cross columns and genuine metric Schur. The zero-dimensional natural stable completion and the new cell principal inverse do not imply that the positive head kernel vanishes.

## WPT10. Immutable primary evidence

All paths in the table are relative to topics/visible-flex-exact-nearby/. Every listed text was read completely; no binary or large report body was fetched.

| Use | Path | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| Complete raw operator and mean | results/R133-supplement-complete-moving-root-scalarization.md | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| Exact head spaces and all cross equations | results/R133-supplement-exact-positive-radial-head-Fredholm-reduction-and-trace-safe-finite-factors.md | 0cb48560534119452e71ec1bc6e23df7af245943 | 28267 | 289935c35a77f706ce4f9c151ae40c85b67e14743899eaed293747e5704dbad4 |
| Original zero-Volterra contract | results/R133-supplement-zero-Volterra-preconditioning-and-readonly-positive-head-mesh-contract.md | 9e377b773c6ef05bb6213e41de3c28a66b556441 | 22319 | e993f0685dad2bd61740cf1fc02ff20d8cd5c02f43970d2eee05fdba885d5dd2 |
| Actual failed sufficient gate | notes/zero_volterra_positive_head_ci/run-43838214094-1/actual-scientific-conclusion.json | ebe7ae42c2482ce9b20e7af1d41e02f89b920010 | 12011 | ff5d6e5231e6be66107217d670133b18727dd5b24b81e7566fa884973b29df72 |
| True source and dual windows | results/R133-supplement-full-delta-negative-one-positive-source-and-regular-ports.md | 6765382c0ea8af731b6593b687cbc84401a4f7ec | 15756 | 0f1383da8611aef931829876b49579f41c7a967435c795ef68a85d2a142cac23 |
| Complete given-head actual graph | results/R133-supplement-actual-full-delta-negative-one-positive-source-graph.md | 8b28bcd0929df468f44186236dd0cf2e9c037dad | 10464 | e144ad9f8cd7dbc29904f92524e9da9511f4bb8d403e06620d8ad85f3105742c |
| Original whole source columns | notes/full_delta_negative_one_positive_ci/run-43627228225-1-full-real-delta-negative-one-positive-graph/evidence/full-real-delta-negative-one-positive-graph-summary.json | 3abd0f6b7291e0f9318dc035a58a4b6e8dfb851c | 41797 | 0a3fb8e1be19b9ad82655099da8d5446ac49d92f073e7f6626d08a0626ec4fef |
| Same full body and large/small source | scripts/fourfold_codazzi_full_delta_positive_high_Volterra.py | f4dd9ad8b324e39fed478183b88095c949d5c09a | 19660 | 0df3ae7181d5ac8808928e9b0ed4bcf225fa3f80ae5df944b2a96a5e4d3ae117 |

This certificate changes the treatment of the infinite radial tail while preserving the actual positive problem and every physical input.
