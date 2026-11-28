# Saved target from design step 10, and four fixed-metric steps

**Numerical evidence.** G10 uses 958 physical radii, two angular grids (128 and 192), all 4,291,840 physical residual rows and physical Sobolev damping. G11 independently evaluates 668 radii at 256 shifted angles, including 540 radii outside training. Held is the existing local guide distance (target 0.65). Whole-closed diameter, continuous isometry, global reach and all-time embedding remain open. The strong budget uses whole-closed $D\le 3.2$.

Freeze every physical knot and all 87 saved dyadic coefficients from design step 10. Manifest SHA-256 0208220f1622e8260fadda35964736b92f0a7e84d09260880f09b78b3dad287c. Baseline training values and independent G11 statistics agree with design 10. Frozen own counter starts at zero. On the first step the original FD probe at $10^{-6}$ gave 3.21067e-5, and the same direction at $10^{-7}$ gave 2.98935e-8. The adjoint defect was 5.662e-14. Whole four-step wrapper returned 0 in 883.10017 seconds, peak RSS 541984 KiB.

| own step | R14² | G10 metric / κ / held | G11 metric / κ / held | full normal relative residual | trial lengths (− rejected, + accepted) | solve seconds / peak KiB |
|---:|---:|---|---|---:|---|---:|
| 1 | 0.00770123553096 | 0.1643993344 / 25.83616072 / 0.6074535198 | 0.1591497304 / 25.91515354 / 0.6076277832 | 1.622e-13 | −1.0, +0.5 | 239.43680 / 541984 |
| 2 | 0.00736412234426 | 0.1638760324 / 41.61519597 / 0.6087001871 | 0.158377512 / 40.37716755 / 0.6088653204 | 6.374e-14 | −1.0, +0.5 | 238.91613 / 484908 |
| 3 | 0.00684123690041 | 0.1631089012 / 23.60785866 / 0.6093251273 | 0.1576895349 / 23.6611003 / 0.6094875046 | 5.635e-14 | +1.0 | 252.15456 / 494152 |
| 4 | 0.00652098690516 | 0.1608461777 / 20.19933858 / 0.6091442634 | 0.1555797 / 20.47231942 / 0.6093065665 | 1.233e-13 | −1.0, −0.5, +0.25 | 140.26231 / 469132 |

## Source and output identities

- Step 1 state `c4771d668ac496977e5336a1b360ead7eed499c0e5804ae57dbba0bee5309150`, G11 `60ec8c033eeff9f42201fac07bf43496f994d546f1defd37c777cf0893573b6a`.
- Step 2 state `165bbcca0db3ca6bb588a6c2b163b67ef301194c5d65b727a05db992a428afa8`, G11 `1947e3d399289443dc21b1766c351dabf6484228defc1ba6b918843bc70fcd77`.
- Step 3 state `01702afabf1e36af9dd8bd3552443e75cff094e9235ce0396ff9eac98bfb8285`, G11 `bcca71c8e3d1d9e221d17c1e32ec3d8d7ba6a7a2a3639df7ec461428886c7e50`.
- Step 4 state `10fee0325bba32ab5eb1f58b84c8be1b87ca14efab9474adb27011f66063707f`, G11 `ddf167ab8552db6b26ce2458ad467b7230243878db4123a0d472af82f8507a14`.

- 2ecf-polar-freeze-designed-target.py `733f29fb793c8f6eb126a5b5b3b33acb1b57ae2c615362002ab74dcc479a70c3`.
- 2ecf-polar-frozen-designed-g-solve.py `f97d3bf174d0e7fb10d6ac42aa5df958ed1b4844807f0ff3675cbe065ef9c8c3`.
- 2ecf-polar-frozen-designed-g-observe.py `24c40ffb502c9df5a3a6ce8d6dcc825eb8fc2c5709450110ab1eca192fa3d138`.

## Reproduction

Use the G10 complete-source/four-baseline recipe, the independent G11 shifted-256 source, and the continuation preceding the first step in this table. Set S to the topic scripts directory and W to the separate run directory containing the preceding states and source masters. Place all cited 2ecf entry scripts in W as in the source recipe. These are the actual inner commands with portable directories. Each succeeded with natural return code 0.

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
python3 -u $W/2ecf-polar-freeze-designed-target.py --state $W/polar-design-G10s-fast-step10-step01-state.json --output $W/polar-designed-alpha10-frozen-target.json
python3 -u $W/2ecf-polar-frozen-designed-g-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --design-state $W/polar-design-G10s-fast-step10-step01-state.json --prefix $W/polar-frozen-alpha10-baseline --steps 0 --initial-damping 0.0010666666666666667
python3 -u $W/2ecf-polar-frozen-designed-g-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-frozen-alpha10-baseline-initial.json --reference-observation $W/polar-design-G10s-fast-step10-G11.json --output $W/polar-frozen-alpha10-baseline-G11.json
python3 -u $W/2ecf-polar-frozen-designed-g-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-frozen-alpha10-baseline-initial.json --prefix $W/polar-frozen-alpha10-step01 --steps 1 --initial-damping 0.0010666666666666667
python3 -u $W/2ecf-polar-frozen-designed-g-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --state $W/polar-frozen-alpha10-step01-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-frozen-alpha10-step01-G11.json
python3 -u $W/2ecf-polar-frozen-designed-g-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-frozen-alpha10-step01-step01-state.json --prefix $W/polar-frozen-alpha10-step02 --steps 1 --initial-damping 0.0010666666666666667
python3 -u $W/2ecf-polar-frozen-designed-g-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --state $W/polar-frozen-alpha10-step02-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-frozen-alpha10-step02-G11.json
python3 -u $W/2ecf-polar-frozen-designed-g-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-frozen-alpha10-step02-step01-state.json --prefix $W/polar-frozen-alpha10-step03 --steps 1 --initial-damping 0.0010666666666666667
python3 -u $W/2ecf-polar-frozen-designed-g-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --state $W/polar-frozen-alpha10-step03-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-frozen-alpha10-step03-G11.json
python3 -u $W/2ecf-polar-frozen-designed-g-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-frozen-alpha10-step03-step01-state.json --prefix $W/polar-frozen-alpha10-step04 --steps 1 --initial-damping 0.0010666666666666667
python3 -u $W/2ecf-polar-frozen-designed-g-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --frozen-target $W/polar-designed-alpha10-frozen-target.json --state $W/polar-frozen-alpha10-step04-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-frozen-alpha10-step04-G11.json
```
