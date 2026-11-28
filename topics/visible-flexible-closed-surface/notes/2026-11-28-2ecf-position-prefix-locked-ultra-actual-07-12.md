# position-prefix-locked-ultra: returned physical steps 7–12

**Numerical evidence.**

Continue the same 5292-column, original fixed-g and original full literal position prefix from its accepted step 6. Each input/line search/G11 belongs to this epoch. Although the total cost decreases, the G11 metric remains roughly .25 and the curvature near 21. No closed geometry or refinement convergence follows. Outer driver returned 0 in 902.803101 s, peak 432888 KiB.

| own | R14² | G10 metric / κ / held | G11 metric / κ / held | physical normal relative | lengths (− rejected, + accepted) | solve s / KiB |
|---:|---:|---|---|---:|---|---:|
| 7 | 0.0685217490194 | 0.2526107107 / 20.83201264 / 0.7081105439 | 0.2530679013 / 20.94486041 / 0.7082652875 | 5.348e-15 | −1.0, +0.5 | 180.1464 / 400496 |
| 8 | 0.0682699091376 | 0.2533095711 / 20.95297032 / 0.7071739461 | 0.2541239246 / 21.09454277 / 0.7073147382 | 1.149e-14 | −1.0, +0.5 | 171.4405 / 398296 |
| 9 | 0.0681464520352 | 0.2535788277 / 20.99664057 / 0.7062424029 | 0.2543932479 / 21.12750904 / 0.7063756754 | 1.417e-14 | −1.0, +0.5 | 150.7720 / 380680 |
| 10 | 0.0677315899998 | 0.2534734213 / 21.02597677 / 0.705839455 | 0.2542957153 / 21.15640707 / 0.7059725611 | 1.386e-14 | −1.0, −0.5, +0.25 | 99.6719 / 432888 |
| 11 | 0.0674502604642 | 0.2551190053 / 21.21387163 / 0.7038667678 | 0.255870969 / 21.32885379 / 0.7040126625 | 1.838e-14 | +1.0 | 86.1171 / 400920 |
| 12 | 0.0674129451375 | 0.25451434 / 21.25289197 / 0.7029318534 | 0.2551431156 / 21.34979322 / 0.703075551 | 4.382e-14 | −1.0, +0.5 | 202.9738 / 380728 |

Independent G11 uses 668 radii × 256 shifted angles, separate from the 4,291,840 physical training rows. No continuous metric or whole-closed reach follows.

## Reproduction

Set S to the topic scripts directory and W to the run directory containing the source masters and scientific scripts. Use the G10/G11 complete-source and continuation recipes associated with the named input states. These are the returned inner commands.

```sh
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-fixed-prefix-original16-step06-step01-state.json --prefix $W/polar-fixed-prefix-original16-step07 --initial-damping 0.001 --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step07-step01-state.json --output $W/polar-fixed-prefix-original16-step07-G11.json
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-fixed-prefix-original16-step07-step01-state.json --prefix $W/polar-fixed-prefix-original16-step08 --initial-damping 0.001 --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step08-step01-state.json --output $W/polar-fixed-prefix-original16-step08-G11.json
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-fixed-prefix-original16-step08-step01-state.json --prefix $W/polar-fixed-prefix-original16-step09 --initial-damping 0.001 --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step09-step01-state.json --output $W/polar-fixed-prefix-original16-step09-G11.json
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-fixed-prefix-original16-step09-step01-state.json --prefix $W/polar-fixed-prefix-original16-step10 --initial-damping 0.001 --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step10-step01-state.json --output $W/polar-fixed-prefix-original16-step10-G11.json
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-fixed-prefix-original16-step10-step01-state.json --prefix $W/polar-fixed-prefix-original16-step11 --initial-damping 0.001 --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step11-step01-state.json --output $W/polar-fixed-prefix-original16-step11-G11.json
python3 -u $W/2ecf-polar-fixed-prefix-position-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-fixed-prefix-original16-step11-step01-state.json --prefix $W/polar-fixed-prefix-original16-step12 --initial-damping 0.001 --steps 1
python3 -u $W/2ecf-polar-fixed-prefix-position-observe.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --observer $W/polar-independent-G11r-shifted256-independent.json --state $W/polar-fixed-prefix-original16-step12-step01-state.json --output $W/polar-fixed-prefix-original16-step12-G11.json
```

## Scientific SHA-256

- `polar-fixed-prefix-original16-ultra-07-12-driver-exit.json`  `9e6cc02c6092f893c6a251bfd4c170900b3e9a0eee3200f0ab7c00e074065b2a`.
- `polar-fixed-prefix-original16-step07-step01-state.json`  `f6bfdcf6105c42784d0dd13c68ad7c63a1fa7b728d3e62324965fac7104437ed`.
- `polar-fixed-prefix-original16-step07-G11.json`  `0706e00e9de663b9f293c8c785d23f5331633d447dc999ee110b2be353b529e3`.
- `polar-fixed-prefix-original16-step08-step01-state.json`  `7a169b21037beea52dc4ed4971e441097de1b23daa5620abd595bea9ace94f92`.
- `polar-fixed-prefix-original16-step08-G11.json`  `7e8df02e9be256322baf77d6937a44a79caeabc557f63bdd46eb781b8f96c01c`.
- `polar-fixed-prefix-original16-step09-step01-state.json`  `311cc7b82d6f917b056d69bc9044e4999c6004e493d0b2fdf05aefb4836b1215`.
- `polar-fixed-prefix-original16-step09-G11.json`  `bd99ec1ed9b5b2b6c30e307c6ee31e1347bd01bbf6cb625920e022207c20a310`.
- `polar-fixed-prefix-original16-step10-step01-state.json`  `ead8e4760cb8884f733cd7276dde49fbc2a2bd50d9a79ba02b10e82438b99136`.
- `polar-fixed-prefix-original16-step10-G11.json`  `ebe75638ec40845c3cbca18c2ef14bdb9a9fe68a25997ef6ace580c687b5c116`.
- `polar-fixed-prefix-original16-step11-step01-state.json`  `4b396e102a95bdac4f849c3e2c54becb8d5d7759e6ba9c2f733fbb21d2afd63a`.
- `polar-fixed-prefix-original16-step11-G11.json`  `91ba7d6414a3f9167c8d2a987709342c76d43d908054504a1de70d83130acd25`.
- `polar-fixed-prefix-original16-step12-step01-state.json`  `385fb2f8e725da5bde39932ef26183158a7e2c1562fe0a80b8149ebe5a9d6f15`.
- `polar-fixed-prefix-original16-step12-G11.json`  `a286e01bc872099de1162c814c1325436e524f0e36db06575dcd96dd23a23137`.
