# 十八个真实平领抬高及互补短喉输入

**数值证据。**

以 R290 双球场和前条远法球场为两个物理底图，在 b..T 上增加 Δ·S5((t−t0)/(t1−t0)) e_z，t=(s−b)/(T−b)，阶跃在两端截断。所有六 jets 使用该位置的真导数；T 后的完整平盘提升 Δ，真实新喉取 Z=.415+Δ、η=.115−Δ、L=8η/(3π)。故固定凸帽位置和十个固定标记保持，喉母线与其共同度量真正变更。每次端位和两 jets 都按新场匹配。冻结 b..T 原连接度量，完整重算 G10/G11、额外释放尾 193×272；几何高度窗口取真 Z 及额外 .113−Δ。
另在 113×96 的整个上连接加完整平环的 11 个内圈上，对 s 差至少 .32 的实际近对重建列表，表列该有限近对的双向最小法球比，尚需包含帽与全部相位的连续证明。直接生成这些新输入没有优化器接受。

| 位置底图 | 阶跃范围 t0..t1 | Δ | 全 G11 误差 / κ / held | 远端采样法球比 |
|---|---|---:|---|---:|
| 双球 | 0..1 | 0.04 | 0.1588316505 / 10.20970977 / 0.6602944616 | 0.086255219 |
| 双球 | 0..1 | 0.06 | 0.2207086642 / 10.44309738 / 0.6632692631 | 0.095303167 |
| 双球 | 0..1 | 0.08 | 0.2871261719 / 10.6742895 / 0.6662272458 | 0.10454002 |
| 双球 | 0..1 | 0.09 | 0.3214709177 / 10.79502517 / 0.6677017649 | 0.1090845 |
| 双球 | 0.38..0.94 | 0.04 | 0.1566625159 / 10.3023012 / 0.6543040235 | 0.08670285 |
| 双球 | 0.38..0.94 | 0.06 | 0.2124923394 / 10.93254104 / 0.6543046607 | 0.095998358 |
| 双球 | 0.38..0.94 | 0.08 | 0.2973675175 / 11.58527182 / 0.6543052979 | 0.10541508 |
| 双球 | 0.38..0.94 | 0.09 | 0.3417554403 / 11.90465772 / 0.6543056165 | 0.10553347 |
| 双球 | 0.52..0.94 | 0.04 | 0.1926534776 / 10.80331075 / 0.654302749 | 0.086672254 |
| 双球 | 0.52..0.94 | 0.06 | 0.2655751066 / 11.55528902 / 0.654302749 | 0.095950165 |
| 双球 | 0.52..0.94 | 0.08 | 0.3367697111 / 12.44912688 / 0.654302749 | 0.10534929 |
| 双球 | 0.52..0.94 | 0.09 | 0.3691313939 / 12.90083927 / 0.654302749 | 0.10553347 |
| 远法球 | 0..1 | 0.02 | 0.2098130702 / 11.01547587 / 0.6565843624 | 0.099500153 |
| 远法球 | 0..1 | 0.04 | 0.2122194505 / 10.99126816 / 0.6591572098 | 0.10835971 |
| 远法球 | 0.38..0.94 | 0.02 | 0.207476764 / 11.03974362 / 0.6539706607 | 0.099569439 |
| 远法球 | 0.38..0.94 | 0.04 | 0.207476764 / 11.03974362 / 0.6539706607 | 0.10530181 |
| 远法球 | 0.52..0.94 | 0.02 | 0.207476764 / 11.03974362 / 0.6539706607 | 0.099569439 |
| 远法球 | 0.52..0.94 | 0.04 | 0.223311005 / 11.03974362 / 0.6539706607 | 0.10530181 |

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-moving-actual-flat-cuff-and-throat.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-moving-flat-hard.json --solution polar-released40-actual-cartesian-hardspheres.json
python3 -u "$S/2ecf-polar-released-moving-actual-flat-cuff-and-throat.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-moving-flat-normal.json --solution polar-released40-true-far-retry-ball.json --deltas .02 .04
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-moving-actual-flat-cuff-and-throat.py | 5840ba689318e8878980b897c4910654c91adf8d4540e36ab1f70a8b74af6ae2 |
| polar-released40-moving-flat-hard.json | 89fbc0357d178fe003d17f794037fba4feb29472b0ae462e49e6c3199c470f51 |
| polar-released40-moving-flat-normal.json | a10da0502dbb3290c345446f39a260110dbf020bd7d17a9aec8f1ac3cd2a6612 |
| polar-released40-moving-flat-hard-exit.json | 11c3c80637bbc83d865286769222c14d5451557675ad0829ea7ffffefdd28a0f |
| polar-released40-moving-flat-hard.log | 689b87f01961fb60c6f9f825959463a56475080ce43605bb99545eb36956d0b1 |
| polar-released40-moving-flat-normal-exit.json | f6704ef20002230799ecb5cb3c6f6feb4d1b58a932717ea910ddc5bf9c9d496e |
| polar-released40-moving-flat-normal.log | 6e560a1ed1843ddb851df229f3645e366c86271bfa2a7f20066d7f3d2bf409ab |
