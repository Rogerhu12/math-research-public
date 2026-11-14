# Thirteen original query grids with complete local condensation

Date: 2026-11-14. This independently named continuation adds only original collocation midpoint482 to the complete request45 warm algorithm. It preserves the original finite BVP, scalar profile, boundary equations, field representation, nonlinear tolerances, and native tail. Optimizer progress is not a full nonlinear BVP, a new native height solution, or a closed surface.

## 1. Actual reason and parent

See [the complete actual45 note](2026-11-14-actual-request45-condensed-QP-and-midpoint482-limit.md). During request45, the original twelve modeled grids were positive at the three nearest rejected trial lengths $1/4$, $1/8$, and $1/16$, while original collocation midpoint482 failed the actual domain test. At $1/16$, its saved minimum of $\beta^2$ was `-0.08309044083909534`, at physical angle index1014. The accepted step was $1/32$.

Those were trials from the actual42 parent in request45's model. They are not claimed to have been reevaluated at the newly saved request45 warm. This new entry starts from that saved warm and constructs a fresh model. No extra left-RMS query482 is introduced.

The first parent is hard locked to:

- Run `43627827085`, source `3689913753612b02021e439082eaf1c166091183`.
- `condensed-warm/warm-001.json.gz`: `8ce98e5b325eae8188f8b4c707d1abfaa109e50a790c9abe5850ef1a52d08b75`.
- `condensed-warm/driver-status.json`: `70be19b675c9f558cddbfa9532777a119a7bbe0629f505368e1588842aade30d`.
- Parent schema: `exact-constraint-twelve-query-condensed-complete-H-warm-v1`.

The new schema is `exact-constraint-thirteen-query-condensed-complete-H-warm-v1`. Later use of the same frozen entry can resume its own completed warm/status pair. The original complete producer validator checks the source ledger, original prepared/accepted/anchor/config identities, scalar definition, constant global parameters, field representation, mesh, status-to-warm identity and unaccepted flags. The entire original parent producer subtree is preserved.

## 2. Frozen sources

| New file | Bytes | SHA256 |
|---|---:|---|
| `computations/geometry_20261114_thirteen_query_domain_operator.py` | 28524 | `d674a64e11cfac1f57f0c24166546a55045847633935dddb8ef53df4024d3cff` |
| `computations/geometry_20261114_thirteen_query_condensed_warm.py` | 38686 | `7785f4eb905da4c3e80ba988c79fa8a34b0a27017e6b8abc99764d8105eccc7c` |
| `computations/geometry_20261114_thirteen_query_condensed_response.py` | 2613 | `2cbd850a3a810f4296920e13629e86a9ca11545d7dd002d1a0d569e9e6d2319a` |

The old numerical sources remain byte for byte unchanged, including:

- Request45 warm: `5d398d3d702e0fd93af3777504fc1d4e918110c7e5f0683601eac5d21c49914a`.
- Local QP: `ea93b88df867bd2d365bb783963ad4455d652057252384c2eecba899433e2173`.
- R270 condensation: `84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b`.
- Complete regularized QR: `596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722`.
- Twelve-query domain: `6a428d2f8412659cbd318321aa992c3b4565ff41177131a9cc9d268c6fbb7b1f`.
- Fixed C-support helper: `0c5573ea26d2c69c1a22595e00de9e41b38981793b88f4f52086d7713d111f68`.

## 3. Typed queries and complete coordinates

| Query indices | Kind | Intervals | Fraction |
|---|---|---|---|
| 0 through8 | Original left RMS | 470,471,472,473,475,477,479,480,481 | `0.17267316464601146` |
| 9 through12 | Original collocation midpoint | 473,475,477,482 | `0.5` |

Every block has2048 original physical angle rows, for26624 actual finite constraints. The unique capture intervals are `(470,471,472,473,475,477,479,480,481,482)`. The same original `CompleteLinearization` supplies14 physical nodes470 through483. Endpoint483 is in the original chunk supplying interval482; no second complete Jacobian is requested.

The full unknown count remains236036. Complete B local support becomes14 nodes times338 physical coordinates plus3 global scalar parameters, hence4735. Free core, all outside physical nodes, and all original controls remain in complete A.

A read-only interval view of the complete capture compiles only the nine retained left-RMS blocks. The view neither changes captured arrays nor calls a Jacobian. Immediately after that component is built, the full capture and all14 endpoint indices are restored for the complete operator, its complex-chain check and export. This prevents an accidental tenth RMS block merely because midpoint482 needs its endpoints.

Kind, interval, fraction, station and original base identity are explicit per block. Equal interval IDs do not collapse an RMS and a midpoint into one query.

## 4. Original midpoint chain

The new base is the exact returned `state.middle[482]` and `problem.mid[482]`, not a new RMS or spline replacement. For interval length $h$,

$$
Y_m=\frac{Y_L+Y_R}{2}-\frac h8(f_R-f_L),\qquad
\delta Y_m=\frac{\delta Y_L+\delta Y_R}{2}-\frac h8(\delta f_R-\delta f_L).
$$

Let $J_L,J_R,P_L,P_R$ be the captured original physical and scalar RHS derivatives and $\Gamma,\Pi$ the original all-angle margin derivatives. Before exact-chart scaling,

