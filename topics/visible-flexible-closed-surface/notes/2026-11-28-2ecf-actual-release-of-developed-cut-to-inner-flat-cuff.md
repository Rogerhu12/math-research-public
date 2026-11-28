# 将旧开发切圈释放到真实平领内环的两个固定度量解

**数值证据。**

以原材料变量延长实际位置自由区至 T=fl(S+2/5)，旧 S 对应半径 .8 的圆成为内部未知位置。T 的准确半径 r*=4/5+S−T=4503599627370497/11258999068426240，随后到 .32 开平 cuff 的整个原平面环、真喉和两个固定原帽保留。全目标 g 冻结，11 个原对数半径系数仅在原 b..S 生效；S..T 继续使用原准确平尾半径 4/5+S−s。以旧真实场作为初始参考，用两个端口真实位置/速度/加速度构造单位方向修正，生成实际空间场并开放旧切圈所有六 jets。
首个场为 28 个径向 span 和 12 阶角，富集场为 42 个径向 span 和 16 阶角，来自前一实场系数在新方向基上的最小二乘暖启动。两个场分别生成 96 和 128 个物理 Hermite 单元及100/140阶角 Fourier 数据，与真端口按函数拼接。两个新源分别完整计算原 G10 的 4,291,840 行、独立错移 G11，以及位于 .4..8 新释放尾内的额外 193×272 错移网格。表中的初末局部曲率只是采样量，原 2e−9 精度和整闭 reach 尚未支付。

| 实际位置控制数 / 本次接受 | 全 G11 误差 / κ / held | 新释放尾专网误差 / κ / held | 原 .8 切处位置坐标最大变化 |
|---:|---|---|---:|
| 675 / 350 | 0.1833300173 / 9.858531267 / 0.6113266013 | 0.06079850902 / 9.624748952 / 0.8282840669 | 0.10484518 |
| 1353 / 460 | 0.168596075 / 9.714037793 / 0.6172956622 | 0.05712311825 / 9.7218509 / 0.8296808714 | 0.10084185 |

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-developed-cut-to-actual-flat-collar.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --iterations 350 --field polar-released-cut-true-flat40.npz --output polar-released-cut-true-flat40.json
python3 -u "$S/2ecf-polar-released-developed-cut-to-actual-flat-collar.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --design polar-released-cut-true-flat40.json --field polar-released-cut-true-flat40.npz --output polar-released-cut-true-flat40-full.json
python3 -u "$S/2ecf-polar-released-cut-fixed-metric-enrichment.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --start-state polar-released-cut-true-flat40.json --iterations 460 --field polar-released-cut-flat40-enriched.npz --output polar-released-cut-flat40-enriched.json
python3 -u "$S/2ecf-polar-released-cut-fixed-metric-enrichment.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --design polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released-cut-flat40-enriched-full.json --start-state polar-released-cut-true-flat40.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-developed-cut-to-actual-flat-collar.py | 8750e370752632f0ec0f22d5740f251166d8304f1e41112c2e4c15bc7eb73102 |
| 2ecf-polar-released-cut-fixed-metric-enrichment.py | ae9dac39198302b139e5f1d5d8952f40ab8ffcc3e2b5b1ce220c27bb97640442 |
| polar-released-cut-true-flat40.json | 744f80940623ec03feb765cfc5cc42a9a81b38e522baa96e413e7c623140f395 |
| polar-released-cut-true-flat40.npz | 6924d4ade9b7c4e218513264482a75ac2326e74ce8d082e66a8bb6e2dd4dccda |
| polar-released-cut-true-flat40-full.json | 3eca21490fb49d343edc9f2d42d645f0a71a4d091014c32911bf0a859ddab77c |
| polar-released-cut-flat40-enriched.json | 3c1cffcf3225917d49d0524ec2281344df361753789e12ef1c711531682fa448 |
| polar-released-cut-flat40-enriched.npz | eebfc624be640eb288c7c3949a8a274cb98d3cdbdaf02660f193250b63a2195f |
| polar-released-cut-flat40-enriched-full.json | 5d8c09d13c569ef97d087bdea146157aa121fe49bdc71bfae04a9dca93ba86dd |
| polar-released-cut-true-flat40-exit.json | fdbfec55c29af50a4c8d1e1239e89ccad074fdfcf48ee1a42c905b91c3bd8edf |
| polar-released-cut-true-flat40.log | e57fe841c459dc4bd1d1d863bc644a8d56fdc6092377e5730a91d07dc75f1246 |
| polar-released-cut-true-flat40-full-exit.json | 2a1eaddaf203ca7c9c7a92d104efd1e0d7955c1c0b6db8569459e605c84fb6bc |
| polar-released-cut-true-flat40-full.log | 510444f6e8f0d0a1d23aef8cb67b56c01244503628753ed559df756e5b91641c |
| polar-released-cut-flat40-enriched-exit.json | 6f6f7d92289675c8b5cf640479d17de94cebb106ec4a65d6a26033720ac3c735 |
| polar-released-cut-flat40-enriched.log | 6f694a8992271241d2f10488d79bb523900c2ec593e5ef574a4f3b74525508b6 |
| polar-released-cut-flat40-enriched-full-exit.json | 7a5f1eb7277f8a451b297ab7d363005c94135558117476f043bc53af27b36bf8 |
| polar-released-cut-flat40-enriched-full.log | 72db339361665e92159e006feee1cb266906f9f82ff98d2b723f5b740f7492d1 |
