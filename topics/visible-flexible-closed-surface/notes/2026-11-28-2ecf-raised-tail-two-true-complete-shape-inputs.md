# 新长喉下的真端口 lifting 与整个位置的空间变换

**数值证据。**

准确几何见 [R273](../results/R273-raised-developed-tail-new-throat-and-ambient-diffeomorphism.md)。全新固定帽喉度量对应真实 Z=.415,η=.115。每一组都使用同一新帽、gap 23/25 和同一原源的 5292 第 2 步 W。第一组改变真实端口的 P、V、A 及角导数，以右 Hermite lifting 上移全尺寸开发盘并更换帽，在不同实际径向支撑 60% 或 100% 上完成两端两 jets；完整14个输入中选择正弯角且 G10 完整成本最小的。第二组使 R273 的空间变换作用于含原 W 的整个原位置，逐一算全六 jets；其 8 个输入取完整成本最小者。全部原 14 行及原权保留；新喉的高度 allowance 用 .113 代替旧 .0195，对应新的准确 .115 上抬量，内部开始/完成半径仍为 .52/.54。其余配置、面积、物理平滑等保持。不同新构造间收敛次数均为零。

| 实际新场构造 | 所选参数 | G10 R² | G11 metric / κ / held |
|---|---|---:|---|
| 真右端口位置差五次 lifting | [0.4, 0.56, 1.0] | 30.992437698 | 1.1112685506 / 122.00835949 / 0.69786977225 |
| R273 全空间作用于含原 W 的全位置 | [0.2, 0.56] | 53777.442157 | 11.518787929 / 89.609090183 / 0.63677779949 |

表中 lifting 参数为 [A,c,相对支撑长度]，空间变换参数为 [A,c]。向上新尾可达坐标和帽窗口在整片上已经证明。两种实际数值起点的完整 metric 和峰曲率均变差。全空间作用没有使原场的度量精度随它转移。对新场直接与新的解析开发尾比较所有六 jets，误差上界 3.7271574715447287e-13；前缀全六 jets 逐字节相同。此空间作用数值用 binary64 与32点 Gauss 求导，数学证明用真积分及准确 cuff 高度差。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-raised-tail-tall-throat-source.py" --mode select --scripts "$S" --prepared polar-new-gap-092-prepared.json --donor polar-new-gap-092-fixed-step02-step01-state.json --independent polar-new-gap-092-independent.json --output polar-gap092-raised-true-tail-select.json
python3 -u "$S/2ecf-polar-raised-tail-tall-throat-source.py" --mode observe --scripts "$S" --prepared polar-new-gap-092-prepared.json --donor polar-new-gap-092-fixed-step02-step01-state.json --independent polar-new-gap-092-independent.json --selection polar-gap092-raised-true-tail-select.json --output polar-gap092-raised-true-tail-G11.json
python3 -u "$S/2ecf-polar-raised-tail-ambient-transport.py" --mode select --scripts "$S" --prepared polar-new-gap-092-prepared.json --donor polar-new-gap-092-fixed-step02-step01-state.json --independent polar-new-gap-092-independent.json --output polar-gap092-raised-ambient-select.json
python3 -u "$S/2ecf-polar-raised-tail-ambient-transport.py" --mode observe --scripts "$S" --prepared polar-new-gap-092-prepared.json --donor polar-new-gap-092-fixed-step02-step01-state.json --independent polar-new-gap-092-independent.json --selection polar-gap092-raised-ambient-select.json --output polar-gap092-raised-ambient-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-raised-tail-tall-throat-source.py | 2c331ded22a5a952a5236a371c84a2f0a60f4c9c96e64962b0ac863bba2fe8c8 |
| 2ecf-polar-raised-tail-ambient-transport.py | 52559227facb8bcf3e957631084207464896c339324abb0bfe6676ee381b6ad3 |
| polar-gap092-raised-true-tail-select.json | 8c785abe3f9d6d66703d750bbbbe78fd2e2a46cb7db3fdafa5a3573c1d5c21ad |
| polar-gap092-raised-true-tail-G11.json | 50b293626bcadfbc3e625ec744a28351302c703ddeee9cd42c478b0465e504d8 |
| polar-gap092-raised-ambient-select.json | 6b7f3b0c6c0399dd4c2e33496208a11523bdf92ae83e91f3984dafb930b1df00 |
| polar-gap092-raised-ambient-G11.json | 429cb286bce86698b2e5fa6aacf56c4ff9a7f7d80f67ed7cf5da3d6719478b56 |
| polar-gap092-raised-true-tail-select-real-exit.json | 5fe3557bcb2e1e9b82dd38a613b1d8c488d6226496e81487001e54718f8e0edf |
| polar-gap092-raised-true-tail-select-real.log | 4eb33a811c4de01d612841a79e7a09fcef67acd097a46ea8f4da6856fa864cf8 |
| polar-gap092-raised-true-tail-G11-exit.json | 2d44bee577a22297ca6864e257bef57401982da1454ac4f1b221ad311a00fca7 |
| polar-gap092-raised-true-tail-G11.log | e61478d28de67d00c2f69b8da0228583f2fb2683b0ab6871d41c50f6392f986c |
| polar-gap092-raised-ambient-select-exit.json | f53734bd8eefecd3543ea67aa055a875721a81dda5856e000c02e769ea787df8 |
| polar-gap092-raised-ambient-select.log | 5821b0057e87464c85a66b611bd0cffc544f6d53f88bd29949326279dcfd0624 |
| polar-gap092-raised-ambient-G11-exit.json | ebc6d6735ee7d58dcd19a98e6b05d327b959c66097c15e7f14b2a16307544b7f |
| polar-gap092-raised-ambient-G11.log | 77d0bdea79494c5d3654f8302c8c9b29b8ba34323f18dc186044b0e9bb77f545 |
