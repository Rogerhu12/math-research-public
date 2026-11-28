# 真实新平领高度及远层约束下的 408 个空间位置

**数值证据。**

在释放的整材料 b..T 上选择 Δ=存储的 .065，Z=83/200+Δ、η=53/100−Z，连接底图用 128 个物理 Hermite 格和 141 个非负 Fourier 频，另加准确阶跃 Δ S5((s−b)/(T−b))e_z。外平环、实际短喉和整固定原凸帽保留。以此前双球物理场的 216 个系数投影为新暖启动，18 span、每个空间方向 8 个角频给 408 个位置数。冻结这张真闭材料上的 g，其中喉用新 η 的实际母线度量；在所有原 14 行、真实 held 与两向归一法球罚下做三个权重阶段，各自 300 次接受，返回同一个 408 系数向量。
完整 G11 的误差 / κ / held 为 0.151632472 / 9.917385059 / 0.6520683618；额外 193×272 新尾内网为 0.09461218494 / 10.39378495 / 0.8482870542。设计网远区重新搜索得到最小法球比 0.10074107429036916，局部尾网仍有 κ>1/.097。首次存档存在临时路径退出错误，另一次 .08 同类较大进程受 signal 9 未生成状态。这里使用上述明确完成的 .065 输入。

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-higher-cuff-true-spatial-design-checkpoint.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-optimized-higher-v2-065.json --radials 111 --angles 72 --start polar-released40-actual-cartesian-hardspheres.json --delta .065
python3 -u "$S/2ecf-polar-released-higher-cuff-true-spatial-design-checkpoint.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-optimized-higher-v2-065-full.json --solution polar-released40-optimized-higher-v2-065.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-higher-cuff-true-spatial-design-checkpoint.py | e9e1eaacfdbe98fa2cba56e67806ad67c2a01ec30cdc88c49aeb601ce3bd534a |
| polar-released40-optimized-higher-v2-065.json | 4a19f25ec1cb72de09e21d675850249cc1a1eb2a9c83473713eeaaaae942021b |
| polar-released40-optimized-higher-v2-065-full.json | a2e389726b45887a83f405761e201e57ad9644d9729cb72e2608470aa7103120 |
| 2ecf-polar-released-higher-cuff-true-spatial-design.py | 50cd560db033f31d72cbdfc31da55c3ee01c943154fc8248bd72f4947a5d8fa7 |
| polar-released40-optimized-higher-065-exit.json | b67d5093bb98b105b2ec75d891dec50c7d9b3d94cb83920376c6e1888f2a4dbb |
| polar-released40-optimized-higher-080-exit.json | 956c2d773993466ce60e5884cdf3d42011b1a7dfb57024a6e126e82166d494e4 |
| polar-released40-optimized-higher-v2-080-exit.json | d0afbfc172fa22a0dd32327435bfbbea8bba1b41384e1da6b9bd35c667f5cd6a |
| polar-released40-optimized-higher-v2-065-exit.json | 57d98568fd0741dc7f02251056c0533df339297822915179d7c43f159e6ba881 |
| polar-released40-optimized-higher-v2-065.log | ba7bc8ebe93f3d96bce111affdb7d4e31568c8caa0a1f2ca129bc540537d2137 |
| polar-released40-optimized-higher-v2-065-full-exit.json | f376bda032494451073bfe8c9a46e2c34a9c58874ff1847283191040c1381233 |
| polar-released40-optimized-higher-v2-065-full.log | 170be2d584d68e1008e1c2ec42a6f2603fb1ddc6099b83a346e9e79f358fdbfa |
