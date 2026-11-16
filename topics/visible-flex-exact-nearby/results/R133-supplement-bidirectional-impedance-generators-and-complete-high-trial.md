# R133 supplement: bidirectional impedance generators and an all-input high-response trial

2026-11-16, newton_source.

WIC proves the actual inherited refinement-160 tail inverse with norm at most 3 and fixes a complete reference finite inverse in the true weighted coordinates. This supplement gives a more efficient exact representation of that same reference inverse and specifies a full-input high-response trial for the next signed residual calculation.

The reference finite matrix has dimension 193N+193 with N=24480. Its radial off-diagonal blocks can be represented by scalar transition products. No division by a transition is used. The new high trial takes every L2 radial head input, including its mean, and has a complete ordinary source residual in the original seven-port problem. It is not a collection of sampled columns. No new norm or actual finite inverse is evaluated or asserted here.

## WQS1. The same complete finite coordinate maps

Use WIC.6--16 without change. Each nonzero mode is the normalized real pair
(sqrt(2) sin(4j phi),sqrt(2) cos(4j phi)), 1<=j<=96. Its inputs are N odd and N even normalized cell row coefficients and the two raw endpoint row coordinates. Its outputs are N odd and N even normalized cell coefficients, the root odd coordinate, and the actual outer H^{-5/6} coordinate.

The physical mean is the separate N+1 dimensional circuit in WIC.24. The full root complement contains these 96 odd coordinates and that mean. Prescribed c96 remains in the two original WOB/WDS right-side rows; it is not a second initial condition in the circuit.

Let the complete signed WIC coefficients be p_i,tau_i,lambda_i,mu_i,sigma_i,upsilon_i, with p_N=p0=13/80. Write
$$
 g_i=\tau_i g_{i+1}-\lambda_i r_i^o-\mu_i r_i^e,\qquad
 g_N=g^o+p_0g^e,
 \tag{WQS.1}
$$
$$
 \zeta_{i+1}=\tau_i\zeta_i+\sigma_i g_{i+1}
                    +\sigma_i r_i^o-\upsilon_i r_i^e,\qquad
 \zeta_0=0,\qquad \xi_i=g_i-p_i\zeta_i .
 \tag{WQS.2}
$$
Every scalar refers to the fixed same mode and the same complete mesh. The index is suppressed only for readability.

The primary rational normalizer is rho_2(x)=1+x^2/12. Its WIC halfsteps obey
$$
 a_ib_i=\frac{x_i^2}{4\rho_2(x_i)^2}\le\frac34,
 \qquad
 \rho_2(x)^2-\frac{x^2}{3}=(1-x^2/12)^2\ge0 .
 \tag{WQS.3}
$$
Consequently this particular reference has 0<tau_i<=1. The algebra below needs no positivity of tau and remains valid for the general WIC circuit, including a zero transition. The stronger sign is useful for bounds; it does not authorize subtracting norm upper bounds for any other coefficient.

## WQS2. Two independent scalar states

Define
$$
 H_0=0,\qquad H_{i+1}=\tau_i^2 H_i+\sigma_i,\qquad
 y_i=\zeta_i-H_i g_i .
 \tag{WQS.4}
$$
This H_i is a scalar circuit coefficient. It is unrelated to the Airy matrix H, the head Hilbert space or a physical mean.

Substitute (WQS.1) in (WQS.2), then subtract H_{i+1}g_{i+1}. The exact result is
$$
 y_{i+1}=\tau_i y_i+\alpha_i r_i^o+\beta_i r_i^e,\qquad
 y_0=0,
 \tag{WQS.5}
$$
where
$$
 \alpha_i=\sigma_i-\tau_iH_i\lambda_i,\qquad
 \beta_i=-\upsilon_i-\tau_iH_i\mu_i.
 \tag{WQS.6}
$$
The backward state g and forward state y are now independent recurrences driven by the original input. Recover
$$
 \zeta_i=y_i+H_i g_i,\qquad
 \xi_i=(1-p_iH_i)g_i-p_i y_i .
 \tag{WQS.7}
$$
Every difference in (WQS.6)--7 is a complete signed scalar expression. Its enclosure is not obtained by subtracting independently saved positive norm uppers.

Let K_i=1-p_iH_i. Before the final WIC output weights, the two cell brackets are
$$
 \binom{\rho_i v_i^o}{\rho_i v_i^e}
      =F_i y_i+G_i g_{i+1}+D_i^{\rm loc}\binom{r_i^o}{r_i^e},
 \tag{WQS.8}
