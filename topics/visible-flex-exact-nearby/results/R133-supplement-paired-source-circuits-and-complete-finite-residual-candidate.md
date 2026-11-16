# R133 supplement: paired ordinary-source circuits and a complete finite residual candidate

2026-11-16, newton_source, with the complete high-kernel appendix supplied by phase_inverse.

The already proved inherited refinement-160 tail inverse has norm at most 3. The remaining problem is the genuine finite signed Schur matrix. This note removes an avoidable loss in its residual: the ordinary low source enters the body and endpoint rows together. It must be received by that same pair before a norm is taken.

The result is an exact finite source circuit, a complete continuous-principal source identity, and a fixed full-input candidate for the actual three residuals E0, D, T. The candidate retains all root, mean, exterior, affine and high-state corrections. Its numerical residual has not been evaluated. No finite inverse follows merely from writing or running a reference circuit.

## WPS1. Fixed true coordinates and the source pair

Use the published WIC, WQS and WDS operators, their same selected member and ordinary radial interval I=[r_star,R]. The inherited m=160 mesh has N=24480 and finite dimension 193N+193. The actual tail inverse bound kappa=3 is an analytic theorem; the two completed old m=1,2 sufficient tests remain false.

The raw head has the normalized real odd96, mean1, even96 basis. Its transformed body coordinate is u=S a, with S constant on each inherited cell. Raw cell values of a constant vector are a_i=h_i^{-1/2}S_i^{-1}u_i. The full finite unknown is (cell coefficients,d97,b96), where d is the root odd complement plus the physical mean, and b is the genuine outer low chart in H^{-5/6}. Prescribed root-even c96 stays in the two original right-side rows.

Let V0 denote ordinary zero-initial integration. For a complete raw low ordinary source g in L2(I;E_L), define its complete body/endpoint pair
$$
 {\cal V}g=\binom{S V_0g}{-\int_I g(r)\,dr}.
 \tag{WPS.1}
$$
The endpoint sign is part of the definition. It is not an independently estimated positive column. Let P_N,Q_N be the actual radial cell projection and its complement in the transformed body space. Split the first row of (1) by P_N,Q_N, retaining the entire endpoint row in the finite space.

Let Q_f be the WIC rational-normalizer finite inverse. Define
$$
 {\cal J}_f g
   =Q_f\binom{P_NS V_0g}{-\int_I g}.
 \tag{WPS.2}
$$
An additional independent endpoint datum is still a separate Q_f(0,end) input. The pair (1) does not remove the true high trace, regular Robin remainder, exterior mean, original affine endpoint, or any independent function-valued port.

All source identities are first proved in raw coordinates. A change of S between cells does not introduce a jump in the raw state or a derivative of a coordinate step.

## WPS2. Exactly two ordinary moments for the projected finite pair

Fix one nonzero angular mode and write the WIC reference generator on a cell as D_i. Let its rational normalizer be rho_i. For local t in [0,h_i], set
$$
 G_i=\int_0^{h_i}g(r_i+t)\,dt,\qquad
 r_i^g=\int_0^{h_i}(1/2-t/h_i)g(r_i+t)\,dt.
 \tag{WPS.3}
$$
These are vector rows on all ordinary L2 inputs, with norms sqrt(h_i) and sqrt(h_i/12). They are orthogonal rows.

To see their exact role, put x=E_d d+V0(D a+g), with a equal to its cell reference value v_i. The equations for the finite pair (2) become
$$
 x_{i+1}-x_i=h_iD_iv_i+G_i,\qquad
 \rho_i v_i=(x_i+x_{i+1})/2+r_i^g.
 \tag{WPS.4}
$$
Indeed, the average of V0g on the cell differs from the average of its two endpoint values by the second integral in (3). The endpoint input -int g in (2) is absorbed into x; the remaining endpoint condition has exactly the original independent endpoint right side. No source derivative is used.

Let b_i=h_i k eta_hat_i/(2rho_i), a_i=b_i q_i^2, and use the same positive WIC pivot den_i=1+2b_i p_{i+1}+a_i b_i. Write x_i=(xi_i,zeta_i), xi_i=g_i-p_i zeta_i. Direct elimination gives
$$
 \begin{split}
 g_i={}&\tau_i g_{i+1}-\lambda_i r_i^o-\mu_i r_i^e\\
 &-\frac{(1+b_i p_{i+1})G_i^o+(p_{i+1}+a_i)G_i^e}
             {{\rm den}_i},\\
 \zeta_{i+1}={}&\tau_i\zeta_i+\sigma_i g_{i+1}
                    +\sigma_i r_i^o-\upsilon_i r_i^e
                    +\frac{G_i^e-b_iG_i^o}{{\rm den}_i}.
 \end{split}
 \tag{WPS.5}
$$
Here r_i means the complete vector r_i^g in (3), not a point value of the source. Root D0=0 has its identity branch. No division by a_i, b_i or tau_i is used.

The WQS independent state y_i=zeta_i-H_i g_i retains
H_{i+1}=tau_i^2 H_i+sigma_i. If
$$
 c_i^o=(1+b_i p_{i+1})/{\rm den}_i,\qquad
 c_i^e=(p_{i+1}+a_i)/{\rm den}_i,
$$
then the extra two y drivers are
$$
 A_i^o=-b_i/{\rm den}_i-\tau_iH_i c_i^o,\qquad
 A_i^e=1/{\rm den}_i-\tau_iH_i c_i^e .
 \tag{WPS.6}
$$
Together with the old two drivers, this is a two-state circuit with four local inputs. Its local output matrix is the exact WQS two-by-four extension obtained from
xi_i=(1-p_iH_i)g_i-p_i y_i and zeta_i=y_i+H_i g_i. The companion module states every entry; it takes absolute values only after these complete signed contractions.

