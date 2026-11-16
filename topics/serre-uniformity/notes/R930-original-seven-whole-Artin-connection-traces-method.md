# R930 execution method: seven original whole-Artin target connections and traces

## 1. The completed inputs

This execution consumes the exact formulas already proved in the final R922 paper, Sections 6–10. It does not introduce a replacement connection, projector, or height normalization.

R922 has completed the original four-coefficient polynomial matrix $R=gG^{-1}$, with all eight coefficients of $RG=M_g$ verified. Its actual run is `43913992769`, source `fec176005094b37d86b143de7e460b4ab60471ea`, configuration SHA `94a0009b06ff3ca92b2eacafdc2bbf526c1facec2b9ef5d5c3dec4ab9fb576cd`. The complete certificate is 11,271 bytes with SHA `921c5992dfe0658e8febfb21cb4a435f5bb72eb34baa6af79ada8514e7bebce9`.

R926 has completed all seven bounded numerator expressions and every one of their $277\cdot272$ polynomial equations. Its actual run is `43916091665`, source `665dd92b8703fa7118d90fbee0eba7f07e2d60ee`, configuration SHA `8d865612158629b0241e9a0f0799ad6ae4270fd934a43af2d3782e040cc697ff`. The complete certificate is 12,088 bytes with SHA `e60d5ebbe3c4a6b3632db30856c5f697130ba41fb26f352b72983616fea6bb54`.

R928 has completed the original full quotient derivative and target differential-frame ratio $J$ in actual run `43918212179`, source `10288e01680361bddf2a650cd98c38eb7b47889e`, configuration SHA `68132fe8e1e35804bde764cee49cba9d4f207630963303b8c44033dbf0693f5d`. Its complete certificate is 20,552 bytes with SHA `713fcc41b6276513dbad0110fa660963d9d8c93c91f95007c29ab8bb69e66f5c`. The wrapper reads the selected integer $t$ and the exact unit-trial reference from the already completed, manifest-bound transport stage. It does not infer either from a stage count or the proposed trial schedule.

The remaining inputs are completed: R905 identifies the seven exact section-1 connections and original 543-coordinate gauges; R885 supplies the whole correspondence and every target normal coordinate; R919 supplies the completed differential-trace row. All old sources retain their original identities. The R928 carrier can transport the required R885 and R919 files without downloading their old larger archives. Only the R905 metadata and complete certificate are required to compare the original connection and auxiliary-place identities.

## 2. Exact conventions

The divisor labels, in order, are
$$
D_1,D_2,D_3,D_4,D_5,X,D_N.
$$
For each label the original connection is on $\mathcal O(H-D)$, in its rational section $1$, with the full logarithmic principal parts $H-D$. The exact expression is
$$
\alpha_D=B_D\nu,\qquad
B_D=\frac{y_D^tR\beta}{d_D}.
$$
Here $y_D$ has the original 274 coefficient rows, and $d_D(z)=\det F_D(z)/\det F_D(a_D)$ has the original 273 coefficient slots. These include any zero leading coefficients; no squarefree replacement is made.

The auxiliary place remains $\ell=1000000753$, with the original $\zeta=549966761,s=99932770,B=3197390$. The source fibre is the completed $z_s=0$ fibre. The full algebras are
$$
A_0=\mathbf F_\ell[X]/(\chi_0),\qquad
E=A_0[U]/(P/a_8),
$$
of dimensions 272 and 2176. The target coordinate is still $V=K(U)/P_U(U)$. No coefficient or value from a different branch or prime is admitted.

The selected source carrier stores the original R922, R926, R928 and R905 metadata and only the needed completed mathematical outputs. The R928 original input carrier is hashed in full; the new carrier retains just the required original R885 and R919 members. The actual selected unit-trial file is derived from R928's completed transport, checked against that producer's full manifest, and included unchanged in the expanded configuration and mathematical tag.

The new source checks compare the original R827 identity across R905, R922 and R928. They also compare the R885/R919 source identities and each selected reference with R928's actual source inventory. A successful finite-place computation remains a computation at this place, not a characteristic-zero coordinate expansion or a prime-41 period.

## 3. Test the complete target denominator first

For each label evaluate the actual scalar polynomial $d_D(U)$ by Horner evaluation in all of $E$. The frozen whole-Artin helper computes its rank-eight characteristic polynomial, retains all bottom-algebra factors, proves the full norm Bézout identity against $\chi_0$, and multiplies any inverse back in all 2176 coordinates.

Only a whole-algebra unit permits the target quotient in this scope. The previously completed $F_D(a_D)$ unit is not used to infer this target unit. If $d_D(U)$ is a nonunit, retain the entire witness, mark that label unresolved and proceed to the other labels. No component is removed and no cancellation is claimed.

Such a failure can arise from a nonminimal determinant denominator. It does not establish that the exact connection or its true target value fails to exist. Resolving it would require an actual complete local-module cancellation or a separately certified source fibre. That is not silently performed here.

## 4. Finite matrix contractions before $U$-Horner

