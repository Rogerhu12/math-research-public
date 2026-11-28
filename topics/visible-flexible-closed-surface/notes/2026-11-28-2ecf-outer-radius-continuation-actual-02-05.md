# outer-radius-continuation: returned physical steps 2–5

**Numerical evidence.**

All 12,789 Cartesian coefficients and only the outer 36 radius coefficients are free. The first 51 scalar coefficients are identically zero, so the original target through b is unchanged. This is a continuing provisional metric design; it is distinct from both the 87-alpha design and the 5292-column fixed-prefix-position input. The outer finite wrapper returned natural 0 in 830.26717 s.

| own | R14² | G10 metric / κ / held | G11 metric / κ / held | physical normal relative | lengths (− rejected, + accepted) | solve s / KiB |
|---:|---:|---|---|---:|---|---:|
| 2 | 0.018139396135 | 0.1934870406 / 36.75289262 / 0.6994330687 | 0.1879709591 / 36.35169195 / 0.6995665718 | 8.854e-14 | +1.0 | 232.1299 / 584396 |
| 3 | 0.0172481979128 | 0.1912332917 / 30.19094144 / 0.694569674 | 0.1856469841 / 29.92672366 / 0.6947063591 | 8.106e-14 | −1.0, −0.5, +0.25 | 145.2039 / 579152 |
| 4 | 0.0156933006053 | 0.1888337773 / 38.59998837 / 0.6831744245 | 0.1832148493 / 39.39767052 / 0.6833000639 | 6.246e-14 | −1.0, +0.5 | 175.9150 / 573104 |
| 5 | 0.0149574337395 | 0.185849444 / 26.67442902 / 0.672657605 | 0.1802700075 / 26.86032884 / 0.6727817928 | 1.066e-13 | −1.0, +0.5 | 259.3288 / 555324 |

Independent G11 uses 668 radii × 256 shifted angles, separate from the 4,291,840 physical training rows. No continuous metric or whole-closed reach follows.

## Reproduction

Set S to the topic scripts directory and W to the run directory containing the source masters and scientific scripts. Use the G10/G11 complete-source and continuation recipes associated with the named input states. These are the returned inner commands.

```sh
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u $W/2ecf-polar-restricted-radius-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-restricted-radius-step01-step01-state.json --prefix $W/polar-restricted-radius-step02 --steps 1 --initial-damping 0.0009481481481481482
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-restricted-radius-step02-step01-state.json --output $W/polar-restricted-radius-step02-G11.json
python3 -u $W/2ecf-polar-restricted-radius-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-restricted-radius-step02-step01-state.json --prefix $W/polar-restricted-radius-step03 --steps 1 --initial-damping 0.0009481481481481482
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-restricted-radius-step03-step01-state.json --output $W/polar-restricted-radius-step03-G11.json
python3 -u $W/2ecf-polar-restricted-radius-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-restricted-radius-step03-step01-state.json --prefix $W/polar-restricted-radius-step04 --steps 1 --initial-damping 0.0009481481481481482
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-restricted-radius-step04-step01-state.json --output $W/polar-restricted-radius-step04-G11.json
python3 -u $W/2ecf-polar-restricted-radius-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-restricted-radius-step04-step01-state.json --prefix $W/polar-restricted-radius-step05 --steps 1 --initial-damping 0.0009481481481481482
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-restricted-radius-step05-step01-state.json --output $W/polar-restricted-radius-step05-G11.json
```

## Scientific SHA-256

- `polar-restricted-radius-step02-step01-state.json`  `85717dc5e2fe6d614551fe52232285f84a65be16c055f8f6b79b64cd67bd7676`.
- `polar-restricted-radius-step02-G11.json`  `b279a1df2d500a207c098f34bb75594444d522335dbe30049b98e79469875e6c`.
- `polar-restricted-radius-step03-step01-state.json`  `7be579be13f395bbc24f1b16372d3e9e54b6b702f3759f333c62023656a5e733`.
- `polar-restricted-radius-step03-G11.json`  `6f48dcb5b5db7d7dbb74afd16fdea4106ad89a469342fce231d480f3567e93f0`.
- `polar-restricted-radius-step04-step01-state.json`  `449077c8f80d9ecaa2359b42cda7c7913aa24981dbe85bc31d19aff173958634`.
- `polar-restricted-radius-step04-G11.json`  `99a7d412c1a167b017e569558f437b25a0cf773d8418456bd65e3b00c9c87125`.
- `polar-restricted-radius-step05-step01-state.json`  `827f4e41b89e7b69b8d9cb108a08ed928594d85e2ff7c9b50d806d1b27808f08`.
- `polar-restricted-radius-step05-G11.json`  `8d333e9a099fe8497980a99311d5b83ecb3b174b7aa0b1a165cd52a14b1985a4`.

Exact reproducible inspections of each changed target:

```sh
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-restricted-radius-step02-step01-state.json --output $W/polar-restricted-radius-step02-target.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-restricted-radius-step03-step01-state.json --output $W/polar-restricted-radius-step03-target.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-restricted-radius-step04-step01-state.json --output $W/polar-restricted-radius-step04-target.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-restricted-radius-step05-step01-state.json --output $W/polar-restricted-radius-step05-target.json
```

- State 2, sampled target |K| on G10 13.8711009, G11 13.91743877, output `8a48b816dd97b75448105ea78e08af8381d2f652ee58393a2713a4a4dc731f13`.
- State 3, sampled target |K| on G10 16.11896162, G11 16.2712886, output `7fe7d2daef0af0d2f8b114a9ab699a2966dde3a20c67d8387a34befeb77cacdc`.
- State 4, sampled target |K| on G10 19.34298656, G11 19.4962841, output `dd2462a3e0c7d26501b96fdbb2a08e757f512e2cb2197c623377e8a0caa4228d`.
- State 5, sampled target |K| on G10 21.37014949, G11 21.5359165, output `9af564bae54377a6eb091ab57514949e6c2f0fca1e65468aecde7bd2c40d616c`.