The code obtains the two positive source coefficients without dividing by a zero reference halfstep:
$$
 c_i^o={1\over{\rm den}_i}+{p_{i+1}\sigma_i\over2},\qquad
 c_i^e={p_{i+1}\over{\rm den}_i}
          +{\mu_i\over2(1+b_i p_{i+1})},\qquad
 b_i={\sigma_i{\rm den}_i\over2}.
 \tag{WPS.7}
$$
These are exact identities, not alternative approximate coefficients.

Normalize the source rows as
$$
 z_i^0=h_i^{-1/2}G_i,\qquad
 z_i^1=(h_i/12)^{-1/2}r_i^g .
 \tag{WPS.8}
$$
They are two orthonormal radial moments for each of the two physical angular components. The map from the full L2 source to all 4N coordinates is a coisometry. Thus the norm of the complete source matrix in the code is the norm of (2), not merely a bound for cellconstant sources. Its exact transpose returns all four moments and both independent endpoint dual coordinates.

Input weights are sqrt(h_i) and sqrt(h_i/12). Output weights are the original sqrt(h_i)S_i/rho_i, root weight1, and outer theta_j. The source contains no additional S_i input factor: g is raw in (1). If a different specified source Sobolev window is used, its actual angular Riesz map is inserted before the source moments.

## WPS3. Physical mean, comparison weights and the unprojected source

The mean is a separate exact branch. With endpoint mean e_m, its cell output and root mean are
$$
 \begin{split}
 u_i^m&=\sqrt{h_i}s_i
       \left(e_m-\sum_{k>i}G_k^m-\tfrac12G_i^m+r_i^{g,m}\right),\\
 d_0&=e_m-\sum_kG_k^m .
 \end{split}
 \tag{WPS.9}
$$
This follows from the mean reference equation a_m(r)=e_m-int_r^R g_m. It includes the original mean-one basis, not sqrt(2), and does not assert that the actual mean generator is zero. All actual mean coefficients and couplings enter the operator difference below.

The source module includes the exact reverse of (9). Its source-only norm has independent e_m=0; the full application still retains e_m. Likewise its nonzero-mode source-only norm sets the two independent endpoint data to zero only for that declared column.

Use any strictly positive input and output comparison weights in the unchanged Hilbert coordinates. A complete positive forward source graph and the exact transpose of that same graph give weighted Schur row/column bounds as in WQS.15a--c. Source moment weights sqrt(h_i) are legitimate choices. Each numerator uses complete upper endpoints and each denominator a positive lower endpoint; each ratio is upper-rounded before its maximum.

There is a necessary distinction. Equations (3)--8 suffice only for Q_f acting on the projected finite pair (2). The full principal left trial also contains the term involving Q_NS V0g. That term depends on the complete L2 source, not just two moments. It is retained next through an exact full Green identity. The code for (2) must not be used as a replacement for that full operator.

## WPS4. Pairing the principal tail before taking norms

Write the complete principal operator as
Acal_D=[A_D B_D; C_D R_D]. The WIC trials satisfy
Z=R_D^{-1}C_D and Y=R_D^{-*}B_D^*Q_f^*. Define
$$
 L^*=(Q_f,-Y^*),\qquad
 {\cal J}_\rho=L^*{\cal V}.
 \tag{WPS.10}
$$
In (10), the body row in (1) is split by P_N,Q_N before L^* is applied.

Let G_D denote the genuine principal two-boundary Green map for an arbitrary raw low source: the homogeneous root even condition, complete unknown root complement, reference outer odd/even relation, and the separate mean condition are exactly those fixed by WIC. Its full projected output P_fG_D contains the normalized cell coefficients, d97 and weighted b96.

The actual principal finite Schur matrix is M_D=A_rho-Delta_rho. Therefore
$$
 \boxed{\quad
 {\cal J}_\rho=(Id-Q_f\Delta_\rho)\,P_fG_D .
 \quad}
 \tag{WPS.11}
$$
Proof: if x=Acal_D^{-1}Vcal g, block elimination gives
M_D x_f=Vcal_f g-B_D R_D^{-1}Vcal_t g. Multiplying by Q_f yields (11). This argument includes the full unprojected source and every principal boundary row. It does not truncate g to the two moments in (3).

The continuous nonzero-mode Green kernel is exactly the one in Appendix K, now on modes1..96. Its root row is
-int E(r_star,s)(1,p(s))g(s)ds; its outer weighted row is
theta_j int E(s,R)(-H(s),1-H(s)p(s))g(s)ds.
The mean is (9) before projection. These rows are part of the Green map norm.

Consequently complete kernel estimates use the output measure consisting of ordinary dr for the body plus one atom for each root and outer coordinate. The body carries S(r), the outer carries theta_j, and the input carries its specified physical angular weight. The weighted Schur proof in Appendix K works without change for this mixed measure. Cell projection is contractive in the transformed body norm and is applied only afterwards. No sqrt(N) loss or unweighted trace inference is needed.

An independent global bound for q=||Q_f|| is not a prerequisite for a finite existence gate if the complete composite quantities below are directly certified. It is needed when using the numerical formula ||M^{-1}||<=q/(1-delta), and can be saved once using the WQS whole weighted graph. It must not be used automatically in place of the composite (11).

The complete principal error Q_f Delta_rho is a separate new whole target. Use WIC's full nonnegative local bound min(x^2/12,x^4/720), preserving the complete cell weights. Do not recompute either old m=1,2 tail test or a completed WPTVS coefficient maximum.

## WPS5. The complete actual source and endpoint observation maps

