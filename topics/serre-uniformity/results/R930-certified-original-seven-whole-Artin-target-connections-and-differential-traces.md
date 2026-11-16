# R930. Certified original seven whole-Artin target connections and differential traces

## 1. The completed statement and its exact scope

The public Actions computation [43921420577](https://github.com/Rogerhu12/math-research-public/actions/runs/43921420577), compute job 133489560210, has completed all seven original target connection values and differential traces. Its source commit is 280f1840a717c80665133b0ddab8a55a02af7d4e. The mathematical core returned exit code 0, complete true, error null, and 10.262631071999998 seconds. The complete output contains 277 mathematical stages and one explicitly separate current checkpoint.

The seven labels are
$$
D_1,D_2,D_3,D_4,D_5,X,D_N.
\tag{930.1}
$$
For each of these original divisors, the computation certifies the following at the original auxiliary place and in the complete correspondence algebra:

1. The actual determinant denominator $d_D(U)$ is a unit in the entire algebra $E$.
2. The full $2176$-coordinate target value $B_D(U,V)$ is the value of the original section-1 connection coefficient.
3. The full $272$-coordinate vector of
   $\operatorname{Tr}_{E/A_0}(B_DJ)$ agrees both with the trace of its rank-eight multiplication matrix and with the original R922 quotient-transport identity.
4. The original connection, gauge, principal parts, source and target frames, and canonical dual-7 transport remain attached to the result.

The exact source-bound characteristic-zero expressions are retained as an executable mathematical DAG. The newly expanded coordinate tables are at $\ell=1000000753$. No characteristic-zero connection coordinates, five Picard $\sigma/c_Y$ combination, endpoint calibration, non-$p$ term, period, or height is asserted by this result.

This is the actual execution of the formulas in [R922](R922-original-bounded-connection-numerators-and-whole-Hecke-evaluation.md), using the completed [R905 connections](R905-certified-original-seven-trace-dual-connections-and-five-Picard-inputs.md), R926 bounded numerators, R928 target transport, and R919 differential-trace row. The [R930 execution method](../notes/R930-original-seven-whole-Artin-connection-traces-method.md) fixes the source and stage conventions used below.

## 2. Original objects and place

For each label, let $\alpha_D$ be the completed R905 connection on $\mathcal O(H-D)$ in its original rational section $1$. Its full logarithmic principal parts are $H-D$, with the original 543-coordinate gauge and all 544 principal-part equations preserved. Write
$$
\alpha_D=B_D\nu,\qquad
B_D=\frac{y_D^tR\beta}{d_D}.
\tag{930.2}
$$
The matrix $R=gG^{-1}$ is the shared original polynomial trace-dual multiplier certified by R922. The numerator $y_D$ and denominator
$$
d_D(z)=\frac{\det F_D(z)}{\det F_D(a_D)}
\tag{930.3}
$$
are exactly the completed R926 expressions. Their stored coefficient slots, including leading zero slots, remain unchanged. R926 supplies the complete $277\cdot272$ polynomial equations defining each numerator, with the same original connection and gauge.

The place is
$$
\ell=1000000753,\quad
\zeta=549966761,\quad s=99932770,\quad B=3197390.
\tag{930.4}
$$
The source fibre is the original $z_s=0$ fibre. Its complete algebra and the full cyclic-seven correspondence algebra are
$$
A_0=\mathbf F_\ell[X]/(\chi_0),\qquad
E=A_0[U]/(P/a_8).
\tag{930.5}
$$
The dimensions are $\dim_{\mathbf F_\ell}A_0=272$, $\operatorname{rank}_{A_0}E=8$, and $\dim_{\mathbf F_\ell}E=2176$. All original factors, multiplicities, and nilpotent directions are retained.

The target coordinate is the original quotient
$$
V=\frac{K(U)}{P_U(U)}.
\tag{930.6}
$$
Here $K$ denotes the eight original numerator coefficients, not the target coordinate itself. The old $P_U^{-1}$ and the complete quotient derivative were consumed unchanged from their completed sources. No replacement $V=K$ or derivative omitting the denominator is used.

The selected input carrier contains 85 original files: R922 has 8, R926 has 26, R928 has 12, R905 has 5, R885 has 27, and R919 has 7. Their original source identities and selected byte specifications are bound in the new configuration. The R885 and R919 bytes came through the already completed R928 input carrier, retaining their original identities.

## 3. Seven actual whole-algebra units

For every $D$ in (930.1), the core evaluated $d_D(U)$ in all of $E$ and obtained a complete unit certificate. Each certificate records the rank-eight multiplication matrix, its division-free characteristic polynomial, the full norm Bézout identity in the original $A_0$, the inverse, and the multiplication back to $1$ in all $2176$ scalar coordinates.

Thus the actual result is
$$
d_D(U)\in E^\times
\quad
\text{for all seven original labels}.
\tag{930.7}
$$
The completed source $F_D(a_D)$ being invertible was not treated as evidence for (930.7). The target units were checked separately in this computation. No factor was removed, no squarefree quotient substituted, and no geometric point selection used to obtain a successful inverse.

All seven selected unit stages have complete true, whole_E_unit true, source_F0_unit_not_used_as_target_unit true, and factor_removal_or_cancellation_claimed false. Their filenames are R930-label-whole-target-denominator-unit.json.gz, with label replaced by the first column below.

| Label | Bytes | SHA-256 |
|---|---:|---|
| D1 | 146,575 | ce4433f668d62c133266e8ee993fb8fd672c541c3307b7419697a9224438d063 |
| D2 | 146,366 | a5be9ec99cc2bbbedd297c0dfb8c424e6c97e3e4182ed5e292b1d92932e38365 |
| D3 | 146,434 | cc68fa4dcfa829843556f45056ececbd0480cacfc2caf8b79acc038118b5abfa |
| D4 | 146,549 | f9d6072d9b50ee05d7ab083006d041c91ee838412edd0caa0f1a73fe48b09758 |
| D5 | 146,451 | 7a91fbbac9fd8b574253e7dbc7ae0871f18750d4b16514e1d012e3db96d6556c |
| X | 146,565 | 88b44d8303382024da2390913b22a56d99fba3040335ca4da5a1a36d12280363 |
| DN | 146,121 | 609fd33ea3b445f823a05b3f286ac98ca4c413832fe402f3460c96f670954af4 |

The final nonunit_target_denominators object is empty. This closes the target denominator question for these seven actual source-bound expressions at this whole fibre.

## 4. Complete target numerator and quotient identities

Put $\epsilon=(0,1^{144},2^{127})$. The completed inputs have
$$
\deg(y_D)_i\le271+\epsilon_i,\qquad
\deg R_{ij}\le3-\epsilon_i-\epsilon_j.
$$
Consequently, for $r_D^t=y_D^tR$,
$$
\deg(r_D)_j\le274-\epsilon_j.
\tag{930.8}
$$
The new core performed the finite matrix contraction before $U$-Horner evaluation. It retained all 277 coefficient rows, checked all weighted bounds, and verified the entire degree-275 and degree-276 tails to be zero. Each label's actual contraction index reports all277_times272_product_coordinates_and_weights_verified and zero_tail_degrees275_and276_certified as true.

The old complete table of all $272$ target normal coordinates was then used to compute
$$
N_D(U,V)=\sum_j(r_D)_j(U)\beta_j(U,V)
\tag{930.9}
$$
in the full $E$. The saved coefficient blocks and descending Horner chain preserve the entire target algebra, rather than selecting values at reduced points. Combining (930.7) with (930.9), the actual target connection coefficient is
$$
B_D(U,V)=N_D(U,V)d_D(U)^{-1}.
\tag{930.10}
$$
Every label certifies all $2176$ coordinates of
$$
d_D(U)B_D(U,V)=N_D(U,V).
\tag{930.11}
$$
The complete certificates retain both sides, the target numerator, the target connection coefficient, and their original source references.

This step did not recompute the old $R,G,y_D,d_D$, old target normal coordinates, initial Schur systems, Gamma operators, or any of their completed inverses.

## 5. The original differential ratio and the two full trace checks

R928 supplies the already completed target/source differential ratio $J$. In the original notation,
$$
Jg_t=\dot U,\qquad Jh_t=\dot V.
\tag{930.12}
$$
The selected actual R928 parameter, read from its completed transport rather than inferred from the proposed schedule, is
$$
t=0.
\tag{930.13}
$$
The original $\ell_t=g_t+t h_t$ inverse is retained. R930 neither computes $J^{-1}$ nor asserts that $J$ is a unit.

The direct target differential trace is
$$
\operatorname{Tr}_{\pi_s}(\pi_t^*\alpha_D)
=
\operatorname{Tr}_{E/A_0}\!\left(B_D(U,V)J\right)\nu_s.
\tag{930.14}
$$
The trace in (930.14) is the ordinary, unnormalized trace of the full rank-eight multiplication matrix over $A_0$. It is not a trace to $\mathbf F_\ell$ and has no inserted factor $1/8$ or $1/7$.

For reusable evaluation, the core completed the ordinary trace row
$$
\mathcal T(e)=a_8^{-1}[U^7]\bigl(eP_U\bmod(P/a_8)\bigr).
\tag{930.15}
$$
It verified all eight basis values against the corresponding full multiplication diagonals, keeping all $272$ source coordinates. The original $a_8$ and $P_U$ inverses were read, not recomputed. This identity holds in the complete finite algebra; it does not require the chosen fibre to be reduced.

For every label the saved rank-eight multiplication diagonal of $B_DJ$ has been summed and compared with its ordinary-row evaluation, giving all $272$ coordinate equalities in (930.14). In addition, the actual result was compared with the completed R919 differential row $\mathcal L$ through the original R922 formula
$$
\mathcal L\!\left(
 B_D\ell_t^{-1}(1+tP_U^{-1}\mathcal H_K)
\right)
+
t\mathcal T\!\left(
 B_D\ell_t^{-1}P_U^{-1}\Delta_K
\right).
\tag{930.16}
$$
The definitions of $\Delta_K,\mathcal H_K$ and $\dot V$ are the full quotient-rule definitions of R922 and R928. All their inputs were retained from those completed computations. Formula (930.16) is recorded with its complete source even though the actual choice (930.13) makes its second summand zero.

Every one of the seven complete certificates reports the following three flags as true:

- all2176_target_connection_quotient_coordinates_verified;
- all272_trace_coordinates_verified_by_full_rank8_multiplication;
- all272_R922_quotient_transport_trace_coordinates_verified.

The source and target nilpotent directions and multiplicities remain present in these equalities. These flags certify complete algebra identities, not sampled agreement.

## 6. Exact source expressions and frame orientation

The output DAG retains the original R926 characteristic-zero unit-solve expression for each connection, the exact R922 trace-dual expression, and the original R928 transport. Its formula is (930.2) followed by target pullback and (930.14). Its exact_original_characteristic_zero_expressions_defined flag is true; its characteristic_zero_coordinates_expanded and finite_fibre_values_substituted_for_global_functions flags are false.

The direction of the computed numerical table is exactly
$$
\operatorname{Tr}_{\pi_s}\pi_t^*\alpha_D.
\tag{930.17}
$$
The canonical dual-7 identification with the frozen Hecke direction retains both determinant frames, scalar $7$, the diamond action, the original minus-3 descent, and the original $\kappa,\nu$ data. Endomorphism self-adjointness is not substituted for that rigidified identification. No endpoint determinant or numerical $\kappa,\nu$ calibration has been evaluated here.

The original geometric semilinear $c_Y$ is retained as a sourced operation, not replaced by coefficient conjugation. It has not yet been applied to these seven coordinate tables.

In particular, the $D_N$ table is the trace of $\alpha_{D_N}$ itself. It is not the trace of $\alpha_{D_N}-d\log Q_N$. The original construction must first make that principal correction and only then form its genuine sevenfold average. The five $Q_j$ likewise retain the already specified negative $\chi$-powers. No principal correction, Galois average, or geometric $c_Y$ average is included in the success statement of this execution.

## 7. Actual run, source, and principal output identities

The actual configuration SHA is
c3ab2ae711bb7cf5b241e85b18d20ed14556cc278f98f42be34ce01109237910.

| Item | Actual identity |
|---|---|
| Run / compute job | 43921420577 / 133489560210 |
| Source commit | 280f1840a717c80665133b0ddab8a55a02af7d4e |
| Core | scripts/R930_original_seven_whole_Artin_connection_traces.py |
| Core bytes / SHA-256 | 45,219 / c35f63bec49f3b795c040c64d4900d955af1eed5cf326e3640226880401a0f4e |
| Standard-library wrapper bytes / SHA-256 | 66,817 / 2fad50f49c2e5670d54980da5db75b137eef53d5a265e7bc3895050edd007ec0 |
| Unchanged whole-Artin helper SHA-256 | e47cd50d254700b98446866297d79694c100f1435c46f3b4f42e3835763f897d |
| Execution method bytes / SHA-256 | 10,561 / b204e207052dfa231172a0903de8318f59efcdfff06bd64f4e008f074187c855 |
| Mathematical exit / complete / error | 0 / true / null |
| Mathematical seconds | 10.262631071999998 |
| Complete mathematical stages / current checkpoints | 277 / 1 |
| Actual completed connections | 7 |
| Actual unresolved target denominator set | Empty |

The actual platform artifact is 14254752421, named serre-global-R930-seven-whole-Artin-connection-traces-43921420577-1. It has 42,518,654 bytes and platform ZIP SHA-256
70740e910313d6be510a8d1bab302388f67057d7a56f4ad613f6af1001179f2d,
with expiry 2026-11-17T17:44:51Z.

The final certificate is p41-original-seven-whole-Artin-connection-traces-certificate.json, 20,805 bytes, SHA-256
13793936ee94a232a8fd7c952ee11b295fb4fc6e7bd6d532835248f416714363.

The full output manifest contains 288 entries, has 41,434 bytes, and SHA-256
1261b9cf43e691a00e05ac04f7cf48e83e393a58027fa8983dcaa70bc363ef92.
Its reference has 189 bytes and SHA-256
25bfee927e777c1b327c425baadc60fb4141242dda48830b40f28bb7534472f8.

The content-named complete mathematical stage manifest is
R930-stage-manifest-5e0697b0e211aca5335b1e3a12b1e52dbb5b41f371cbef8f1e39c44881c4b5ea.json.gz,
21,729 bytes, SHA-256
505cb1ca4f83df33d925cc8abc59f723932b5216b1d4eb4e9daca2a011ca223e.

The seven complete certificate filenames are R930-label-complete-whole-target-connection-and-trace.json.gz.

| Label | Bytes | SHA-256 |
|---|---:|---|
| D1 | 91,407 | 8dd5e2215c38b85714156238cbf02966d4efcde0f520eb23ab80dc06677f1fa3 |
| D2 | 91,266 | ab882d53c0199d049ed954adcc2693b6675dfd274774fe588db5272a064bf715 |
| D3 | 91,197 | a019d106a3e6b697d52f96b97e158fe6f5c255cb9a3efe34aeb7354e86618e3e |
| D4 | 91,272 | 29ea36ebe64d7eddbd46747d7f6c4381cd643774fc336bb4ec1f49d82abcaf25 |
| D5 | 91,354 | 26c2f22a8f16ab3fcf88362b90e65036cd42c9ee12268518ccefb76b60494661 |
| X | 91,270 | 9db6f3bda41514baf652d39879f3c28b59e02ca2c25f0b858e674230251e775d |
| DN | 91,235 | 86e6e0555ac12448be4675b37a2017d032a63f27a2e1afaaafec305b87e2378e |

The shared ordinary trace row has 66,881 bytes and SHA-256
c0aeaba98020289729faf002ee4f6ad1da8ecace29abec5412c2283729405f2c.
The completed trace-transport factors have 29,885 bytes and SHA-256
d7a7a3e6ef72c6ca971c2c396410bba1f0d427fac343f16d4278d79428e1de97.
The exact seven-connection DAG has 9,543 bytes and SHA-256
59f0fec7ca125ad00985b0e60e02b9b2b60f4c72ffda169e3e6cd9a4c5cd8685.

The new minimal original-input carrier has 13,135,687 bytes and SHA-256
ef1b025f47d85c00fce9497415f90df9e3097b2cd792da7a93163b4094e52483.
Its source inventory has 45,403 bytes and SHA-256
6570470c76c446c23d82eb15a7b526e389822afadbe9e7b6c2acf66049f522bc.
These are source-preserving transport records; copying them is not new mathematics.

## 8. Independent pure IO reading and the remaining boundary

The successful selected-output reader [43922638810](https://github.com/Rogerhu12/math-research-public/actions/runs/43922638810), job 133493726793, fetched the original manifest and reference plus 30 selected files. It read all seven complete certificates, all seven whole-target unit stages, all seven contraction indices, the shared trace stages, the exact DAG, source audit, final and necessary metadata. Its selected-members-verified-against-original-manifest flag is true; new_mathematics_executed is false.

The selected transport tar has 1,902,101 bytes and SHA-256
148fe1e08ea2b9f490e9665b642f10a539689d2e81a76791b303216ddaf082a6.
The reader used HTTP ranges and did not claim to rehash every byte of the 42.5 MB original archive. The platform artifact digest and the individual original member SHA checks are recorded separately. No 13 MB original-input carrier was fetched in this small output read.

The original FINAL and the selected raw scalar/schema summaries agree on all seven units, all seven complete quotient and trace identities, the actual $t=0$, the original principal parts $H-D$, rational section $1$, and preserved gauges. All source-bound mathematical execution occurred in the public Actions run above.

The precise new output is therefore the seven full target connection values and seven original differential traces in the complete $E/A_0$, together with their exact sourced expression DAG. The following claims remain false in the actual FINAL: $J$ inversion or unit assertion; characteristic-zero expanded connection coordinates; five Picard $\sigma/c_Y$ or principal-function combinations; original Hecke projector or endpoint calibration; non-$p$ terms, Poincare periods, and heights. Completing those objects requires their own original action and marked-principal inputs, not a relabeling of the seven tables certified here.
