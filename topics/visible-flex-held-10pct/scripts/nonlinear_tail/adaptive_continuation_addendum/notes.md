# Adaptive continuation and fixed-metric refinement

**Status: numerical evidence.** Every accepted row below uses an actual nonlinear DN and the original acceptance residuals. The design rows retain one physical tail metric but refit the prefix parameter delta; they are not fixed-whole-metric refinement. The last row freezes the q=.004 prefix metric and the complete physical tail, then raises Fourier, angular and radial resolution.

| Case | Actual core q | delta | Prefix metric | Tail full Darboux | Tail actual metric | min A | Tail formal K |
|---|---:|---:|---:|---:|---:|---:|---:|
| design q=.002 | 0.002 | 0.1718183369254722 | 1.2142e-09 | 5.0528e-11 | 2.6202e-14 | 0.9370077 | 9.9652767 |
| design q=.004 | 0.004 | 0.1718182706205134 | 2.4373e-09 | 1.9399e-08 | 9.9829e-12 | 0.8527189 | 10.354007 |
| design q=.006, tol3e-6 | 0.006 | 0.1718181596738146 | 3.6693e-09 | 4.9888e-07 | 2.5659e-10 | 0.7536373 | 11.192072 |
| design q=.008, tol3e-6 | 0.008 | 0.1718180049569564 | 4.9105e-09 | 4.6866e-06 | 2.3795e-09 | 0.6554982 | 12.319225 |
| fixed q004 metric, M12 | 0.0040116065091 | 0.1718182706205134 | 2.6151e-10 | 2.5837e-11 | 7.994e-15 | 0.8521752 | 10.359446 |

The q=.006 M8 run with collocation tolerance 1e-6 exhausted 4,000 allowed nodes with a residual plateau 2.14e-6. It remains recorded as unsuccessful. A separate explicitly labeled tolerance-3e-6 design run gave accepted q=.006 and .008 states; no tail guard was weakened. The original nonlinear boundary residual is normalized by bcweights=.02: its 1e-7 acceptance gate corresponds to the physical 2e-9 gate.

For the frozen q=.004 metric, M8/N128/steps32 became M12/N256/steps64 and the prefix collocation tolerance became 3e-7. The actual core coefficient shifted to .0040116065091 while the physical profile delta remained exactly .17181827062051344. This is legitimate fixed-parameter refinement with a measured geometric coefficient, not a silent retuning of the metric. Two levels do not prove convergence. The complete height second-jet seam of the refined row is at most 1.35e-10.

The q=.008 reflected-prefix sample has max norm 1.50146364476, hence centered diameter about 3.00292728952; together with the reported tail curvature 12.31922519 its normalized curvature budget is unfavorable. The full Darboux defect also grows to 4.69e-6. These finite values do not establish any nonexistence claim, but they prevent treating the small metric residual alone as closure or thickness evidence. No further adaptive physical design was started after this finite continuation.

Exact height-to-Cartesian seam uniqueness is already proved in this topic’s R12 (`results/R12-height-metric-jets-determine-cartesian-seam.md`). The previous q=.002 run added the actual 512-angle Cartesian comparison and finite-tail geometric audit. An independent Gauss–Weingarten derivation is only a cross-check of R12.

Exact parameters, scalar outputs and hashes of every prefix/tail pair are in `record.json`. Recomputable states and arrays remain in scratch. Source and the complete seed recovery command are in `../adaptive_coupled_seed_deliverable`; the continuation driver is `continue_smallcut_coupled.py`.

Reproduce using the already restored q=.002 seed package and its generated run directory:

```bash
OPENBLAS_NUM_THREADS=1 python reproduce_addendum.py \
  --seed-package ../adaptive_coupled_seed_deliverable \
  --seed-run PRIOR_Q002_RUN \
  --source-topic RECOVERY/bundle/topics/visible-flexible-closed-surface \
  --prefix-recovery RECOVERY \
  --output NEW_SCRATCH_ADDENDUM_RUN
```

The physical metric descriptor hash is SHA-256 of canonical JSON (`sort_keys=True`, compact separators) containing the prefix profile, physical tail parameters and factory hash; both q004 levels have hash `2f0673b81719758b1e65cb5e462f8b1e64e26e049ac41553de60fee0c1c4f1a8`.
