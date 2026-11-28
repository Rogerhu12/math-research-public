# all-alpha: returned physical steps 18–20

**Numerical evidence.**

The old invocation retained the step-18 initial file without a returned result or exit; old final status is unknown. The new wrapper resumed the actually returned 87-alpha metric-design step17. These steps update provisional target metrics and count in that design epoch only. The replacement wrapper returned natural 0 in 659.7111915739988 seconds.

| own | R14² | G10 metric / κ / held | G11 metric / κ / held | physical normal relative | lengths (− rejected, + accepted) | solve s / KiB |
|---:|---:|---|---|---:|---|---:|
| 18 | 0.00551265982956 | 0.1518894238 / 15.64901072 / 0.6128333694 | 0.1470836892 / 15.65145459 / 0.6129891746 | 2.563e-13 | −1.0, +0.5 | 249.9387 / 583896 |
| 19 | 0.00538459581358 | 0.1496734184 / 14.55793254 / 0.6146151988 | 0.1449109805 / 14.40296327 / 0.6147677296 | 3.146e-13 | +1.0 | 168.9117 / 572740 |
| 20 | 0.00528358675571 | 0.1474374663 / 24.54068084 / 0.6166087056 | 0.1427388947 / 24.23893727 / 0.6167542004 | 3.797e-13 | +1.0 | 225.8831 / 565400 |

At step 18, target |K| maxima on G10/G11 were 48.9619421/47.6049385.
At step 19, target |K| maxima on G10/G11 were 48.6639092/47.3232288.
At step 20, target |K| maxima on G10/G11 were 48.214887/46.8998127.
Independent G11 uses 668 radii × 256 shifted angles, separate from the 4,291,840 physical training rows. No continuous metric or whole-closed reach follows.

## Reproduction

Set S to the topic scripts directory and W to the run directory containing the source masters and scientific scripts. Use the G10/G11 complete-source and continuation recipes associated with the named input states. These are the returned inner commands.

```sh
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-step17-step01-state.json --prefix $W/polar-design-G10s-fast-astra-step18 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-astra-step18-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-astra-step18-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-astra-step18-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-astra-step18-target-audit.json
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-astra-step18-step01-state.json --prefix $W/polar-design-G10s-fast-astra-step19 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-astra-step19-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-astra-step19-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-astra-step19-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-astra-step19-target-audit.json
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-astra-step19-step01-state.json --prefix $W/polar-design-G10s-fast-astra-step20 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-astra-step20-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-astra-step20-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-astra-step20-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-astra-step20-target-audit.json
```

## Scientific SHA-256

- `polar-design-G10s-fast-astra-step18-step01-state.json`  `75d7d3ad9b94eb4130a6686cdc35774ba78acd36cbb242bf9da449e4667443fc`.
- `polar-design-G10s-fast-astra-step18-G11.json`  `7150787d435281ebbdeed0351a797a914b82e933f414c854a38945e754ce8ab8`.
- `polar-design-G10s-fast-astra-step18-target-audit.json`  `531fd043e70d5d8d36801957c14f4669f1dbd46265f451b956fde137d459a7fd`.
- `polar-design-G10s-fast-astra-step19-step01-state.json`  `d639b00368f7277c1cbea27a788e09ae238b86a672740b20c8cc4849c9599fac`.
- `polar-design-G10s-fast-astra-step19-G11.json`  `ef8750996abcdb985b3086fe8b41964da0e88571231e313ffd90aa7ffac94669`.
- `polar-design-G10s-fast-astra-step19-target-audit.json`  `42369719d58ffe4795883ac7d08485cf0e8a69fdbb529f45a2b0476b570b2cdb`.
- `polar-design-G10s-fast-astra-step20-step01-state.json`  `59fd904cef4837c5696945220563c978156d3ddda1a3e8158a134ea53373dde9`.
- `polar-design-G10s-fast-astra-step20-G11.json`  `87862d7e47f36ca34d1caa102e0ba0dd302ca3c3651f20648de6a903f9d73ae2`.
- `polar-design-G10s-fast-astra-step20-target-audit.json`  `4fd4989044a7e469739d213b30d5508faf75adbc7dd76b919bc4e6eae60adc42`.
