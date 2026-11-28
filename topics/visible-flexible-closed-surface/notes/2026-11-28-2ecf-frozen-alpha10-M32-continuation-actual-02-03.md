# frozen-alpha10-M32-continuation: returned physical steps 2–3

**Numerical evidence.**

After the exact M24-to-M32 transfer, keep exactly the design-10 frozen target and all physical source samples, with 16,965 Cartesian degrees of freedom. The refined space has a separate counter. Its first step is reported separately. The two-step continuation wrapper returned natural 0 in 608.21032 s. Training R14² decreases while the sampled curvature and peak metric need not move monotonically.

| own | R14² | G10 metric / κ / held | G11 metric / κ / held | physical normal relative | lengths (− rejected, + accepted) | solve s / KiB |
|---:|---:|---|---|---:|---|---:|
| 2 | 0.00539926528884 | 0.1631924689 / 37.49758255 / 0.6100157366 | 0.1569459302 / 36.45886688 / 0.6102043334 | 7.741e-14 | +1.0 | 286.5339 / 612112 |
| 3 | 0.0051766905182 | 0.1607944965 / 37.26150829 / 0.6099415732 | 0.1546766896 / 36.75261588 / 0.610130555 | 4.361e-14 | −1.0, +0.5 | 314.3067 / 637920 |

Independent G11 uses 668 radii × 256 shifted angles, separate from the 4,291,840 physical training rows. No continuous metric or whole-closed reach follows.

## Reproduction

Set S to the topic scripts directory and W to the run directory containing the source masters and scientific scripts. Use the G10/G11 complete-source and continuation recipes associated with the named input states. These are the returned inner commands.

```sh
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u $W/2ecf-polar-frozen-designed-g-fourier-solve.py --scripts $W/../math-research-public/topics/visible-flexible-closed-surface/scripts --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --state $W/polar-frozen-alpha10-M32-step01-step01-state.json --prefix $W/polar-frozen-alpha10-M32-step02 --modes 32 --steps 1 --initial-damping 0.004266666666666667
python3 -u $W/2ecf-polar-frozen-designed-g-fourier-observe.py --scripts $W/../math-research-public/topics/visible-flexible-closed-surface/scripts --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-frozen-alpha10-M32-step02-step01-state.json --output $W/polar-frozen-alpha10-M32-step02-G11.json
python3 -u $W/2ecf-polar-frozen-designed-g-fourier-solve.py --scripts $W/../math-research-public/topics/visible-flexible-closed-surface/scripts --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --state $W/polar-frozen-alpha10-M32-step02-step01-state.json --prefix $W/polar-frozen-alpha10-M32-step03 --modes 32 --steps 1 --initial-damping 0.004266666666666667
python3 -u $W/2ecf-polar-frozen-designed-g-fourier-observe.py --scripts $W/../math-research-public/topics/visible-flexible-closed-surface/scripts --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-frozen-alpha10-M32-step03-step01-state.json --output $W/polar-frozen-alpha10-M32-step03-G11.json
```

## Scientific SHA-256

- `polar-frozen-alpha10-M32-step02-step01-state.json`  `a81043af45035e018b285dd60a140b539c61dc6e575e1dad073f354e5844e9ec`.
- `polar-frozen-alpha10-M32-step02-G11.json`  `fee71ce399d9596129dbae3cfc78087748e3352d92b3f269a47a0d230d144cce`.
- `polar-frozen-alpha10-M32-step03-step01-state.json`  `9c7ad36a1126df5069a5f0f3417a1d081482beeff7600e6fcb72490f57e40f99`.
- `polar-frozen-alpha10-M32-step03-G11.json`  `ca7dfa2a1658f35fac9d273ee9dc90e2e57497982455ffe9d28ef27604b5ca5f`.