$$
where
$$
 F_i=\frac12\binom{-p_i-p_{i+1}\tau_i}{1+\tau_i},\qquad
 G_i=\frac12\binom{K_i\tau_i+K_{i+1}}{H_i\tau_i+H_{i+1}},
 \tag{WQS.9}
$$
$$
 D_i^{\rm loc}=
 \begin{pmatrix}
 1-\frac12(K_i\lambda_i+p_{i+1}\alpha_i)&
       -\frac12(K_i\mu_i+p_{i+1}\beta_i)\\
 \frac12(\alpha_i-H_i\lambda_i)&
       1+\frac12(\beta_i-H_i\mu_i)
 \end{pmatrix}.
 \tag{WQS.10}
$$
The actual output is sqrt(h_i)S_i v_i. Thus the source implementation multiplies the first bracket by sqrt(h_i)/rho_i and the second by sqrt(h_i)s_i/rho_i. Inputs r_i still use the complete inverse weights 1/sqrt(h_i) and 1/(sqrt(h_i)s_i).

The two remaining modal outputs are
$$
 d_j=g_0,\qquad
 \widehat b_j=\theta_j\{y_N+H_Ng_N-g^e\}.
 \tag{WQS.11}
$$
Both the direct -theta_j g^e term and the independent p0 g^e path inside g_N remain. These are the same rows as WIC, not new boundary conditions.

## WQS3. Off-diagonal rank one without inverses of tau

For a<=b define the product
$$
 P(a,b)=\prod_{\ell=a}^{b-1}\tau_\ell,\qquad P(a,a)=1.
 \tag{WQS.12}
$$
The exact states are
$$
 g_{i+1}=P(i+1,N)g_N+
       \sum_{k=i+1}^{N-1}P(i+1,k)(-\lambda_k r_k^o-\mu_k r_k^e),
$$
$$
 y_i=\sum_{k=0}^{i-1}P(k+1,i)(\alpha_k r_k^o+\beta_k r_k^e).
 \tag{WQS.13}
$$
Thus for k>i the raw body block from cell k to cell i is
$$
                G_iP(i+1,k)(-\lambda_k,-\mu_k),
 \tag{WQS.14}
$$
and for k<i it is
$$
                F_iP(k+1,i)(\alpha_k,\beta_k).
 \tag{WQS.15}
$$
Complete input and output diagonal weights surround these formulas.

Across any fixed radial cut, split each transition product at that cut. Every strictly upper cross block factors through one scalar state, as does every strictly lower cross block. Each therefore has rank at most one within a fixed angular mode. This property is often called a quasiseparable representation; equations (WQS.12)--15 are its exact definition here.

No ratio of products is taken. A zero tau is preserved as a zero transition and causes no singularity. Local two-by-two blocks, the two endpoint inputs, root output and weighted outer output are additional complete pieces; they are not discarded to claim the rank.

The complete 96-mode circuit is a direct sum of these pieces and the independent mean circuit. Angularly coupled actual coefficients may mix the modes later. Their coupling does not disappear because the reference happens to split.

## WQS4. Exact transpose and a collected positive majorant

The companion no-entry source first forms all complete signed coefficients in (WQS.6), (WQS.9)--10, then applies the two independent states. Its reverse algorithm is the exact transpose:

- reverse the weighted local output maps;
- reverse the forward y recurrence in decreasing cell order;
- reverse the backward g recurrence in increasing cell order;
- return both terminal g_N paths and the direct outer path.

The reverse accumulator of y_0 is not an input. The root output contributes to g_0. Every input and output factor in WIC.5 is traversed exactly once.

Take outward absolute values only after the signed local contractions have been formed. This gives one positive state graph that entrywise dominates the exact same Q_j. A full all-ones forward pass and a full all-ones reverse pass provide complete row and column sums in O(N). The square root of the product of their maxima bounds the whole two-norm.

This collected majorant can be sharper than taking absolute values in the longer WIC graph. Both bound the same exact operator. A later comparison must retain complete norm candidates; it does not select signed entries from different operators. There is still no extra sqrt(96) in the final modal maximum.

A more useful complete candidate uses positive comparison weights. Let M be the entire positive majorant, v>0 on every input coordinate and w>0 on every output coordinate, and set
$$
 R(v,w)=\max_a\frac{(Mv)_a}{w_a},\qquad
 C(v,w)=\max_b\frac{(M^t w)_b}{v_b}.
 \tag{WQS.15a}