$$
B_L=\frac12\Gamma+\frac h8\Gamma J_L,\quad
B_R=\frac12\Gamma-\frac h8\Gamma J_R,\quad
B_p=\frac h8(\Gamma P_L-\Gamma P_R)+\Pi.
$$

Rows act on $z=S\delta q$, so assembled coefficient columns divide by $S$ once. Both nodal scalar chains and direct $\Pi$ remain. The inherited exact inlet injection is retained wherever applicable. Reconstruction of the algebraic base is diagnostic only. The independent complex check uses the original complete augmented RHS at the14 selected endpoints and the actual typed query formula; it does not rebuild a full Jacobian.

## 5. Fixed C comparison and complete H candidate

The C candidate still corrects only nodes471 through482 and global p, dimension4059. With that support denoted by $S_C$, its offsets remain

$$
\widetilde c=c+B_{\overline S_C}z_{0,\overline S_C}.
$$

The complete outside term now includes nodes470 and483. It is neither omitted nor set to zero. The unchanged helper forms it from complete B and the actual raw direction. Negative offsets and a restricted infeasible set do not become scientific rejection gates: the original full-vector radial and feasible-ray safeguards remain.

The full-H alternative uses [R270](../results/R270-exact-local-support-damped-QP-condensation.md) with the same actual fixed model

$$
f(z)=\frac12\|b+Az\|^2+\frac{\lambda^2}{2}\|z\|^2,
\qquad A=W_rJS^{-1},\quad\lambda=270,\quad g=A^Tb.
$$

Original full QR and affine elimination retain the true linear term and every pure-global row. All outside variables, including free core, have their conditional optimal response. The dynamic frozen library consumes4735 local coordinates; it is not changed. The local QP remains the original bounded working-row algorithm.

Actual full recovery is reread through original A, AT, B and BT. Full-vector radial/segment repair may subsequently change outside coordinates too. The final direction is not claimed to preserve exactly the external raw direction or to be an exact floating-point conditional optimum.

C and H are compared using the same actual full $f$ in this new model. Original nonlinear trials still determine real progress. Float KKT/R267 values are diagnostics, not validated enclosures or new BVP acceptance gates. Cross-model merits with freshly frozen weights are not subtracted.

## 6. Command-line contract

Use the unchanged original accepted96 source, prepared699 field, true completed zero-H T112 J and config:

```sh
python computations/geometry_20261114_thirteen_query_condensed_warm.py \
  --accepted "$ACCEPTED96" --prepared "$PREPARED699" \
  --tail-anchor "$ZERO112" --tail-config "$CONFIG112" \
  --resume "$PARENT45/warm-001.json.gz" \
  --expected-resume-sha 8ce98e5b325eae8188f8b4c707d1abfaa109e50a790c9abe5850ef1a52d08b75 \
  --parent-status "$PARENT45/driver-status.json" \
  --expected-parent-status-sha 70be19b675c9f558cddbfa9532777a119a7bbe0629f505368e1588842aade30d \
  --out "$OUT/thirteen-condensed-warm" \
  --iterations 1 --damping 270 --lsmr-iterations 200 \
  --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200 --angles 4096 --jac-workers 2 \
  --condensed-budget-seconds 600 \
  --condensed-trial-reserve-seconds 90 \
  --condensed-recovery-reserve-seconds 30 \
  --condensed-max-working 256 --condensed-dual-sweeps 200 \
  --condensed-store-root
```

Read the actual `driver-status.json` filename and SHA after a completed warm. Do not assume an output exists after a failed step. Then run:

```sh
python computations/geometry_20261114_thirteen_query_condensed_response.py \
  --accepted "$ACCEPTED96" --prepared "$ACTUAL_NEW_WARM" \
  --tail-anchor "$ZERO112" --tail-config "$CONFIG112" \
  --out "$OUT/physical-response" --angles 4096
```

The FD entry actually recomputes the original Rphi directions, steps and Richardson checks, using the new warm SHA and full producer. The threshold stays `5e-5`; an old pass is not relabelled. The native zero-H J remains an explicitly affine reference. Any later full nonlinear continuation must truly solve the new H and retain fresh final audit.

Budget parameters are optimization limits, not equation changes or tolerance relaxations.

## 7. Output and verification scope

Outputs retain the complete actual warm states/RHS/mesh/scalar, original trial and midpoint-observer records, all B/Gamma/Pi parts, full current ledger and original parent subtree, C/H comparison, local QP history/arrays, recovery report and fresh complete-model posterior. Large `condensed-root/` and `condensed-arrays/` remain artifact-only with identities, not a Git-size scientific gate.

`accepted_warm_steps=1` and `optimization_progress=true` describe optimization only. `success=false` and `new_coupled_finite_acceptance=false` remain. A same-schema restart still requires the completed exact warm/status pair; an uncompleted direction or prepared field is not a parent.

Only source/AST/hash checks preceded dispatch. `project`, `choose`, `CapturedLinearization`, complete-model `evidence`, scalar serialization and compact metadata have identical ASTs to request45. The new independent binding changes the explicit parent, typed grid set, dynamic local support and current identity. Frozen original file hashes were checked unchanged. All actual matrices, optimization, original real-domain trials and new FD run exclusively in this public repository's Actions.
