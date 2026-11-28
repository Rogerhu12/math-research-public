# original-recovered: returned physical steps 15–16

**Numerical evidence.**

The old outer invocation lost its handle and retained the step-15 initial file without an accepted result or exit. Its final exit status is unknown. A fresh invocation resumed the actually returned original fixed-g14, retained its counter once and returned steps 15 and 16 plus G11. The replacement wrapper returned natural 0 in 382.77482 seconds. All original 12,789 positions remained free; the target never changed.

| own | R14² | G10 metric / κ / held | G11 metric / κ / held | physical normal relative | lengths (− rejected, + accepted) | solve s / KiB |
|---:|---:|---|---|---:|---|---:|
| 15 | 0.0261271890779 | 0.2152809123 / 38.32474026 / 0.7239667833 | 0.2096264905 / 37.24791943 / 0.7241084874 | 5.443e-14 | −1.0, −0.5, +0.25 | 209.4933 / 486752 |
| 16 | 0.0251876131439 | 0.2162892613 / 23.77146266 / 0.7243334209 | 0.2104690485 / 23.22342931 / 0.7244721813 | 1.753e-14 | −1.0, +0.5 | 167.7894 / 501844 |

Independent G11 uses 668 radii × 256 shifted angles, separate from the 4,291,840 physical training rows. No continuous metric or whole-closed reach follows.

## Reproduction

Set S to the topic scripts directory and W to the run directory containing the source masters and scientific scripts. Use the G10/G11 complete-source and continuation recipes associated with the named input states. These are the returned inner commands.

```sh
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u $W/2ecf-polar-c2-g10-fast-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-G10s-fast-step14-step01-state.json --prefix $W/polar-G10s-fast-astra-step15 --steps 1 --initial-damping 0.0001
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-fast-astra-step15-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-G10s-fast-astra-step15-G11.json
python3 -u $W/2ecf-polar-c2-g10-fast-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-G10s-fast-astra-step15-step01-state.json --prefix $W/polar-G10s-fast-astra-step16 --steps 1 --initial-damping 0.0001
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-fast-astra-step16-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-G10s-fast-astra-step16-G11.json
```

## Scientific SHA-256

- `polar-G10s-fast-astra-step15-step01-state.json`  `d6f69ca91d3ad49a2823732bd83d2ff236e9258177c2c6d4f61aa0636784b754`.
- `polar-G10s-fast-astra-step15-G11.json`  `239a0cd99f384c880c1a990b1d594a5f49b12cfd95bf589982688cbde8886768`.
- `polar-G10s-fast-astra-step16-step01-state.json`  `59cc2869802fd526f144fa8b8af7ec0e107ce75ddcd471f479c76b4dce77bd2d`.
- `polar-G10s-fast-astra-step16-G11.json`  `18d576f6cf6279e09e3f64537d724e9125dc170e425fa4d14742153e612a77a8`.
