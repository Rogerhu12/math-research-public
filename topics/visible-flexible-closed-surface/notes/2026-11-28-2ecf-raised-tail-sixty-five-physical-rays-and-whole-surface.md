# 65 条规定速率的真实极径线与四张完整 Cartesian 曲面

**数值证据。**

沿 R267 与 R273 真端口取一个全象限 65 个空间极角。在每条射线的半径–高度平面中，用正速率三次 Hermite 插值端点速度及其导数，端切向角与其径导数同样由物理 PVA 确定。另加 12 格三次 B 样条去掉两端各两个系数作为内部转角自由度。积分 v(cosθ,sinθ) 的两分量须接到真实末位置，SLSQP 带真实射线曲率损失。参考[新 S 两条轴曲线的端角方法](../scripts/2ecf-strong-axial-curve-physical-design.py)，这里使用不同的原 S、gap 23/25、上弯新真端口以及全象限每条实际射线自己的端速率。独立 4097 点 Simpson 积分后残余向量乘 S5(t) 修补末位置，保留端速度和加速度。后两项另在每条真实径线中惩罚 held、宽度、球包和上下高度超窗。
用 DCT-I 将 65 个径向节点的 [logρ,z] 及前两物理径导写成完整 0,2,…,128 偶角频率，在内节点取存储 dyadic 系数，径向用五次 Hermite；两端取准确 Γ95 或真实开发尾的完整极角函数迹。将整个表面接上原两端物理角钟，再用全链法则求六个 Cartesian jets。有限实现用 2048 角端函数周期插值，与两端真实数值入口独立比对，所有网格六分量最大误差 <5.3e−9；精确定义仍采用原端口函数。四张完整表面均计算 4291840 G10 行和独立 G11。

| 真实端 A / c | 径线解 | 65 射线最大 κ | 完整面 G11 metric / κ / held |
|---|---|---:|---|
| 0.4 / 0.56 | 同向转角 | 11.9830799 | 0.84211817215 / 14.076742402 / 0.5740429658 |
| 0.4 / 0.56 | 反向一周 | 52.7693511 | 306.38359817 / 41883.433329 / 0.7522527599 |
| 0.4 / 0.56 | 同向含几何窗 | 14.4059047 | 2.8736975758 / 27.580618866 / 0.61818722257 |
| 0.85 / 0.52 | 高短轴端含几何窗 | 16.9732043 | 1.4883593822 / 16.95694121 / 0.64932398853 |

