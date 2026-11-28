# Prefix target retained through b and 36 free outer radius coefficients: first actual step

**Numerical evidence.**

Initialize from the original fixed-g step 14 field with every stored alpha zero. Only the last 36 alpha directions are admissible. They are the inherited clamped b..S functions from R248: h, h′, h″ vanish at b and h is identically zero left of b. Thus the original scalar target is unchanged on the entire prefix. All 12,789 Cartesian coefficients, including the prefix ones, remain free. The new provisional target is allowed to change outside the prefix. Its own accept count begins at zero.
The production baseline reproduced the complete original-g14 objective and groups. All 4,291,840 physical rows and the H² increment damping are unchanged. The tangent now has 12,825 free components. J/JT defect 6.99854e-15; raw centered FD at epsilons 1e-6, 1e-7, 1e-8, 1e-9, 1e-10 gave .0712033, .0246022, .00884509, .00381977, 1.15178e-7. The last satisfies the original 2e-5 tolerance. Independent full physical normal relative residual 1.31619e-13. Rejected length 1, accepted 0.5, own 1/1. All first 51 alpha remained zero; maximum absolute active coefficient .0297694553.
G10 R14² .02692066519 → .02132616187, metric .2184943351 → .1972369813, curvature 48.66463 → 45.09983, held .72373650 → .71013752. The curvature and metric guides remain unmet; the existing .65 held guide remains satisfied on these samples.
G11 independent metric 0.191818077916, curvature 43.6587266181, held 0.710288632195. Actual target |K| sample maxima 8.939344073 on G10 and 9.080648927 on G11. These are measured target values, distinct from the position curvature and from reach. No whole-closed or all-time result follows.

## Reproduction

Set S to the topic scripts directory and W to the run directory containing the source masters and scientific scripts. Use the G10/G11 complete-source and continuation recipes associated with the named input states. These are the returned inner commands.

```sh
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u $W/2ecf-polar-restricted-radius-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --warm-state $W/polar-G10s-fast-step14-step01-state.json --prefix $W/polar-restricted-radius-step01 --steps 1 --initial-damping 0.0009481481481481482
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-restricted-radius-step01-step01-state.json --output $W/polar-restricted-radius-step01-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-restricted-radius-step01-step01-state.json --output $W/polar-restricted-radius-step01-target.json
```

## Scientific SHA-256

- `2ecf-polar-restricted-radius-design-solve.py`  `d08987f68fa7b29a360946b001588b2584ec1e96174d95e4af47964a71aa729e`.
- `polar-restricted-radius-step01-initial.json`  `5fd478775abf797d980215902e806486e77d9097bec757ceab8b91a9ad6ecd8b`.
- `polar-restricted-radius-step01-actual-derivative-check.json`  `e3a69cc8782a66d724b7804807ba0d0412c08151a3f34dae3da8831d54ca771c`.
- `polar-restricted-radius-step01-step01-state.json`  `388835346195a0d4bd9b3cdc6ab445460760e92c9d2323d95293eb9c02602473`.
- `polar-restricted-radius-step01-G11.json`  `6d92f830427223a3575c3aa356cfcbf4d847520e35bbf0974968ccfa307ea6ca`.
- `polar-restricted-radius-step01-target.json`  `768e0093d7292b69caa046f29c4f3d8c2b2cf949d5f1e86c07f4962c30840965`.
