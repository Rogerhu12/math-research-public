# Joint 87-parameter metric design, accepted steps 9–17

**Numerical evidence.** G10 uses 958 physical radii, two angular grids (128 and 192), all 4,291,840 physical residual rows and physical Sobolev damping. G11 independently evaluates 668 radii at 256 shifted angles, including 540 radii outside training. Held is the existing local guide distance (target 0.65). Whole-closed diameter, continuous isometry, global reach and all-time embedding remain open. The strong budget uses whole-closed $D\le 3.2$.

All 87 scalar target-radius coefficients can change along with 12,789 Cartesian coefficients. Every accepted step belongs to this provisional target optimization. Fixed-target accept count is zero.

| own step | R14² | G10 metric / κ / held | G11 metric / κ / held | full normal relative residual | trial lengths (− rejected, + accepted) | solve seconds / peak KiB |
|---:|---:|---|---|---:|---|---:|
| 9 | 0.0102569685104 | 0.165877201 / 35.0593378 / 0.6067514827 | 0.1613340399 / 34.56087981 / 0.6069345343 | 1.477e-13 | −1.0, −0.5, +0.25 | 146.44023 / 523620 |
| 10 | 0.00941343042696 | 0.1650757253 / 31.88027066 / 0.6068815683 | 0.1604416144 / 31.45077093 / 0.6070634776 | 2.898e-13 | −1.0, −0.5, −0.25, +0.125 | 137.10404 / 565356 |
| 11 | 0.0078917049612 | 0.1632033634 / 24.79940485 / 0.6073522954 | 0.1579973058 / 24.80644765 / 0.6075271512 | 1.669e-13 | −1.0, +0.5 | 142.06949 / 566052 |
| 12 | 0.00739825667427 | 0.1627567658 / 41.88740262 / 0.6086738662 | 0.157265541 / 40.76466402 / 0.6088399287 | 5.786e-14 | −1.0, +0.5 | 138.93144 / 566240 |
| 13 | 0.00679207402355 | 0.1621205446 / 21.84433921 / 0.6095102519 | 0.1567792646 / 21.96900931 / 0.6096747794 | 5.101e-14 | +1.0 | 142.89073 / 552264 |
| 14 | 0.0063885657729 | 0.159763707 / 18.73315995 / 0.6095292022 | 0.1545545358 / 18.8478398 / 0.6096936729 | 1.416e-13 | −1.0, −0.5, +0.25 | 194.27871 / 566788 |
| 15 | 0.00588937221609 | 0.1604378965 / 17.27521172 / 0.6100928379 | 0.1553719506 / 17.00050302 / 0.6102547969 | 8.831e-14 | +1.0 | 151.03915 / 566124 |
| 16 | 0.00573800879198 | 0.1581453483 / 13.55293752 / 0.6104247223 | 0.1531340306 / 13.43123981 / 0.6105861599 | 1.827e-13 | −1.0, +0.5 | 173.41249 / 566512 |
| 17 | 0.0056159571193 | 0.1542895117 / 14.64309759 / 0.6118019586 | 0.1493759354 / 14.52397405 / 0.6119607845 | 1.68e-13 | +1.0 | 147.03385 / 566348 |

## Source and output identities