Let a denote the raw low head and b the actual outer low chart. Use the original zero-stable high columns Pa,Pb and endpoint observations Ya,Yb. The exact ordinary perturbation of the principal head equation is
$$
 \Gamma(a,b)=(A_L-D_L)a+B_{LH}{\cal P}_a a+F_b b,
 \qquad F_b=B_{LH}{\cal P}_b .
 \tag{WPS.12}
$$
If the original realization has additional independent low forcing columns, they are kept with their original right side or exposed unknown port. Formula (12) does not absorb an unknown radial function into b.

Let B_R^ell and B_R^H be WOB's complete raw exterior reconstruction, and B_R,0^ell its principal reference at p0=13/80. Define
$$
 {\cal O}(a,b)
 =B_R^H Y_a a+
       (B_R^\ell-B_{R,0}^\ell+B_R^H Y_b)b.
 \tag{WPS.13}
$$
The true outer mean is part of these raw rows. In particular B_R^H contains the entire E_R and mu_R contributions; its leading p_R high term alone has zero low projection. No actual mean is set to zero.

Let \widetilde a=S a. In the complete body/endpoint realization, before splitting into P_N,Q_N, the exact operator difference is
$$
 (\mathcal A-\mathcal A_D)(\widetilde a,d,b)
        =-{\cal V}\Gamma(S^{-1}\widetilde a,b)
                         -{\cal E}_{\rm end}{\cal O}(S^{-1}\widetilde a,b),
 \tag{WPS.14}
$$
where E_end inserts a raw endpoint row and zero body. To verify both signs, its body is -S V0 Gamma and its endpoint is +int Gamma-O. These are the actual zero-IVP rows, not a new boundary chart. The root d embedding is identical in Acal and Acal_D.

All physical coefficients in A_L remain, including eta-principal differences, drift, reaction, ordered primitives and the gamma mean rank. The cross-cutoff mean-output identity for B_LH may be used only in its already proved form. It does not remove a low physical mean input, the A_L mean equation, or any high error produced by the full degree96 family.

## WPS6. The true finite residual in paired form

Let W=(Id,-Z) be the full WIC right lift and let Q_t inject the radial-meanzero tail, with zero root/outer coordinates. Put
Q_end=Q_f E_end. Define Gamma and O on the corresponding full coordinates as in (14).

Since the principal defects T and D vanish exactly, substitution of (14) into the full WDS identities gives
$$
 \begin{split}
 E_0&=Q_f\Delta_\rho+{\cal J}_\rho\Gamma W+Q_{\rm end}{\cal O}W,\\
 D_{\rm res}^*&=-{\cal J}_\rho\Gamma Q_t-Q_{\rm end}{\cal O}Q_t,\\
 T&=-Q_NS V_0\Gamma W .
 \end{split}
 \tag{WPS.15}
$$
Every equality is on the original weighted domain, with the original complete adjoint. In particular D is the operator on all tail inputs. It is not a collection of tested dual columns.

The source pair and its principal-tail correction are both retained in J_rho. The endpoint observation is outside it. Moving that observation into the ordinary source without a proved identity would change (15). Conversely estimating Q_f and V0 separately before combining the first pair is unnecessary.

The centered source row TV=Q_NS V0 obeys the complete cell inequality
$$
 \|T_Vg\|^2
       \le\sum_i(h_i/\pi)^2\,\|S_i g\|_{L^2(I_i)}^2 .
 \tag{WPS.16}
$$
Past-cell constants vanish under Q_i because S_i is constant on the cell. There is no extra Q_i on the input of the local Volterra integral. The physical mean is included. A more accurate complete kernel estimate is allowed, but (16) is already a fully specified safe candidate.

With complete e,d,t bounds for (15), the actual sufficient condition is
$$
                 e+3dt<1 .
 \tag{WPS.17}
$$
Only this strict whole gate proves the genuine finite Schur inverse. Its success would feed the full two WDS right sides and tail reconstruction. All 96 physical columns, their signed normalization, nu, Theta, independent functions and any additional finite compatibility are retained. A complete failed candidate is not evidence of singularity.

## WPS7. One declared signed candidate, with complete error channels

Here is a concrete first candidate which needs no signed approximation to an unknown outer graph.

On every original parent, use the same degree32 physical centre and exact rational reference identity already admitted by WPTVS. Form its full raw low generator A_L^0, including its mean column, and both signed cross blocks B_LH^0,B_HL^0. The actual-to-reference principal difference is included when A_L^0-D_L is formed; eta_hat is not silently identified with the actual eta. The original physical alpha, mean offset, angular basis and repair difference are unchanged.

For the high state use exactly the WQS cutoff trial
Phat_a=chi G0 chi B_HL^0 on modes97..160. Its entire residual and full-input kernel are Appendix K. Take Phat_b=0 as a declared initial approximation only. The resulting signed candidate is
$$
 \widehat\Gamma(a,b)
      =(A_L^0-D_L)a+B_{LH}^0\widehat{\mathcal P}_a a,\qquad
 \widehat{\cal O}=0 .
 \tag{WPS.18}
$$
This candidate specifies all columns; the complete b and endpoint corrections below are not optional.

Its ordinary error is exactly
$$
 \begin{split}
 (\Gamma-\widehat\Gamma)(a,b)
   ={}&(A_L-A_L^0)a
      +(B_{LH}-B_{LH}^0)\widehat{\mathcal P}_a a\\
     &+B_{LH}({\cal P}_a-\widehat{\mathcal P}_a)a
      +B_{LH}{\cal P}_b b .
 \end{split}
 \tag{WPS.19}
$$
Every difference is either a full signed interval minus the declared exact reference, or the proved full centre/degree96 two-factor difference. No positive upper is subtracted from another positive upper.

