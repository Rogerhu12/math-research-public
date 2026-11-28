# position-suffix-local-h-quartering: returned physical steps 1–1

**Numerical evidence.**

Start from the actual original-prefix 5292-dimensional step 9, SHA 311cc7b82d6f917b056d69bc9044e4999c6004e493d0b2fdf05aefb4836b1215. Preserve the fixed target, source, all existing knots, all angular channels, and 4,291,840 original G10 rows. Quarter each of the first three active physical b..S spans, nearest-binary64 new knot positions. Nine new simple knots give 45 radial functions × 147 Cartesian channels = 6615 columns. The first-span worst metric and curvature occur near .204 and .194, respectively.
With quintic old knot vector T and a single new interior knot in old span k, exact new control i in k−4..k is (1−a_i)P_(i−1)+a_i P_i, a_i=(t−T_i)/(T_(i+5)−T_i). Earlier controls are copied and later ones shifted. Composing all nine rational insertion matrices preserves the entire continuous parent spline mathematically and both clamped two-jets. Check out each new coefficient only once to binary64. Maximum exact coefficient checkout error 585706194591383/375579577303343810674990694531072.
Own0 new initial G10 differences measured against physical parent {'squaredNorm': 0.0, 'maxRelativeMetric': 4.440892098500626e-16, 'maxCurvature': 7.105427357601002e-15, 'minHeldDistance': 0.0, 'minImmersion': 2.220446049250313e-16}. Independent G11 baseline metric 0.2543932479220666 and curvature 21.127509035502968. The new step's own full finite-difference and adjoint checks used all 6615 columns and 4291840 rows. Coarse-parent accepts are provenance only. The literal prefix remains unsolved to arbitrary tolerance; R258 pertains to the accurate fixed prefix.
For these commands start in W. Replace the relative repository scripts argument with S, and use the numerically corresponding .py entry from the topic scripts. All input state paths and exact outputs are recorded below. The G11 baseline command consumes the initial state produced by the solve; run the solve before that inspection.

| own | R14² | G10 metric / κ / held | G11 metric / κ / held | physical normal relative | lengths (− rejected, + accepted) | solve s / KiB |
|---:|---:|---|---|---:|---|---:|
| 1 | 0.0673898678681 | 0.2476680985 / 20.71336391 / 0.7069593104 | 0.2477779775 / 20.78333205 / 0.7071009086 | 9.841e-14 | −1.0, −0.5, −0.25, −0.125, +0.0625 | 189.8477 / 467384 |

Independent G11 uses 668 radii × 256 shifted angles, separate from the 4,291,840 physical training rows. No continuous metric or whole-closed reach follows.

## Reproduction

Set S to the topic scripts directory and W to the run directory containing the source masters and scientific scripts. Use the G10/G11 complete-source and continuation recipes associated with the named input states. These are the returned inner commands.

```sh
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u 2ecf-polar-local-suffix-h-solve.py --scripts $S --prepare-entry 2ecf-polar-c2-g10-split-prepare.py --prepared polar-c2-G10s-prepared.json --normal-audit polar-G10s-sparse-jet-full-normal-audit.json --warm-state polar-fixed-prefix-original16-step09-step01-state.json --prefix polar-local-suffix-h9-step01 --initial-damping 0.0035555555555555553 --steps 1
python3 -u 2ecf-polar-local-suffix-h-observe.py --scripts $S --prepare-entry 2ecf-polar-c2-g10-split-prepare.py --prepared polar-c2-G10s-prepared.json --observer polar-independent-G11r-shifted256-independent.json --state polar-local-suffix-h9-step01-initial.json --output polar-local-suffix-h9-baseline-G11.json
python3 -u 2ecf-polar-local-suffix-h-observe.py --scripts $S --prepare-entry 2ecf-polar-c2-g10-split-prepare.py --prepared polar-c2-G10s-prepared.json --observer polar-independent-G11r-shifted256-independent.json --state polar-local-suffix-h9-step01-step01-state.json --output polar-local-suffix-h9-step01-G11.json
```

## Scientific SHA-256

- `2ecf-polar-local-suffix-boehm.py`  `551382710d43d50b79cf0e1add72f21746990307b2187f72924a8110ae55198b`.
- `2ecf-polar-local-suffix-h-solve.py`  `a8fd83a700bf737c9985841841acb3682a0d122df1dcc9c50195d8267d775f4e`.
- `2ecf-polar-local-suffix-h-observe.py`  `425d51bb2ef4a4b297d760485d5051e84d49777e60f3a6fb9c1738d80637a719`.
- `polar-local-suffix-h9-baseline-G11.json`  `130ecd1fcd835ad39bd8364ec84e26f4cde5f9cb984ccc5e022aca2efe9cb59f`.
- `polar-local-suffix-h9-step01-initial.json`  `07f5581eb05b565b40a828cdf3710a57f6455d638b4f3292240c7239388270a5`.
- `polar-local-suffix-h9-step01-actual-derivative-check.json`  `917ad06a3bd93cd6261e2afcac3f21c1c9e69984754c0e3d3b8c4e68b9c8304e`.
- `polar-local-suffix-h9-step01-exit.json`  `79a2c96bb9f8932f36e343fb720c32847c5683f1227cfdeebd3659b48be1d1f4`.
- `polar-local-suffix-h9-step01-G11-exit.json`  `ead5c40b16bc8286fc39d4a9c49ba9f3d83bfad40249bec69ba535581a4b1be8`.
- `polar-local-suffix-h9-baseline-G11-exit.json`  `205bd32c5b327b01c16ffc61354e3ce5368af247e4e2e029fe75ad5d99c1ee70`.
- `polar-local-suffix-h9-step01-step01-state.json`  `02448a24ec4bd1c353fbde9f1e508bff5cf69e42efa7209267245188e68b114c`.
- `polar-local-suffix-h9-step01-G11.json`  `4950a1980466e67d152a6fc73c75be6e7f596e7320e65ca32f4e70e44988c3f4`.
