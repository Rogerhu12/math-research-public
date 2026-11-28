# 同一释放平领场的双球距离与局部曲率实际求解

**数值证据。**

冻住前条 42 span、16 阶球向富集场和原 11 半径系数目标 g。在这个真位置上叠加 216 个实际三维 Cartesian 位置系数：径向五次开 B-spline，13 span，各端删三列；x 用奇次余弦、y 用奇次正弦、z 用偶次余弦，分别六项。整个 b..T 可变而两个切口的全部两 jets 准确夹持，内环至真实 .32 平领、两真喉及固定帽接合保留。先用两球距离平方正部在设计网的物理距离损失配合全部 14 条原行，之后提高两球权重和导向半径，分别记录两个输入各自的真实 L-BFGS 接受。外部完整 G10 和独立 G11 均使用原物理行。

| 设计排球半径 / 权重 | 自身接受 | G10 训练 误差 / κ / held | 完整 G11 误差 / κ / held | 新释放尾 193×272 |
|---|---:|---|---|---|
| 0.6535 / 4000.0 | 523 | 0.1564153551 / 9.828149253 / 0.6430022836 | 0.1557242532 / 9.877123085 / 0.6431536161 | 0.06948827347 / 9.829267485 / 0.8560825262 |
| 0.6547 / 750000.0 | 456 | 0.1573249844 / 9.84200912 / 0.6541647912 | 0.1566625159 / 9.898687846 / 0.654302749 | 0.07928343881 / 9.837893231 / 0.8685509217 |

第二场在完整独立 G11 上同时给出 held>.6543 与 κ<9.899；该场高度 guide 的 G11 最大超额 .042695，度量误差仍大于 .15。局部采样量没有支付不同材料区之间的法球。第一场系数为第二场暖启动；第二场存储全部 216 个最终系数，直接加到前条富集场 NPZ 的 Fourier–Hermite 位置。无需将两个修正系数相加。

## 可移植重生

W 含前条富集场、冻结 11 半径状态、真实 G10/G11 和 gap .92 两个 master；S 是课题 scripts 的绝对路径。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-actual-cartesian-guarded-design.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-actual-cartesian-guarded.json
python3 -u "$S/2ecf-polar-released-actual-cartesian-guarded-design.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-actual-cartesian-guarded-full.json --solution polar-released40-actual-cartesian-guarded.json
python3 -u "$S/2ecf-polar-released-actual-cartesian-guarded-design.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-actual-cartesian-hardspheres.json --start polar-released40-actual-cartesian-guarded.json --held .6547 --guard 750000 --iterations 750
python3 -u "$S/2ecf-polar-released-actual-cartesian-guarded-design.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-actual-cartesian-hardspheres-full.json --solution polar-released40-actual-cartesian-hardspheres.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-actual-cartesian-guarded-design.py | 0170e240baee1af32dbb497ca809b3a2f6e5e60008ae48efdebd8ba31b61c504 |
| polar-released40-actual-cartesian-guarded.json | b5cd1874206fffbf8f2ac455a30c4d76c79bcaba60bccbba55aefe94bb5090f2 |
| polar-released40-actual-cartesian-guarded-full.json | 54e56bbe2bdfbe23378ac3512886b6f45a624097cdf4177246ff3bdf95b5057b |
| polar-released40-actual-cartesian-hardspheres.json | d8a7affa67b13a53b4d3108cefe04af361828d37a6c44d4975e0854bb4320061 |
| polar-released40-actual-cartesian-hardspheres-full.json | 92b565f85f52d28cf51f49f5ca2a2db4a258f7d9d061315aaddfde07d3b4c964 |
| polar-released40-actual-cartesian-guarded-exit.json | 1897e778ae3fe0379b9c0903e03734bc246af616ed133d7d84b81c11781cc489 |
| polar-released40-actual-cartesian-guarded.log | 1b69761241c169291e63cd6e3c92a3deb79fe6bf88a059027f285bf83e57d22d |
| polar-released40-actual-cartesian-guarded-full-exit.json | b0ae0acc3da5c7718a78eb4ba58267c6a53f67907e7fea93582ecf863fba9b93 |
| polar-released40-actual-cartesian-guarded-full.log | 22c2bd07846a7839b69810d914d1c9dd0025bad345cdfed8dae7a6dfe76d1c9a |
| polar-released40-actual-cartesian-hardspheres-exit.json | 6c8c9a69eccb7c6119e575b67fd9b74e3302e7d490a17c025b357efd091714f0 |
| polar-released40-actual-cartesian-hardspheres.log | c3e12df8ab8de00ccca675720f7d7d1d1aee54e3fdd329e84f07c6b400ffb1a2 |
| polar-released40-actual-cartesian-hardspheres-full-exit.json | bf9e8ea751aa1e87e78461192875465df4dcb308bb8a5ec19b427d3c01c42d8b |
| polar-released40-actual-cartesian-hardspheres-full.log | 5817c70db2856ca3694df50b57caf05d578eb2bc15cccf52a9028256a4a855fc |