The high-state error in (19) is received from the complete ordinary residual in Appendix K using the already completed collar/body source columns. Its true outer error uses the original corresponding endpoint columns. Root and affine defects of this particular cut trial are zero only because its complete raw trial vanishes near the two endpoints and has identity-interface continuity. All independent nonzero original ports remain in the general right side.

Write G_f=P_fG_D. The important complete composite receivers are
$$
 G_fB_{LH}:\mathscr V\longrightarrow X_f,\qquad
 {\cal J}_\rho B_{LH}:\mathscr V\longrightarrow X_f,\qquad
 T_V B_{LH}:\mathscr V\longrightarrow X_t .
 \tag{WPS.20}
$$
The first and third suffice for the explicit scalar candidate (24). The middle one is an optional sharper direct certificate for (15). From (11), a complete upper for the first gives one for the middle after multiplication by 1+e_rho; the converse is not asserted.
where V is the original whole positive L2(dr;H^{-1}) raw high space. Use each true source frequency weight on the complete 97..288 shell before taking a norm. It is unnecessary to replace all these weights by 1153 and then multiply the old CK or Fb bound. Those old complete bounds remain legal alternatives, not new targets to recompute.

The centre part of (20) reads only its actual 97..160 shell and lands in the corresponding low modes. Its complete full-family and repair differences remain. The exact centre mean-input or output zeros do not transfer to an arbitrary actual block. The original Pi2 B_LH=0 output identity, where applicable, is independent of the full A_L mean coupling.

For example, the third term of (19) after G_f is bounded by the new complete norm of G_f B_LH multiplied by the complete old-source reception of the new high residual. Its b term uses the same complete composite multiplied by the already saved P_b raw column. A direct (15) candidate can instead use its complete J_rho B_LH composite. This is composition of the same operators in the actual order, not deletion of a high response.

## WPS8. Full endpoint reception without a raw 1153 or 142 replacement

WOB gives
B_R y=(J_phi(p_R Id+E_R)y,y+mu_R y),
with the true p_R in [1/8,1/5] and the two complete old norms E_minus,mu_minus. In particular |p_R-p0|<=3/80 exactly.

Define new complete reference endpoint receivers
$$
 q_o\ge\|Q_{\rm end}(J_\phi P_\ell\,\cdot,0)\|_{H^{-5/6}\to X_f},
 \qquad
 q_m\ge\|Q_{\rm end}(0,\cdot\,1)\|_{\mathbb R\to X_f}.
 \tag{WPS.21}
$$
Their rows include all body, root and weighted outer outputs. The input of q_o contains the true H^{-5/6} Riesz weights before the same finite circuit is applied. The mean uses norm1. The old whole E_minus and mu_minus are read unchanged.

Then the complete high-trace endpoint receiver can be taken as
$$
              q_R=q_o E_-+q_m\mu_- .
 \tag{WPS.22}
$$
For a high trace y_H the scalar p_R term projects to zero; for a low b it remains. Therefore, with complete typed trace errors Y_a^err and the old Y_b^0,
$$
 \begin{split}
 \|Q_{\rm end}{\cal O}(\cdot,0)\|&\le q_R Y_a^{err},\\
 \|Q_{\rm end}{\cal O}(0,\cdot)\|
   &\le(3/80+E_-)q_o+\mu_-q_m+q_RY_b^0 .
 \end{split}
 \tag{WPS.23}
$$
For the chosen zero-endpoint high trial, Y_a^err is the received complete source residual, in the transformed head input if that is the chosen input space. An old raw-head trace bound may be compared only after its complete S^{-1} conversion. The b norm is already the actual H^{-5/6} coordinate norm.

Equations (21)--23 retain the exact nonmean second row, which cancels only with that same principal b row, and the independent true mean. They do not replace b by a raw endpoint. All exterior affine terms keep the original full three boundary ports and their original complete old receiver. They contribute to the right side, or to an explicitly retained unknown column, not to a fictitious zero.

## WPS9. An explicit sufficient scalar gate for this entire candidate

For concise statement, set a=S^{-1}u and regard the following norms as full operators on the transformed body space. Every displayed target is new unless its complete object is already saved.

Let e_rho bound Q_f Delta_rho. Let w_0 bound the complete head lift E_N-Z_D; orthogonality gives w_0^2<=1+z_0^2 with the complete principal profile bound z_0. Do not apply this identity to a raw head before its S^{-1} conversion.

Let K_H and eps_H bound respectively
P_fG_D Gammahat(S^{-1}.,0) and
P_fG_D(Gamma-Gammahat)(S^{-1}.,0).
Let eps_b bound P_fG_D Gamma(0,.).
All three use the same full Green and source coordinates. The sum in eps_H is exactly (19). In particular the true high response is paid through complete source and trace receivers, and eps_b retains its original outer-input norm.

Let o_H,o_b be the complete two endpoint bounds in (23). Finally let t_H,t_b bound TV Gamma(S^{-1}.,0) and TV Gamma(0,.), with every term in (19) retained. Formula (16) or a sharper same-operator kernel certificate can pay these two whole targets.

The following complete candidates then suffice:
$$
 \begin{split}
 e={}& e_\rho+
       (1+e_\rho)
       \sqrt{\,w_0^2(K_H+\varepsilon_H)^2+\varepsilon_b^2\,}
       +\sqrt{\,w_0^2o_H^2+o_b^2\,},\\
 d={}&(1+e_\rho)(K_H+\varepsilon_H)+o_H,\\
 t={}&\sqrt{\,w_0^2t_H^2+t_b^2\,}.
 \end{split}
 \tag{WPS.24}