Let $\epsilon=(0,1^{144},2^{127})$. The completed sources give
$$
\deg y_i\le271+\epsilon_i,\qquad
\deg R_{ij}\le3-\epsilon_i-\epsilon_j.
$$
Thus, for $r^t=y^tR$,
$$
\deg r_j\le274-\epsilon_j.
$$
The core computes all 277 coefficients of the product using four finite-field matrix products per coefficient block. It checks every weighted zero, including both complete degree-275 and degree-276 rows.

For a block of 16 polynomial coefficients, multiply the resulting $16\times272$ matrix by the already completed $272\times2176$ table of all target $\beta_j(U,V)$. This yields coefficients in the complete $E$, not values at selected geometric points. Save that contraction as an immutable block, then run $U$-Horner in descending block order. The resulting numerator is
$$
N_D(U,V)=\sum_j r_j(U)\beta_j(U,V).
$$
The core records the complete Horner chain so a budget stop does not replay completed contractions or higher-degree blocks.

After the whole denominator unit has succeeded, set
$$
B_D(U,V)=N_D(U,V)d_D(U)^{-1}
$$
and verify all 2176 coordinates of $d_D(U)B_D=N_D$. The old $R,G,y,d$, normal coordinates, Schur systems, Gamma data and inverses are never recomputed.

## 5. The complete ordinary trace and the old differential trace

The completed R928 source provides $J$ and its full identities
$$
Jg_t=\dot U,\qquad Jh_t=\dot V.
$$
This scope reads $J$ unchanged and never asks for $J^{-1}$.

The direct target differential trace is
$$
\operatorname{Tr}_{\pi_s}(\pi_t^*\alpha_D)
=\operatorname{Tr}_{E/A_0}(B_DJ)\,\nu_s.
$$
The trace is the trace of the full rank-eight multiplication matrix over the original $A_0$; all 272 source coordinates are retained.

For reusable linear evaluation, the core forms the new ordinary trace row
$$
\mathcal T(e)=a_8^{-1}[U^7](eP_U\bmod(P/a_8)).
$$
It uses the original $a_8^{-1}$ and $P_U$, and verifies all eight basis values against the full rank-eight multiplication diagonal. This is the complete coefficient identity needed by the current computation, not a second task or a new trace-Gram inverse.

For each connection, save the entire multiplication diagonal of $B_DJ$, its trace, and the ordinary-row evaluation; compare all 272 entries. Also check the original R922 quotient-transport expression
$$
\mathcal L\!\left(B_D\ell_t^{-1}(1+tP_U^{-1}\mathcal H_K)\right)
+t\mathcal T\!\left(B_D\ell_t^{-1}P_U^{-1}\Delta_K\right),
$$
where $\mathcal L$ is the unchanged completed R919 differential row and every remaining factor is read from R928 or the original correspondence. The two methods must give the same complete source-algebra vector. No $\delta K,\delta P,\dot U$, inverse, or original Gamma calculation is repeated.

The trace has its original unnormalized rank-eight convention. No factor $1/8$, $1/7$, or unexplained sign is introduced.

## 6. Frames and exact expressions

The exact output DAG is the composition of the original R926 section-1 connection, the original R922 trace-dual expression, and the original R928 differential transport. The actual direction of the computed table is
$\operatorname{Tr}_{\pi_s}\pi_t^*\alpha_D$. The canonical dual-7 transport to the frozen Hecke direction, both determinant frames, scalar 7, the diamond action, the original minus-3 descent, and the original $\kappa,\nu$ constants remain explicitly sourced.

This table does not evaluate the endpoint rigidification constants. It does not replace the true geometric semilinear $c_Y$ by coefficient conjugation.

In particular, the $D_N$ table is the trace of the original $\alpha_{D_N}$. It has not yet been corrected by $-d\log Q_N$. The later original construction must first form $\alpha_{D_N}-d\log Q_N$, then perform its actual sevenfold average. Likewise, the five $Q_j$ already include their original negative $\chi$-powers. This consumer performs no principal-function correction, Galois average, or $c_Y$ average and does not claim the five Picard inputs numerically complete.

## 7. Stage identity and endpoints

The result is `R930-original-seven-whole-Artin-connection-traces`; the final filename is
`p41-original-seven-whole-Artin-connection-traces-certificate.json`.

The tag binds the core, unchanged algebra helper, method, original proof files, selected source identities and byte specifications, all mathematical inputs, and the fixed strategy. The time budget and requested divisor-prefix length are runtime controls. The source order and block size are fixed by the strategy.

Each label has a complete target-denominator witness, coefficient-contraction blocks, a descending Horner chain, and a complete target-value/trace certificate if its unit succeeds. The shared ordinary-trace row and transport factors are also atomic complete stages. A content-named stage manifest lists the actual complete stages; the current checkpoint remains explicitly incomplete.

Completion means all seven actual target quotients and all seven complete differential traces have passed the described identities. A failed denominator or incomplete budget yields an honest incomplete final while preserving every complete stage. Restoration uses the same core/tag and actual manifest; a historical incomplete final does not constrain a newer current checkpoint.

All new mathematical execution occurs only in the authorized public Actions. The wrapper only performs source/hash/schema/shape work. Full five-Picard $\sigma/c_Y$ combinations, principal calibrations, original Hecke projectors, endpoint values, non-$p$ terms, Poincare periods and heights remain false.