- Step 9 state `c55e142bc421aacb44fd57a111971f1ae3156069c8a169206728c91d50255ae0`, G11 `1312bf90b6e75330afdc7a1cf04e3c0025d5b136b7569eee578476012931fafb`.
- Step 10 state `4821eb2ccc2cb62096913a812cfee7c6222e41729d9ced1b26cad66bc8406730`, G11 `67b6bc1b19e587c3e4be588e78cc8c17189cfeb979fc89f4aeb82d0db11f3e97`.
- Step 11 state `27b00ffa124d96623e8d7f51f2c993166d82f4eee274009e7a62dd49bddb546d`, G11 `e7584c3c2c0bb0a5b49e24ddf65b262beaf274f70a0cd74f127f61988c393e8b`.
- Step 12 state `3978a6243d68fb1c263866539bb6fdb1c05ee4f7815529ec8a9877069f1c195f`, G11 `649e0866fe4bf30c71447113970b2a46c16db2bf543551ed572900de2d4a680f`.
- Step 13 state `bb68ffd2484464e35184201406ff380ec08ed5a6160a506a88a8e32d085018a5`, G11 `9ec7bc2657ad0cd0b80d768fc1c042dc2371a2768cfa2b88685359070a86ec5c`.
- Step 14 state `b8d0710c9b1554bd4177f06365a9e8c955326754abeeb1deee2ae4665cfd66b4`, G11 `cd646fbc828272162f86bca97bbe8213b683f0e047ba7b34de52bbf460506dd1`.
- Step 15 state `bd70cbfbe1257b52b3c5d2f7ef07086985fe9fc02c4bef54f03ae4760ddb2c2d`, G11 `ef361465d142e0fd9a080a70eaed6b9d7571a714064424584cdfb17eceb180bf`.
- Step 16 state `c32dd50ecb9ecfbbb436c0ba01b6a85e2ec9f1eeaffccb90c9ba901c458eec61`, G11 `43813c27b3bfeb8697dc0977e68e0c1cdb44fe1bb69603d6d3aebbdcd3ef9cbd`.
- Step 17 state `0b74a5755c8bfc46b7024f9feeec057465a1d9252bc4a5de4b2a22cb801594b2`, G11 `1c8e35bdbc291e0d7b35a03f76a50f04fc7fc81bc5f574e8419c50c144b17971`.
- Step 9 target |K|, G10 52.7913715, G11 51.281245, audit `4a8421a79c50fb6b89ae492908e588afcc4ab4dc7b7f31655d728d801b5c9f12`.
- Step 10 target |K|, G10 52.7467406, G11 51.2377605, audit `88bce428b4402449fa3f274e037a3cc9f3b508c075d17ce160083443f7194362`.
- Step 11 target |K|, G10 53.1365842, G11 51.6530669, audit `7ea331a7201d7a411ded767df0242178abda1266f8c2ae45b7700e121cfee645`.
- Step 12 target |K|, G10 52.0280806, G11 50.5028807, audit `cea56935951e773f0c5f95316ccfea274c1ab1f3f48dff4c615a1b296350e2aa`.
- Step 13 target |K|, G10 51.5973995, G11 50.0955011, audit `baecbea60b61bc9bd47dcdae3985fdb54b464a12b40fdddaebdc75d8000d706b`.
- Step 14 target |K|, G10 50.9307711, G11 49.4660403, audit `68e94f3f5c9246f4b2973c326719b489183abcdcc38cdd096b168f6cd84f5adb`.
- Step 15 target |K|, G10 50.2071068, G11 48.7824297, audit `23ef1c6f8d7d77d2c0e6cfd23eaf841bdf388419163cecdd4de27e68f99ba14f`.
- Step 16 target |K|, G10 49.9006232, G11 48.4922127, audit `a96462f353cd6ac4959f1f3c74a13ddd7e1c0101568143a694fcc0d355889df4`.
- Step 17 target |K|, G10 49.0148079, G11 47.6552526, audit `ac246c99cd72dd104a984fc062b6b61eb85045f955eefb21dfef3bb2bb4144b4`.

- 2ecf-polar-design-resume-driver.py `26b234cdbaa3a77668e64fbb0e227a5e8d45c28a60083c1b15e82d585f036e12`.

## Reproduction

Use the G10 complete-source/four-baseline recipe, the independent G11 shifted-256 source, and the continuation preceding the first step in this table. Set S to the topic scripts directory and W to the separate run directory containing the preceding states and source masters. Place all cited 2ecf entry scripts in W as in the source recipe. These are the actual inner commands with portable directories. Each succeeded with natural return code 0.

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-step08-step01-state.json --prefix $W/polar-design-G10s-fast-step09 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step09-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step09-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step09-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step09-target-audit.json
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-step09-step01-state.json --prefix $W/polar-design-G10s-fast-step10 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step10-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step10-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step10-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step10-target-audit.json
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-step10-step01-state.json --prefix $W/polar-design-G10s-fast-step11 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step11-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step11-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step11-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step11-target-audit.json
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-step11-step01-state.json --prefix $W/polar-design-G10s-fast-step12 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step12-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step12-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step12-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step12-target-audit.json
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-step12-step01-state.json --prefix $W/polar-design-G10s-fast-step13 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step13-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step13-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step13-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step13-target-audit.json
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-step13-step01-state.json --prefix $W/polar-design-G10s-fast-step14 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step14-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step14-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step14-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step14-target-audit.json
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-step14-step01-state.json --prefix $W/polar-design-G10s-fast-step15 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step15-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step15-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step15-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step15-target-audit.json
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-step15-step01-state.json --prefix $W/polar-design-G10s-fast-step16 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step16-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step16-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step16-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step16-target-audit.json
python3 -u $W/2ecf-polar-log-radius-fast-normal-design-solve.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --normal-audit $W/polar-G10s-sparse-jet-full-normal-audit.json --state $W/polar-design-G10s-fast-step16-step01-state.json --prefix $W/polar-design-G10s-fast-step17 --steps 1
python3 -u $W/2ecf-polar-c2-independent-g11-resume-observe.py observe --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step17-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step17-G11.json
python3 -u $W/2ecf-polar-log-radius-target-audit.py --scripts $S --prepare-entry $W/2ecf-polar-c2-g10-split-prepare.py --prepared $W/polar-c2-G10s-prepared.json --state $W/polar-design-G10s-fast-step17-step01-state.json --observer $W/polar-independent-G11r-shifted256-independent.json --output $W/polar-design-G10s-fast-step17-target-audit.json
```