$$
Use these in (17). The square roots in (24) are input-product Cauchy--Schwarz bounds for the independent body and b inputs; no orthogonality of outputs is assumed. The root d coordinate has zero perturbation column in (14), and remains an actual unknown in the principal finite inverse. It has not been dropped from the matrix.

Proof of (24): use (11) with ||Id-Q_f Delta_rho||<=1+e_rho. Apply the complete head lift to the head terms and identity to b. In D^*, Q_t has no b or root coordinate and has body norm1. In T use the full two input columns and (16). Thus (24) bounds exactly all three operators in (15).

This is a concrete first whole candidate, not a promise that it passes. A more accurate complete signed kernel estimate of E0 may replace its first line; it must still include every term of (15). It may not replace separate entries by smaller values from a different trial.

## WPS10. Executable input and resource specification

The next numerical consumer need not allocate a 4724833-square matrix or enumerate its columns. It has the following fixed inputs and stages.

1. Read the completed WPTVS scope, all five whole maxima and original source/endpoint bounds verbatim. Admit the published analytic m160 tail theorem. Materialize the same exact 153-parent reference identities and inherit their 160 children; verify the published complete chain. Stop coordinate materialization before any old coefficient or norm producer.

2. Read only the declared degree32 centre, physical alpha/offset, complete original coefficient enclosures, repaired-family difference fees, and their original raw identity-interface qualification. Full degree96 signed shards are unnecessary for a difference already paid by the full old enclosure. The actual-to-centre differences needed in (19), in their new composite windows, are new complete targets.

3. Prepare the signed WIC/WQS modes sequentially. The source module supplies the exact finite projected source action and reverse. Complete q_o,q_m,e_rho and, if desired for the eventual inverse norm, q are whole weighted graph targets. No all-ones dimension loss or missing sqrt(h)/theta factor is allowed.

4. For the full source identity use the continuous kernels in Appendix K on low modes1..96 and high trial modes97..160. Include the root and outer atoms of WPS4 in low Green estimates. The mean kernel is the independent backward scalar integral. These kernels, not the two-moment projection alone, receive arbitrary L2 inputs.

5. Form signed parent-local coefficient contractions before absolute values. Keep the entire local multiplication and both triangular kernels. Their row/column integrals can be enclosed by the fixed scalar comparison construction in WPS11. Assemble all complete targets in (19)--24, with original collar/body, endpoint, mean and affine units.

6. Save each complete target and its full scientific scope before using its printed value downstream. Keep exact witness identities and a complete running prefix; temporary mode, coefficient and kernel arrays remain in Actions. Failure stops the declared candidate and does not trigger more mesh levels, more modes, or a changed trial.

One workable logical output graph is: complete_reference_receivers; complete_high_trial_source; complete_actual_paired_receivers; complete_local_signed_remainder; complete_endpoint_correction; complete_E_D_T; strict_finite_gate. Each has complete row/column or full correction records as needed, rather than a table of finite matrix entries. A future driver must freeze the exact record list and static output model before execution. All records may fit a small conclusion; this text does not use that statement as a substitute for a measured byte model.

The reference graph alone costs O(96N) operations and O(N) temporary storage. The new continuous kernel norms need no N-by-N radial pair loop: the two directions are scalar state recurrences. Angular contractions must still be counted explicitly. On a parent, centre high states have 128 real components and the head has193. Acting with the degree32-centre generator can extend high output through224; the complete full-family residual can extend it through352. Complete error norms on the latter support remain mandatory.

A numerical cap must cover all original 4801 inherited parent/row intersections for coefficient enclosure, all 153 parent references, added fixed cutoff boundaries, all 96+64 declared reference modes, every signed local contraction and both directions of every kernel. The cap must not count only reference modes and ignore actual angular products. No present statement asserts that an unimplemented coupled calculation fits a particular wall time.

## WPS11. Scalar interval integration without an old ODE rerun

The finite-state kernel bounds can use an explicit positive comparison rather than an adaptive numerical ODE solver.

On a constant-reference interval, the exact endpoint transition in Appendix K is
$$
 \tau_c={\operatorname{sech}(\kappa qh)
                   \over1+(p_{\rm right}/q)\tanh(\kappa qh)},\qquad
 \sigma_c={\tanh(\kappa qh)\over q+p_{\rm right}\tanh(\kappa qh)} ,
 \tag{WPS.25}
$$
and H_right=tau_c^2 H_left+sigma_c. These formulas follow from the complete raw two-by-two transfer, with no division by tau. Their evaluations use nonpositive exponential arguments only. The p update is Appendix K/WQS.18. Root zero rates use their exact zero limits.

Choose complete positive lower p_min on a declared piece and set a= k eta_hat p_min>=0. Then the exact transition E(r,s) is bounded by exp(-a(s-r)) within that piece. Replace each already formed complete signed angular factor by one complete nonnegative interval upper on that piece. The resulting declared majorant is a scalar two-direction linear state graph.

For a nonnegative constant driver upper f on a piece, its forward positive state obeys the complete comparison
$$
 z_{\rm right}\le e^{-ah}z_{\rm left}
                +h\,\varphi(ah)f,\qquad
 \varphi(x)=(1-e^{-x})/x,\quad\varphi(0)=1 .
 \tag{WPS.26}
$$
The same formula in reverse order bounds the backward state. The comparison solution is monotone between its endpoint values when its two constants are fixed, so its supremum is bounded by their maximum. A coarser z_left+h f bound is also valid as a distinct complete candidate.

For every reference piece p lies between its endpoint values and q. H is nonnegative and has the complete bound 1/(2 p_global_min); a tighter exact transition enclosure may be used without changing the operator. These bounds are for reference functions, not signs of an actual solution. They supply complete positive denominators for (25)--26.