$$
Then
$$
              \|Q_j\|_2\le\|M\|_2\le\sqrt{R(v,w)C(v,w)} .
 \tag{WQS.15b}
$$
Indeed, weighted Cauchy--Schwarz gives
|(Mx)_a|^2 <= (Mv)_a sum_b M_ab |x_b|^2/v_b.
Sum over a, use Mv<=Rw and M^t w<=Cv, and obtain (15b). This is a bound in the unchanged actual Hilbert coordinates; no condition number of a coordinate similarity is being omitted.

One predeclared comparison pair is
$$
 v_i^o=w_i^o=\sqrt{h_i},\qquad
 v_i^e=w_i^e=\sqrt{h_i}s_i,\qquad
 v_{\rm end}^o=v_{\rm end}^e=w_{\rm root}=1,\qquad
 w_{\rm outer}=\theta_j .
 \tag{WQS.15c}
$$
All these weights are strictly positive by the existing coordinate contract. The raw source weights in the graph cancel the corresponding cell factors in Mv; the endpoint-to-body factors cancel the output comparison weights. The reverse graph integrates the corresponding cell lengths. This prevents a purely artificial sqrt(N) contribution from replacing a bounded integral by an unweighted endpoint row sum. It does not assert an N-independent estimate for an arbitrary actual coupled remainder.

The code evaluates M at complete upper weight endpoints and divides by complete positive lower endpoints of w. It evaluates the exact transpose of the same M at complete upper endpoints of w and divides by positive lower endpoints of v. It takes the upper of each quotient before the maximum. Thus nonexact square roots and interval weights cannot invalidate the Schur bound. All-ones, (15c), or another predeclared pair are distinct complete norm candidates for the same Q_j; an implementation records each whole candidate before any whole minimum.

The physical mean still uses its complete exact WIC shear norm. No sqrt(96) appears in the modal maximum. The source consumes a fully prepared WIC mode. It imports no old or new scientific producer, creates no files, and has no entry point. Reading it does not evaluate H_i, the weights, or any new norm.

## WQS5. A continuous principal high Green operator with the same stable structure

Here is an explicit full-input trial for the actual high given-head response. It is separate from the proven actual G_H and is not used as a replacement theorem for it.

For a high angular mode j, set k=4j and choose the same nonnegative piecewise-constant eta_hat and positive q reference. On the original positive interval define
$$
 \xi'=\kappa q^2\zeta+f_o,\qquad
 \zeta'=\kappa\xi+f_e,\qquad \kappa=k\widehat\eta\ge0,
 \tag{WQS.16}
$$
with reference conditions zeta(r_star)=0 and xi(R)+p0 zeta(R)=0. Raw states are continuous across every reference subdivision. A change in q does not impose continuity in a changed S coordinate.

The backward impedance solves
$$
        p'=\kappa(p^2-q^2),\qquad p(R)=p0 .
 \tag{WQS.17}
$$
On a constant-reference cell of length h its exact update is
$$
 p_{\rm left}
   =q\,\frac{p_{\rm right}+q\tanh(\kappa qh)}
                {q+p_{\rm right}\tanh(\kappa qh)}.
 \tag{WQS.18}
$$
Its denominator is at least q>0; p stays between its terminal value and q. Consequently p is positive and bounded on the entire finite interval. The actual root curvature is not a denominator. A zero reference generator gives an identity cell.

Writing xi=g-p zeta gives
$$
        g'=\kappa p\,g+f_o+p f_e,\qquad g(R)=0,
 \qquad
        \zeta'=-\kappa p\,\zeta+\kappa g+f_e,\quad \zeta(r_star)=0.
 \tag{WQS.19}
$$
The first equation is integrated backward and the second forward. Both use decaying propagators in their integration direction. A homogeneous energy identity, with terminal value -p0 zeta(R)^2, proves uniqueness. Existence follows from these explicit formulas. This defines a genuine bounded reference map on the complete L2 source space for the finitely many declared angular modes.

There is also a continuous independent-state form. Let
$$
       H'=\kappa(1-2pH),\qquad H(r_star)=0,\qquad y=\zeta-Hg .
$$
Then
$$
       y'=-\kappa p\,y-Hf_o+(1-Hp)f_e,\qquad
       \xi=(1-pH)g-py .
 \tag{WQS.20}
