# R893 — Certified complete initial RR spaces for the five original sum-Hom maps

Date: 2026-11-16. Session: serre-public-astra-20261115.

**Status: actually completed in the public repository's GitHub Actions.** All five original initial Riemann–Roch spaces, with dimensions $168,376,250,386,343$, have complete source-bound characteristic-zero unit-solve definitions. Their modular arrays, selected unit minors, and every original whole-fibre relation have been certified. This does not yet produce the marked two-section pencils, the padded degree-272 representatives, the five $L_j$ spaces, or a height exclusion.

## 1. The actual run and its exact scope

The computation is [run 43861874528](https://github.com/Rogerhu12/math-research-public/actions/runs/43861874528), compute job 133280560534, source commit
$$
\texttt{fe27ac55e0c5d538ac60473df9f1c33f1f90f3b3}.
$$
Its actual conclusion is success, the process exit code is zero, and all five requested directions are complete. The core receipt records 412.672739265 seconds. There are 632 complete mathematical stages and 131 selected original source files; the final full manifest lists 643 files, before its own manifest and reference are added to the artifact.

The mathematical source and transport are unchanged:

| Item | Bytes | SHA256 |
|---|---:|---|
| Mathematical core | 72282 | c199ccbf95de73fb8e1f156a4adaea9ce517cb1c42c427b55c2dcc4901065daa |
| Standard-library wrapper | 61581 | 247980f1ecec1616004dd4569724b8742ce356df8b45a28231b6725c004beaac |
| Execution method | 9112 | 83867053c51ddfed388ff6b07982ffafe0e2993bb91a550ae8fcc1768da7ca6e |
| Activated request | 14276 | f64b3922abe18d512ff243204c24c5e4931c8d503d454a034d47033636590019 |
| Workflow | 6315 | 2b01feaed7931d911530abe0e10a401ea6279fda679d3f67e85327449fbcd426 |

The actual mathematical configuration fingerprint is
$$
\texttt{cd3f53628b4d16176691923ad029eae443075ccc7804927c9377a6d67dc94c9d}.
$$
The detailed source-independent proof is [R893](R893-original-five-sum-Hom-full-fiber-and-initial-RR-Schur-certificates.md); the implemented source contract is the [initial-RR method](../notes/R893-original-five-sum-Hom-initial-RR-consumer-method.md). The actual scripts are [core](../scripts/R893_original_five_sum_Hom_initial_RR.py) and [wrapper](../scripts/R893_public_original_five_sum_Hom_initial_RR.py).

## 2. The five complete spaces and actual unit determinants

Keep the original genus-127 curve $Y$, $H=(\tau=0)$ of degree 272, normal basis degrees
$$
\epsilon=(0,1^{144},2^{127}),
\qquad V_n=H^0(Y,\mathcal O(nH)),
\qquad \dim V_n=272n-126.
$$
For the original positive maps $g_j=(1+T^j)f$, let $y_j$ be the original global target coordinate and $E_j$ its actual pole divisor. The completed space is
$$
\mathcal R_j=\{(A,B)\in V_{n_j}^2:A=y_jB\}.
$$
Projection to $B$ identifies it with the full $H^0(n_jH-E_j)$. The exact objects use the original global function DAG and its true pole ideals; no divisor inferred solely from the auxiliary reduction replaces $E_j$.

All following determinants are actual reductions at $p_{\rm aux}=1000000753$:

| $j$ | $n_j$ | $\deg E_j$ | Complete $\dim\mathcal R_j$ | Actual whole nodes | Schur shape | Actual selected-minor determinant |
|---:|---:|---:|---:|---|---|---:|
| 1 | 12 | 2970 | 168 | 0 through 22 | 3118 × 3138 | 616468787 |
| 2 | 8 | 1674 | 376 | 0 through 14 | 2030 × 2050 | 430045922 |
| 3 | 8 | 1800 | 250 | 0 through 14 | 2030 × 2050 | 995767766 |
| 4 | 13 | 3024 | 386 | 0 through 24 | 3390 × 3410 | 89257000 |
| 5 | 14 | 3339 | 343 | 0 through 26 | 3662 × 3682 | 953617641 |

Each selected minor has size $\deg E_j$ and is a unit at the specified place. The rows, pivot columns, and free columns refer to the unchanged original Schur matrix, not to a relabelled row-reduced matrix.

The full-fibre lengths and global zero budgets are:

| $j$ | Whole-fibre length | Degree bound for $A-y_jB$ |
|---:|---:|---:|
| 1 | 6256 | 6234 |
| 2 | 4080 | 3850 |
| 3 | 4080 | 3976 |
| 4 | 6800 | 6560 |
| 5 | 7344 | 7147 |

The strict inequalities in this table, with the actual whole-denominator units, are exactly the global injection used in the proof. They concern the original $A-y_jB$ relation. They do not assert a generic injection on $V_{2n_j}$.

The coefficient-array shapes of both $A$ and $B$ are respectively
$$
3138\times168,\quad2050\times376,\quad2050\times250,\quad
3410\times386,\quad3682\times343.
$$
These arrays are modular images of the exact unit-solve expressions. No characteristic-zero coefficient array has been reconstructed or asserted to equal a list of residue representatives.

## 3. Why the actual certificate identifies characteristic-zero RR spaces

The frozen core uses the original same-weight-98 numerator and denominator from R893, including the original $\rho_j^3$ correction, Hodge-coordinate transport, and the single exact cancellation already proved there. In each complete algebra
$$
A_a=L[w]/(\chi_a(w)),\qquad\dim A_a=272,
$$
it retains the full characteristic polynomial, including all residue factors and nilpotents. An actual polynomial Bezout identity proves that the complete denominator $Q_j$ is a unit in that algebra. It does not impose unrelated units on the separate $C_0,F,W_j$ factors.

For each $j$, three scalar Vandermonde systems of lengths $n_j+1,n_j,n_j-1$ eliminate $A$ in the unchanged normal basis. The resulting complete Schur matrix $S_j$ has the shape in §2. The independently proved global RR dimension gives its characteristic-zero rank $\deg E_j$. Its actual original selected minor is a DVR unit by the displayed determinant.

Let $I,J,F$ be the retained original rows, pivot columns, and free columns. The exact denominator basis is
$$
B_J=-S_j[I,J]^{-1}S_j[I,F],\qquad B_F=I.
$$
Thus it is a uniquely specified characteristic-zero unit solve. Equal characteristic-zero rank forces every other row of $S_j$ to vanish on it. The core also verifies all original Schur rows on the modular arrays and the whole free-coordinate identity.

It recovers $A$ by the three scalar interpolation blocks and then verifies, at every selected whole fibre, all
$$
272\cdot\dim\mathcal R_j
$$
entries of $A-y_jB$. The strict global inequalities of §2 turn these original fibre relations into the required exact global relation. Projection to $B$ is injective, so these are complete RR spaces with the claimed independent dimensions.

The actual final certificate has all three flags true for every direction:

- complete initial RR space certified;
- all original Schur rows verified;
- all complete-fibre original $A-y_jB$ relations verified.

It keeps the characteristic-zero-reconstruction and later-padding flags false.

## 4. Original sources actually reused

The source audit retains
$$
B=3197390,\quad b=637573097,\quad s=99932770,\quad
\zeta=549966761\pmod {1000000753},
$$
with the original scale relation and the true sigma order
$$
(0,6,1,2,4,3,5).
$$
The original $\rho_j$ values, in direction order, are
$$
265682400,\ 384431414,\ 128277977,\ 173835487,\ 701215367.
$$
These values and every original rational scale are preserved; the integral normal scale is not applied a second time.

The actual selected source counts are:

| Group | Selected original files | Used information |
|---|---:|---|
| R880 | 13 | Seven original normal inputs and six conjugate $A/B$ pairs |
| R877 | 7 | Original zero-branch $A$ |
| R809 | 24 | Six original Hodge coordinates and their complete field-coordinate reductions |
| R849 | 7 | Original global sum-Hom and pole-ideal DAG |
| R827 | 54 | Original normal basis, operators, zero-branch $B$, old Krylov data and original $C$-column |
| R885 | 16 | Completed characteristic polynomial and original old-node data |
| DSTAR | 10 | Already completed five nonzero-branch $B$-derivatives |

The derivative inputs have not been confused with new derivatives. The zero-branch $B$-derivative is transported from the completed original $C$-column and original monic $C$-basis. Five nonzero-branch $B$-derivatives are read from the actual six-$D^*$ output. Only the required six $A$-derivatives are new. The original $g,\Gamma$ operators have 17 row blocks each; no frozen operator source was replaced by a 16-block count.

The eight completed nodes $0,\ldots,7$, their Krylov inverses, and the characteristic polynomial are reused. The remaining required nodes are $8,\ldots,26$. The core constructs only the missing Krylov systems; it checks their original full characteristic relations and both inverse products. Nothing is inferred from selecting a residue-field component.

## 5. Complete-array and unit-minor identities

The following are original manifest entries. All raw arrays remain in the one-day Actions artifacts, not in Git or Releases.

| $j$ | Complete $A$: bytes / SHA256 | Complete $B$: bytes / SHA256 |
|---:|---|---|
| 1 | 2684488 / 230e73193302d05e5ccd91fd6cc490e1a54d143c2a3ea044ad0ad5d4ea95f1c5 | 2550398 / 0db8ed818b1a3a663442174811f8b0401b9c09263181ec0dcb2673610509ed12 |
| 2 | 3910437 / c828b93cc5ed56eb6919b982eb5571520105703a1acbb6e9231b0fea52871661 | 3203270 / de2f6fd731305ba0c914dec13d4715265a376a5c73290da14515304f85cedde1 |
| 3 | 2605898 / 637056221ec135f9d9ed152c0f2aae53296adc4f3362c77c8e14a42f4743a858 | 2295166 / 456632232f9d41f5ec51c373bff46cc2605f12a7f723281b264b18f5826388f5 |
| 4 | 6671125 / 14dab187d0846ad3e619c20832a7c24d954a09843a4007e6c3805b3424cac0d1 | 5930233 / d97146d90b6e24c28521b5de3ab7e50f0e29a489583af2550ead252c908b9939 |
| 5 | 6403602 / 85a6b7c828dd1131ca7d71dd79937c02516cd2bde9b33f52b5c5c20507bc1f1a | 5820259 / 68b64b6e3392aa1c9ae04a3a888e4ef5f50297e5f3c0555e332ca82350019e05 |

| $j$ | Original unit-minor certificate: bytes / SHA256 | Complete initial-RR certificate: bytes / SHA256 |
|---:|---|---|
| 1 | 35418 / 9b530c9e2b12cfd763593cc6e6eb37b2dcea674018a304ab441012d17c4b5244 | 8806 / 1118173ea1a401d43fe109edaa156d732cb5a8fbb2d04c8c8d7391a62daf09dd |
| 2 | 23704 / cf66544e9412a7e9c6d878b682caf7a751eb9210adb81da88362bf4f982d37ec | 8388 / 05de16ad557ca442ed3c6e6edf37b7b21d218ceec9cd3de16e04f2a0f21a8c53 |
| 3 | 24924 / 0f0ebd67c122f9dcd36b20451f402a108527736742d60fabad0ac796db134258 | 8403 / 7a78ee8d633696866379225d5a301c40632060a6f7a04e5f1b9d4d4373afe8d5 |
| 4 | 35926 / 1ae94b74d029186b2ded568b317c3f259dd6bd1f14d5b579b79d52c01b3150ad | 8947 / c81fedf1a2641e18e6dfb317ee532997cc85cde6383a60b886a4ee334fa213a8 |
| 5 | 38777 / f4e065218707876b53f6e1124f8be9547b7dea6c9dbbc88e234f41f4c7e7c80d | 9045 / c42974249f4fe50fca7c618b884aac2b2a9768fa7ab7939d30ff31ce3c4b0ecd |

Every per-direction certificate also retains the original global pole-ideal node IDs, selected whole-fibre references, all complete relation references, and its exact $A/B$ source graph.

The completed $B$-values and $y_jB$-values at every selected whole fibre are retained as full $272\times\dim\mathcal R_j$ arrays. These are the exact existing data required by [R896](R896-original-two-denominator-low-weight-residual-RR-kernels.md); the next consumer need not repeat the initial Schur calculation, denominator inversion, or those evaluations.

## 6. Final manifest and necessary active transport

| Item | Bytes | SHA256 |
|---|---:|---|
| Final complete certificate | 18395 | ad135ab7a624beaad0e1fba76230a63cfe478b3aa667b6b33624f763269cf728 |
| Complete mathematical-stage manifest | 40119 | d0b4a008aff2f81f1a668b0b2a1e8e15e29294d6699eab75cc3ee2ead1a01c23 |
| Full output manifest, 643 entries | 98261 | 58a66985fc3bcb663ab5e7c4238546d8d33a876a3fd69663e9f4f817fb8eb8b4 |
| Original source audit | 7683 | 8778c9131e6f95212d27fa27e439311f5e83b5568463baa63e998db88c93486a |
| Retained 131-source carrier | 146082255 | 49ef05b979288838096e7426a5ec37938daaae108b4169682ed45cbee7de1dba |
| Original source inventory | 75893 | 0988844a0b285f2ad5ecf0a4f8f652c8afe0de76a97d3893c51b9b7d381438d2 |

The actual source artifact is 14224626902, named
serre-global-R893-five-sum-Hom-initial-RR-43861874528-1,
576747513 bytes, advertised digest
$$
\texttt{cc7cc8e58754205f1472929b4a733e20bf594732aae869a19004d9c32fb01893}.
$$
Its recorded expiry is 2026-11-17 12:03:18 UTC.

The necessary source-only intake is [run 43864802081](https://github.com/Rogerhu12/math-research-public/actions/runs/43864802081), job 133290576721, source
9d3c15161c03fa207a06fcf99ba95093198b8dd7. It follows the actual final certificate to the five initial certificates, their $A/B$ bases, selected fibres, unit minors, original $B/yB$ values, relation certificates, and required Krylov nodes. It does not fetch the large retained source carrier, Schur row blocks, or normal-multiplier matrices.

It preserves 392 necessary original members plus the manifest and its reference in
R893-five-initial-RR-complete-intake-selected-original-sources.tar.gz,
150809978 bytes / SHA256
c599a9335b1fc8a2a519d066d8d0cfec471fd7ee4cf2ce241517f82638888397.

The intake artifact is 14224774305, 151090834 bytes / advertised SHA256
fed29b488d1c87ef68d0b07ff21cbad4f833722f81a50ab729fbc6b92e7fbf6f,
expiring 2026-11-17 12:17:51 UTC. The transfer actually used 206 HTTP ranges and 256511716 bytes. Each selected member was checked against the original manifest. This is not a claim to have downloaded or rehashed all 576747513 source-artifact bytes.

## 7. Exact continuation boundary

This completed result supplies the actual complete spaces needed by R896. It does not yet certify a marked $A(P_0)$ unit, two $B$-sections with exactly the original common zero divisor, the residual low-weight kernel, padding, or a new 418-dimensional bounded representative. Those require their own actual unit minors and full relations.

The true five $L_j$, the 128/144-dimensional line-bundle spaces, their original descent and marked frames, the non-$p$ data, connection, period, and height remain separate. The source artifact's complete flag applies exactly to the five initial RR spaces described here.

This registration uses the original completed mathematical run and source-only reading. It introduces no new arithmetic outside the public repository's Actions and no independent audit computation.