第一组 65 条实际射线的速度在 .999999998 至 1.00881692 之间，整面 metric 为 .84211817。第四组短轴端进一步上抬后，G11 held .64932399，κ16.95694。每个初图的优化接受数为零，完整曲面的连续同 g 和 reach 仍待另证。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-raised-all-physical-ray-design.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --winding 0 --field polar-gap092-raised-rays-positive.npz --output polar-gap092-raised-rays-positive.json
python3 -u "$S/2ecf-polar-raised-physical-ray-field-observe.py" --scripts "$S" --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --field polar-gap092-raised-rays-positive.npz --design polar-gap092-raised-rays-positive.json --output polar-gap092-raised-rays-positive-full.json
python3 -u "$S/2ecf-polar-raised-all-physical-ray-design.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --winding -1 --field polar-gap092-raised-rays-negative.npz --output polar-gap092-raised-rays-negative.json
python3 -u "$S/2ecf-polar-raised-physical-ray-field-observe.py" --scripts "$S" --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --field polar-gap092-raised-rays-negative.npz --design polar-gap092-raised-rays-negative.json --output polar-gap092-raised-rays-negative-full.json
python3 -u "$S/2ecf-polar-raised-all-ray-geometric-design.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --winding 0 --field polar-gap092-raised-rays-geometric.npz --output polar-gap092-raised-rays-geometric.json
python3 -u "$S/2ecf-polar-raised-physical-ray-field-observe.py" --scripts "$S" --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --field polar-gap092-raised-rays-geometric.npz --design polar-gap092-raised-rays-geometric.json --output polar-gap092-raised-rays-geometric-full.json
python3 -u "$S/2ecf-polar-raised-all-ray-geometric-design.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --winding 0 --amplitude .85 --flat .52 --geometry-weight 200000 --field polar-gap092-raised-ridge-rays.npz --output polar-gap092-raised-ridge-rays.json
python3 -u "$S/2ecf-polar-raised-physical-ray-field-observe.py" --scripts "$S" --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --field polar-gap092-raised-ridge-rays.npz --design polar-gap092-raised-ridge-rays.json --output polar-gap092-raised-ridge-full.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-raised-all-physical-ray-design.py | 89559745f6696d113bbaeb9aa038250b09e38c18b81da73164288c6b99cd93dd |
| 2ecf-polar-raised-all-ray-geometric-design.py | 0c975e06a89598cd1f8ae7c212643607a347830f803b665355b878638977dc32 |
| 2ecf-polar-raised-physical-ray-field-observe.py | 1428648f963b3d0ef5674d9de166fbef8ce7b73ee9f9d888ce8bf1d3f0dabefe |
| polar-gap092-raised-rays-positive.json | 0c1c16a21d777c0a214c44aa107ae98562dc63300d3b90c675399817bd13fb7c |
| polar-gap092-raised-rays-positive.npz | f2016e5194785ac2d79cd527a6d9f40b228352deb2566dc0d4f33e5a040865da |
| polar-gap092-raised-rays-positive-full.json | e1e655332beee58447df9a0d084c7ed9d1ca80b3f0126b1cfa03cc2f9dc966a4 |
| polar-gap092-raised-rays-negative.json | 5cd04ee685cbff17ab389d1101a4993a607e850aaa730359f7df756098322802 |
| polar-gap092-raised-rays-negative.npz | 66194301607536438004c6731dcc596dd6324c09717a7f26e25630cd0d4c2c6f |
| polar-gap092-raised-rays-negative-full.json | bcdc9c8c9ba8d04c8ce6004d541b9901d333fef2decce496a3d851978bea50fc |
| polar-gap092-raised-rays-geometric.json | e3d2b44c39b35f3867fe8b8492a3f024de6d0033711b5814ccb58e9ad2bd77b0 |
| polar-gap092-raised-rays-geometric.npz | 0d81851bf8fb05782b09113e793e11addb4b562322861551f6e825c20610cb90 |
| polar-gap092-raised-rays-geometric-full.json | 0583fd452cdd94fd19fb46df20102f0728152d9449f7e0bb9bda4322660b92c2 |
| polar-gap092-raised-ridge-rays.json | 0a51efac146222c210b610d34fa9e457d2c40f0a75283b48554d1fc4b3367059 |
| polar-gap092-raised-ridge-rays.npz | 10b836b7027bc2f7cc7cebfd456403217d5e1197a704ebfba2ca62ae8d3a08d1 |
| polar-gap092-raised-ridge-full.json | 792301c8a024956c80fe81c97457a69d2588530a48c14dc7debafa00a4c93f73 |
| polar-gap092-raised-all-rays-positive-exit.json | e98f1ac3ec94c202193ba46dd7c411d1642c64f55db961c44520d44624a1f43e |
| polar-gap092-raised-all-rays-positive.log | d958bb94c7059ab17c905773ad6899084c35ec9ed70347702f30c63dab0adb3c |
| polar-gap092-raised-rays-positive-full-exit.json | 2805657319e18de1e1a81f73fb5c52b20a36596c63e8af72f9fad37ddd288d37 |
| polar-gap092-raised-rays-positive-full.log | d041f0e574fd189ffef1ce31e5e82a29afb05bdc911c7b324a5defc1b0279354 |
| polar-gap092-raised-all-rays-negative-exit.json | abb126e46f1200b24c5271ac99d5844a37eddb37bfe06541c5e1bcf443a5a777 |
| polar-gap092-raised-all-rays-negative.log | 8fb1440c29b0d452cbfe7416ebdb7e25f30d49cd4ae139373f48a60cb04b62f5 |
| polar-gap092-raised-rays-negative-full-exit.json | 8dd356b072f67d31b3801b2b05c4359e5aba5caaba04e058bc77e7ee4ae5f9a4 |
| polar-gap092-raised-rays-negative-full.log | 7b5bc7b7b1d464356cd162dd8e7f36607cfa3eb5f2f81ff1ccc137564e481237 |
| polar-gap092-raised-all-rays-geometric-exit.json | 4dc54059cfad295917b305a169a1ba09b968275de3401a2232fae115e80e7b2a |
| polar-gap092-raised-all-rays-geometric.log | c87890871762069c06d37daeaa681863b9ad43ffd0e8a9b1f1ca7c99844fb1e5 |
| polar-gap092-raised-rays-geometric-full-exit.json | 68b1dd152876486841aa12f9c95331568fc74b4cdb26bf73adca483955c1cc51 |
| polar-gap092-raised-rays-geometric-full.log | fb087ece1fc68e0bd139fdd8fc7d6c6d40b7cf1ccd615cc1a83ca7362b4c66a7 |
| polar-gap092-raised-ridge-all-rays-exit.json | 45ad6008b3b8e2805ff0eb2d148d16e420cacf712f1d26db02b2c6ef22497c38 |
| polar-gap092-raised-ridge-all-rays.log | b1d9e0deedfe096c0b1f7d9c36b0b0595be0e981ad7f5192aecb62a895723e30 |
| polar-gap092-raised-ridge-full-exit.json | 069dbfa2c18aed19f518a9f6aa9db9fd59e6aa39ac436d3b2d1009d670af306f |
| polar-gap092-raised-ridge-full.log | b16d475b513ee0f9df3b88afc4f2b766a91817a6bfc6344da138cb5ec98ad64c |