The other kernel coefficient has the sharper complete invariant
$$
                         0\le K=1-pH\le1.
 \tag{WPS.27}
$$
For the continuous reference, $p>0$ and (K.1) give
$$
 K'=\kappa q^2/p-\kappa(p+q^2/p)K,\qquad K(r_*)=1.
$$
At $K=0$ its derivative is nonnegative; at $K=1$ it is nonpositive. Scalar comparison on each piece, with continuous raw values at all interfaces, proves (27), including zero rates. For the discrete WIC/WQS circuit the exact identities give
$$
 K_{i+1}
   =\frac{p_{i+1}\tau_i^2K_i+2a_i/{\rm den}_i}{p_i},
 \qquad K_0=1 .
$$
All pivots and $p_i$ are positive and $a_i\ge0$, so this recurrence proves $K_i\ge0$ by induction. The already proved $H_i\ge0$ gives $K_i\le1$. There is no division by $a_i$, $b_i$ or $\tau_i$. This is an invariant of the declared reference, not an actual coercivity claim. It can be used in the same complete kernel and transpose majorant before estimating their norms.

Crucially both row and column estimates must use this same piecewise positive kernel and the same declared comparison weights. Root and outer atoms contribute their whole kernel rows to the reverse column sum. The local multiplication term contributes to both sums separately. Thus (26) is an explicit full-input integral certificate, not a quadrature sample.

Only new reference expressions and new composite norm targets are evaluated by such a consumer. Old WPTVS coefficient maxima, old positive graph/Green columns, old negative-side error budgets and old m1/m2 tests are read verbatim. The method does not assume a background PDE or assign a favorable sign to its complete lower-order terms.

## WPS12. Complete limits and primary pins

The actual tail gate is already true analytically at m160. The actual finite gate (17) is not yet evaluated. The reference source circuit and the full Green identity are tools for that remaining gate, not substitutes for it. They preserve the entire seven-port problem, including ordinary collar and body sources, stable data, exterior data and the three real jump classes, and preserve all independent affine/mean inputs.

All original physical 96 columns and their signed normalization are still required by the full problem. A successful finite Schur certificate would construct them through the original two right sides, not identify them with reference coordinate vectors. All later nu/Theta/mean/border equations remain.

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| Published WIC | 019b1136ebe81e44e98399dff5fb895aafb4362e | 29026 | 527fc35e48f8bb8807e2dc7e7a4b8726e381d35183f31bf8977b252dbb66e59f |
| Published WQS | ff2d61db92e89cc9397c6131675bbcd6294a025c | 25336 | bea9137248b445405c7ae483fdc56c4875cc515820632b1d34fdee8b6bfc6fee |
| Full WDS | 5e93ca37c37d82787ea870aad977712f41b2d4ea | 32943 | 4c7c9d6e582a486f0fe233ac2e617b0f3136ac8a1ed168001f7134050b2230f9 |
| Complete WPTVS actual | c79f9de99b0f6e398c97f840e82a7e653b5e6626 | 24767 | bdd8857cf98d3497600b349b05fc81b8aab7441cd7020b6a5f337b6067f774ef |
| WOB complete outer/source contract | 8a55c94d8decc25f33876665119b327eb1d1fd29 | 41683 | f13024a72e09d9b388fc51eac39d675b656d4d75ee72cdafe449a1c325e92979 |
| Completed WOBSA old receiver records | b21c6d0717bccd6827eff4792bb12b8b1cd40d05 | 60416 | ba8e647cc4572333407b8979f98315e94dbab53ff2ff0086fe1d1dcdb0f17b79 |
| New no-entry source-pair circuit | 2e1224e5a9210b1a3ec59ac7c2837fc53801641b | 11553 | 388cb56b607fa80da928d71cbd9fd514969b936b99315f9cedfd3478bbc3fc5d |

No mathematical callable was executed to write this proof or its source.

---

# WPS appendix: exact two-sided high kernels and complete continuous Schur reception

2026-11-16. Mathematical appendix for the paired-source and complete finite-residual construction. This text evaluates no scalar, kernel integral, reference mode, or previously completed target.

The primary is the published WQS proof:
topics/visible-flex-exact-nearby/results/R133-supplement-bidirectional-impedance-generators-and-complete-high-trial.md,
Git ff2d61db92e89cc9397c6131675bbcd6294a025c, 25,336 bytes,
SHA256 bea9137248b445405c7ae483fdc56c4875cc515820632b1d34fdee8b6bfc6fee.
Its exact raw reference and its original angular, radial, endpoint, and mean coordinates are retained.

## K1. The complete reference Green kernel

Fix one declared nonzero high mode, on the original ordinary-radial interval $I=[r_*,R]$. Let $\kappa=k\widehat\eta\ge0$ and $q>0$ be the same piecewise constant reference as WQS.16, and let $p,H$ be the continuous functions specified by
$$
 p'=\kappa(p^2-q^2),\quad p(R)=p_0,\qquad
 H'=\kappa(1-2pH),\quad H(r_*)=0.
 \tag{K.1}
$$
These are functions of the declared reference, independent of the input. All changes of the reference use continuous raw states. Write
$$
 E(r,s)=\exp\!\left(-\int_r^s\kappa(u)p(u)\,du\right)
 \quad (r\le s),\qquad K(r)=1-p(r)H(r).
 \tag{K.2}
