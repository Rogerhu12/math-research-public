# 真实校正场侧向经线的高度转向与空间长度

**数值证据。**

在真实 G10 两网格的 u=π/2 上，直接以每个状态的坐标系数求原完整 b..S 六 jet。折线取全部 656 个实际材料半径。所有状态的 x 偏差小于 1.1e−13。近点为 s=.8152879230，表中切向校正取原底场的固定极角方向 w=∂s−(Θ_s/Θ_u)∂u 上的 |dW(w)|。相邻的准确 R266 见证在 s≈.815615，原 native 侧角与上述材料路径也有极小偏移。以下均为这条实际采样材料经线的数值。

| 实际场 | 分段 TVρ | 分段 TVz | 空间折线长 | 近点切向校正模 |
|---|---:|---:|---:|---:|
| source | 0.4469893697 | 0.1469133061 | 0.5126693312 | 0 |
| 原g | 0.4303572303 | 0.5728859496 | 0.7992723393 | 0.8126214804 |
| 设计 01 | 0.4405393497 | 0.5683339206 | 0.8005430466 | 0.8079436547 |
| 设计 02 | 0.4607998746 | 0.5603052642 | 0.8050348018 | 0.8090041593 |
| 设计 03 | 0.4649494474 | 0.5528217244 | 0.8005154567 | 0.7859833097 |
| 设计 04 | 0.4780358541 | 0.54509291 | 0.7996806022 | 0.7809066767 |
| 设计 05 | 0.491251108 | 0.5404496889 | 0.8006132393 | 0.7768556312 |
| 设计 06 | 0.5046462521 | 0.5306247569 | 0.7981730948 | 0.7746723021 |
| 固定设计3，六次步 01 | 0.4800305109 | 0.5460785928 | 0.8007755813 | 0.7857126968 |

材料区间长约 .79567395；原场在这些节点高度单调至舍入，而各校正场明显有下降与再上升。真实 XYZ 已经通过高度转向增加侧向经线长度。折线变差本身只给出采样量，不充作连续 TV 上界，亦无法从单条路径推全域等距。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-side-meridian-actual-corrections.py" --scripts "$S" --prepared polar-physical-H65-prepared.json --states polar-physical-H65-coarse9-step01-state.json polar-H65-two-space-design-step01-step01-state.json polar-H65-two-space-design-step02-step01-state.json polar-H65-two-space-design-step03-step01-state.json polar-H65-two-space-design-step04-step01-state.json polar-H65-two-space-design-step05-step01-state.json polar-H65-two-space-design-step06-step01-state.json polar-H65-frozen-design3-sextic-step01-step01-state.json --output polar-H65-side-meridian-v1.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-side-meridian-actual-corrections.py | 171287100c59445f0e4aaf2a4b099782c7dd90a9ca3c6f60e64dbb1056b14a71 |
| polar-H65-side-meridian-v1.json | 252648a2a92af0ae817d881718409d95531e18deb4d67bed9e564ff78df36694 |
| polar-H65-side-meridian-v1-exit.json | 770ea3d7ccdf8a6be8b4de6f58cc78507608a4cfc876306dc0356ac977104b39 |
| polar-H65-side-meridian-v1.log | 5bbb0f373d05d52401cb122ca1c2d0895cd8d18a945bc06fe2e79674bab26467 |
