# 释放平领图上的两个真实径向度量系数与冻结加密

**数值证据。**

在保持真实两端和新释放内段的条件下，另设径向速度和圈半径两组正系数。令 L=T-b，在相同材料 s 上把目标置为 exp(2a(s))ds²+f_old(s)²exp(2h(s))du²，a,h 为五次开 B-spline 径窗，各端三列夹持；两端和外部回到同一入口、开平领和真实帽目标。在真实弧长坐标中将二阶子午速度换成 exp(−2a)(Xss−a′Xs)，混合速度亦乘 exp(−a)，完整曲率、面积和全部 13 点行按这个目标重算。空间曲率作为几何量在此坐标换算下保持。

第一输入有 320 个实际位置/目标参数，自身 900 次接受。新目标散列 6c4684fc4d37f5d026ce67ad1c3c5b2953b6baf1e40507778c7a4d38a106493d，完整独立 G11 误差 / κ / held 为 0.1302183616 / 9.784665794 / 0.6541094034。随后精确冻结两个径窗的全部系数，另在 24 span、9 角阶、690 真实位置控制下做 1000 次接受。G11 为 0.1334862064 / 9.719701142 / 0.6544264538；原 G10 平方和虽下降，独立点峰略升。严密全图法管与原目标完成精度仍待。

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-true-two-radial-target-design.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-physical-metric-joint.json --warm polar-released40-actual-cartesian-hardspheres.json
python3 -u "$S/2ecf-polar-released-true-two-radial-target-design.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-physical-metric-joint-full.json --warm polar-released40-actual-cartesian-hardspheres.json --solution polar-released40-physical-metric-joint.json
python3 -u "$S/2ecf-polar-released-true-two-radial-target-design.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-physical-metric-joint-frozen.json --warm polar-released40-physical-metric-joint.json --fixed-metric --spans 24 --modes 9 --angles 112 --radials 165 --iterations 1000
python3 -u "$S/2ecf-polar-released-true-two-radial-target-design.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-physical-metric-joint-frozen-full.json --warm polar-released40-physical-metric-joint.json --solution polar-released40-physical-metric-joint-frozen.json --fixed-metric --spans 24 --modes 9 --angles 112 --radials 165 --iterations 1000
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-true-two-radial-target-design.py | 7bc064a2db6b2762dee4d86d8a8fe4dca38c0bdd3e82148dc06b96ffe0fe2d08 |
| polar-released40-physical-metric-joint.json | 71a4d8a9ee798ae4c353729cee93b1de04afaf9dc71661feeb28f172dca978c0 |
| polar-released40-physical-metric-joint-full.json | 91c61291b93ecea87d8d75d546b787dcf5a0108a66be337609947c9d98855206 |
| polar-released40-physical-metric-joint-frozen.json | 96a53a5145fb81e2b39dde4b9616635e65c34558f16964c2531817037f94eb17 |
| polar-released40-physical-metric-joint-frozen-full.json | af3a98c5fb30f850e25e4d415e13ef95059c43c9aa44f12ae4780a8e9ce8e96f |
| polar-released40-physical-metric-joint-exit.json | a760346ee0519ade85ce97e92d36756391052eb47d407858fc2a07faaa764930 |
| polar-released40-physical-metric-joint.log | 39f6af765a9bcab1f1e2d9d7428628abffbcffa64ff09081cef8ae1d15b4d118 |
| polar-released40-physical-metric-joint-full-exit.json | 2b30ad0a003b8e20989a70f5bbf83b3e97815e85d21a4973e98b0eb7ec978eb2 |
| polar-released40-physical-metric-joint-full.log | 8693610b556275df2f11c0249d4e8ad040df449eccc75ac161688ade5bc84980 |
| polar-released40-physical-metric-joint-frozen-exit.json | 41939ac3b44bb77f18854c4b8349ba9b71bf0f04a969c14550110251d404025e |
| polar-released40-physical-metric-joint-frozen.log | f98eb64e8ff9eb7027ad6d7eb269b26b2ae3b59bab708a5cabf2b23fa8610bd9 |
| polar-released40-physical-metric-joint-frozen-full-exit.json | 57f939d9acf2f514427ade5e95a68c3e9556a80e45547d2e390e2a5b33fb9cda |
| polar-released40-physical-metric-joint-frozen-full.log | d45bb47ab018d2864392294f8b6c63ec88d7a6a0c1d7b70e051dd01aea2f0df8 |