$$
The integral in (K.2) is an exact definition, not an already evaluated new target. It is nonnegative in the exponent with a minus sign, so $0<E(r,s)\le1$. Define the columns and rows
$$
 F(r)=\binom{-p(r)}{1},\quad
 R_0(r)=\binom{K(r)}{H(r)},\quad
 L(s)=(1,p(s)),\quad
 J(s)=(-H(s),1-H(s)p(s)).
 \tag{K.3}
$$
For an arbitrary complete raw source $f=(f_o,f_e)\in L^2(I;\mathbb R^2)$, the two independent scalar states are
$$
 g(r)=-\int_r^R E(r,s)L(s)f(s)\,ds,\qquad
 y(r)=\int_{r_*}^r E(s,r)J(s)f(s)\,ds.
 \tag{K.4}
$$
Consequently the same reference state $v=(\xi,\zeta)$ is
$$
 v(r)=R_0(r)g(r)+F(r)y(r)
     =\int_I {\cal G}_0(r,s)f(s)\,ds,
 \tag{K.5}
$$
where the complete two-sided kernel is
$$
 {\cal G}_0(r,s)=
 \begin{cases}
 F(r)E(s,r)J(s),&s<r,\\
 -R_0(r)E(r,s)L(s),&s>r.
 \end{cases}
 \tag{K.6}
$$
The value on the diagonal can be assigned arbitrarily for this integral operator.

The full diagonal jump is exact:
$$
 F(r)J(r)+R_0(r)L(r)
 =
 \begin{pmatrix}
 pH+K&-p+p^2H+pK\\
 -H+H&1-Hp+Hp
 \end{pmatrix}
 =Id.
 \tag{K.7}
$$
Thus differentiating (K.5) gives the original full source $f$, including both of its components. Splitting the terms in (K.7) into separate positive upper bounds before this identity would lose an actual cancellation.

At the root $H(r_*)=0$ and $y(r_*)=0$, so $\zeta(r_*)=0$. At the outer endpoint $g(R)=0$ and $p(R)=p_0$, so $\xi(R)+p_0\zeta(R)=0$. The kernel therefore has precisely WQS's two reference boundary conditions. It does not impose an additional zero root odd coordinate. The actual prescribed root input remains in the original right side.

The functions $p,H,E$ are continuous across genuine reference subdivisions. A jump of the reference value $q$ changes their derivatives, not their raw traces. The resulting state has no interface impulse. This statement does not remove independent affine jump inputs in the actual seven-port problem.

For the finitely many declared modes, $p,H$ and the coefficient fields in (K.6) are bounded on the compact interval. Formula (K.6) is a bounded map on the full $L^2$ source space. It applies to all radial inputs, not merely to sources constant on a mesh cell or to selected basis columns. The physical mean is the separate original mean circuit; it is not silently put through this nonzero-mode formula.

## K2. Local multiplication and the complete residual kernel

Let $B^0_{HL}(r)$ be the original signed centre cross block, with its full 193-dimensional head input. Let $\chi$ be the exact cutoff in WQS.6. Form the full-input trial
$$
 \widehat{\mathcal P}_a a
   =\chi\,G_0(\chi B^0_{HL}a).
 \tag{K.8}
$$
All nonzero reference modes in $G_0$ are assembled into a block diagonal kernel before the actual angular couplings are applied.

Set $\Delta A=A_{HH}-D^0_H$. The complete ordinary source residual is
$$
 {\cal S}a(r)=D_{\rm loc}(r)a(r)
              +\int_I {\cal K}(r,s)a(s)\,ds,
 \tag{K.9}
