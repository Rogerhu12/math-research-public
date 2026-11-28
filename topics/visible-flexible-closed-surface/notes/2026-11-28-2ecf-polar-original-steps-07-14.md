# Original fixed metric, complete fast assembly and accepted steps 7–14

**Numerical evidence.** G10 uses 958 physical radii, two angular grids (128 and 192), all 4,291,840 physical residual rows and physical Sobolev damping. G11 independently evaluates 668 radii at 256 shifted angles, including 540 radii outside training. Held is the existing local guide distance (target 0.65). Whole-closed diameter, continuous isometry, global reach and all-time embedding remain open. The strong budget uses whole-closed $D\le 3.2$.

Original target fixed, 12,789 Cartesian columns. Steps 7–8 used the original normal assembly. Step 9 retained the complete field, target and all cross terms under the sparse angular contraction, after reproducing the previous objective. Counts 1–8 occurred only once.

| own step | R14² | G10 metric / κ / held | G11 metric / κ / held | full normal relative residual | trial lengths (− rejected, + accepted) | solve seconds / peak KiB |
|---:|---:|---|---|---:|---|---:|
| 7 | 0.107274626593 | 0.381950754 / 186.2847277 / 0.7216880782 | 0.3782505966 / 185.3018876 / 0.7218281092 | 1.172e-14 | +1.0 | 349.60928 / 571740 |
| 8 | 0.077215748905 | 0.3434564686 / 104.3166501 / 0.7210926576 | 0.3387274084 / 103.3465843 / 0.7212213284 | 1.357e-14 | +1.0 | 315.40896 / 551560 |
| 9 | 0.049487680473 | 0.3112862796 / 77.67442029 / 0.7216303936 | 0.3085560083 / 76.21099022 / 0.7217700381 | 1.788e-14 | −1.0, +0.5 | 177.18661 / 490208 |
| 10 | 0.0285221646356 | 0.2302798834 / 47.85890736 / 0.7208036171 | 0.2281301005 / 47.17068291 / 0.7209587195 | 2.217e-14 | +1.0 | 154.14224 / 475192 |
| 11 | 0.0278182662418 | 0.2231182926 / 43.41762869 / 0.7211090475 | 0.2210043423 / 42.78466968 / 0.721262969 | 4.418e-14 | −1.0, −0.5, −0.25, +0.125 | 128.49331 / 486292 |
| 12 | 0.0275720833062 | 0.2134962922 / 71.85208733 / 0.7231724242 | 0.2089741813 / 70.26208688 / 0.7233137864 | 1.733e-14 | +1.0 | 178.11415 / 499404 |
| 13 | 0.0271586913919 | 0.2132943489 / 64.53628788 / 0.723245332 | 0.2076212329 / 63.08099201 / 0.723386727 | 3.953e-14 | −1.0, −0.5, −0.25, +0.125 | 152.43371 / 498636 |
| 14 | 0.0269206651904 | 0.2184943351 / 48.66463081 / 0.7237364962 | 0.2127421876 / 47.02782995 / 0.7238793437 | 1.72e-14 | +1.0 | 126.98542 / 478560 |

## Source and output identities

