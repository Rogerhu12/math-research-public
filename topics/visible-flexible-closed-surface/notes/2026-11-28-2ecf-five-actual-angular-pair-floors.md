# Metric mismatch on five actual fields persists under arbitrary angularly invariant target redesign

**Numerical evidence.**

Every one of the 668 independent G11 rings at 256 shifted angles was scanned. All 43,778,048 ordered same-ring angle pairs per field were compared by their 2×2 first-form pencil; at the maximizing pair the scalar evaluation was checked against a symmetric Cholesky eigensolve. No position or target was optimized. The analytic two-angle comparison permits any symmetric positive definite common angular target, including variable meridional speed and an off-diagonal entry.

| field | lower bound for every angularly invariant target | s | angular indices | largest generalized eigenvalue |
|---|---:|---:|---|---:|
| polar-G10s-fast-step14-step01-state.json | 0.17391836909 | 0.103942893417 | [255, 9] | 1.42106823971 |
| polar-design-G10s-fast-step17-step01-state.json | 0.123308053329 | 0.103942893417 | [127, 136] | 1.28130303648 |
| polar-frozen-alpha10-step04-step01-state.json | 0.127441464119 | 0.103942893417 | [127, 136] | 1.29210983304 |
| polar-frozen-alpha10-M32-step01-step01-state.json | 0.120530088801 | 0.103942893417 | [127, 135] | 1.27409712889 |
| polar-restricted-radius-step01-step01-state.json | 0.156232631026 | 0.103942893417 | [127, 137] | 1.37032157623 |

The largest measured pair on every field occurs near the inner end of the first prefix span. Any rotationally invariant target alone, even with arbitrary cross term and local meridional speed, leaves a large metric error on these fixed fields. The reported numbers use floating-point first jets at finitely many actual points. They do not certify continuous metric maxima or exclude a changed position field.

## Reproduction

Set S to the topic scripts directory and W to the run directory containing the source masters and scientific scripts. Use the G10/G11 complete-source and continuation recipes associated with the named input states. These are the returned inner commands.

```sh
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u $W/2ecf-polar-angular-pair-metric-floor.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --states $W/polar-G10s-fast-step14-step01-state.json $W/polar-design-G10s-fast-step17-step01-state.json $W/polar-frozen-alpha10-step04-step01-state.json $W/polar-frozen-alpha10-M32-step01-step01-state.json $W/polar-restricted-radius-step01-step01-state.json --output $W/polar-angular-pair-floor.json
```

## Scientific SHA-256

- `2ecf-polar-angular-pair-metric-floor.py`  `8aa22c297a269837a98543b9d64be91b5de223ff40a2759af89e94b0bd750698`.
- `polar-angular-pair-floor.json`  `038ccd76ca4507e6c25034b7e8662d50a540bd94867c22992c6134e5476fe281`.