$$
with
$$
 D_{\rm loc}=\chi^2B^0_{HL}-B_{HL},
 \qquad
 {\cal K}(r,s)=
   [\chi'(r)Id-\chi(r)\Delta A(r)]\,
        {\cal G}_0(r,s)\,\chi(s)B^0_{HL}(s).
 \tag{K.10}
$$
Here $\Delta A$ acts on the angular variable at $r$. On the declared finite angular trial it is the full finite rectangular action, including angular derivative, drift, reaction, ordered primitives, and every projection and mean term belonging to the actual high equation. There is no radial derivative of the arbitrary input $a$.

Equations (K.9)--10 are WQS.22 with its complete kernel made explicit. They preserve the signed local multiplication term. They also preserve all the true angular output support created by the actual coefficients; the output is not truncated back to the reference support.

For each side $s<r$ or $s>r$, first form the entire signed products in (K.10), including the local angular contraction into $F$ or $R_0$ and the input contraction out of $J$ or $L$. Only then take outward absolute values for a positive majorant. No upper bound for $\Delta A$ or $B_{HL}-B^0_{HL}$ is obtained by subtracting two positive norm uppers.

On the original collar $B^0_{HL}=0$ is only the declared reference identity; $D_{\rm loc}$ still contains the complete actual $-B_{HL}$. In particular, if a centre mean-input high column vanishes, its actual counterpart remains in $D_{\rm loc}$. The input dimension remains 193 throughout.

## K3. Actual Hilbert coordinates before taking norms

Let $W_{\rm in}(s)$ and $W_{\rm out}(r)$ be the exact coordinate maps from the specified physical input and output fibers into their Euclidean Hilbert coordinates. The matrices used in an operator estimate are
$$
 \widetilde D(r)=W_{\rm out}(r)D_{\rm loc}(r)W_{\rm in}(r)^{-1},
$$
$$
 \widetilde{\cal K}(r,s)
   =W_{\rm out}(r){\cal K}(r,s)W_{\rm in}(s)^{-1}.
 \tag{K.11}
$$
For the ordinary residual source, $W_{\rm out}$ contains the original physical Fourier weight $\Lambda_j^{-2/3}$. A raw-state estimate instead uses its original $\Lambda_j^{-1}$ weight. A head represented through the original piecewise constant $S_i$ has that exact input map, and hence $S_i^{-1}$ on the right in (K.11). For a raw unweighted head the corresponding map is the identity.

These are different specified estimates, not a free identification of raw and Sobolev norms. Any subsequent cell averaging, $\sqrt{h_i}$ Riesz factor, $P_N/Q_N$ projection, or weighted outer trace is applied in its original order. No derivative of a merely piecewise constant coordinate map is introduced: the differential identity was first proved in raw variables.

The continuous trial has no WIC discrete $\rho_i$ factor. Such a factor belongs only to the separately defined finite reference circuit. Mixing the two normalizations would change the trial.

## K4. Continuous weighted Schur with the multiplication term retained

Suppose nonnegative complete majorants satisfy
$$
 |\widetilde D_{ab}(r)|\le d_{ab}(r),\qquad
 |\widetilde{\cal K}_{ab}(r,s)|\le k_{ab}(r,s).
 \tag{K.12}
$$
Choose any declared, finite, strictly positive measurable comparison weights $v_b(s)$ and $w_a(r)$. They are comparison functions in the unchanged actual Hilbert coordinates, not a change of coordinates.

A complete forward row bound is
$$
 {\cal R}=
 {\mathop{\rm ess\,sup}}_{r,a}
 \frac{\displaystyle
       \sum_b d_{ab}(r)v_b(r)
       +\int_I\sum_b k_{ab}(r,s)v_b(s)\,ds}{w_a(r)}.
 \tag{K.13}
$$
The reverse bound uses the same majorant:
$$
 {\cal C}=
 {\mathop{\rm ess\,sup}}_{s,b}
 \frac{\displaystyle
       \sum_a d_{ab}(s)w_a(s)
       +\int_I\sum_a k_{ab}(r,s)w_a(r)\,dr}{v_b(s)}.
 \tag{K.14}
$$
If both are finite, then
$$
       \|{\cal S}\|_{L^2_{\rm in}\to L^2_{\rm out}}
                   \le\sqrt{{\cal R}{\cal C}} .
 \tag{K.15}
$$
To prove this, apply weighted Cauchy--Schwarz to the complete sum of the local terms and the integral terms at each output $(r,a)$. Use (K.13), integrate and sum over the output, apply Tonelli to the nonnegative integral, and then use (K.14). The local term contributes exactly the first sum in both (K.13) and (K.14). It cannot be charged as a pointwise value of an ordinary integral kernel or discarded because the off-diagonal kernel has rank one.

The two triangular integration regions in (K.6) must both be included, and the reverse pass must reverse this same complete graph. No output orthogonality or disjoint input-column assumption is used. A declared all-ones pair and a different positive pair are distinct complete candidates; each is saved before a whole comparison.

An implementation using interval comparison weights multiplies with their complete upper endpoints and divides by strictly positive lower endpoints. Exact rational comparison functions may avoid this additional enclosure. The denominators are comparison weights, not assertions that an actual solution or Green function is nonzero.

## K5. Collar/body reception and the complete actual certificate

For the original collar/body source split, restrict the output variable $r$ in (K.9) and in (K.13)--14 to the original interval of each source port. Do not move either cutoff. This gives complete source norms $\alpha_c,\alpha_b$ on the same full head input space. The original seven-port receiver then yields
$$
 \|\mathcal P_a-\widehat{\mathcal P}_a\|_{\rm raw}
       \le C_c\alpha_c+C_b\alpha_b,
 \tag{K.16}
$$
and its original outer row gives the corresponding complete endpoint error, with the original factor 4 if it is not already included in the saved row. The input remains arbitrary and shared between the two source restrictions; (K.16) uses the complete receiver statement, not an unsupported orthogonality claim for the two received states.

The trial vanishes near both physical endpoints. Its actual correction still has the complete endpoint and mean response supplied by that receiver. The reference's zero trial trace does not make the actual response trace zero.

To enter WQS.26--28 or WDS, place these complete errors into the actual four-block approximation with the specified left and right trial factors. The signed low rows, the original $c_{96}$ right side, the 97-dimensional root complement, the actual 96 physical columns and their still uncomputed signed normalization, both stored density means, the independent physical mean, $\nu$, $\Theta$, cokernel rows, and independent external functions remain separate and unchanged.

## K6. Callable specification for a new full-input calculation

No scientific callable is executed by this appendix. A subsequent fixed Actions consumer may implement the following pure interfaces.

- prepare_reference_kernel(mode, reference): return the exact reference definition, the complete piecewise $p,H$ representation, and the two factors in (K.6), with raw seam continuity and original boundary conditions.
- signed_residual_factors(r_piece, s_piece, side): form complete signed $D_{\rm loc}$ and the two complete angular products in (K.10), then apply (K.11).
- forward_integral_bound(output_piece, comparison_pair): enclose the full ordinary-$ds$ integral in (K.13), including every input piece and both triangular sides.
- reverse_integral_bound(input_piece, comparison_pair): enclose the ordinary-$dr$ integral of the exact same positive majorant in (K.14), including every output piece and the full local multiplication.
- complete_source_port_bound(port, comparison_pair): save complete row/column bounds, their square-root product and all scope before any whole candidate comparison.

The frozen contract must specify the finite angular support, all original genuine seams and reference subdivisions, every comparison weight, the complete source and output coordinate maps, and an actual interval integration or analytic-moment rule. It must bound all inputs, including the head mean, and all outputs in the declared support.

Uncomputed kernel integrals, reference coefficients, full-input residual norms, signed finite contractions and finite gates remain new targets. Existing completed collar/body receiver records, difference fees, principal-tail bounds and source identities are read verbatim. No old numerical target is recomputed, and no actual inverse or small residual is asserted.
