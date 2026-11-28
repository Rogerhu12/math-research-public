# 两个固定度量上的完整实角三维位置修正

**数值证据。**

在原 432 空间场及其真实新双钟上分别增加 4305 个独立位置系数。取 36 个径向五次 span，每个坐标完整保留常数及 1..20 各自 sin、cos。三坐标所有通道独立，35×41×3 个系数在 b..T 开区间改变真实空间位置，两个真端口位置及全两 jets 固定。新钟分支的实际位置增量在复合之后按原材料坐标加入。全部原 13 点行与面积极小值行之外，保护各设计网上实际见证球和远材料两端法向球，并对法向的切向量也完整求导。两个输入各从自己的零增量开始，分别有五次矩阵自由 Gauss–Newton 接受。每轮用原场的近邻包构造远球行并计算两向微分，完整重选下一轮。设计网 145×112，矩阵/转置和实际目标的方向差分均检查。原 G10 及错移 G11、末带均实际重算。

| 固定目标 | 自身接受 | 设计目标 | 独立 G11 误差 / κ / held | 193×272 末带 |
|---|---:|---:|---|---|
| 原固定 g | 5 | 0.014277836 → 0.010063684 | 0.1491166845 / 10.06414905 / 0.6520628855 | 0.09287125618 / 10.13561999 / 0.8495338708 |
| 冻结新 g 及其真双钟 | 5 | 0.011737767 → 0.0082073243 | 0.1421692911 / 10.1642703 / 0.6516104042 | 0.07403988652 / 10.44108034 / 0.8402578538 |

这次增量改变实际空间像，R296、R297 与原真实闭像的非局部结论不能移给成品。第二个解的额外释放尾 κ≈10.44108，超过 1/.096；完整同 g 误差精化仍未到目标。

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-full-angle-physical-position-normal.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-R293-full-angle-4305-original.json --spatial polar-released40-genuine-floor-R293.json --closed polar-released40-genuine-floor-R293-full.json
python3 -u "$S/2ecf-polar-released-full-angle-physical-position-observation.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-R293-full-angle-4305-original-full.json --spatial polar-released40-genuine-floor-R293.json --closed polar-released40-genuine-floor-R293-full.json --perturbation polar-R293-full-angle-4305-original.json
python3 -u "$S/2ecf-polar-released-full-angle-physical-position-normal.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-R293-full-angle-4305-newclock.json --spatial polar-released40-genuine-floor-R293.json --closed polar-released40-genuine-floor-R293-full.json --clock polar-actual-R293-two-clock-scaled-new.json
python3 -u "$S/2ecf-polar-released-full-angle-physical-position-observation.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-R293-full-angle-4305-newclock-full.json --spatial polar-released40-genuine-floor-R293.json --closed polar-released40-genuine-floor-R293-full.json --clock polar-actual-R293-two-clock-scaled-new.json --perturbation polar-R293-full-angle-4305-newclock.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-full-angle-physical-position-normal.py | 2a7da830b64aac03a291fd2ee69e80ceae23b61918cc49e8ce2a6b03bfd571e8 |
| 2ecf-polar-released-full-angle-physical-position-observation.py | 2df7d3e9030318cb3ba9a014be8b1a2618283d8111c8c7072092bf01bed50554 |
| polar-R293-full-angle-4305-original.json | 941c34037fec1b63b3d87557639344a2bf31012139274c94ee68fdbdb0f3f728 |
| polar-R293-full-angle-4305-original-full.json | 8475214c8c2d8e9da88aa8f4e4dee68e4e8e5925702724f956d65ca125aecec6 |
| polar-R293-full-angle-4305-newclock.json | 56004a9aa9fbe0f2990927363532005ef2c47162adf001fb0b444064bfdda14a |
| polar-R293-full-angle-4305-newclock-full.json | 5187d5f6d60bdf80dde119b26340f58e83cdd2756c027ce991740ca9e111335b |
| polar-R293-full-angle-4305-original-exit.json | 2d39d40dd673654ec0b5a5fb7b3cea6e8e4fd615057e4894a211ddef75988d09 |
| polar-R293-full-angle-4305-original.log | 81a8ff26059b1216cc90e81f27db87155fc2b63e968b72f4a1e1ad4926decd05 |
| polar-R293-full-angle-4305-original-full-exit.json | 5b079a5474dca250c98623586fc83b67f28100c3f7f7c1029258001f678081c4 |
| polar-R293-full-angle-4305-original-full.log | be41498f2a54f1b92d5576be672450e72703786230c4dda1e762a5accf2547ee |
| polar-R293-full-angle-4305-newclock-exit.json | e9aaaaae0bb2463f29714339c05898679eb4ceb8508fbbf043631cb3e70d0ad6 |
| polar-R293-full-angle-4305-newclock.log | 1047929cf19cac88f3b8f51d3d85af13fce2081dbb8aa21661c02f924fa10ff9 |
| polar-R293-full-angle-4305-newclock-full-exit.json | 4d5ea0beaa9aed98e0dae7adc310fbbffc430eb285414e52dca69ba3e82ec357 |
| polar-R293-full-angle-4305-newclock-full.log | a77a7fa84025733f1d0ebdff1aa570e221c2025fa855157523994645cd304636 |
