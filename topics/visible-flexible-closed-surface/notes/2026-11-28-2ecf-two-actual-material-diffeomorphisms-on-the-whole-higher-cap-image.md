# 完整新帽曲面的两个真实材料微分同胚与各自的度量误差

**数值证据。**

取 R296、R297 同一张真实 432 系数闭曲面，在 b..T 施加二维材料映射。以 t=(s−b)/(T−b)，两钟为 (t+H(t,u),u+K(t,u))。H 用常数及偶频余弦，K 用偶频正弦；16 个径向五次 span 删除三行两端控制。225 个材料参数独立调节，其位置、一导、二导均在两端接回恒等。第一组固定整域原 g。第二组同时设计 30 个对数径速与对数周长系数，完成后固定完整新 g。首试无缩放 L-BFGS 在恒等处记录一次零移动；两正式行将参数实际尺度改为 .0125。优化时用 385×256 的内禀张量三次插值，每个成品的全原行另用 141 个实际位置频率、432 个真实 B-spline 控制及两真端迹逐点在移动后坐标重算六 jets，带二阶链式法则。G10 原 4,291,840 行、独立 G11 及末段加密网分别消费。
两场确为全域微分同胚。对每个方向，五次 B-spline 凸包与端点填零后的相邻系数差给出 t 导数界；u 导直接将每个模乘频率并向外求和。表中下界精确有理求得：若 (A,B,C,D) 依次包住 |H_t|、|H_u|、|K_t|、|K_u|，则 det≥(1−A)(1−D)−BC>0，另有 A<1、D<1。两端固定，t+H 随 t 严格增加，整个输入柱面映到闭柱面。内部为 proper 的局部微分同胚，边界恒等且两函数周期，映射度一，覆盖层数一。故每一相位恰有原空间闭像，逐材料点固定的两帽、R296 两强距离和 R297 整体曲率结论都继承。误差取相应材料目标与实际完整映射计算。

| 目标 | 自身迭代 | 全域行列式下界（近似显示） | 独立 G11 误差 / κ / held | 193×272 末带 |
|---|---:|---:|---|---|
| 原固定 g | 99 | 0.8284939816 | 0.1530104699 / 10.02546252 / 0.6536438625 | 0.1158116093 / 10.25674211 / 0.8524850133 |
| 新径速及周长设计 | 470 | 0.7574555749 | 0.1469587494 / 10.16349614 / 0.6536454281 | 0.1012679067 / 10.24559574 / 0.8440658059 |