- Step 7 state `a2105ebc2d31abf37b9bc1b1bf6aaab1bc43464d1d802c299d1d86706f2eb647`, G11 `9548ea7678ae82caa9887cf77ac5859bb376a145a6d99102ecc041b3f55d8494`.
- Step 8 state `fecd97c8d313ca201fe80bb4da67e7a309d25e5d4ac3cf809955696c3d95cfc3`, G11 `fa172a978cd0562f7b6d8203101e48cb31c391e16f32a047abeb7fad6bb33784`.
- Step 9 state `a5847aaf54086dab3b8f8700e16751a74441c094d2ba6d8eb6410769c62c2093`, G11 `2c75e1f2737785b5e70913922e795184b69d5d8e02f9abffefe7b5a675c0f754`.
- Step 10 state `caaac16be9567e6584797d0831c2384298bde8932a5f592840c20c7d966bb80d`, G11 `79e4df817839675f15f221d6144d708c7a59afea90e1e042be19acf95a9e62ed`.
- Step 11 state `3b48aa2198acb4a949752d72560c9d3480d0e2b0e11f0524b6b06a122bbf4ba6`, G11 `f61d2631b53fe0b68fbe22100e69910fd20d7567364bc11da6df923eb445be69`.
- Step 12 state `cd6fd5aac1a6045008feff74d5723813f2ec554a3ebafee24d51aed07ae407e6`, G11 `f24ebb15ad1246045be8a60b0287a2447684a4c727f6adb274220a7ae19bda0f`.
- Step 13 state `79f8f028e7db386b1cc5cb4abe80b0cfa808088a9303f06a05bd0f2306696a6d`, G11 `7a76a40230a8c39b39074a2537a331ea23c3a801396b45c57d2664e718d37fae`.
- Step 14 state `c66ae970d4e6fa2ab1886c18a22a9bcf77eccb5d4f0c719eb82336829a5f3c15`, G11 `2da9fa323982f9796e8ff4213bab9b6c711f0df1b74370365a665468c8d0f40a`.

- 2ecf-polar-c2-g10-fast-solve.py `7436c31cce61b8e1ff4a827b8ddfbcdcc7eed833c87d126fd127de598f3ca7b1`.
- 2ecf-polar-fixed-metric-resume-driver.py `ab93b3d16ae321a1558a78b79d226c7a578c720df594b9bd1d4482e86296157f`.

## Reproduction

Use the G10 complete-source/four-baseline recipe, the independent G11 shifted-256 source, and the continuation preceding the first step in this table. Set S to the topic scripts directory and W to the separate run directory containing the preceding states and source masters. Place all cited 2ecf entry scripts in W as in the source recipe. These are the actual inner commands with portable directories. Each succeeded with natural return code 0.

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
python3 -u $W/2ecf-polar-c2-g10-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-step06-step01-state.json --prefix $W/polar-G10s-step07 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-step07-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-G11r-G10s-step07.json
python3 -u $W/2ecf-polar-c2-g10-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-step07-step01-state.json --prefix $W/polar-G10s-step08 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-step08-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-G11r-G10s-step08.json
python3 -u $W/2ecf-polar-c2-g10-fast-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-G10s-step08-step01-state.json --prefix $W/polar-G10s-fast-step09 --steps 1 --initial-damping 0.0001
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-fast-step09-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-G10s-fast-step09-G11.json
python3 -u $W/2ecf-polar-c2-g10-fast-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-G10s-fast-step09-step01-state.json --prefix $W/polar-G10s-fast-step10 --steps 1 --initial-damping 0.0001
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-fast-step10-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-G10s-fast-step10-G11.json
python3 -u $W/2ecf-polar-c2-g10-fast-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-G10s-fast-step10-step01-state.json --prefix $W/polar-G10s-fast-step11 --steps 1 --initial-damping 0.0001
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-fast-step11-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-G10s-fast-step11-G11.json
python3 -u $W/2ecf-polar-c2-g10-fast-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-G10s-fast-step11-step01-state.json --prefix $W/polar-G10s-fast-step12 --steps 1 --initial-damping 0.0001
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-fast-step12-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-G10s-fast-step12-G11.json
python3 -u $W/2ecf-polar-c2-g10-fast-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-G10s-fast-step12-step01-state.json --prefix $W/polar-G10s-fast-step13 --steps 1 --initial-damping 0.0001
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-fast-step13-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-G10s-fast-step13-G11.json
python3 -u $W/2ecf-polar-c2-g10-fast-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-G10s-fast-step13-step01-state.json --prefix $W/polar-G10s-fast-step14 --steps 1 --initial-damping 0.0001
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-G10s-fast-step14-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-G10s-fast-step14-G11.json
```
