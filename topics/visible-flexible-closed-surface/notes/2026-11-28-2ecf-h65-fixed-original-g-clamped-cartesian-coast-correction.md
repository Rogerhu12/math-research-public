# 固定原度量的十八个夹紧 coast 位置方向

**数值证据。**

以 H65 原度量第 1 态 A 与实际延拓 coast 的 C 为输入，在 b..b+.24 给三个笛卡尔分量各六个独立径向控制，令 W_i=h_i(C_i−A_i)。每个 h_i 在支撑两端都准确消失到二阶，保持输入端口的两 jet。每次线搜索都重新评价完整 4291840 行、原四次 metric 与全部原曲率、几何、Q2；该 18 维空间的完整实际物理导数及 H² 在支撑内直接积分。新空间自身六次接受。首个实际全目标方向导数相对误差 1.336e−6。G10 R² 从 .06773158998 降至 .067615205 左右。

| 自身步 | G11 metric / κ / held |
|---:|---|
| 0 | 0.2542957153 / 21.15640707 / 0.7059725611 |
| 1 | 0.2377572481 / 19.30127816 / 0.7059725611 |
| 2 | 0.2446703584 / 19.54557415 / 0.7059725611 |
| 3 | 0.2409747481 / 19.47508367 / 0.7059725611 |
| 4 | 0.242911334 / 19.51000056 / 0.7059725611 |
| 5 | 0.2418629997 / 19.49105502 / 0.7059725611 |
| 6 | 0.2424131187 / 19.50060736 / 0.7059725611 |

所有候选的完整闭面 reach、真实后缀连续误差仍待证明。

## 可移植重生

在运行目录 W 中执行。S 是公开课题 scripts 的绝对路径，E 是同次物理 IVP 采样产生 ramp-33.npz 与 ramp-65.npz 的目录。先按原记录产生 G10/G11 的原材料与原 5292 第 9 态。原命令只将脚本及 master 的位置换成这三个变量。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-clamped-coast-modes.py" --scripts "$S" --prepared polar-physical-H65-prepared.json --state polar-physical-H65-coarse9-step01-state.json --training-coast polar-extended-coast-training-extended-coast.json --observer-coast polar-extended-coast-observer-extended-coast.json --steps 6 --damping 0.01 --output polar-H65-clamped-coast-correction.json
python3 -u "$S/2ecf-polar-coast-alternatives-observe.py" --scripts "$S" --prepared polar-physical-H65-prepared.json --state polar-physical-H65-coarse9-step01-state.json --observer polar-physical-H65-independent.json --coast polar-extended-coast-independent-extended-coast.json --mode clamped --input polar-H65-clamped-coast-correction.json --output polar-H65-clamped-coast-correction-G11.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-clamped-coast-modes.py | d954eb46bee90ecad90b7bcd554a27486a52487e7f3c337195b6ecf8bf3b6d64 |
| polar-H65-clamped-coast-correction.json | 6de22d47d1091cf8b3f8d8e1ead740f9e279b0647d1054424fd4d61f18304652 |
| polar-H65-clamped-coast-correction-G11.json | 25645f46d7c735322a03778f0d27ae9b1d566c3b9b284fe272f6eea692082559 |
| polar-H65-clamped-coast-correction-exit.json | c8eed8542734d2ff0622dddae5639627876e0b3d47a7161b7522270d7e7bfe4b |
| polar-H65-clamped-coast-correction.log | 13b629bdf0368f601bf097268d955963258f0ed3a011b8a31bc0b23ff9953ba6 |
| polar-H65-clamped-coast-correction-G11-exit.json | ce87a71515d1a234f2941ea0235db911ca937328345ef96e25279ba3aa9b782e |
| polar-H65-clamped-coast-correction-G11.log | 01037a66589fbc2c36d4e8aed8f0735b79f26185613369c3cfdcf62e8cc75646 |