新目标身份为 4c6ac22b27307ce9a45825e0247516ab19d2a7ebecd07590977ec70f04c4a21e；原冻结目标身份为 f39bfa22b563e751b641b67d8933206091921b6f3e33e73755405d64dcf4b8ee。独立网使用实际对称归一 Gram 差的算子范数。两场均待精化到同 g 精度。

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-material-physical-two-clock-design.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-actual-R293-two-clock-fixed.json --spatial polar-released40-genuine-floor-R293.json --closed polar-released40-genuine-floor-R293-full.json
python3 -u "$S/2ecf-polar-released-material-clock-scaled-physical-step.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-actual-R293-two-clock-scaled-fixed.json --spatial polar-released40-genuine-floor-R293.json --closed polar-released40-genuine-floor-R293-full.json
python3 -u "$S/2ecf-polar-released-true-irregular-material-clock-observation.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-actual-R293-two-clock-scaled-fixed-true-full.json --spatial polar-released40-genuine-floor-R293.json --closed polar-released40-genuine-floor-R293-full.json --clock polar-actual-R293-two-clock-scaled-fixed.json
python3 -u "$S/2ecf-polar-released-material-clock-exact-diffeomorphism.py" --clock polar-actual-R293-two-clock-scaled-fixed.json --output polar-actual-R293-two-clock-scaled-fixed-exact-diffeo.json
python3 -u "$S/2ecf-polar-released-material-clock-scaled-physical-step.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-actual-R293-two-clock-scaled-new.json --spatial polar-released40-genuine-floor-R293.json --closed polar-released40-genuine-floor-R293-full.json --new-target
python3 -u "$S/2ecf-polar-released-true-irregular-material-clock-observation.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-actual-R293-two-clock-scaled-new-true-full.json --spatial polar-released40-genuine-floor-R293.json --closed polar-released40-genuine-floor-R293-full.json --clock polar-actual-R293-two-clock-scaled-new.json
python3 -u "$S/2ecf-polar-released-material-clock-exact-diffeomorphism.py" --clock polar-actual-R293-two-clock-scaled-new.json --output polar-actual-R293-two-clock-scaled-new-exact-diffeo.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-material-clock-scaled-physical-step.py | b53f54b8ef3dd14a5160d7c18fec38480343748e79499dc658e4b4510e194ef5 |
| 2ecf-polar-released-true-irregular-material-clock-observation.py | 07af03fb1112e39c91a99d9b8630909e67b0b8529c1c0a60b72695e0fdc56f99 |
| 2ecf-polar-released-material-clock-exact-diffeomorphism.py | 3a853cfdff62be8b5a3fc6e73f90e69d13332bde1047e0feb0cd419bf0649a17 |
| polar-actual-R293-two-clock-fixed.json | 364a11f9adbf0e64238c27aa415fde9f80d41c2e030f3c0ba8fc92eb01458fa4 |
| polar-actual-R293-two-clock-scaled-fixed.json | fa1d8d646faf7cf2d04caedd381442da4d97c5e4471ffb006123ca257e2fd413 |
| polar-actual-R293-two-clock-scaled-fixed-true-full.json | 9ee527c01f7d21050b6385c2b9804cd8175f9903e43e8ab577a8eb49fe91dbd0 |
| polar-actual-R293-two-clock-scaled-fixed-exact-diffeo.json | 1e6ca8d459a6f302f99cc830f808c636fea3a000f8ac04fcd14223a56deaaf5c |
| polar-actual-R293-two-clock-scaled-new.json | fd46045da330beb3d4c26cc1c76e5cd88cca72ceb875cae333ce7adb98873542 |
| polar-actual-R293-two-clock-scaled-new-true-full.json | 3a5d28221d5e8d7a6613d6e9044214e70af5d6cbb9f6138f03189d38f43b6562 |
| polar-actual-R293-two-clock-scaled-new-exact-diffeo.json | 85be15347c6f9af69256f750020d140b109f9ec16b956b297f2cdbe53d422ea0 |
| polar-actual-R293-two-clock-fixed-exit.json | db6c6ef8b5aa7f9a5c8d680252079d7739cd058565917a6a2c7021996a1d6c6d |
| polar-actual-R293-two-clock-fixed.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| polar-actual-R293-two-clock-scaled-fixed-exit.json | b034337ba6beeb964dc740b8e597c60ed0871474eac2c5a68712b4f5e42b0d5a |
| polar-actual-R293-two-clock-scaled-fixed.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| polar-actual-R293-two-clock-scaled-fixed-true-full-exit.json | 895d87c567a94946b34009948045f4be1533922cd8433b25a3985b62a9086af8 |
| polar-actual-R293-two-clock-scaled-fixed-true-full.log | e9c67ed95914cc2b11513cfbb00c3590a2412b0004db21657121d7151590f2fa |
| polar-actual-R293-two-clock-scaled-fixed-exact-diffeo-exit.json | e8733a823791ecfa63232bd79297b97e6bd9b4b96a48a9a7c5c6afc07b55541c |
| polar-actual-R293-two-clock-scaled-fixed-exact-diffeo.log | e73764088ac301cf24244a67b256eaef520cb813d3419e49cce6b4be929d429a |
| polar-actual-R293-two-clock-scaled-new-exit.json | 48cec43f68091ceb5fcb08a14713773ee3c873247e7fafb15781038660eb78ab |
| polar-actual-R293-two-clock-scaled-new.log | 4872f5c22dc8669c9396a6244b985f7ac6863514da44046933a9c996bdeadec3 |
| polar-actual-R293-two-clock-scaled-new-true-full-exit.json | 3f2489055ebc5aef38dec88ef7a149a547dcd56827bd679c037118760b74ba37 |
| polar-actual-R293-two-clock-scaled-new-true-full.log | 949355e7f4c65a62958ab878a8a727bef0c446f0a8b617509c7541efab59aee0 |
| polar-actual-R293-two-clock-scaled-new-exact-diffeo-exit.json | 5e4c3ab314a6c05c8ee6bdca652fb913bee2866321d3aedc493624841b407ff9 |
| polar-actual-R293-two-clock-scaled-new-exact-diffeo.log | f34a52bcfbb08475a60df4ef3f379c2e13d36c5417b76fcf5babdaf2d2cf05e9 |