$$
If p_min is a complete positive lower for p, scalar comparison gives
0<=H<=1/(2p_min). This is a bound on this reference function, not on any actual background coefficient.

For the homogeneous transfer, use tanh x=(1-exp(-2x))/(1+exp(-2x)) and sech x=2exp(-x)/(1+exp(-2x)). All exponential arguments are nonpositive. Root x=0 has its exact identity branch. No large positive transfer matrix needs to be formed or inverted.

This reference high Green map, denoted G0, still carries all physical angular weights. In a single mode the source normalization is Lambda_j^{-2/3} and the raw-state normalization is Lambda_j^{-1}; the corresponding kernel conversion is included before a Hilbert norm is taken. A raw Euclidean kernel estimate is not silently relabeled as the original source-to-state norm.

## WQS6. A concrete full-input trial that needs no signed root or outer chart

Let B_HL^0 be exactly the original frozen degree32-centre cross block used by WPTVS, including all its signed ordered primitive terms. Its entire 193-dimensional input is retained. Its high output is supported in modes 97 through 160 because its total angular shift is at most 64. Its zero high image for the mean and certain low inputs is a centre identity, not a property assigned to the full degree96 family.

Set G0 to act on all these 64 high modal pairs. Fix a C1 scalar cutoff chi, identically zero on the original collar and near R, and supported in the original positive interval. One fully specified choice is the product of two cubic smooth steps:

- chi_L=0 through c_body and 1 from c_body+1/32 onward;
- chi_R=1 through R-1/16 and 0 from R-1/32 onward;
- each transition uses P(t)=3t^2-2t^3 on its stated affine unit interval.

Then chi=chi_L chi_R has all its actual transition derivatives retained. No cutoff is chosen after a numerical residual is observed.

For every actual L2 head a define
$$
       v=G_0(\chi B_{HL}^0 a),\qquad
       \widehat{\mathcal P}_a a=\chi v.
 \tag{WQS.21}
$$
The trial is a linear bounded operator on the full head space, not a table of selected head columns. Its reference state v is radially H1 on each piece and continuous in raw coordinates. The cut trial has zero raw trace near both physical endpoints.

Let L_H=partial_r-A_HH be the actual high differential operator. Direct differentiation gives the complete ordinary residual
$$
 \boxed{\quad
 L_H(\chi v)-B_{HL}a
 =(\chi^2B_{HL}^0-B_{HL})a+
          \chi'v-\chi(A_{HH}-D_H^0)v .
 \quad}
 \tag{WQS.22}
$$
No radial derivative of the arbitrary head a appears. The cutoff derivative, the full actual-minus-reference generator and the entire cross-block difference are present.

The source remains in the original L2(dr;H^{-2/3}) pair window. With the full actual degree96 background, applying A_HH to this trial has support at most mode 352. This is a finite residual support statement, not a claim that the true high state is bandlimited.

The head mean is not removed. The centre may have a zero mean-input high column, but the first term of (WQS.22) retains the complete actual B_HL on that column. Similarly all actual physical mean/finite equations outside the high subsystem retain their original rows.

For this zero-stable, zero-exterior-column trial, the root and exterior high mismatches are zero because the trial vanishes in neighborhoods of both endpoints. Its raw identity-interface jumps are zero. Reference coefficient changes create ordinary piecewise residuals, not impulses. Original independent affine jump ports are still separate inputs of the actual problem; (WQS.21) does not set those ports to zero in a different right side.

Thus the correction for this trial can be paid by the original two ordinary-source columns of the complete seven-port receiver. It requires no guess for a signed root chart or a signed regular exterior map. Whether this first trial is sharp enough is a numerical question, not asserted here. A later trial with nonzero boundary traces must pay its actual complete chart defects.

## WQS7. Centre data and complete difference fees

The approximation in (WQS.21) can use exactly the same frozen signed B_HL^0 whose parent reference hashes appear in the completed WPTVS chain. On the body,
$$
 \chi^2B_{HL}^0-B_{HL}
   =(\chi^2-1)B_{HL}^0-(B_{HL}-B_{HL}^0).
 \tag{WQS.23}
$$
The final term, with its true S^{-1} input conversion, can use the already completed whole E_b. The cutoff term is a new complete contraction. On the original collar B_HL^0=0, and the whole original A_c bound applies. Neither old quantity is computed again.

For signed local pairings, restore or materialize only the declared degree32 centre and the exact reference definition. The complete original degree96 difference and repair are paid by their saved whole enclosures and the exact ordered two-factor decomposition. It is unnecessary to recover signed degree96 shards merely to enclose that difference. No difference is obtained by subtracting two norm uppers.

