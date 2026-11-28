# position-prefix-locked: returned physical steps 1–2

**Numerical evidence.**

New restricted fixed original-g input. Start from original16 but permit only the 36 clamped b..S quintics × 147 Cartesian angular channels (5292). Each inherited seven-knot window is checked exactly against its full-basis parent. Position value, first and second derivatives of the correction vanish throughout 0..b. The original 13+q2 rows, physical quadrature weights and actual source at every point stay in the objective, including guide violations on the locked prefix. The admissible H² is evaluated with the same physical quadrature and the restricted functions. Old accepts are provenance only.
Four actual 5292-column own0 baselines: literal suffix coefficient copy R14² 446.488564; Greville quintic taper lengths .06 and .18 give 36.275829 and 4.220569; zero 97.091081. Select .18 by full squared norm; baseline metric 1.51924149, curvature 32.76571, held .72433342. Taper applies to initial coefficients only. Every allowed suffix coefficient is free on subsequent steps.
The first independent G11 metric maximum is at s=.29169009 in the movable suffix, away from the previous full-position first-span hotspot. As a restricted construction this can improve the suffix without damaging the fixed literal prefix. Its residual still exceeds the full-space input. An intrinsic error of the fixed prefix cannot be reduced by a suffix-only mesh refinement.

| own | R14² | G10 metric / κ / held | G11 metric / κ / held | physical normal relative | lengths (− rejected, + accepted) | solve s / KiB |
|---:|---:|---|---|---:|---|---:|
| 1 | 1.11301141946 | 0.9811351444 / 28.02952437 / 0.7034741764 | 0.9718686328 / 27.94421262 / 0.7035920412 | 1.433e-15 | +1.0 | 123.8860 / 496700 |
| 2 | 0.21189390564 | 0.5505423459 / 23.60746339 / 0.711174447 | 0.5450337233 / 23.72228764 / 0.7113098126 | 7.172e-16 | +1.0 | 122.4640 / 369532 |

Independent G11 uses 668 radii × 256 shifted angles, separate from the 4,291,840 physical training rows. No continuous metric or whole-closed reach follows.

## Reproduction

Set S to the topic scripts directory and W to the run directory containing the source masters and scientific scripts. Use the G10/G11 complete-source and continuation recipes associated with the named input states. These are the returned inner commands.

```sh
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --initial-damping 0.001 --prefix $W/polar-fixed-prefix-original16-copy --warm-state $W/polar-G10s-fast-astra-step16-step01-state.json --taper 0 --steps 0
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --initial-damping 0.001 --prefix $W/polar-fixed-prefix-original16-short --warm-state $W/polar-G10s-fast-astra-step16-step01-state.json --taper 0.06 --steps 0
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --initial-damping 0.001 --prefix $W/polar-fixed-prefix-original16-long --warm-state $W/polar-G10s-fast-astra-step16-step01-state.json --taper 0.18 --steps 0
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --initial-damping 0.001 --prefix $W/polar-fixed-prefix-original16-zero --zero --steps 0
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --initial-damping 0.001 --prefix $W/polar-fixed-prefix-original16-step01 --state $W/polar-fixed-prefix-original16-long-initial.json --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step01-step01-state.json --output $W/polar-fixed-prefix-original16-step01-G11.json
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-fixed-prefix-original16-step01-step01-state.json --prefix $W/polar-fixed-prefix-original16-step02 --initial-damping 0.001 --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step02-step01-state.json --output $W/polar-fixed-prefix-original16-step02-G11.json
```

The four-baseline selector and actual first-step launcher can equivalently be run with:

```sh
python3 -u $W/2ecf-polar-fixed-prefix-warm-choice.py --work $W --scripts $S --warm-state $W/polar-G10s-fast-astra-step16-step01-state.json --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --prefix $W/polar-fixed-prefix-original16
```

## Scientific SHA-256

- `2ecf-polar-fixed-prefix-position-basis.py`  `dc2d07aacb578100ec0df7bf5143fb895848c1e93f7c8b858dea7ccf47f9f29c`.
- `2ecf-polar-fixed-prefix-position-solve.py`  `ccdd4cdbc8b4a8c51771a393c886d90fe7828302a531bf55104284493c55c80a`.
- `2ecf-polar-fixed-prefix-position-observe.py`  `f3a5ba66d964ea34eaadbccae761b9b59247fb7f0c9dfa3f4d8484b1bdcf2b56`.
- `2ecf-polar-fixed-prefix-warm-choice.py`  `448dbd7d6212c8e05fad89ee1678b9950b6f91a9a21a04ba305b1ab4a0d01329`.
- `polar-fixed-prefix-original16-selection.json`  `b904fda229ff94a6110f6221682b3f219808b8777c783da85926451c665a31cf`.
- `polar-fixed-prefix-original16-step01-actual-derivative-check.json`  `715fc91cb3288ca5df2695eee88d114a8f2968d832eb0bff1a151f02a129fb6e`.
- `polar-fixed-prefix-original16-step01-step01-state.json`  `f11ae567f7697be4d33e660860d07b0dcf50df882f80c36888cdafb8ed70f290`.
- `polar-fixed-prefix-original16-step01-G11.json`  `c1ad9dc1fd2ea731cad637c3aa68193adfd27fc3fe63a686b8c78e9a13dd427b`.
- `polar-fixed-prefix-original16-step02-step01-state.json`  `937768227d1c710462819ed2ba2fcaa38d15f0425d67bbf7367c64faaa7d0350`.
- `polar-fixed-prefix-original16-step02-G11.json`  `1a69edbcedc416a9f06cb59f4f1cbe1e05fb2cfd048bb3b350059f87af4ce5d9`.
