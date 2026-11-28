# 间隙 23/25 的完整极坐标后缀和两端口

**数值证据。**

在不同几何之间显式接入整个新后段。b 左侧使用新中央、完整 raw H65 图及新 Γ95 coast。coast 原长度 ell 的准确终点接入 literal b，采用 R261 的极小五次材料重参数化，保持出口两 jets。b..S 的准确位置定义为 R265 原 polar 图加两端五次 Hermite。其左端 P,V,A 均取“新准确 Γ95 出口减原准确 Γ95 出口”的差，其右端三个差为零。对角导数使用同一 Hermite 权线性作用于 P_u,V_u,A_u 及 P_uu,V_uu,A_uu。因该加法与角微分可交换，b、S 的六个 jets 按函数精确接合。G10/G11 通过各自实际 literal 原底场和两份数值 coast 端口重算。没有把准确源与 literal 采样的逐点误差默认为零。独立全网格在 cut 之后逐字节等于原 tail。
该新设计的标量半径从准确上下文中的原 f 出发，在 b 左加两组 dyadic 中央椭圆的准确均半径差，在 b..S 用左端值基函数 H00(t) 乘同一差，S 之后消失。程序以 75 位小数求用于有限缓存的差，值为 9.07363707614594e-17。两条完整真帽及其平 collar、cuff 高度与原来相同。全域非局部 reach 以及含后缀的畸变需要重付。

| 真采样 | 新前缀 metric 峰 | 新前缀 κ 峰 |
|---|---:|---:|
| training | 4.06763511851e-11 | 7.47424990676 |
| observer | 4.06763511851e-11 | 7.47424990676 |
| independent | 3.80141232842e-11 | 7.47348605874 |

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-new-central-gap-compose.py" --scripts "$S" --master polar-new-gap-092-master.json --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --old-ramp "$E/ramp-65.npz" --old-coast gap105-prefix-coast-master.npz --parent-prepared polar-physical-H65-prepared.json --parent-observer polar-physical-H65-independent.json --prefix polar-new-gap-092
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-new-central-gap-compose.py | a0b1b29da63ea54272eb4339bdc1487a2e76013e3c56799f25492da60708e844 |
| polar-new-gap-092-prepared.json | b6fbe1c1fe87cd62ee230e3317512566d6d3b3ab45f9bf6d6fec3f997e7ad13f |
| polar-new-gap-092-independent.json | 04d7b710a06d00526d42b77268c4973fa166666643eb4ebe977ee4ce87c8204b |
| polar-new-gap-092-training-source.json | 187f90fb1233386dc1be5b85af900c083a30559a81edd1f7872b2de548ced315 |
| polar-new-gap-092-training-jets.npy | 31730d25b766f2091a1362e025d35572d4555d7469f452f12004d288a17d8071 |
| polar-new-gap-092-training-radius.npy | 457f9d4c197254ef2406c635a56c88031fb600f56ef850ae71ad0bd837f1d00c |
| polar-new-gap-092-observer-source.json | f9d022a6f43194b2ca593dc15134777f73d03fd942b530cc491fb6a94a38d2af |
| polar-new-gap-092-observer-jets.npy | 930b13602a0931c21f6a303230a34c7e9cab9cd53011d41b37fbb5c4cfe6c284 |
| polar-new-gap-092-observer-radius.npy | 457f9d4c197254ef2406c635a56c88031fb600f56ef850ae71ad0bd837f1d00c |
| polar-new-gap-092-independent-source.json | b894f696fef4ee4e44d0542375f9016d9512cd270c3b8d4932b9c400ce7e46b8 |
| polar-new-gap-092-independent-jets.npy | 250487c4912f755c2f640cd5f503ae9ee43c34d2534a59f6602f87e47c4cd08d |
| polar-new-gap-092-independent-radius.npy | 657aa05c74488b63c0e0f79b2d43afd82eab5b6b3c7bbab6e5f915ae929548f9 |
| polar-new-gap-092-compose-exit.json | cae320e360b17c26bc6a51c902618b29c2b1816732306eb12856353a7d1703b0 |
| polar-new-gap-092-compose.log | 75c9a25a652fdc9c6bc02bfb4c0ef90c8df12d54edf9dfa8f1e267e4e5adfe93 |