Likewise every occurrence of A_HH-D_H^0 in (WQS.22) retains the actual principal coefficient difference, drift, reaction and ordered nonlocal primitive. Only exact cross-cutoff identities already proved in WPTV may remove a term. In particular the independent low physical mean remains in A_L and the actual outer/mean row. The finite source support does not discard the high error beyond the reference support.

If an approximate low row also uses B_LH^0 rather than the actual B_LH, its complete difference is kept. For example
$$
 B_{LH}\mathcal P_a-B_{LH}^0\widehat{\mathcal P}_a
 =B_{LH}(\mathcal P_a-\widehat{\mathcal P}_a)
       +(B_{LH}-B_{LH}^0)\widehat{\mathcal P}_a .
 \tag{WQS.24}
$$
The first term uses the full true shell receiver; the second is a new complete signed/interval contraction on the finite trial. This decomposition does not charge a false zero to the centre-to-actual difference.

For a complete ordinary residual norm vector alpha, retain the original receiver statements
$$
 \|v_{\rm true}-v_{\rm trial}\|_{\rm raw}
       \le{\bf c}\cdot\alpha,\qquad
 \|y_R-y_{R,\rm trial}\|_{H^{-5/6}}
       \le4{\bf y}\cdot\alpha .
 \tag{WQS.25}
$$
If a saved WOBSA row already includes the factor 4, it is read once instead. The complete endpoint error is placed in the actual C0/outer row. It does not disappear when the chosen trial has zero endpoint.

The trial for the independent b column may initially be zero, in which case its complete original B-port defect and mean/height conventions are retained. This is a full candidate, not a claim that the actual b response vanishes. More accurate b, root or external-function trials require their own complete old-port normalization.

## WQS8. Full residual transfer from a certified operator approximation

Let Acal=[A B; C R] be the full WDS operator in its true weighted spaces. Let Ahat be any fully specified finite-state trial for that entire operator, formed using the preceding new high trial, signed local rows and complete approximate outer rows. Its construction must specify every block. An unsigned norm column is not a signed trial row.

Keep the WIC Q_f and principal tail trials Z,Y. Define
$$
 \widehat T=\widehat C-\widehat R Z,\qquad
 \widehat D=\widehat B^*Q_f^*-\widehat R^*Y,
$$
$$
 \widehat E_0
   =Id-\binom{Q_f^*}{-Y}^{\!*}
                   \widehat{\mathcal A}\binom{Id}{-Z}.
 \tag{WQS.26}
$$
Before any positive majorant, remove the exact principal identity as in WIC.36. This prevents an artificial estimate of Id and its cancelling principal inverse as two unrelated large norms. It does not remove an actual coefficient, boundary or mean term.

Suppose a full-input certificate gives
||Acal-Ahat||<=epsilon in the actual product spaces. Put
$$
       L_*=\sqrt{\|Q_f\|^2+\|Y\|^2},\qquad
       R_*=\sqrt{1+\|Z\|^2}.
$$
The complete error transfers are
$$
 \|T-\widehat T\|\le\epsilon R_*,\quad
 \|D-\widehat D\|\le\epsilon L_*,\quad
 \|E_0-\widehat E_0\|\le\epsilon L_*R_* .
 \tag{WQS.27}
$$
These follow by projection and the exact left/right trial factors. They retain all four blocks. They do not infer a whole norm from finitely many tested head inputs.

Consequently one valid actual finite certificate is
$$
 \|\widehat E_0\|+\epsilon L_*R_*
  +3(\|\widehat D\|+\epsilon L_*)
       (\|\widehat T\|+\epsilon R_*)<1 .
 \tag{WQS.28}
$$
The factor 3 is the actual tail bound already proved in WIC.1. It is not an assumed inverse of the reference trial.

A single epsilon may be unnecessarily large. A sharper implementation may propagate a complete block-error matrix or a complete receiver factor through the same left/right trial graphs. Then the cell and outer Riesz factors can combine in their actual order before taking norms. Every complete alternative must still include all blocks and all direct boundary/mean terms; entries from different trial operators cannot be mixed.

The original two right-side rows are unchanged. WDS.10--11 supplies their complete evaluation and tail reconstruction after an actual strict gate. No part of this argument removes c96, d97, b96, nu, Theta, either stored density mean, the independent physical mean equation, cokernel rows or independent external functions.

