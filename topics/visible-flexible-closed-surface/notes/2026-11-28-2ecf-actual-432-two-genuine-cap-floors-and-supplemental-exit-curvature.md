# 两副实体帽、完整平领与 432 个真实三维位置的求解

**数值证据。**

从 R294 实际升高 .065 平领场出发，以 19 span 五次开 B-spline、每坐标八个角系数取 432 个实际空间位置。在旧凸帽（R219）和真实提高的凸帽（R293）分别构造一张闭材料输入。真 Z=83/200+Δ 与 b..T 原连接目标相同，η 分别为 .53−Z、.635−Z，全喉目标和完整帽相异。原 14 行、两个实见证、两向远层法球、实际高度/宽度及额外 35×100 末带曲率导数均入各自求解，分别取 270+270 次接受。两输入各有单独目标身份。成品432系数叠于原升高后的128格 Fourier–Hermite 场上。

| 固定帽 | η | G11 误差 / κ / held | 193×272 释放尾专网 | 设计网远层最小法球比 |
|---|---:|---|---|---:|
| R219 | 0.05 | 0.2794035904 / 9.982342472 / 0.651058601 | 0.1786413939 / 10.10781191 / 0.834487744 | 0.10010626 |
| R293 | 0.155 | 0.1529865061 / 10.08711362 / 0.6536479373 | 0.1038994056 / 10.2616384 / 0.8530926946 | 0.10038137 |

对 R293 另消费全部128单元的两端和每格10个错移内点、768角。最高真实采样 κ=10.27214678，在第102格。这次观察只测局部量，完整连续项由后续 R297 单独支付。

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-released-physical-cap-roof-and-exit-curvature.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-genuine-floor-R219.json --start polar-released40-optimized-higher-v2-065.json --cap R219
python3 -u "$S/2ecf-polar-released-actual-selected-complete-cap-consumer.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-genuine-floor-R219-full.json --solution polar-released40-genuine-floor-R219.json
python3 -u "$S/2ecf-polar-released-physical-cap-roof-and-exit-curvature.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-genuine-floor-R293.json --start polar-released40-optimized-higher-v2-065.json --cap R293
python3 -u "$S/2ecf-polar-released-actual-selected-complete-cap-consumer.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-released40-genuine-floor-R293-full.json --solution polar-released40-genuine-floor-R293.json
python3 -u "$S/2ecf-polar-released-actual-cell-curvature-search.py" --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-gap092-raised-ridge-rays.json --donor polar-gap092-material-implicit-frozen11.json --donor-field polar-gap092-material-implicit-frozen11.npz --frozen polar-gap092-material-implicit-radius11.json --state polar-released-cut-flat40-enriched.json --field polar-released-cut-flat40-enriched.npz --output polar-R293-432-true-every-cell-curvature.json --spatial polar-released40-genuine-floor-R293.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-released-physical-cap-roof-and-exit-curvature.py | 8a665f1869909b2f4885d351ff086e357b2dce19f0d761699fd728a98f918ff6 |
| 2ecf-polar-released-actual-selected-complete-cap-consumer.py | 21daca2c9858875fd33a7b75e0d6eb41633ca5ce28f3a860992583c804bb5cda |
| 2ecf-polar-released-actual-cell-curvature-search.py | 4b37c578c5a5b95c6220c4cac8335fa10de13115b55320b4e0efe7c1dc36100b |
| 2ecf-polar-released-material-physical-two-clock-design.py | 7061ce0fea2e46e59a3c7336208da0710d87aac2f04857dfa33465cc8a4c7d05 |
| polar-released40-genuine-floor-R219.json | 442521806f76817e9fcdfa0e8b795c7e8d89bbfa70a2c86122878053741bcffe |
| polar-released40-genuine-floor-R219-full.json | 2f5df6321f64de582adf96880cf835a8f4549a8da49a589d9b21072ff397bf71 |
| polar-released40-genuine-floor-R293.json | e66355e8fdccd0222e4e1ea7de1a901bd2b2709eb4266c113258cee46811bb0d |
| polar-released40-genuine-floor-R293-full.json | 34ec8b65d3cf877b6939bbfa28f0c6469e3fd6dfff315643cd543c7c2dd99463 |
| polar-R293-432-true-every-cell-curvature.json | 8020e37889afa9195ab5658d8547c1e148927dd4cf39064440c3a0c448be2498 |
| polar-released40-genuine-floor-R219-exit.json | 6f6779ad88951c63d108be2810a16c837e4ecd778e36b37e22528cd96171f0da |
| polar-released40-genuine-floor-R219.log | 986c25e538b1e6b2d164f2ab3a6f9e74f0b765ea6d07b99566a075d1c28f2fe7 |
| polar-released40-genuine-floor-R219-full-exit.json | 9cd5e189e7e04eb63838e676748bad5e41aeb967ed413b917358f75961c59fbc |
| polar-released40-genuine-floor-R219-full.log | 6d22e334e50f9181b0d107281992aae0f466f59e80b020d0721aba4bd750ccae |
| polar-released40-genuine-floor-R293-exit.json | 28527f612051492ca4ab43160aa60a56568c43705ab29c91ee96a12dbef7c30c |
| polar-released40-genuine-floor-R293.log | 78ad0a00554e635950e80466602e96f2cc33f24daa02aff61e725e06a0c2cce3 |
| polar-released40-genuine-floor-R293-full-exit.json | 44020e6b0d43e98979204be7bf140b74f42052121a9f1b1e0d57155517d40564 |
| polar-released40-genuine-floor-R293-full.log | 44c1451bfaf61bb101ee951925d73171afeab6f19781d8233f2abd9a3a49324c |
| polar-R293-432-true-every-cell-curvature-exit.json | 6ada81875283a4420b6af7d9fecb44e2b71c320873089cc00334d270854c9528 |
| polar-R293-432-true-every-cell-curvature.log | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
