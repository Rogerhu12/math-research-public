# position-prefix-locked-continuation: returned physical steps 3–6

**Numerical evidence.**

The 5292-dimensional space retains the exact original target and original position throughout 0..b, with both endpoint two-jets clamped. It contains every b..S admissible quintic Cartesian coefficient. These are actual new accepts from the previously reported 5292-dimensional step 2. All 4,291,840 training rows and shifted independent G11 are evaluated.

| own | R14² | G10 metric / κ / held | G11 metric / κ / held | physical normal relative | lengths (− rejected, + accepted) | solve s / KiB |
|---:|---:|---|---|---:|---|---:|
| 3 | 0.116077028634 | 0.5070981413 / 29.60197548 / 0.7106430872 | 0.4969510193 / 29.36272148 / 0.7107867477 | 9.342e-16 | +1.0 | 157.1153 / 393920 |
| 4 | 0.0903355975981 | 0.3903985648 / 19.8093707 / 0.7108823953 | 0.3854676798 / 19.76236583 / 0.7110314582 | 1.29e-15 | −1.0, +0.5 | 189.2212 / 412928 |
| 5 | 0.0715202202835 | 0.2578283069 / 20.35642061 / 0.7104077204 | 0.2566807356 / 20.52322247 / 0.7105486539 | 1.077e-15 | +1.0 | 123.7495 / 405216 |
| 6 | 0.0697228931865 | 0.2511088341 / 20.73283318 / 0.7091844673 | 0.2509047259 / 20.90341971 / 0.7093248156 | 5.037e-15 | −1.0, +0.5 | 136.8706 / 422348 |

Independent G11 uses 668 radii × 256 shifted angles, separate from the 4,291,840 physical training rows. No continuous metric or whole-closed reach follows.

## Reproduction

Set S to the topic scripts directory and W to the run directory containing the source masters and scientific scripts. Use the G10/G11 complete-source and continuation recipes associated with the named input states. These are the returned inner commands.

```sh
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-fixed-prefix-original16-step02-step01-state.json --prefix $W/polar-fixed-prefix-original16-step03 --initial-damping 0.001 --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step03-step01-state.json --output $W/polar-fixed-prefix-original16-step03-G11.json
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-fixed-prefix-original16-step03-step01-state.json --prefix $W/polar-fixed-prefix-original16-step04 --initial-damping 0.001 --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step04-step01-state.json --output $W/polar-fixed-prefix-original16-step04-G11.json
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-fixed-prefix-original16-step04-step01-state.json --prefix $W/polar-fixed-prefix-original16-step05 --initial-damping 0.001 --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step05-step01-state.json --output $W/polar-fixed-prefix-original16-step05-G11.json
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-fixed-prefix-original16-step05-step01-state.json --prefix $W/polar-fixed-prefix-original16-step06 --initial-damping 0.001 --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step06-step01-state.json --output $W/polar-fixed-prefix-original16-step06-G11.json
```

## Scientific SHA-256

- `polar-fixed-prefix-original16-step03-step01-state.json`  `79b2b9d0e3d48db0266762803795e088d249c884eeeafcad6c9df2eba9dfcd96`.
- `polar-fixed-prefix-original16-step03-G11.json`  `153f0f853c2517b30a21f3188d1b784146d6c8f1b9b2be9b2e5b6517e8a17846`.
- `polar-fixed-prefix-original16-step04-step01-state.json`  `7550afa99f8a2e41e84de13934fde31af8b1a4959c3a321dd792e9c2dd684fd8`.
- `polar-fixed-prefix-original16-step04-G11.json`  `9b4fbe88dc42e3d33c063d5635ddad54f9708cb135f81536d04d8f7abbdc6c89`.
- `polar-fixed-prefix-original16-step05-step01-state.json`  `80f818cc10b0015426e46b5b9d051c1d8e7ceb43e86da3979cbbfbc0bcb8272c`.
- `polar-fixed-prefix-original16-step05-G11.json`  `58dcc4002424b3874a3a201f8aaccf4b507a788813e42e76a9d598f8e1549414`.
- `polar-fixed-prefix-original16-step06-step01-state.json`  `49b442c9334042b618f5a3b83347aa6896b653673712fa2a606f3a87a1628fef`.
- `polar-fixed-prefix-original16-step06-G11.json`  `83005c0ba839e7265513de0ff35c29e604608a7027f05bd2306a327f4d160d47`.