## WQS9. A concrete small-output computational contract

The following staged preparation is finite and reproducible, without a dense 4724833-square allocation.

1. Admit the complete published WIC/WDS/WPTVS identities and exact coordinate recipe. Reuse the existing 153-parent reference chain and inherit refinement 160. Materialize coordinates only; do not rerun a completed coefficient maximum or repair bound.

2. Prepare one complete WIC mode, form the signed coefficients (WQS.4--10), and retain its exact symbolic definition. Evaluate interval enclosures in Actions only. Process modes sequentially. Whole reference norm targets use the full weighted forward/reverse graphs of (15a), with the all-ones candidate optionally retained; no individual basis-column enumeration is necessary.

3. If the high trial is selected, declare exactly modes 97..160, the reference two-point conditions, cutoff above, the complete signed centre cross matrices and source/target weights. Construct its full scalar-state kernels using (WQS.17)--20. All parent transitions are in raw coordinates.

4. Enclose (WQS.22) as an operator on all L2 head inputs. Its local term and finite-state terms admit complete weighted row/column kernel estimates or another proved full-input norm method. Ordinary collar/body pieces, all endpoint/mean conversions and any additional original ports are included before the old receiver is applied.

5. Form the complete signed finite-state expression (WQS.26), with the principal cancellation already exact. Use a full positive graph only after each complete signed local contraction. Kernel row/column integrals, not samples, must be enclosed. Reverse that same graph for the dual whole sums. A general angular coupling costs a full small block contraction; the rank-one radial structure does not make it diagonal.

6. Save complete new target records, full candidate scope, exact coefficients/source identities, complete input coverage and the last completed target/prefix. Temporary coefficient and state arrays stay in Actions. No new matrix or per-cell-array artifact is published.

The scalar-state transition representation has storage proportional to N per angular channel; it never uses inverses of tau. A complete reference norm uses O(96N) work. The actual coupled residual includes new angular contractions and kernel integrations, whose full count must be budgeted separately before a run. This theorem does not label that additional work O(96N) without proof.

A numerical manifest must freeze its finite-state rank, quadrature or analytic-moment order, angular support, rounding precision, memory, runtime and output caps. Any deficient full-input estimate is a complete failed candidate; it cannot trigger an automatic mesh, support or trial enlargement. The frozen m160 actual-tail theorem is not lost if a subsequent finite candidate fails.

## WQS10. Complete scope and primary identities

The actual refinement-160 tail inverse and all completed old bounds remain as proved in WIC. The present results are: an exact rank-one off-diagonal representation of the same finite reference inverse; its exact weighted transpose and whole norm recipe; an explicit bounded principal high Green trial; and its complete all-input residual and transfer to the actual signed certificate.

No new numerical target or actual finite inverse has been evaluated. No background PDE exactness, actual low-input rank cancellation, signed regular chart, global physical inverse, negative radial head or metric inverse is added.

| Primary | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WIC actual inherited tail and complete weighted reference | 019b1136ebe81e44e98399dff5fb895aafb4362e | 29026 | 527fc35e48f8bb8807e2dc7e7a4b8726e381d35183f31bf8977b252dbb66e59f |
| WIC no-entry complete modal circuit | b181bb80373c870769e2c35b28e764ab7be76e44 | 11013 | c5de896f603424c0fed3892287031d38d775843e55580f52f4759fe1daba4de3 |
| WDS full four-block and seven-port certificate | 5e93ca37c37d82787ea870aad977712f41b2d4ea | 32943 | 4c7c9d6e582a486f0fe233ac2e617b0f3136ac8a1ed168001f7134050b2230f9 |
| Completed WPTVS actual | c79f9de99b0f6e398c97f840e82a7e653b5e6626 | 24767 | bdd8857cf98d3497600b349b05fc81b8aab7441cd7020b6a5f337b6067f774ef |
| WPTV complete centre/actual difference theorem | ddccd14e855ba95048fe92cbd21edfb82ebd8e6f | 21178 | dda500b8f5e2d02a39fbef4efcc5c2ad10dac93eef194f6e8d5b9b5a816cd0e9 |
| New no-entry bidirectional generators | d39ae08753f04a5b59c90231d605f8443b8cb9eb | 10070 | 878c4aec5ed14f4d5e5f3d24ecd23476373a5e26c7b1dd4119b2198e9b73bb02 |

No original scientific producer was imported or executed.
