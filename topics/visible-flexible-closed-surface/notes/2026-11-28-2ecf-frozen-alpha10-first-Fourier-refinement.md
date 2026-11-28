# Actual M24 to M32 Cartesian refinement with design-10 target frozen

**Numerical evidence.**

All 87 target coefficients and all radial functions remain fixed. The 12,789 coefficients of the step-four coarse Cartesian field extend by exact zero insertion to 16,965 coefficients. G10 and shifted G11 baseline statistics agree identically with the coarse field. All six directly evaluated G11 jet difference maxima are zero. The finer space then accepted its own first update at length 0.5 after rejecting length 1.

G10 on 958 radii and 128+192 angles: residual squared 0.00652098690516 → 0.00593909416218, worst relative metric 0.1608461777 → 0.1598787186, largest absolute curvature 20.19934 → 29.84578, local held guide 0.6091443 → 0.6099021. All 4,291,840 rows remain. G11 on 668 radii and 256 shifted angles: metric 0.1555797000 → 0.1539058635, curvature 20.47232 → 30.82517, held 0.60930657 → 0.61007264.

Full physical 16,965-column J/JT adjoint error 3.64153e-14. Centered FD at 1e-6 yielded 2.26200e-5, exceeding the existing 2e-5 threshold. At 1e-7 it gave 2.98791e-8. Full independent normal residual 2.64012e-13. Solve natural exit 0 in 192.12174 s. Next damping 0.008533333333333334.

This is one genuine same-target angular-space refinement with one accepted step. The held guide still falls short of 0.65 and the curvature worsens. Neither a converged refinement sequence nor a continuous metric or whole-closed reach estimate follows.

## Reproduction

Set S to the topic scripts directory and W to the separate run directory. Use the G10 complete-source and four-baseline recipe and preceding steps for the prepared sources and states. For the small operator check use the preceding extended prepared source from the local log-radius audit. Place the cited scripts in W. All commands below have an actual natural exit 0.

```sh
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
python3 -u $W/2ecf-polar-frozen-designed-g-fourier-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --warm-state $W/polar-frozen-alpha10-step04-step01-state.json --prefix $W/polar-frozen-alpha10-M32-step01 --modes 32 --steps 1 --initial-damping 0.004266666666666667
python3 -u $W/2ecf-polar-frozen-designed-g-fourier-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-frozen-alpha10-M32-step01-initial.json --output $W/polar-frozen-alpha10-M32-baseline-G11.json --reference-observation $W/polar-frozen-alpha10-step04-G11.json
python3 -u $W/2ecf-polar-frozen-designed-g-fourier-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-frozen-alpha10-M32-step01-step01-state.json --output $W/polar-frozen-alpha10-M32-accepted-G11.json
```

## SHA-256

- `2ecf-polar-fourier-refinement.py`  `8c739afc6716854a21adc36f3d17280461714926b529b62b215df37e7169ec60`.
- `2ecf-polar-frozen-designed-g-fourier-solve.py`  `0e93e06b0df8cfa5df03522980efd288d5b9c80aabaa4534fee65c69ebc09815`.
- `2ecf-polar-frozen-designed-g-fourier-observe.py`  `6873a641d3c491652a42bc5bda9acadda04513b78e52ae2f6cdbcfe37fafbea9`.
- `polar-frozen-alpha10-M32-step01-initial.json`  `162956fca4935ebc3c5298903e8f429bec1d111d32a8e71fa29edd7f82f8c7e9`.
- `polar-frozen-alpha10-M32-step01-step01-state.json`  `a8a4d2231af9b89ce25317d8e93f2a8541eb5fd384a588f72bfcf1f3bd9e0d09`.
- `polar-frozen-alpha10-M32-step01-actual-derivative-check.json`  `9a4ccde394d713236823784141bf29c6f27d581be3f0be692edb441dc970e6c9`.
- `polar-frozen-alpha10-M32-step01-report.json`  `99b9660b18001ffac585e7c4c80cbf73c719600d1a4e537445b8d98231f85847`.
- `polar-frozen-alpha10-M32-baseline-G11.json`  `c3ac88d015b7424d0d1707a2d461a9027e91ad7d9207f4a7bcae5b74d3193400`.
- `polar-frozen-alpha10-M32-accepted-G11.json`  `01e26eb439b0744848e652f8010e695e4fe3280790876c30e3cb5fa9057521ac`.
